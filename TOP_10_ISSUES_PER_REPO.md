# Top 10 Biggest Performance Opportunities Per Repo

This version is intentionally filtered.

Included only if at least one of these is true:
- the current flamegraph/test run is visibly dominated by it
- it is a top-ranked hotspot in the static report with structural signs of double-digit impact under scale
- it is a test-harness issue that clearly adds multi-millisecond or seconds-level cost to every run

Excluded:
- tiny formatting-only issues
- one-off low-confidence micro-allocations
- findings that are likely below the noise floor of the current workloads

## JSON-java

Current runtime note: the refreshed run still has only 7 execution samples, so the flamegraph is not dense. The reliable takeaway is that XML-heavy paths are still the biggest opportunity; finer ranking inside those paths is partly static.

1. `High confidence, large` XML parse/build in `org.json.XML` is still the dominant code-path candidate. The static report scores `XML.java` far above every other file, and the current workload was built specifically around XML and parser tests. Any reduction in repeated object creation inside that parser is the most likely route to a 10%+ gain on XML-heavy workloads.
2. `High confidence, large` `XML.java` repeatedly creates `JSONArray` instances inside deep parse loops at lines 340, 415, and 966. That is exactly the kind of hot allocation pattern that can shift both latency and GC materially when documents are large.
3. `High confidence, large` `XML.java` does repeated nested lookup work in deep loops at lines 340 and 415. Those are depth-3 to depth-5 loops in the strict report, so they are not micro issues; they are the main scalability risk in the parser.
4. `Medium-high confidence, large` `XML.removeEmpty` at line 510 is another nested recursive cleanup pass over already-built structures. If XML payloads are large, removing or collapsing that extra traversal can produce noticeable end-to-end savings.
5. `Medium-high confidence, large` `XML.unescape` at line 192 is a second pass over escape-heavy text content. On documents with many entities, this is a real throughput lever rather than a cosmetic issue.
6. `High confidence, large` `JSONML.java` is the second-highest hotspot file in the repo. If the XML route is the main path under load, `JSONML` is the next place where repeated structure building can plausibly account for double-digit overhead.
7. `High confidence, large` `JSONObject.java` remains a major construction/serialization hotspot. In practice this means repeated map growth, coercion, and stringification around the core object model, not tiny formatting waste.
8. `Medium-high confidence, large` `JSONTokener.java` is still a central parser cost center. Any repeated character-by-character advancement or reparsing there hits nearly every parse workload and compounds quickly with input size.
9. `Medium confidence, large` `XMLTokener.java` and `CDL.java` are both secondary data-movement hotspots, but `XMLTokener` matters more because it feeds the dominant XML path. If there is one non-`XML.java` parser to inspect first, it is this one.
10. `High confidence, large test-setup issue` the JSON-java profile is still too short to expose many steady-state library frames. The biggest remaining improvement in the harness is to turn the current one-pass batch into a repeated parse/write loop so test bootstrap stops consuming such a large share of the recording.

## Commons IO

Current runtime note: the refreshed run improved to 7 samples over an 89.8s run, but the flamegraph still shows a lot of test and temp-directory setup. The biggest confirmed runtime issue is that the current monitoring and temp-dir-heavy tests inject large overhead before the library's hot loops fully dominate.

1. `High confidence, large` the biggest measured cost in the current Commons run is still test setup around temp directories and secure-random name generation. This is not a small issue: it is taking a meaningful share of an 89.8 second run, so the current workload should be changed if you want cleaner library flamegraphs.
2. `High confidence, large` `Tailer.java` is the top real library hotspot and the strongest production candidate. It creates raw threads directly and also builds single-thread executors, which scales badly in monitoring-heavy deployments.
3. `High confidence, large` `ReadAheadInputStream.java` has the same pattern: per-instance thread and executor creation. On workloads with many streams this can become a double-digit overhead source through scheduling, idle threads, and context switching.
4. `High confidence, large` `Tailer` is also the clearest waiting/polling hotspot in the exercised workload. If the goal is reducing wasted CPU, this is the first Commons IO class to change.
5. `Medium-high confidence, large` `ReadAheadInputStream` has a deep nested loop around line 438 in the strict report in addition to its concurrency overhead. That means it has both control-plane waste and data-path waste.
6. `Medium-high confidence, large` `IOUtils.java` remains one of the biggest broad-surface cost centers because it sits under copy, write, and line-processing operations. The nested and materialization-heavy work at lines 2585, 3931, and 3976 is large enough to matter across many call sites.
7. `Medium-high confidence, large` `FileUtils.java` stays in the top band because file-tree and metadata-heavy operations multiply filesystem lookups. The nested work around line 1372 is the kind of hotspot that can dominate large directory traversals.
8. `Medium-high confidence, large` `PathUtils.java` is another serious tree-size amplifier. The comparison and content-equality style work around lines 351 and 751 will scale poorly on big directory comparisons.
9. `Medium confidence, large` `ReaderInputStream.java` and `UnsynchronizedBufferedReader.java` are still worth treating as large opportunities because char-byte conversion and refill loops sit in central transport paths, not edge features.
10. `High confidence, large test-setup issue` the Commons workload still needs one more adjustment: fewer temp-dir-centric tests and more repeated in-memory copy/read loops. Until that changes, the flamegraph will keep overstating harness entropy and understating the actual IO inner loops.

## Jackson-core

Current runtime note: the selected batch passes, but the current JFR path still produced `0` execution samples. So this section is ranked from the strongest large static opportunities plus the test-setup problem itself.

1. `High confidence, large test-setup issue` the biggest Jackson issue is still measurement failure. With zero execution samples, the harness is not attaching at the right JVM boundary or the tests are too short in the forked JVM. Fixing that is the largest remaining prerequisite because it blocks every real hotspot decision.
2. `High confidence, large` `JsonPointer.java` is the top-ranked hotspot in the repo and the best first optimization target. Its repeated segment construction in `valueOf` around line 740 is a central path, not an edge-case formatter.
3. `High confidence, large` `JsonPointer.valueOf` also has repeated nested work around line 863. For long or repeated pointer parsing, this is a plausible double-digit cost center.
4. `High confidence, large` `TextBuffer.java` is the second major target. The strict report flags deep nested loops at lines 542, 759, and 1205, which indicates real scalability pressure in buffer growth and segment processing.
5. `Medium-high confidence, large` parser buffer and text handling in `TextBuffer` are likely to affect many read paths simultaneously, so changes there can produce broad wins rather than isolated micro-improvements.
6. `Medium confidence, large` `UTF8StreamJsonParser.java` is still a major candidate simply because it is one of the central streaming parsers and appears in the hotspot list. Even though the current analyzer mostly caught allocation-heavy error paths, the class is too central to ignore.
7. `Medium confidence, large` `UTF8DataInputJsonParser.java` is the same story on the data-input route: broad parse-surface exposure makes it a stronger candidate than the low-level individual findings suggest.
8. `Medium confidence, large` `ReaderBasedJsonParser.java` belongs in the top tier because reader-backed parsing is a distinct hot path that the current workload should stress more directly.
9. `Medium confidence, large` `JsonGenerator.java` is one of the few write-side entries in the hotspot list, which makes it important if the target use case includes heavy serialization as well as parsing.
10. `Medium confidence, large` `FilteringParserDelegate.java` and recycler/buffer-pool behavior are still worth investigation, but the `JsonRecyclerPools` findings in the strict report must be manually filtered because the analyzer over-matched `ThreadLocal` text as thread creation. Treat the pool area as important, but do not trust the raw thread-creation labels there.

## Log4j2

Current runtime note: the narrowed Log4j API run now passes and yields 25 samples over 386.6 seconds. Even here, the flamegraph still shows large harness overhead from JUnit, temp dirs, System Stubs, Mockito, and class retransformation before the library's own utility paths fully dominate.

1. `High confidence, large` the biggest measured issue in the current Log4j test batch is still harness overhead: Mockito inline instrumentation, System Stubs environment patching, temp-dir creation, and JUnit discovery all consume a visible share of the recording. This is a seconds-level problem in the current profiling setup.
2. `High confidence, large` `PropertiesUtil` is the clearest runtime-visible library hotspot in the passing Log4j run. Charset resolution and provider loading show up directly, so this is the best proven API-layer optimization candidate today.
3. `High confidence, large` `ProviderUtil` and service/provider discovery remain a large startup-style cost center. When logging boots frequently or properties are read repeatedly, this is exactly the kind of control-plane cost that can move latency materially.
4. `High confidence, large` `ThreadContext` and `DefaultThreadContextMap` are still top API-surface candidates because they sit in per-log-call context handling. That means even moderate inefficiency there multiplies quickly under load.
5. `High confidence, large` `Unbox.java` is the top `log4j-api` static hotspot and one of the few API classes explicitly called out near the top of the repo-wide ranking. Boxing avoidance paths are central to hot logging throughput, so this is not a small issue.
6. `High confidence, large` `log4j-core` `tools.picocli.CommandLine.java` is the single highest-scoring hotspot in the whole repo by a wide margin. It contains multiple deep nested-loop sites and repeated parsing/setup work, so it stays near the top even though the current runtime batch is API-focused.
7. `High confidence, large` `ScriptManager.java` is the second major core-side candidate. Repeated script setup or dispatch is expensive enough that it remains top-tier without additional runtime proof.
8. `High confidence, large` `Rfc5424Layout.java` is a serious formatting and payload-construction hotspot. Structured logging layouts can easily turn this into a multi-millisecond path on large events.
9. `High confidence, large` `DefaultMergeStrategy.java`, `MapFilter.java`, and `StructuredDataFilter.java` are all configuration/filtering hotspots built around repeated scans and matching. If you want the biggest config-path savings, these are the dominant targets.
10. `High confidence, large test-setup issue` the Log4j workload still needs another adjustment if the goal is pure library profiling: fewer mocking-heavy tests and more long-running repeated property/context/string/unbox loops. Right now the harness still hides part of the true library cost behind framework startup and bytecode instrumentation.

## Bottom Line

- `JSON-java`: biggest code opportunities are still XML parsing and XML-to-object construction paths.
- `commons-io`: biggest proven waste is test setup plus the `Tailer` and `ReadAheadInputStream` concurrency model.
- `jackson-core`: biggest issue is still that the profile is not capturing runtime samples; `JsonPointer` and `TextBuffer` remain the best large static targets.
- `log4j2`: biggest proven runtime library signal is `PropertiesUtil`/provider/context setup, but the current test harness still burns a lot of time in JUnit, Mockito, and temp-dir plumbing.
