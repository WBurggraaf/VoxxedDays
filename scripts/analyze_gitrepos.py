#!/usr/bin/env python3
"""Batch green-code static analysis for Java repositories under GitRepos."""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Iterable


SEVERITY_WEIGHTS = {"High": 3, "Medium": 2, "Low": 1}
PATTERN_LABELS = {
    "idle-compute": "Idle compute",
    "waiting-pattern": "Waiting pattern",
    "chatty-io": "Chatty I/O",
    "repeated-work": "Repeated work",
    "algorithmic-waste": "Algorithmic waste",
    "allocation-pressure": "Allocation pressure",
    "concurrency-misuse": "Concurrency misuse",
    "data-movement-bloat": "Data movement bloat",
}
LOG_TOKENS = ("log.", "logger.", "LOGGER.", "System.out.", "System.err.")
REMOTE_IO_VERBS = (
    "fetch",
    "query",
    "select",
    "insert",
    "delete",
    "execute",
    "request",
)
REMOTE_ROLE_TOKENS = (
    "client",
    "repository",
    "dao",
    "service",
    "socket",
    "urlconnection",
    "resttemplate",
    "webclient",
    "entitymanager",
    "jdbc",
    "statement",
)
LOCAL_STREAM_TOKENS = ("read(", "write(", "reader", "writer", "inputstream", "outputstream", "channel", "file")
BUFFER_TOKENS = ("buffer", "buffered", "char[]", "byte[]")
POLLING_TOKENS = ("ready", "done", "complete", "finished", "alive", "status", "flag", "available")
ALLOC_TOKENS = (
    "new ArrayList",
    "new HashMap",
    "new HashSet",
    "new LinkedList",
    "new StringBuilder",
    "new StringBuffer",
    "new JSONObject",
    "new JSONArray",
    "new ObjectMapper",
    "Pattern.compile",
    "DateTimeFormatter.ofPattern",
    "SimpleDateFormat",
)
CONCURRENCY_TOKENS = (
    "new Thread",
    "Executors.new",
    "CompletableFuture",
    "parallelStream(",
    "ForkJoinPool",
)
PARSER_TOKENS = ("parse(", "fromJson(", "toJson(", "readValue(", "writeValue")
CONTROL_KEYWORDS = {"if", "for", "while", "switch", "catch", "return", "throw", "new", "else", "do", "try"}


@dataclass
class LoopInfo:
    line: int
    kind: str
    nesting_depth: int
    body: list[str] = field(default_factory=list)


@dataclass
class MethodInfo:
    name: str
    start_line: int
    end_line: int


@dataclass
class Finding:
    severity: str
    confidence: str
    pattern: str
    title: str
    location: str
    what_was_found: str
    why_it_is_wasteful: str
    likely_impact: str
    recommended_remediation: str
    low_waste_rationale: str
    evidence: list[str] = field(default_factory=list)


@dataclass
class FileAnalysis:
    file: str
    is_test: bool
    classes: list[str]
    methods: list[MethodInfo]
    loops: list[LoopInfo]
    stream_pipelines: list[int]
    synchronized_blocks: list[int]
    concurrency_usage: list[str]
    findings: list[Finding]


class JavaGreenAnalyzer:
    class_pattern = re.compile(r"\b(class|interface|enum|record)\s+([A-Za-z_][A-Za-z0-9_]*)")
    method_pattern = re.compile(
        r"^\s*(?:public|protected|private|static|final|native|synchronized|abstract|\s)+"
        r"[\w<>\[\], ?]+\s+([A-Za-z_][A-Za-z0-9_]*)\s*\([^;]*\)\s*\{"
    )
    loop_pattern = re.compile(r"\b(for|while)\s*\(")

    def analyze_file(self, path: Path) -> FileAnalysis:
        lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
        classes = [match.group(2) for line in lines for match in self.class_pattern.finditer(line)]
        methods = self._extract_methods(lines)
        loops = self._extract_loops(lines)
        stream_pipelines = [index for index, line in enumerate(lines, start=1) if ".stream()" in line or ".parallelStream()" in line]
        synchronized_blocks = [index for index, line in enumerate(lines, start=1) if "synchronized" in line]
        concurrency_usage = [line.strip() for line in lines if any(token in line for token in CONCURRENCY_TOKENS)]
        findings = self._build_findings(lines, loops, methods)
        return FileAnalysis(
            file=str(path),
            is_test=is_test_path(path),
            classes=classes,
            methods=methods,
            loops=loops,
            stream_pipelines=stream_pipelines,
            synchronized_blocks=synchronized_blocks,
            concurrency_usage=concurrency_usage,
            findings=findings,
        )

    def _extract_methods(self, lines: list[str]) -> list[MethodInfo]:
        methods: list[MethodInfo] = []
        brace_depth = 0
        open_method: MethodInfo | None = None
        method_depth = 0
        for index, line in enumerate(lines, start=1):
            if open_method is None:
                match = self.method_pattern.match(line)
                if match:
                    method_name = match.group(1)
                    if method_name in CONTROL_KEYWORDS:
                        brace_depth += line.count("{") - line.count("}")
                        continue
                    open_method = MethodInfo(name=method_name, start_line=index, end_line=index)
                    method_depth = brace_depth + line.count("{") - line.count("}")
            brace_depth += line.count("{") - line.count("}")
            if open_method is not None and brace_depth < method_depth:
                open_method.end_line = index
                methods.append(open_method)
                open_method = None
        if open_method is not None:
            open_method.end_line = len(lines)
            methods.append(open_method)
        return methods

    def _extract_loops(self, lines: list[str]) -> list[LoopInfo]:
        loops: list[LoopInfo] = []
        brace_depth = 0
        for index, line in enumerate(lines, start=1):
            current_depth = brace_depth
            match = self.loop_pattern.search(line)
            brace_depth += line.count("{") - line.count("}")
            if not match:
                continue
            body, _ = self._capture_block(lines, index - 1)
            loops.append(LoopInfo(line=index, kind=match.group(1), nesting_depth=max(current_depth, 0), body=body))
        return loops

    def _capture_block(self, lines: list[str], start_index: int) -> tuple[list[str], int]:
        body: list[str] = []
        opened = 0
        started = False
        index = start_index
        while index < len(lines):
            line = lines[index]
            if not started and "{" in line:
                started = True
            if started:
                opened += line.count("{")
                body.append(line)
                opened -= line.count("}")
                if opened <= 0 and index > start_index:
                    break
            elif index == start_index:
                body.append(line)
                break
            index += 1
        return body, index

    def _build_findings(self, lines: list[str], loops: list[LoopInfo], methods: list[MethodInfo]) -> list[Finding]:
        findings: list[Finding] = []
        findings.extend(self._detect_busy_wait(loops, methods))
        findings.extend(self._detect_chatty_io(loops, methods))
        findings.extend(self._detect_repeated_work(loops, methods))
        findings.extend(self._detect_algorithmic_waste(lines, loops, methods))
        findings.extend(self._detect_allocation_pressure(loops, methods))
        findings.extend(self._detect_concurrency_misuse(lines, methods))
        findings.extend(self._detect_data_bloat(loops, methods))
        findings.sort(key=lambda item: (-SEVERITY_WEIGHTS[item.severity], item.title, item.location))
        return findings

    def _detect_busy_wait(self, loops: list[LoopInfo], methods: list[MethodInfo]) -> list[Finding]:
        findings: list[Finding] = []
        for loop in loops:
            body_text = "\n".join(loop.body)
            lowered = body_text.lower()
            stripped = [entry.strip() for entry in loop.body if entry.strip()]
            location = self._locate(loop.line, methods)
            looks_like_polling = loop.kind == "while" and any(token in lowered for token in POLLING_TOKENS)
            looks_like_data_processing = any(token in lowered for token in ("read(", "next(", "parse(", "tokener", "scanner", "iterator", "hasnext", "append"))
            if (
                looks_like_polling
                and len(stripped) <= 3
                and "Thread.sleep" not in body_text
                and "wait(" not in body_text
                and not looks_like_data_processing
            ):
                findings.append(
                    Finding(
                        severity="High",
                        confidence="Medium",
                        pattern="idle-compute",
                        title="Polling loop without blocking",
                        location=location,
                        what_was_found=f"{loop.kind} loop at line {loop.line} appears to poll shared state without a blocking primitive.",
                        why_it_is_wasteful="A polling loop repeatedly burns CPU to recheck readiness instead of sleeping until useful work can continue.",
                        likely_impact="Higher CPU utilization, thermal pressure, and reduced throughput for other work on the same host.",
                        recommended_remediation="Replace polling with a blocking primitive, callback, latch, queue, or at least bounded backoff.",
                        low_waste_rationale="Blocking or event-driven coordination cuts useless instructions and improves value per watt.",
                        evidence=[f"line {loop.line}"],
                    )
                )
            if "Thread.sleep" in body_text and ("retry" in lowered or looks_like_polling):
                findings.append(
                    Finding(
                        severity="Medium",
                        confidence="Medium",
                        pattern="waiting-pattern",
                        title="Sleep-based coordination loop",
                        location=location,
                        what_was_found=f"{loop.kind} loop at line {loop.line} uses `Thread.sleep(...)` as a coordination mechanism.",
                        why_it_is_wasteful="Sleep polling still wakes up periodically to recheck state, adding latency and unnecessary scheduler churn.",
                        likely_impact="Longer wait times, avoidable wakeups, and lower efficiency under load.",
                        recommended_remediation="Move to completion signals, blocking queues, futures, or exponential backoff with strict bounds.",
                        low_waste_rationale="Reducing periodic wakeups lowers wasted CPU time and coordination overhead.",
                        evidence=[f"line {loop.line}"],
                    )
                )
        return findings

    def _detect_chatty_io(self, loops: list[LoopInfo], methods: list[MethodInfo]) -> list[Finding]:
        findings: list[Finding] = []
        for loop in loops:
            remote_calls = [entry.strip() for entry in loop.body if self._looks_like_remote_io(entry)]
            log_calls = [entry.strip() for entry in loop.body if any(token in entry for token in LOG_TOKENS)]
            if not remote_calls and not log_calls:
                continue
            if remote_calls:
                severity = "High" if len(remote_calls) > 1 or loop.nesting_depth > 0 else "Medium"
                findings.append(
                    Finding(
                        severity=severity,
                        confidence="Medium",
                        pattern="chatty-io",
                        title="Remote or service call inside loop",
                        location=self._locate(loop.line, methods),
                        what_was_found=f"Loop at line {loop.line} contains calls that look like repository, client, network, or database access.",
                        why_it_is_wasteful="Repeated external calls inside iteration amplify latency and often create N+1 style traffic.",
                        likely_impact="Slower batch processing, more round trips, and higher infrastructure cost.",
                        recommended_remediation="Batch external calls, prefetch data before iterating, or aggregate writes after the loop.",
                        low_waste_rationale="Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.",
                        evidence=remote_calls[:3],
                    )
                )
            if log_calls and len(log_calls) >= 2:
                findings.append(
                    Finding(
                        severity="Low",
                        confidence="High",
                        pattern="chatty-io",
                        title="Repeated logging inside loop",
                        location=self._locate(loop.line, methods),
                        what_was_found=f"Loop at line {loop.line} logs on the hot iteration path.",
                        why_it_is_wasteful="Per-item logging adds formatting work and I/O overhead that can dominate lightweight loops.",
                        likely_impact="Lower throughput and larger log volumes for routine processing paths.",
                        recommended_remediation="Log summaries outside the loop or guard verbose logs behind debug checks.",
                        low_waste_rationale="Reducing log volume cuts bytes written and CPU spent formatting low-value output.",
                        evidence=log_calls[:3],
                    )
                )
        return findings

    def _detect_repeated_work(self, loops: list[LoopInfo], methods: list[MethodInfo]) -> list[Finding]:
        findings: list[Finding] = []
        for loop in loops:
            matches = [entry.strip() for entry in loop.body if any(token in entry for token in ALLOC_TOKENS + PARSER_TOKENS)]
            if not matches:
                continue
            findings.append(
                Finding(
                    severity="Medium",
                    confidence="High",
                    pattern="repeated-work",
                    title="Repeated setup or parsing inside loop",
                    location=self._locate(loop.line, methods),
                    what_was_found=f"Loop at line {loop.line} recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.",
                    why_it_is_wasteful="Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.",
                    likely_impact="Higher latency, avoidable GC churn, and lower throughput on larger collections.",
                    recommended_remediation="Hoist reusable helpers outside the loop and cache invariant computations.",
                    low_waste_rationale="Reusing expensive helpers reduces instructions executed and memory churn per item processed.",
                    evidence=matches[:3],
                )
            )
        return findings

    def _detect_algorithmic_waste(self, lines: list[str], loops: list[LoopInfo], methods: list[MethodInfo]) -> list[Finding]:
        findings: list[Finding] = []
        for loop in loops:
            body_text = "\n".join(loop.body)
            if ".contains(" in body_text and "List<" in "\n".join(lines[max(loop.line - 6, 0):loop.line]):
                findings.append(
                    Finding(
                        severity="Medium",
                        confidence="Medium",
                        pattern="algorithmic-waste",
                        title="List membership checks inside loop",
                        location=self._locate(loop.line, methods),
                        what_was_found=f"Loop at line {loop.line} performs `.contains(...)` checks that may scan collections repeatedly.",
                        why_it_is_wasteful="Repeated linear scans inside iteration can push runtime toward O(n^2) as data sets grow.",
                        likely_impact="Throughput degradation and elevated CPU time for larger inputs.",
                        recommended_remediation="Use a `Set` for membership lookups or pre-index data before the loop.",
                        low_waste_rationale="Indexing once avoids repeated scans and reduces wasted CPU work.",
                        evidence=[f"line {loop.line}"],
                    )
                )
            nested_hotspots = ("contains(", "indexOf(", ".get(", ".find(", ".stream()", ".parallelStream()", ".sort(")
            if loop.nesting_depth >= 2 and any(token in body_text for token in nested_hotspots):
                findings.append(
                    Finding(
                        severity="Medium",
                        confidence="Medium",
                        pattern="algorithmic-waste",
                        title="Nested loop with repeated lookup work",
                        location=self._locate(loop.line, methods),
                        what_was_found=f"Loop at line {loop.line} is nested at depth {loop.nesting_depth} and also performs repeated lookup or transformation work.",
                        why_it_is_wasteful="Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.",
                        likely_impact="Poor scalability, longer batch runtimes, and excess CPU consumption.",
                        recommended_remediation="Pre-index shared data, reduce nested scans, or collapse passes where possible.",
                        low_waste_rationale="Lowering algorithmic complexity reduces operations and energy for the same user-visible result.",
                        evidence=[f"line {loop.line}"],
                    )
                )
        return findings

    def _detect_allocation_pressure(self, loops: list[LoopInfo], methods: list[MethodInfo]) -> list[Finding]:
        findings: list[Finding] = []
        for loop in loops:
            allocs = [entry.strip() for entry in loop.body if any(token in entry for token in ALLOC_TOKENS)]
            if allocs:
                findings.append(
                    Finding(
                        severity="Medium",
                        confidence="High",
                        pattern="allocation-pressure",
                        title="Allocation-heavy loop body",
                        location=self._locate(loop.line, methods),
                        what_was_found=f"Loop at line {loop.line} allocates new collections, builders, or mapping helpers during iteration.",
                        why_it_is_wasteful="Frequent temporary allocations increase GC activity and memory traffic without adding durable value.",
                        likely_impact="Higher heap pressure, more garbage collection, and reduced steady-state performance.",
                        recommended_remediation="Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.",
                        low_waste_rationale="Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.",
                        evidence=allocs[:3],
                    )
                )
            concat_lines = [entry.strip() for entry in loop.body if re.search(r'".*"\s*\+', entry)]
            if concat_lines:
                findings.append(
                    Finding(
                        severity="Low",
                        confidence="Medium",
                        pattern="allocation-pressure",
                        title="String concatenation in loop",
                        location=self._locate(loop.line, methods),
                        what_was_found=f"Loop at line {loop.line} builds strings through repeated concatenation.",
                        why_it_is_wasteful="Repeated concatenation can allocate many intermediate strings in hot iteration paths.",
                        likely_impact="Extra allocation churn and slower formatting-heavy paths.",
                        recommended_remediation="Use a shared `StringBuilder` or defer formatting until it is needed.",
                        low_waste_rationale="Reducing intermediate strings lowers heap churn and CPU spent copying characters.",
                        evidence=concat_lines[:3],
                    )
                )
        return findings

    def _detect_concurrency_misuse(self, lines: list[str], methods: list[MethodInfo]) -> list[Finding]:
        findings: list[Finding] = []
        for index, line in enumerate(lines, start=1):
            stripped = line.strip()
            location = self._locate(index, methods)
            if "Executors.new" in stripped:
                findings.append(
                    Finding(
                        severity="Medium",
                        confidence="High",
                        pattern="concurrency-misuse",
                        title="Executor created in application code path",
                        location=location,
                        what_was_found=f"Line {index} creates a new executor instance.",
                        why_it_is_wasteful="Creating executors per call can fragment thread pools and increase context switching and idle threads.",
                        likely_impact="Higher memory use, poorer scheduling efficiency, and harder concurrency control.",
                        recommended_remediation="Reuse a bounded shared executor sized to the workload.",
                        low_waste_rationale="Bounded executor reuse reduces idle threads and CPU overhead without reducing useful throughput.",
                        evidence=[stripped],
                    )
                )
            if ".parallelStream()" in stripped:
                findings.append(
                    Finding(
                        severity="Low",
                        confidence="Medium",
                        pattern="concurrency-misuse",
                        title="Parallel stream usage requires workload validation",
                        location=location,
                        what_was_found=f"Line {index} uses `parallelStream()`.",
                        why_it_is_wasteful="Parallel streams can add splitting, synchronization, and scheduling overhead when workloads are small or blocking.",
                        likely_impact="Higher CPU use and worse latency instead of better throughput.",
                        recommended_remediation="Validate collection size and workload type, or prefer explicit bounded executors for heavy tasks.",
                        low_waste_rationale="Concurrency should only add parallel work when it reduces total operations per useful result.",
                        evidence=[stripped],
                    )
                )
            if "new Thread" in stripped:
                findings.append(
                    Finding(
                        severity="High",
                        confidence="High",
                        pattern="concurrency-misuse",
                        title="Direct thread creation",
                        location=location,
                        what_was_found=f"Line {index} creates a thread directly.",
                        why_it_is_wasteful="Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.",
                        likely_impact="Thread proliferation, unstable latency, and reduced machine efficiency under load.",
                        recommended_remediation="Route work through bounded executors or structured concurrency instead of raw thread creation.",
                        low_waste_rationale="Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.",
                        evidence=[stripped],
                    )
                )
        return findings

    def _detect_data_bloat(self, loops: list[LoopInfo], methods: list[MethodInfo]) -> list[Finding]:
        findings: list[Finding] = []
        for loop in loops:
            bulky = [
                entry.strip()
                for entry in loop.body
                if any(token in entry for token in ("toString()", "writeValueAsString", "JSONObject(", "JSONArray(", "collect(Collectors.toList())"))
            ]
            if bulky:
                findings.append(
                    Finding(
                        severity="Medium",
                        confidence="Medium",
                        pattern="data-movement-bloat",
                        title="Payload construction inside loop",
                        location=self._locate(loop.line, methods),
                        what_was_found=f"Loop at line {loop.line} serializes, materializes, or expands payload-like objects during iteration.",
                        why_it_is_wasteful="Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.",
                        likely_impact="Higher memory use, longer serialization time, and avoidable network or logging overhead.",
                        recommended_remediation="Filter earlier, narrow the fields being built, or batch serialization closer to the sink.",
                        low_waste_rationale="Constructing only the bytes that are actually needed reduces memory traffic and output overhead.",
                        evidence=bulky[:3],
                    )
                )
        return findings

    def _looks_like_remote_io(self, line: str) -> bool:
        lowered = line.lower()
        if any(token in lowered for token in LOCAL_STREAM_TOKENS):
            return False
        if any(role in lowered for role in REMOTE_ROLE_TOKENS) and ('.' in line or '(' in line):
            return True
        return any(re.search(rf'(?<![A-Za-z0-9_]){verb}[A-Za-z0-9_]*\s*\(', lowered) for verb in REMOTE_IO_VERBS)

    def _locate(self, line_number: int, methods: list[MethodInfo]) -> str:
        for method in methods:
            if method.start_line <= line_number <= method.end_line:
                return f"{method.name} (line {line_number})"
        return f"line {line_number}"


def summarize_project(name: str, analyses: list[FileAnalysis]) -> dict:
    severity_counts = Counter()
    pattern_counts = Counter()
    scored_files = []
    for analysis in analyses:
        for finding in analysis.findings:
            severity_counts[finding.severity] += 1
            pattern_counts[finding.pattern] += 1
        score = sum(SEVERITY_WEIGHTS[finding.severity] for finding in analysis.findings)
        if score:
            scored_files.append((score, analysis.file, len(analysis.findings)))
    scored_files.sort(reverse=True)
    overall_risk = "Low"
    if severity_counts["High"] >= 5 or sum(severity_counts.values()) >= 25:
        overall_risk = "High"
    elif severity_counts["High"] or severity_counts["Medium"] >= 8:
        overall_risk = "Medium"
    return {
        "project": name,
        "overall_risk": overall_risk,
        "java_files": len(analyses),
        "source_files": sum(1 for analysis in analyses if not analysis.is_test),
        "test_files": sum(1 for analysis in analyses if analysis.is_test),
        "findings": dict(severity_counts),
        "top_patterns": [PATTERN_LABELS[key] for key, _ in pattern_counts.most_common(5)],
        "hotspots": [
            {"file": file_path, "score": score, "findings": finding_count}
            for score, file_path, finding_count in scored_files[:10]
        ],
    }


def write_json(output_path: Path, payload: dict) -> None:
    output_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def write_project_markdown(output_path: Path, summary: dict, analyses: list[FileAnalysis], project_root: Path) -> None:
    lines: list[str] = []
    lines.append(f"# {summary['project']} Green Code Report")
    lines.append("")
    lines.append("## Summary")
    lines.append(f"- Project root: `{project_root}`")
    lines.append(f"- Java files reviewed: {summary['java_files']}")
    lines.append(f"- Source files: {summary['source_files']}")
    lines.append(f"- Test files: {summary['test_files']}")
    lines.append(f"- Overall risk level: {summary['overall_risk']}")
    counts = summary["findings"]
    lines.append(
        "- Findings by severity: "
        f"High {counts.get('High', 0)}, Medium {counts.get('Medium', 0)}, Low {counts.get('Low', 0)}"
    )
    top_patterns = ", ".join(summary["top_patterns"]) if summary["top_patterns"] else "None"
    lines.append(f"- Top efficiency themes: {top_patterns}")
    lines.append("")
    lines.append("## Hotspots")
    if summary["hotspots"]:
        for hotspot in summary["hotspots"]:
            rel_path = Path(hotspot["file"]).relative_to(project_root)
            lines.append(f"- `{rel_path}`: score {hotspot['score']}, findings {hotspot['findings']}")
    else:
        lines.append("- No findings detected by the current heuristic set.")
    lines.append("")
    lines.append("## File Findings")
    ranked_files = sorted(
        analyses,
        key=lambda item: sum(SEVERITY_WEIGHTS[finding.severity] for finding in item.findings),
        reverse=True,
    )
    for analysis in ranked_files:
        if not analysis.findings:
            continue
        rel_path = Path(analysis.file).relative_to(project_root)
        lines.append(f"### `{rel_path}`")
        lines.append("")
        lines.append(
            f"- Pre-analysis: classes {len(analysis.classes)}, methods {len(analysis.methods)}, "
            f"loops {len(analysis.loops)}, streams {len(analysis.stream_pipelines)}, synchronized blocks {len(analysis.synchronized_blocks)}"
        )
        for index, finding in enumerate(analysis.findings, start=1):
            lines.append(f"#### {index}. {finding.title}")
            lines.append(f"- Severity: {finding.severity}")
            lines.append(f"- Confidence: {finding.confidence}")
            lines.append(f"- Location: {finding.location}")
            lines.append(f"- Pattern: {finding.pattern}")
            lines.append(f"- What was found: {finding.what_was_found}")
            lines.append(f"- Why it is wasteful: {finding.why_it_is_wasteful}")
            lines.append(f"- Likely impact: {finding.likely_impact}")
            lines.append(f"- Recommended remediation: {finding.recommended_remediation}")
            lines.append(f"- Low-waste rationale: {finding.low_waste_rationale}")
            if finding.evidence:
                lines.append(f"- Evidence: {' | '.join(finding.evidence)}")
        lines.append("")
    lines.append("## Cautions")
    lines.append("- This is static analysis only; findings indicate likely waste patterns, not measured bottlenecks.")
    lines.append("- Method extraction and loop classification are heuristic and may miss unconventional Java syntax.")
    output_path.write_text("\n".join(lines), encoding="utf-8")


def write_rollup_markdown(output_path: Path, summaries: list[dict]) -> None:
    lines = ["# GitRepos Green Code Rollup", "", "## Projects"]
    for summary in summaries:
        counts = summary["findings"]
        lines.append(
            f"- `{summary['project']}`: risk {summary['overall_risk']}, "
            f"files {summary['java_files']}, findings H/M/L = "
            f"{counts.get('High', 0)}/{counts.get('Medium', 0)}/{counts.get('Low', 0)}"
        )
    output_path.write_text("\n".join(lines), encoding="utf-8")


def write_rollup_csv(output_path: Path, summaries: list[dict]) -> None:
    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["project", "overall_risk", "java_files", "source_files", "test_files", "high", "medium", "low", "top_patterns"])
        for summary in summaries:
            counts = summary["findings"]
            writer.writerow([
                summary["project"],
                summary["overall_risk"],
                summary["java_files"],
                summary["source_files"],
                summary["test_files"],
                counts.get("High", 0),
                counts.get("Medium", 0),
                counts.get("Low", 0),
                "; ".join(summary["top_patterns"]),
            ])


def write_project_findings_csv(output_path: Path, analyses: list[FileAnalysis], project_root: Path) -> None:
    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["file", "is_test", "severity", "confidence", "pattern", "title", "location", "what_was_found"])
        for analysis in analyses:
            rel_path = Path(analysis.file).relative_to(project_root)
            for finding in analysis.findings:
                writer.writerow([
                    str(rel_path),
                    analysis.is_test,
                    finding.severity,
                    finding.confidence,
                    finding.pattern,
                    finding.title,
                    finding.location,
                    finding.what_was_found,
                ])


def serialize_analysis(analysis: FileAnalysis) -> dict:
    payload = asdict(analysis)
    payload["methods"] = [asdict(method) for method in analysis.methods]
    payload["loops"] = [asdict(loop) for loop in analysis.loops]
    payload["findings"] = [asdict(finding) for finding in analysis.findings]
    return payload


def iter_projects(root: Path) -> Iterable[Path]:
    for child in sorted(root.iterdir()):
        if child.is_dir():
            yield child


def is_test_path(path: Path) -> bool:
    lowered = str(path).replace('\\', '/').lower()
    return '/src/test/' in lowered or '/test/' in lowered or lowered.endswith('test.java') or lowered.endswith('tests.java')


def main() -> int:
    parser = argparse.ArgumentParser(description="Analyze Java projects under GitRepos for green-code inefficiency patterns.")
    parser.add_argument("--repos-root", default="GitRepos", help="Directory containing project folders.")
    parser.add_argument("--output-root", default="analysis_reports", help="Directory for generated reports.")
    parser.add_argument("--include-tests", action="store_true", help="Include files under test source roots.")
    args = parser.parse_args()

    repos_root = Path(args.repos_root).resolve()
    output_root = Path(args.output_root).resolve()
    output_root.mkdir(parents=True, exist_ok=True)

    analyzer = JavaGreenAnalyzer()
    summaries: list[dict] = []

    for project_root in iter_projects(repos_root):
        java_files = sorted(project_root.rglob("*.java"))
        if not args.include_tests:
            java_files = [path for path in java_files if not is_test_path(path)]
        analyses = [analyzer.analyze_file(path) for path in java_files]
        summary = summarize_project(project_root.name, analyses)
        summaries.append(summary)

        project_output = output_root / project_root.name
        project_output.mkdir(parents=True, exist_ok=True)
        write_json(
            project_output / "analysis.json",
            {
                "summary": summary,
                "files": [serialize_analysis(analysis) for analysis in analyses],
            },
        )
        write_project_markdown(project_output / "report.md", summary, analyses, project_root)
        write_project_findings_csv(project_output / "findings.csv", analyses, project_root)

    write_json(output_root / "rollup.json", {"projects": summaries})
    write_rollup_markdown(output_root / "README.md", summaries)
    write_rollup_csv(output_root / "rollup.csv", summaries)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
