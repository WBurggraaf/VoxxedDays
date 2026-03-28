from __future__ import annotations

import argparse
import json
import os
import shlex
import subprocess
import sys
from collections import Counter
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Iterable

FRAME_HEIGHT = 18
SVG_WIDTH = 1600
MIN_TEXT_WIDTH = 36


@dataclass
class CommandResult:
    command_id: str
    command: list[str]
    recording_path: Path
    log_path: Path
    return_code: int
    duration_seconds: float
    iteration: int


class FlameNode:
    def __init__(self, name: str) -> None:
        self.name = name
        self.value = 0
        self.children: dict[str, FlameNode] = {}


def load_config(config_path: Path) -> dict:
    return json.loads(config_path.read_text(encoding="utf-8"))


def slugify(text: str) -> str:
    return text.lower().replace("/", "-").replace(" ", "-").replace("_", "-")


def timestamp_utc() -> str:
    return datetime.now(UTC).isoformat()


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def build_maven_command(command_cfg: dict, recording_path: Path, stack_depth: int, maven_repo_local: Path) -> list[str]:
    executable = "mvn.cmd" if os.name == "nt" else "mvn"
    jfr_arg = f"-XX:StartFlightRecording=filename={recording_path},dumponexit=true,settings=profile"
    stack_arg = f"-XX:FlightRecorderOptions=stackdepth={stack_depth}"
    arg_line = f"{jfr_arg} {stack_arg}"

    command = [executable, "-B", f"-Dmaven.repo.local={maven_repo_local}"]
    projects = command_cfg.get("projects", [])
    if projects:
        command.extend(["-pl", ",".join(projects), "-am"])
    command.extend(command_cfg.get("extra_args", []))
    command.extend(
        [
            f"-D{command_cfg.get('test_property', 'test')}={','.join(command_cfg['tests'])}",
            "-Dsurefire.failIfNoSpecifiedTests=false",
            "-DfailIfNoTests=false",
            "-DforkCount=1",
            "-DreuseForks=false",
            f"-DargLine={arg_line}",
            command_cfg.get("goal", "test"),
        ]
    )
    return command


def build_gradle_command(command_cfg: dict, recording_path: Path, stack_depth: int, init_script_path: Path, gradle_user_home: Path) -> list[str]:
    executable = ["cmd", "/c", "gradlew.bat"] if os.name == "nt" else ["./gradlew"]
    jvm_args = "||".join(
        [
            f"-XX:StartFlightRecording=filename={recording_path},dumponexit=true,settings=profile",
            f"-XX:FlightRecorderOptions=stackdepth={stack_depth}",
        ]
    )
    command = [
        *executable,
        "--no-daemon",
        "--gradle-user-home",
        str(gradle_user_home),
        "--init-script",
        str(init_script_path),
        f"-PflamegraphJvmArgs={jvm_args}",
        command_cfg.get("task", "test"),
    ]
    for test_name in command_cfg["tests"]:
        command.extend(["--tests", test_name])
    return command


def run_command(command: list[str], workdir: Path, log_path: Path, dry_run: bool) -> tuple[int, float]:
    if dry_run:
        log_path.write_text("DRY RUN\n" + " ".join(shlex.quote(part) for part in command) + "\n", encoding="utf-8")
        return 0, 0.0

    started = datetime.now()
    process = subprocess.run(
        command,
        cwd=workdir,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        errors="replace",
        shell=False,
    )
    finished = datetime.now()
    log_path.write_text(process.stdout, encoding="utf-8")
    duration = (finished - started).total_seconds()
    return process.returncode, duration


def parse_jfr_samples(jfr_path: Path) -> Counter[str]:
    command = [
        "jfr",
        "print",
        "--json",
        "--events",
        "jdk.ExecutionSample",
        "--stack-depth",
        "256",
        str(jfr_path),
    ]
    result = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="replace",
        shell=False,
        check=True,
    )
    payload = json.loads(result.stdout or "{}")
    folded = Counter()

    events = payload.get("recording", {}).get("events", [])
    for event in events:
        values = event.get("values", {})
        stack_trace = values.get("stackTrace") or {}
        frames = stack_trace.get("frames") or []
        frame_names: list[str] = []
        for frame in reversed(frames):
            method = frame.get("method") or {}
            owner = method.get("type", {}).get("name", "unknown").replace("/", ".")
            name = method.get("name", "unknown")
            frame_names.append(f"{owner}.{name}")
        if frame_names:
            folded[";".join(frame_names)] += 1
    return folded


def write_folded(path: Path, folded: Counter[str]) -> None:
    lines = [f"{stack} {count}" for stack, count in folded.most_common()]
    path.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")


def escape_xml(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def color_for(name: str) -> str:
    value = sum((index + 1) * ord(ch) for index, ch in enumerate(name))
    hue = value % 360
    return f"hsl({hue},65%,70%)"


def build_tree(folded: Counter[str]) -> FlameNode:
    root = FlameNode("root")
    for stack, count in folded.items():
        node = root
        node.value += count
        for part in stack.split(";"):
            node = node.children.setdefault(part, FlameNode(part))
            node.value += count
    return root


def tree_depth(node: FlameNode, depth: int = 0) -> int:
    if not node.children:
        return depth
    return max(tree_depth(child, depth + 1) for child in node.children.values())


def render_svg(title: str, folded: Counter[str], output_path: Path, subtitle: str | None = None) -> None:
    if not folded:
        message = subtitle or "No JFR execution samples captured"
        output_path.write_text(
            "<svg xmlns='http://www.w3.org/2000/svg' width='800' height='120'>"
            "<text x='20' y='40' font-family='Verdana' font-size='20'>No JFR execution samples captured</text>"
            f"<text x='20' y='68' font-family='Verdana' font-size='12'>{escape_xml(message)}</text>"
            "</svg>",
            encoding="utf-8",
        )
        return

    root = build_tree(folded)
    max_depth = tree_depth(root)
    meta_rows = 2 if subtitle else 1
    height = (max_depth + 3 + meta_rows) * FRAME_HEIGHT
    width_per_sample = SVG_WIDTH / max(root.value, 1)
    meta_y = 40
    parts = [
        f"<svg xmlns='http://www.w3.org/2000/svg' width='{SVG_WIDTH}' height='{height}'>",
        "<style>",
        "text { font-family: Verdana, sans-serif; font-size: 12px; fill: #1f2937; }",
        ".title { font-size: 18px; font-weight: bold; }",
        ".meta { font-size: 11px; fill: #4b5563; }",
        "</style>",
        f"<text class='title' x='12' y='22'>{escape_xml(title)}</text>",
        f"<text class='meta' x='12' y='{meta_y}'>Total samples: {root.value}</text>",
    ]
    if subtitle:
        meta_y += 16
        parts.append(f"<text class='meta' x='12' y='{meta_y}'>{escape_xml(subtitle)}</text>")

    def visit(node: FlameNode, depth: int, x: float) -> float:
        current_x = x
        sorted_children = sorted(node.children.values(), key=lambda child: (-child.value, child.name))
        for child in sorted_children:
            width = child.value * width_per_sample
            y = height - ((depth + 2) * FRAME_HEIGHT)
            rect_x = current_x
            label = child.name
            parts.append(
                f"<g><title>{escape_xml(label)} ({child.value} samples)</title><rect x='{rect_x:.2f}' y='{y:.2f}' width='{width:.2f}' height='{FRAME_HEIGHT - 1}' fill='{color_for(label)}' stroke='#ffffff' stroke-width='0.5'/></g>"
            )
            if width >= MIN_TEXT_WIDTH:
                approx_chars = max(int((width - 6) / 7), 0)
                visible = label if len(label) <= approx_chars else label[: max(approx_chars - 1, 0)] + "..."
                parts.append(f"<text x='{rect_x + 3:.2f}' y='{y + 13:.2f}'>{escape_xml(visible)}</text>")
            visit(child, depth + 1, current_x)
            current_x += width
        return current_x

    visit(root, 0, 0.0)
    parts.append("</svg>")
    output_path.write_text("\n".join(parts), encoding="utf-8")


def write_repo_index(output_root: Path, repo_summaries: list[dict]) -> None:
    lines = [
        "<!DOCTYPE html>",
        "<html lang='en'><head><meta charset='utf-8'/>",
        "<title>Flamegraph Index</title>",
        "<style>body{font-family:Verdana,sans-serif;margin:24px;background:#f8fafc;color:#0f172a}table{border-collapse:collapse;width:100%}th,td{padding:10px;border-bottom:1px solid #cbd5e1;text-align:left}a{color:#0f766e;text-decoration:none}</style></head><body>",
        "<h1>Library Flamegraphs</h1>",
        "<table><thead><tr><th>Repository</th><th>Samples</th><th>Status</th><th>Artifacts</th></tr></thead><tbody>",
    ]
    for summary in repo_summaries:
        repo_id = summary["repo_id"]
        artifact_links = []
        if summary.get("svg"):
            artifact_links.append(f"<a href='{repo_id}/{Path(summary['svg']).name}'>svg</a>")
        if summary.get("folded"):
            artifact_links.append(f"<a href='{repo_id}/{Path(summary['folded']).name}'>folded</a>")
        if summary.get("meta"):
            artifact_links.append(f"<a href='{repo_id}/{Path(summary['meta']).name}'>meta</a>")
        lines.append(
            "<tr>"
            f"<td>{escape_xml(summary['display_name'])}</td>"
            f"<td>{summary.get('samples', 0)}</td>"
            f"<td>{escape_xml(summary.get('status', 'unknown'))}</td>"
            f"<td>{' | '.join(artifact_links)}</td>"
            "</tr>"
        )
    lines.extend(["</tbody></table></body></html>"])
    (output_root / "index.html").write_text("\n".join(lines), encoding="utf-8")


def iter_selected_repos(config: dict, selected: set[str] | None) -> Iterable[dict]:
    for repo in config["repos"]:
        if selected is None or repo["id"] in selected:
            yield repo


def filter_folded(folded: Counter[str], focus_terms: list[str]) -> Counter[str]:
    lowered = [term.lower() for term in focus_terms]
    scoped = Counter()
    for stack, count in folded.items():
        haystack = stack.lower()
        if any(term in haystack for term in lowered):
            scoped[stack] = count
    return scoped


def command_artifact_stem(index: int, command_id: str) -> str:
    return f"{index:02d}-{slugify(command_id)}"


def main() -> int:
    parser = argparse.ArgumentParser(description="Run repeatable library test profiles and render flamegraphs.")
    parser.add_argument("--repos", help="Comma-separated repo ids from flamegraph/repos.json")
    parser.add_argument("--config", default="flamegraph/repos.json", help="Path to the repo manifest")
    parser.add_argument("--output-root", default="flamegraph/output", help="Output directory")
    parser.add_argument("--dry-run", action="store_true", help="Write commands without executing them")
    parser.add_argument("--continue-on-error", action="store_true", help="Continue even if one repo fails")
    args = parser.parse_args()

    workspace = Path(__file__).resolve().parents[1]
    config_path = (workspace / args.config).resolve()
    output_root = (workspace / args.output_root).resolve()
    ensure_dir(output_root)

    config = load_config(config_path)
    selected = {entry.strip() for entry in args.repos.split(",")} if args.repos else None
    stack_depth = int(config.get("recording", {}).get("stack_depth", 128))
    init_script_path = workspace / "flamegraph" / "gradle-test-jfr.init.gradle"
    gradle_user_home = workspace / "flamegraph" / ".gradle-user-home"
    ensure_dir(gradle_user_home)
    maven_repo_local = workspace / "flamegraph" / ".m2" / "repository"
    ensure_dir(maven_repo_local)

    repo_summaries: list[dict] = []
    overall_failures = 0

    for repo in iter_selected_repos(config, selected):
        repo_root = workspace / repo["repo_path"]
        repo_output = output_root / repo["id"]
        ensure_dir(repo_output)
        results: list[CommandResult] = []
        aggregate_folded = Counter()
        command_metadata: list[dict] = []
        print(f"[run] {repo['display_name']}")

        try:
            for index, command_cfg in enumerate(repo["commands"], start=1):
                iterations = int(command_cfg.get("iterations", 1))
                per_command_results: list[CommandResult] = []
                command_folded = Counter()
                stem = command_artifact_stem(index, command_cfg["id"])

                for iteration in range(1, iterations + 1):
                    suffix = f"-run{iteration:02d}" if iterations > 1 else ""
                    recording_path = repo_output / f"{stem}{suffix}.jfr"
                    log_path = repo_output / f"{stem}{suffix}.log"
                    if repo["build_tool"] == "maven":
                        command = build_maven_command(command_cfg, recording_path, stack_depth, maven_repo_local)
                    elif repo["build_tool"] == "gradle":
                        command = build_gradle_command(command_cfg, recording_path, stack_depth, init_script_path, gradle_user_home)
                    else:
                        raise ValueError(f"Unsupported build tool: {repo['build_tool']}")

                    return_code, duration = run_command(command, repo_root, log_path, args.dry_run)
                    result = CommandResult(
                        command_id=command_cfg["id"],
                        command=command,
                        recording_path=recording_path,
                        log_path=log_path,
                        return_code=return_code,
                        duration_seconds=duration,
                        iteration=iteration,
                    )
                    results.append(result)
                    per_command_results.append(result)
                    if return_code != 0:
                        raise RuntimeError(f"Command failed for {repo['id']}: {command_cfg['id']} iteration {iteration} (exit {return_code})")

                    if not args.dry_run and recording_path.exists():
                        parsed = parse_jfr_samples(recording_path)
                        command_folded.update(parsed)
                        aggregate_folded.update(parsed)

                command_folded_path = repo_output / f"{stem}.folded.txt"
                command_svg_path = repo_output / f"{stem}.svg"
                write_folded(command_folded_path, command_folded)
                render_svg(
                    f"{repo['display_name']} / {command_cfg['id']}",
                    command_folded,
                    command_svg_path,
                    subtitle=f"tests={', '.join(command_cfg['tests'])} | iterations={iterations}",
                )

                proofs_meta: list[dict] = []
                for proof_cfg in command_cfg.get("proofs", []):
                    proof_folded = filter_folded(command_folded, proof_cfg["focus_terms"])
                    proof_stem = f"{stem}-{slugify(proof_cfg['id'])}"
                    proof_folded_path = repo_output / f"{proof_stem}.folded.txt"
                    proof_svg_path = repo_output / f"{proof_stem}.svg"
                    write_folded(proof_folded_path, proof_folded)
                    render_svg(
                        f"{repo['display_name']} / {proof_cfg['title']}",
                        proof_folded,
                        proof_svg_path,
                        subtitle=f"focus={', '.join(proof_cfg['focus_terms'])}",
                    )
                    proofs_meta.append(
                        {
                            "id": proof_cfg["id"],
                            "title": proof_cfg["title"],
                            "focus_terms": proof_cfg["focus_terms"],
                            "samples": sum(proof_folded.values()),
                            "svg": str(proof_svg_path),
                            "folded": str(proof_folded_path),
                        }
                    )

                command_metadata.append(
                    {
                        "id": command_cfg["id"],
                        "tests": command_cfg["tests"],
                        "iterations": iterations,
                        "samples": sum(command_folded.values()),
                        "svg": str(command_svg_path),
                        "folded": str(command_folded_path),
                        "proofs": proofs_meta,
                        "runs": [
                            {
                                "iteration": result.iteration,
                                "command": result.command,
                                "recording_path": str(result.recording_path),
                                "log_path": str(result.log_path),
                                "return_code": result.return_code,
                                "duration_seconds": result.duration_seconds,
                            }
                            for result in per_command_results
                        ],
                    }
                )

            folded_path = repo_output / f"{repo['id']}.folded.txt"
            svg_path = repo_output / f"{repo['id']}.svg"
            meta_path = repo_output / f"{repo['id']}.meta.json"

            write_folded(folded_path, aggregate_folded)
            render_svg(repo["display_name"], aggregate_folded, svg_path)
            metadata = {
                "repo_id": repo["id"],
                "display_name": repo["display_name"],
                "repo_path": str(repo_root),
                "generated_at": timestamp_utc(),
                "status": "dry-run" if args.dry_run else "ok",
                "samples": sum(aggregate_folded.values()),
                "commands": command_metadata,
            }
            meta_path.write_text(json.dumps(metadata, indent=2), encoding="utf-8")
            repo_summaries.append(
                {
                    "repo_id": repo["id"],
                    "display_name": repo["display_name"],
                    "status": metadata["status"],
                    "samples": metadata["samples"],
                    "svg": str(svg_path),
                    "folded": str(folded_path),
                    "meta": str(meta_path),
                }
            )
        except Exception as exc:
            overall_failures += 1
            meta_path = repo_output / f"{repo['id']}.meta.json"
            metadata = {
                "repo_id": repo["id"],
                "display_name": repo["display_name"],
                "repo_path": str(repo_root),
                "generated_at": timestamp_utc(),
                "status": "failed",
                "error": str(exc),
                "commands": command_metadata,
            }
            meta_path.write_text(json.dumps(metadata, indent=2), encoding="utf-8")
            repo_summaries.append(
                {
                    "repo_id": repo["id"],
                    "display_name": repo["display_name"],
                    "status": "failed",
                    "samples": 0,
                    "meta": str(meta_path),
                }
            )
            if not args.continue_on_error:
                write_repo_index(output_root, repo_summaries)
                print(str(exc), file=sys.stderr)
                return 1

    write_repo_index(output_root, repo_summaries)
    return 1 if overall_failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
