# JSON-java-master Green Code Report

## Summary
- Project root: `C:\VoxxedDays\GitRepos\JSON-java-master`
- Java files reviewed: 26
- Source files: 26
- Test files: 0
- Overall risk level: High
- Findings by severity: High 0, Medium 51, Low 9
- Top efficiency themes: Data movement bloat, Allocation pressure, Algorithmic waste, Repeated work

## Hotspots
- `src\main\java\org\json\XML.java`: score 33, findings 18
- `src\main\java\org\json\JSONML.java`: score 15, findings 8
- `src\main\java\org\json\JSONObject.java`: score 14, findings 7
- `src\main\java\org\json\JSONTokener.java`: score 11, findings 6
- `src\main\java\org\json\CDL.java`: score 11, findings 7
- `src\main\java\org\json\XMLTokener.java`: score 9, findings 5
- `src\main\java\org\json\JSONArray.java`: score 8, findings 4
- `src\main\java\org\json\HTTPTokener.java`: score 4, findings 2
- `src\main\java\org\json\Property.java`: score 2, findings 1
- `src\main\java\org\json\CookieList.java`: score 2, findings 1

## File Findings
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

### `src\main\java\org\json\CookieList.java`

- Pre-analysis: classes 2, methods 1, loops 2, streams 0, synchronized blocks 0
#### 1. Payload construction inside loop
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