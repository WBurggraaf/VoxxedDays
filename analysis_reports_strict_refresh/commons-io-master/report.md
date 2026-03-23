# commons-io-master Green Code Report

## Summary
- Project root: `C:\VoxxedDays\GitRepos\commons-io-master`
- Java files reviewed: 268
- Source files: 268
- Test files: 0
- Overall risk level: High
- Findings by severity: High 6, Medium 23, Low 5
- Top efficiency themes: Algorithmic waste, Concurrency misuse, Data movement bloat, Allocation pressure, Chatty I/O

## Hotspots
- `src\main\java\org\apache\commons\io\input\Tailer.java`: score 10, findings 4
- `src\main\java\org\apache\commons\io\input\ReadAheadInputStream.java`: score 9, findings 4
- `src\main\java\org\apache\commons\io\IOUtils.java`: score 6, findings 3
- `src\main\java\org\apache\commons\io\FileUtils.java`: score 5, findings 3
- `src\main\java\org\apache\commons\io\input\UnsynchronizedBufferedReader.java`: score 4, findings 2
- `src\main\java\org\apache\commons\io\input\ReaderInputStream.java`: score 4, findings 2
- `src\main\java\org\apache\commons\io\input\CharSequenceInputStream.java`: score 4, findings 2
- `src\main\java\org\apache\commons\io\file\PathUtils.java`: score 4, findings 2
- `src\main\java\org\apache\commons\io\FilenameUtils.java`: score 4, findings 2
- `src\main\java\org\apache\commons\io\monitor\FileAlterationMonitor.java`: score 3, findings 1

## File Findings
### `src\main\java\org\apache\commons\io\input\Tailer.java`

- Pre-analysis: classes 7, methods 36, loops 4, streams 0, synchronized blocks 0
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
- Evidence: * Thread thread = new Thread(tailer);
#### 2. Direct thread creation
- Severity: High
- Confidence: High
- Location: newDaemonThread (line 177)
- Pattern: concurrency-misuse
- What was found: Line 177 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: final Thread thread = new Thread(runnable, "commons-io-tailer");
#### 3. Executor created in application code path
- Severity: Medium
- Confidence: High
- Location: line 153
- Pattern: concurrency-misuse
- What was found: Line 153 creates a new executor instance.
- Why it is wasteful: Creating executors per call can fragment thread pools and increase context switching and idle threads.
- Likely impact: Higher memory use, poorer scheduling efficiency, and harder concurrency control.
- Recommended remediation: Reuse a bounded shared executor sized to the workload.
- Low-waste rationale: Bounded executor reuse reduces idle threads and CPU overhead without reducing useful throughput.
- Evidence: *   .setExecutorService(Executors.newSingleThreadExecutor(Builder::newDaemonThread))
#### 4. Executor created in application code path
- Severity: Medium
- Confidence: High
- Location: line 189
- Pattern: concurrency-misuse
- What was found: Line 189 creates a new executor instance.
- Why it is wasteful: Creating executors per call can fragment thread pools and increase context switching and idle threads.
- Likely impact: Higher memory use, poorer scheduling efficiency, and harder concurrency control.
- Recommended remediation: Reuse a bounded shared executor sized to the workload.
- Low-waste rationale: Bounded executor reuse reduces idle threads and CPU overhead without reducing useful throughput.
- Evidence: private ExecutorService executorService = Executors.newSingleThreadExecutor(Builder::newDaemonThread);

### `src\main\java\org\apache\commons\io\input\ReadAheadInputStream.java`

- Pre-analysis: classes 3, methods 11, loops 2, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: newDaemonThread (line 146)
- Pattern: concurrency-misuse
- What was found: Line 146 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: final Thread thread = new Thread(r, "commons-io-read-ahead");
#### 2. Executor created in application code path
- Severity: Medium
- Confidence: High
- Location: line 62
- Pattern: concurrency-misuse
- What was found: Line 62 creates a new executor instance.
- Why it is wasteful: Creating executors per call can fragment thread pools and increase context switching and idle threads.
- Likely impact: Higher memory use, poorer scheduling efficiency, and harder concurrency control.
- Recommended remediation: Reuse a bounded shared executor sized to the workload.
- Low-waste rationale: Bounded executor reuse reduces idle threads and CPU overhead without reducing useful throughput.
- Evidence: *   .setExecutorService(Executors.newSingleThreadExecutor(ReadAheadInputStream::newThread))
#### 3. Executor created in application code path
- Severity: Medium
- Confidence: High
- Location: newExecutorService (line 157)
- Pattern: concurrency-misuse
- What was found: Line 157 creates a new executor instance.
- Why it is wasteful: Creating executors per call can fragment thread pools and increase context switching and idle threads.
- Likely impact: Higher memory use, poorer scheduling efficiency, and harder concurrency control.
- Recommended remediation: Reuse a bounded shared executor sized to the workload.
- Low-waste rationale: Bounded executor reuse reduces idle threads and CPU overhead without reducing useful throughput.
- Evidence: return Executors.newSingleThreadExecutor(ReadAheadInputStream::newDaemonThread);
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 438
- Pattern: algorithmic-waste
- What was found: Loop at line 438 is nested at depth 5 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 438

### `src\main\java\org\apache\commons\io\IOUtils.java`

- Pre-analysis: classes 12, methods 65, loops 24, streams 0, synchronized blocks 6
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 2585
- Pattern: algorithmic-waste
- What was found: Loop at line 2585 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 2585
#### 2. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: line 3931
- Pattern: data-movement-bloat
- What was found: Loop at line 3931 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: write(line.toString(), output, charset);
#### 3. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: line 3976
- Pattern: data-movement-bloat
- What was found: Loop at line 3976 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: writer.write(line.toString());

### `src\main\java\org\apache\commons\io\FileUtils.java`

- Pre-analysis: classes 1, methods 62, loops 10, streams 3, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 1372
- Pattern: algorithmic-waste
- What was found: Loop at line 1372 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1372
#### 2. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: decodeUrl (line 1205)
- Pattern: data-movement-bloat
- What was found: Loop at line 1205 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: builder.append(StandardCharsets.UTF_8.decode(byteBuffer).toString());
#### 3. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: toFiles (line 3093)
- Pattern: allocation-pressure
- What was found: Loop at line 3093 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw new IllegalArgumentException("Can only convert file URL to a File: " + url);

### `src\main\java\org\apache\commons\io\file\PathUtils.java`

- Pre-analysis: classes 2, methods 40, loops 4, streams 1, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 351
- Pattern: algorithmic-waste
- What was found: Loop at line 351 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 351
#### 2. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: line 751
- Pattern: data-movement-bloat
- What was found: Loop at line 751 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: Comparator.comparing(p -> RelativeSortedPaths.extractKey(p.getFileSystem().getSeparator(), p.toString()))); | if (!fileContentEquals(path1.resolve(path.toString()), path2.resolve(path.toString()), linkOptions, openOptions)) {

### `src\main\java\org\apache\commons\io\FilenameUtils.java`

- Pre-analysis: classes 8, methods 46, loops 11, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: isIPv6Address (line 1134)
- Pattern: algorithmic-waste
- What was found: Loop at line 1134 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1134
#### 2. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: splitOnTokens (line 1510)
- Pattern: data-movement-bloat
- What was found: Loop at line 1510 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: list.add(buffer.toString());

### `src\main\java\org\apache\commons\io\input\CharSequenceInputStream.java`

- Pre-analysis: classes 2, methods 15, loops 4, streams 0, synchronized blocks 2
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 304
- Pattern: algorithmic-waste
- What was found: Loop at line 304 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 304
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 330
- Pattern: algorithmic-waste
- What was found: Loop at line 330 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 330

### `src\main\java\org\apache\commons\io\input\ReaderInputStream.java`

- Pre-analysis: classes 6, methods 16, loops 2, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 419
- Pattern: algorithmic-waste
- What was found: Loop at line 419 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 419
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 461
- Pattern: algorithmic-waste
- What was found: Loop at line 461 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 461

### `src\main\java\org\apache\commons\io\input\UnsynchronizedBufferedReader.java`

- Pre-analysis: classes 2, methods 3, loops 5, streams 0, synchronized blocks 4
#### 1. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: line 371
- Pattern: data-movement-bloat
- What was found: Loop at line 371 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: return result.toString(); | return result.length() > 0 || eol != NUL ? result.toString() : null; | return result.toString();
#### 2. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: line 383
- Pattern: data-movement-bloat
- What was found: Loop at line 383 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: return result.toString();

### `src\main\java\org\apache\commons\io\FileCleaningTracker.java`

- Pre-analysis: classes 9, methods 16, loops 1, streams 0, synchronized blocks 7
#### 1. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: run (line 69)
- Pattern: chatty-io
- What was found: Loop at line 69 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: if (!tracker.delete()) {

### `src\main\java\org\apache\commons\io\monitor\FileAlterationMonitor.java`

- Pre-analysis: classes 1, methods 10, loops 3, streams 0, synchronized blocks 4
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 182
- Pattern: concurrency-misuse
- What was found: Line 182 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: thread = new Thread(this, "commons-io-FileAlterationMonitor");

### `src\main\java\org\apache\commons\io\ThreadMonitor.java`

- Pre-analysis: classes 1, methods 5, loops 0, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: start (line 63)
- Pattern: concurrency-misuse
- What was found: Line 63 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: final Thread monitor = new Thread(new ThreadMonitor(thread, timeout), "commons-io-ThreadMonitor");

### `src\main\java\org\apache\commons\io\build\AbstractOrigin.java`

- Pre-analysis: classes 16, methods 43, loops 2, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 465
- Pattern: allocation-pressure
- What was found: Loop at line 465 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw new UnsupportedOperationException("Only READ is supported for byte[] origins: " + Arrays.toString(options));
#### 2. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 586
- Pattern: allocation-pressure
- What was found: Loop at line 586 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw new UnsupportedOperationException("Only READ is supported for CharSequence origins: " + Arrays.toString(options));

### `src\main\java\org\apache\commons\io\ByteOrderMark.java`

- Pre-analysis: classes 1, methods 10, loops 5, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: equals (line 165)
- Pattern: algorithmic-waste
- What was found: Loop at line 165 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 165

### `src\main\java\org\apache\commons\io\filefilter\AbstractFileFilter.java`

- Pre-analysis: classes 1, methods 13, loops 2, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: append (line 103)
- Pattern: algorithmic-waste
- What was found: Loop at line 103 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 103

### `src\main\java\org\apache\commons\io\input\XmlStreamReader.java`

- Pre-analysis: classes 4, methods 12, loops 1, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 331
- Pattern: algorithmic-waste
- What was found: Loop at line 331 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 331

### `src\main\java\org\apache\commons\io\input\CircularInputStream.java`

- Pre-analysis: classes 2, methods 3, loops 1, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: validate (line 45)
- Pattern: allocation-pressure
- What was found: Loop at line 45 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw new IllegalArgumentException("repeatContent contains the end-of-stream marker " + IOUtils.EOF);

### `src\main\java\org\apache\commons\io\input\ReversedLinesFileReader.java`

- Pre-analysis: classes 3, methods 7, loops 5, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: readLine (line 222)
- Pattern: allocation-pressure
- What was found: Loop at line 222 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw new IllegalStateException("Unexpected negative line length=" + lineLengthBytes);

## Cautions
- This is static analysis only; findings indicate likely waste patterns, not measured bottlenecks.
- Method extraction and loop classification are heuristic and may miss unconventional Java syntax.