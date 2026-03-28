from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from pathlib import Path
from textwrap import dedent

import run_flamegraphs as harness

WORKSPACE = Path(__file__).resolve().parents[1]
PAIR_ROOT = WORKSPACE / "flamegraph" / "pairs"
OUTPUT_ROOT = WORKSPACE / "flamegraph" / "output_pairs"
M2_ROOT = WORKSPACE / "flamegraph" / ".m2" / "repository"
STACK_DEPTH = 128


def json_object_test() -> str:
    return dedent("""
        package org.json.junit;

        import static org.junit.Assert.assertTrue;

        import org.json.JSONArray;
        import org.json.JSONObject;
        import org.junit.Test;

        public class JSONObjectProofProfileTest {
            @Test
            public void profileToStringPath() {
                JSONObject template = new JSONObject();
                for (int i = 0; i < 48; i++) {
                    JSONArray nested = new JSONArray();
                    for (int j = 0; j < 12; j++) {
                        nested.put("value-" + i + '-' + j);
                    }
                    template.put("key" + i, nested);
                }
                long total = 0L;
                for (int round = 0; round < 4000; round++) {
                    String json = template.toString(2);
                    total += json.length();
                }
                assertTrue(total > 0L);
            }
        }
    """).strip() + "\n"


def json_xml_test() -> str:
    return dedent("""
        package org.json.junit;

        import static org.junit.Assert.assertTrue;

        import org.json.JSONObject;
        import org.json.XML;
        import org.junit.Test;

        public class XMLProofProfileTest {
            @Test
            public void profileStringToValuePath() {
                String xml = "<root>"
                        + "<item enabled='true' count='42' ratio='12.50'>12345</item>"
                        + "<item enabled='false' count='7' ratio='2.75'>67890</item>"
                        + "<item enabled='true' count='19' ratio='4.25'>24680</item>"
                        + "</root>";
                long total = 0L;
                for (int i = 0; i < 5000; i++) {
                    JSONObject object = XML.toJSONObject(xml);
                    total += object.toString().length();
                }
                assertTrue(total > 0L);
            }
        }
    """).strip() + "\n"


def jackson_readstring_test() -> str:
    return dedent("""
        package tools.jackson.core.unittest.read;

        import static org.junit.jupiter.api.Assertions.assertTrue;

        import java.io.StringWriter;
        import java.io.Writer;

        import org.junit.jupiter.api.Test;

        import tools.jackson.core.JsonParser;
        import tools.jackson.core.JsonToken;
        import tools.jackson.core.json.JsonFactory;

        class ReadStringProofProfileTest {
            private static final JsonFactory JSON_FACTORY = new JsonFactory();

            @Test
            void profileReadStringPath() throws Exception {
                String payload = makePayload();
                long total = 0L;
                for (int i = 0; i < 1200; i++) {
                    try (JsonParser parser = JSON_FACTORY.createParser(payload)) {
                        parser.nextToken();
                        parser.nextToken();
                        Writer writer = new StringWriter();
                        total += parser.readString(writer);
                        if (parser.currentToken() == JsonToken.VALUE_STRING) {
                            parser.finishToken();
                        }
                    }
                }
                assertTrue(total > 0L);
            }

            private static String makePayload() {
                StringBuilder sb = new StringBuilder(14000);
                sb.append('[').append('"');
                for (int i = 0; i < 6000; i++) {
                    sb.append((char) ('a' + (i % 26)));
                }
                sb.append('"').append(']');
                return sb.toString();
            }
        }
    """).strip() + "\n"



def jackson_textbuffer_test() -> str:
    return dedent("""
        package tools.jackson.core.unittest.util;

        import static org.junit.jupiter.api.Assertions.assertTrue;

        import java.nio.charset.StandardCharsets;

        import org.junit.jupiter.api.Test;

        import tools.jackson.core.util.TextBuffer;

        class TextBufferProofProfileTest {
            @Test
            void profileResetWithUtf8() throws Exception {
                byte[] bytes = makePayload().getBytes(StandardCharsets.UTF_8);
                TextBuffer buffer = new TextBuffer(null);
                long total = 0L;
                for (int i = 0; i < 20000; i++) {
                    buffer.resetWithUTF8(bytes, 0, bytes.length);
                    total += buffer.contentsAsString().length();
                }
                assertTrue(total > 0L);
            }

            private static String makePayload() {
                StringBuilder sb = new StringBuilder(128);
                for (int i = 0; i < 48; i++) {
                    sb.append((char) ('a' + (i % 26)));
                }
                return sb.toString();
            }
        }
    """).strip() + "\n"


def log4j_copy_test() -> str:
    return dedent("""
        package org.apache.logging.log4j.spi;

        import static org.junit.jupiter.api.Assertions.assertEquals;

        import java.util.Map;

        import org.junit.jupiter.api.Test;

        class DefaultThreadContextMapProofProfileTest {
            @Test
            void profileGetCopyPath() {
                DefaultThreadContextMap map = new DefaultThreadContextMap();
                for (int i = 0; i < 24; i++) {
                    map.put("key" + i, "value" + i);
                }
                long total = 0L;
                for (int i = 0; i < 30000; i++) {
                    Map<String, String> copy = map.getCopy();
                    total += copy.size();
                }
                assertEquals(24L * 30000L, total);
            }
        }
    """).strip() + "\n"


EXAMPLES = [
    {
        "id": "json-java-jsonobject-tostring",
        "repo_id": "json-java",
        "command_id": "jsonobject-serialize",
        "proof_id": "jsonobject-tostring",
        "title": "JSON-java / JSONObject toString() path",
        "repo_path": "GitRepos/JSON-java-master",
        "patch_path": "pr_patches/867.patch",
        "patch_subject": "Subject: [PATCH 04/20] #863 compute initial capacity for StringBuilderWriter",
        "tests": ["org.json.junit.JSONObjectProofProfileTest"],
        "iterations": 5,
        "focus_terms": [
            "org.json.JSONObject.toString",
            "org.json.JSONObject.write",
            "org.json.StringBuilderWriter.write",
            "org.json.StringBuilderWriter.append",
        ],
        "inject_files": {
            "src/test/java/org/json/junit/JSONObjectProofProfileTest.java": json_object_test,
        },
    },
    {
        "id": "json-java-xml-coercion",
        "repo_id": "json-java",
        "command_id": "xml-parse-coercion",
        "proof_id": "xml-string-to-value",
        "title": "JSON-java / XML coercion path",
        "repo_path": "GitRepos/JSON-java-master",
        "patch_path": "pr_patches/794.patch",
        "patch_subject": "Subject: [PATCH 3/3] #790 - Update XML with changes for string to number",
        "tests": ["org.json.junit.XMLProofProfileTest"],
        "iterations": 5,
        "focus_terms": [
            "org.json.XML.parse",
            "org.json.XML.stringToValue",
            "org.json.XML.stringToNumber",
            "org.json.JSONObject.accumulate",
        ],
        "inject_files": {
            "src/test/java/org/json/junit/XMLProofProfileTest.java": json_xml_test,
        },
    },
    {
        "id": "commons-io-tailer",
        "repo_id": "commons-io",
        "command_id": "tailer-polling",
        "proof_id": "tailer-run-loop",
        "title": "Commons IO / Tailer polling loop",
        "repo_path": "GitRepos/commons-io-master",
        "patch_path": "pr_patches/commonsio-2.patch",
        "patch_subject": None,
        "tests": ["org.apache.commons.io.input.TailerTest"],
        "iterations": 3,
        "focus_terms": [
            "org.apache.commons.io.input.Tailer.run",
            "org.apache.commons.io.input.Tailer.readLines",
            "org.apache.commons.io.ThreadUtils.sleep",
            "java.lang.Thread.sleep",
        ],
    },
    {
        "id": "jackson-readstring",
        "repo_id": "jackson-core",
        "command_id": "reader-string-streaming",
        "proof_id": "readerbasedjsonparser-readstring",
        "title": "Jackson-core / readString(Writer) buffered streaming",
        "repo_path": "GitRepos/jackson-core-3.x",
        "patch_path": "pr_patches_new/jackson-1543.patch",
        "patch_subject": "Subject: [PATCH 03/15] #1288: Optimize readString(Writer) with buffered writes",
        "tests": ["tools.jackson.core.unittest.read.ReadStringProofProfileTest"],
        "iterations": 5,
        "extra_args": ["-Djacoco.skip=true"],
        "focus_terms": [
            "tools.jackson.core.json.ReaderBasedJsonParser.readString",
            "tools.jackson.core.json.ReaderBasedJsonParser._streamString",
            "tools.jackson.core.util.TextBuffer.contentsToWriter",
        ],
        "inject_files": {
            "src/test/java/tools/jackson/core/unittest/read/ReadStringProofProfileTest.java": jackson_readstring_test,
        },
    },
    {
        "id": "jackson-textbuffer-utf8",
        "repo_id": "jackson-core",
        "command_id": "textbuffer-utf8",
        "proof_id": "textbuffer-reset-with-utf8",
        "title": "Jackson-core / TextBuffer resetWithUTF8",
        "repo_path": "GitRepos/jackson-core-3.x",
        "patch_path": "pr_patches_new/jackson-1486.patch",
        "patch_subject": "Subject: [PATCH 2/2] ...",
        "tests": ["tools.jackson.core.unittest.util.TextBufferProofProfileTest"],
        "iterations": 5,
        "extra_args": ["-Djacoco.skip=true"],
        "focus_terms": [
            "tools.jackson.core.util.TextBuffer.resetWithUTF8",
            "tools.jackson.core.util.TextBuffer.contentsAsString",
            "tools.jackson.core.util.TextBuffer.contentsToWriter",
        ],
        "inject_files": {
            "src/test/java/tools/jackson/core/unittest/util/TextBufferProofProfileTest.java": jackson_textbuffer_test,
        },
    },
    {
        "id": "log4j2-threadcontext-copy",
        "repo_id": "log4j2",
        "command_id": "thread-context-copy",
        "proof_id": "defaultthreadcontextmap-getcopy",
        "title": "Log4j2 / DefaultThreadContextMap.getCopy()",
        "repo_path": "GitRepos/logging-log4j2-2.x",
        "patch_path": "pr_patches_new/log4j2-3939.patch",
        "patch_subject": "Subject: [PATCH 1/3] Optimize DefaultThreadContextMap.getCopy() performance",
        "tests": ["org.apache.logging.log4j.spi.DefaultThreadContextMapProofProfileTest"],
        "iterations": 5,
        "pom_file": "log4j-api-test/pom.xml",
        "extra_args": ["-Dxml.skip=true"],
        "focus_terms": [
            "org.apache.logging.log4j.ThreadContext.getContext",
            "org.apache.logging.log4j.spi.DefaultThreadContextMap.getCopy",
            "java.util.HashMap.put",
        ],
        "inject_files": {
            "log4j-api-test/src/test/java/org/apache/logging/log4j/spi/DefaultThreadContextMapProofProfileTest.java": log4j_copy_test,
        },
    },
]


def run_git_apply(workdir: Path, args: list[str]) -> None:
    subprocess.run(["git", "-C", str(workdir), "apply", *args], check=True)


def safe_rmtree(path: Path) -> None:
    if not path.exists():
        return
    resolved = path.resolve()
    allowed = PAIR_ROOT.resolve()
    if allowed != resolved and allowed not in resolved.parents:
        raise RuntimeError(f"Unsafe delete refused: {resolved}")
    shutil.rmtree(resolved)


def extract_patch(source: Path, subject: str | None, target: Path) -> Path:
    if subject is None:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(source.read_text(encoding="utf-8", errors="replace"), encoding="utf-8")
        return target
    text = source.read_text(encoding="utf-8", errors="replace")
    idx = text.index(subject)
    start = text.rfind("From ", 0, idx)
    next_from = text.find("\nFrom ", idx)
    part = text[start:] if next_from == -1 else text[start:next_from + 1]
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(part, encoding="utf-8")
    return target


def build_maven_command(example: dict, recording_path: Path) -> list[str]:
    executable = "mvn.cmd"
    jfr_arg = f"-XX:StartFlightRecording=filename={recording_path},dumponexit=true,settings=profile"
    stack_arg = f"-XX:FlightRecorderOptions=stackdepth={STACK_DEPTH}"
    arg_line = f"{jfr_arg} {stack_arg}"
    command = [executable, "-B", f"-Dmaven.repo.local={M2_ROOT}"]
    if example.get("pom_file"):
        command.extend(["-f", example["pom_file"]])
    if example.get("projects"):
        command.extend(["-pl", ",".join(example["projects"]), "-am"])
    command.extend(example.get("extra_args", []))
    command.extend([
        f"-D{example.get('test_property', 'test')}={','.join(example['tests'])}",
        "-Dsurefire.failIfNoSpecifiedTests=false",
        "-DfailIfNoTests=false",
        "-DforkCount=1",
        "-DreuseForks=false",
        f"-DargLine={arg_line}",
        example.get("goal", "test"),
    ])
    return command


def prepare_side(example: dict, side: str) -> tuple[Path, Path]:
    source_repo = (WORKSPACE / example["repo_path"]).resolve()
    side_root = PAIR_ROOT / example["id"] / side
    safe_rmtree(side_root)
    shutil.copytree(source_repo, side_root)
    patch_target = PAIR_ROOT / example["id"] / "patches" / f"{side}.patch"
    extracted_patch = extract_patch((WORKSPACE / example["patch_path"]).resolve(), example.get("patch_subject"), patch_target)
    if side == "before":
        run_git_apply(side_root, ["-R", str(extracted_patch)])
    for relative_path, builder in example.get("inject_files", {}).items():
        file_path = side_root / relative_path
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(builder(), encoding="utf-8")
    return side_root, extracted_patch


def summarize_runs(runs: list[dict]) -> dict:
    ms = [round(run["duration_seconds"] * 1000.0, 3) for run in runs]
    average_ms = round(sum(ms) / max(len(ms), 1), 3)
    return {
        "durations_ms": ms,
        "average_ms": average_ms,
        "min_ms": min(ms) if ms else 0.0,
        "max_ms": max(ms) if ms else 0.0,
    }


def run_side(example: dict, side: str) -> dict:
    repo_dir, extracted_patch = prepare_side(example, side)
    example_output = OUTPUT_ROOT / example["id"] / side
    harness.ensure_dir(example_output)
    folded = harness.Counter()
    runs = []
    for iteration in range(1, example["iterations"] + 1):
        recording_path = example_output / f"{side}-run{iteration:02d}.jfr"
        log_path = example_output / f"{side}-run{iteration:02d}.log"
        command = build_maven_command(example, recording_path)
        return_code, duration = harness.run_command(command, repo_dir, log_path, dry_run=False)
        if return_code != 0:
            raise RuntimeError(f"{example['id']} {side} iteration {iteration} failed with exit {return_code}")
        if recording_path.exists():
            folded.update(harness.parse_jfr_samples(recording_path))
        runs.append({
            "iteration": iteration,
            "command": command,
            "recording_path": str(recording_path),
            "log_path": str(log_path),
            "duration_seconds": duration,
        })
    focused = harness.filter_folded(folded, example["focus_terms"])
    folded_path = example_output / f"{side}.folded.txt"
    focused_path = example_output / f"{side}.focused.folded.txt"
    svg_path = example_output / f"{side}.svg"
    focused_svg_path = example_output / f"{side}.focused.svg"
    harness.write_folded(folded_path, folded)
    harness.write_folded(focused_path, focused)
    subtitle = f"patch={'reversed' if side == 'before' else 'current'} | subject={example.get('patch_subject') or 'single patch'}"
    harness.render_svg(f"{example['title']} / {side}", folded, svg_path, subtitle=subtitle)
    harness.render_svg(
        f"{example['title']} / {side} focused",
        focused,
        focused_svg_path,
        subtitle=f"focus={', '.join(example['focus_terms'])}",
    )
    timing = summarize_runs(runs)
    return {
        "samples": sum(folded.values()),
        "focused_samples": sum(focused.values()),
        "svg": str(svg_path),
        "focused_svg": str(focused_svg_path),
        "folded": str(folded_path),
        "focused_folded": str(focused_path),
        "runs": runs,
        "timing": timing,
        "patch": str(extracted_patch),
    }


def pair_delta(before: dict, after: dict) -> dict:
    before_ms = before["timing"]["average_ms"]
    after_ms = after["timing"]["average_ms"]
    diff_ms = round(before_ms - after_ms, 3)
    pct = round((diff_ms / before_ms) * 100.0, 2) if before_ms else 0.0
    return {
        "average_ms_before": before_ms,
        "average_ms_after": after_ms,
        "average_ms_saved": diff_ms,
        "average_ms_saved_pct": pct,
        "focused_samples_before": before["focused_samples"],
        "focused_samples_after": after["focused_samples"],
        "focused_sample_delta": before["focused_samples"] - after["focused_samples"],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Run before/after patch-based flamegraph proofs.")
    parser.add_argument("--examples", help="Comma-separated example ids")
    args = parser.parse_args()

    selected = {entry.strip() for entry in args.examples.split(",")} if args.examples else None
    harness.ensure_dir(OUTPUT_ROOT)
    for example in EXAMPLES:
        if selected and example["id"] not in selected:
            continue
        print(f"[pair] {example['id']}")
        before = run_side(example, "before")
        after = run_side(example, "after")
        payload = {
            "id": example["id"],
            "repo_id": example["repo_id"],
            "command_id": example["command_id"],
            "proof_id": example["proof_id"],
            "title": example["title"],
            "repo_path": str((WORKSPACE / example["repo_path"]).resolve()),
            "patch_path": str((WORKSPACE / example["patch_path"]).resolve()),
            "patch_subject": example.get("patch_subject"),
            "focus_terms": example["focus_terms"],
            "generated_at": harness.timestamp_utc(),
            "before": before,
            "after": after,
            "delta": pair_delta(before, after),
        }
        meta_path = OUTPUT_ROOT / example["id"] / "pair.meta.json"
        meta_path.parent.mkdir(parents=True, exist_ok=True)
        meta_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
