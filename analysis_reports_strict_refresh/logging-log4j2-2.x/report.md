# logging-log4j2-2.x Green Code Report

## Summary
- Project root: `C:\VoxxedDays\GitRepos\logging-log4j2-2.x`
- Java files reviewed: 1487
- Source files: 1487
- Test files: 0
- Overall risk level: High
- Findings by severity: High 95, Medium 275, Low 96
- Top efficiency themes: Algorithmic waste, Allocation pressure, Chatty I/O, Concurrency misuse, Repeated work

## Hotspots
- `log4j-core\src\main\java\org\apache\logging\log4j\core\tools\picocli\CommandLine.java`: score 40, findings 23
- `log4j-core\src\main\java\org\apache\logging\log4j\core\script\ScriptManager.java`: score 23, findings 10
- `log4j-core\src\main\java\org\apache\logging\log4j\core\layout\Rfc5424Layout.java`: score 21, findings 11
- `log4j-core\src\main\java\org\apache\logging\log4j\core\config\composite\DefaultMergeStrategy.java`: score 20, findings 10
- `log4j-core\src\main\java\org\apache\logging\log4j\core\filter\MapFilter.java`: score 18, findings 10
- `log4j-core\src\main\java\org\apache\logging\log4j\core\appender\rolling\DefaultRolloverStrategy.java`: score 18, findings 10
- `log4j-api\src\main\java\org\apache\logging\log4j\util\Unbox.java`: score 17, findings 7
- `log4j-core\src\main\java\org\apache\logging\log4j\core\net\TcpSocketManager.java`: score 16, findings 7
- `log4j-core\src\main\java\org\apache\logging\log4j\core\lookup\StrSubstitutor.java`: score 15, findings 7
- `log4j-core\src\main\java\org\apache\logging\log4j\core\filter\StructuredDataFilter.java`: score 15, findings 8

## File Findings
### `log4j-core\src\main\java\org\apache\logging\log4j\core\tools\picocli\CommandLine.java`

- Pre-analysis: classes 118, methods 248, loops 81, streams 0, synchronized blocks 0
#### 1. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: line 584
- Pattern: chatty-io
- What was found: Loop at line 584 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: result.add(execute(parsed));
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Text (line 5144)
- Pattern: algorithmic-waste
- What was found: Loop at line 5144 is nested at depth 5 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 5144
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: assertNoMissingParameters (line 2931)
- Pattern: algorithmic-waste
- What was found: Loop at line 2931 is nested at depth 5 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 2931
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: createDefaultValue (line 4008)
- Pattern: algorithmic-waste
- What was found: Loop at line 4008 is nested at depth 6 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 4008
#### 5. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 2157
- Pattern: algorithmic-waste
- What was found: Loop at line 2157 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 2157
#### 6. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 2296
- Pattern: algorithmic-waste
- What was found: Loop at line 2296 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 2296
#### 7. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 2655
- Pattern: algorithmic-waste
- What was found: Loop at line 2655 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 2655
#### 8. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 2667
- Pattern: algorithmic-waste
- What was found: Loop at line 2667 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 2667
#### 9. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 2744
- Pattern: algorithmic-waste
- What was found: Loop at line 2744 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 2744
#### 10. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 3505
- Pattern: algorithmic-waste
- What was found: Loop at line 3505 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 3505
#### 11. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 3530
- Pattern: algorithmic-waste
- What was found: Loop at line 3530 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 3530
#### 12. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: parse (line 5028)
- Pattern: algorithmic-waste
- What was found: Loop at line 5028 is nested at depth 5 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 5028
#### 13. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: toString (line 4681)
- Pattern: algorithmic-waste
- What was found: Loop at line 4681 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 4681
#### 14. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: toString (line 4681)
- Pattern: data-movement-bloat
- What was found: Loop at line 4681 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: row.append(column.toString()); | text.append(row.toString()).append(System.getProperty("line.separator"));
#### 15. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: Text (line 5144)
- Pattern: repeated-work
- What was found: Loop at line 5144 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: final IStyle[] styles = Style.parse(items[0]);
#### 16. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: line 2157
- Pattern: repeated-work
- What was found: Loop at line 2157 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: commands.get(arg).interpreter.parse(parsedCommands, args, originalArgs);
#### 17. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: Interpreter (line 2022)
- Pattern: allocation-pressure
- What was found: Loop at line 2022 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw new InitializationException("Subcommand " + sub.getName() | "Cannot instantiate subcommand " + sub.getName() + ": the class has no constructor", | "Could not instantiate and add subcommand " + sub.getName() + ": " + ex, ex);
#### 18. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: Interpreter (line 2031)
- Pattern: allocation-pressure
- What was found: Loop at line 2031 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw new InitializationException("Subcommand " + sub.getName() | "Cannot instantiate subcommand " + sub.getName() + ": the class has no constructor", | "Could not instantiate and add subcommand " + sub.getName() + ": " + ex, ex);
#### 19. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 1916
- Pattern: allocation-pressure
- What was found: Loop at line 1916 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: "A field can be either @Option or @Parameters, but '" + field.getName() + "' is both.");
#### 20. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 2296
- Pattern: allocation-pressure
- What was found: Loop at line 2296 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: "args[" + indexRange + "] at position " + position);
#### 21. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 2594
- Pattern: allocation-pressure
- What was found: Loop at line 2594 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: "Value for option " + optionDescription("", field, 0) | + " should be in KEY=VALUE format but was " + value); | "Value for option " + optionDescription("", field, 0) + " should be in KEY=VALUE["
#### 22. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: renderParameterLabel (line 4238)
- Pattern: allocation-pressure
- What was found: Loop at line 4238 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: result = result.append("[" + sep).append(paramName);
#### 23. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: validatePositionalParameters (line 1953)
- Pattern: allocation-pressure
- What was found: Loop at line 1953 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw new ParameterIndexGapException("Missing field annotated with @Parameter(index=" + min | + "). Nearest field '" + field.getName() + "' has index=" + index.min);

### `log4j-core\src\main\java\org\apache\logging\log4j\core\script\ScriptManager.java`

- Pre-analysis: classes 5, methods 17, loops 4, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: addScript (line 150)
- Pattern: concurrency-misuse
- What was found: Line 150 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: scriptRunners.put(script.getId(), new ThreadLocalScriptRunner(script));
#### 2. Direct thread creation
- Severity: High
- Confidence: High
- Location: fileModified (line 191)
- Pattern: concurrency-misuse
- What was found: Line 191 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: scriptRunners.put(script.getId(), new ThreadLocalScriptRunner(script));
#### 3. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 276
- Pattern: concurrency-misuse
- What was found: Line 276 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: private final ThreadLocal<MainScriptRunner> runners = new ThreadLocal<MainScriptRunner>() {
#### 4. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: line 88
- Pattern: allocation-pressure
- What was found: Loop at line 88 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: final StringBuilder names = new StringBuilder();
#### 5. List membership checks inside loop
- Severity: Medium
- Confidence: Medium
- Location: line 95
- Pattern: algorithmic-waste
- What was found: Loop at line 95 performs `.contains(...)` checks that may scan collections repeatedly.
- Why it is wasteful: Repeated linear scans inside iteration can push runtime toward O(n^2) as data sets grow.
- Likely impact: Throughput degradation and elevated CPU time for larger inputs.
- Recommended remediation: Use a `Set` for membership lookups or pre-index data before the loop.
- Low-waste rationale: Indexing once avoids repeated scans and reduces wasted CPU work.
- Evidence: line 95
#### 6. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 123
- Pattern: algorithmic-waste
- What was found: Loop at line 123 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 123
#### 7. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 124
- Pattern: algorithmic-waste
- What was found: Loop at line 124 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 124
#### 8. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 88
- Pattern: algorithmic-waste
- What was found: Loop at line 88 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 88
#### 9. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 95
- Pattern: algorithmic-waste
- What was found: Loop at line 95 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 95
#### 10. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: line 88
- Pattern: repeated-work
- What was found: Loop at line 88 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: final StringBuilder names = new StringBuilder();

### `log4j-core\src\main\java\org\apache\logging\log4j\core\layout\Rfc5424Layout.java`

- Pre-analysis: classes 4, methods 55, loops 16, streams 0, synchronized blocks 2
#### 1. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: escapeSDParams (line 591)
- Pattern: allocation-pressure
- What was found: Loop at line 591 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: output = new StringBuilder(value.substring(0, i));
#### 2. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: format (line 913)
- Pattern: allocation-pressure
- What was found: Loop at line 913 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: final StringBuilder buffer = new StringBuilder();
#### 3. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: line 224
- Pattern: allocation-pressure
- What was found: Loop at line 224 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: final Map<String, List<PatternFormatter>> sdParams = new HashMap<>();
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: checkRequired (line 565)
- Pattern: algorithmic-waste
- What was found: Loop at line 565 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 565
#### 5. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: format (line 913)
- Pattern: data-movement-bloat
- What was found: Loop at line 913 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: map.put(entry.getKey(), buffer.toString());
#### 6. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: line 224
- Pattern: data-movement-bloat
- What was found: Loop at line 224 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: sdIdMap.put(key.toString(), fieldFormatter);
#### 7. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: escapeSDParams (line 591)
- Pattern: repeated-work
- What was found: Loop at line 591 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: output = new StringBuilder(value.substring(0, i));
#### 8. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: format (line 913)
- Pattern: repeated-work
- What was found: Loop at line 913 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: final StringBuilder buffer = new StringBuilder();
#### 9. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: line 224
- Pattern: repeated-work
- What was found: Loop at line 224 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: final Map<String, List<PatternFormatter>> sdParams = new HashMap<>(); | final List<PatternFormatter> formatters = fieldParser.parse(entry.getValue());
#### 10. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: line 231
- Pattern: repeated-work
- What was found: Loop at line 231 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: final List<PatternFormatter> formatters = fieldParser.parse(entry.getValue());
#### 11. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: checkRequired (line 565)
- Pattern: allocation-pressure
- What was found: Loop at line 565 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw new LoggingException("Required key " + key + " is missing from the " + mdcId);

### `log4j-core\src\main\java\org\apache\logging\log4j\core\config\composite\DefaultMergeStrategy.java`

- Pre-analysis: classes 1, methods 6, loops 13, streams 0, synchronized blocks 0
#### 1. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: mergConfigurations (line 129)
- Pattern: allocation-pressure
- What was found: Loop at line 129 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: final Map<String, Node> targetLoggers = new HashMap<>();
#### 2. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: mergConfigurations (line 132)
- Pattern: allocation-pressure
- What was found: Loop at line 132 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: final Map<String, Node> targetLoggers = new HashMap<>();
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: getLoggerNode (line 246)
- Pattern: algorithmic-waste
- What was found: Loop at line 246 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 246
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: mergConfigurations (line 129)
- Pattern: algorithmic-waste
- What was found: Loop at line 129 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 129
#### 5. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: mergConfigurations (line 132)
- Pattern: algorithmic-waste
- What was found: Loop at line 132 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 132
#### 6. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: mergConfigurations (line 150)
- Pattern: algorithmic-waste
- What was found: Loop at line 150 is nested at depth 6 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 150
#### 7. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: mergConfigurations (line 151)
- Pattern: algorithmic-waste
- What was found: Loop at line 151 is nested at depth 7 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 151
#### 8. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: mergConfigurations (line 169)
- Pattern: algorithmic-waste
- What was found: Loop at line 169 is nested at depth 6 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 169
#### 9. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: mergConfigurations (line 129)
- Pattern: repeated-work
- What was found: Loop at line 129 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: final Map<String, Node> targetLoggers = new HashMap<>();
#### 10. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: mergConfigurations (line 132)
- Pattern: repeated-work
- What was found: Loop at line 132 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: final Map<String, Node> targetLoggers = new HashMap<>();

### `log4j-core\src\main\java\org\apache\logging\log4j\core\appender\rolling\DefaultRolloverStrategy.java`

- Pre-analysis: classes 2, methods 37, loops 4, streams 0, synchronized blocks 0
#### 1. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: purgeAscending (line 546)
- Pattern: chatty-io
- What was found: Loop at line 546 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: if (!action.execute()) {
#### 2. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: purgeDescending (line 603)
- Pattern: chatty-io
- What was found: Loop at line 603 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: if (!action.execute()) {
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: purgeAscending (line 531)
- Pattern: algorithmic-waste
- What was found: Loop at line 531 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 531
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: purgeDescending (line 591)
- Pattern: algorithmic-waste
- What was found: Loop at line 591 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 591
#### 5. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: purgeAscending (line 546)
- Pattern: data-movement-bloat
- What was found: Loop at line 546 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: String renameTo = buf.toString();
#### 6. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: purgeDescending (line 603)
- Pattern: data-movement-bloat
- What was found: Loop at line 603 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: String renameTo = buf.toString();
#### 7. Repeated logging inside loop
- Severity: Low
- Confidence: High
- Location: purgeAscending (line 531)
- Pattern: chatty-io
- What was found: Loop at line 531 logs on the hot iteration path.
- Why it is wasteful: Per-item logging adds formatting work and I/O overhead that can dominate lightweight loops.
- Likely impact: Lower throughput and larger log volumes for routine processing paths.
- Recommended remediation: Log summaries outside the loop or guard verbose logs behind debug checks.
- Low-waste rationale: Reducing log volume cuts bytes written and CPU spent formatting low-value output.
- Evidence: LOGGER.debug("Eligible files: {}", eligibleFiles); | LOGGER.debug("Deleting {}", eligibleFiles.get(key).toFile().getAbsolutePath()); | LOGGER.error("Unable to delete {}, {}", eligibleFiles.firstKey(), ioe.getMessage(), ioe);
#### 8. Repeated logging inside loop
- Severity: Low
- Confidence: High
- Location: purgeAscending (line 546)
- Pattern: chatty-io
- What was found: Loop at line 546 logs on the hot iteration path.
- Why it is wasteful: Per-item logging adds formatting work and I/O overhead that can dominate lightweight loops.
- Likely impact: Lower throughput and larger log volumes for routine processing paths.
- Recommended remediation: Log summaries outside the loop or guard verbose logs behind debug checks.
- Low-waste rationale: Reducing log volume cuts bytes written and CPU spent formatting low-value output.
- Evidence: LOGGER.debug("DefaultRolloverStrategy.purgeAscending executing {}", action); | LOGGER.warn("Exception during purge in RollingFileAppender", ex);
#### 9. Repeated logging inside loop
- Severity: Low
- Confidence: High
- Location: purgeDescending (line 591)
- Pattern: chatty-io
- What was found: Loop at line 591 logs on the hot iteration path.
- Why it is wasteful: Per-item logging adds formatting work and I/O overhead that can dominate lightweight loops.
- Likely impact: Lower throughput and larger log volumes for routine processing paths.
- Recommended remediation: Log summaries outside the loop or guard verbose logs behind debug checks.
- Low-waste rationale: Reducing log volume cuts bytes written and CPU spent formatting low-value output.
- Evidence: LOGGER.debug("Deleting {}", eligibleFiles.get(key).toFile().getAbsolutePath()); | LOGGER.error("Unable to delete {}, {}", eligibleFiles.firstKey(), ioe.getMessage(), ioe);
#### 10. Repeated logging inside loop
- Severity: Low
- Confidence: High
- Location: purgeDescending (line 603)
- Pattern: chatty-io
- What was found: Loop at line 603 logs on the hot iteration path.
- Why it is wasteful: Per-item logging adds formatting work and I/O overhead that can dominate lightweight loops.
- Likely impact: Lower throughput and larger log volumes for routine processing paths.
- Recommended remediation: Log summaries outside the loop or guard verbose logs behind debug checks.
- Low-waste rationale: Reducing log volume cuts bytes written and CPU spent formatting low-value output.
- Evidence: LOGGER.debug("DefaultRolloverStrategy.purgeDescending executing {}", action); | LOGGER.warn("Exception during purge in RollingFileAppender", ex);

### `log4j-core\src\main\java\org\apache\logging\log4j\core\filter\MapFilter.java`

- Pre-analysis: classes 1, methods 8, loops 6, streams 0, synchronized blocks 0
#### 1. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: line 315
- Pattern: allocation-pressure
- What was found: Loop at line 315 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: list = new ArrayList<>();
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: filter (line 111)
- Pattern: algorithmic-waste
- What was found: Loop at line 111 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 111
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: filter (line 85)
- Pattern: algorithmic-waste
- What was found: Loop at line 85 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 85
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: filter (line 98)
- Pattern: algorithmic-waste
- What was found: Loop at line 98 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 98
#### 5. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 315
- Pattern: algorithmic-waste
- What was found: Loop at line 315 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 315
#### 6. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: toString (line 269)
- Pattern: algorithmic-waste
- What was found: Loop at line 269 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 269
#### 7. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: toString (line 269)
- Pattern: data-movement-bloat
- What was found: Loop at line 269 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: final String value = list.size() > 1 ? list.get(0) : list.toString();
#### 8. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: line 315
- Pattern: repeated-work
- What was found: Loop at line 315 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: list = new ArrayList<>();
#### 9. Repeated logging inside loop
- Severity: Low
- Confidence: High
- Location: line 315
- Pattern: chatty-io
- What was found: Loop at line 315 logs on the hot iteration path.
- Why it is wasteful: Per-item logging adds formatting work and I/O overhead that can dominate lightweight loops.
- Likely impact: Lower throughput and larger log volumes for routine processing paths.
- Recommended remediation: Log summaries outside the loop or guard verbose logs behind debug checks.
- Low-waste rationale: Reducing log volume cuts bytes written and CPU spent formatting low-value output.
- Evidence: LOGGER.error("A null key is not valid in MapFilter"); | LOGGER.error("A null value for key " + key + " is not allowed in MapFilter");
#### 10. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 315
- Pattern: allocation-pressure
- What was found: Loop at line 315 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: LOGGER.error("A null value for key " + key + " is not allowed in MapFilter");

### `log4j-api\src\main\java\org\apache\logging\log4j\util\Unbox.java`

- Pre-analysis: classes 5, methods 17, loops 2, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 108
- Pattern: concurrency-misuse
- What was found: Line 108 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: private static ThreadLocal<State> threadLocalState = new ThreadLocal<>();
#### 2. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 71
- Pattern: concurrency-misuse
- What was found: Line 71 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: private final ThreadLocal<StringBuilder[]> ringBuffer = new ThreadLocal<>();
#### 3. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 72
- Pattern: concurrency-misuse
- What was found: Line 72 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: private final ThreadLocal<int[]> current = new ThreadLocal<>();
#### 4. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: State (line 96)
- Pattern: allocation-pressure
- What was found: Loop at line 96 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: ringBuffer[i] = new StringBuilder(21);
#### 5. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: getStringBuilder (line 78)
- Pattern: allocation-pressure
- What was found: Loop at line 78 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: array[i] = new StringBuilder(21);
#### 6. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: State (line 96)
- Pattern: repeated-work
- What was found: Loop at line 96 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: ringBuffer[i] = new StringBuilder(21);
#### 7. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: getStringBuilder (line 78)
- Pattern: repeated-work
- What was found: Loop at line 78 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: array[i] = new StringBuilder(21);

### `log4j-core\src\main\java\org\apache\logging\log4j\core\net\TcpSocketManager.java`

- Pre-analysis: classes 5, methods 19, loops 5, streams 0, synchronized blocks 3
#### 1. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: errorMessage (line 604)
- Pattern: chatty-io
- What was found: Loop at line 604 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: for (int i = 0; i < socketAddresses.size(); ++i) { | sb.append(socketAddresses.get(i).getAddress().getHostAddress()); | sb.append(":").append(socketAddresses.get(i).getPort());
#### 2. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: line 409
- Pattern: chatty-io
- What was found: Loop at line 409 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: for (InetSocketAddress socketAddress : socketAddresses) { | LOGGER.debug("Reconnecting " + socketAddress); | connect(socketAddress);
#### 3. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: line 583
- Pattern: chatty-io
- What was found: Loop at line 583 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: for (InetSocketAddress socketAddress : socketAddresses) { | return TcpSocketManager.createSocket(socketAddress, data.socketOptions, data.connectTimeoutMillis);
#### 4. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: line 634
- Pattern: chatty-io
- What was found: Loop at line 634 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: socketAddresses.add(new InetSocketAddress(address, port));
#### 5. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: errorMessage (line 604)
- Pattern: algorithmic-waste
- What was found: Loop at line 604 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 604
#### 6. Repeated logging inside loop
- Severity: Low
- Confidence: High
- Location: run (line 386)
- Pattern: chatty-io
- What was found: Loop at line 386 logs on the hot iteration path.
- Why it is wasteful: Per-item logging adds formatting work and I/O overhead that can dominate lightweight loops.
- Likely impact: Lower throughput and larger log volumes for routine processing paths.
- Recommended remediation: Log summaries outside the loop or guard verbose logs behind debug checks.
- Low-waste rationale: Reducing log volume cuts bytes written and CPU spent formatting low-value output.
- Evidence: LOGGER.debug("Reconnection interrupted."); | LOGGER.debug("{}:{} refused connection", host, port); | LOGGER.debug("Unable to reconnect to {}:{}", host, port);
#### 7. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 409
- Pattern: allocation-pressure
- What was found: Loop at line 409 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: LOGGER.debug("Reconnecting " + socketAddress);

### `log4j-core\src\main\java\org\apache\logging\log4j\core\filter\StructuredDataFilter.java`

- Pre-analysis: classes 1, methods 6, loops 4, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 48
- Pattern: concurrency-misuse
- What was found: Line 48 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: private static ThreadLocal<StringBuilder> threadLocalStringBuilder = new ThreadLocal<>();
#### 2. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: line 168
- Pattern: allocation-pressure
- What was found: Loop at line 168 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: list = new ArrayList<>();
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 168
- Pattern: algorithmic-waste
- What was found: Loop at line 168 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 168
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: listContainsValue (line 128)
- Pattern: algorithmic-waste
- What was found: Loop at line 128 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 128
#### 5. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: listContainsValue (line 135)
- Pattern: algorithmic-waste
- What was found: Loop at line 135 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 135
#### 6. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: line 168
- Pattern: repeated-work
- What was found: Loop at line 168 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: list = new ArrayList<>();
#### 7. Repeated logging inside loop
- Severity: Low
- Confidence: High
- Location: line 168
- Pattern: chatty-io
- What was found: Loop at line 168 logs on the hot iteration path.
- Why it is wasteful: Per-item logging adds formatting work and I/O overhead that can dominate lightweight loops.
- Likely impact: Lower throughput and larger log volumes for routine processing paths.
- Recommended remediation: Log summaries outside the loop or guard verbose logs behind debug checks.
- Low-waste rationale: Reducing log volume cuts bytes written and CPU spent formatting low-value output.
- Evidence: LOGGER.error("A null key is not valid in MapFilter"); | LOGGER.error("A null value for key " + key + " is not allowed in MapFilter");
#### 8. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 168
- Pattern: allocation-pressure
- What was found: Loop at line 168 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: LOGGER.error("A null value for key " + key + " is not allowed in MapFilter");

### `log4j-core\src\main\java\org\apache\logging\log4j\core\lookup\StrSubstitutor.java`

- Pre-analysis: classes 8, methods 59, loops 7, streams 0, synchronized blocks 0
#### 1. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: line 1033
- Pattern: chatty-io
- What was found: Loop at line 1033 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: buf.deleteCharAt(pos - 1);
#### 2. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: line 1033
- Pattern: allocation-pressure
- What was found: Loop at line 1033 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: priorVariables = new ArrayList<>(); | final StringBuilder bufName = new StringBuilder(varNameExpr); | priorVariables = new ArrayList<>();
#### 3. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: line 1051
- Pattern: allocation-pressure
- What was found: Loop at line 1051 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: priorVariables = new ArrayList<>(); | final StringBuilder bufName = new StringBuilder(varNameExpr); | priorVariables = new ArrayList<>();
#### 4. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: line 1033
- Pattern: data-movement-bloat
- What was found: Loop at line 1033 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: varNameExpr = bufName.toString();
#### 5. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: line 1051
- Pattern: data-movement-bloat
- What was found: Loop at line 1051 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: varNameExpr = bufName.toString();
#### 6. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: line 1033
- Pattern: repeated-work
- What was found: Loop at line 1033 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: priorVariables = new ArrayList<>(); | final StringBuilder bufName = new StringBuilder(varNameExpr); | priorVariables = new ArrayList<>();
#### 7. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: line 1051
- Pattern: repeated-work
- What was found: Loop at line 1051 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: priorVariables = new ArrayList<>(); | final StringBuilder bufName = new StringBuilder(varNameExpr); | priorVariables = new ArrayList<>();

### `log4j-core\src\main\java\org\apache\logging\log4j\core\config\AbstractConfiguration.java`

- Pre-analysis: classes 5, methods 64, loops 29, streams 0, synchronized blocks 10
#### 1. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: doConfigure (line 729)
- Pattern: allocation-pressure
- What was found: Loop at line 729 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: final List<CustomLevelConfig> copy = new ArrayList<>(customLevels);
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: doConfigure (line 788)
- Pattern: algorithmic-waste
- What was found: Loop at line 788 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 788
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: doConfigure (line 790)
- Pattern: algorithmic-waste
- What was found: Loop at line 790 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 790
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: getLoggerConfig (line 1051)
- Pattern: algorithmic-waste
- What was found: Loop at line 1051 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1051
#### 5. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: doConfigure (line 729)
- Pattern: repeated-work
- What was found: Loop at line 729 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: final List<CustomLevelConfig> copy = new ArrayList<>(customLevels);
#### 6. Repeated logging inside loop
- Severity: Low
- Confidence: High
- Location: processConditionals (line 601)
- Pattern: chatty-io
- What was found: Loop at line 601 logs on the hot iteration path.
- Why it is wasteful: Per-item logging adds formatting work and I/O overhead that can dominate lightweight loops.
- Likely impact: Lower throughput and larger log volumes for routine processing paths.
- Recommended remediation: Log summaries outside the loop or guard verbose logs behind debug checks.
- Low-waste rationale: Reducing log volume cuts bytes written and CPU spent formatting low-value output.
- Evidence: LOGGER.error( | LOGGER.error(
#### 7. Repeated logging inside loop
- Severity: Low
- Confidence: High
- Location: processSelect (line 654)
- Pattern: chatty-io
- What was found: Loop at line 654 logs on the hot iteration path.
- Why it is wasteful: Per-item logging adds formatting work and I/O overhead that can dominate lightweight loops.
- Likely impact: Lower throughput and larger log volumes for routine processing paths.
- Recommended remediation: Log summaries outside the loop or guard verbose logs behind debug checks.
- Low-waste rationale: Reducing log volume cuts bytes written and CPU spent formatting low-value output.
- Evidence: LOGGER.error("Invalid Node {} for Select. Must be a Condition", child.getName()); | LOGGER.error("No PluginType for node {}", child.getName());
#### 8. Repeated logging inside loop
- Severity: Low
- Confidence: High
- Location: setParents (line 1238)
- Pattern: chatty-io
- What was found: Loop at line 1238 logs on the hot iteration path.
- Why it is wasteful: Per-item logging adds formatting work and I/O overhead that can dominate lightweight loops.
- Likely impact: Lower throughput and larger log volumes for routine processing paths.
- Recommended remediation: Log summaries outside the loop or guard verbose logs behind debug checks.
- Low-waste rationale: Reducing log volume cuts bytes written and CPU spent formatting low-value output.
- Evidence: logger.setParent(parent); | logger.setParent(root);
#### 9. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: preConfigure (line 576)
- Pattern: allocation-pressure
- What was found: Loop at line 576 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: LOGGER.error("Unable to locate plugin type for " + child.getName());

### `log4j-1.2-api\src\main\java\org\apache\log4j\PropertyConfigurator.java`

- Pre-analysis: classes 6, methods 26, loops 9, streams 0, synchronized blocks 1
#### 1. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: parseCatsAndRenderers (line 610)
- Pattern: chatty-io
- What was found: Loop at line 610 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: final Logger logger = loggerRepository.getLogger(loggerName, loggerFactory); | if (loggerRepository instanceof RendererSupport) { | RendererMap.addRenderer((RendererSupport) loggerRepository, renderedClass, renderingClass);
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: SortedKeyEnumeration (line 101)
- Pattern: algorithmic-waste
- What was found: Loop at line 101 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 101
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: SortedKeyEnumeration (line 99)
- Pattern: algorithmic-waste
- What was found: Loop at line 99 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 99
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: parseAppenderFilters (line 489)
- Pattern: algorithmic-waste
- What was found: Loop at line 489 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 489
#### 5. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: parseAppenderFilters (line 514)
- Pattern: algorithmic-waste
- What was found: Loop at line 514 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 514
#### 6. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 588
- Pattern: allocation-pressure
- What was found: Loop at line 588 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: LogLog.debug("Parsing appender named \"" + appenderName + "\".");
#### 7. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: parseAppenderFilters (line 514)
- Pattern: allocation-pressure
- What was found: Loop at line 514 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: LogLog.debug("Filter key: [" + key + "] class: [" + properties.getProperty(key) + "] props: " | LogLog.debug("Adding filter of type [" + filter.getClass() + "] to appender named [" | LogLog.warn("Missing class definition for filter: [" + key + "]");

### `log4j-core\src\main\java\org\apache\logging\log4j\core\filter\ThreadContextMapFilter.java`

- Pre-analysis: classes 1, methods 3, loops 2, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 313
- Pattern: concurrency-misuse
- What was found: Line 313 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: return new ThreadContextMapFilter(map, isAnd, match, mismatch);
#### 2. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: line 288
- Pattern: allocation-pressure
- What was found: Loop at line 288 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: list = new ArrayList<>();
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: filter (line 113)
- Pattern: algorithmic-waste
- What was found: Loop at line 113 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 113
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 288
- Pattern: algorithmic-waste
- What was found: Loop at line 288 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 288
#### 5. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: line 288
- Pattern: repeated-work
- What was found: Loop at line 288 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: list = new ArrayList<>();
#### 6. Repeated logging inside loop
- Severity: Low
- Confidence: High
- Location: line 288
- Pattern: chatty-io
- What was found: Loop at line 288 logs on the hot iteration path.
- Why it is wasteful: Per-item logging adds formatting work and I/O overhead that can dominate lightweight loops.
- Likely impact: Lower throughput and larger log volumes for routine processing paths.
- Recommended remediation: Log summaries outside the loop or guard verbose logs behind debug checks.
- Low-waste rationale: Reducing log volume cuts bytes written and CPU spent formatting low-value output.
- Evidence: LOGGER.error("A null key is not valid in MapFilter"); | LOGGER.error("A null value for key " + key + " is not allowed in MapFilter");
#### 7. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 288
- Pattern: allocation-pressure
- What was found: Loop at line 288 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: LOGGER.error("A null value for key " + key + " is not allowed in MapFilter");

### `log4j-core\src\main\java\org\apache\logging\log4j\core\pattern\PatternParser.java`

- Pre-analysis: classes 4, methods 4, loops 11, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: extractOptions (line 619)
- Pattern: algorithmic-waste
- What was found: Loop at line 619 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 619
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 138
- Pattern: algorithmic-waste
- What was found: Loop at line 138 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 138
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 147
- Pattern: algorithmic-waste
- What was found: Loop at line 147 is nested at depth 5 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 147
#### 4. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: extractOptions (line 384)
- Pattern: data-movement-bloat
- What was found: Loop at line 384 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: literalPattern(currentLiteral.toString(), convertBackslashes));
#### 5. Repeated logging inside loop
- Severity: Low
- Confidence: High
- Location: line 138
- Pattern: chatty-io
- What was found: Loop at line 138 logs on the hot iteration path.
- Why it is wasteful: Per-item logging adds formatting work and I/O overhead that can dominate lightweight loops.
- Likely impact: Lower throughput and larger log volumes for routine processing paths.
- Recommended remediation: Log summaries outside the loop or guard verbose logs behind debug checks.
- Low-waste rationale: Reducing log volume cuts bytes written and CPU spent formatting low-value output.
- Evidence: LOGGER.warn( | LOGGER.error("Error processing plugin " + type.getElementName(), ex);
#### 6. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: extractOptions (line 384)
- Pattern: allocation-pressure
- What was found: Loop at line 384 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: LOGGER.error("Error occurred in position " + i | + ".\n Was expecting digit, instead got char \"" + c + "\".");
#### 7. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: extractOptions (line 637)
- Pattern: allocation-pressure
- What was found: Loop at line 637 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: LOGGER.error("Class " + converterClass + " cannot contain multiple static newInstance methods");
#### 8. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: extractOptions (line 661)
- Pattern: allocation-pressure
- What was found: Loop at line 661 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: LOGGER.error("Unknown parameter type " + clazz.getName() + " for static newInstance method of "
#### 9. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 138
- Pattern: allocation-pressure
- What was found: Loop at line 138 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: LOGGER.error("Error processing plugin " + type.getElementName(), ex);

### `log4j-core\src\main\java\org\apache\logging\log4j\core\async\JCToolsBlockingQueueFactory.java`

- Pre-analysis: classes 4, methods 9, loops 4, streams 0, synchronized blocks 0
#### 1. Polling loop without blocking
- Severity: High
- Confidence: Medium
- Location: line 103
- Pattern: idle-compute
- What was found: while loop at line 103 appears to poll shared state without a blocking primitive.
- Why it is wasteful: A polling loop repeatedly burns CPU to recheck readiness instead of sleeping until useful work can continue.
- Likely impact: Higher CPU utilization, thermal pressure, and reduced throughput for other work on the same host.
- Recommended remediation: Replace polling with a blocking primitive, callback, latch, queue, or at least bounded backoff.
- Low-waste rationale: Blocking or event-driven coordination cuts useless instructions and improves value per watt.
- Evidence: line 103
#### 2. Polling loop without blocking
- Severity: High
- Confidence: Medium
- Location: line 115
- Pattern: idle-compute
- What was found: while loop at line 115 appears to poll shared state without a blocking primitive.
- Why it is wasteful: A polling loop repeatedly burns CPU to recheck readiness instead of sleeping until useful work can continue.
- Likely impact: Higher CPU utilization, thermal pressure, and reduced throughput for other work on the same host.
- Recommended remediation: Replace polling with a blocking primitive, callback, latch, queue, or at least bounded backoff.
- Low-waste rationale: Blocking or event-driven coordination cuts useless instructions and improves value per watt.
- Evidence: line 115
#### 3. Polling loop without blocking
- Severity: High
- Confidence: Medium
- Location: line 139
- Pattern: idle-compute
- What was found: while loop at line 139 appears to poll shared state without a blocking primitive.
- Why it is wasteful: A polling loop repeatedly burns CPU to recheck readiness instead of sleeping until useful work can continue.
- Likely impact: Higher CPU utilization, thermal pressure, and reduced throughput for other work on the same host.
- Recommended remediation: Replace polling with a blocking primitive, callback, latch, queue, or at least bounded backoff.
- Low-waste rationale: Blocking or event-driven coordination cuts useless instructions and improves value per watt.
- Evidence: line 139
#### 4. Polling loop without blocking
- Severity: High
- Confidence: Medium
- Location: line 87
- Pattern: idle-compute
- What was found: while loop at line 87 appears to poll shared state without a blocking primitive.
- Why it is wasteful: A polling loop repeatedly burns CPU to recheck readiness instead of sleeping until useful work can continue.
- Likely impact: Higher CPU utilization, thermal pressure, and reduced throughput for other work on the same host.
- Recommended remediation: Replace polling with a blocking primitive, callback, latch, queue, or at least bounded backoff.
- Low-waste rationale: Blocking or event-driven coordination cuts useless instructions and improves value per watt.
- Evidence: line 87

### `log4j-core\src\main\java\org\apache\logging\log4j\core\config\json\JsonConfiguration.java`

- Pre-analysis: classes 3, methods 10, loops 10, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: constructNode (line 148)
- Pattern: algorithmic-waste
- What was found: Loop at line 148 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 148
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: constructNode (line 157)
- Pattern: algorithmic-waste
- What was found: Loop at line 157 is nested at depth 5 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 157
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: constructNode (line 170)
- Pattern: algorithmic-waste
- What was found: Loop at line 170 is nested at depth 6 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 170
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: constructNode (line 179)
- Pattern: algorithmic-waste
- What was found: Loop at line 179 is nested at depth 8 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 179
#### 5. Repeated logging inside loop
- Severity: Low
- Confidence: High
- Location: constructNode (line 148)
- Pattern: chatty-io
- What was found: Loop at line 148 logs on the hot iteration path.
- Why it is wasteful: Per-item logging adds formatting work and I/O overhead that can dominate lightweight loops.
- Likely impact: Lower throughput and larger log volumes for routine processing paths.
- Recommended remediation: Log summaries outside the loop or guard verbose logs behind debug checks.
- Low-waste rationale: Reducing log volume cuts bytes written and CPU spent formatting low-value output.
- Evidence: LOGGER.debug("Processing node for array {}", entry.getKey()); | LOGGER.debug("Processing {}[{}]", entry.getKey(), i); | LOGGER.debug("Processing {} {}[{}]", pluginType, entry.getKey(), i);
#### 6. Repeated logging inside loop
- Severity: Low
- Confidence: High
- Location: constructNode (line 157)
- Pattern: chatty-io
- What was found: Loop at line 157 logs on the hot iteration path.
- Why it is wasteful: Per-item logging adds formatting work and I/O overhead that can dominate lightweight loops.
- Likely impact: Lower throughput and larger log volumes for routine processing paths.
- Recommended remediation: Log summaries outside the loop or guard verbose logs behind debug checks.
- Low-waste rationale: Reducing log volume cuts bytes written and CPU spent formatting low-value output.
- Evidence: LOGGER.debug("Processing {}[{}]", entry.getKey(), i); | LOGGER.debug("Processing {} {}[{}]", pluginType, entry.getKey(), i); | LOGGER.debug("Processing node for object {}", itemEntry.getKey());
#### 7. Repeated logging inside loop
- Severity: Low
- Confidence: High
- Location: constructNode (line 170)
- Pattern: chatty-io
- What was found: Loop at line 170 logs on the hot iteration path.
- Why it is wasteful: Per-item logging adds formatting work and I/O overhead that can dominate lightweight loops.
- Likely impact: Lower throughput and larger log volumes for routine processing paths.
- Recommended remediation: Log summaries outside the loop or guard verbose logs behind debug checks.
- Low-waste rationale: Reducing log volume cuts bytes written and CPU spent formatting low-value output.
- Evidence: LOGGER.debug("Processing node for object {}", itemEntry.getKey()); | LOGGER.debug("Processing array for object {}", entryName);
#### 8. Repeated logging inside loop
- Severity: Low
- Confidence: High
- Location: setup (line 110)
- Pattern: chatty-io
- What was found: Loop at line 110 logs on the hot iteration path.
- Why it is wasteful: Per-item logging adds formatting work and I/O overhead that can dominate lightweight loops.
- Likely impact: Lower throughput and larger log volumes for routine processing paths.
- Recommended remediation: Log summaries outside the loop or guard verbose logs behind debug checks.
- Low-waste rationale: Reducing log volume cuts bytes written and CPU spent formatting low-value output.
- Evidence: LOGGER.debug("Processing node for object {}", entry.getKey()); | LOGGER.error("Arrays are not supported at the root configuration.");

### `log4j-perf-test\src\main\java\org\apache\logging\log4j\perf\nogc\ParameterizedMessage.java`

- Pre-analysis: classes 2, methods 37, loops 9, streams 0, synchronized blocks 0
#### 1. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: appendCollection (line 697)
- Pattern: allocation-pressure
- What was found: Loop at line 697 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: recursiveDeepToString(anOCol, str, new HashSet<>(dejaVu));
#### 2. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: appendMap (line 670)
- Pattern: allocation-pressure
- What was found: Loop at line 670 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: recursiveDeepToString(key, str, new HashSet<>(dejaVu)); | recursiveDeepToString(value, str, new HashSet<>(dejaVu));
#### 3. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: line 646
- Pattern: allocation-pressure
- What was found: Loop at line 646 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: recursiveDeepToString(current, str, new HashSet<>(dejaVu));
#### 4. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: appendCollection (line 697)
- Pattern: repeated-work
- What was found: Loop at line 697 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: recursiveDeepToString(anOCol, str, new HashSet<>(dejaVu));
#### 5. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: appendMap (line 670)
- Pattern: repeated-work
- What was found: Loop at line 670 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: recursiveDeepToString(key, str, new HashSet<>(dejaVu)); | recursiveDeepToString(value, str, new HashSet<>(dejaVu));
#### 6. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: line 646
- Pattern: repeated-work
- What was found: Loop at line 646 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: recursiveDeepToString(current, str, new HashSet<>(dejaVu));

### `log4j-1.2-api\src\main\java\org\apache\log4j\config\Log4j1ConfigurationParser.java`

- Pre-analysis: classes 2, methods 20, loops 6, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: buildClassToPropertyPrefixMap (line 150)
- Pattern: algorithmic-waste
- What was found: Loop at line 150 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 150
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: buildLoggers (line 415)
- Pattern: algorithmic-waste
- What was found: Loop at line 415 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 415
#### 3. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: buildClassToPropertyPrefixMap (line 150)
- Pattern: data-movement-bloat
- What was found: Loop at line 150 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: final String key = keyObj.toString().trim(); | map.put(name, value.toString().trim());
#### 4. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: buildLoggers (line 415)
- Pattern: data-movement-bloat
- What was found: Loop at line 415 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: final String key = keyObj.toString().trim(); | final String valueStr = value.toString().trim();
#### 5. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: buildProperties (line 134)
- Pattern: data-movement-bloat
- What was found: Loop at line 134 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: final String key = entry.getKey().toString();
#### 6. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: buildLoggers (line 415)
- Pattern: allocation-pressure
- What was found: Loop at line 415 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: warn("Level is missing for entry " + entry);

### `log4j-core\src\main\java\org\apache\logging\log4j\core\util\CronExpression.java`

- Pre-analysis: classes 2, methods 27, loops 14, streams 0, synchronized blocks 0
#### 1. Polling loop without blocking
- Severity: High
- Confidence: Medium
- Location: getTimeAfter (line 1551)
- Pattern: idle-compute
- What was found: while loop at line 1551 appears to poll shared state without a blocking primitive.
- Why it is wasteful: A polling loop repeatedly burns CPU to recheck readiness instead of sleeping until useful work can continue.
- Likely impact: Higher CPU utilization, thermal pressure, and reduced throughput for other work on the same host.
- Recommended remediation: Replace polling with a blocking primitive, callback, latch, queue, or at least bounded backoff.
- Low-waste rationale: Blocking or event-driven coordination cuts useless instructions and improves value per watt.
- Evidence: line 1551
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: getTimeAfter (line 1173)
- Pattern: algorithmic-waste
- What was found: Loop at line 1173 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1173
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 450
- Pattern: algorithmic-waste
- What was found: Loop at line 450 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 450
#### 4. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: getExpressionSetSummary (line 876)
- Pattern: data-movement-bloat
- What was found: Loop at line 876 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: final String val = iVal.toString();
#### 5. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: getExpressionSetSummary (line 902)
- Pattern: data-movement-bloat
- What was found: Loop at line 902 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: final String val = iVal.toString();

### `log4j-core\src\main\java\org\apache\logging\log4j\core\appender\db\jdbc\JdbcDatabaseManager.java`

- Pre-analysis: classes 6, methods 41, loops 9, streams 0, synchronized blocks 1
#### 1. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: line 868
- Pattern: chatty-io
- What was found: Loop at line 868 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: setStatementObject(j, mapping.getNameKey(), value);
#### 2. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: writeInternal (line 966)
- Pattern: chatty-io
- What was found: Loop at line 966 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: this.statement.setObject(j++, event.getContextData().toMap()); | this.statement.setObject(j++, event.getContextStack().asList()); | this.statement.setObject(
#### 3. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: writeInternal (line 993)
- Pattern: chatty-io
- What was found: Loop at line 993 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: this.statement.setTimestamp(j++, new Timestamp(event.getTimeMillis())); | this.statement.setNString( | this.statement.setString(
#### 4. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 868
- Pattern: allocation-pressure
- What was found: Loop at line 868 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: value instanceof String ? "\"" + value + "\"" : Objects.toString(value, null);

### `log4j-1.2-api\src\main\java\org\apache\log4j\config\PropertiesConfiguration.java`

- Pre-analysis: classes 5, methods 17, loops 6, streams 1, synchronized blocks 0
#### 1. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: parseAppenderFilters (line 571)
- Pattern: allocation-pressure
- What was found: Loop at line 571 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: final List<NameValue> filterOpts = filters.computeIfAbsent(filterKey, k -> new ArrayList<>());
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: parseAppenderFilters (line 571)
- Pattern: algorithmic-waste
- What was found: Loop at line 571 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 571
#### 3. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: parseAppenderFilters (line 571)
- Pattern: repeated-work
- What was found: Loop at line 571 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: final List<NameValue> filterOpts = filters.computeIfAbsent(filterKey, k -> new ArrayList<>());
#### 4. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: parseAppenderFilters (line 589)
- Pattern: repeated-work
- What was found: Loop at line 589 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: filter = manager.parse(clazz, entry.getKey(), props, this, BuilderManager.INVALID_FILTER);
#### 5. Repeated logging inside loop
- Severity: Low
- Confidence: High
- Location: line 434
- Pattern: chatty-io
- What was found: Loop at line 434 logs on the hot iteration path.
- Why it is wasteful: Per-item logging adds formatting work and I/O overhead that can dominate lightweight loops.
- Likely impact: Lower throughput and larger log volumes for routine processing paths.
- Recommended remediation: Log summaries outside the loop or guard verbose logs behind debug checks.
- Low-waste rationale: Reducing log volume cuts bytes written and CPU spent formatting low-value output.
- Evidence: LOGGER.debug("Parsing appender named \"{}\".", appenderName); | LOGGER.debug("Adding appender named [{}] to loggerConfig [{}].", appenderName, loggerConfig.getName()); | LOGGER.debug("Appender named [{}] not found.", appenderName);

### `log4j-1.2-api\src\main\java\org\apache\log4j\helpers\OptionConverter.java`

- Pre-analysis: classes 11, methods 16, loops 3, streams 0, synchronized blocks 0
#### 1. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: line 426
- Pattern: allocation-pressure
- What was found: Loop at line 426 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: final List<String> usedKeys = new ArrayList<>(keys);
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 426
- Pattern: algorithmic-waste
- What was found: Loop at line 426 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 426
#### 3. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: line 426
- Pattern: data-movement-bloat
- What was found: Loop at line 426 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: return sbuf.toString();
#### 4. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: line 426
- Pattern: repeated-work
- What was found: Loop at line 426 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: final List<String> usedKeys = new ArrayList<>(keys);
#### 5. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 426
- Pattern: allocation-pressure
- What was found: Loop at line 426 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: Strings.dquote(val) + " has no closing brace. Opening brace at position " + j + '.');

### `log4j-api\src\main\java\org\apache\logging\log4j\message\ReusableMessageFactory.java`

- Pre-analysis: classes 4, methods 1, loops 0, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 45
- Pattern: concurrency-misuse
- What was found: Line 45 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: private final transient ThreadLocal<ReusableParameterizedMessage> threadLocalParameterized = new ThreadLocal<>();
#### 2. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 46
- Pattern: concurrency-misuse
- What was found: Line 46 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: private final transient ThreadLocal<ReusableSimpleMessage> threadLocalSimpleMessage = new ThreadLocal<>();
#### 3. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 47
- Pattern: concurrency-misuse
- What was found: Line 47 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: private final transient ThreadLocal<ReusableObjectMessage> threadLocalObjectMessage = new ThreadLocal<>();

### `log4j-core\src\main\java\org\apache\logging\log4j\core\config\properties\PropertiesConfigurationBuilder.java`

- Pre-analysis: classes 1, methods 14, loops 14, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: build (line 85)
- Pattern: algorithmic-waste
- What was found: Loop at line 85 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 85
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 199
- Pattern: algorithmic-waste
- What was found: Loop at line 199 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 199
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 370
- Pattern: algorithmic-waste
- What was found: Loop at line 370 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 370
#### 4. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: build (line 130)
- Pattern: allocation-pressure
- What was found: Loop at line 130 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: builder.add(createFilter(name, PropertiesUtil.extractSubset(rootProperties, "filter." + name)));
#### 5. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: build (line 146)
- Pattern: allocation-pressure
- What was found: Loop at line 146 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: appenderName.trim(), PropertiesUtil.extractSubset(rootProperties, "appender." + name)));
#### 6. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: build (line 162)
- Pattern: allocation-pressure
- What was found: Loop at line 162 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: builder.add(createLogger(name, PropertiesUtil.extractSubset(rootProperties, "logger." + name)));

### `log4j-core\src\main\java\org\apache\logging\log4j\core\impl\ContextDataInjectorFactory.java`

- Pre-analysis: classes 4, methods 2, loops 0, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: createDefaultInjector (line 86)
- Pattern: concurrency-misuse
- What was found: Line 86 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: return new ThreadContextDataInjector.ForDefaultThreadContextMap(); // for non StringMap-based context maps
#### 2. Direct thread creation
- Severity: High
- Confidence: High
- Location: createDefaultInjector (line 89)
- Pattern: concurrency-misuse
- What was found: Line 89 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: return new ThreadContextDataInjector.ForCopyOnWriteThreadContextMap();
#### 3. Direct thread creation
- Severity: High
- Confidence: High
- Location: createDefaultInjector (line 91)
- Pattern: concurrency-misuse
- What was found: Line 91 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: return new ThreadContextDataInjector.ForGarbageFreeThreadContextMap();

### `log4j-core\src\main\java\org\apache\logging\log4j\core\util\OptionConverter.java`

- Pre-analysis: classes 7, methods 1, loops 2, streams 0, synchronized blocks 0
#### 1. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: OptionConverter (line 363)
- Pattern: allocation-pressure
- What was found: Loop at line 363 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: final List<String> usedKeys = new ArrayList<>(keys);
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: OptionConverter (line 363)
- Pattern: algorithmic-waste
- What was found: Loop at line 363 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 363
#### 3. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: OptionConverter (line 363)
- Pattern: data-movement-bloat
- What was found: Loop at line 363 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: return sbuf.toString();
#### 4. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: OptionConverter (line 363)
- Pattern: repeated-work
- What was found: Loop at line 363 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: final List<String> usedKeys = new ArrayList<>(keys);
#### 5. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: OptionConverter (line 363)
- Pattern: allocation-pressure
- What was found: Loop at line 363 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: Strings.dquote(val) + " has no closing brace. Opening brace at position " + j + '.');

### `log4j-perf-test\src\main\java\org\apache\logging\log4j\perf\jmh\ThreadsafeDateFormatBenchmark.java`

- Pre-analysis: classes 5, methods 10, loops 0, streams 0, synchronized blocks 2
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 103
- Pattern: concurrency-misuse
- What was found: Line 103 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: private final ThreadLocal<char[]> reusableBuffer = new ThreadLocal<>() {
#### 2. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 43
- Pattern: concurrency-misuse
- What was found: Line 43 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: private final ThreadLocal<SimpleDateFormat> threadLocalSDFormat = new ThreadLocal<>() {
#### 3. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 50
- Pattern: concurrency-misuse
- What was found: Line 50 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: private final ThreadLocal<FormatterSimple> threadLocalCachedSDFormat = new ThreadLocal<>() {

### `log4j-core\src\main\java\org\apache\logging\log4j\core\config\composite\CompositeConfiguration.java`

- Pre-analysis: classes 2, methods 6, loops 7, streams 0, synchronized blocks 0
#### 1. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: setup (line 116)
- Pattern: allocation-pressure
- What was found: Loop at line 116 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: final StringBuilder sb = new StringBuilder();
#### 2. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: setup (line 116)
- Pattern: data-movement-bloat
- What was found: Loop at line 116 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: System.out.println(sb.toString());
#### 3. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: setup (line 116)
- Pattern: repeated-work
- What was found: Loop at line 116 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: final StringBuilder sb = new StringBuilder();
#### 4. Repeated logging inside loop
- Severity: Low
- Confidence: High
- Location: reconfigure (line 149)
- Pattern: chatty-io
- What was found: Loop at line 149 logs on the hot iteration path.
- Why it is wasteful: Per-item logging adds formatting work and I/O overhead that can dominate lightweight loops.
- Likely impact: Lower throughput and larger log volumes for routine processing paths.
- Recommended remediation: Log summaries outside the loop or guard verbose logs behind debug checks.
- Low-waste rationale: Reducing log volume cuts bytes written and CPU spent formatting low-value output.
- Evidence: LOGGER.warn( | LOGGER.warn("Unable to reload configuration {}, changes to it will be ignored", config.getName());
#### 5. Repeated logging inside loop
- Severity: Low
- Confidence: High
- Location: setup (line 116)
- Pattern: chatty-io
- What was found: Loop at line 116 logs on the hot iteration path.
- Why it is wasteful: Per-item logging adds formatting work and I/O overhead that can dominate lightweight loops.
- Likely impact: Lower throughput and larger log volumes for routine processing paths.
- Recommended remediation: Log summaries outside the loop or guard verbose logs behind debug checks.
- Low-waste rationale: Reducing log volume cuts bytes written and CPU spent formatting low-value output.
- Evidence: if (LOGGER.isEnabled(Level.ALL)) { | System.out.println(sb.toString());

### `log4j-core\src\main\java\org\apache\logging\log4j\core\impl\ThreadContextDataInjector.java`

- Pre-analysis: classes 6, methods 1, loops 7, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: initServiceProviders (line 154)
- Pattern: algorithmic-waste
- What was found: Loop at line 154 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 154
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: initServiceProviders (line 204)
- Pattern: algorithmic-waste
- What was found: Loop at line 204 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 204
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: initServiceProviders (line 245)
- Pattern: algorithmic-waste
- What was found: Loop at line 245 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 245
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: initServiceProviders (line 275)
- Pattern: algorithmic-waste
- What was found: Loop at line 275 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 275

### `log4j-layout-template-json\src\main\java\org\apache\logging\log4j\layout\template\json\resolver\TemplateResolvers.java`

- Pre-analysis: classes 16, methods 1, loops 4, streams 2, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: TemplateResolvers (line 101)
- Pattern: algorithmic-waste
- What was found: Loop at line 101 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 101
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: TemplateResolvers (line 176)
- Pattern: algorithmic-waste
- What was found: Loop at line 176 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 176
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: TemplateResolvers (line 345)
- Pattern: algorithmic-waste
- What was found: Loop at line 345 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 345
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: TemplateResolvers (line 362)
- Pattern: algorithmic-waste
- What was found: Loop at line 362 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 362

### `log4j-layout-template-json\src\main\java\org\apache\logging\log4j\layout\template\json\util\JsonWriter.java`

- Pre-analysis: classes 3, methods 62, loops 16, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: writeArray (line 310)
- Pattern: algorithmic-waste
- What was found: Loop at line 310 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 310
#### 2. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: writeArray (line 310)
- Pattern: repeated-work
- What was found: Loop at line 310 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: writeValue(item);
#### 3. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: writeArray (line 473)
- Pattern: repeated-work
- What was found: Loop at line 473 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: writeValue(item);
#### 4. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: writeObject (line 257)
- Pattern: repeated-work
- What was found: Loop at line 257 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: writeValue(value);

### `log4j-perf-test\src\main\java\org\apache\logging\log4j\perf\jmh\instant\InstantPatternFormatterImpactBenchmark.java`

- Pre-analysis: classes 1, methods 9, loops 4, streams 1, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 120
- Pattern: algorithmic-waste
- What was found: Loop at line 120 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 120
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 147
- Pattern: algorithmic-waste
- What was found: Loop at line 147 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 147
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 174
- Pattern: algorithmic-waste
- What was found: Loop at line 174 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 174
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 93
- Pattern: algorithmic-waste
- What was found: Loop at line 93 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 93

### `log4j-1.2-api\src\main\java\org\apache\log4j\pattern\NameAbbreviator.java`

- Pre-analysis: classes 7, methods 11, loops 6, streams 0, synchronized blocks 0
#### 1. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: abbreviate (line 54)
- Pattern: chatty-io
- What was found: Loop at line 54 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: buf.delete(nameStart, pos + 1);
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: abbreviate (line 54)
- Pattern: algorithmic-waste
- What was found: Loop at line 54 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 54
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: getAbbreviator (line 281)
- Pattern: algorithmic-waste
- What was found: Loop at line 281 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 281

### `log4j-core\src\main\java\org\apache\logging\log4j\core\async\TimeoutBlockingWaitStrategy.java`

- Pre-analysis: classes 7, methods 4, loops 2, streams 0, synchronized blocks 3
#### 1. Polling loop without blocking
- Severity: High
- Confidence: Medium
- Location: line 75
- Pattern: idle-compute
- What was found: while loop at line 75 appears to poll shared state without a blocking primitive.
- Why it is wasteful: A polling loop repeatedly burns CPU to recheck readiness instead of sleeping until useful work can continue.
- Likely impact: Higher CPU utilization, thermal pressure, and reduced throughput for other work on the same host.
- Recommended remediation: Replace polling with a blocking primitive, callback, latch, queue, or at least bounded backoff.
- Low-waste rationale: Blocking or event-driven coordination cuts useless instructions and improves value per watt.
- Evidence: line 75
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 75
- Pattern: algorithmic-waste
- What was found: Loop at line 75 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 75
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: synchronized (line 65)
- Pattern: algorithmic-waste
- What was found: Loop at line 65 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 65

### `log4j-core\src\main\java\org\apache\logging\log4j\core\config\plugins\util\PluginRegistry.java`

- Pre-analysis: classes 4, methods 1, loops 4, streams 0, synchronized blocks 1
#### 1. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: PluginRegistry (line 224)
- Pattern: allocation-pressure
- What was found: Loop at line 224 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: newPluginsByCategory.put(categoryLowerCase, list = new ArrayList<>());
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: PluginRegistry (line 224)
- Pattern: algorithmic-waste
- What was found: Loop at line 224 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 224
#### 3. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: PluginRegistry (line 224)
- Pattern: repeated-work
- What was found: Loop at line 224 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: newPluginsByCategory.put(categoryLowerCase, list = new ArrayList<>());
#### 4. Repeated logging inside loop
- Severity: Low
- Confidence: High
- Location: PluginRegistry (line 176)
- Pattern: chatty-io
- What was found: Loop at line 176 logs on the hot iteration path.
- Why it is wasteful: Per-item logging adds formatting work and I/O overhead that can dominate lightweight loops.
- Likely impact: Lower throughput and larger log volumes for routine processing paths.
- Recommended remediation: Log summaries outside the loop or guard verbose logs behind debug checks.
- Low-waste rationale: Reducing log volume cuts bytes written and CPU spent formatting low-value output.
- Evidence: LOGGER.info("Plugin [{}] could not be loaded due to missing classes.", className, e); | LOGGER.info("Plugin [{}] could not be loaded due to linkage error.", className, e);

### `log4j-core\src\main\java\org\apache\logging\log4j\core\config\plugins\util\ResolverUtil.java`

- Pre-analysis: classes 16, methods 13, loops 6, streams 0, synchronized blocks 0
#### 1. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: loadImplementationsInDirectory (line 316)
- Pattern: allocation-pressure
- What was found: Loop at line 316 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: builder = new StringBuilder();
#### 2. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: loadImplementationsInDirectory (line 316)
- Pattern: data-movement-bloat
- What was found: Loop at line 316 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: final String packageOrClass = parent == null ? file.getName() : builder.toString();
#### 3. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: loadImplementationsInDirectory (line 316)
- Pattern: repeated-work
- What was found: Loop at line 316 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: builder = new StringBuilder();
#### 4. Repeated logging inside loop
- Severity: Low
- Confidence: High
- Location: findInPackage (line 191)
- Pattern: chatty-io
- What was found: Loop at line 191 logs on the hot iteration path.
- Why it is wasteful: Per-item logging adds formatting work and I/O overhead that can dominate lightweight loops.
- Likely impact: Lower throughput and larger log volumes for routine processing paths.
- Recommended remediation: Log summaries outside the loop or guard verbose logs behind debug checks.
- Low-waste rationale: Reducing log volume cuts bytes written and CPU spent formatting low-value output.
- Evidence: LOGGER.debug("Scanning for classes in '{}' matching criteria {}", urlPath, test); | LOGGER.warn("Could not read entries", ioe);

### `log4j-core\src\main\java\org\apache\logging\log4j\core\tools\Generate.java`

- Pre-analysis: classes 16, methods 7, loops 5, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Generate (line 1044)
- Pattern: algorithmic-waste
- What was found: Loop at line 1044 is nested at depth 5 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1044
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: javadocDescription (line 1149)
- Pattern: algorithmic-waste
- What was found: Loop at line 1149 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1149
#### 3. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: Generate (line 1044)
- Pattern: data-movement-bloat
- What was found: Loop at line 1044 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: System.err.println("Cannot parse custom level '" + values.get(i) + "': " + ex.toString());
#### 4. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: Generate (line 1044)
- Pattern: allocation-pressure
- What was found: Loop at line 1044 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: System.err.println("Cannot parse custom level '" + values.get(i) + "': " + ex.toString());

### `log4j-1.2-api\src\main\java\org\apache\log4j\spi\LocationInfo.java`

- Pre-analysis: classes 3, methods 7, loops 1, streams 0, synchronized blocks 0
#### 1. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: LocationInfo (line 72)
- Pattern: allocation-pressure
- What was found: Loop at line 72 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: final StringBuilder builder = new StringBuilder();
#### 2. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: LocationInfo (line 72)
- Pattern: data-movement-bloat
- What was found: Loop at line 72 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: this.fullInfo = builder.toString();
#### 3. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: LocationInfo (line 72)
- Pattern: repeated-work
- What was found: Loop at line 72 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: final StringBuilder builder = new StringBuilder();

### `log4j-api\src\main\java\org\apache\logging\log4j\message\ThreadDumpMessage.java`

- Pre-analysis: classes 5, methods 13, loops 2, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: readResolve (line 156)
- Pattern: concurrency-misuse
- What was found: Line 156 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: return new ThreadDumpMessage(formattedMsg, title);
#### 2. Direct thread creation
- Severity: High
- Confidence: High
- Location: writeReplace (line 130)
- Pattern: concurrency-misuse
- What was found: Line 130 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: return new ThreadDumpMessageProxy(this);

### `log4j-core\src\main\java\org\apache\logging\log4j\core\appender\rolling\action\CompositeAction.java`

- Pre-analysis: classes 1, methods 5, loops 2, streams 0, synchronized blocks 0
#### 1. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: line 71
- Pattern: chatty-io
- What was found: Loop at line 71 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: if (!action.execute()) {
#### 2. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: line 82
- Pattern: chatty-io
- What was found: Loop at line 82 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: status &= action.execute();

### `log4j-core\src\main\java\org\apache\logging\log4j\core\appender\rolling\RollingFileManager.java`

- Pre-analysis: classes 5, methods 38, loops 4, streams 0, synchronized blocks 5
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 75
- Pattern: concurrency-misuse
- What was found: Line 75 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: /* This executor pool will create a new Thread for every work async action to be performed. Using it allows
#### 2. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 78
- Pattern: concurrency-misuse
- What was found: Line 78 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: new ThreadPoolExecutor(0, Integer.MAX_VALUE, 0, TimeUnit.MILLISECONDS, new EmptyQueue(), threadFactory);

### `log4j-core\src\main\java\org\apache\logging\log4j\core\config\LoggerConfig.java`

- Pre-analysis: classes 8, methods 97, loops 9, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: getProperties (line 600)
- Pattern: algorithmic-waste
- What was found: Loop at line 600 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 600
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 715
- Pattern: algorithmic-waste
- What was found: Loop at line 715 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 715
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: requiresLocation (line 777)
- Pattern: algorithmic-waste
- What was found: Loop at line 777 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 777

### `log4j-core\src\main\java\org\apache\logging\log4j\core\config\plugins\processor\internal\ReachabilityMetadata.java`

- Pre-analysis: classes 6, methods 14, loops 4, streams 0, synchronized blocks 0
#### 1. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: line 225
- Pattern: repeated-work
- What was found: Loop at line 225 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: method.toJson(jsonWriter);
#### 2. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: line 238
- Pattern: repeated-work
- What was found: Loop at line 238 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: field.toJson(jsonWriter);
#### 3. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: line 264
- Pattern: repeated-work
- What was found: Loop at line 264 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: type.toJson(jsonWriter);

### `log4j-core\src\main\java\org\apache\logging\log4j\core\config\plugins\processor\PluginProcessor.java`

- Pre-analysis: classes 4, methods 13, loops 5, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: processBuilderAttribute (line 209)
- Pattern: algorithmic-waste
- What was found: Loop at line 209 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 209
#### 2. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: processBuilderAttribute (line 209)
- Pattern: data-movement-bloat
- What was found: Loop at line 209 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: final String methodName = methodElement.getSimpleName().toString();
#### 3. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: visitType (line 340)
- Pattern: data-movement-bloat
- What was found: Loop at line 340 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: entry.setClassName(elements.getBinaryName(e).toString());

### `log4j-core\src\main\java\org\apache\logging\log4j\core\config\plugins\util\PluginManager.java`

- Pre-analysis: classes 1, methods 10, loops 5, streams 2, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: collectPlugins (line 175)
- Pattern: algorithmic-waste
- What was found: Loop at line 175 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 175
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: collectPlugins (line 183)
- Pattern: algorithmic-waste
- What was found: Loop at line 183 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 183
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 232
- Pattern: algorithmic-waste
- What was found: Loop at line 232 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 232

### `log4j-core\src\main\java\org\apache\logging\log4j\core\impl\JdkMapAdapterStringMap.java`

- Pre-analysis: classes 1, methods 21, loops 3, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: forEach (line 117)
- Pattern: algorithmic-waste
- What was found: Loop at line 117 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 117
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: forEach (line 126)
- Pattern: algorithmic-waste
- What was found: Loop at line 126 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 126
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: toString (line 207)
- Pattern: algorithmic-waste
- What was found: Loop at line 207 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 207

### `log4j-core\src\main\java\org\apache\logging\log4j\core\jmx\Server.java`

- Pre-analysis: classes 2, methods 1, loops 5, streams 0, synchronized blocks 0
#### 1. Executor created in application code path
- Severity: Medium
- Confidence: High
- Location: Server (line 81)
- Pattern: concurrency-misuse
- What was found: Line 81 creates a new executor instance.
- Why it is wasteful: Creating executors per call can fragment thread pools and increase context switching and idle threads.
- Likely impact: Higher memory use, poorer scheduling efficiency, and harder concurrency control.
- Recommended remediation: Reuse a bounded shared executor sized to the workload.
- Low-waste rationale: Bounded executor reuse reduces idle threads and CPU overhead without reducing useful throughput.
- Evidence: ? Executors.newFixedThreadPool(1, Log4jThreadFactory.createDaemonThreadFactory(THREAD_NAME_PREFIX))
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Server (line 357)
- Pattern: algorithmic-waste
- What was found: Loop at line 357 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 357
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Server (line 374)
- Pattern: algorithmic-waste
- What was found: Loop at line 374 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 374

### `log4j-core\src\main\java\org\apache\logging\log4j\core\layout\GelfLayout.java`

- Pre-analysis: classes 5, methods 42, loops 4, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: valueNeedsLookup (line 785)
- Pattern: concurrency-misuse
- What was found: Line 785 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: private static final ThreadLocal<StringBuilder> messageStringBuilder = new ThreadLocal<>();
#### 2. Direct thread creation
- Severity: High
- Confidence: High
- Location: valueNeedsLookup (line 814)
- Pattern: concurrency-misuse
- What was found: Line 814 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: private static final ThreadLocal<StringBuilder> timestampStringBuilder = new ThreadLocal<>();

### `log4j-core\src\main\java\org\apache\logging\log4j\core\layout\ScriptPatternSelector.java`

- Pre-analysis: classes 2, methods 13, loops 7, streams 0, synchronized blocks 0
#### 1. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: line 179
- Pattern: repeated-work
- What was found: Loop at line 179 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: parser.parse(property.getPattern(), alwaysWriteExceptions, disableAnsi, noConsoleNoAnsi);
#### 2. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: line 226
- Pattern: repeated-work
- What was found: Loop at line 226 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: parser.parse(property.getPattern(), alwaysWriteExceptions, disableAnsi, noConsoleNoAnsi);
#### 3. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 179
- Pattern: allocation-pressure
- What was found: Loop at line 179 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw new IllegalArgumentException("Cannot parse pattern '" + property.getPattern() + "'", ex);
#### 4. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 226
- Pattern: allocation-pressure
- What was found: Loop at line 226 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw new IllegalArgumentException("Cannot parse pattern '" + property.getPattern() + "'", ex);

### `log4j-core\src\main\java\org\apache\logging\log4j\core\osgi\Activator.java`

- Pre-analysis: classes 1, methods 6, loops 2, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 64
- Pattern: concurrency-misuse
- What was found: Line 64 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: final ContextDataProvider threadContextProvider = new ThreadContextDataProvider();
#### 2. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: loadContextProviders (line 100)
- Pattern: chatty-io
- What was found: Loop at line 100 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: for (final ServiceReference<ContextDataProvider> serviceReference : serviceReferences) { | final ContextDataProvider provider = bundleContext.getService(serviceReference);

### `log4j-core\src\main\java\org\apache\logging\log4j\core\pattern\CachedDateFormat.java`

- Pre-analysis: classes 2, methods 9, loops 1, streams 0, synchronized blocks 0
#### 1. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: findMillisecondStart (line 197)
- Pattern: allocation-pressure
- What was found: Loop at line 197 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: final StringBuffer formattedMillis = new StringBuffer("ABC");
#### 2. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: findMillisecondStart (line 197)
- Pattern: data-movement-bloat
- What was found: Loop at line 197 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: && formattedMillis.toString().regionMatches(0, formatted, i, magicString.length())
#### 3. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: findMillisecondStart (line 197)
- Pattern: repeated-work
- What was found: Loop at line 197 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: final StringBuffer formattedMillis = new StringBuffer("ABC");

### `log4j-core\src\main\java\org\apache\logging\log4j\core\pattern\HighlightConverter.java`

- Pre-analysis: classes 1, methods 5, loops 2, streams 1, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: createLevelStyleMap (line 154)
- Pattern: algorithmic-waste
- What was found: Loop at line 154 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 154
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: format (line 247)
- Pattern: algorithmic-waste
- What was found: Loop at line 247 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 247
#### 3. Repeated logging inside loop
- Severity: Low
- Confidence: High
- Location: createLevelStyleMap (line 154)
- Pattern: chatty-io
- What was found: Loop at line 154 logs on the hot iteration path.
- Why it is wasteful: Per-item logging adds formatting work and I/O overhead that can dominate lightweight loops.
- Likely impact: Lower throughput and larger log volumes for routine processing paths.
- Recommended remediation: Log summaries outside the loop or guard verbose logs behind debug checks.
- Low-waste rationale: Reducing log volume cuts bytes written and CPU spent formatting low-value output.
- Evidence: LOGGER.error("Unknown level style: " + value + ". Use one of " | LOGGER.warn("Setting style for yet unknown level name {}", key);
#### 4. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: createLevelStyleMap (line 154)
- Pattern: allocation-pressure
- What was found: Loop at line 154 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: LOGGER.error("Unknown level style: " + value + ". Use one of "

### `log4j-core\src\main\java\org\apache\logging\log4j\core\selector\ClassLoaderContextSelector.java`

- Pre-analysis: classes 3, methods 11, loops 3, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: getLoggerContexts (line 176)
- Pattern: algorithmic-waste
- What was found: Loop at line 176 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 176
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 194
- Pattern: algorithmic-waste
- What was found: Loop at line 194 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 194
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: removeContext (line 158)
- Pattern: algorithmic-waste
- What was found: Loop at line 158 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 158

### `log4j-core\src\main\java\org\apache\logging\log4j\core\util\WatchManager.java`

- Pre-analysis: classes 6, methods 25, loops 6, streams 0, synchronized blocks 0
#### 1. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: start (line 294)
- Pattern: chatty-io
- What was found: Loop at line 294 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: for (WatchEventService service : eventServiceList) { | service.subscribe(this);
#### 2. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: stop (line 302)
- Pattern: chatty-io
- What was found: Loop at line 302 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: for (WatchEventService service : eventServiceList) { | service.unsubscribe(this);

### `log4j-layout-template-json\src\main\java\org\apache\logging\log4j\layout\template\json\resolver\ExceptionResolver.java`

- Pre-analysis: classes 1, methods 11, loops 1, streams 0, synchronized blocks 0
#### 1. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: readTruncationPointMatcherRegexes (line 319)
- Pattern: allocation-pressure
- What was found: Loop at line 319 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: Pattern.compile(regex);
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: readTruncationPointMatcherRegexes (line 319)
- Pattern: algorithmic-waste
- What was found: Loop at line 319 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 319
#### 3. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: readTruncationPointMatcherRegexes (line 319)
- Pattern: repeated-work
- What was found: Loop at line 319 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: Pattern.compile(regex);

### `log4j-layout-template-json\src\main\java\org\apache\logging\log4j\layout\template\json\resolver\ThreadContextDataResolverFactory.java`

- Pre-analysis: classes 1, methods 1, loops 0, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: ThreadContextDataResolverFactory (line 44)
- Pattern: concurrency-misuse
- What was found: Line 44 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: return new ThreadContextDataResolver(context, config);
#### 2. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 28
- Pattern: concurrency-misuse
- What was found: Line 28 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: private static final ThreadContextDataResolverFactory INSTANCE = new ThreadContextDataResolverFactory();

### `log4j-layout-template-json\src\main\java\org\apache\logging\log4j\layout\template\json\resolver\ThreadContextStackResolverFactory.java`

- Pre-analysis: classes 1, methods 1, loops 0, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: ThreadContextStackResolverFactory (line 44)
- Pattern: concurrency-misuse
- What was found: Line 44 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: return new ThreadContextStackResolver(config);
#### 2. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 28
- Pattern: concurrency-misuse
- What was found: Line 28 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: private static final ThreadContextStackResolverFactory INSTANCE = new ThreadContextStackResolverFactory();

### `log4j-layout-template-json\src\main\java\org\apache\logging\log4j\layout\template\json\resolver\ThreadResolverFactory.java`

- Pre-analysis: classes 1, methods 1, loops 0, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: ThreadResolverFactory (line 44)
- Pattern: concurrency-misuse
- What was found: Line 44 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: return new ThreadResolver(config);
#### 2. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 28
- Pattern: concurrency-misuse
- What was found: Line 28 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: private static final ThreadResolverFactory INSTANCE = new ThreadResolverFactory();

### `log4j-layout-template-json\src\main\java\org\apache\logging\log4j\layout\template\json\util\ThreadLocalRecyclerFactory.java`

- Pre-analysis: classes 1, methods 1, loops 0, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: ThreadLocalRecyclerFactory (line 34)
- Pattern: concurrency-misuse
- What was found: Line 34 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: return new ThreadLocalRecycler<>(supplier, cleaner);
#### 2. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 24
- Pattern: concurrency-misuse
- What was found: Line 24 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: private static final ThreadLocalRecyclerFactory INSTANCE = new ThreadLocalRecyclerFactory();

### `log4j-1.2-api\src\main\java\org\apache\log4j\helpers\PatternParser.java`

- Pre-analysis: classes 11, methods 24, loops 3, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: convert (line 421)
- Pattern: algorithmic-waste
- What was found: Loop at line 421 is nested at depth 6 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 421
#### 2. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: parse (line 126)
- Pattern: data-movement-bloat
- What was found: Loop at line 126 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: addToList(new LiteralPatternConverter(currentLiteral.toString()));
#### 3. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: parse (line 126)
- Pattern: allocation-pressure
- What was found: Loop at line 126 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: LogLog.error("Error occurred in position " + i + ".\n Was expecting digit, instead got char \""

### `log4j-api\src\main\java\org\apache\logging\log4j\spi\AbstractLogger.java`

- Pre-analysis: classes 13, methods 318, loops 1, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 106
- Pattern: concurrency-misuse
- What was found: Line 106 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: private static final ThreadLocal<int[]> recursionDepthHolder = new ThreadLocal<>(); // LOG4J2-1518, LOG4J2-2031
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: entryMsg (line 724)
- Pattern: algorithmic-waste
- What was found: Loop at line 724 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 724

### `log4j-api\src\main\java\org\apache\logging\log4j\util\PropertiesUtil.java`

- Pre-analysis: classes 6, methods 26, loops 10, streams 2, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: reload (line 504)
- Pattern: concurrency-misuse
- What was found: Line 504 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: private final ThreadLocal<PropertySource> CURRENT_PROPERTY_SOURCE = new ThreadLocal<>();
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: reload (line 658)
- Pattern: algorithmic-waste
- What was found: Loop at line 658 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 658

### `log4j-cassandra\src\main\java\org\apache\logging\log4j\cassandra\CassandraManager.java`

- Pre-analysis: classes 3, methods 5, loops 4, streams 0, synchronized blocks 0
#### 1. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: convertAndAddDefaultPorts (line 252)
- Pattern: chatty-io
- What was found: Loop at line 252 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: for (int i = 0; i < inetSocketAddresses.length; i++) { | inetSocketAddresses[i] = socketAddress.getPort() == 0 | ? new InetSocketAddress(socketAddress.getAddress(), DEFAULT_PORT)
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: writeInternal (line 96)
- Pattern: algorithmic-waste
- What was found: Loop at line 96 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 96

### `log4j-core\src\main\java\org\apache\logging\log4j\core\appender\routing\RoutingAppender.java`

- Pre-analysis: classes 5, methods 38, loops 5, streams 0, synchronized blocks 3
#### 1. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: line 231
- Pattern: data-movement-bloat
- What was found: Loop at line 231 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: error("Multiple default routes. Route " + route.toString() + " will be ignored");
#### 2. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: createAppender (line 367)
- Pattern: allocation-pressure
- What was found: Loop at line 367 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: error("Unable to create Appender of type " + node.getName());
#### 3. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 231
- Pattern: allocation-pressure
- What was found: Loop at line 231 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: error("Multiple default routes. Route " + route.toString() + " will be ignored");
#### 4. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: start (line 260)
- Pattern: allocation-pressure
- What was found: Loop at line 260 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: error("Appender " + route.getAppenderRef() + " cannot be located. Route ignored");

### `log4j-core\src\main\java\org\apache\logging\log4j\core\async\AsyncLogger.java`

- Pre-analysis: classes 5, methods 13, loops 1, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 85
- Pattern: concurrency-misuse
- What was found: Line 85 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: private final ThreadLocal<RingBufferLogEventTranslator> threadLocalTranslator = new ThreadLocal<>();
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: onPropertiesPresent (line 574)
- Pattern: algorithmic-waste
- What was found: Loop at line 574 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 574

### `log4j-core\src\main\java\org\apache\logging\log4j\core\config\ConfigurationFactory.java`

- Pre-analysis: classes 4, methods 21, loops 15, streams 2, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: parseConfigLocations (line 668)
- Pattern: algorithmic-waste
- What was found: Loop at line 668 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 668
#### 2. Repeated logging inside loop
- Severity: Low
- Confidence: High
- Location: getConfiguration (line 641)
- Pattern: chatty-io
- What was found: Loop at line 641 logs on the hot iteration path.
- Why it is wasteful: Per-item logging adds formatting work and I/O overhead that can dominate lightweight loops.
- Likely impact: Lower throughput and larger log volumes for routine processing paths.
- Recommended remediation: Log summaries outside the loop or guard verbose logs behind debug checks.
- Low-waste rationale: Reducing log volume cuts bytes written and CPU spent formatting low-value output.
- Evidence: LOGGER.debug("Loaded configuration from {}", source); | LOGGER.error("Cannot determine the ConfigurationFactory to use for {}", config);
#### 3. Repeated logging inside loop
- Severity: Low
- Confidence: High
- Location: getConfiguration (line 644)
- Pattern: chatty-io
- What was found: Loop at line 644 logs on the hot iteration path.
- Why it is wasteful: Per-item logging adds formatting work and I/O overhead that can dominate lightweight loops.
- Likely impact: Lower throughput and larger log volumes for routine processing paths.
- Recommended remediation: Log summaries outside the loop or guard verbose logs behind debug checks.
- Low-waste rationale: Reducing log volume cuts bytes written and CPU spent formatting low-value output.
- Evidence: LOGGER.debug("Loaded configuration from {}", source); | LOGGER.error("Cannot determine the ConfigurationFactory to use for {}", config);
#### 4. Repeated logging inside loop
- Severity: Low
- Confidence: High
- Location: line 464
- Pattern: chatty-io
- What was found: Loop at line 464 logs on the hot iteration path.
- Why it is wasteful: Per-item logging adds formatting work and I/O overhead that can dominate lightweight loops.
- Likely impact: Lower throughput and larger log volumes for routine processing paths.
- Recommended remediation: Log summaries outside the loop or guard verbose logs behind debug checks.
- Low-waste rationale: Reducing log volume cuts bytes written and CPU spent formatting low-value output.
- Evidence: LOGGER.error("Failed to created configuration at {}", sourceLocation); | LOGGER.warn("Unable to create configuration for {}, ignoring", sourceLocation);

### `log4j-core\src\main\java\org\apache\logging\log4j\core\config\plugins\util\PluginBuilder.java`

- Pre-analysis: classes 4, methods 13, loops 12, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 217
- Pattern: algorithmic-waste
- What was found: Loop at line 217 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 217
#### 2. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: generateParameters (line 277)
- Pattern: allocation-pressure
- What was found: Loop at line 277 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: final String argName = "arg[" + i + "](" + simpleName(value) + ")";
#### 3. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 217
- Pattern: allocation-pressure
- What was found: Loop at line 217 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: reason += "field '" + field.getName() + "' has invalid value '" + value + "'";
#### 4. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 221
- Pattern: allocation-pressure
- What was found: Loop at line 221 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: reason += "field '" + field.getName() + "' has invalid value '" + value + "'";

### `log4j-core\src\main\java\org\apache\logging\log4j\core\config\plugins\visitors\PluginElementVisitor.java`

- Pre-analysis: classes 1, methods 2, loops 3, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 85
- Pattern: algorithmic-waste
- What was found: Loop at line 85 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 85
#### 2. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: line 48
- Pattern: data-movement-bloat
- What was found: Loop at line 48 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: log.append(child.toString());
#### 3. Repeated logging inside loop
- Severity: Low
- Confidence: High
- Location: line 48
- Pattern: chatty-io
- What was found: Loop at line 48 logs on the hot iteration path.
- Why it is wasteful: Per-item logging adds formatting work and I/O overhead that can dominate lightweight loops.
- Likely impact: Lower throughput and larger log volumes for routine processing paths.
- Recommended remediation: Log summaries outside the loop or guard verbose logs behind debug checks.
- Low-waste rationale: Reducing log volume cuts bytes written and CPU spent formatting low-value output.
- Evidence: log.append(", "); | LOGGER.error("Null object returned for {} in {}.", child.getName(), node.getName()); | log.append(Arrays.toString((Object[]) childObject)).append('}');

### `log4j-core\src\main\java\org\apache\logging\log4j\core\layout\LevelPatternSelector.java`

- Pre-analysis: classes 2, methods 11, loops 5, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: getFormatters (line 188)
- Pattern: algorithmic-waste
- What was found: Loop at line 188 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 188
#### 2. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: line 148
- Pattern: repeated-work
- What was found: Loop at line 148 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: parser.parse(property.getPattern(), alwaysWriteExceptions, disableAnsi, noConsoleNoAnsi);
#### 3. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 148
- Pattern: allocation-pressure
- What was found: Loop at line 148 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw new IllegalArgumentException("Cannot parse pattern '" + property.getPattern() + "'", ex);

### `log4j-core\src\main\java\org\apache\logging\log4j\core\layout\MarkerPatternSelector.java`

- Pre-analysis: classes 2, methods 11, loops 5, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: getFormatters (line 188)
- Pattern: algorithmic-waste
- What was found: Loop at line 188 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 188
#### 2. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: line 148
- Pattern: repeated-work
- What was found: Loop at line 148 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: parser.parse(property.getPattern(), alwaysWriteExceptions, disableAnsi, noConsoleNoAnsi);
#### 3. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 148
- Pattern: allocation-pressure
- What was found: Loop at line 148 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw new IllegalArgumentException("Cannot parse pattern '" + property.getPattern() + "'", ex);

### `log4j-core\src\main\java\org\apache\logging\log4j\core\pattern\JAnsiTextRenderer.java`

- Pre-analysis: classes 2, methods 6, loops 4, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 281
- Pattern: algorithmic-waste
- What was found: Loop at line 281 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 281
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: render (line 246)
- Pattern: algorithmic-waste
- What was found: Loop at line 246 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 246
#### 3. Repeated logging inside loop
- Severity: Low
- Confidence: High
- Location: line 281
- Pattern: chatty-io
- What was found: Loop at line 281 logs on the hot iteration path.
- Why it is wasteful: Per-item logging adds formatting work and I/O overhead that can dominate lightweight loops.
- Likely impact: Lower throughput and larger log volumes for routine processing paths.
- Recommended remediation: Log summaries outside the loop or guard verbose logs behind debug checks.
- Low-waste rationale: Reducing log volume cuts bytes written and CPU spent formatting low-value output.
- Evidence: LOGGER.warn( | LOGGER.warn("Missing argument in ANSI escape specification '{}'", spec);

### `log4j-layout-template-json\src\main\java\org\apache\logging\log4j\layout\template\json\util\StringParameterParser.java`

- Pre-analysis: classes 8, methods 1, loops 4, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: StringParameterParser (line 291)
- Pattern: algorithmic-waste
- What was found: Loop at line 291 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 291
#### 2. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: StringParameterParser (line 159)
- Pattern: repeated-work
- What was found: Loop at line 159 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: readValue();
#### 3. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: StringParameterParser (line 159)
- Pattern: allocation-pressure
- What was found: Loop at line 159 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw new IllegalStateException("unknown state: " + state);

### `log4j-perf-test\src\main\java\org\apache\logging\log4j\perf\jmh\ThreadLocalVsPoolBenchmark.java`

- Pre-analysis: classes 7, methods 17, loops 1, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 94
- Pattern: concurrency-misuse
- What was found: Line 94 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: private static final ThreadLocalPool INSTANCE = new ThreadLocalPool();
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: serialize (line 183)
- Pattern: algorithmic-waste
- What was found: Loop at line 183 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 183

### `log4j-api\src\main\java\org\apache\logging\log4j\MarkerManager.java`

- Pre-analysis: classes 4, methods 24, loops 8, streams 0, synchronized blocks 4
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: addParents (line 155)
- Pattern: algorithmic-waste
- What was found: Loop at line 155 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 155
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: addParents (line 172)
- Pattern: algorithmic-waste
- What was found: Loop at line 172 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 172

### `log4j-api\src\main\java\org\apache\logging\log4j\spi\MutableThreadContextStack.java`

- Pre-analysis: classes 1, methods 31, loops 2, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: formatTo (line 204)
- Pattern: algorithmic-waste
- What was found: Loop at line 204 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 204
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: trim (line 113)
- Pattern: algorithmic-waste
- What was found: Loop at line 113 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 113

### `log4j-api\src\main\java\org\apache\logging\log4j\util\ServiceLoaderUtil.java`

- Pre-analysis: classes 9, methods 1, loops 1, streams 0, synchronized blocks 0
#### 1. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: ServiceLoaderUtil (line 103)
- Pattern: chatty-io
- What was found: Loop at line 103 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: if (serviceIterator.hasNext()) { | action.accept(serviceIterator.next()); | } catch (final ServiceConfigurationError | LinkageError e) {
#### 2. Repeated logging inside loop
- Severity: Low
- Confidence: High
- Location: ServiceLoaderUtil (line 103)
- Pattern: chatty-io
- What was found: Loop at line 103 logs on the hot iteration path.
- Why it is wasteful: Per-item logging adds formatting work and I/O overhead that can dominate lightweight loops.
- Likely impact: Lower throughput and larger log volumes for routine processing paths.
- Recommended remediation: Log summaries outside the loop or guard verbose logs behind debug checks.
- Low-waste rationale: Reducing log volume cuts bytes written and CPU spent formatting low-value output.
- Evidence: logger.warn("Unable to load implementation for service {}", serviceName, e); | logger.warn("Unexpected exception  while loading implementation for service {}", serviceName, e);

### `log4j-core\src\main\java\org\apache\logging\log4j\core\appender\AsyncAppenderEventDispatcher.java`

- Pre-analysis: classes 1, methods 5, loops 4, streams 1, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: dispatch (line 124)
- Pattern: algorithmic-waste
- What was found: Loop at line 124 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 124
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: dispatchAll (line 78)
- Pattern: algorithmic-waste
- What was found: Loop at line 78 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 78

### `log4j-core\src\main\java\org\apache\logging\log4j\core\appender\rewrite\PropertiesRewritePolicy.java`

- Pre-analysis: classes 1, methods 1, loops 3, streams 0, synchronized blocks 0
#### 1. List membership checks inside loop
- Severity: Medium
- Confidence: Medium
- Location: PropertiesRewritePolicy (line 59)
- Pattern: algorithmic-waste
- What was found: Loop at line 59 performs `.contains(...)` checks that may scan collections repeatedly.
- Why it is wasteful: Repeated linear scans inside iteration can push runtime toward O(n^2) as data sets grow.
- Likely impact: Throughput degradation and elevated CPU time for larger inputs.
- Recommended remediation: Use a `Set` for membership lookups or pre-index data before the loop.
- Low-waste rationale: Indexing once avoids repeated scans and reduces wasted CPU work.
- Evidence: line 59
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: PropertiesRewritePolicy (line 59)
- Pattern: algorithmic-waste
- What was found: Loop at line 59 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 59

### `log4j-core\src\main\java\org\apache\logging\log4j\core\config\plugins\processor\GraalVmProcessor.java`

- Pre-analysis: classes 1, methods 13, loops 3, streams 1, synchronized blocks 1
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: processPlugin (line 137)
- Pattern: algorithmic-waste
- What was found: Loop at line 137 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 137
#### 2. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: processPlugin (line 137)
- Pattern: data-movement-bloat
- What was found: Loop at line 137 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: switch (executableChild.getSimpleName().toString()) {

### `log4j-core\src\main\java\org\apache\logging\log4j\core\impl\ThrowableFormatOptions.java`

- Pre-analysis: classes 1, methods 13, loops 3, streams 0, synchronized blocks 0
#### 1. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: newInstance (line 259)
- Pattern: allocation-pressure
- What was found: Loop at line 259 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: packages = new ArrayList<>(array.length);
#### 2. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: newInstance (line 259)
- Pattern: repeated-work
- What was found: Loop at line 259 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: packages = new ArrayList<>(array.length);

### `log4j-core\src\main\java\org\apache\logging\log4j\core\pattern\EqualsBaseReplacementConverter.java`

- Pre-analysis: classes 1, methods 3, loops 2, streams 1, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: format (line 65)
- Pattern: algorithmic-waste
- What was found: Loop at line 65 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 65
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: parseSubstitution (line 94)
- Pattern: algorithmic-waste
- What was found: Loop at line 94 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 94

### `log4j-core\src\main\java\org\apache\logging\log4j\core\pattern\NameAbbreviator.java`

- Pre-analysis: classes 7, methods 15, loops 5, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: DROP (line 189)
- Pattern: algorithmic-waste
- What was found: Loop at line 189 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 189
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: getAbbreviator (line 95)
- Pattern: algorithmic-waste
- What was found: Loop at line 95 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 95

### `log4j-core\src\main\java\org\apache\logging\log4j\core\util\datetime\FastDatePrinter.java`

- Pre-analysis: classes 45, methods 58, loops 10, streams 0, synchronized blocks 0
#### 1. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: parsePattern (line 199)
- Pattern: chatty-io
- What was found: Loop at line 199 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: rule = selectNumberRule(Calendar.YEAR, tokenLen < 4 ? 4 : tokenLen); | rule = selectNumberRule(Calendar.DAY_OF_MONTH, tokenLen); | rule = new TwelveHourField(selectNumberRule(Calendar.HOUR, tokenLen));
#### 2. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: parsePattern (line 199)
- Pattern: allocation-pressure
- What was found: Loop at line 199 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw new IllegalArgumentException("Illegal pattern component: " + token);

### `log4j-core\src\main\java\org\apache\logging\log4j\core\util\DefaultShutdownCallbackRegistry.java`

- Pre-analysis: classes 2, methods 9, loops 1, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: run (line 72)
- Pattern: algorithmic-waste
- What was found: Loop at line 72 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 72
#### 2. Repeated logging inside loop
- Severity: Low
- Confidence: High
- Location: run (line 72)
- Pattern: chatty-io
- What was found: Loop at line 72 logs on the hot iteration path.
- Why it is wasteful: Per-item logging adds formatting work and I/O overhead that can dominate lightweight loops.
- Likely impact: Lower throughput and larger log volumes for routine processing paths.
- Recommended remediation: Log summaries outside the loop or guard verbose logs behind debug checks.
- Low-waste rationale: Reducing log volume cuts bytes written and CPU spent formatting low-value output.
- Evidence: LOGGER.error(SHUTDOWN_HOOK_MARKER, "Caught exception executing shutdown hook {}", hook, t1); | System.err.println(
#### 3. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: run (line 72)
- Pattern: allocation-pressure
- What was found: Loop at line 72 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: "Caught exception " + t2.getClass() + " logging exception " + t1.getClass());

### `log4j-jul\src\main\java\org\apache\logging\log4j\jul\Log4jBridgeHandler.java`

- Pre-analysis: classes 1, methods 10, loops 6, streams 0, synchronized blocks 2
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: debugPrintJulLoggers (line 309)
- Pattern: allocation-pressure
- What was found: Loop at line 309 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: txt.add("(!null-Logger '" + ln + "')  #" + n); | txt.add("(null-Level Logger '" + ln + "')  #" + n); | txt.add("Logger '" + ln + "',  lvl = " + lg.getLevel() + "  #" + n);
#### 2. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: debugPrintJulLoggers (line 322)
- Pattern: allocation-pressure
- What was found: Loop at line 322 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: System.out.println("  - " + s);
#### 3. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: propagateLogLevels (line 271)
- Pattern: allocation-pressure
- What was found: Loop at line 271 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: // if (DEVTEST)  outTxt.add("propagating '" + lcfg.getName() + "' / " + lcfg.getLevel() + "  ->  " +
#### 4. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: propagateLogLevels (line 282)
- Pattern: allocation-pressure
- What was found: Loop at line 282 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: // if (DEVTEST)  for (String s : outTxt)  System.out.println("+ " + s);

### `log4j-layout-template-json\src\main\java\org\apache\logging\log4j\layout\template\json\resolver\StackTraceStringResolver.java`

- Pre-analysis: classes 1, methods 4, loops 9, streams 1, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 168
- Pattern: algorithmic-waste
- What was found: Loop at line 168 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 168
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 186
- Pattern: algorithmic-waste
- What was found: Loop at line 186 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 186

### `log4j-layout-template-json\src\main\java\org\apache\logging\log4j\layout\template\json\util\MapAccessor.java`

- Pre-analysis: classes 1, methods 20, loops 2, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: getList (line 103)
- Pattern: algorithmic-waste
- What was found: Loop at line 103 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 103
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: getObject (line 144)
- Pattern: algorithmic-waste
- What was found: Loop at line 144 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 144

### `log4j-1.2-api\src\main\java\org\apache\log4j\config\PropertySetter.java`

- Pre-analysis: classes 2, methods 8, loops 2, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: setProperties (line 105)
- Pattern: algorithmic-waste
- What was found: Loop at line 105 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 105
#### 2. Repeated logging inside loop
- Severity: Low
- Confidence: High
- Location: setProperties (line 105)
- Pattern: chatty-io
- What was found: Loop at line 105 logs on the hot iteration path.
- Why it is wasteful: Per-item logging adds formatting work and I/O overhead that can dominate lightweight loops.
- Likely impact: Lower throughput and larger log volumes for routine processing paths.
- Recommended remediation: Log summaries outside the loop or guard verbose logs behind debug checks.
- Low-waste rationale: Reducing log volume cuts bytes written and CPU spent formatting low-value output.
- Evidence: LOGGER.warn("Failed to set property [{}] to value \"{}\".", key, value, ex); | LOGGER.warn("Failed to set property [{}] to value \"{}\".", key, value, ex);

### `log4j-1.2-api\src\main\java\org\apache\log4j\or\RendererMap.java`

- Pre-analysis: classes 5, methods 8, loops 2, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: get (line 133)
- Pattern: algorithmic-waste
- What was found: Loop at line 133 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 133
#### 2. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: get (line 133)
- Pattern: allocation-pressure
- What was found: Loop at line 133 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: // System.out.println("Searching for class: "+c);

### `log4j-1.2-api\src\main\java\org\apache\log4j\or\ThreadGroupRenderer.java`

- Pre-analysis: classes 1, methods 1, loops 1, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: doRender (line 35)
- Pattern: concurrency-misuse
- What was found: Line 35 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: final Thread[] threads = new Thread[threadGroup.activeCount()];

### `log4j-1.2-api\src\main\java\org\apache\log4j\pattern\FormattingInfo.java`

- Pre-analysis: classes 1, methods 6, loops 2, streams 0, synchronized blocks 0
#### 1. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: format (line 92)
- Pattern: chatty-io
- What was found: Loop at line 92 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: buffer.insert(fieldStart, SPACES);

### `log4j-api\src\main\java\org\apache\logging\log4j\spi\DefaultThreadContextMap.java`

- Pre-analysis: classes 1, methods 21, loops 1, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: DefaultThreadContextMap (line 72)
- Pattern: concurrency-misuse
- What was found: Line 72 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: : new ThreadLocal<>();

### `log4j-api\src\main\java\org\apache\logging\log4j\spi\DefaultThreadContextStack.java`

- Pre-analysis: classes 1, methods 28, loops 0, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 38
- Pattern: concurrency-misuse
- What was found: Line 38 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: private static final ThreadLocal<MutableThreadContextStack> STACK = new ThreadLocal<>();

### `log4j-api\src\main\java\org\apache\logging\log4j\util\Activator.java`

- Pre-analysis: classes 3, methods 6, loops 4, streams 0, synchronized blocks 0
#### 1. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: loadProvider (line 116)
- Pattern: chatty-io
- What was found: Loop at line 116 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: for (final ServiceReference<Provider> serviceReference : serviceReferences) { | final Provider provider = bundleContext.getService(serviceReference);

### `log4j-api\src\main\java\org\apache\logging\log4j\util\LoaderUtil.java`

- Pre-analysis: classes 89, methods 1, loops 4, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 82
- Pattern: concurrency-misuse
- What was found: Line 82 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: private static final PrivilegedAction<ClassLoader> TCCL_GETTER = new ThreadContextClassLoaderGetter();

### `log4j-api\src\main\java\org\apache\logging\log4j\util\SortedArrayStringMap.java`

- Pre-analysis: classes 2, methods 33, loops 8, streams 0, synchronized blocks 0
#### 1. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: merge (line 297)
- Pattern: chatty-io
- What was found: Loop at line 297 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: insertAt(~index, keys[i], values[i]);

### `log4j-api\src\main\java\org\apache\logging\log4j\util\Timer.java`

- Pre-analysis: classes 2, methods 16, loops 0, streams 0, synchronized blocks 5
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 49
- Pattern: concurrency-misuse
- What was found: Line 49 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: private ThreadLocal<Long> startTime = new ThreadLocal<Long>() {

### `log4j-core\src\main\java\org\apache\logging\log4j\core\appender\FailoverAppender.java`

- Pre-analysis: classes 1, methods 6, loops 4, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: start (line 92)
- Pattern: algorithmic-waste
- What was found: Loop at line 92 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 92
#### 2. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: start (line 92)
- Pattern: allocation-pressure
- What was found: Loop at line 92 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: LOGGER.error("Failover appender " + name + " is not configured");

### `log4j-core\src\main\java\org\apache\logging\log4j\core\appender\HttpURLConnectionManager.java`

- Pre-analysis: classes 1, methods 0, loops 3, streams 0, synchronized blocks 0
#### 1. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: line 100
- Pattern: chatty-io
- What was found: Loop at line 100 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: urlConnection.setRequestProperty(

### `log4j-core\src\main\java\org\apache\logging\log4j\core\appender\MemoryMappedFileManager.java`

- Pre-analysis: classes 3, methods 2, loops 2, streams 0, synchronized blocks 4
#### 1. Sleep-based coordination loop
- Severity: Medium
- Confidence: Medium
- Location: setEndOfBatch (line 241)
- Pattern: waiting-pattern
- What was found: for loop at line 241 uses `Thread.sleep(...)` as a coordination mechanism.
- Why it is wasteful: Sleep polling still wakes up periodically to recheck state, adding latency and unnecessary scheduler churn.
- Likely impact: Longer wait times, avoidable wakeups, and lower efficiency under load.
- Recommended remediation: Move to completion signals, blocking queues, futures, or exponential backoff with strict bounds.
- Low-waste rationale: Reducing periodic wakeups lowers wasted CPU time and coordination overhead.
- Evidence: line 241
#### 2. Repeated logging inside loop
- Severity: Low
- Confidence: High
- Location: setEndOfBatch (line 241)
- Pattern: chatty-io
- What was found: Loop at line 241 logs on the hot iteration path.
- Why it is wasteful: Per-item logging adds formatting work and I/O overhead that can dominate lightweight loops.
- Likely impact: Lower throughput and larger log volumes for routine processing paths.
- Recommended remediation: Log summaries outside the loop or guard verbose logs behind debug checks.
- Low-waste rationale: Reducing log volume cuts bytes written and CPU spent formatting low-value output.
- Evidence: LOGGER.debug("MMapAppender remapping {} start={}, size={}", fileName, start, size); | LOGGER.debug("MMapAppender remapped {} OK in {} millis", fileName, millis); | LOGGER.debug("Remap attempt {}/{} failed. Retrying...", i, MAX_REMAP_COUNT, e);

### `log4j-core\src\main\java\org\apache\logging\log4j\core\appender\rolling\action\DeleteAction.java`

- Pre-analysis: classes 1, methods 3, loops 3, streams 0, synchronized blocks 0
#### 1. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: line 108
- Pattern: chatty-io
- What was found: Loop at line 108 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: delete(path);

### `log4j-core\src\main\java\org\apache\logging\log4j\core\appender\routing\IdlePurgePolicy.java`

- Pre-analysis: classes 1, methods 8, loops 2, streams 0, synchronized blocks 1
#### 1. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: purge (line 76)
- Pattern: chatty-io
- What was found: Loop at line 76 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: routingAppender.deleteAppender(entry.getKey());

### `log4j-core\src\main\java\org\apache\logging\log4j\core\async\AsyncLoggerConfig.java`

- Pre-analysis: classes 4, methods 19, loops 0, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 98
- Pattern: concurrency-misuse
- What was found: Line 98 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: private static final ThreadLocal<Boolean> ASYNC_LOGGER_ENTERED = new ThreadLocal<Boolean>() {

### `log4j-core\src\main\java\org\apache\logging\log4j\core\async\ThreadNameCachingStrategy.java`

- Pre-analysis: classes 1, methods 4, loops 0, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 49
- Pattern: concurrency-misuse
- What was found: Line 49 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: private static final ThreadLocal<String> THREADLOCAL_NAME = new ThreadLocal<>();

### `log4j-core\src\main\java\org\apache\logging\log4j\core\config\AppenderControl.java`

- Pre-analysis: classes 1, methods 20, loops 0, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 39
- Pattern: concurrency-misuse
- What was found: Line 39 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: private final ThreadLocal<AppenderControl> recursive = new ThreadLocal<>();

### `log4j-core\src\main\java\org\apache\logging\log4j\core\context\internal\GarbageFreeSortedArrayThreadContextMap.java`

- Pre-analysis: classes 2, methods 22, loops 3, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: GarbageFreeSortedArrayThreadContextMap (line 74)
- Pattern: concurrency-misuse
- What was found: Line 74 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: : new ThreadLocal<>();

### `log4j-core\src\main\java\org\apache\logging\log4j\core\impl\ContextAnchor.java`

- Pre-analysis: classes 1, methods 1, loops 0, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 29
- Pattern: concurrency-misuse
- What was found: Line 29 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: public static final ThreadLocal<LoggerContext> THREAD_CONTEXT = new ThreadLocal<>();

### `log4j-core\src\main\java\org\apache\logging\log4j\core\impl\Log4jContextFactory.java`

- Pre-analysis: classes 6, methods 13, loops 1, streams 0, synchronized blocks 0
#### 1. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: line 315
- Pattern: data-movement-bloat
- What was found: Loop at line 315 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: LOGGER.warn("Unable to locate configuration {}, ignoring", configLocation.toString()); | LOGGER.info("Unable to access configuration {}, ignoring", configLocation.toString());
#### 2. Repeated logging inside loop
- Severity: Low
- Confidence: High
- Location: line 315
- Pattern: chatty-io
- What was found: Loop at line 315 logs on the hot iteration path.
- Why it is wasteful: Per-item logging adds formatting work and I/O overhead that can dominate lightweight loops.
- Likely impact: Lower throughput and larger log volumes for routine processing paths.
- Recommended remediation: Log summaries outside the loop or guard verbose logs behind debug checks.
- Low-waste rationale: Reducing log volume cuts bytes written and CPU spent formatting low-value output.
- Evidence: LOGGER.warn("Unable to locate configuration {}, ignoring", configLocation.toString()); | LOGGER.error( | LOGGER.info("Unable to access configuration {}, ignoring", configLocation.toString());

### `log4j-core\src\main\java\org\apache\logging\log4j\core\impl\ReusableLogEventFactory.java`

- Pre-analysis: classes 3, methods 3, loops 0, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 40
- Pattern: concurrency-misuse
- What was found: Line 40 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: private static final ThreadLocal<MutableLogEvent> mutableLogEventThreadLocal = new ThreadLocal<>();

### `log4j-core\src\main\java\org\apache\logging\log4j\core\layout\AbstractStringLayout.java`

- Pre-analysis: classes 7, methods 25, loops 0, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 119
- Pattern: concurrency-misuse
- What was found: Line 119 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: private static final ThreadLocal<StringBuilder> threadLocal = new ThreadLocal<>();

### `log4j-core\src\main\java\org\apache\logging\log4j\core\layout\StringBuilderEncoder.java`

- Pre-analysis: classes 2, methods 5, loops 0, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 44
- Pattern: concurrency-misuse
- What was found: Line 44 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: private final ThreadLocal<Object[]> threadLocal = new ThreadLocal<>();

### `log4j-core\src\main\java\org\apache\logging\log4j\core\net\SslSocketManager.java`

- Pre-analysis: classes 3, methods 4, loops 1, streams 1, synchronized blocks 0
#### 1. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: line 333
- Pattern: chatty-io
- What was found: Loop at line 333 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: for (InetSocketAddress socketAddress : socketAddresses) { | return SslSocketManager.createSocket( | data.socketOptions);

### `log4j-core\src\main\java\org\apache\logging\log4j\core\pattern\FormattingInfo.java`

- Pre-analysis: classes 1, methods 8, loops 2, streams 0, synchronized blocks 0
#### 1. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: format (line 199)
- Pattern: chatty-io
- What was found: Loop at line 199 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: buffer.insert(fieldStart, paddingArray);

### `log4j-core\src\main\java\org\apache\logging\log4j\core\pattern\ThreadIdPatternConverter.java`

- Pre-analysis: classes 1, methods 3, loops 0, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 35
- Pattern: concurrency-misuse
- What was found: Line 35 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: private static final ThreadIdPatternConverter INSTANCE = new ThreadIdPatternConverter();

### `log4j-core\src\main\java\org\apache\logging\log4j\core\pattern\ThreadNamePatternConverter.java`

- Pre-analysis: classes 1, methods 3, loops 0, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 33
- Pattern: concurrency-misuse
- What was found: Line 33 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: private static final ThreadNamePatternConverter INSTANCE = new ThreadNamePatternConverter();

### `log4j-core\src\main\java\org\apache\logging\log4j\core\pattern\ThreadPriorityPatternConverter.java`

- Pre-analysis: classes 1, methods 3, loops 0, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 35
- Pattern: concurrency-misuse
- What was found: Line 35 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: private static final ThreadPriorityPatternConverter INSTANCE = new ThreadPriorityPatternConverter();

### `log4j-core\src\main\java\org\apache\logging\log4j\core\util\internal\instant\InstantPatternDynamicFormatter.java`

- Pre-analysis: classes 7, methods 49, loops 6, streams 1, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 366
- Pattern: algorithmic-waste
- What was found: Loop at line 366 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 366
#### 2. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: sequencePattern (line 228)
- Pattern: allocation-pressure
- What was found: Loop at line 228 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: final PatternSequence sequence = new StaticPatternSequence("" + c);

### `log4j-core\src\main\java\org\apache\logging\log4j\core\util\JsonUtils.java`

- Pre-analysis: classes 2, methods 4, loops 3, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 58
- Pattern: concurrency-misuse
- What was found: Line 58 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: private static final ThreadLocal<char[]> _qbufLocal = new ThreadLocal<>();

### `log4j-perf-test\src\main\java\org\apache\logging\log4j\perf\jmh\ClocksBenchmark.java`

- Pre-analysis: classes 4, methods 2, loops 1, streams 0, synchronized blocks 1
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: baseline (line 144)
- Pattern: concurrency-misuse
- What was found: Line 144 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: final Thread updater = new Thread(

### `log4j-perf-test\src\main\java\org\apache\logging\log4j\perf\jmh\StackWalkBenchmark.java`

- Pre-analysis: classes 2, methods 4, loops 2, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 41
- Pattern: concurrency-misuse
- What was found: Line 41 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: private static final ThreadLocal<String> FQCN = new ThreadLocal<>();

### `log4j-perf-test\src\main\java\org\apache\logging\log4j\perf\jmh\TextEncoderHelperBenchmark.java`

- Pre-analysis: classes 2, methods 13, loops 0, streams 0, synchronized blocks 2
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 122
- Pattern: concurrency-misuse
- What was found: Line 122 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: // private static final ThreadLocal<StringBuilderEncoder> textEncoderHelper = new ThreadLocal<>();

### `log4j-perf-test\src\main\java\org\apache\logging\log4j\perf\jmh\ThreadLocalVsConcurrentHashMapBenchmark.java`

- Pre-analysis: classes 1, methods 6, loops 0, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 32
- Pattern: concurrency-misuse
- What was found: Line 32 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: private static ThreadLocal<StringBuilder> threadLocal = new ThreadLocal<>();

### `log4j-perf-test\src\main\java\org\apache\logging\log4j\perf\nogc\NoGcMessage.java`

- Pre-analysis: classes 2, methods 6, loops 1, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 36
- Pattern: concurrency-misuse
- What was found: Line 36 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: private final ThreadLocal<InternalState> state = new ThreadLocal<>();

### `log4j-perf-test\src\main\java\org\apache\logging\log4j\perf\nogc\OpenHashStringMap.java`

- Pre-analysis: classes 3, methods 45, loops 15, streams 0, synchronized blocks 0
#### 1. Polling loop without blocking
- Severity: High
- Confidence: Medium
- Location: rehash (line 666)
- Pattern: idle-compute
- What was found: while loop at line 666 appears to poll shared state without a blocking primitive.
- Why it is wasteful: A polling loop repeatedly burns CPU to recheck readiness instead of sleeping until useful work can continue.
- Likely impact: Higher CPU utilization, thermal pressure, and reduced throughput for other work on the same host.
- Recommended remediation: Replace polling with a blocking primitive, callback, latch, queue, or at least bounded backoff.
- Low-waste rationale: Blocking or event-driven coordination cuts useless instructions and improves value per watt.
- Evidence: line 666

### `log4j-slf4j2-impl\src\main\java\org\apache\logging\slf4j\Log4jMDCAdapter.java`

- Pre-analysis: classes 2, methods 15, loops 0, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 37
- Pattern: concurrency-misuse
- What was found: Line 37 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: private final ThreadLocalMapOfStacks mapOfStacks = new ThreadLocalMapOfStacks();

### `log4j-spring-boot\src\main\java\org\apache\logging\log4j\spring\boot\Log4j2SpringBootLoggingSystem.java`

- Pre-analysis: classes 2, methods 10, loops 2, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: parseConfigLocations (line 216)
- Pattern: algorithmic-waste
- What was found: Loop at line 216 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 216
#### 2. Repeated logging inside loop
- Severity: Low
- Confidence: High
- Location: loadConfiguration (line 166)
- Pattern: chatty-io
- What was found: Loop at line 166 logs on the hot iteration path.
- Why it is wasteful: Per-item logging adds formatting work and I/O overhead that can dominate lightweight loops.
- Likely impact: Lower throughput and larger log volumes for routine processing paths.
- Recommended remediation: Log summaries outside the loop or guard verbose logs behind debug checks.
- Low-waste rationale: Reducing log volume cuts bytes written and CPU spent formatting low-value output.
- Evidence: LOGGER.warn( | LOGGER.warn(

### `log4j-1.2-api\src\main\java\org\apache\log4j\Category.java`

- Pre-analysis: classes 3, methods 63, loops 5, streams 1, synchronized blocks 3
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: getResourceBundle (line 459)
- Pattern: algorithmic-waste
- What was found: Loop at line 459 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 459

### `log4j-1.2-api\src\main\java\org\apache\log4j\rewrite\MapRewritePolicy.java`

- Pre-analysis: classes 1, methods 2, loops 2, streams 0, synchronized blocks 0
#### 1. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: rewrite (line 69)
- Pattern: data-movement-bloat
- What was found: Loop at line 69 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: props.put(entry.getKey(), entry.getValue().toString());

### `log4j-1.2-api\src\main\java\org\apache\log4j\rewrite\PropertyRewritePolicy.java`

- Pre-analysis: classes 1, methods 1, loops 3, streams 0, synchronized blocks 1
#### 1. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: PropertyRewritePolicy (line 60)
- Pattern: data-movement-bloat
- What was found: Loop at line 60 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: entry.nextElement().toString().trim(), | entry.nextElement().toString().trim());

### `log4j-api\src\main\java\org\apache\logging\log4j\CloseableThreadContext.java`

- Pre-analysis: classes 2, methods 1, loops 4, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: CloseableThreadContext (line 169)
- Pattern: algorithmic-waste
- What was found: Loop at line 169 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 169

### `log4j-api\src\main\java\org\apache\logging\log4j\internal\map\UnmodifiableArrayBackedMap.java`

- Pre-analysis: classes 5, methods 40, loops 11, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: copyAndRemoveAll (line 378)
- Pattern: algorithmic-waste
- What was found: Loop at line 378 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 378

### `log4j-api\src\main\java\org\apache\logging\log4j\message\LocalizedMessage.java`

- Pre-analysis: classes 3, methods 23, loops 2, streams 0, synchronized blocks 0
#### 1. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: line 278
- Pattern: data-movement-bloat
- What was found: Loop at line 278 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: stringArgs[i] = obj.toString();

### `log4j-api\src\main\java\org\apache\logging\log4j\message\MapMessageJsonFormatter.java`

- Pre-analysis: classes 1, methods 20, loops 11, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: formatList (line 208)
- Pattern: algorithmic-waste
- What was found: Loop at line 208 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 208

### `log4j-api\src\main\java\org\apache\logging\log4j\status\StatusLogger.java`

- Pre-analysis: classes 6, methods 42, loops 5, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: getLevel (line 728)
- Pattern: algorithmic-waste
- What was found: Loop at line 728 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 728

### `log4j-api\src\main\java\org\apache\logging\log4j\util\PropertySource.java`

- Pre-analysis: classes 3, methods 1, loops 2, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: forEach (line 157)
- Pattern: algorithmic-waste
- What was found: Loop at line 157 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 157

### `log4j-core\src\main\java\org\apache\logging\log4j\core\appender\AppenderSet.java`

- Pre-analysis: classes 2, methods 11, loops 1, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: build (line 64)
- Pattern: algorithmic-waste
- What was found: Loop at line 64 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 64

### `log4j-core\src\main\java\org\apache\logging\log4j\core\appender\AsyncAppender.java`

- Pre-analysis: classes 3, methods 29, loops 3, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: start (line 104)
- Pattern: algorithmic-waste
- What was found: Loop at line 104 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 104

### `log4j-core\src\main\java\org\apache\logging\log4j\core\appender\rewrite\MapRewritePolicy.java`

- Pre-analysis: classes 2, methods 3, loops 3, streams 0, synchronized blocks 0
#### 1. Repeated logging inside loop
- Severity: Low
- Confidence: High
- Location: line 136
- Pattern: chatty-io
- What was found: Loop at line 136 logs on the hot iteration path.
- Why it is wasteful: Per-item logging adds formatting work and I/O overhead that can dominate lightweight loops.
- Likely impact: Lower throughput and larger log volumes for routine processing paths.
- Recommended remediation: Log summaries outside the loop or guard verbose logs behind debug checks.
- Low-waste rationale: Reducing log volume cuts bytes written and CPU spent formatting low-value output.
- Evidence: LOGGER.error("A null key is not valid in MapRewritePolicy"); | LOGGER.error("A null value for key " + key + " is not allowed in MapRewritePolicy");
#### 2. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 136
- Pattern: allocation-pressure
- What was found: Loop at line 136 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: LOGGER.error("A null value for key " + key + " is not allowed in MapRewritePolicy");

### `log4j-core\src\main\java\org\apache\logging\log4j\core\appender\rolling\CompositeTriggeringPolicy.java`

- Pre-analysis: classes 1, methods 6, loops 3, streams 0, synchronized blocks 0
#### 1. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: initialize (line 51)
- Pattern: data-movement-bloat
- What was found: Loop at line 51 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: LOGGER.debug("Initializing triggering policy {}", triggeringPolicy.toString());

### `log4j-core\src\main\java\org\apache\logging\log4j\core\appender\rolling\DirectWriteRolloverStrategy.java`

- Pre-analysis: classes 2, methods 29, loops 1, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: purge (line 374)
- Pattern: algorithmic-waste
- What was found: Loop at line 374 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 374

### `log4j-core\src\main\java\org\apache\logging\log4j\core\appender\routing\Routes.java`

- Pre-analysis: classes 2, methods 20, loops 2, streams 0, synchronized blocks 0
#### 1. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: toString (line 267)
- Pattern: data-movement-bloat
- What was found: Loop at line 267 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: sb.append(route.toString());

### `log4j-core\src\main\java\org\apache\logging\log4j\core\config\AwaitCompletionReliabilityStrategy.java`

- Pre-analysis: classes 1, methods 9, loops 1, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: waitForCompletion (line 173)
- Pattern: algorithmic-waste
- What was found: Loop at line 173 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 173

### `log4j-core\src\main\java\org\apache\logging\log4j\core\config\ConfigurationScheduler.java`

- Pre-analysis: classes 2, methods 17, loops 1, streams 0, synchronized blocks 1
#### 1. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: toString (line 272)
- Pattern: data-movement-bloat
- What was found: Loop at line 272 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: sb.append(runnable.toString());

### `log4j-core\src\main\java\org\apache\logging\log4j\core\filter\CompositeFilter.java`

- Pre-analysis: classes 1, methods 15, loops 18, streams 0, synchronized blocks 0
#### 1. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: toString (line 665)
- Pattern: data-movement-bloat
- What was found: Loop at line 665 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: sb.append(filters[i].toString());

### `log4j-core\src\main\java\org\apache\logging\log4j\core\impl\ThrowableProxyHelper.java`

- Pre-analysis: classes 4, methods 6, loops 3, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 91
- Pattern: algorithmic-waste
- What was found: Loop at line 91 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 91

### `log4j-core\src\main\java\org\apache\logging\log4j\core\jmx\LoggerConfigAdmin.java`

- Pre-analysis: classes 1, methods 10, loops 1, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: getAppenderRefs (line 108)
- Pattern: algorithmic-waste
- What was found: Loop at line 108 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 108

### `log4j-core\src\main\java\org\apache\logging\log4j\core\jmx\StatusLoggerAdmin.java`

- Pre-analysis: classes 1, methods 4, loops 1, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: postRegister (line 143)
- Pattern: algorithmic-waste
- What was found: Loop at line 143 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 143

### `log4j-core\src\main\java\org\apache\logging\log4j\core\message\ExtendedThreadInformation.java`

- Pre-analysis: classes 2, methods 6, loops 3, streams 0, synchronized blocks 0
#### 1. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: printStack (line 57)
- Pattern: data-movement-bloat
- What was found: Loop at line 57 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: sb.append("\tat ").append(element.toString());

### `log4j-core\src\main\java\org\apache\logging\log4j\core\pattern\AbstractStyleNameConverter.java`

- Pre-analysis: classes 18, methods 19, loops 1, streams 1, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: format (line 370)
- Pattern: algorithmic-waste
- What was found: Loop at line 370 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 370

### `log4j-core\src\main\java\org\apache\logging\log4j\core\pattern\DynamicWordAbbreviator.java`

- Pre-analysis: classes 1, methods 4, loops 2, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: split (line 99)
- Pattern: algorithmic-waste
- What was found: Loop at line 99 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 99

### `log4j-core\src\main\java\org\apache\logging\log4j\core\pattern\EncodingPatternConverter.java`

- Pre-analysis: classes 2, methods 9, loops 6, streams 1, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: format (line 92)
- Pattern: algorithmic-waste
- What was found: Loop at line 92 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 92

### `log4j-core\src\main\java\org\apache\logging\log4j\core\pattern\MaxLengthConverter.java`

- Pre-analysis: classes 1, methods 4, loops 1, streams 1, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: format (line 88)
- Pattern: algorithmic-waste
- What was found: Loop at line 88 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 88

### `log4j-core\src\main\java\org\apache\logging\log4j\core\pattern\StyleConverter.java`

- Pre-analysis: classes 1, methods 5, loops 1, streams 1, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: format (line 116)
- Pattern: algorithmic-waste
- What was found: Loop at line 116 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 116

### `log4j-core\src\main\java\org\apache\logging\log4j\core\pattern\ThrowableExtendedStackTraceRenderer.java`

- Pre-analysis: classes 11, methods 4, loops 3, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 118
- Pattern: algorithmic-waste
- What was found: Loop at line 118 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 118

### `log4j-core\src\main\java\org\apache\logging\log4j\core\pattern\ThrowableStackTraceRenderer.java`

- Pre-analysis: classes 3, methods 7, loops 5, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 314
- Pattern: algorithmic-waste
- What was found: Loop at line 314 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 314

### `log4j-core\src\main\java\org\apache\logging\log4j\core\pattern\VariablesNotEmptyReplacementConverter.java`

- Pre-analysis: classes 1, methods 3, loops 2, streams 1, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: format (line 84)
- Pattern: algorithmic-waste
- What was found: Loop at line 84 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 84

### `log4j-core\src\main\java\org\apache\logging\log4j\core\util\internal\InternalLoggerRegistry.java`

- Pre-analysis: classes 2, methods 1, loops 2, streams 3, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: InternalLoggerRegistry (line 85)
- Pattern: algorithmic-waste
- What was found: Loop at line 85 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 85

### `log4j-core\src\main\java\org\apache\logging\log4j\core\util\Transform.java`

- Pre-analysis: classes 2, methods 1, loops 3, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Transform (line 103)
- Pattern: algorithmic-waste
- What was found: Loop at line 103 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 103

### `log4j-jul\src\main\java\org\apache\logging\log4j\jul\DefaultLevelConverter.java`

- Pre-analysis: classes 2, methods 7, loops 1, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: nearestLevel (line 101)
- Pattern: algorithmic-waste
- What was found: Loop at line 101 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 101

### `log4j-layout-template-json\src\main\java\org\apache\logging\log4j\layout\template\json\resolver\MessageParameterResolver.java`

- Pre-analysis: classes 2, methods 5, loops 1, streams 0, synchronized blocks 0
#### 1. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: resolve (line 122)
- Pattern: repeated-work
- What was found: Loop at line 122 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: jsonWriter.writeValue(parameter);

### `log4j-layout-template-json\src\main\java\org\apache\logging\log4j\layout\template\json\resolver\TemplateResolverFactories.java`

- Pre-analysis: classes 3, methods 1, loops 1, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: TemplateResolverFactories (line 79)
- Pattern: algorithmic-waste
- What was found: Loop at line 79 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 79

### `log4j-layout-template-json\src\main\java\org\apache\logging\log4j\layout\template\json\resolver\TemplateResolverInterceptors.java`

- Pre-analysis: classes 3, methods 1, loops 1, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: TemplateResolverInterceptors (line 76)
- Pattern: algorithmic-waste
- What was found: Loop at line 76 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 76

### `log4j-perf-test\src\main\java\org\apache\logging\log4j\layout\template\json\JsonTemplateLayoutBenchmarkReport.java`

- Pre-analysis: classes 5, methods 9, loops 1, streams 6, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: readObjectAtPath (line 230)
- Pattern: algorithmic-waste
- What was found: Loop at line 230 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 230

### `log4j-perf-test\src\main\java\org\apache\logging\log4j\perf\jmh\ThreadContextBenchmark2.java`

- Pre-analysis: classes 5, methods 13, loops 5, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: threadContextMap (line 220)
- Pattern: algorithmic-waste
- What was found: Loop at line 220 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 220

### `log4j-slf4j-impl\src\main\java\org\apache\logging\slf4j\Log4jMarkerFactory.java`

- Pre-analysis: classes 1, methods 6, loops 1, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 108
- Pattern: algorithmic-waste
- What was found: Loop at line 108 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 108

### `log4j-slf4j2-impl\src\main\java\org\apache\logging\slf4j\Log4jMarkerFactory.java`

- Pre-analysis: classes 1, methods 6, loops 1, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 108
- Pattern: algorithmic-waste
- What was found: Loop at line 108 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 108

### `log4j-to-slf4j\src\main\java\org\apache\logging\slf4j\SLF4JLogger.java`

- Pre-analysis: classes 1, methods 22, loops 1, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 115
- Pattern: algorithmic-waste
- What was found: Loop at line 115 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 115

### `log4j-1.2-api\src\main\java\org\apache\log4j\jmx\AbstractDynamicMBean.java`

- Pre-analysis: classes 1, methods 4, loops 3, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: postRegister (line 114)
- Pattern: allocation-pressure
- What was found: Loop at line 114 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: getLogger().warn("Missing MBean " + name.getCanonicalName()); | getLogger().warn("Failed unregistering " + name.getCanonicalName());

### `log4j-1.2-api\src\main\java\org\apache\log4j\RollingFileAppender.java`

- Pre-analysis: classes 1, methods 9, loops 1, streams 0, synchronized blocks 1
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: rollOver (line 133)
- Pattern: allocation-pressure
- What was found: Loop at line 133 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: file = new File(fileName + "." + i); | LogLog.debug("Renaming file " + file + " to " + target);

### `log4j-1.2-api\src\main\java\org\apache\log4j\varia\FallbackErrorHandler.java`

- Pre-analysis: classes 1, methods 8, loops 1, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: error (line 82)
- Pattern: allocation-pressure
- What was found: Loop at line 82 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: LogLog.debug("FB: Searching for [" + primary.getName() + "] in logger [" + l.getName() + "]."); | LogLog.debug("FB: Replacing [" + primary.getName() + "] by [" + backup.getName() + "] in logger [" | LogLog.debug("FB: Adding appender [" + backup.getName() + "] to logger " + l.getName());

### `log4j-core\src\main\java\org\apache\logging\log4j\core\appender\rewrite\RewriteAppender.java`

- Pre-analysis: classes 1, methods 3, loops 3, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: start (line 65)
- Pattern: allocation-pressure
- What was found: Loop at line 65 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: LOGGER.error("Appender " + ref + " cannot be located. Reference ignored");

### `log4j-core\src\main\java\org\apache\logging\log4j\core\config\LoggersPlugin.java`

- Pre-analysis: classes 1, methods 1, loops 1, streams 0, synchronized blocks 0
#### 1. Repeated logging inside loop
- Severity: Low
- Confidence: High
- Location: LoggersPlugin (line 43)
- Pattern: chatty-io
- What was found: Loop at line 43 logs on the hot iteration path.
- Why it is wasteful: Per-item logging adds formatting work and I/O overhead that can dominate lightweight loops.
- Likely impact: Lower throughput and larger log volumes for routine processing paths.
- Recommended remediation: Log summaries outside the loop or guard verbose logs behind debug checks.
- Low-waste rationale: Reducing log volume cuts bytes written and CPU spent formatting low-value output.
- Evidence: if (logger.getName().isEmpty()) { | loggerMap.put(logger.getName(), logger);

### `log4j-core\src\main\java\org\apache\logging\log4j\core\jackson\Log4jStackTraceElementDeserializer.java`

- Pre-analysis: classes 2, methods 1, loops 1, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 53
- Pattern: allocation-pressure
- What was found: Loop at line 53 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: jp, "Non-numeric token (" + t + ") for property 'line'", e);

### `log4j-core\src\main\java\org\apache\logging\log4j\core\pattern\LevelPatternConverter.java`

- Pre-analysis: classes 3, methods 8, loops 2, streams 0, synchronized blocks 0
#### 1. Repeated logging inside loop
- Severity: Low
- Confidence: High
- Location: newInstance (line 68)
- Pattern: chatty-io
- What was found: Loop at line 68 logs on the hot iteration path.
- Why it is wasteful: Per-item logging adds formatting work and I/O overhead that can dominate lightweight loops.
- Likely impact: Lower throughput and larger log volumes for routine processing paths.
- Recommended remediation: Log summaries outside the loop or guard verbose logs behind debug checks.
- Low-waste rationale: Reducing log volume cuts bytes written and CPU spent formatting low-value output.
- Evidence: LOGGER.error("Invalid option {}", def); | LOGGER.error("Invalid Level {}", key);

### `log4j-core\src\main\java\org\apache\logging\log4j\core\util\NetUtils.java`

- Pre-analysis: classes 3, methods 8, loops 5, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: toURIs (line 187)
- Pattern: allocation-pressure
- What was found: Loop at line 187 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: final URI uri = NetUtils.toURI(scheme != null ? scheme + ":" + part.trim() : part.trim());

### `log4j-core-java9\src\main\java\org\apache\logging\log4j\core\jackson\Log4jStackTraceElementDeserializer.java`

- Pre-analysis: classes 2, methods 1, loops 1, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 58
- Pattern: allocation-pressure
- What was found: Loop at line 58 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: jp, "Non-numeric token (" + t + ") for property 'line'", e);

### `log4j-perf-test\src\main\java\org\apache\logging\log4j\perf\jmh\FileAppenderThrowableBenchmark.java`

- Pre-analysis: classes 34, methods 14, loops 1, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: getComplexThrowable (line 151)
- Pattern: allocation-pressure
- What was found: Loop at line 151 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: Class.forName(FileAppenderThrowableBenchmark.class.getName() + "$TestIface" + (i % 31))

### `log4j-perf-test\src\main\java\org\apache\logging\log4j\perf\jmh\MDCFilterBenchmark.java`

- Pre-analysis: classes 2, methods 7, loops 1, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: ThreadContextState (line 50)
- Pattern: allocation-pressure
- What was found: Loop at line 50 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: ThreadContext.put("user" + i, "Apache"); | MDC.put("user" + i, "Apache");

### `log4j-taglib\src\main\java\org\apache\logging\log4j\taglib\DumpTag.java`

- Pre-analysis: classes 2, methods 4, loops 1, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 59
- Pattern: allocation-pressure
- What was found: Loop at line 59 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: this.pageContext.getOut().write("<dt><code>" + name + "</code></dt>"); | this.pageContext.getOut().write("<dd><code>" + value + "</code></dd>");

## Cautions
- This is static analysis only; findings indicate likely waste patterns, not measured bottlenecks.
- Method extraction and loop classification are heuristic and may miss unconventional Java syntax.