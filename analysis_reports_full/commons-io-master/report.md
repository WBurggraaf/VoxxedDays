# commons-io-master Green Code Report

## Summary
- Project root: `C:\VoxxedDays\GitRepos\commons-io-master`
- Java files reviewed: 555
- Source files: 268
- Test files: 287
- Overall risk level: High
- Findings by severity: High 44, Medium 66, Low 73
- Top efficiency themes: Allocation pressure, Algorithmic waste, Concurrency misuse, Chatty I/O, Data movement bloat

## Hotspots
- `src\test\java\org\apache\commons\io\input\TailerTest.java`: score 60, findings 22
- `src\test\java\org\apache\commons\io\IOUtilsMultithreadedSkipTest.java`: score 14, findings 8
- `src\test\java\org\apache\commons\io\LineIteratorTest.java`: score 13, findings 9
- `src\main\java\org\apache\commons\io\input\Tailer.java`: score 13, findings 5
- `src\test\java\org\apache\commons\io\FileUtilsTest.java`: score 12, findings 7
- `src\test\java\org\apache\commons\io\FileSystemTest.java`: score 12, findings 7
- `src\main\java\org\apache\commons\io\IOUtils.java`: score 12, findings 5
- `src\test\java\org\apache\commons\io\input\BoundedInputStreamTest.java`: score 10, findings 10
- `src\test\java\org\apache\commons\io\IOUtilsConcurrentTest.java`: score 10, findings 4
- `src\main\java\org\apache\commons\io\input\ReadAheadInputStream.java`: score 9, findings 4

## File Findings
### `src\test\java\org\apache\commons\io\input\TailerTest.java`

- Pre-analysis: classes 3, methods 12, loops 9, streams 0, synchronized blocks 2
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 242
- Pattern: concurrency-misuse
- What was found: Line 242 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: final Thread thread = new Thread(tailer, "commons-io-tailer-testBufferBreak");
#### 2. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 350
- Pattern: concurrency-misuse
- What was found: Line 350 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: final Thread thread = new Thread(tailer, "commons-io-tailer-testInterrupt");
#### 3. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 373
- Pattern: concurrency-misuse
- What was found: Line 373 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: final Thread thread = new Thread(tailer, "commons-io-tailer-testIO335");
#### 4. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 403
- Pattern: concurrency-misuse
- What was found: Line 403 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: final Thread thread = new Thread(tailer, "commons-io-tailer-testLongFile");
#### 5. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 428
- Pattern: concurrency-misuse
- What was found: Line 428 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: final Thread thread = new Thread(tailer, "commons-io-tailer-testMultiByteBreak");
#### 6. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 461
- Pattern: concurrency-misuse
- What was found: Line 461 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: final Thread thread = new Thread(tailer, "commons-io-tailer-testSimpleConstructor");
#### 7. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 473
- Pattern: concurrency-misuse
- What was found: Line 473 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: final Thread thread = new Thread(tailer, "commons-io-tailer-testSimpleConstructorWithDelay");
#### 8. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 485
- Pattern: concurrency-misuse
- What was found: Line 485 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: final Thread thread = new Thread(tailer, "commons-io-tailer-testSimpleConstructorWithDelayAndFromStart");
#### 9. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 497
- Pattern: concurrency-misuse
- What was found: Line 497 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: final Thread thread = new Thread(tailer, "commons-io-tailer-testSimpleConstructorWithDelayAndFromStartWithBufferSize");
#### 10. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 509
- Pattern: concurrency-misuse
- What was found: Line 509 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: final Thread thread = new Thread(tailer, "commons-io-tailer-testSimpleConstructorWithDelayAndFromStartWithReopen");
#### 11. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 521
- Pattern: concurrency-misuse
- What was found: Line 521 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: final Thread thread = new Thread(tailer, "commons-io-tailer-testSimpleConstructorWithDelayAndFromStartWithReopenAndBufferSize");
#### 12. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 533
- Pattern: concurrency-misuse
- What was found: Line 533 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: final Thread thread = new Thread(tailer, "commons-io-tailer-testSimpleConstructorWithDelayAndFromStartWithReopenAndBufferSizeAndCharset");
#### 13. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 590
- Pattern: concurrency-misuse
- What was found: Line 590 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: final Thread thread = new Thread(tailer, "commons-io-tailer-testTailer");
#### 14. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 652
- Pattern: concurrency-misuse
- What was found: Line 652 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: final Thread thread = new Thread(tailer, "commons-io-tailer-testTailerEndOfFileReached");
#### 15. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 676
- Pattern: concurrency-misuse
- What was found: Line 676 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: final Thread thread = new Thread(tailer, "commons-io-tailer-testTailerEof");
#### 16. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 701
- Pattern: concurrency-misuse
- What was found: Line 701 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: final Thread thread = new Thread(tailer, "commons-io-tailer-testTailerIgnoreTouch");
#### 17. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 727
- Pattern: concurrency-misuse
- What was found: Line 727 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: final Thread thread = new Thread(tailer, "commons-io-tailer-testTailerReissueOnTouch");
#### 18. Executor created in application code path
- Severity: Medium
- Confidence: High
- Location: line 259
- Pattern: concurrency-misuse
- What was found: Line 259 creates a new executor instance.
- Why it is wasteful: Creating executors per call can fragment thread pools and increase context switching and idle threads.
- Likely impact: Higher memory use, poorer scheduling efficiency, and harder concurrency control.
- Recommended remediation: Reuse a bounded shared executor sized to the workload.
- Low-waste rationale: Bounded executor reuse reduces idle threads and CPU overhead without reducing useful throughput.
- Evidence: .setExecutorService(Executors.newSingleThreadExecutor())
#### 19. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 246
- Pattern: algorithmic-waste
- What was found: Loop at line 246 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 246
#### 20. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 406
- Pattern: algorithmic-waste
- What was found: Loop at line 406 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 406
#### 21. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 444
- Pattern: algorithmic-waste
- What was found: Loop at line 444 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 444
#### 22. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 444
- Pattern: allocation-pressure
- What was found: Loop at line 444 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: fail("Line: " + i + "\nExp: (" + expected.length() + ") " + expected + "\nAct: (" + actual.length() + ") " + actual);

### `src\test\java\org\apache\commons\io\IOUtilsMultithreadedSkipTest.java`

- Pre-analysis: classes 1, methods 2, loops 6, streams 0, synchronized blocks 0
#### 1. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: line 103
- Pattern: chatty-io
- What was found: Loop at line 103 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: executorCompletionService.submit(() -> {
#### 2. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: line 123
- Pattern: chatty-io
- What was found: Loop at line 123 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: final Future<Integer> future = executorCompletionService.take();
#### 3. Executor created in application code path
- Severity: Medium
- Confidence: High
- Location: line 100
- Pattern: concurrency-misuse
- What was found: Line 100 creates a new executor instance.
- Why it is wasteful: Creating executors per call can fragment thread pools and increase context switching and idle threads.
- Likely impact: Higher memory use, poorer scheduling efficiency, and harder concurrency control.
- Recommended remediation: Reuse a bounded shared executor sized to the workload.
- Low-waste rationale: Bounded executor reuse reduces idle threads and CPU overhead without reducing useful throughput.
- Evidence: final ExecutorService executorService = Executors.newFixedThreadPool(numThreads);
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 123
- Pattern: algorithmic-waste
- What was found: Loop at line 123 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 123
#### 5. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 103
- Pattern: allocation-pressure
- What was found: Loop at line 103 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertEquals(expected[skipIndex], c, "failed on seed=" + seed + " iteration=" + iteration); | assertEquals(expected[skipIndex], is.read(), "failed on seed=" + seed + " iteration=" + iteration);
#### 6. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 105
- Pattern: allocation-pressure
- What was found: Loop at line 105 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertEquals(expected[skipIndex], c, "failed on seed=" + seed + " iteration=" + iteration); | assertEquals(expected[skipIndex], is.read(), "failed on seed=" + seed + " iteration=" + iteration);
#### 7. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 107
- Pattern: allocation-pressure
- What was found: Loop at line 107 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertEquals(expected[skipIndex], c, "failed on seed=" + seed + " iteration=" + iteration); | assertEquals(expected[skipIndex], is.read(), "failed on seed=" + seed + " iteration=" + iteration);
#### 8. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 123
- Pattern: allocation-pressure
- What was found: Loop at line 123 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: fail("failed on seed=" + seed);

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
#### 3. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: run (line 1007)
- Pattern: chatty-io
- What was found: Loop at line 1007 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: try (RandomAccessResourceBridge save = reader) { | readLines(save);
#### 4. Executor created in application code path
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
#### 5. Executor created in application code path
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

### `src\test\java\org\apache\commons\io\LineIteratorTest.java`

- Pre-analysis: classes 1, methods 4, loops 6, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: assertLines (line 53)
- Pattern: algorithmic-waste
- What was found: Loop at line 53 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 53
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 121
- Pattern: algorithmic-waste
- What was found: Loop at line 121 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 121
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 176
- Pattern: algorithmic-waste
- What was found: Loop at line 176 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 176
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 275
- Pattern: algorithmic-waste
- What was found: Loop at line 275 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 275
#### 5. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: assertLines (line 53)
- Pattern: allocation-pressure
- What was found: Loop at line 53 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertEquals(lines.get(i), line, "nextLine() line " + i);
#### 6. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: createStringLines (line 98)
- Pattern: allocation-pressure
- What was found: Loop at line 98 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: lines.add("LINE " + i);
#### 7. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 121
- Pattern: allocation-pressure
- What was found: Loop at line 121 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertEquals(lines.get(idx), line, "Comparing line " + idx); | assertTrue(idx < lines.size(), "Exceeded expected idx=" + idx + " size=" + lines.size());
#### 8. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 176
- Pattern: allocation-pressure
- What was found: Loop at line 176 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertEquals(lines.get(idx), line, "Comparing line " + idx); | assertTrue(idx < lines.size(), "Exceeded expected idx=" + idx + " size=" + lines.size());
#### 9. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 275
- Pattern: allocation-pressure
- What was found: Loop at line 275 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertEquals(lines.get(i), line, "next() line " + i);

### `src\main\java\org\apache\commons\io\IOUtils.java`

- Pre-analysis: classes 12, methods 65, loops 24, streams 0, synchronized blocks 6
#### 1. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: line 2585
- Pattern: chatty-io
- What was found: Loop at line 2585 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: // See https://issues.apache.org/jira/browse/IO-203 for why we use read() rather than delegating to skip()
#### 2. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: line 2650
- Pattern: chatty-io
- What was found: Loop at line 2650 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: // See https://issues.apache.org/jira/browse/IO-203 for why we use read() rather than delegating to skip()
#### 3. Nested loop with repeated lookup work
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
#### 4. Payload construction inside loop
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
#### 5. Payload construction inside loop
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

### `src\test\java\org\apache\commons\io\FileSystemTest.java`

- Pre-analysis: classes 1, methods 19, loops 16, streams 0, synchronized blocks 0
#### 1. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: testMaxNameLength_MatchesRealSystem (line 408)
- Pattern: chatty-io
- What was found: Loop at line 408 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: assertDoesNotThrow(() -> createAndDelete(tempDir, fileName), "OS should accept max-length name: " + fileName); | createAndDelete(tempDir, tooLongName);
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testIsReservedFileNameOnWindows (line 352)
- Pattern: algorithmic-waste
- What was found: Loop at line 352 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 352
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testIsReservedFileNameOnWindows (line 360)
- Pattern: algorithmic-waste
- What was found: Loop at line 360 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 360
#### 4. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: testIsReservedFileNameOnWindows (line 360)
- Pattern: data-movement-bloat
- What was found: Loop at line 360 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: //            assertEquals(exists, Files.exists(path), path.toString());
#### 5. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 536
- Pattern: allocation-pressure
- What was found: Loop at line 536 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertEquals(name1, xmlFromPath, "i =  " + i); | assertEquals(name1, parsedValue, "i =  " + i); | assertEquals(name2, parsedValue, "i =  " + i);
#### 6. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 554
- Pattern: allocation-pressure
- What was found: Loop at line 554 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: //            assertEquals(name1, xmlFromPath, "i =  " + i); | //            assertEquals(name1, parsedValue, "i =  " + i); | //            assertEquals(name2, parsedValue, "i =  " + i);
#### 7. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: testMaxNameLength_MatchesRealSystem (line 408)
- Pattern: allocation-pressure
- What was found: Loop at line 408 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertDoesNotThrow(() -> createAndDelete(tempDir, fileName), "OS should accept max-length name: " + fileName); | assertTrue(fs.isLegalFileName(fileName, UTF_8), "Commons IO should accept max-length name: " + fileName); | assertFalse(fs.isLegalFileName(tooLongName, UTF_8), "Commons IO should reject too-long name: " + tooLongName);

### `src\test\java\org\apache\commons\io\FileUtilsTest.java`

- Pre-analysis: classes 2, methods 54, loops 8, streams 1, synchronized blocks 0
#### 1. List membership checks inside loop
- Severity: Medium
- Confidence: Medium
- Location: line 295
- Pattern: algorithmic-waste
- What was found: Loop at line 295 performs `.contains(...)` checks that may scan collections repeatedly.
- Why it is wasteful: Repeated linear scans inside iteration can push runtime toward O(n^2) as data sets grow.
- Likely impact: Throughput degradation and elevated CPU time for larger inputs.
- Recommended remediation: Use a `Set` for membership lookups or pre-index data before the loop.
- Low-waste rationale: Indexing once avoids repeated scans and reduces wasted CPU work.
- Evidence: line 295
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 2192
- Pattern: algorithmic-waste
- What was found: Loop at line 2192 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 2192
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 2210
- Pattern: algorithmic-waste
- What was found: Loop at line 2210 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 2210
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 2215
- Pattern: algorithmic-waste
- What was found: Loop at line 2215 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 2215
#### 5. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 295
- Pattern: algorithmic-waste
- What was found: Loop at line 295 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 295
#### 6. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 2295
- Pattern: allocation-pressure
- What was found: Loop at line 2295 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: fail("Cannot create file " + theFile + " as the parent directory does not exist");
#### 7. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 295
- Pattern: allocation-pressure
- What was found: Loop at line 295 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: () -> "Unexpected directory/file " + file + ", expected one of " + expectedFilesAndDirs);

### `src\test\java\org\apache\commons\io\input\BoundedInputStreamTest.java`

- Pre-analysis: classes 1, methods 4, loops 10, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: compare (line 123)
- Pattern: allocation-pressure
- What was found: Loop at line 123 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertEquals(expected[i], actual[i], () -> message + " byte[" + mi + "]");
#### 2. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 225
- Pattern: allocation-pressure
- What was found: Loop at line 225 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertEquals(expectedCh, actualCh, "limit = length byte[" + i + "]"); | assertEquals(actualStart + readCount, bounded.getCount(), "i=" + i);
#### 3. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 256
- Pattern: allocation-pressure
- What was found: Loop at line 256 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertEquals(expectedCh, actualCh, "limit = length byte[" + i + "]"); | assertEquals(actualStart + readCount, bounded.getCount(), "i=" + i);
#### 4. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 284
- Pattern: allocation-pressure
- What was found: Loop at line 284 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertEquals(hello[i], bounded.read(), "limit < length byte[" + i + "]");
#### 5. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 450
- Pattern: allocation-pressure
- What was found: Loop at line 450 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertEquals(helloWorld[i], bounded.read(), "limit = length byte[" + i + "]");
#### 6. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 482
- Pattern: allocation-pressure
- What was found: Loop at line 482 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertEquals(helloWorld[i], bounded.read(), "limit > length byte[" + i + "]");
#### 7. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 511
- Pattern: allocation-pressure
- What was found: Loop at line 511 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertEquals(hello[i], bounded.read(), "limit < length byte[" + i + "]");
#### 8. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 625
- Pattern: allocation-pressure
- What was found: Loop at line 625 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertEquals(helloWorld[i], bounded.read(), "limit = length byte[" + i + "]");
#### 9. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 636
- Pattern: allocation-pressure
- What was found: Loop at line 636 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertEquals(helloWorld[i], bounded.read(), "limit > length byte[" + i + "]");
#### 10. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 646
- Pattern: allocation-pressure
- What was found: Loop at line 646 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertEquals(hello[i], bounded.read(), "limit < length byte[" + i + "]");

### `src\test\java\org\apache\commons\io\IOUtilsConcurrentTest.java`

- Pre-analysis: classes 2, methods 4, loops 4, streams 0, synchronized blocks 0
#### 1. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: line 133
- Pattern: chatty-io
- What was found: Loop at line 133 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: checksum.update(data, 0 , data.length);
#### 2. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: line 147
- Pattern: chatty-io
- What was found: Loop at line 147 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: checksum.update(bytes, 0, bytes.length);
#### 3. Executor created in application code path
- Severity: Medium
- Confidence: High
- Location: line 182
- Pattern: concurrency-misuse
- What was found: Line 182 creates a new executor instance.
- Why it is wasteful: Creating executors per call can fragment thread pools and increase context switching and idle threads.
- Likely impact: Higher memory use, poorer scheduling efficiency, and harder concurrency control.
- Recommended remediation: Reuse a bounded shared executor sized to the workload.
- Low-waste rationale: Bounded executor reuse reduces idle threads and CPU overhead without reducing useful throughput.
- Evidence: final ExecutorService threadPool = Executors.newFixedThreadPool(THREAD_COUNT);
#### 4. Executor created in application code path
- Severity: Medium
- Confidence: High
- Location: line 205
- Pattern: concurrency-misuse
- What was found: Line 205 creates a new executor instance.
- Why it is wasteful: Creating executors per call can fragment thread pools and increase context switching and idle threads.
- Likely impact: Higher memory use, poorer scheduling efficiency, and harder concurrency control.
- Recommended remediation: Reuse a bounded shared executor sized to the workload.
- Low-waste rationale: Bounded executor reuse reduces idle threads and CPU overhead without reducing useful throughput.
- Evidence: final ExecutorService threadPool = Executors.newFixedThreadPool(THREAD_COUNT);

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

### `src\test\java\org\apache\commons\io\DirectoryWalkerTest.java`

- Pre-analysis: classes 6, methods 32, loops 5, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: checkContainsFiles (line 277)
- Pattern: algorithmic-waste
- What was found: Loop at line 277 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 277
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: checkContainsString (line 283)
- Pattern: algorithmic-waste
- What was found: Loop at line 283 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 283
#### 3. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: checkContainsString (line 283)
- Pattern: data-movement-bloat
- What was found: Loop at line 283 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: assertTrue(results.contains(files[i].toString()), prefix + "[" + i + "] " + files[i]);
#### 4. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: checkContainsFiles (line 277)
- Pattern: allocation-pressure
- What was found: Loop at line 277 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertTrue(results.contains(files[i]), prefix + "[" + i + "] " + files[i]);
#### 5. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: checkContainsString (line 283)
- Pattern: allocation-pressure
- What was found: Loop at line 283 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertTrue(results.contains(files[i].toString()), prefix + "[" + i + "] " + files[i]);

### `src\test\java\org\apache\commons\io\file\AccumulatorPathVisitorTest.java`

- Pre-analysis: classes 1, methods 3, loops 4, streams 0, synchronized blocks 0
#### 1. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: line 220
- Pattern: chatty-io
- What was found: Loop at line 220 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: Files.delete(file);
#### 2. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: line 265
- Pattern: chatty-io
- What was found: Loop at line 265 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: Files.delete(file);
#### 3. Executor created in application code path
- Severity: Medium
- Confidence: High
- Location: line 216
- Pattern: concurrency-misuse
- What was found: Line 216 creates a new executor instance.
- Why it is wasteful: Creating executors per call can fragment thread pools and increase context switching and idle threads.
- Likely impact: Higher memory use, poorer scheduling efficiency, and harder concurrency control.
- Recommended remediation: Reuse a bounded shared executor sized to the workload.
- Low-waste rationale: Bounded executor reuse reduces idle threads and CPU overhead without reducing useful throughput.
- Evidence: final ExecutorService executor = Executors.newSingleThreadExecutor();

### `src\test\java\org\apache\commons\io\FileCleaningTrackerTest.java`

- Pre-analysis: classes 1, methods 11, loops 5, streams 0, synchronized blocks 0
#### 1. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: line 367
- Pattern: allocation-pressure
- What was found: Loop at line 367 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: List<String> list = new ArrayList<>();
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: pauseForDeleteToComplete (line 76)
- Pattern: algorithmic-waste
- What was found: Loop at line 76 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 76
#### 3. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: pauseForDeleteToComplete (line 76)
- Pattern: data-movement-bloat
- What was found: Loop at line 76 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: file = Paths.get(file.toAbsolutePath().toString());
#### 4. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: line 367
- Pattern: repeated-work
- What was found: Loop at line 367 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: List<String> list = new ArrayList<>();

### `src\main\java\org\apache\commons\io\input\UnsynchronizedBufferedReader.java`

- Pre-analysis: classes 2, methods 3, loops 5, streams 0, synchronized blocks 4
#### 1. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: line 286
- Pattern: chatty-io
- What was found: Loop at line 286 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: * If we're unmarked and the requested size is greater than our buffer, read the bytes directly into the caller's buffer. We don't read into smaller
#### 2. Payload construction inside loop
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
#### 3. Payload construction inside loop
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

### `src\test\java\org\apache\commons\io\FileUtilsListFilesTest.java`

- Pre-analysis: classes 1, methods 6, loops 3, streams 1, synchronized blocks 0
#### 1. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: line 239
- Pattern: chatty-io
- What was found: Loop at line 239 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: final File file = new File(tempDir.getAbsolutePath(), UUID.randomUUID() + ".deletetester"); | file.deleteOnExit(); | if (!file.delete()) {
#### 2. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: line 258
- Pattern: chatty-io
- What was found: Loop at line 258 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: final Collection<File> files = FileUtils.listFiles(tempDir, new String[] { ".deletetester" }, false);
#### 3. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 239
- Pattern: allocation-pressure
- What was found: Loop at line 239 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: fail("Could not create test file: '" + file.getAbsolutePath() + "': " + e, e); | fail("Could not delete test file: '" + file.getAbsolutePath() + "'");

### `src\test\java\org\apache\commons\io\filefilter\AbstractConditionalFileFilterTest.java`

- Pre-analysis: classes 1, methods 6, loops 3, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testAdd (line 83)
- Pattern: algorithmic-waste
- What was found: Loop at line 83 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 83
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testFilterBuiltUsingAdd (line 100)
- Pattern: algorithmic-waste
- What was found: Loop at line 100 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 100
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testFilterBuiltUsingConstructor (line 134)
- Pattern: algorithmic-waste
- What was found: Loop at line 134 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 134

### `src\test\java\org\apache\commons\io\FilenameUtilsWildcardTest.java`

- Pre-analysis: classes 1, methods 8, loops 2, streams 0, synchronized blocks 0
#### 1. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: testLocaleIndependence (line 88)
- Pattern: data-movement-bloat
- What was found: Loop at line 88 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: assertTrue(match, Locale.getDefault().toString() + ": " + i);
#### 2. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: testLocaleIndependence (line 89)
- Pattern: data-movement-bloat
- What was found: Loop at line 89 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: assertTrue(match, Locale.getDefault().toString() + ": " + i);
#### 3. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: testLocaleIndependence (line 88)
- Pattern: allocation-pressure
- What was found: Loop at line 88 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertTrue(data[i][0].equalsIgnoreCase(data[i][1]), "Test data corrupt: " + i); | assertTrue(match, Locale.getDefault().toString() + ": " + i);
#### 4. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: testLocaleIndependence (line 89)
- Pattern: allocation-pressure
- What was found: Loop at line 89 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertTrue(data[i][0].equalsIgnoreCase(data[i][1]), "Test data corrupt: " + i); | assertTrue(match, Locale.getDefault().toString() + ": " + i);

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

### `src\test\java\org\apache\commons\io\input\NullInputStreamTest.java`

- Pre-analysis: classes 2, methods 4, loops 12, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 114
- Pattern: allocation-pressure
- What was found: Loop at line 114 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertEquals(position, input.read(), "Read Before Mark [" + position + "]");
#### 2. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 122
- Pattern: allocation-pressure
- What was found: Loop at line 122 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertEquals(position + i, input.read(), "Read After Mark [" + i + "]");
#### 3. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 130
- Pattern: allocation-pressure
- What was found: Loop at line 130 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertEquals(position + i, input.read(), "Read After Reset [" + i + "]");
#### 4. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 158
- Pattern: allocation-pressure
- What was found: Loop at line 158 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertEquals(size - i, input.available(), "Check Size [" + i + "]"); | assertEquals(i, input.read(), "Check Value [" + i + "]");
#### 5. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 303
- Pattern: allocation-pressure
- What was found: Loop at line 303 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertEquals(size - i, input.available(), "Check Size [" + i + "]"); | assertEquals(i, input.read(), "Check Value [" + i + "]");

### `src\test\java\org\apache\commons\io\monitor\FileAlterationMonitorTest.java`

- Pre-analysis: classes 1, methods 8, loops 1, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 179
- Pattern: concurrency-misuse
- What was found: Line 179 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: final ThreadFactory threadFactory = new ThreadFactory() {
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: checkFile (line 54)
- Pattern: algorithmic-waste
- What was found: Loop at line 54 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 54

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

### `src\test\java\org\apache\commons\io\DemuxInputStreamTest.java`

- Pre-analysis: classes 3, methods 10, loops 3, streams 0, synchronized blocks 0
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
#### 2. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: run (line 61)
- Pattern: allocation-pressure
- What was found: Loop at line 61 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: // System.out.println( "Reading: " + (char)ch );
#### 3. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: run (line 90)
- Pattern: allocation-pressure
- What was found: Loop at line 90 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: // System.out.println( "Writing: " + (char)byteArray[ i ] );

### `src\test\java\org\apache\commons\io\HexDumpTest.java`

- Pre-analysis: classes 1, methods 2, loops 18, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 134
- Pattern: allocation-pressure
- What was found: Loop at line 134 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertEquals(outputArray[j], actualOutput[j], "array[ " + j + "] mismatch");
#### 2. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 167
- Pattern: allocation-pressure
- What was found: Loop at line 167 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertEquals(outputArray[j], actualOutput[j], "array[ " + j + "] mismatch");
#### 3. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 200
- Pattern: allocation-pressure
- What was found: Loop at line 200 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertEquals(outputArray[j], actualOutput[j], "array[ " + j + "] mismatch");
#### 4. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 244
- Pattern: allocation-pressure
- What was found: Loop at line 244 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertEquals(outputArray[j], actualOutput[j], "array[ " + j + "] mismatch");

### `src\test\java\org\apache\commons\io\input\AbstractInputStreamTest.java`

- Pre-analysis: classes 2, methods 1, loops 24, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 190
- Pattern: algorithmic-waste
- What was found: Loop at line 190 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 190
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 195
- Pattern: algorithmic-waste
- What was found: Loop at line 195 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 195

### `src\test\java\org\apache\commons\io\input\NullReaderTest.java`

- Pre-analysis: classes 2, methods 4, loops 8, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 100
- Pattern: allocation-pressure
- What was found: Loop at line 100 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertEquals(position + i, reader.read(), "Read After Reset [" + i + "]");
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
- Evidence: assertEquals(i, reader.read(), "Check Value [" + i + "]");
#### 3. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 84
- Pattern: allocation-pressure
- What was found: Loop at line 84 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertEquals(position, reader.read(), "Read Before Mark [" + position + "]");
#### 4. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 92
- Pattern: allocation-pressure
- What was found: Loop at line 92 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertEquals(position + i, reader.read(), "Read After Mark [" + i + "]");

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
- Evidence: if (!tracker.delete()) { | deleteFailures.add(tracker.getPath());

### `src\main\java\org\apache\commons\io\input\ClassLoaderObjectInputStream.java`

- Pre-analysis: classes 7, methods 0, loops 1, streams 0, synchronized blocks 0
#### 1. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: line 90
- Pattern: chatty-io
- What was found: Loop at line 90 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: interfaceClasses[i] = Class.forName(interfaces[i], false, classLoader);

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

### `src\main\java\org\apache\commons\io\monitor\FileAlterationObserver.java`

- Pre-analysis: classes 2, methods 32, loops 3, streams 0, synchronized blocks 0
#### 1. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: checkAndFire (line 361)
- Pattern: chatty-io
- What was found: Loop at line 361 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: fireOnDelete(previousEntry);

### `src\main\java\org\apache\commons\io\output\WriterOutputStream.java`

- Pre-analysis: classes 4, methods 15, loops 3, streams 0, synchronized blocks 0
#### 1. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: checkIbmJdkWithBrokenUTF16 (line 214)
- Pattern: chatty-io
- What was found: Loop at line 214 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: throw new UnsupportedOperationException("UTF-16 requested when running on an IBM JDK with broken UTF-16 support. "

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

### `src\test\java\org\apache\commons\io\FileUtilsWaitForTest.java`

- Pre-analysis: classes 2, methods 7, loops 0, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 47
- Pattern: concurrency-misuse
- What was found: Line 47 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: final Thread thread1 = new Thread(() -> {

### `src\test\java\org\apache\commons\io\input\buffer\CircularBufferInputStreamTest.java`

- Pre-analysis: classes 1, methods 2, loops 3, streams 0, synchronized blocks 0
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
- Evidence: assertEquals(buffer[i] & 0xFF, b, "byte at index " + i + " should be equal");
#### 2. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 76
- Pattern: allocation-pressure
- What was found: Loop at line 76 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertEquals(inputBuffer[offset], (byte) res, "Expected " + inputBuffer[offset] + " at offset " + offset + ", got " + res); | assertNotEquals(0, res, "Unexpected zero-byte-result at offset " + offset); | assertEquals(inputBuffer[offset], readBuffer[i], "Expected " + inputBuffer[offset] + " at offset " + offset + ", got " + readBuffer[i]);
#### 3. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 90
- Pattern: allocation-pressure
- What was found: Loop at line 90 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertEquals(inputBuffer[offset], readBuffer[i], "Expected " + inputBuffer[offset] + " at offset " + offset + ", got " + readBuffer[i]);

### `src\test\java\org\apache\commons\io\input\buffer\PeekableInputStreamTest.java`

- Pre-analysis: classes 1, methods 2, loops 3, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 60
- Pattern: allocation-pressure
- What was found: Loop at line 60 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertEquals(buffer[i] & 0xFF, b, "byte at index " + i + " should be equal");
#### 2. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 77
- Pattern: allocation-pressure
- What was found: Loop at line 77 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertEquals(inputBuffer[offset], (byte) res, "Expected " + inputBuffer[offset] + " at offset " + offset + ", got " + res); | assertNotEquals(0, res, "Unexpected zero-byte-result at offset " + offset); | assertEquals(inputBuffer[offset], readBuffer[i], "Expected " + inputBuffer[offset] + " at offset " + offset + ", got " + readBuffer[i]);
#### 3. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 91
- Pattern: allocation-pressure
- What was found: Loop at line 91 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertEquals(inputBuffer[offset], readBuffer[i], "Expected " + inputBuffer[offset] + " at offset " + offset + ", got " + readBuffer[i]);

### `src\test\java\org\apache\commons\io\input\CharSequenceInputStreamTest.java`

- Pre-analysis: classes 1, methods 5, loops 7, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 150
- Pattern: allocation-pressure
- What was found: Loop at line 150 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertEquals(expected.length, offset, "EOF: offset should equal length for charset " + charsetName); | assertTrue(read <= bufferLength, "Read " + read + " <= " + bufferLength); | "offset for " + charsetName + " " + offset + " < " + expected.length);
#### 2. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 159
- Pattern: allocation-pressure
- What was found: Loop at line 159 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: "offset for " + charsetName + " " + offset + " < " + expected.length); | assertEquals(expected[offset], buffer[bufferOffset], "bytes should agree for " + charsetName);
#### 3. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 518
- Pattern: allocation-pressure
- What was found: Loop at line 518 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertTrue(read >= 0, "read " + read + " >=0 "); | assertTrue(read <= 255, "read " + read + " <= 255");

### `src\test\java\org\apache\commons\io\input\QueueInputStreamTest.java`

- Pre-analysis: classes 1, methods 5, loops 2, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 323
- Pattern: concurrency-misuse
- What was found: Line 323 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: final Thread thread = new Thread(() -> {

### `src\test\java\org\apache\commons\io\input\UnsynchronizedBufferedInputStreamTest.java`

- Pre-analysis: classes 1, methods 7, loops 3, streams 0, synchronized blocks 29
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 144
- Pattern: concurrency-misuse
- What was found: Line 144 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: final Thread thread = new Thread(() -> {

### `src\test\java\org\apache\commons\io\jmh\QueueStreamBenchmark.java`

- Pre-analysis: classes 1, methods 0, loops 2, streams 0, synchronized blocks 0
#### 1. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: line 59
- Pattern: chatty-io
- What was found: Loop at line 59 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: while (received < CAPACITY) { | received += len;

### `src\test\java\org\apache\commons\io\test\TestUtils.java`

- Pre-analysis: classes 2, methods 6, loops 7, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 111
- Pattern: allocation-pressure
- What was found: Loop at line 111 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertEquals(c0[i], c1[i], "char " + i + " differs");
#### 2. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 135
- Pattern: allocation-pressure
- What was found: Loop at line 135 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: "The files " + f0 + " and " + f1 + | " have differing number of bytes available (" + n0 + " vs " + n1 + ")"); | assertArrayEquals(buf0, buf1, "The files " + f0 + " and " + f1 + " have different content");
#### 3. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 77
- Pattern: allocation-pressure
- What was found: Loop at line 77 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertEquals(b0[i], b1[i], "byte " + i + " differs");

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

### `src\test\java\org\apache\commons\io\channels\AbstractSeekableByteChannelTest.java`

- Pre-analysis: classes 1, methods 5, loops 1, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 193
- Pattern: algorithmic-waste
- What was found: Loop at line 193 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 193

### `src\test\java\org\apache\commons\io\filefilter\AbstractIOFileFilterTest.java`

- Pre-analysis: classes 3, methods 18, loops 2, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: assertFalseFiltersInvoked (line 90)
- Pattern: allocation-pressure
- What was found: Loop at line 90 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertEquals(invoked[i - 1], filters[i].isInvoked(), "test " + testNumber + " filter " + i + " invoked");
#### 2. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: assertTrueFiltersInvoked (line 125)
- Pattern: allocation-pressure
- What was found: Loop at line 125 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertEquals(invoked[i - 1], filters[i].isInvoked(), "test " + testNumber + " filter " + i + " invoked");

### `src\test\java\org\apache\commons\io\input\CharSequenceReaderTest.java`

- Pre-analysis: classes 1, methods 3, loops 2, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: checkArray (line 43)
- Pattern: allocation-pressure
- What was found: Loop at line 43 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertEquals(expected[i], actual[i], "Compare[" + i + "]");
#### 2. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 49
- Pattern: allocation-pressure
- What was found: Loop at line 49 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertEquals(expected.charAt(i), (char) reader.read(), "Read[" + i + "] of '" + expected + "'");

### `src\test\java\org\apache\commons\io\input\compatibility\XmlStreamReader.java`

- Pre-analysis: classes 3, methods 7, loops 2, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 224
- Pattern: algorithmic-waste
- What was found: Loop at line 224 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 224

### `src\test\java\org\apache\commons\io\input\MessageDigestCalculatingInputStreamTest.java`

- Pre-analysis: classes 1, methods 0, loops 1, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 110
- Pattern: algorithmic-waste
- What was found: Loop at line 110 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 110

### `src\test\java\org\apache\commons\io\input\MessageDigestInputStreamTest.java`

- Pre-analysis: classes 1, methods 1, loops 1, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 126
- Pattern: algorithmic-waste
- What was found: Loop at line 126 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 126

### `src\test\java\org\apache\commons\io\input\ReadAheadInputStreamTest.java`

- Pre-analysis: classes 2, methods 0, loops 0, streams 0, synchronized blocks 1
#### 1. Executor created in application code path
- Severity: Medium
- Confidence: High
- Location: line 92
- Pattern: concurrency-misuse
- What was found: Line 92 creates a new executor instance.
- Why it is wasteful: Creating executors per call can fragment thread pools and increase context switching and idle threads.
- Likely impact: Higher memory use, poorer scheduling efficiency, and harder concurrency control.
- Recommended remediation: Reuse a bounded shared executor sized to the workload.
- Low-waste rationale: Bounded executor reuse reduces idle threads and CPU overhead without reducing useful throughput.
- Evidence: final ExecutorService externalExecutor = Executors.newSingleThreadExecutor();

### `src\test\java\org\apache\commons\io\input\SequenceReaderTest.java`

- Pre-analysis: classes 2, methods 4, loops 3, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: checkArray (line 70)
- Pattern: allocation-pressure
- What was found: Loop at line 70 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertEquals(expected[i], actual[i], "Compare[" + i + "]");
#### 2. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 76
- Pattern: allocation-pressure
- What was found: Loop at line 76 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertEquals(expected.charAt(i), (char) reader.read(), "Read[" + i + "] of '" + expected + "'");

### `src\test\java\org\apache\commons\io\output\QueueOutputStreamTest.java`

- Pre-analysis: classes 1, methods 2, loops 0, streams 0, synchronized blocks 0
#### 1. Executor created in application code path
- Severity: Medium
- Confidence: High
- Location: line 46
- Pattern: concurrency-misuse
- What was found: Line 46 creates a new executor instance.
- Why it is wasteful: Creating executors per call can fragment thread pools and increase context switching and idle threads.
- Likely impact: Higher memory use, poorer scheduling efficiency, and harder concurrency control.
- Recommended remediation: Reuse a bounded shared executor sized to the workload.
- Low-waste rationale: Bounded executor reuse reduces idle threads and CPU overhead without reducing useful throughput.
- Evidence: private static final ExecutorService executorService = Executors.newFixedThreadPool(5);

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

### `src\test\java\org\apache\commons\io\input\BOMInputStreamTest.java`

- Pre-analysis: classes 2, methods 8, loops 2, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: assertData (line 80)
- Pattern: allocation-pressure
- What was found: Loop at line 80 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertEquals(expected[ii], actual[ii], "byte " + ii);

### `src\test\java\org\apache\commons\io\input\ReversedLinesFileReaderParamBlockSizeTest.java`

- Pre-analysis: classes 1, methods 4, loops 2, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 155
- Pattern: allocation-pressure
- What was found: Loop at line 155 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertEqualsAndNoLineBreaks("" + i, reversedLinesFileReader.readLine());

### `src\test\java\org\apache\commons\io\input\XmlStreamReaderTest.java`

- Pre-analysis: classes 1, methods 6, loops 4, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 481
- Pattern: allocation-pressure
- What was found: Loop at line 481 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertTrue(encoding.equalsIgnoreCase(xmlReader.getEncoding()), "Check encoding : " + encoding);

### `src\test\java\org\apache\commons\io\output\CountingOutputStreamTest.java`

- Pre-analysis: classes 1, methods 1, loops 5, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: assertByteArrayEquals (line 35)
- Pattern: allocation-pressure
- What was found: Loop at line 35 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertEquals(array[i], i - start, msg + ": array[" + i + "] mismatch");

### `src\test\java\org\apache\commons\io\output\TeeOutputStreamTest.java`

- Pre-analysis: classes 1, methods 1, loops 4, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: assertByteArrayEquals (line 38)
- Pattern: allocation-pressure
- What was found: Loop at line 38 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertEquals(array1[i], array2[i], msg + ": array[ " + i + "] mismatch");

## Cautions
- This is static analysis only; findings indicate likely waste patterns, not measured bottlenecks.
- Method extraction and loop classification are heuristic and may miss unconventional Java syntax.