# JSON-java-master Green Code Report

## Summary
- Project root: `C:\VoxxedDays\GitRepos\JSON-java-master`
- Java files reviewed: 85
- Source files: 26
- Test files: 59
- Overall risk level: High
- Findings by severity: High 2, Medium 92, Low 22
- Top efficiency themes: Data movement bloat, Allocation pressure, Algorithmic waste, Repeated work, Chatty I/O

## Hotspots
- `src\test\java\org\json\junit\JSONParserConfigurationTest.java`: score 36, findings 20
- `src\main\java\org\json\XML.java`: score 33, findings 18
- `src\test\java\org\json\junit\JSONObjectTest.java`: score 27, findings 15
- `src\main\java\org\json\JSONML.java`: score 15, findings 8
- `src\test\java\org\json\junit\JSONArrayTest.java`: score 14, findings 8
- `src\main\java\org\json\JSONObject.java`: score 14, findings 7
- `src\test\java\org\json\junit\JSONTokenerTest.java`: score 12, findings 8
- `src\main\java\org\json\JSONTokener.java`: score 11, findings 6
- `src\main\java\org\json\CDL.java`: score 11, findings 7
- `src\main\java\org\json\XMLTokener.java`: score 9, findings 5

## File Findings
### `src\test\java\org\json\junit\JSONParserConfigurationTest.java`

- Pre-analysis: classes 1, methods 45, loops 4, streams 0, synchronized blocks 0
#### 1. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: givenInvalidInputArrays_testStrictModeFalse_shouldNotThrowAnyException (line 287)
- Pattern: allocation-pressure
- What was found: Loop at line 287 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: JSONArray jsonArray = new JSONArray(testCase, jsonParserConfiguration);
#### 2. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: givenInvalidInputObjects_testStrictModeFalse_shouldNotThrowAnyException (line 306)
- Pattern: allocation-pressure
- What was found: Loop at line 306 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: JSONObject jsonObject = new JSONObject(testCase, jsonParserConfiguration);
#### 3. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: givenInvalidInputObjects_testStrictModeTrue_shouldThrowJsonException (line 110)
- Pattern: allocation-pressure
- What was found: Loop at line 110 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: JSONObject jsonObject = new JSONObject(testCase, jsonParserConfiguration);
#### 4. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: givenInvalidInput_testStrictModeTrue_shouldThrowJsonException (line 91)
- Pattern: allocation-pressure
- What was found: Loop at line 91 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: JSONArray jsonArray = new JSONArray(testCase, jsonParserConfiguration);
#### 5. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: givenInvalidInputArrays_testStrictModeFalse_shouldNotThrowAnyException (line 287)
- Pattern: algorithmic-waste
- What was found: Loop at line 287 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 287
#### 6. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: givenInvalidInputObjects_testStrictModeFalse_shouldNotThrowAnyException (line 306)
- Pattern: algorithmic-waste
- What was found: Loop at line 306 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 306
#### 7. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: givenInvalidInputObjects_testStrictModeTrue_shouldThrowJsonException (line 110)
- Pattern: algorithmic-waste
- What was found: Loop at line 110 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 110
#### 8. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: givenInvalidInput_testStrictModeTrue_shouldThrowJsonException (line 91)
- Pattern: algorithmic-waste
- What was found: Loop at line 91 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 91
#### 9. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: givenInvalidInputArrays_testStrictModeFalse_shouldNotThrowAnyException (line 287)
- Pattern: data-movement-bloat
- What was found: Loop at line 287 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: JSONArray jsonArray = new JSONArray(testCase, jsonParserConfiguration);
#### 10. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: givenInvalidInputObjects_testStrictModeFalse_shouldNotThrowAnyException (line 306)
- Pattern: data-movement-bloat
- What was found: Loop at line 306 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: JSONObject jsonObject = new JSONObject(testCase, jsonParserConfiguration);
#### 11. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: givenInvalidInputObjects_testStrictModeTrue_shouldThrowJsonException (line 110)
- Pattern: data-movement-bloat
- What was found: Loop at line 110 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: JSONObject jsonObject = new JSONObject(testCase, jsonParserConfiguration); | String s = jsonObject.toString();
#### 12. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: givenInvalidInput_testStrictModeTrue_shouldThrowJsonException (line 91)
- Pattern: data-movement-bloat
- What was found: Loop at line 91 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: JSONArray jsonArray = new JSONArray(testCase, jsonParserConfiguration); | String s = jsonArray.toString();
#### 13. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: givenInvalidInputArrays_testStrictModeFalse_shouldNotThrowAnyException (line 287)
- Pattern: repeated-work
- What was found: Loop at line 287 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: JSONArray jsonArray = new JSONArray(testCase, jsonParserConfiguration);
#### 14. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: givenInvalidInputObjects_testStrictModeFalse_shouldNotThrowAnyException (line 306)
- Pattern: repeated-work
- What was found: Loop at line 306 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: JSONObject jsonObject = new JSONObject(testCase, jsonParserConfiguration);
#### 15. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: givenInvalidInputObjects_testStrictModeTrue_shouldThrowJsonException (line 110)
- Pattern: repeated-work
- What was found: Loop at line 110 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: JSONObject jsonObject = new JSONObject(testCase, jsonParserConfiguration);
#### 16. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: givenInvalidInput_testStrictModeTrue_shouldThrowJsonException (line 91)
- Pattern: repeated-work
- What was found: Loop at line 91 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: JSONArray jsonArray = new JSONArray(testCase, jsonParserConfiguration);
#### 17. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: givenInvalidInputArrays_testStrictModeFalse_shouldNotThrowAnyException (line 287)
- Pattern: allocation-pressure
- What was found: Loop at line 287 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: System.out.println("Unexpected exception: " + e.getMessage() + " Noncompliant Array index: " + i);
#### 18. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: givenInvalidInputObjects_testStrictModeFalse_shouldNotThrowAnyException (line 306)
- Pattern: allocation-pressure
- What was found: Loop at line 306 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: System.out.println("Unexpected exception: " + e.getMessage() + " Noncompliant Array index: " + i);
#### 19. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: givenInvalidInputObjects_testStrictModeTrue_shouldThrowJsonException (line 110)
- Pattern: allocation-pressure
- What was found: Loop at line 110 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: String msg = "Expected an exception, but got: " + s + " Noncompliant Array index: " + i;
#### 20. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: givenInvalidInput_testStrictModeTrue_shouldThrowJsonException (line 91)
- Pattern: allocation-pressure
- What was found: Loop at line 91 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: String msg = "Expected an exception, but got: " + s + " Noncompliant Array index: " + i;

### `src\main\java\org\json\XML.java`

- Pre-analysis: classes 1, methods 14, loops 14, streams 0, synchronized blocks 0
#### 1. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: line 340
- Pattern: allocation-pressure
- What was found: Loop at line 340 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: context.put(tagName, new JSONArray()); | context.put(tagName, new JSONArray());
#### 2. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: line 415
- Pattern: allocation-pressure
- What was found: Loop at line 415 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: context.put(tagName, new JSONArray());
#### 3. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: line 966
- Pattern: allocation-pressure
- What was found: Loop at line 966 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: value = new JSONArray(value);
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 340
- Pattern: algorithmic-waste
- What was found: Loop at line 340 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 340
#### 5. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 415
- Pattern: algorithmic-waste
- What was found: Loop at line 415 is nested at depth 5 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 415
#### 6. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: removeEmpty (line 510)
- Pattern: algorithmic-waste
- What was found: Loop at line 510 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 510
#### 7. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: unescape (line 192)
- Pattern: algorithmic-waste
- What was found: Loop at line 192 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 192
#### 8. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: line 340
- Pattern: data-movement-bloat
- What was found: Loop at line 340 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: context.put(tagName, new JSONArray()); | context.put(tagName, new JSONArray());
#### 9. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: line 415
- Pattern: data-movement-bloat
- What was found: Loop at line 415 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: context.put(tagName, new JSONArray());
#### 10. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: line 966
- Pattern: data-movement-bloat
- What was found: Loop at line 966 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: value = new JSONArray(value); | sb.append(escape(val.toString())); | sb.append(escape(value.toString()));
#### 11. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: line 980
- Pattern: data-movement-bloat
- What was found: Loop at line 980 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: sb.append(escape(val.toString()));
#### 12. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: line 340
- Pattern: repeated-work
- What was found: Loop at line 340 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: context.put(tagName, new JSONArray()); | if (parse(x, jsonObject, tagName, config, currentNestingDepth + 1)) { | context.put(tagName, new JSONArray());
#### 13. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: line 415
- Pattern: repeated-work
- What was found: Loop at line 415 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: if (parse(x, jsonObject, tagName, config, currentNestingDepth + 1)) { | context.put(tagName, new JSONArray());
#### 14. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: line 790
- Pattern: repeated-work
- What was found: Loop at line 790 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: parse(x, jo, null, config, 0);
#### 15. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: line 966
- Pattern: repeated-work
- What was found: Loop at line 966 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: value = new JSONArray(value);
#### 16. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 227
- Pattern: allocation-pressure
- What was found: Loop at line 227 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw new JSONException("'" + string
#### 17. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 340
- Pattern: allocation-pressure
- What was found: Loop at line 340 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw x.syntaxError("Unclosed tag " + tagName); | throw x.syntaxError("Maximum nesting depth of " + config.getMaxNestingDepth() + " reached");
#### 18. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 415
- Pattern: allocation-pressure
- What was found: Loop at line 415 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw x.syntaxError("Unclosed tag " + tagName); | throw x.syntaxError("Maximum nesting depth of " + config.getMaxNestingDepth() + " reached");

### `src\test\java\org\json\junit\JSONObjectTest.java`

- Pre-analysis: classes 15, methods 118, loops 9, streams 0, synchronized blocks 0
#### 1. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: issue654StackOverflowInput (line 3871)
- Pattern: allocation-pressure
- What was found: Loop at line 3871 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: Map<String, Number> map = new HashMap<>(); | assertThrows(JSONException.class, () -> new JSONObject(map));
#### 2. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: issue654StackOverflowInput (line 3881)
- Pattern: allocation-pressure
- What was found: Loop at line 3881 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: assertThrows(JSONException.class, () -> new JSONObject(bean));
#### 3. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: jsonObjectParseControlCharacterNewLineAssertExceptionMessage (line 2293)
- Pattern: allocation-pressure
- What was found: Loop at line 2293 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: JSONObject jo = new JSONObject(source);
#### 4. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: jsonObjectParseControlCharacters (line 2262)
- Pattern: allocation-pressure
- What was found: Loop at line 2262 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: JSONObject jo = new JSONObject(source);
#### 5. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: issue654StackOverflowInput (line 3871)
- Pattern: data-movement-bloat
- What was found: Loop at line 3871 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: assertThrows(JSONException.class, () -> new JSONObject(map));
#### 6. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: issue654StackOverflowInput (line 3881)
- Pattern: data-movement-bloat
- What was found: Loop at line 3881 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: assertThrows(JSONException.class, () -> new JSONObject(bean));
#### 7. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: jsonObjectParseControlCharacterNewLineAssertExceptionMessage (line 2293)
- Pattern: data-movement-bloat
- What was found: Loop at line 2293 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: JSONObject jo = new JSONObject(source);
#### 8. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: jsonObjectParseControlCharacters (line 2262)
- Pattern: data-movement-bloat
- What was found: Loop at line 2262 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: JSONObject jo = new JSONObject(source);
#### 9. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: issue654StackOverflowInput (line 3871)
- Pattern: repeated-work
- What was found: Loop at line 3871 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: Map<String, Number> map = new HashMap<>(); | assertThrows(JSONException.class, () -> new JSONObject(map));
#### 10. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: issue654StackOverflowInput (line 3881)
- Pattern: repeated-work
- What was found: Loop at line 3881 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: assertThrows(JSONException.class, () -> new JSONObject(bean));
#### 11. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: jsonObjectParseControlCharacterNewLineAssertExceptionMessage (line 2293)
- Pattern: repeated-work
- What was found: Loop at line 2293 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: JSONObject jo = new JSONObject(source);
#### 12. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: jsonObjectParseControlCharacters (line 2262)
- Pattern: repeated-work
- What was found: Loop at line 2262 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: JSONObject jo = new JSONObject(source);
#### 13. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: jsonObjectDoubleToString (line 917)
- Pattern: allocation-pressure
- What was found: Loop at line 917 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertTrue("value expected ["+expectedStrs[i]+ | "] found ["+actualStr+ "]",
#### 14. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: jsonObjectParseControlCharacterNewLineAssertExceptionMessage (line 2293)
- Pattern: allocation-pressure
- What was found: Loop at line 2293 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: final String source = "{\"key\":\"" + c + "\"}"; | assertEquals("Unterminated string. " + "Character with int code " + (int) c +
#### 15. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: jsonObjectParseControlCharacters (line 2262)
- Pattern: allocation-pressure
- What was found: Loop at line 2262 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: final String source = "{\"key\":\""+charString+"\"}"; | assertTrue("Expected "+charString+"("+i+") in the JSON Object but did not find it.",charString.equals(jo.getString("key"))); | assertTrue("Only \\0 (U+0000), \\n (U+000A), and \\r (U+000D) should cause an error. Instead "+charString+"("+i+") caused an error",

### `src\main\java\org\json\JSONML.java`

- Pre-analysis: classes 2, methods 1, loops 7, streams 0, synchronized blocks 0
#### 1. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: line 109
- Pattern: allocation-pressure
- What was found: Loop at line 109 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: newja = new JSONArray(); | newjo = new JSONObject();
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 674
- Pattern: algorithmic-waste
- What was found: Loop at line 674 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 674
#### 3. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: line 109
- Pattern: data-movement-bloat
- What was found: Loop at line 109 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: newja = new JSONArray(); | newjo = new JSONObject();
#### 4. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: line 570
- Pattern: data-movement-bloat
- What was found: Loop at line 570 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: sb.append(XML.escape(value.toString()));
#### 5. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: line 650
- Pattern: data-movement-bloat
- What was found: Loop at line 650 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: sb.append(XML.escape(value.toString()));
#### 6. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: line 674
- Pattern: data-movement-bloat
- What was found: Loop at line 674 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: sb.append(XML.escape(object.toString())); | sb.append(object.toString());
#### 7. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: line 109
- Pattern: repeated-work
- What was found: Loop at line 109 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: newja = new JSONArray(); | newjo = new JSONObject(); | closeTag = (String)parse(x, arrayForm, newja, config, currentNestingDepth + 1);
#### 8. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 109
- Pattern: allocation-pressure
- What was found: Loop at line 109 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: "Expected a closing name instead of '" + | throw x.syntaxError("Bad tagName '" + token + "'."); | throw x.syntaxError("Maximum nesting depth of " + config.getMaxNestingDepth() + " reached");

### `src\main\java\org\json\JSONObject.java`

- Pre-analysis: classes 34, methods 56, loops 21, streams 0, synchronized blocks 0
#### 1. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: line 555
- Pattern: allocation-pressure
- What was found: Loop at line 555 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: nextTarget = new JSONObject();
#### 2. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: line 566
- Pattern: allocation-pressure
- What was found: Loop at line 566 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: nextTarget = new JSONObject();
#### 3. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: line 223
- Pattern: data-movement-bloat
- What was found: Loop at line 223 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: if (parseJSONObject(x, jsonParserConfiguration, isInitial)) {
#### 4. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: line 555
- Pattern: data-movement-bloat
- What was found: Loop at line 555 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: JSONObject nextTarget = target.optJSONObject(segment); | nextTarget = new JSONObject();
#### 5. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: line 566
- Pattern: data-movement-bloat
- What was found: Loop at line 566 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: JSONObject nextTarget = target.optJSONObject(segment); | nextTarget = new JSONObject();
#### 6. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: line 555
- Pattern: repeated-work
- What was found: Loop at line 555 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: nextTarget = new JSONObject();
#### 7. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: line 566
- Pattern: repeated-work
- What was found: Loop at line 566 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: nextTarget = new JSONObject();

### `src\test\java\org\json\junit\JSONArrayTest.java`

- Pre-analysis: classes 8, methods 52, loops 6, streams 0, synchronized blocks 0
#### 1. List membership checks inside loop
- Severity: Medium
- Confidence: Medium
- Location: jsonArrayToStringIndent (line 993)
- Pattern: algorithmic-waste
- What was found: Loop at line 993 performs `.contains(...)` checks that may scan collections repeatedly.
- Why it is wasteful: Repeated linear scans inside iteration can push runtime toward O(n^2) as data sets grow.
- Likely impact: Throughput degradation and elevated CPU time for larger inputs.
- Recommended remediation: Use a `Set` for membership lookups or pre-index data before the loop.
- Low-waste rationale: Indexing once avoids repeated scans and reduces wasted CPU work.
- Evidence: line 993
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: jsonArrayToStringIndent (line 1000)
- Pattern: algorithmic-waste
- What was found: Loop at line 1000 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1000
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: jsonArrayToStringIndent (line 993)
- Pattern: algorithmic-waste
- What was found: Loop at line 993 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 993
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testJSONArrayConstructor (line 1372)
- Pattern: algorithmic-waste
- What was found: Loop at line 1372 is nested at depth 5 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1372
#### 5. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testJSONArrayPutAll (line 1392)
- Pattern: algorithmic-waste
- What was found: Loop at line 1392 is nested at depth 5 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1392
#### 6. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: verifyPutAll (line 281)
- Pattern: algorithmic-waste
- What was found: Loop at line 281 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 281
#### 7. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: testJSONArrayConstructor (line 1372)
- Pattern: allocation-pressure
- What was found: Loop at line 1372 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertEquals("index " + i + " are equal", a1.get(i), a2.get(i));
#### 8. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: testJSONArrayPutAll (line 1392)
- Pattern: allocation-pressure
- What was found: Loop at line 1392 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertEquals("index " + i + " are equal", a1.get(i), a2.get(i));

### `src\test\java\org\json\junit\JSONTokenerTest.java`

- Pre-analysis: classes 2, methods 8, loops 6, streams 0, synchronized blocks 0
#### 1. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: testNextBackComboWithNewLines (line 291)
- Pattern: data-movement-bloat
- What was found: Loop at line 291 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: assertTrue(t2.toString().startsWith(" at " + i + " "));
#### 2. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: testNextBackComboWithNewLines (line 298)
- Pattern: data-movement-bloat
- What was found: Loop at line 298 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: assertTrue(t2.toString().startsWith(" at " + i + " "));
#### 3. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: testNextBackComboWithNewLines (line 309)
- Pattern: data-movement-bloat
- What was found: Loop at line 309 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: assertTrue(t2.toString().startsWith(" at " + i + " "));
#### 4. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: testNextBackComboWithNewLines (line 314)
- Pattern: data-movement-bloat
- What was found: Loop at line 314 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: assertTrue(t2.toString().startsWith(" at " + i + " "));
#### 5. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: testNextBackComboWithNewLines (line 291)
- Pattern: allocation-pressure
- What was found: Loop at line 291 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertTrue(t2.toString().startsWith(" at " + i + " "));
#### 6. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: testNextBackComboWithNewLines (line 298)
- Pattern: allocation-pressure
- What was found: Loop at line 298 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertTrue(t2.toString().startsWith(" at " + i + " "));
#### 7. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: testNextBackComboWithNewLines (line 309)
- Pattern: allocation-pressure
- What was found: Loop at line 309 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertTrue(t2.toString().startsWith(" at " + i + " "));
#### 8. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: testNextBackComboWithNewLines (line 314)
- Pattern: allocation-pressure
- What was found: Loop at line 314 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertTrue(t2.toString().startsWith(" at " + i + " "));

### `src\main\java\org\json\CDL.java`

- Pre-analysis: classes 2, methods 3, loops 8, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: rowToString (line 181)
- Pattern: algorithmic-waste
- What was found: Loop at line 181 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 181
#### 2. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: line 306
- Pattern: data-movement-bloat
- What was found: Loop at line 306 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: JSONObject jo = rowToJSONObject(names, x, delimiter);
#### 3. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: line 391
- Pattern: data-movement-bloat
- What was found: Loop at line 391 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: JSONObject jo = ja.optJSONObject(i); | sb.append(rowToString(jo.toJSONArray(names), delimiter));
#### 4. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: rowToString (line 181)
- Pattern: data-movement-bloat
- What was found: Loop at line 181 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: String string = object.toString();
#### 5. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 102
- Pattern: allocation-pressure
- What was found: Loop at line 102 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw x.syntaxError("Bad character '" + c + "' (" +
#### 6. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 114
- Pattern: allocation-pressure
- What was found: Loop at line 114 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw x.syntaxError("Bad character '" + c + "' (" +
#### 7. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 56
- Pattern: allocation-pressure
- What was found: Loop at line 56 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw x.syntaxError("Missing close quote '" + q + "'.");

### `src\main\java\org\json\JSONTokener.java`

- Pre-analysis: classes 1, methods 12, loops 7, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: getPrevious (line 434)
- Pattern: algorithmic-waste
- What was found: Loop at line 434 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 434
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: getPrevious (line 501)
- Pattern: algorithmic-waste
- What was found: Loop at line 501 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 501
#### 3. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: getPrevious (line 345)
- Pattern: data-movement-bloat
- What was found: Loop at line 345 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: return sb.toString();
#### 4. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: getPrevious (line 410)
- Pattern: data-movement-bloat
- What was found: Loop at line 410 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: return sb.toString().trim();
#### 5. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: getPrevious (line 434)
- Pattern: data-movement-bloat
- What was found: Loop at line 434 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: return sb.toString().trim();
#### 6. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: getPrevious (line 345)
- Pattern: allocation-pressure
- What was found: Loop at line 345 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw this.syntaxError("Unterminated string. " + | "Character with int code " + (int) c + " is not allowed within a quoted string."); | throw this.syntaxError("Illegal escape. " +

### `src\main\java\org\json\XMLTokener.java`

- Pre-analysis: classes 1, methods 6, loops 15, streams 0, synchronized blocks 0
#### 1. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: line 106
- Pattern: data-movement-bloat
- What was found: Loop at line 106 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: return sb.toString().trim(); | return sb.toString().trim(); | } else return sb.toString();
#### 2. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: line 366
- Pattern: data-movement-bloat
- What was found: Loop at line 366 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: return sb.toString();
#### 3. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: line 385
- Pattern: data-movement-bloat
- What was found: Loop at line 385 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: return sb.toString(); | return sb.toString(); | return sb.toString();
#### 4. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: line 69
- Pattern: data-movement-bloat
- What was found: Loop at line 69 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: return sb.toString();
#### 5. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 137
- Pattern: allocation-pressure
- What was found: Loop at line 137 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw syntaxError("Missing ';' in XML entity: &" + sb);

### `src\main\java\org\json\JSONArray.java`

- Pre-analysis: classes 11, methods 67, loops 13, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 1996
- Pattern: algorithmic-waste
- What was found: Loop at line 1996 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1996
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 2000
- Pattern: algorithmic-waste
- What was found: Loop at line 2000 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 2000
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 621
- Pattern: algorithmic-waste
- What was found: Loop at line 621 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 621
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: similar (line 1635)
- Pattern: algorithmic-waste
- What was found: Loop at line 1635 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1635

### `src\test\java\org\json\junit\Util.java`

- Pre-analysis: classes 1, methods 6, loops 6, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: checkJSONObjectMaps (line 137)
- Pattern: algorithmic-waste
- What was found: Loop at line 137 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 137
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 30
- Pattern: algorithmic-waste
- What was found: Loop at line 30 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 30
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 48
- Pattern: algorithmic-waste
- What was found: Loop at line 48 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 48

### `src\main\java\org\json\CookieList.java`

- Pre-analysis: classes 2, methods 1, loops 2, streams 0, synchronized blocks 0
#### 1. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: line 60
- Pattern: chatty-io
- What was found: Loop at line 60 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: if (isEndOfPair) { | isEndOfPair = true;
#### 2. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: line 60
- Pattern: data-movement-bloat
- What was found: Loop at line 60 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: sb.append(Cookie.escape(value.toString()));

### `src\main\java\org\json\HTTPTokener.java`

- Pre-analysis: classes 1, methods 1, loops 3, streams 0, synchronized blocks 0
#### 1. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: line 38
- Pattern: data-movement-bloat
- What was found: Loop at line 38 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: return sb.toString();
#### 2. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: line 49
- Pattern: data-movement-bloat
- What was found: Loop at line 49 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: return sb.toString();

### `src\main\java\org\json\HTTP.java`

- Pre-analysis: classes 1, methods 1, loops 2, streams 0, synchronized blocks 0
#### 1. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: line 134
- Pattern: chatty-io
- What was found: Loop at line 134 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: if (!"HTTP-Version".equals(key)      && !"Status-Code".equals(key) && | !"Request-URI".equals(key)   && !JSONObject.NULL.equals(value)) {

### `src\main\java\org\json\Cookie.java`

- Pre-analysis: classes 2, methods 4, loops 5, streams 0, synchronized blocks 0
#### 1. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: line 162
- Pattern: data-movement-bloat
- What was found: Loop at line 162 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: .append(escape(value.toString()));

### `src\main\java\org\json\Property.java`

- Pre-analysis: classes 1, methods 1, loops 2, streams 0, synchronized blocks 0
#### 1. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: line 53
- Pattern: data-movement-bloat
- What was found: Loop at line 53 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: properties.put(key, value.toString());

## Cautions
- This is static analysis only; findings indicate likely waste patterns, not measured bottlenecks.
- Method extraction and loop classification are heuristic and may miss unconventional Java syntax.