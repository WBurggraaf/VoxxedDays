# jackson-core-3.x Green Code Report

## Summary
- Project root: `C:\VoxxedDays\GitRepos\jackson-core-3.x`
- Java files reviewed: 138
- Source files: 138
- Test files: 0
- Overall risk level: Medium
- Findings by severity: High 2, Medium 9, Low 12
- Top efficiency themes: Allocation pressure, Algorithmic waste, Data movement bloat, Concurrency misuse, Repeated work

## Hotspots
- `src\main\java\tools\jackson\core\JsonPointer.java`: score 8, findings 4
- `src\main\java\tools\jackson\core\util\TextBuffer.java`: score 6, findings 3
- `src\main\java\tools\jackson\core\util\JsonRecyclerPools.java`: score 6, findings 2
- `src\main\java\tools\jackson\core\json\UTF8StreamJsonParser.java`: score 3, findings 3
- `src\main\java\tools\jackson\core\json\UTF8DataInputJsonParser.java`: score 3, findings 3
- `src\main\java\tools\jackson\core\sym\SimpleNameMatcher.java`: score 2, findings 1
- `src\main\java\tools\jackson\core\json\ReaderBasedJsonParser.java`: score 2, findings 2
- `src\main\java\tools\jackson\core\JsonGenerator.java`: score 2, findings 2
- `src\main\java\tools\jackson\core\JacksonException.java`: score 2, findings 1
- `src\main\java\tools\jackson\core\filter\FilteringParserDelegate.java`: score 1, findings 1

## File Findings
### `src\main\java\tools\jackson\core\JsonPointer.java`

- Pre-analysis: classes 7, methods 4, loops 12, streams 0, synchronized blocks 0
#### 1. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: valueOf (line 740)
- Pattern: allocation-pressure
- What was found: Loop at line 740 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: StringBuilder sb = new StringBuilder(32);
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: valueOf (line 863)
- Pattern: algorithmic-waste
- What was found: Loop at line 863 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 863
#### 3. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: valueOf (line 740)
- Pattern: data-movement-bloat
- What was found: Loop at line 740 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: final String segment = sb.toString();
#### 4. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: valueOf (line 740)
- Pattern: repeated-work
- What was found: Loop at line 740 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: StringBuilder sb = new StringBuilder(32);

### `src\main\java\tools\jackson\core\util\JsonRecyclerPools.java`

- Pre-analysis: classes 5, methods 17, loops 0, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 105
- Pattern: concurrency-misuse
- What was found: Line 105 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: protected static final ThreadLocalPool GLOBAL = new ThreadLocalPool();
#### 2. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 113
- Pattern: concurrency-misuse
- What was found: Line 113 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: = new ThreadLocal<SoftReference<BufferRecycler>>();

### `src\main\java\tools\jackson\core\util\TextBuffer.java`

- Pre-analysis: classes 2, methods 11, loops 7, streams 0, synchronized blocks 1
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: getCurrentSegmentSize (line 1205)
- Pattern: algorithmic-waste
- What was found: Loop at line 1205 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1205
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 542
- Pattern: algorithmic-waste
- What was found: Loop at line 542 is nested at depth 7 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 542
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 759
- Pattern: algorithmic-waste
- What was found: Loop at line 759 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 759

### `src\main\java\tools\jackson\core\json\UTF8DataInputJsonParser.java`

- Pre-analysis: classes 1, methods 7, loops 35, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: _closeInput (line 454)
- Pattern: allocation-pressure
- What was found: Loop at line 454 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: _reportInvalidBase64Char(b64variant, ch, 3, "expected padding character '"+b64variant.getPaddingChar()+"'");
#### 2. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 2435
- Pattern: allocation-pressure
- What was found: Loop at line 2435 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: match = neg ? "-INF" :"+INF"; | match = neg ? "-Infinity" :"+Infinity"; | _reportError("Non-standard token '"+match+"': enable `JsonReadFeature.ALLOW_NON_NUMERIC_NUMBERS` to allow");
#### 3. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 3045
- Pattern: allocation-pressure
- What was found: Loop at line 3045 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: _reportInvalidBase64Char(b64variant, ch, 3, "expected padding character '"+b64variant.getPaddingChar()+"'");

### `src\main\java\tools\jackson\core\json\UTF8StreamJsonParser.java`

- Pre-analysis: classes 1, methods 4, loops 43, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 3427
- Pattern: allocation-pressure
- What was found: Loop at line 3427 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: match = neg ? "-INF" :"+INF"; | match = neg ? "-Infinity" :"+Infinity";
#### 2. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 4290
- Pattern: allocation-pressure
- What was found: Loop at line 4290 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: _reportInvalidBase64Char(b64variant, ch, 3, "expected padding character '"+b64variant.getPaddingChar()+"'");
#### 3. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 568
- Pattern: allocation-pressure
- What was found: Loop at line 568 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: return _reportInvalidBase64Char(b64variant, ch, 3, "expected padding character '"+b64variant.getPaddingChar()+"'");

### `src\main\java\tools\jackson\core\JacksonException.java`

- Pre-analysis: classes 4, methods 14, loops 3, streams 0, synchronized blocks 0
#### 1. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: getLocation (line 553)
- Pattern: data-movement-bloat
- What was found: Loop at line 553 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: sb.append(it.next().toString());

### `src\main\java\tools\jackson\core\json\ReaderBasedJsonParser.java`

- Pre-analysis: classes 1, methods 3, loops 34, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 2932
- Pattern: allocation-pressure
- What was found: Loop at line 2932 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: _reportInvalidBase64Char(b64variant, ch, 3, "expected padding character '"+b64variant.getPaddingChar()+"'");
#### 2. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 538
- Pattern: allocation-pressure
- What was found: Loop at line 538 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: _reportInvalidBase64Char(b64variant, ch, 3, "expected padding character '"+b64variant.getPaddingChar()+"'");

### `src\main\java\tools\jackson\core\JsonGenerator.java`

- Pre-analysis: classes 2, methods 1, loops 6, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: JsonGenerator (line 2155)
- Pattern: allocation-pressure
- What was found: Loop at line 2155 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw new IllegalStateException("Internal error: unknown current token, "+t);
#### 2. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: JsonGenerator (line 2217)
- Pattern: allocation-pressure
- What was found: Loop at line 2217 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw new IllegalStateException("Internal error: unknown current token, "+t);

### `src\main\java\tools\jackson\core\sym\SimpleNameMatcher.java`

- Pre-analysis: classes 1, methods 4, loops 1, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 70
- Pattern: algorithmic-waste
- What was found: Loop at line 70 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 70

### `src\main\java\tools\jackson\core\Base64Variant.java`

- Pre-analysis: classes 2, methods 8, loops 5, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: getName (line 696)
- Pattern: allocation-pressure
- What was found: Loop at line 696 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: _reportInvalidBase64(ch, 3, "expected padding character '"+getPaddingChar()+"'");

### `src\main\java\tools\jackson\core\filter\FilteringParserDelegate.java`

- Pre-analysis: classes 1, methods 2, loops 5, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: getFilter (line 288)
- Pattern: allocation-pressure
- What was found: Loop at line 288 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw _constructReadException("Unexpected problem: chain of filtered context broken, token: "+t);

## Cautions
- This is static analysis only; findings indicate likely waste patterns, not measured bottlenecks.
- Method extraction and loop classification are heuristic and may miss unconventional Java syntax.