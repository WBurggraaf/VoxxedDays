# guava-master Green Code Report

## Summary
- Project root: `C:\VoxxedDays\GitRepos\guava-master`
- Java files reviewed: 1989
- Source files: 1989
- Test files: 0
- Overall risk level: High
- Findings by severity: High 116, Medium 734, Low 104
- Top efficiency themes: Algorithmic waste, Allocation pressure, Concurrency misuse, Chatty I/O, Repeated work

## Hotspots
- `guava\src\com\google\common\cache\LocalCache.java`: score 53, findings 27
- `android\guava\src\com\google\common\cache\LocalCache.java`: score 51, findings 26
- `guava\src\com\google\common\collect\Sets.java`: score 37, findings 20
- `guava\src\com\google\common\util\concurrent\ServiceManager.java`: score 35, findings 13
- `android\guava\src\com\google\common\util\concurrent\ServiceManager.java`: score 35, findings 13
- `android\guava\src\com\google\common\collect\Sets.java`: score 34, findings 17
- `guava-tests\benchmark\com\google\common\util\concurrent\ExecutionListBenchmark.java`: score 33, findings 11
- `android\guava-tests\benchmark\com\google\common\util\concurrent\ExecutionListBenchmark.java`: score 33, findings 11
- `guava-tests\benchmark\com\google\common\base\JoinerBenchmark.java`: score 30, findings 15
- `android\guava-tests\benchmark\com\google\common\base\JoinerBenchmark.java`: score 30, findings 15

## File Findings
### `guava\src\com\google\common\cache\LocalCache.java`

- Pre-analysis: classes 46, methods 312, loops 63, streams 0, synchronized blocks 4
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: clear (line 3214)
- Pattern: algorithmic-waste
- What was found: Loop at line 3214 is nested at depth 5 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 3214
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: clear (line 3215)
- Pattern: algorithmic-waste
- What was found: Loop at line 3215 is nested at depth 6 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 3215
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: containsValue (line 2774)
- Pattern: algorithmic-waste
- What was found: Loop at line 2774 is nested at depth 5 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 2774
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: containsValue (line 2775)
- Pattern: algorithmic-waste
- What was found: Loop at line 2775 is nested at depth 6 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 2775
#### 5. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: containsValue (line 4182)
- Pattern: algorithmic-waste
- What was found: Loop at line 4182 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 4182
#### 6. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: containsValue (line 4184)
- Pattern: algorithmic-waste
- What was found: Loop at line 4184 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 4184
#### 7. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: containsValue (line 4189)
- Pattern: algorithmic-waste
- What was found: Loop at line 4189 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 4189
#### 8. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: containsValue (line 4190)
- Pattern: algorithmic-waste
- What was found: Loop at line 4190 is nested at depth 5 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 4190
#### 9. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: drainRecencyQueue (line 2585)
- Pattern: algorithmic-waste
- What was found: Loop at line 2585 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 2585
#### 10. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: expand (line 2891)
- Pattern: algorithmic-waste
- What was found: Loop at line 2891 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 2891
#### 11. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: expand (line 2920)
- Pattern: algorithmic-waste
- What was found: Loop at line 2920 is nested at depth 6 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 2920
#### 12. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 2124
- Pattern: algorithmic-waste
- What was found: Loop at line 2124 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 2124
#### 13. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 2233
- Pattern: algorithmic-waste
- What was found: Loop at line 2233 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 2233
#### 14. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 2811
- Pattern: algorithmic-waste
- What was found: Loop at line 2811 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 2811
#### 15. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 3009
- Pattern: algorithmic-waste
- What was found: Loop at line 3009 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 3009
#### 16. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 3064
- Pattern: algorithmic-waste
- What was found: Loop at line 3064 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 3064
#### 17. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 309
- Pattern: algorithmic-waste
- What was found: Loop at line 309 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 309
#### 18. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 3163
- Pattern: algorithmic-waste
- What was found: Loop at line 3163 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 3163
#### 19. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 317
- Pattern: algorithmic-waste
- What was found: Loop at line 317 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 317
#### 20. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 4054
- Pattern: algorithmic-waste
- What was found: Loop at line 4054 is nested at depth 5 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 4054
#### 21. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: nextInTable (line 4406)
- Pattern: algorithmic-waste
- What was found: Loop at line 4406 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 4406
#### 22. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: reclaimKey (line 3305)
- Pattern: algorithmic-waste
- What was found: Loop at line 3305 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 3305
#### 23. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: reclaimValue (line 3341)
- Pattern: algorithmic-waste
- What was found: Loop at line 3341 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 3341
#### 24. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: remove (line 3110)
- Pattern: algorithmic-waste
- What was found: Loop at line 3110 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 3110
#### 25. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: removeEntry (line 3419)
- Pattern: algorithmic-waste
- What was found: Loop at line 3419 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 3419
#### 26. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: replace (line 2948)
- Pattern: algorithmic-waste
- What was found: Loop at line 2948 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 2948
#### 27. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 4054
- Pattern: allocation-pressure
- What was found: Loop at line 4054 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw new InvalidCacheLoadException("loadAll failed to return a value for " + key);

### `android\guava\src\com\google\common\cache\LocalCache.java`

- Pre-analysis: classes 45, methods 306, loops 60, streams 0, synchronized blocks 4
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: clear (line 3124)
- Pattern: algorithmic-waste
- What was found: Loop at line 3124 is nested at depth 5 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 3124
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: clear (line 3125)
- Pattern: algorithmic-waste
- What was found: Loop at line 3125 is nested at depth 6 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 3125
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: containsValue (line 2684)
- Pattern: algorithmic-waste
- What was found: Loop at line 2684 is nested at depth 5 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 2684
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: containsValue (line 2685)
- Pattern: algorithmic-waste
- What was found: Loop at line 2685 is nested at depth 6 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 2685
#### 5. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: containsValue (line 4072)
- Pattern: algorithmic-waste
- What was found: Loop at line 4072 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 4072
#### 6. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: containsValue (line 4074)
- Pattern: algorithmic-waste
- What was found: Loop at line 4074 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 4074
#### 7. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: containsValue (line 4079)
- Pattern: algorithmic-waste
- What was found: Loop at line 4079 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 4079
#### 8. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: containsValue (line 4080)
- Pattern: algorithmic-waste
- What was found: Loop at line 4080 is nested at depth 5 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 4080
#### 9. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: drainRecencyQueue (line 2495)
- Pattern: algorithmic-waste
- What was found: Loop at line 2495 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 2495
#### 10. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: expand (line 2801)
- Pattern: algorithmic-waste
- What was found: Loop at line 2801 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 2801
#### 11. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: expand (line 2830)
- Pattern: algorithmic-waste
- What was found: Loop at line 2830 is nested at depth 6 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 2830
#### 12. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 2120
- Pattern: algorithmic-waste
- What was found: Loop at line 2120 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 2120
#### 13. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 2721
- Pattern: algorithmic-waste
- What was found: Loop at line 2721 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 2721
#### 14. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 2919
- Pattern: algorithmic-waste
- What was found: Loop at line 2919 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 2919
#### 15. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 2974
- Pattern: algorithmic-waste
- What was found: Loop at line 2974 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 2974
#### 16. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 305
- Pattern: algorithmic-waste
- What was found: Loop at line 305 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 305
#### 17. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 3073
- Pattern: algorithmic-waste
- What was found: Loop at line 3073 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 3073
#### 18. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 313
- Pattern: algorithmic-waste
- What was found: Loop at line 313 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 313
#### 19. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 3944
- Pattern: algorithmic-waste
- What was found: Loop at line 3944 is nested at depth 5 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 3944
#### 20. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: nextInTable (line 4262)
- Pattern: algorithmic-waste
- What was found: Loop at line 4262 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 4262
#### 21. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: reclaimKey (line 3215)
- Pattern: algorithmic-waste
- What was found: Loop at line 3215 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 3215
#### 22. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: reclaimValue (line 3251)
- Pattern: algorithmic-waste
- What was found: Loop at line 3251 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 3251
#### 23. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: remove (line 3020)
- Pattern: algorithmic-waste
- What was found: Loop at line 3020 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 3020
#### 24. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: removeEntry (line 3329)
- Pattern: algorithmic-waste
- What was found: Loop at line 3329 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 3329
#### 25. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: replace (line 2858)
- Pattern: algorithmic-waste
- What was found: Loop at line 2858 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 2858
#### 26. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 3944
- Pattern: allocation-pressure
- What was found: Loop at line 3944 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw new InvalidCacheLoadException("loadAll failed to return a value for " + key);

### `guava\src\com\google\common\collect\Sets.java`

- Pre-analysis: classes 24, methods 1, loops 26, streams 7, synchronized blocks 11
#### 1. List membership checks inside loop
- Severity: Medium
- Confidence: Medium
- Location: Sets (line 1596)
- Pattern: algorithmic-waste
- What was found: Loop at line 1596 performs `.contains(...)` checks that may scan collections repeatedly.
- Why it is wasteful: Repeated linear scans inside iteration can push runtime toward O(n^2) as data sets grow.
- Likely impact: Throughput degradation and elevated CPU time for larger inputs.
- Recommended remediation: Use a `Set` for membership lookups or pre-index data before the loop.
- Low-waste rationale: Indexing once avoids repeated scans and reduces wasted CPU work.
- Evidence: line 1596
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Sets (line 1026)
- Pattern: algorithmic-waste
- What was found: Loop at line 1026 is nested at depth 6 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1026
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Sets (line 1050)
- Pattern: algorithmic-waste
- What was found: Loop at line 1050 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1050
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Sets (line 1104)
- Pattern: algorithmic-waste
- What was found: Loop at line 1104 is nested at depth 6 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1104
#### 5. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Sets (line 1110)
- Pattern: algorithmic-waste
- What was found: Loop at line 1110 is nested at depth 6 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1110
#### 6. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Sets (line 1124)
- Pattern: algorithmic-waste
- What was found: Loop at line 1124 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1124
#### 7. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Sets (line 1129)
- Pattern: algorithmic-waste
- What was found: Loop at line 1129 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1129
#### 8. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Sets (line 1445)
- Pattern: algorithmic-waste
- What was found: Loop at line 1445 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1445
#### 9. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Sets (line 1446)
- Pattern: algorithmic-waste
- What was found: Loop at line 1446 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1446
#### 10. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Sets (line 1500)
- Pattern: algorithmic-waste
- What was found: Loop at line 1500 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1500
#### 11. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Sets (line 1501)
- Pattern: algorithmic-waste
- What was found: Loop at line 1501 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1501
#### 12. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Sets (line 1596)
- Pattern: algorithmic-waste
- What was found: Loop at line 1596 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1596
#### 13. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Sets (line 758)
- Pattern: algorithmic-waste
- What was found: Loop at line 758 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 758
#### 14. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Sets (line 838)
- Pattern: algorithmic-waste
- What was found: Loop at line 838 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 838
#### 15. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Sets (line 862)
- Pattern: algorithmic-waste
- What was found: Loop at line 862 is nested at depth 6 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 862
#### 16. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Sets (line 945)
- Pattern: algorithmic-waste
- What was found: Loop at line 945 is nested at depth 6 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 945
#### 17. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Sets (line 969)
- Pattern: algorithmic-waste
- What was found: Loop at line 969 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 969
#### 18. Parallel stream usage requires workload validation
- Severity: Low
- Confidence: Medium
- Location: Sets (line 1044)
- Pattern: concurrency-misuse
- What was found: Line 1044 uses `parallelStream()`.
- Why it is wasteful: Parallel streams can add splitting, synchronization, and scheduling overhead when workloads are small or blocking.
- Likely impact: Higher CPU use and worse latency instead of better throughput.
- Recommended remediation: Validate collection size and workload type, or prefer explicit bounded executors for heavy tasks.
- Low-waste rationale: Concurrency should only add parallel work when it reduces total operations per useful result.
- Evidence: return set1.parallelStream().filter(e -> !set2.contains(e));
#### 19. Parallel stream usage requires workload validation
- Severity: Low
- Confidence: Medium
- Location: Sets (line 1981)
- Pattern: concurrency-misuse
- What was found: Line 1981 uses `parallelStream()`.
- Why it is wasteful: Parallel streams can add splitting, synchronization, and scheduling overhead when workloads are small or blocking.
- Likely impact: Higher CPU use and worse latency instead of better throughput.
- Recommended remediation: Validate collection size and workload type, or prefer explicit bounded executors for heavy tasks.
- Low-waste rationale: Concurrency should only add parallel work when it reduces total operations per useful result.
- Evidence: return delegate.parallelStream();
#### 20. Parallel stream usage requires workload validation
- Severity: Low
- Confidence: Medium
- Location: Sets (line 963)
- Pattern: concurrency-misuse
- What was found: Line 963 uses `parallelStream()`.
- Why it is wasteful: Parallel streams can add splitting, synchronization, and scheduling overhead when workloads are small or blocking.
- Likely impact: Higher CPU use and worse latency instead of better throughput.
- Recommended remediation: Validate collection size and workload type, or prefer explicit bounded executors for heavy tasks.
- Low-waste rationale: Concurrency should only add parallel work when it reduces total operations per useful result.
- Evidence: return set1.parallelStream().filter(set2::contains);

### `android\guava\src\com\google\common\util\concurrent\ServiceManager.java`

- Pre-analysis: classes 14, methods 43, loops 9, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 102
- Pattern: concurrency-misuse
- What was found: Line 102 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: *     Runtime.getRuntime().addShutdownHook(new Thread() {
#### 2. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: ServiceManager (line 225)
- Pattern: chatty-io
- What was found: Loop at line 225 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: for (Service service : copy) { | service.addListener(new ServiceListener(service, stateReference), directExecutor()); | // to a NEW service.
#### 3. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: checkHealthy (line 771)
- Pattern: chatty-io
- What was found: Loop at line 771 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: for (Service service : servicesByState.get(State.FAILED)) { | exception.addSuppressed(new FailedService(service));
#### 4. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: isHealthy (line 394)
- Pattern: chatty-io
- What was found: Loop at line 394 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: for (Service service : services) { | if (!service.isRunning()) {
#### 5. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: markReady (line 569)
- Pattern: chatty-io
- What was found: Loop at line 569 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: for (Service service : servicesByState().values()) { | if (service.state() != NEW) { | servicesInBadStates.add(service);
#### 6. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: servicesByState (line 635)
- Pattern: chatty-io
- What was found: Loop at line 635 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: for (Entry<State, Service> entry : servicesByState.entries()) { | if (!(entry.getValue() instanceof NoOpService)) {
#### 7. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: startAsync (line 274)
- Pattern: chatty-io
- What was found: Loop at line 274 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: for (Service service : services) { | checkState(service.state() == NEW, "Not all services are NEW, cannot start %s", this);
#### 8. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: startAsync (line 277)
- Pattern: chatty-io
- What was found: Loop at line 277 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: for (Service service : services) { | state.tryStartTiming(service); | service.startAsync();
#### 9. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: startupTimes (line 652)
- Pattern: chatty-io
- What was found: Loop at line 652 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: for (Entry<Service, Stopwatch> entry : startupTimers.entrySet()) { | Service service = entry.getKey(); | if (!stopwatch.isRunning() && !(service instanceof NoOpService)) {
#### 10. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: stopAsync (line 344)
- Pattern: chatty-io
- What was found: Loop at line 344 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: for (Service service : services) { | service.stopAsync();
#### 11. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: checkHealthy (line 771)
- Pattern: algorithmic-waste
- What was found: Loop at line 771 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 771
#### 12. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: startAsync (line 277)
- Pattern: algorithmic-waste
- What was found: Loop at line 277 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 277
#### 13. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: startAsync (line 277)
- Pattern: allocation-pressure
- What was found: Loop at line 277 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: logger.get().log(Level.WARNING, "Unable to start Service " + service, e);

### `guava\src\com\google\common\util\concurrent\ServiceManager.java`

- Pre-analysis: classes 14, methods 43, loops 9, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 102
- Pattern: concurrency-misuse
- What was found: Line 102 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: *     Runtime.getRuntime().addShutdownHook(new Thread() {
#### 2. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: ServiceManager (line 225)
- Pattern: chatty-io
- What was found: Loop at line 225 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: for (Service service : copy) { | service.addListener(new ServiceListener(service, stateReference), directExecutor()); | // to a NEW service.
#### 3. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: checkHealthy (line 767)
- Pattern: chatty-io
- What was found: Loop at line 767 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: for (Service service : servicesByState.get(State.FAILED)) { | exception.addSuppressed(new FailedService(service));
#### 4. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: isHealthy (line 392)
- Pattern: chatty-io
- What was found: Loop at line 392 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: for (Service service : services) { | if (!service.isRunning()) {
#### 5. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: markReady (line 565)
- Pattern: chatty-io
- What was found: Loop at line 565 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: for (Service service : servicesByState().values()) { | if (service.state() != NEW) { | servicesInBadStates.add(service);
#### 6. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: servicesByState (line 631)
- Pattern: chatty-io
- What was found: Loop at line 631 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: for (Entry<State, Service> entry : servicesByState.entries()) { | if (!(entry.getValue() instanceof NoOpService)) {
#### 7. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: startAsync (line 274)
- Pattern: chatty-io
- What was found: Loop at line 274 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: for (Service service : services) { | checkState(service.state() == NEW, "Not all services are NEW, cannot start %s", this);
#### 8. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: startAsync (line 277)
- Pattern: chatty-io
- What was found: Loop at line 277 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: for (Service service : services) { | state.tryStartTiming(service); | service.startAsync();
#### 9. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: startupTimes (line 648)
- Pattern: chatty-io
- What was found: Loop at line 648 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: for (Entry<Service, Stopwatch> entry : startupTimers.entrySet()) { | Service service = entry.getKey(); | if (!stopwatch.isRunning() && !(service instanceof NoOpService)) {
#### 10. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: stopAsync (line 343)
- Pattern: chatty-io
- What was found: Loop at line 343 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: for (Service service : services) { | service.stopAsync();
#### 11. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: checkHealthy (line 767)
- Pattern: algorithmic-waste
- What was found: Loop at line 767 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 767
#### 12. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: startAsync (line 277)
- Pattern: algorithmic-waste
- What was found: Loop at line 277 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 277
#### 13. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: startAsync (line 277)
- Pattern: allocation-pressure
- What was found: Loop at line 277 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: logger.get().log(Level.WARNING, "Unable to start Service " + service, e);

### `android\guava\src\com\google\common\collect\Sets.java`

- Pre-analysis: classes 24, methods 1, loops 26, streams 0, synchronized blocks 11
#### 1. List membership checks inside loop
- Severity: Medium
- Confidence: Medium
- Location: Sets (line 1551)
- Pattern: algorithmic-waste
- What was found: Loop at line 1551 performs `.contains(...)` checks that may scan collections repeatedly.
- Why it is wasteful: Repeated linear scans inside iteration can push runtime toward O(n^2) as data sets grow.
- Likely impact: Throughput degradation and elevated CPU time for larger inputs.
- Recommended remediation: Use a `Set` for membership lookups or pre-index data before the loop.
- Low-waste rationale: Indexing once avoids repeated scans and reduces wasted CPU work.
- Evidence: line 1551
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Sets (line 1005)
- Pattern: algorithmic-waste
- What was found: Loop at line 1005 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1005
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Sets (line 1059)
- Pattern: algorithmic-waste
- What was found: Loop at line 1059 is nested at depth 6 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1059
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Sets (line 1065)
- Pattern: algorithmic-waste
- What was found: Loop at line 1065 is nested at depth 6 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1065
#### 5. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Sets (line 1079)
- Pattern: algorithmic-waste
- What was found: Loop at line 1079 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1079
#### 6. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Sets (line 1084)
- Pattern: algorithmic-waste
- What was found: Loop at line 1084 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1084
#### 7. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Sets (line 1400)
- Pattern: algorithmic-waste
- What was found: Loop at line 1400 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1400
#### 8. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Sets (line 1401)
- Pattern: algorithmic-waste
- What was found: Loop at line 1401 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1401
#### 9. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Sets (line 1455)
- Pattern: algorithmic-waste
- What was found: Loop at line 1455 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1455
#### 10. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Sets (line 1456)
- Pattern: algorithmic-waste
- What was found: Loop at line 1456 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1456
#### 11. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Sets (line 1551)
- Pattern: algorithmic-waste
- What was found: Loop at line 1551 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1551
#### 12. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Sets (line 743)
- Pattern: algorithmic-waste
- What was found: Loop at line 743 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 743
#### 13. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Sets (line 823)
- Pattern: algorithmic-waste
- What was found: Loop at line 823 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 823
#### 14. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Sets (line 847)
- Pattern: algorithmic-waste
- What was found: Loop at line 847 is nested at depth 6 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 847
#### 15. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Sets (line 920)
- Pattern: algorithmic-waste
- What was found: Loop at line 920 is nested at depth 6 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 920
#### 16. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Sets (line 934)
- Pattern: algorithmic-waste
- What was found: Loop at line 934 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 934
#### 17. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Sets (line 991)
- Pattern: algorithmic-waste
- What was found: Loop at line 991 is nested at depth 6 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 991

### `android\guava-tests\benchmark\com\google\common\util\concurrent\ExecutionListBenchmark.java`

- Pre-analysis: classes 10, methods 26, loops 15, streams 0, synchronized blocks 6
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 225
- Pattern: concurrency-misuse
- What was found: Line 225 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: new ThreadPoolExecutor(
#### 2. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: addThenExecute_singleThreaded (line 264)
- Pattern: chatty-io
- What was found: Loop at line 264 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: list.execute();
#### 3. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: execute (line 388)
- Pattern: chatty-io
- What was found: Loop at line 388 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: runnables.poll().execute();
#### 4. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: execute (line 451)
- Pattern: chatty-io
- What was found: Loop at line 451 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: executeListener(list.runnable, list.executor);
#### 5. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: execute (line 526)
- Pattern: chatty-io
- What was found: Loop at line 526 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: executeListener(list.runnable, list.executor);
#### 6. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: executeThenAdd_singleThreaded (line 280)
- Pattern: chatty-io
- What was found: Loop at line 280 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: list.execute();
#### 7. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: line 234
- Pattern: chatty-io
- What was found: Loop at line 234 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: executorService.submit(
#### 8. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: line 313
- Pattern: chatty-io
- What was found: Loop at line 313 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: Future<?> possiblyIgnoredError = executorService.submit(addTask); | Future<?> possiblyIgnoredError = executorService.submit(executeTask);
#### 9. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: line 316
- Pattern: chatty-io
- What was found: Loop at line 316 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: Future<?> possiblyIgnoredError = executorService.submit(addTask);
#### 10. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: line 340
- Pattern: chatty-io
- What was found: Loop at line 340 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: Future<?> possiblyIgnoredError = executorService.submit(executeTask); | Future<?> possiblyIgnoredError1 = executorService.submit(addTask);
#### 11. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: line 345
- Pattern: chatty-io
- What was found: Loop at line 345 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: Future<?> possiblyIgnoredError1 = executorService.submit(addTask);

### `guava-tests\benchmark\com\google\common\util\concurrent\ExecutionListBenchmark.java`

- Pre-analysis: classes 10, methods 26, loops 15, streams 0, synchronized blocks 6
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 225
- Pattern: concurrency-misuse
- What was found: Line 225 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: new ThreadPoolExecutor(
#### 2. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: addThenExecute_singleThreaded (line 264)
- Pattern: chatty-io
- What was found: Loop at line 264 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: list.execute();
#### 3. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: execute (line 388)
- Pattern: chatty-io
- What was found: Loop at line 388 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: runnables.poll().execute();
#### 4. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: execute (line 451)
- Pattern: chatty-io
- What was found: Loop at line 451 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: executeListener(list.runnable, list.executor);
#### 5. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: execute (line 526)
- Pattern: chatty-io
- What was found: Loop at line 526 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: executeListener(list.runnable, list.executor);
#### 6. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: executeThenAdd_singleThreaded (line 280)
- Pattern: chatty-io
- What was found: Loop at line 280 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: list.execute();
#### 7. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: line 234
- Pattern: chatty-io
- What was found: Loop at line 234 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: executorService.submit(
#### 8. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: line 313
- Pattern: chatty-io
- What was found: Loop at line 313 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: Future<?> possiblyIgnoredError = executorService.submit(addTask); | Future<?> possiblyIgnoredError = executorService.submit(executeTask);
#### 9. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: line 316
- Pattern: chatty-io
- What was found: Loop at line 316 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: Future<?> possiblyIgnoredError = executorService.submit(addTask);
#### 10. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: line 340
- Pattern: chatty-io
- What was found: Loop at line 340 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: Future<?> possiblyIgnoredError = executorService.submit(executeTask); | Future<?> possiblyIgnoredError1 = executorService.submit(addTask);
#### 11. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: line 345
- Pattern: chatty-io
- What was found: Loop at line 345 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: Future<?> possiblyIgnoredError1 = executorService.submit(addTask);

### `android\guava-tests\benchmark\com\google\common\base\JoinerBenchmark.java`

- Pre-analysis: classes 2, methods 8, loops 12, streams 0, synchronized blocks 0
#### 1. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: alwaysAppendThenBackUp (line 167)
- Pattern: allocation-pressure
- What was found: Loop at line 167 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: StringBuilder sb = new StringBuilder();
#### 2. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: assignDelimiter (line 147)
- Pattern: allocation-pressure
- What was found: Loop at line 147 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: StringBuilder sb = new StringBuilder();
#### 3. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: booleanIfFirst (line 126)
- Pattern: allocation-pressure
- What was found: Loop at line 126 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: StringBuilder sb = new StringBuilder();
#### 4. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: joinerInlined (line 84)
- Pattern: allocation-pressure
- What was found: Loop at line 84 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: StringBuilder sb = new StringBuilder();
#### 5. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: stringBuilderIsEmpty (line 106)
- Pattern: allocation-pressure
- What was found: Loop at line 106 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: StringBuilder sb = new StringBuilder();
#### 6. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: alwaysAppendThenBackUp (line 167)
- Pattern: data-movement-bloat
- What was found: Loop at line 167 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: dummy ^= sb.toString().length();
#### 7. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: assignDelimiter (line 147)
- Pattern: data-movement-bloat
- What was found: Loop at line 147 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: dummy ^= sb.toString().length();
#### 8. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: booleanIfFirst (line 126)
- Pattern: data-movement-bloat
- What was found: Loop at line 126 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: dummy ^= sb.toString().length();
#### 9. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: joinerInlined (line 84)
- Pattern: data-movement-bloat
- What was found: Loop at line 84 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: sb.append(iterator.next().toString()); | dummy ^= sb.toString().length();
#### 10. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: stringBuilderIsEmpty (line 106)
- Pattern: data-movement-bloat
- What was found: Loop at line 106 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: dummy ^= sb.toString().length();
#### 11. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: alwaysAppendThenBackUp (line 167)
- Pattern: repeated-work
- What was found: Loop at line 167 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: StringBuilder sb = new StringBuilder();
#### 12. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: assignDelimiter (line 147)
- Pattern: repeated-work
- What was found: Loop at line 147 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: StringBuilder sb = new StringBuilder();
#### 13. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: booleanIfFirst (line 126)
- Pattern: repeated-work
- What was found: Loop at line 126 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: StringBuilder sb = new StringBuilder();
#### 14. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: joinerInlined (line 84)
- Pattern: repeated-work
- What was found: Loop at line 84 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: StringBuilder sb = new StringBuilder();
#### 15. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: stringBuilderIsEmpty (line 106)
- Pattern: repeated-work
- What was found: Loop at line 106 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: StringBuilder sb = new StringBuilder();

### `guava-tests\benchmark\com\google\common\base\JoinerBenchmark.java`

- Pre-analysis: classes 2, methods 8, loops 12, streams 0, synchronized blocks 0
#### 1. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: alwaysAppendThenBackUp (line 167)
- Pattern: allocation-pressure
- What was found: Loop at line 167 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: StringBuilder sb = new StringBuilder();
#### 2. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: assignDelimiter (line 147)
- Pattern: allocation-pressure
- What was found: Loop at line 147 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: StringBuilder sb = new StringBuilder();
#### 3. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: booleanIfFirst (line 126)
- Pattern: allocation-pressure
- What was found: Loop at line 126 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: StringBuilder sb = new StringBuilder();
#### 4. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: joinerInlined (line 84)
- Pattern: allocation-pressure
- What was found: Loop at line 84 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: StringBuilder sb = new StringBuilder();
#### 5. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: stringBuilderIsEmpty (line 106)
- Pattern: allocation-pressure
- What was found: Loop at line 106 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: StringBuilder sb = new StringBuilder();
#### 6. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: alwaysAppendThenBackUp (line 167)
- Pattern: data-movement-bloat
- What was found: Loop at line 167 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: dummy ^= sb.toString().length();
#### 7. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: assignDelimiter (line 147)
- Pattern: data-movement-bloat
- What was found: Loop at line 147 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: dummy ^= sb.toString().length();
#### 8. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: booleanIfFirst (line 126)
- Pattern: data-movement-bloat
- What was found: Loop at line 126 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: dummy ^= sb.toString().length();
#### 9. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: joinerInlined (line 84)
- Pattern: data-movement-bloat
- What was found: Loop at line 84 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: sb.append(iterator.next().toString()); | dummy ^= sb.toString().length();
#### 10. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: stringBuilderIsEmpty (line 106)
- Pattern: data-movement-bloat
- What was found: Loop at line 106 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: dummy ^= sb.toString().length();
#### 11. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: alwaysAppendThenBackUp (line 167)
- Pattern: repeated-work
- What was found: Loop at line 167 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: StringBuilder sb = new StringBuilder();
#### 12. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: assignDelimiter (line 147)
- Pattern: repeated-work
- What was found: Loop at line 147 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: StringBuilder sb = new StringBuilder();
#### 13. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: booleanIfFirst (line 126)
- Pattern: repeated-work
- What was found: Loop at line 126 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: StringBuilder sb = new StringBuilder();
#### 14. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: joinerInlined (line 84)
- Pattern: repeated-work
- What was found: Loop at line 84 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: StringBuilder sb = new StringBuilder();
#### 15. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: stringBuilderIsEmpty (line 106)
- Pattern: repeated-work
- What was found: Loop at line 106 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: StringBuilder sb = new StringBuilder();

### `android\guava\src\com\google\common\collect\MapMakerInternalMap.java`

- Pre-analysis: classes 54, methods 139, loops 38, streams 0, synchronized blocks 3
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: containsValue (line 2398)
- Pattern: algorithmic-waste
- What was found: Loop at line 2398 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 2398
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: containsValue (line 2400)
- Pattern: algorithmic-waste
- What was found: Loop at line 2400 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 2400
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: containsValue (line 2405)
- Pattern: algorithmic-waste
- What was found: Loop at line 2405 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 2405
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: containsValue (line 2406)
- Pattern: algorithmic-waste
- What was found: Loop at line 2406 is nested at depth 5 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 2406
#### 5. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: maybeDrainReferenceQueues (line 1479)
- Pattern: algorithmic-waste
- What was found: Loop at line 1479 is nested at depth 5 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1479
#### 6. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: maybeDrainReferenceQueues (line 1480)
- Pattern: algorithmic-waste
- What was found: Loop at line 1480 is nested at depth 6 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1480
#### 7. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: maybeDrainReferenceQueues (line 1514)
- Pattern: algorithmic-waste
- What was found: Loop at line 1514 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1514
#### 8. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: maybeDrainReferenceQueues (line 1578)
- Pattern: algorithmic-waste
- What was found: Loop at line 1578 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1578
#### 9. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: maybeDrainReferenceQueues (line 1607)
- Pattern: algorithmic-waste
- What was found: Loop at line 1607 is nested at depth 6 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1607
#### 10. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: maybeDrainReferenceQueues (line 1633)
- Pattern: algorithmic-waste
- What was found: Loop at line 1633 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1633
#### 11. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: nextInTable (line 2578)
- Pattern: algorithmic-waste
- What was found: Loop at line 2578 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 2578

### `guava\src\com\google\common\collect\MapMakerInternalMap.java`

- Pre-analysis: classes 54, methods 139, loops 38, streams 0, synchronized blocks 3
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: containsValue (line 2398)
- Pattern: algorithmic-waste
- What was found: Loop at line 2398 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 2398
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: containsValue (line 2400)
- Pattern: algorithmic-waste
- What was found: Loop at line 2400 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 2400
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: containsValue (line 2405)
- Pattern: algorithmic-waste
- What was found: Loop at line 2405 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 2405
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: containsValue (line 2406)
- Pattern: algorithmic-waste
- What was found: Loop at line 2406 is nested at depth 5 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 2406
#### 5. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: maybeDrainReferenceQueues (line 1479)
- Pattern: algorithmic-waste
- What was found: Loop at line 1479 is nested at depth 5 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1479
#### 6. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: maybeDrainReferenceQueues (line 1480)
- Pattern: algorithmic-waste
- What was found: Loop at line 1480 is nested at depth 6 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1480
#### 7. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: maybeDrainReferenceQueues (line 1514)
- Pattern: algorithmic-waste
- What was found: Loop at line 1514 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1514
#### 8. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: maybeDrainReferenceQueues (line 1578)
- Pattern: algorithmic-waste
- What was found: Loop at line 1578 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1578
#### 9. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: maybeDrainReferenceQueues (line 1607)
- Pattern: algorithmic-waste
- What was found: Loop at line 1607 is nested at depth 6 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1607
#### 10. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: maybeDrainReferenceQueues (line 1633)
- Pattern: algorithmic-waste
- What was found: Loop at line 1633 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1633
#### 11. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: nextInTable (line 2578)
- Pattern: algorithmic-waste
- What was found: Loop at line 2578 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 2578

### `android\guava\src\com\google\common\util\concurrent\AtomicLongMap.java`

- Pre-analysis: classes 4, methods 26, loops 11, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: addAndGet (line 110)
- Pattern: algorithmic-waste
- What was found: Loop at line 110 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 110
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: addAndGet (line 120)
- Pattern: algorithmic-waste
- What was found: Loop at line 120 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 120
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: getAndAdd (line 163)
- Pattern: algorithmic-waste
- What was found: Loop at line 163 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 163
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: getAndAdd (line 173)
- Pattern: algorithmic-waste
- What was found: Loop at line 173 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 173
#### 5. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: put (line 200)
- Pattern: algorithmic-waste
- What was found: Loop at line 200 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 200
#### 6. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: put (line 210)
- Pattern: algorithmic-waste
- What was found: Loop at line 210 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 210
#### 7. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: putIfAbsent (line 411)
- Pattern: algorithmic-waste
- What was found: Loop at line 411 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 411
#### 8. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: remove (line 252)
- Pattern: algorithmic-waste
- What was found: Loop at line 252 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 252
#### 9. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: removeAllZeros (line 307)
- Pattern: algorithmic-waste
- What was found: Loop at line 307 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 307
#### 10. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: sum (line 323)
- Pattern: algorithmic-waste
- What was found: Loop at line 323 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 323

### `android\guava-tests\benchmark\com\google\common\util\concurrent\MoreExecutorsDirectExecutorBenchmark.java`

- Pre-analysis: classes 3, methods 8, loops 6, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: before (line 79)
- Pattern: concurrency-misuse
- What was found: Line 79 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: new Thread() {
#### 2. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: before (line 77)
- Pattern: chatty-io
- What was found: Loop at line 77 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: executor.execute(localRunnable);
#### 3. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: before (line 83)
- Pattern: chatty-io
- What was found: Loop at line 83 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: executor.execute(localRunnable);
#### 4. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: timeContendedExecute (line 125)
- Pattern: chatty-io
- What was found: Loop at line 125 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: executor.execute(countingRunnable);
#### 5. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: timeUncontendedExecute (line 110)
- Pattern: chatty-io
- What was found: Loop at line 110 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: executor.execute(countingRunnable);
#### 6. Executor created in application code path
- Severity: Medium
- Confidence: High
- Location: line 20
- Pattern: concurrency-misuse
- What was found: Line 20 creates a new executor instance.
- Why it is wasteful: Creating executors per call can fragment thread pools and increase context switching and idle threads.
- Likely impact: Higher memory use, poorer scheduling efficiency, and harder concurrency control.
- Recommended remediation: Reuse a bounded shared executor sized to the workload.
- Low-waste rationale: Bounded executor reuse reduces idle threads and CPU overhead without reducing useful throughput.
- Evidence: import static com.google.common.util.concurrent.MoreExecutors.newDirectExecutorService;
#### 7. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: before (line 77)
- Pattern: algorithmic-waste
- What was found: Loop at line 77 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 77

### `guava-tests\benchmark\com\google\common\util\concurrent\MoreExecutorsDirectExecutorBenchmark.java`

- Pre-analysis: classes 3, methods 8, loops 6, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: before (line 79)
- Pattern: concurrency-misuse
- What was found: Line 79 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: new Thread() {
#### 2. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: before (line 77)
- Pattern: chatty-io
- What was found: Loop at line 77 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: executor.execute(localRunnable);
#### 3. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: before (line 83)
- Pattern: chatty-io
- What was found: Loop at line 83 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: executor.execute(localRunnable);
#### 4. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: timeContendedExecute (line 125)
- Pattern: chatty-io
- What was found: Loop at line 125 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: executor.execute(countingRunnable);
#### 5. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: timeUncontendedExecute (line 110)
- Pattern: chatty-io
- What was found: Loop at line 110 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: executor.execute(countingRunnable);
#### 6. Executor created in application code path
- Severity: Medium
- Confidence: High
- Location: line 20
- Pattern: concurrency-misuse
- What was found: Line 20 creates a new executor instance.
- Why it is wasteful: Creating executors per call can fragment thread pools and increase context switching and idle threads.
- Likely impact: Higher memory use, poorer scheduling efficiency, and harder concurrency control.
- Recommended remediation: Reuse a bounded shared executor sized to the workload.
- Low-waste rationale: Bounded executor reuse reduces idle threads and CPU overhead without reducing useful throughput.
- Evidence: import static com.google.common.util.concurrent.MoreExecutors.newDirectExecutorService;
#### 7. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: before (line 77)
- Pattern: algorithmic-waste
- What was found: Loop at line 77 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 77

### `android\guava\src\com\google\common\collect\ConcurrentHashMultiset.java`

- Pre-analysis: classes 5, methods 23, loops 10, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: add (line 235)
- Pattern: algorithmic-waste
- What was found: Loop at line 235 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 235
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: add (line 245)
- Pattern: algorithmic-waste
- What was found: Loop at line 245 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 245
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: entryIterator (line 538)
- Pattern: algorithmic-waste
- What was found: Loop at line 538 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 538
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: remove (line 305)
- Pattern: algorithmic-waste
- What was found: Loop at line 305 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 305
#### 5. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: removeExactly (line 346)
- Pattern: algorithmic-waste
- What was found: Loop at line 346 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 346
#### 6. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: setCount (line 375)
- Pattern: algorithmic-waste
- What was found: Loop at line 375 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 375
#### 7. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: setCount (line 389)
- Pattern: algorithmic-waste
- What was found: Loop at line 389 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 389
#### 8. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: size (line 168)
- Pattern: algorithmic-waste
- What was found: Loop at line 168 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 168
#### 9. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: add (line 235)
- Pattern: allocation-pressure
- What was found: Loop at line 235 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: "Overflow adding " + occurrences + " occurrences to a count of " + oldValue);
#### 10. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: add (line 245)
- Pattern: allocation-pressure
- What was found: Loop at line 245 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: "Overflow adding " + occurrences + " occurrences to a count of " + oldValue);

### `android\guava\src\com\google\common\collect\Lists.java`

- Pre-analysis: classes 15, methods 1, loops 13, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Lists (line 1024)
- Pattern: algorithmic-waste
- What was found: Loop at line 1024 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1024
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Lists (line 1065)
- Pattern: algorithmic-waste
- What was found: Loop at line 1065 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1065
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Lists (line 1071)
- Pattern: algorithmic-waste
- What was found: Loop at line 1071 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1071
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Lists (line 1097)
- Pattern: algorithmic-waste
- What was found: Loop at line 1097 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1097
#### 5. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Lists (line 1103)
- Pattern: algorithmic-waste
- What was found: Loop at line 1103 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1103
#### 6. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Lists (line 424)
- Pattern: algorithmic-waste
- What was found: Loop at line 424 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 424
#### 7. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Lists (line 425)
- Pattern: algorithmic-waste
- What was found: Loop at line 425 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 425
#### 8. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Lists (line 482)
- Pattern: algorithmic-waste
- What was found: Loop at line 482 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 482
#### 9. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Lists (line 483)
- Pattern: algorithmic-waste
- What was found: Loop at line 483 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 483

### `android\guava-testlib\src\com\google\common\collect\testing\Helpers.java`

- Pre-analysis: classes 6, methods 35, loops 13, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 306
- Pattern: algorithmic-waste
- What was found: Loop at line 306 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 306
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 309
- Pattern: algorithmic-waste
- What was found: Loop at line 309 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 309
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 317
- Pattern: algorithmic-waste
- What was found: Loop at line 317 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 317
#### 4. Nested loop with repeated lookup work
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
#### 5. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 333
- Pattern: algorithmic-waste
- What was found: Loop at line 333 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 333
#### 6. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 342
- Pattern: algorithmic-waste
- What was found: Loop at line 342 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 342
#### 7. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 306
- Pattern: allocation-pressure
- What was found: Loop at line 306 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: comparator + ".compare(" + lesser + ", " + t + ")", comparator.compare(lesser, t) < 0); | assertEquals(comparator + ".compare(" + t + ", " + t + ")", 0, comparator.compare(t, t)); | comparator + ".compare(" + greater + ", " + t + ")",
#### 8. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 309
- Pattern: allocation-pressure
- What was found: Loop at line 309 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: comparator + ".compare(" + lesser + ", " + t + ")", comparator.compare(lesser, t) < 0);
#### 9. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 317
- Pattern: allocation-pressure
- What was found: Loop at line 317 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: comparator + ".compare(" + greater + ", " + t + ")",
#### 10. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 330
- Pattern: allocation-pressure
- What was found: Loop at line 330 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertTrue(lesser + ".compareTo(" + t + ')', lesser.compareTo(t) < 0); | assertEquals(t + ".compareTo(" + t + ')', 0, t.compareTo(t)); | assertTrue(greater + ".compareTo(" + t + ')', greater.compareTo(t) > 0);
#### 11. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 333
- Pattern: allocation-pressure
- What was found: Loop at line 333 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertTrue(lesser + ".compareTo(" + t + ')', lesser.compareTo(t) < 0);
#### 12. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 342
- Pattern: allocation-pressure
- What was found: Loop at line 342 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertTrue(greater + ".compareTo(" + t + ')', greater.compareTo(t) > 0);

### `guava\src\com\google\common\collect\ConcurrentHashMultiset.java`

- Pre-analysis: classes 5, methods 23, loops 10, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: add (line 235)
- Pattern: algorithmic-waste
- What was found: Loop at line 235 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 235
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: add (line 245)
- Pattern: algorithmic-waste
- What was found: Loop at line 245 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 245
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: entryIterator (line 538)
- Pattern: algorithmic-waste
- What was found: Loop at line 538 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 538
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: remove (line 305)
- Pattern: algorithmic-waste
- What was found: Loop at line 305 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 305
#### 5. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: removeExactly (line 346)
- Pattern: algorithmic-waste
- What was found: Loop at line 346 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 346
#### 6. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: setCount (line 375)
- Pattern: algorithmic-waste
- What was found: Loop at line 375 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 375
#### 7. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: setCount (line 389)
- Pattern: algorithmic-waste
- What was found: Loop at line 389 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 389
#### 8. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: size (line 168)
- Pattern: algorithmic-waste
- What was found: Loop at line 168 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 168
#### 9. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: add (line 235)
- Pattern: allocation-pressure
- What was found: Loop at line 235 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: "Overflow adding " + occurrences + " occurrences to a count of " + oldValue);
#### 10. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: add (line 245)
- Pattern: allocation-pressure
- What was found: Loop at line 245 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: "Overflow adding " + occurrences + " occurrences to a count of " + oldValue);

### `guava\src\com\google\common\collect\Lists.java`

- Pre-analysis: classes 15, methods 1, loops 13, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Lists (line 1038)
- Pattern: algorithmic-waste
- What was found: Loop at line 1038 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1038
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Lists (line 1079)
- Pattern: algorithmic-waste
- What was found: Loop at line 1079 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1079
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Lists (line 1085)
- Pattern: algorithmic-waste
- What was found: Loop at line 1085 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1085
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Lists (line 1111)
- Pattern: algorithmic-waste
- What was found: Loop at line 1111 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1111
#### 5. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Lists (line 1117)
- Pattern: algorithmic-waste
- What was found: Loop at line 1117 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1117
#### 6. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Lists (line 425)
- Pattern: algorithmic-waste
- What was found: Loop at line 425 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 425
#### 7. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Lists (line 426)
- Pattern: algorithmic-waste
- What was found: Loop at line 426 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 426
#### 8. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Lists (line 483)
- Pattern: algorithmic-waste
- What was found: Loop at line 483 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 483
#### 9. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Lists (line 484)
- Pattern: algorithmic-waste
- What was found: Loop at line 484 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 484

### `guava-testlib\src\com\google\common\collect\testing\Helpers.java`

- Pre-analysis: classes 6, methods 35, loops 13, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 306
- Pattern: algorithmic-waste
- What was found: Loop at line 306 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 306
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 309
- Pattern: algorithmic-waste
- What was found: Loop at line 309 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 309
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 317
- Pattern: algorithmic-waste
- What was found: Loop at line 317 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 317
#### 4. Nested loop with repeated lookup work
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
#### 5. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 333
- Pattern: algorithmic-waste
- What was found: Loop at line 333 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 333
#### 6. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 342
- Pattern: algorithmic-waste
- What was found: Loop at line 342 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 342
#### 7. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 306
- Pattern: allocation-pressure
- What was found: Loop at line 306 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: comparator + ".compare(" + lesser + ", " + t + ")", comparator.compare(lesser, t) < 0); | assertEquals(comparator + ".compare(" + t + ", " + t + ")", 0, comparator.compare(t, t)); | comparator + ".compare(" + greater + ", " + t + ")",
#### 8. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 309
- Pattern: allocation-pressure
- What was found: Loop at line 309 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: comparator + ".compare(" + lesser + ", " + t + ")", comparator.compare(lesser, t) < 0);
#### 9. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 317
- Pattern: allocation-pressure
- What was found: Loop at line 317 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: comparator + ".compare(" + greater + ", " + t + ")",
#### 10. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 330
- Pattern: allocation-pressure
- What was found: Loop at line 330 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertTrue(lesser + ".compareTo(" + t + ')', lesser.compareTo(t) < 0); | assertEquals(t + ".compareTo(" + t + ')', 0, t.compareTo(t)); | assertTrue(greater + ".compareTo(" + t + ')', greater.compareTo(t) > 0);
#### 11. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 333
- Pattern: allocation-pressure
- What was found: Loop at line 333 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertTrue(lesser + ".compareTo(" + t + ')', lesser.compareTo(t) < 0);
#### 12. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 342
- Pattern: allocation-pressure
- What was found: Loop at line 342 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertTrue(greater + ".compareTo(" + t + ')', greater.compareTo(t) > 0);

### `android\guava\src\com\google\common\collect\Collections2.java`

- Pre-analysis: classes 8, methods 1, loops 14, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Collections2 (line 186)
- Pattern: algorithmic-waste
- What was found: Loop at line 186 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 186
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Collections2 (line 200)
- Pattern: algorithmic-waste
- What was found: Loop at line 200 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 200
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Collections2 (line 302)
- Pattern: algorithmic-waste
- What was found: Loop at line 302 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 302
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Collections2 (line 437)
- Pattern: algorithmic-waste
- What was found: Loop at line 437 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 437
#### 5. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Collections2 (line 526)
- Pattern: algorithmic-waste
- What was found: Loop at line 526 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 526
#### 6. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Collections2 (line 541)
- Pattern: algorithmic-waste
- What was found: Loop at line 541 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 541
#### 7. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Collections2 (line 681)
- Pattern: algorithmic-waste
- What was found: Loop at line 681 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 681
#### 8. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Collections2 (line 692)
- Pattern: algorithmic-waste
- What was found: Loop at line 692 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 692

### `android\guava\src\com\google\common\collect\Maps.java`

- Pre-analysis: classes 41, methods 1, loops 22, streams 2, synchronized blocks 20
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Maps (line 2790)
- Pattern: algorithmic-waste
- What was found: Loop at line 2790 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 2790
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Maps (line 2804)
- Pattern: algorithmic-waste
- What was found: Loop at line 2804 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 2804
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Maps (line 2915)
- Pattern: algorithmic-waste
- What was found: Loop at line 2915 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 2915
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Maps (line 2929)
- Pattern: algorithmic-waste
- What was found: Loop at line 2929 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 2929
#### 5. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Maps (line 3053)
- Pattern: algorithmic-waste
- What was found: Loop at line 3053 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 3053
#### 6. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Maps (line 3913)
- Pattern: algorithmic-waste
- What was found: Loop at line 3913 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 3913
#### 7. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Maps (line 3928)
- Pattern: algorithmic-waste
- What was found: Loop at line 3928 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 3928
#### 8. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Maps (line 4018)
- Pattern: algorithmic-waste
- What was found: Loop at line 4018 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 4018

### `android\guava-tests\benchmark\com\google\common\collect\SortedCopyBenchmark.java`

- Pre-analysis: classes 2, methods 7, loops 7, streams 0, synchronized blocks 0
#### 1. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: collections (line 93)
- Pattern: allocation-pressure
- What was found: Loop at line 93 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: List<Integer> copy = new ArrayList<>(input);
#### 2. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: collections (line 99)
- Pattern: allocation-pressure
- What was found: Loop at line 99 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: List<Integer> copy = new ArrayList<>(input);
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: collections (line 93)
- Pattern: algorithmic-waste
- What was found: Loop at line 93 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 93
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: collections (line 99)
- Pattern: algorithmic-waste
- What was found: Loop at line 99 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 99
#### 5. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: ordering (line 112)
- Pattern: algorithmic-waste
- What was found: Loop at line 112 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 112
#### 6. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: ordering (line 116)
- Pattern: algorithmic-waste
- What was found: Loop at line 116 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 116
#### 7. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: collections (line 93)
- Pattern: repeated-work
- What was found: Loop at line 93 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: List<Integer> copy = new ArrayList<>(input);
#### 8. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: collections (line 99)
- Pattern: repeated-work
- What was found: Loop at line 99 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: List<Integer> copy = new ArrayList<>(input);

### `guava\src\com\google\common\collect\Maps.java`

- Pre-analysis: classes 41, methods 1, loops 22, streams 2, synchronized blocks 20
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Maps (line 2898)
- Pattern: algorithmic-waste
- What was found: Loop at line 2898 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 2898
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Maps (line 2912)
- Pattern: algorithmic-waste
- What was found: Loop at line 2912 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 2912
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Maps (line 3023)
- Pattern: algorithmic-waste
- What was found: Loop at line 3023 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 3023
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Maps (line 3037)
- Pattern: algorithmic-waste
- What was found: Loop at line 3037 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 3037
#### 5. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Maps (line 3161)
- Pattern: algorithmic-waste
- What was found: Loop at line 3161 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 3161
#### 6. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Maps (line 4116)
- Pattern: algorithmic-waste
- What was found: Loop at line 4116 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 4116
#### 7. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Maps (line 4131)
- Pattern: algorithmic-waste
- What was found: Loop at line 4131 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 4131
#### 8. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Maps (line 4221)
- Pattern: algorithmic-waste
- What was found: Loop at line 4221 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 4221

### `guava-tests\benchmark\com\google\common\collect\SortedCopyBenchmark.java`

- Pre-analysis: classes 2, methods 7, loops 7, streams 0, synchronized blocks 0
#### 1. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: collections (line 93)
- Pattern: allocation-pressure
- What was found: Loop at line 93 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: List<Integer> copy = new ArrayList<>(input);
#### 2. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: collections (line 99)
- Pattern: allocation-pressure
- What was found: Loop at line 99 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: List<Integer> copy = new ArrayList<>(input);
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: collections (line 93)
- Pattern: algorithmic-waste
- What was found: Loop at line 93 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 93
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: collections (line 99)
- Pattern: algorithmic-waste
- What was found: Loop at line 99 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 99
#### 5. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: ordering (line 112)
- Pattern: algorithmic-waste
- What was found: Loop at line 112 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 112
#### 6. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: ordering (line 116)
- Pattern: algorithmic-waste
- What was found: Loop at line 116 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 116
#### 7. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: collections (line 93)
- Pattern: repeated-work
- What was found: Loop at line 93 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: List<Integer> copy = new ArrayList<>(input);
#### 8. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: collections (line 99)
- Pattern: repeated-work
- What was found: Loop at line 99 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: List<Integer> copy = new ArrayList<>(input);

### `android\guava\src\com\google\common\util\concurrent\ThreadFactoryBuilder.java`

- Pre-analysis: classes 2, methods 1, loops 0, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: ThreadFactoryBuilder (line 100)
- Pattern: concurrency-misuse
- What was found: Line 100 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: * @param daemon whether or not new Threads created with this ThreadFactory will be daemon threads
#### 2. Direct thread creation
- Severity: High
- Confidence: High
- Location: ThreadFactoryBuilder (line 117)
- Pattern: concurrency-misuse
- What was found: Line 117 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: * @param priority the priority for new Threads created with this ThreadFactory
#### 3. Direct thread creation
- Severity: High
- Confidence: High
- Location: ThreadFactoryBuilder (line 144)
- Pattern: concurrency-misuse
- What was found: Line 144 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: * @param uncaughtExceptionHandler the uncaught exception handler for new Threads created with
#### 4. Direct thread creation
- Severity: High
- Confidence: High
- Location: ThreadFactoryBuilder (line 196)
- Pattern: concurrency-misuse
- What was found: Line 196 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: return new ThreadFactory() {
#### 5. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 47
- Pattern: concurrency-misuse
- What was found: Line 47 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: * instead of {@code new ThreadFactoryBuilder().setPriority(priority).setDaemon(false).build()}, use

### `guava\src\com\google\common\util\concurrent\ThreadFactoryBuilder.java`

- Pre-analysis: classes 2, methods 1, loops 0, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: ThreadFactoryBuilder (line 100)
- Pattern: concurrency-misuse
- What was found: Line 100 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: * @param daemon whether or not new Threads created with this ThreadFactory will be daemon threads
#### 2. Direct thread creation
- Severity: High
- Confidence: High
- Location: ThreadFactoryBuilder (line 117)
- Pattern: concurrency-misuse
- What was found: Line 117 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: * @param priority the priority for new Threads created with this ThreadFactory
#### 3. Direct thread creation
- Severity: High
- Confidence: High
- Location: ThreadFactoryBuilder (line 144)
- Pattern: concurrency-misuse
- What was found: Line 144 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: * @param uncaughtExceptionHandler the uncaught exception handler for new Threads created with
#### 4. Direct thread creation
- Severity: High
- Confidence: High
- Location: ThreadFactoryBuilder (line 196)
- Pattern: concurrency-misuse
- What was found: Line 196 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: return new ThreadFactory() {
#### 5. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 47
- Pattern: concurrency-misuse
- What was found: Line 47 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: * instead of {@code new ThreadFactoryBuilder().setPriority(priority).setDaemon(false).build()}, use

### `android\guava\src\com\google\common\graph\Graphs.java`

- Pre-analysis: classes 10, methods 1, loops 19, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Graphs (line 105)
- Pattern: algorithmic-waste
- What was found: Loop at line 105 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 105
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Graphs (line 549)
- Pattern: algorithmic-waste
- What was found: Loop at line 549 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 549
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Graphs (line 550)
- Pattern: algorithmic-waste
- What was found: Loop at line 550 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 550
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Graphs (line 576)
- Pattern: algorithmic-waste
- What was found: Loop at line 576 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 576
#### 5. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Graphs (line 577)
- Pattern: algorithmic-waste
- What was found: Loop at line 577 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 577
#### 6. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Graphs (line 607)
- Pattern: algorithmic-waste
- What was found: Loop at line 607 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 607
#### 7. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Graphs (line 608)
- Pattern: algorithmic-waste
- What was found: Loop at line 608 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 608

### `guava\src\com\google\common\graph\Graphs.java`

- Pre-analysis: classes 10, methods 1, loops 19, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Graphs (line 106)
- Pattern: algorithmic-waste
- What was found: Loop at line 106 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 106
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Graphs (line 570)
- Pattern: algorithmic-waste
- What was found: Loop at line 570 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 570
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Graphs (line 571)
- Pattern: algorithmic-waste
- What was found: Loop at line 571 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 571
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Graphs (line 597)
- Pattern: algorithmic-waste
- What was found: Loop at line 597 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 597
#### 5. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Graphs (line 598)
- Pattern: algorithmic-waste
- What was found: Loop at line 598 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 598
#### 6. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Graphs (line 628)
- Pattern: algorithmic-waste
- What was found: Loop at line 628 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 628
#### 7. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Graphs (line 629)
- Pattern: algorithmic-waste
- What was found: Loop at line 629 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 629

### `android\guava-testlib\src\com\google\common\testing\ClassSanityTester.java`

- Pre-analysis: classes 13, methods 22, loops 18, streams 0, synchronized blocks 0
#### 1. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: line 601
- Pattern: allocation-pressure
- What was found: Loop at line 601 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: List<Object> newArgs = new ArrayList<>(args);
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 457
- Pattern: algorithmic-waste
- What was found: Loop at line 457 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 457
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 601
- Pattern: algorithmic-waste
- What was found: Loop at line 601 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 601
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 629
- Pattern: algorithmic-waste
- What was found: Loop at line 629 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 629
#### 5. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: line 601
- Pattern: repeated-work
- What was found: Loop at line 601 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: List<Object> newArgs = new ArrayList<>(args);
#### 6. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 457
- Pattern: allocation-pressure
- What was found: Loop at line 457 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw new AssertionError("Null check failed on return value of " + factory, e);
#### 7. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 504
- Pattern: allocation-pressure
- What was found: Loop at line 504 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: "Serialization failed on return value of " + factory, e.getCause());
#### 8. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 529
- Pattern: allocation-pressure
- What was found: Loop at line 529 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: "Serialization failed on return value of " + factory, e.getCause()); | "Return value of " + factory + " reserialized to an unequal value", e);

### `guava-testlib\src\com\google\common\testing\ClassSanityTester.java`

- Pre-analysis: classes 13, methods 22, loops 18, streams 0, synchronized blocks 0
#### 1. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: line 601
- Pattern: allocation-pressure
- What was found: Loop at line 601 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: List<Object> newArgs = new ArrayList<>(args);
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 457
- Pattern: algorithmic-waste
- What was found: Loop at line 457 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 457
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 601
- Pattern: algorithmic-waste
- What was found: Loop at line 601 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 601
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 629
- Pattern: algorithmic-waste
- What was found: Loop at line 629 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 629
#### 5. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: line 601
- Pattern: repeated-work
- What was found: Loop at line 601 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: List<Object> newArgs = new ArrayList<>(args);
#### 6. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 457
- Pattern: allocation-pressure
- What was found: Loop at line 457 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw new AssertionError("Null check failed on return value of " + factory, e);
#### 7. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 504
- Pattern: allocation-pressure
- What was found: Loop at line 504 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: "Serialization failed on return value of " + factory, e.getCause());
#### 8. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 529
- Pattern: allocation-pressure
- What was found: Loop at line 529 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: "Serialization failed on return value of " + factory, e.getCause()); | "Return value of " + factory + " reserialized to an unequal value", e);

### `android\guava\src\com\google\common\util\concurrent\CycleDetectingLockFactory.java`

- Pre-analysis: classes 18, methods 45, loops 8, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 464
- Pattern: concurrency-misuse
- What was found: Line 464 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: new ThreadLocal<List<LockGraphNode>>() {
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: ExampleStackTrace (line 497)
- Pattern: algorithmic-waste
- What was found: Loop at line 497 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 497
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: createNodes (line 315)
- Pattern: algorithmic-waste
- What was found: Loop at line 315 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 315
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: createNodes (line 319)
- Pattern: algorithmic-waste
- What was found: Loop at line 319 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 319
#### 5. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: lockStateChanged (line 736)
- Pattern: algorithmic-waste
- What was found: Loop at line 736 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 736

### `android\guava-tests\benchmark\com\google\common\collect\ConcurrentHashMultisetBenchmark.java`

- Pre-analysis: classes 4, methods 33, loops 11, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 71
- Pattern: concurrency-misuse
- What was found: Line 71 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: threadPool = newFixedThreadPool(threads, new ThreadFactoryBuilder().setDaemon(true).build());
#### 2. Executor created in application code path
- Severity: Medium
- Confidence: High
- Location: line 22
- Pattern: concurrency-misuse
- What was found: Line 22 creates a new executor instance.
- Why it is wasteful: Creating executors per call can fragment thread pools and increase context switching and idle threads.
- Likely impact: Higher memory use, poorer scheduling efficiency, and harder concurrency control.
- Recommended remediation: Reuse a bounded shared executor sized to the workload.
- Low-waste rationale: Bounded executor reuse reduces idle threads and CPU overhead without reducing useful throughput.
- Evidence: import static java.util.concurrent.Executors.newFixedThreadPool;
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 104
- Pattern: algorithmic-waste
- What was found: Loop at line 104 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 104
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: runAddRemoveSingleThread (line 127)
- Pattern: algorithmic-waste
- What was found: Loop at line 127 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 127
#### 5. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: runAddSingleThread (line 114)
- Pattern: algorithmic-waste
- What was found: Loop at line 114 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 114

### `guava\src\com\google\common\util\concurrent\CycleDetectingLockFactory.java`

- Pre-analysis: classes 18, methods 45, loops 8, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 464
- Pattern: concurrency-misuse
- What was found: Line 464 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: new ThreadLocal<List<LockGraphNode>>() {
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: ExampleStackTrace (line 497)
- Pattern: algorithmic-waste
- What was found: Loop at line 497 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 497
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: createNodes (line 315)
- Pattern: algorithmic-waste
- What was found: Loop at line 315 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 315
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: createNodes (line 319)
- Pattern: algorithmic-waste
- What was found: Loop at line 319 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 319
#### 5. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: lockStateChanged (line 736)
- Pattern: algorithmic-waste
- What was found: Loop at line 736 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 736

### `guava-tests\benchmark\com\google\common\collect\ConcurrentHashMultisetBenchmark.java`

- Pre-analysis: classes 4, methods 33, loops 11, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 71
- Pattern: concurrency-misuse
- What was found: Line 71 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: threadPool = newFixedThreadPool(threads, new ThreadFactoryBuilder().setDaemon(true).build());
#### 2. Executor created in application code path
- Severity: Medium
- Confidence: High
- Location: line 22
- Pattern: concurrency-misuse
- What was found: Line 22 creates a new executor instance.
- Why it is wasteful: Creating executors per call can fragment thread pools and increase context switching and idle threads.
- Likely impact: Higher memory use, poorer scheduling efficiency, and harder concurrency control.
- Recommended remediation: Reuse a bounded shared executor sized to the workload.
- Low-waste rationale: Bounded executor reuse reduces idle threads and CPU overhead without reducing useful throughput.
- Evidence: import static java.util.concurrent.Executors.newFixedThreadPool;
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 104
- Pattern: algorithmic-waste
- What was found: Loop at line 104 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 104
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: runAddRemoveSingleThread (line 127)
- Pattern: algorithmic-waste
- What was found: Loop at line 127 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 127
#### 5. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: runAddSingleThread (line 114)
- Pattern: algorithmic-waste
- What was found: Loop at line 114 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 114

### `android\guava\src\com\google\common\collect\CartesianList.java`

- Pre-analysis: classes 1, methods 7, loops 5, streams 0, synchronized blocks 0
#### 1. List membership checks inside loop
- Severity: Medium
- Confidence: Medium
- Location: contains (line 162)
- Pattern: algorithmic-waste
- What was found: Loop at line 162 performs `.contains(...)` checks that may scan collections repeatedly.
- Why it is wasteful: Repeated linear scans inside iteration can push runtime toward O(n^2) as data sets grow.
- Likely impact: Throughput degradation and elevated CPU time for larger inputs.
- Recommended remediation: Use a `Set` for membership lookups or pre-index data before the loop.
- Low-waste rationale: Indexing once avoids repeated scans and reduces wasted CPU work.
- Evidence: line 162
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: contains (line 162)
- Pattern: algorithmic-waste
- What was found: Loop at line 162 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 162
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: indexOf (line 81)
- Pattern: algorithmic-waste
- What was found: Loop at line 81 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 81
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: lastIndexOf (line 103)
- Pattern: algorithmic-waste
- What was found: Loop at line 103 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 103
#### 5. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 56
- Pattern: algorithmic-waste
- What was found: Loop at line 56 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 56

### `android\guava\src\com\google\common\collect\StandardTable.java`

- Pre-analysis: classes 18, methods 83, loops 14, streams 0, synchronized blocks 2
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 544
- Pattern: algorithmic-waste
- What was found: Loop at line 544 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 544
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: removeAll (line 978)
- Pattern: algorithmic-waste
- What was found: Loop at line 978 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 978
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: removeFromColumnIf (line 467)
- Pattern: algorithmic-waste
- What was found: Loop at line 467 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 467
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: retainAll (line 947)
- Pattern: algorithmic-waste
- What was found: Loop at line 947 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 947
#### 5. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: retainAll (line 991)
- Pattern: algorithmic-waste
- What was found: Loop at line 991 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 991

### `android\guava-tests\benchmark\com\google\common\collect\MapBenchmark.java`

- Pre-analysis: classes 2, methods 19, loops 20, streams 0, synchronized blocks 1
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: get (line 216)
- Pattern: algorithmic-waste
- What was found: Loop at line 216 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 216
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: iterateValuesAndGet (line 275)
- Pattern: algorithmic-waste
- What was found: Loop at line 275 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 275
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: iterateValuesAndGet (line 276)
- Pattern: algorithmic-waste
- What was found: Loop at line 276 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 276
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: iterateWithKeySetAndGet (line 261)
- Pattern: algorithmic-waste
- What was found: Loop at line 261 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 261
#### 5. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: iterateWithKeySetAndGet (line 262)
- Pattern: algorithmic-waste
- What was found: Loop at line 262 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 262

### `android\guava-tests\benchmark\com\google\common\util\concurrent\SingleThreadAbstractFutureBenchmark.java`

- Pre-analysis: classes 1, methods 0, loops 8, streams 0, synchronized blocks 0
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
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 125
- Pattern: algorithmic-waste
- What was found: Loop at line 125 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 125
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 58
- Pattern: algorithmic-waste
- What was found: Loop at line 58 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 58
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 73
- Pattern: algorithmic-waste
- What was found: Loop at line 73 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 73
#### 5. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 94
- Pattern: algorithmic-waste
- What was found: Loop at line 94 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 94

### `guava\src\com\google\common\collect\CartesianList.java`

- Pre-analysis: classes 1, methods 7, loops 5, streams 0, synchronized blocks 0
#### 1. List membership checks inside loop
- Severity: Medium
- Confidence: Medium
- Location: contains (line 162)
- Pattern: algorithmic-waste
- What was found: Loop at line 162 performs `.contains(...)` checks that may scan collections repeatedly.
- Why it is wasteful: Repeated linear scans inside iteration can push runtime toward O(n^2) as data sets grow.
- Likely impact: Throughput degradation and elevated CPU time for larger inputs.
- Recommended remediation: Use a `Set` for membership lookups or pre-index data before the loop.
- Low-waste rationale: Indexing once avoids repeated scans and reduces wasted CPU work.
- Evidence: line 162
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: contains (line 162)
- Pattern: algorithmic-waste
- What was found: Loop at line 162 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 162
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: indexOf (line 81)
- Pattern: algorithmic-waste
- What was found: Loop at line 81 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 81
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: lastIndexOf (line 103)
- Pattern: algorithmic-waste
- What was found: Loop at line 103 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 103
#### 5. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 56
- Pattern: algorithmic-waste
- What was found: Loop at line 56 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 56

### `guava\src\com\google\common\collect\StandardTable.java`

- Pre-analysis: classes 18, methods 85, loops 14, streams 0, synchronized blocks 2
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 574
- Pattern: algorithmic-waste
- What was found: Loop at line 574 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 574
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: removeAll (line 1008)
- Pattern: algorithmic-waste
- What was found: Loop at line 1008 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1008
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: removeFromColumnIf (line 497)
- Pattern: algorithmic-waste
- What was found: Loop at line 497 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 497
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: retainAll (line 1021)
- Pattern: algorithmic-waste
- What was found: Loop at line 1021 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1021
#### 5. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: retainAll (line 977)
- Pattern: algorithmic-waste
- What was found: Loop at line 977 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 977

### `guava-tests\benchmark\com\google\common\collect\MapBenchmark.java`

- Pre-analysis: classes 2, methods 19, loops 20, streams 0, synchronized blocks 1
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: get (line 216)
- Pattern: algorithmic-waste
- What was found: Loop at line 216 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 216
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: iterateValuesAndGet (line 275)
- Pattern: algorithmic-waste
- What was found: Loop at line 275 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 275
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: iterateValuesAndGet (line 276)
- Pattern: algorithmic-waste
- What was found: Loop at line 276 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 276
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: iterateWithKeySetAndGet (line 261)
- Pattern: algorithmic-waste
- What was found: Loop at line 261 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 261
#### 5. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: iterateWithKeySetAndGet (line 262)
- Pattern: algorithmic-waste
- What was found: Loop at line 262 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 262

### `guava-tests\benchmark\com\google\common\util\concurrent\SingleThreadAbstractFutureBenchmark.java`

- Pre-analysis: classes 1, methods 0, loops 8, streams 0, synchronized blocks 0
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
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 125
- Pattern: algorithmic-waste
- What was found: Loop at line 125 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 125
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 58
- Pattern: algorithmic-waste
- What was found: Loop at line 58 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 58
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 73
- Pattern: algorithmic-waste
- What was found: Loop at line 73 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 73
#### 5. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 94
- Pattern: algorithmic-waste
- What was found: Loop at line 94 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 94

### `android\guava\src\com\google\common\net\MediaType.java`

- Pre-analysis: classes 4, methods 39, loops 7, streams 0, synchronized blocks 0
#### 1. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: parse (line 1111)
- Pattern: allocation-pressure
- What was found: Loop at line 1111 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: StringBuilder valueBuilder = new StringBuilder();
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: charset (line 863)
- Pattern: algorithmic-waste
- What was found: Loop at line 863 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 863
#### 3. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: parse (line 1111)
- Pattern: data-movement-bloat
- What was found: Loop at line 1111 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: value = valueBuilder.toString();
#### 4. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: parse (line 1111)
- Pattern: repeated-work
- What was found: Loop at line 1111 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: StringBuilder valueBuilder = new StringBuilder();
#### 5. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: charset (line 863)
- Pattern: allocation-pressure
- What was found: Loop at line 863 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: "Multiple charset values defined: " + value + ", " + currentValue);

### `android\guava\src\com\google\common\util\concurrent\AbstractScheduledService.java`

- Pre-analysis: classes 16, methods 10, loops 1, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: AbstractScheduledService (line 376)
- Pattern: concurrency-misuse
- What was found: Line 376 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: Executors.newSingleThreadScheduledExecutor(new ThreadFactoryImpl());
#### 2. Executor created in application code path
- Severity: Medium
- Confidence: High
- Location: AbstractScheduledService (line 372)
- Pattern: concurrency-misuse
- What was found: Line 372 creates a new executor instance.
- Why it is wasteful: Creating executors per call can fragment thread pools and increase context switching and idle threads.
- Likely impact: Higher memory use, poorer scheduling efficiency, and harder concurrency control.
- Recommended remediation: Reuse a bounded shared executor sized to the workload.
- Low-waste rationale: Bounded executor reuse reduces idle threads and CPU overhead without reducing useful throughput.
- Evidence: return MoreExecutors.newThread(serviceName(), runnable);
#### 3. Executor created in application code path
- Severity: Medium
- Confidence: High
- Location: AbstractScheduledService (line 376)
- Pattern: concurrency-misuse
- What was found: Line 376 creates a new executor instance.
- Why it is wasteful: Creating executors per call can fragment thread pools and increase context switching and idle threads.
- Likely impact: Higher memory use, poorer scheduling efficiency, and harder concurrency control.
- Recommended remediation: Reuse a bounded shared executor sized to the workload.
- Low-waste rationale: Bounded executor reuse reduces idle threads and CPU overhead without reducing useful throughput.
- Evidence: Executors.newSingleThreadScheduledExecutor(new ThreadFactoryImpl());
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 80
- Pattern: algorithmic-waste
- What was found: Loop at line 80 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 80

### `guava\src\com\google\common\net\MediaType.java`

- Pre-analysis: classes 4, methods 39, loops 7, streams 0, synchronized blocks 0
#### 1. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: parse (line 1111)
- Pattern: allocation-pressure
- What was found: Loop at line 1111 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: StringBuilder valueBuilder = new StringBuilder();
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: charset (line 863)
- Pattern: algorithmic-waste
- What was found: Loop at line 863 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 863
#### 3. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: parse (line 1111)
- Pattern: data-movement-bloat
- What was found: Loop at line 1111 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: value = valueBuilder.toString();
#### 4. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: parse (line 1111)
- Pattern: repeated-work
- What was found: Loop at line 1111 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: StringBuilder valueBuilder = new StringBuilder();
#### 5. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: charset (line 863)
- Pattern: allocation-pressure
- What was found: Loop at line 863 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: "Multiple charset values defined: " + value + ", " + currentValue);

### `guava\src\com\google\common\util\concurrent\AbstractScheduledService.java`

- Pre-analysis: classes 16, methods 10, loops 1, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: AbstractScheduledService (line 374)
- Pattern: concurrency-misuse
- What was found: Line 374 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: Executors.newSingleThreadScheduledExecutor(new ThreadFactoryImpl());
#### 2. Executor created in application code path
- Severity: Medium
- Confidence: High
- Location: AbstractScheduledService (line 370)
- Pattern: concurrency-misuse
- What was found: Line 370 creates a new executor instance.
- Why it is wasteful: Creating executors per call can fragment thread pools and increase context switching and idle threads.
- Likely impact: Higher memory use, poorer scheduling efficiency, and harder concurrency control.
- Recommended remediation: Reuse a bounded shared executor sized to the workload.
- Low-waste rationale: Bounded executor reuse reduces idle threads and CPU overhead without reducing useful throughput.
- Evidence: return MoreExecutors.newThread(serviceName(), runnable);
#### 3. Executor created in application code path
- Severity: Medium
- Confidence: High
- Location: AbstractScheduledService (line 374)
- Pattern: concurrency-misuse
- What was found: Line 374 creates a new executor instance.
- Why it is wasteful: Creating executors per call can fragment thread pools and increase context switching and idle threads.
- Likely impact: Higher memory use, poorer scheduling efficiency, and harder concurrency control.
- Recommended remediation: Reuse a bounded shared executor sized to the workload.
- Low-waste rationale: Bounded executor reuse reduces idle threads and CPU overhead without reducing useful throughput.
- Evidence: Executors.newSingleThreadScheduledExecutor(new ThreadFactoryImpl());
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 80
- Pattern: algorithmic-waste
- What was found: Loop at line 80 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 80

### `android\guava\src\com\google\common\base\CharMatcher.java`

- Pre-analysis: classes 35, methods 21, loops 24, streams 0, synchronized blocks 0
#### 1. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: CharMatcher (line 843)
- Pattern: allocation-pressure
- What was found: Loop at line 843 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: StringBuilder builder = new StringBuilder(len).append(sequence, 0, i).append(replacement);
#### 2. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: CharMatcher (line 793)
- Pattern: data-movement-bloat
- What was found: Loop at line 793 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: return sequence.subSequence(first, len).toString();
#### 3. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: CharMatcher (line 813)
- Pattern: data-movement-bloat
- What was found: Loop at line 813 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: return sequence.subSequence(0, last + 1).toString();
#### 4. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: CharMatcher (line 843)
- Pattern: repeated-work
- What was found: Loop at line 843 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: StringBuilder builder = new StringBuilder(len).append(sequence, 0, i).append(replacement);

### `android\guava\src\com\google\common\hash\BloomFilterStrategies.java`

- Pre-analysis: classes 2, methods 13, loops 9, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 134
- Pattern: algorithmic-waste
- What was found: Loop at line 134 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 134
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 81
- Pattern: algorithmic-waste
- What was found: Loop at line 81 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 81
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: putAll (line 264)
- Pattern: algorithmic-waste
- What was found: Loop at line 264 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 264
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: toPlainArray (line 222)
- Pattern: algorithmic-waste
- What was found: Loop at line 222 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 222

### `android\guava\src\com\google\common\util\concurrent\AbstractFuture.java`

- Pre-analysis: classes 11, methods 14, loops 6, streams 0, synchronized blocks 0
#### 1. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: AbstractFuture (line 773)
- Pattern: chatty-io
- What was found: Loop at line 773 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: executeListener(task, requireNonNull(curr.executor));
#### 2. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: AbstractFuture (line 796)
- Pattern: chatty-io
- What was found: Loop at line 796 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: executeListener(task, requireNonNull(curr.executor));
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: AbstractFuture (line 752)
- Pattern: algorithmic-waste
- What was found: Loop at line 752 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 752

### `android\guava\src\com\google\common\util\concurrent\AtomicDoubleArray.java`

- Pre-analysis: classes 2, methods 12, loops 6, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: addAndGet (line 200)
- Pattern: algorithmic-waste
- What was found: Loop at line 200 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 200
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: getAndAdd (line 179)
- Pattern: algorithmic-waste
- What was found: Loop at line 179 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 179
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: toString (line 226)
- Pattern: algorithmic-waste
- What was found: Loop at line 226 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 226
#### 4. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: toString (line 226)
- Pattern: data-movement-bloat
- What was found: Loop at line 226 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: return b.append(']').toString();

### `android\guava\src\com\google\common\util\concurrent\MoreExecutors.java`

- Pre-analysis: classes 8, methods 1, loops 2, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: MoreExecutors (line 300)
- Pattern: concurrency-misuse
- What was found: Line 300 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: new ThreadFactoryBuilder()
#### 2. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: MoreExecutors (line 747)
- Pattern: chatty-io
- What was found: Loop at line 747 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: futures.add(submitAndAddQueueListener(executorService, it.next(), futureQueue));
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: MoreExecutors (line 747)
- Pattern: algorithmic-waste
- What was found: Loop at line 747 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 747

### `android\guava\src\com\google\common\util\concurrent\Striped.java`

- Pre-analysis: classes 12, methods 1, loops 7, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Striped (line 148)
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
- Location: Striped (line 155)
- Pattern: algorithmic-waste
- What was found: Loop at line 155 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 155
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Striped (line 381)
- Pattern: algorithmic-waste
- What was found: Loop at line 381 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 381
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Striped (line 429)
- Pattern: algorithmic-waste
- What was found: Loop at line 429 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 429

### `android\guava-testlib\src\com\google\common\collect\testing\AbstractMapTester.java`

- Pre-analysis: classes 2, methods 36, loops 6, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: expectContents (line 196)
- Pattern: algorithmic-waste
- What was found: Loop at line 196 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 196
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: expectMissing (line 175)
- Pattern: algorithmic-waste
- What was found: Loop at line 175 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 175
#### 3. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: expectContents (line 196)
- Pattern: allocation-pressure
- What was found: Loop at line 196 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: "Wrong value for key " + entry.getKey(), entry.getValue(), getMap().get(entry.getKey()));
#### 4. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: expectMissing (line 175)
- Pattern: allocation-pressure
- What was found: Loop at line 175 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertFalse("Should not contain entry " + entry, actualContents().contains(entry)); | "Should not contain key " + entry.getKey() + " mapped to value " + entry.getValue(),
#### 5. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: expectMissingKeys (line 71)
- Pattern: allocation-pressure
- What was found: Loop at line 71 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertFalse("Should not contain key " + element, getMap().containsKey(element));
#### 6. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: expectMissingValues (line 77)
- Pattern: allocation-pressure
- What was found: Loop at line 77 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertFalse("Should not contain value " + element, getMap().containsValue(element));

### `android\guava-testlib\src\com\google\common\collect\testing\SpliteratorTester.java`

- Pre-analysis: classes 6, methods 15, loops 6, streams 0, synchronized blocks 0
#### 1. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: expect (line 307)
- Pattern: allocation-pressure
- What was found: Loop at line 307 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: List<E> resultsForStrategy = new ArrayList<>();
#### 2. List membership checks inside loop
- Severity: Medium
- Confidence: Medium
- Location: expect (line 307)
- Pattern: algorithmic-waste
- What was found: Loop at line 307 performs `.contains(...)` checks that may scan collections repeatedly.
- Why it is wasteful: Repeated linear scans inside iteration can push runtime toward O(n^2) as data sets grow.
- Likely impact: Throughput degradation and elevated CPU time for larger inputs.
- Recommended remediation: Use a `Set` for membership lookups or pre-index data before the loop.
- Low-waste rationale: Indexing once avoids repeated scans and reduces wasted CPU work.
- Evidence: line 307
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: expect (line 307)
- Pattern: algorithmic-waste
- What was found: Loop at line 307 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 307
#### 4. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: expect (line 307)
- Pattern: repeated-work
- What was found: Loop at line 307 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: List<E> resultsForStrategy = new ArrayList<>();

### `android\guava-testlib\src\com\google\common\collect\testing\testers\SortedMapNavigationTester.java`

- Pre-analysis: classes 1, methods 13, loops 5, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testHeadMap (line 124)
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
- Location: testSubMap (line 149)
- Pattern: algorithmic-waste
- What was found: Loop at line 149 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 149
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testSubMap (line 150)
- Pattern: algorithmic-waste
- What was found: Loop at line 150 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 150
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testTailMap (line 136)
- Pattern: algorithmic-waste
- What was found: Loop at line 136 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 136

### `android\guava-testlib\src\com\google\common\testing\CollectorTester.java`

- Pre-analysis: classes 2, methods 7, loops 5, streams 0, synchronized blocks 0
#### 1. List membership checks inside loop
- Severity: Medium
- Confidence: Medium
- Location: doExpectCollects (line 165)
- Pattern: algorithmic-waste
- What was found: Loop at line 165 performs `.contains(...)` checks that may scan collections repeatedly.
- Why it is wasteful: Repeated linear scans inside iteration can push runtime toward O(n^2) as data sets grow.
- Likely impact: Throughput degradation and elevated CPU time for larger inputs.
- Recommended remediation: Use a `Set` for membership lookups or pre-index data before the loop.
- Low-waste rationale: Indexing once avoids repeated scans and reduces wasted CPU work.
- Evidence: line 165
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: doExpectCollects (line 165)
- Pattern: algorithmic-waste
- What was found: Loop at line 165 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 165
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: result (line 106)
- Pattern: algorithmic-waste
- What was found: Loop at line 106 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 106
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: result (line 120)
- Pattern: algorithmic-waste
- What was found: Loop at line 120 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 120

### `android\guava-tests\benchmark\com\google\common\collect\IteratorBenchmark.java`

- Pre-analysis: classes 1, methods 10, loops 19, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: arrayListIndexed (line 91)
- Pattern: algorithmic-waste
- What was found: Loop at line 91 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 91
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: arrayListIndexed (line 92)
- Pattern: algorithmic-waste
- What was found: Loop at line 92 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 92
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: arrayListIndexedLength (line 102)
- Pattern: algorithmic-waste
- What was found: Loop at line 102 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 102
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: arrayListIndexedLength (line 103)
- Pattern: algorithmic-waste
- What was found: Loop at line 103 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 103

### `guava\src\com\google\common\base\CharMatcher.java`

- Pre-analysis: classes 35, methods 21, loops 24, streams 0, synchronized blocks 0
#### 1. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: CharMatcher (line 843)
- Pattern: allocation-pressure
- What was found: Loop at line 843 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: StringBuilder builder = new StringBuilder(len).append(sequence, 0, i).append(replacement);
#### 2. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: CharMatcher (line 793)
- Pattern: data-movement-bloat
- What was found: Loop at line 793 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: return sequence.subSequence(first, len).toString();
#### 3. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: CharMatcher (line 813)
- Pattern: data-movement-bloat
- What was found: Loop at line 813 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: return sequence.subSequence(0, last + 1).toString();
#### 4. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: CharMatcher (line 843)
- Pattern: repeated-work
- What was found: Loop at line 843 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: StringBuilder builder = new StringBuilder(len).append(sequence, 0, i).append(replacement);

### `guava\src\com\google\common\collect\Collections2.java`

- Pre-analysis: classes 8, methods 1, loops 10, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Collections2 (line 328)
- Pattern: algorithmic-waste
- What was found: Loop at line 328 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 328
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Collections2 (line 463)
- Pattern: algorithmic-waste
- What was found: Loop at line 463 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 463
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Collections2 (line 552)
- Pattern: algorithmic-waste
- What was found: Loop at line 552 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 552
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Collections2 (line 567)
- Pattern: algorithmic-waste
- What was found: Loop at line 567 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 567

### `guava\src\com\google\common\hash\BloomFilterStrategies.java`

- Pre-analysis: classes 2, methods 13, loops 9, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 135
- Pattern: algorithmic-waste
- What was found: Loop at line 135 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 135
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 82
- Pattern: algorithmic-waste
- What was found: Loop at line 82 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 82
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: putAll (line 265)
- Pattern: algorithmic-waste
- What was found: Loop at line 265 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 265
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: toPlainArray (line 223)
- Pattern: algorithmic-waste
- What was found: Loop at line 223 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 223

### `guava\src\com\google\common\util\concurrent\AbstractFuture.java`

- Pre-analysis: classes 11, methods 14, loops 6, streams 0, synchronized blocks 0
#### 1. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: AbstractFuture (line 773)
- Pattern: chatty-io
- What was found: Loop at line 773 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: executeListener(task, requireNonNull(curr.executor));
#### 2. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: AbstractFuture (line 796)
- Pattern: chatty-io
- What was found: Loop at line 796 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: executeListener(task, requireNonNull(curr.executor));
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: AbstractFuture (line 752)
- Pattern: algorithmic-waste
- What was found: Loop at line 752 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 752

### `guava\src\com\google\common\util\concurrent\AtomicDoubleArray.java`

- Pre-analysis: classes 2, methods 16, loops 6, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: getAndUpdate (line 240)
- Pattern: algorithmic-waste
- What was found: Loop at line 240 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 240
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: toString (line 288)
- Pattern: algorithmic-waste
- What was found: Loop at line 288 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 288
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: updateAndGet (line 262)
- Pattern: algorithmic-waste
- What was found: Loop at line 262 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 262
#### 4. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: toString (line 288)
- Pattern: data-movement-bloat
- What was found: Loop at line 288 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: return b.append(']').toString();

### `guava\src\com\google\common\util\concurrent\MoreExecutors.java`

- Pre-analysis: classes 8, methods 1, loops 2, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: MoreExecutors (line 297)
- Pattern: concurrency-misuse
- What was found: Line 297 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: new ThreadFactoryBuilder()
#### 2. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: MoreExecutors (line 743)
- Pattern: chatty-io
- What was found: Loop at line 743 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: futures.add(submitAndAddQueueListener(executorService, it.next(), futureQueue));
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: MoreExecutors (line 743)
- Pattern: algorithmic-waste
- What was found: Loop at line 743 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 743

### `guava\src\com\google\common\util\concurrent\Striped.java`

- Pre-analysis: classes 12, methods 1, loops 7, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Striped (line 148)
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
- Location: Striped (line 155)
- Pattern: algorithmic-waste
- What was found: Loop at line 155 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 155
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Striped (line 381)
- Pattern: algorithmic-waste
- What was found: Loop at line 381 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 381
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Striped (line 429)
- Pattern: algorithmic-waste
- What was found: Loop at line 429 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 429

### `guava-testlib\src\com\google\common\collect\testing\AbstractIteratorTester.java`

- Pre-analysis: classes 8, methods 22, loops 5, streams 0, synchronized blocks 0
#### 1. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: verify (line 377)
- Pattern: chatty-io
- What was found: Loop at line 377 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: stimuli[i].executeAndCompare(reference, target);
#### 2. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: verify (line 336)
- Pattern: allocation-pressure
- What was found: Loop at line 336 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: List<E> targetElements = new ArrayList<>();
#### 3. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: verify (line 336)
- Pattern: repeated-work
- What was found: Loop at line 336 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: List<E> targetElements = new ArrayList<>();
#### 4. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: verify (line 377)
- Pattern: allocation-pressure
- What was found: Loop at line 377 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw new AssertionError("failed with stimuli " + subListCopy(stimuli, i + 1), cause);

### `guava-testlib\src\com\google\common\collect\testing\AbstractMapTester.java`

- Pre-analysis: classes 2, methods 36, loops 6, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: expectContents (line 196)
- Pattern: algorithmic-waste
- What was found: Loop at line 196 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 196
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: expectMissing (line 175)
- Pattern: algorithmic-waste
- What was found: Loop at line 175 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 175
#### 3. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: expectContents (line 196)
- Pattern: allocation-pressure
- What was found: Loop at line 196 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: "Wrong value for key " + entry.getKey(), entry.getValue(), getMap().get(entry.getKey()));
#### 4. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: expectMissing (line 175)
- Pattern: allocation-pressure
- What was found: Loop at line 175 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertFalse("Should not contain entry " + entry, actualContents().contains(entry)); | "Should not contain key " + entry.getKey() + " mapped to value " + entry.getValue(),
#### 5. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: expectMissingKeys (line 71)
- Pattern: allocation-pressure
- What was found: Loop at line 71 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertFalse("Should not contain key " + element, getMap().containsKey(element));
#### 6. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: expectMissingValues (line 77)
- Pattern: allocation-pressure
- What was found: Loop at line 77 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertFalse("Should not contain value " + element, getMap().containsValue(element));

### `guava-testlib\src\com\google\common\collect\testing\SpliteratorTester.java`

- Pre-analysis: classes 6, methods 15, loops 6, streams 0, synchronized blocks 0
#### 1. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: expect (line 302)
- Pattern: allocation-pressure
- What was found: Loop at line 302 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: List<E> resultsForStrategy = new ArrayList<>();
#### 2. List membership checks inside loop
- Severity: Medium
- Confidence: Medium
- Location: expect (line 302)
- Pattern: algorithmic-waste
- What was found: Loop at line 302 performs `.contains(...)` checks that may scan collections repeatedly.
- Why it is wasteful: Repeated linear scans inside iteration can push runtime toward O(n^2) as data sets grow.
- Likely impact: Throughput degradation and elevated CPU time for larger inputs.
- Recommended remediation: Use a `Set` for membership lookups or pre-index data before the loop.
- Low-waste rationale: Indexing once avoids repeated scans and reduces wasted CPU work.
- Evidence: line 302
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: expect (line 302)
- Pattern: algorithmic-waste
- What was found: Loop at line 302 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 302
#### 4. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: expect (line 302)
- Pattern: repeated-work
- What was found: Loop at line 302 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: List<E> resultsForStrategy = new ArrayList<>();

### `guava-testlib\src\com\google\common\collect\testing\testers\SortedMapNavigationTester.java`

- Pre-analysis: classes 1, methods 13, loops 5, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testHeadMap (line 124)
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
- Location: testSubMap (line 149)
- Pattern: algorithmic-waste
- What was found: Loop at line 149 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 149
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testSubMap (line 150)
- Pattern: algorithmic-waste
- What was found: Loop at line 150 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 150
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testTailMap (line 136)
- Pattern: algorithmic-waste
- What was found: Loop at line 136 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 136

### `guava-testlib\src\com\google\common\testing\CollectorTester.java`

- Pre-analysis: classes 2, methods 7, loops 5, streams 0, synchronized blocks 0
#### 1. List membership checks inside loop
- Severity: Medium
- Confidence: Medium
- Location: doExpectCollects (line 163)
- Pattern: algorithmic-waste
- What was found: Loop at line 163 performs `.contains(...)` checks that may scan collections repeatedly.
- Why it is wasteful: Repeated linear scans inside iteration can push runtime toward O(n^2) as data sets grow.
- Likely impact: Throughput degradation and elevated CPU time for larger inputs.
- Recommended remediation: Use a `Set` for membership lookups or pre-index data before the loop.
- Low-waste rationale: Indexing once avoids repeated scans and reduces wasted CPU work.
- Evidence: line 163
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: doExpectCollects (line 163)
- Pattern: algorithmic-waste
- What was found: Loop at line 163 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 163
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: result (line 104)
- Pattern: algorithmic-waste
- What was found: Loop at line 104 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 104
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: result (line 118)
- Pattern: algorithmic-waste
- What was found: Loop at line 118 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 118

### `guava-tests\benchmark\com\google\common\collect\IteratorBenchmark.java`

- Pre-analysis: classes 1, methods 13, loops 23, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: arrayListIndexed (line 91)
- Pattern: algorithmic-waste
- What was found: Loop at line 91 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 91
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: arrayListIndexed (line 92)
- Pattern: algorithmic-waste
- What was found: Loop at line 92 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 92
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: arrayListIndexedLength (line 102)
- Pattern: algorithmic-waste
- What was found: Loop at line 102 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 102
#### 4. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: arrayListIndexedLength (line 103)
- Pattern: algorithmic-waste
- What was found: Loop at line 103 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 103

### `android\guava\src\com\google\common\eventbus\SubscriberRegistry.java`

- Pre-analysis: classes 6, methods 11, loops 6, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: getSubscribers (line 131)
- Pattern: algorithmic-waste
- What was found: Loop at line 131 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 131
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: register (line 77)
- Pattern: algorithmic-waste
- What was found: Loop at line 77 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 77
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: unregister (line 97)
- Pattern: algorithmic-waste
- What was found: Loop at line 97 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 97
#### 4. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: unregister (line 97)
- Pattern: allocation-pressure
- What was found: Loop at line 97 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: "missing event subscriber for an annotated method. Is " + listener + " registered?");

### `android\guava\src\com\google\common\io\BaseEncoding.java`

- Pre-analysis: classes 9, methods 69, loops 29, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: canDecode (line 1186)
- Pattern: algorithmic-waste
- What was found: Loop at line 1186 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1186
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: ignoringReader (line 1067)
- Pattern: algorithmic-waste
- What was found: Loop at line 1067 is nested at depth 5 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1067
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 1198
- Pattern: algorithmic-waste
- What was found: Loop at line 1198 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1198
#### 4. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: decodingStream (line 793)
- Pattern: allocation-pressure
- What was found: Loop at line 793 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw new DecodingException("Invalid input length " + readChars); | throw new DecodingException("Padding cannot start at index " + readChars); | "Expected padding character but found '" + ch + "' at index " + readChars);

### `android\guava\src\com\google\common\net\InetAddresses.java`

- Pre-analysis: classes 10, methods 1, loops 20, streams 0, synchronized blocks 0
#### 1. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: InetAddresses (line 840)
- Pattern: chatty-io
- What was found: Loop at line 840 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: for (int i = 0; i < clientBytes.length; i++) { | // Teredo obfuscates the mapped client IP, per section 4 of the RFC. | clientBytes[i] = (byte) ~clientBytes[i];
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: InetAddresses (line 255)
- Pattern: algorithmic-waste
- What was found: Loop at line 255 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 255
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: InetAddresses (line 319)
- Pattern: algorithmic-waste
- What was found: Loop at line 319 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 319

### `android\guava-testlib\src\com\google\common\collect\testing\AbstractContainerTester.java`

- Pre-analysis: classes 3, methods 25, loops 2, streams 0, synchronized blocks 0
#### 1. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: getOrderedElements (line 226)
- Pattern: allocation-pressure
- What was found: Loop at line 226 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: for (E e : getSubjectGenerator().order(new ArrayList<E>(getSampleElements()))) {
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: expectMissing (line 168)
- Pattern: algorithmic-waste
- What was found: Loop at line 168 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 168
#### 3. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: getOrderedElements (line 226)
- Pattern: repeated-work
- What was found: Loop at line 226 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: for (E e : getSubjectGenerator().order(new ArrayList<E>(getSampleElements()))) {
#### 4. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: expectMissing (line 168)
- Pattern: allocation-pressure
- What was found: Loop at line 168 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertFalse("Should not contain " + element, actualContents().contains(element));

### `android\guava-testlib\src\com\google\common\collect\testing\testers\CollectionToArrayTester.java`

- Pre-analysis: classes 1, methods 16, loops 2, streams 0, synchronized blocks 0
#### 1. List membership checks inside loop
- Severity: Medium
- Confidence: Medium
- Location: testToArray_oversizedArray (line 141)
- Pattern: algorithmic-waste
- What was found: Loop at line 141 performs `.contains(...)` checks that may scan collections repeatedly.
- Why it is wasteful: Repeated linear scans inside iteration can push runtime toward O(n^2) as data sets grow.
- Likely impact: Throughput degradation and elevated CPU time for larger inputs.
- Recommended remediation: Use a `Set` for membership lookups or pre-index data before the loop.
- Low-waste rationale: Indexing once avoids repeated scans and reduces wasted CPU work.
- Evidence: line 141
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testToArray_oversizedArray (line 141)
- Pattern: algorithmic-waste
- What was found: Loop at line 141 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 141
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testToArray_oversizedArray_ordered (line 161)
- Pattern: algorithmic-waste
- What was found: Loop at line 161 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 161
#### 4. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: testToArray_oversizedArray (line 141)
- Pattern: allocation-pressure
- What was found: Loop at line 141 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: "toArray(overSizedE[]) should contain element " + expectedSubArray[i],

### `guava\src\com\google\common\collect\JdkBackedImmutableMap.java`

- Pre-analysis: classes 1, methods 7, loops 2, streams 0, synchronized blocks 0
#### 1. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: line 51
- Pattern: allocation-pressure
- What was found: Loop at line 51 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: duplicates = new HashMap<>();
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 71
- Pattern: algorithmic-waste
- What was found: Loop at line 71 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 71
#### 3. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: line 51
- Pattern: repeated-work
- What was found: Loop at line 51 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: duplicates = new HashMap<>();
#### 4. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 51
- Pattern: allocation-pressure
- What was found: Loop at line 51 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw conflictException("key", entryArray[i], entryArray[i].getKey() + "=" + oldValue);

### `guava\src\com\google\common\eventbus\SubscriberRegistry.java`

- Pre-analysis: classes 6, methods 11, loops 6, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: getSubscribers (line 131)
- Pattern: algorithmic-waste
- What was found: Loop at line 131 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 131
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: register (line 77)
- Pattern: algorithmic-waste
- What was found: Loop at line 77 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 77
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: unregister (line 97)
- Pattern: algorithmic-waste
- What was found: Loop at line 97 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 97
#### 4. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: unregister (line 97)
- Pattern: allocation-pressure
- What was found: Loop at line 97 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: "missing event subscriber for an annotated method. Is " + listener + " registered?");

### `guava\src\com\google\common\io\BaseEncoding.java`

- Pre-analysis: classes 9, methods 69, loops 29, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: canDecode (line 1186)
- Pattern: algorithmic-waste
- What was found: Loop at line 1186 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1186
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: ignoringReader (line 1067)
- Pattern: algorithmic-waste
- What was found: Loop at line 1067 is nested at depth 5 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1067
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 1198
- Pattern: algorithmic-waste
- What was found: Loop at line 1198 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1198
#### 4. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: decodingStream (line 793)
- Pattern: allocation-pressure
- What was found: Loop at line 793 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw new DecodingException("Invalid input length " + readChars); | throw new DecodingException("Padding cannot start at index " + readChars); | "Expected padding character but found '" + ch + "' at index " + readChars);

### `guava\src\com\google\common\net\InetAddresses.java`

- Pre-analysis: classes 10, methods 1, loops 20, streams 0, synchronized blocks 0
#### 1. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: InetAddresses (line 840)
- Pattern: chatty-io
- What was found: Loop at line 840 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: for (int i = 0; i < clientBytes.length; i++) { | // Teredo obfuscates the mapped client IP, per section 4 of the RFC. | clientBytes[i] = (byte) ~clientBytes[i];
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: InetAddresses (line 255)
- Pattern: algorithmic-waste
- What was found: Loop at line 255 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 255
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: InetAddresses (line 319)
- Pattern: algorithmic-waste
- What was found: Loop at line 319 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 319

### `guava-testlib\src\com\google\common\collect\testing\AbstractContainerTester.java`

- Pre-analysis: classes 3, methods 25, loops 2, streams 0, synchronized blocks 0
#### 1. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: getOrderedElements (line 226)
- Pattern: allocation-pressure
- What was found: Loop at line 226 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: for (E e : getSubjectGenerator().order(new ArrayList<E>(getSampleElements()))) {
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: expectMissing (line 168)
- Pattern: algorithmic-waste
- What was found: Loop at line 168 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 168
#### 3. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: getOrderedElements (line 226)
- Pattern: repeated-work
- What was found: Loop at line 226 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: for (E e : getSubjectGenerator().order(new ArrayList<E>(getSampleElements()))) {
#### 4. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: expectMissing (line 168)
- Pattern: allocation-pressure
- What was found: Loop at line 168 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertFalse("Should not contain " + element, actualContents().contains(element));

### `guava-testlib\src\com\google\common\collect\testing\testers\CollectionToArrayTester.java`

- Pre-analysis: classes 1, methods 16, loops 2, streams 0, synchronized blocks 0
#### 1. List membership checks inside loop
- Severity: Medium
- Confidence: Medium
- Location: testToArray_oversizedArray (line 141)
- Pattern: algorithmic-waste
- What was found: Loop at line 141 performs `.contains(...)` checks that may scan collections repeatedly.
- Why it is wasteful: Repeated linear scans inside iteration can push runtime toward O(n^2) as data sets grow.
- Likely impact: Throughput degradation and elevated CPU time for larger inputs.
- Recommended remediation: Use a `Set` for membership lookups or pre-index data before the loop.
- Low-waste rationale: Indexing once avoids repeated scans and reduces wasted CPU work.
- Evidence: line 141
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testToArray_oversizedArray (line 141)
- Pattern: algorithmic-waste
- What was found: Loop at line 141 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 141
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testToArray_oversizedArray_ordered (line 161)
- Pattern: algorithmic-waste
- What was found: Loop at line 161 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 161
#### 4. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: testToArray_oversizedArray (line 141)
- Pattern: allocation-pressure
- What was found: Loop at line 141 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: "toArray(overSizedE[]) should contain element " + expectedSubArray[i],

### `android\guava\src\com\google\common\collect\Iterators.java`

- Pre-analysis: classes 12, methods 22, loops 27, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Iterators (line 209)
- Pattern: algorithmic-waste
- What was found: Loop at line 209 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 209
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Iterators (line 254)
- Pattern: algorithmic-waste
- What was found: Loop at line 254 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 254
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Iterators (line 383)
- Pattern: algorithmic-waste
- What was found: Loop at line 383 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 383

### `android\guava\src\com\google\common\collect\SortedLists.java`

- Pre-analysis: classes 3, methods 1, loops 3, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: SortedLists (line 100)
- Pattern: algorithmic-waste
- What was found: Loop at line 100 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 100
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: SortedLists (line 289)
- Pattern: algorithmic-waste
- What was found: Loop at line 289 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 289
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: SortedLists (line 74)
- Pattern: algorithmic-waste
- What was found: Loop at line 74 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 74

### `android\guava\src\com\google\common\eventbus\Dispatcher.java`

- Pre-analysis: classes 6, methods 10, loops 5, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 81
- Pattern: concurrency-misuse
- What was found: Line 81 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: new ThreadLocal<Queue<Event>>() {
#### 2. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 91
- Pattern: concurrency-misuse
- What was found: Line 91 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: new ThreadLocal<Boolean>() {

### `android\guava\src\com\google\common\hash\Murmur3_32HashFunction.java`

- Pre-analysis: classes 2, methods 27, loops 11, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: putBytes (line 325)
- Pattern: algorithmic-waste
- What was found: Loop at line 325 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 325
#### 2. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: hashString (line 179)
- Pattern: data-movement-bloat
- What was found: Loop at line 179 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: return hashBytes(input.toString().getBytes(charset));
#### 3. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: putString (line 375)
- Pattern: data-movement-bloat
- What was found: Loop at line 375 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: putBytes(input.subSequence(i, utf16Length).toString().getBytes(charset));

### `android\guava\src\com\google\common\util\concurrent\ExecutionSequencer.java`

- Pre-analysis: classes 11, methods 1, loops 1, streams 0, synchronized blocks 1
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: ExecutionSequencer (line 104)
- Pattern: concurrency-misuse
- What was found: Line 104 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: @LazyInit private ThreadConfinedTaskQueue latestTaskQueue = new ThreadConfinedTaskQueue();
#### 2. Direct thread creation
- Severity: High
- Confidence: High
- Location: ExecutionSequencer (line 395)
- Pattern: concurrency-misuse
- What was found: Line 395 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: ThreadConfinedTaskQueue executingTaskQueue = new ThreadConfinedTaskQueue();

### `android\guava\src\com\google\common\util\concurrent\SequentialExecutor.java`

- Pre-analysis: classes 3, methods 5, loops 1, streams 0, synchronized blocks 7
#### 1. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: workOnQueue (line 211)
- Pattern: chatty-io
- What was found: Loop at line 211 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: // from execute().
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: workOnQueue (line 211)
- Pattern: algorithmic-waste
- What was found: Loop at line 211 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 211
#### 3. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: workOnQueue (line 211)
- Pattern: allocation-pressure
- What was found: Loop at line 211 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: log.get().log(Level.SEVERE, "Exception while executing runnable " + task, e);

### `android\guava-testlib\src\com\google\common\collect\testing\google\AbstractBiMapTester.java`

- Pre-analysis: classes 1, methods 3, loops 3, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: expectContents (line 61)
- Pattern: algorithmic-waste
- What was found: Loop at line 61 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 61
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: expectMissing (line 72)
- Pattern: algorithmic-waste
- What was found: Loop at line 72 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 72
#### 3. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: expectContents (line 61)
- Pattern: allocation-pressure
- What was found: Loop at line 61 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: "Wrong key for value " + entry.getValue(),
#### 4. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: expectMissing (line 72)
- Pattern: allocation-pressure
- What was found: Loop at line 72 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: "Inverse should not contain entry " + reversed, inv.entrySet().contains(reversed)); | "Inverse should not contain key " + reversed.getKey(), | "Inverse should not contain value " + reversed.getValue(),

### `android\guava-testlib\src\com\google\common\collect\testing\google\ListMultimapPutTester.java`

- Pre-analysis: classes 1, methods 2, loops 3, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testPutAddsValueAtEnd (line 43)
- Pattern: algorithmic-waste
- What was found: Loop at line 43 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 43
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testPutAddsValueAtEnd (line 44)
- Pattern: algorithmic-waste
- What was found: Loop at line 44 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 44
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testPutDuplicateValue (line 64)
- Pattern: algorithmic-waste
- What was found: Loop at line 64 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 64

### `android\guava-testlib\src\com\google\common\collect\testing\google\MultimapAsMapTester.java`

- Pre-analysis: classes 1, methods 9, loops 2, streams 0, synchronized blocks 0
#### 1. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: testAsMapGet (line 55)
- Pattern: allocation-pressure
- What was found: Loop at line 55 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: List<V> expectedValues = new ArrayList<>();
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testAsMapGet (line 55)
- Pattern: algorithmic-waste
- What was found: Loop at line 55 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 55
#### 3. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: testAsMapGet (line 55)
- Pattern: repeated-work
- What was found: Loop at line 55 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: List<V> expectedValues = new ArrayList<>();

### `android\guava-testlib\src\com\google\common\collect\testing\google\MultimapTestSuiteBuilder.java`

- Pre-analysis: classes 9, methods 51, loops 16, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: computeMultimapGetFeatures (line 289)
- Pattern: algorithmic-waste
- What was found: Loop at line 289 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 289
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: create (line 518)
- Pattern: algorithmic-waste
- What was found: Loop at line 518 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 518
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: order (line 384)
- Pattern: algorithmic-waste
- What was found: Loop at line 384 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 384

### `android\guava-testlib\src\com\google\common\collect\testing\google\MultisetTestSuiteBuilder.java`

- Pre-analysis: classes 6, methods 18, loops 5, streams 0, synchronized blocks 0
#### 1. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: order (line 249)
- Pattern: allocation-pressure
- What was found: Loop at line 249 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: for (E e : gen.order(new ArrayList<E>(map.keySet()))) {
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: order (line 249)
- Pattern: algorithmic-waste
- What was found: Loop at line 249 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 249
#### 3. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: order (line 249)
- Pattern: repeated-work
- What was found: Loop at line 249 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: for (E e : gen.order(new ArrayList<E>(map.keySet()))) {

### `android\guava-tests\benchmark\com\google\common\hash\HashStringBenchmark.java`

- Pre-analysis: classes 2, methods 8, loops 7, streams 0, synchronized blocks 0
#### 1. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: setUp (line 104)
- Pattern: allocation-pressure
- What was found: Loop at line 104 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: StringBuilder sb = new StringBuilder();
#### 2. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: setUp (line 104)
- Pattern: data-movement-bloat
- What was found: Loop at line 104 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: strings[i] = sb.toString();
#### 3. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: setUp (line 104)
- Pattern: repeated-work
- What was found: Loop at line 104 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: StringBuilder sb = new StringBuilder();

### `android\guava-tests\benchmark\com\google\common\math\QuantilesBenchmark.java`

- Pre-analysis: classes 1, methods 8, loops 8, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: allDeciles (line 108)
- Pattern: algorithmic-waste
- What was found: Loop at line 108 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 108
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: percentiles90And99 (line 90)
- Pattern: algorithmic-waste
- What was found: Loop at line 90 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 90
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: threePercentiles (line 99)
- Pattern: algorithmic-waste
- What was found: Loop at line 99 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 99

### `guava\src\com\google\common\collect\Iterators.java`

- Pre-analysis: classes 12, methods 22, loops 27, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Iterators (line 209)
- Pattern: algorithmic-waste
- What was found: Loop at line 209 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 209
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Iterators (line 254)
- Pattern: algorithmic-waste
- What was found: Loop at line 254 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 254
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Iterators (line 383)
- Pattern: algorithmic-waste
- What was found: Loop at line 383 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 383

### `guava\src\com\google\common\collect\SortedLists.java`

- Pre-analysis: classes 3, methods 1, loops 3, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: SortedLists (line 100)
- Pattern: algorithmic-waste
- What was found: Loop at line 100 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 100
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: SortedLists (line 289)
- Pattern: algorithmic-waste
- What was found: Loop at line 289 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 289
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: SortedLists (line 74)
- Pattern: algorithmic-waste
- What was found: Loop at line 74 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 74

### `guava\src\com\google\common\eventbus\Dispatcher.java`

- Pre-analysis: classes 6, methods 10, loops 5, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 81
- Pattern: concurrency-misuse
- What was found: Line 81 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: new ThreadLocal<Queue<Event>>() {
#### 2. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 91
- Pattern: concurrency-misuse
- What was found: Line 91 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: new ThreadLocal<Boolean>() {

### `guava\src\com\google\common\hash\Murmur3_32HashFunction.java`

- Pre-analysis: classes 2, methods 27, loops 11, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: putBytes (line 325)
- Pattern: algorithmic-waste
- What was found: Loop at line 325 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 325
#### 2. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: hashString (line 179)
- Pattern: data-movement-bloat
- What was found: Loop at line 179 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: return hashBytes(input.toString().getBytes(charset));
#### 3. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: putString (line 375)
- Pattern: data-movement-bloat
- What was found: Loop at line 375 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: putBytes(input.subSequence(i, utf16Length).toString().getBytes(charset));

### `guava\src\com\google\common\util\concurrent\ExecutionSequencer.java`

- Pre-analysis: classes 11, methods 1, loops 1, streams 0, synchronized blocks 1
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: ExecutionSequencer (line 104)
- Pattern: concurrency-misuse
- What was found: Line 104 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: @LazyInit private ThreadConfinedTaskQueue latestTaskQueue = new ThreadConfinedTaskQueue();
#### 2. Direct thread creation
- Severity: High
- Confidence: High
- Location: ExecutionSequencer (line 395)
- Pattern: concurrency-misuse
- What was found: Line 395 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: ThreadConfinedTaskQueue executingTaskQueue = new ThreadConfinedTaskQueue();

### `guava\src\com\google\common\util\concurrent\SequentialExecutor.java`

- Pre-analysis: classes 3, methods 5, loops 1, streams 0, synchronized blocks 7
#### 1. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: workOnQueue (line 211)
- Pattern: chatty-io
- What was found: Loop at line 211 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: // from execute().
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: workOnQueue (line 211)
- Pattern: algorithmic-waste
- What was found: Loop at line 211 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 211
#### 3. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: workOnQueue (line 211)
- Pattern: allocation-pressure
- What was found: Loop at line 211 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: log.get().log(Level.SEVERE, "Exception while executing runnable " + task, e);

### `guava-testlib\src\com\google\common\collect\testing\google\AbstractBiMapTester.java`

- Pre-analysis: classes 1, methods 3, loops 3, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: expectContents (line 61)
- Pattern: algorithmic-waste
- What was found: Loop at line 61 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 61
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: expectMissing (line 72)
- Pattern: algorithmic-waste
- What was found: Loop at line 72 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 72
#### 3. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: expectContents (line 61)
- Pattern: allocation-pressure
- What was found: Loop at line 61 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: "Wrong key for value " + entry.getValue(),
#### 4. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: expectMissing (line 72)
- Pattern: allocation-pressure
- What was found: Loop at line 72 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: "Inverse should not contain entry " + reversed, inv.entrySet().contains(reversed)); | "Inverse should not contain key " + reversed.getKey(), | "Inverse should not contain value " + reversed.getValue(),

### `guava-testlib\src\com\google\common\collect\testing\google\ListMultimapPutTester.java`

- Pre-analysis: classes 1, methods 2, loops 3, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testPutAddsValueAtEnd (line 43)
- Pattern: algorithmic-waste
- What was found: Loop at line 43 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 43
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testPutAddsValueAtEnd (line 44)
- Pattern: algorithmic-waste
- What was found: Loop at line 44 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 44
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testPutDuplicateValue (line 64)
- Pattern: algorithmic-waste
- What was found: Loop at line 64 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 64

### `guava-testlib\src\com\google\common\collect\testing\google\MultimapAsMapTester.java`

- Pre-analysis: classes 1, methods 9, loops 2, streams 0, synchronized blocks 0
#### 1. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: testAsMapGet (line 55)
- Pattern: allocation-pressure
- What was found: Loop at line 55 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: List<V> expectedValues = new ArrayList<>();
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testAsMapGet (line 55)
- Pattern: algorithmic-waste
- What was found: Loop at line 55 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 55
#### 3. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: testAsMapGet (line 55)
- Pattern: repeated-work
- What was found: Loop at line 55 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: List<V> expectedValues = new ArrayList<>();

### `guava-testlib\src\com\google\common\collect\testing\google\MultimapTestSuiteBuilder.java`

- Pre-analysis: classes 9, methods 51, loops 16, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: computeMultimapGetFeatures (line 290)
- Pattern: algorithmic-waste
- What was found: Loop at line 290 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 290
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: create (line 519)
- Pattern: algorithmic-waste
- What was found: Loop at line 519 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 519
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: order (line 385)
- Pattern: algorithmic-waste
- What was found: Loop at line 385 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 385

### `guava-testlib\src\com\google\common\collect\testing\google\MultisetTestSuiteBuilder.java`

- Pre-analysis: classes 6, methods 18, loops 5, streams 0, synchronized blocks 0
#### 1. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: order (line 250)
- Pattern: allocation-pressure
- What was found: Loop at line 250 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: for (E e : gen.order(new ArrayList<E>(map.keySet()))) {
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: order (line 250)
- Pattern: algorithmic-waste
- What was found: Loop at line 250 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 250
#### 3. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: order (line 250)
- Pattern: repeated-work
- What was found: Loop at line 250 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: for (E e : gen.order(new ArrayList<E>(map.keySet()))) {

### `guava-tests\benchmark\com\google\common\hash\HashStringBenchmark.java`

- Pre-analysis: classes 2, methods 8, loops 7, streams 0, synchronized blocks 0
#### 1. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: setUp (line 104)
- Pattern: allocation-pressure
- What was found: Loop at line 104 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: StringBuilder sb = new StringBuilder();
#### 2. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: setUp (line 104)
- Pattern: data-movement-bloat
- What was found: Loop at line 104 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: strings[i] = sb.toString();
#### 3. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: setUp (line 104)
- Pattern: repeated-work
- What was found: Loop at line 104 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: StringBuilder sb = new StringBuilder();

### `guava-tests\benchmark\com\google\common\math\QuantilesBenchmark.java`

- Pre-analysis: classes 1, methods 8, loops 8, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: allDeciles (line 108)
- Pattern: algorithmic-waste
- What was found: Loop at line 108 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 108
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: percentiles90And99 (line 90)
- Pattern: algorithmic-waste
- What was found: Loop at line 90 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 90
#### 3. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: threePercentiles (line 99)
- Pattern: algorithmic-waste
- What was found: Loop at line 99 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 99

### `android\guava\src\com\google\common\cache\Striped64.java`

- Pre-analysis: classes 7, methods 7, loops 4, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 134
- Pattern: concurrency-misuse
- What was found: Line 134 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: static final ThreadLocal<int @Nullable []> threadHashCode = new ThreadLocal<>();
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: getUnsafe (line 305)
- Pattern: algorithmic-waste
- What was found: Loop at line 305 is nested at depth 5 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 305

### `android\guava\src\com\google\common\collect\LinkedHashMultimap.java`

- Pre-analysis: classes 5, methods 27, loops 9, streams 0, synchronized blocks 1
#### 1. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: clear (line 438)
- Pattern: chatty-io
- What was found: Loop at line 438 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: multimapIterationChain.delete(entry);
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 517
- Pattern: algorithmic-waste
- What was found: Loop at line 517 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 517

### `android\guava\src\com\google\common\hash\Striped64.java`

- Pre-analysis: classes 7, methods 7, loops 4, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 134
- Pattern: concurrency-misuse
- What was found: Line 134 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: static final ThreadLocal<int @Nullable []> threadHashCode = new ThreadLocal<>();
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: getUnsafe (line 305)
- Pattern: algorithmic-waste
- What was found: Loop at line 305 is nested at depth 5 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 305

### `android\guava\src\com\google\common\util\concurrent\AbstractIdleService.java`

- Pre-analysis: classes 4, methods 5, loops 0, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 43
- Pattern: concurrency-misuse
- What was found: Line 43 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: private final Supplier<String> threadNameSupplier = new ThreadNameSupplier();
#### 2. Executor created in application code path
- Severity: Medium
- Confidence: High
- Location: line 17
- Pattern: concurrency-misuse
- What was found: Line 17 creates a new executor instance.
- Why it is wasteful: Creating executors per call can fragment thread pools and increase context switching and idle threads.
- Likely impact: Higher memory use, poorer scheduling efficiency, and harder concurrency control.
- Recommended remediation: Reuse a bounded shared executor sized to the workload.
- Low-waste rationale: Bounded executor reuse reduces idle threads and CPU overhead without reducing useful throughput.
- Evidence: import static com.google.common.util.concurrent.MoreExecutors.newThread;

### `android\guava\src\com\google\common\util\concurrent\JdkFutureAdapters.java`

- Pre-analysis: classes 2, methods 5, loops 0, streams 0, synchronized blocks 0
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
- Evidence: new ThreadFactoryBuilder()
#### 2. Executor created in application code path
- Severity: Medium
- Confidence: High
- Location: line 19
- Pattern: concurrency-misuse
- What was found: Line 19 creates a new executor instance.
- Why it is wasteful: Creating executors per call can fragment thread pools and increase context switching and idle threads.
- Likely impact: Higher memory use, poorer scheduling efficiency, and harder concurrency control.
- Recommended remediation: Reuse a bounded shared executor sized to the workload.
- Low-waste rationale: Bounded executor reuse reduces idle threads and CPU overhead without reducing useful throughput.
- Evidence: import static java.util.concurrent.Executors.newCachedThreadPool;

### `android\guava\src\com\google\common\util\concurrent\ListenerCallQueue.java`

- Pre-analysis: classes 5, methods 9, loops 3, streams 0, synchronized blocks 7
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: dispatch (line 120)
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
- Location: run (line 194)
- Pattern: algorithmic-waste
- What was found: Loop at line 194 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 194
#### 3. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: run (line 194)
- Pattern: allocation-pressure
- What was found: Loop at line 194 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: "Exception while executing callback: " + listener + " " + nextLabel,

### `android\guava-testlib\src\com\google\common\testing\ArbitraryInstances.java`

- Pre-analysis: classes 14, methods 20, loops 1, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: newThread (line 466)
- Pattern: concurrency-misuse
- What was found: Line 466 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: return new Thread(r);
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 388
- Pattern: algorithmic-waste
- What was found: Loop at line 388 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 388

### `android\guava-tests\benchmark\com\google\common\util\concurrent\AbstractFutureFootprintBenchmark.java`

- Pre-analysis: classes 2, methods 1, loops 4, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: measureSize (line 73)
- Pattern: concurrency-misuse
- What was found: Line 73 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: new Thread() {
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: measureSize (line 71)
- Pattern: algorithmic-waste
- What was found: Loop at line 71 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 71

### `guava\src\com\google\common\collect\LinkedHashMultimap.java`

- Pre-analysis: classes 5, methods 30, loops 10, streams 0, synchronized blocks 1
#### 1. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: clear (line 450)
- Pattern: chatty-io
- What was found: Loop at line 450 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: multimapIterationChain.delete(entry);
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 540
- Pattern: algorithmic-waste
- What was found: Loop at line 540 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 540

### `guava\src\com\google\common\util\concurrent\AbstractIdleService.java`

- Pre-analysis: classes 4, methods 5, loops 0, streams 0, synchronized blocks 0
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
- Evidence: private final Supplier<String> threadNameSupplier = new ThreadNameSupplier();
#### 2. Executor created in application code path
- Severity: Medium
- Confidence: High
- Location: line 17
- Pattern: concurrency-misuse
- What was found: Line 17 creates a new executor instance.
- Why it is wasteful: Creating executors per call can fragment thread pools and increase context switching and idle threads.
- Likely impact: Higher memory use, poorer scheduling efficiency, and harder concurrency control.
- Recommended remediation: Reuse a bounded shared executor sized to the workload.
- Low-waste rationale: Bounded executor reuse reduces idle threads and CPU overhead without reducing useful throughput.
- Evidence: import static com.google.common.util.concurrent.MoreExecutors.newThread;

### `guava\src\com\google\common\util\concurrent\JdkFutureAdapters.java`

- Pre-analysis: classes 2, methods 5, loops 0, streams 0, synchronized blocks 0
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
- Evidence: new ThreadFactoryBuilder()
#### 2. Executor created in application code path
- Severity: Medium
- Confidence: High
- Location: line 19
- Pattern: concurrency-misuse
- What was found: Line 19 creates a new executor instance.
- Why it is wasteful: Creating executors per call can fragment thread pools and increase context switching and idle threads.
- Likely impact: Higher memory use, poorer scheduling efficiency, and harder concurrency control.
- Recommended remediation: Reuse a bounded shared executor sized to the workload.
- Low-waste rationale: Bounded executor reuse reduces idle threads and CPU overhead without reducing useful throughput.
- Evidence: import static java.util.concurrent.Executors.newCachedThreadPool;

### `guava\src\com\google\common\util\concurrent\ListenerCallQueue.java`

- Pre-analysis: classes 5, methods 9, loops 3, streams 0, synchronized blocks 7
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: dispatch (line 120)
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
- Location: run (line 194)
- Pattern: algorithmic-waste
- What was found: Loop at line 194 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 194
#### 3. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: run (line 194)
- Pattern: allocation-pressure
- What was found: Loop at line 194 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: "Exception while executing callback: " + listener + " " + nextLabel,

### `guava-testlib\src\com\google\common\testing\ArbitraryInstances.java`

- Pre-analysis: classes 14, methods 20, loops 1, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: newThread (line 478)
- Pattern: concurrency-misuse
- What was found: Line 478 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: return new Thread(r);
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 400
- Pattern: algorithmic-waste
- What was found: Loop at line 400 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 400

### `guava-tests\benchmark\com\google\common\util\concurrent\AbstractFutureFootprintBenchmark.java`

- Pre-analysis: classes 2, methods 1, loops 4, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: measureSize (line 73)
- Pattern: concurrency-misuse
- What was found: Line 73 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: new Thread() {
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: measureSize (line 71)
- Pattern: algorithmic-waste
- What was found: Loop at line 71 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 71

### `android\guava\src\com\google\common\base\CaseFormat.java`

- Pre-analysis: classes 4, methods 20, loops 1, streams 0, synchronized blocks 0
#### 1. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: convert (line 141)
- Pattern: allocation-pressure
- What was found: Loop at line 141 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: out = new StringBuilder(s.length() + 4 * format.wordSeparator.length());
#### 2. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: convert (line 141)
- Pattern: repeated-work
- What was found: Loop at line 141 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: out = new StringBuilder(s.length() + 4 * format.wordSeparator.length());

### `android\guava\src\com\google\common\base\Predicates.java`

- Pre-analysis: classes 13, methods 62, loops 4, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: apply (line 425)
- Pattern: algorithmic-waste
- What was found: Loop at line 425 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 425
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: apply (line 470)
- Pattern: algorithmic-waste
- What was found: Loop at line 470 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 470

### `android\guava\src\com\google\common\cache\CacheBuilderSpec.java`

- Pre-analysis: classes 18, methods 24, loops 1, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: parse (line 145)
- Pattern: algorithmic-waste
- What was found: Loop at line 145 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 145
#### 2. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: parse (line 145)
- Pattern: repeated-work
- What was found: Loop at line 145 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: valueParser.parse(spec, key, value);

### `android\guava\src\com\google\common\collect\Iterables.java`

- Pre-analysis: classes 4, methods 1, loops 4, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Iterables (line 205)
- Pattern: algorithmic-waste
- What was found: Loop at line 205 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 205
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Iterables (line 240)
- Pattern: algorithmic-waste
- What was found: Loop at line 240 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 240

### `android\guava\src\com\google\common\collect\Multisets.java`

- Pre-analysis: classes 10, methods 1, loops 14, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Multisets (line 456)
- Pattern: algorithmic-waste
- What was found: Loop at line 456 is nested at depth 6 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 456
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Multisets (line 588)
- Pattern: algorithmic-waste
- What was found: Loop at line 588 is nested at depth 6 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 588

### `android\guava\src\com\google\common\collect\SparseImmutableTable.java`

- Pre-analysis: classes 1, methods 6, loops 6, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 61
- Pattern: algorithmic-waste
- What was found: Loop at line 61 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 61
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: writeReplace (line 137)
- Pattern: algorithmic-waste
- What was found: Loop at line 137 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 137

### `android\guava\src\com\google\common\graph\EndpointPairIterator.java`

- Pre-analysis: classes 4, methods 5, loops 3, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 125
- Pattern: algorithmic-waste
- What was found: Loop at line 125 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 125
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 131
- Pattern: algorithmic-waste
- What was found: Loop at line 131 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 131

### `android\guava\src\com\google\common\net\InternetDomainName.java`

- Pre-analysis: classes 6, methods 25, loops 2, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: ancestor (line 561)
- Pattern: algorithmic-waste
- What was found: Loop at line 561 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 561
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: validateSyntax (line 240)
- Pattern: algorithmic-waste
- What was found: Loop at line 240 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 240

### `android\guava\src\com\google\common\util\concurrent\AtomicDouble.java`

- Pre-analysis: classes 3, methods 15, loops 2, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: addAndGet (line 173)
- Pattern: algorithmic-waste
- What was found: Loop at line 173 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 173
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: getAndAdd (line 153)
- Pattern: algorithmic-waste
- What was found: Loop at line 153 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 153

### `android\guava\src\com\google\common\util\concurrent\FuturesGetChecked.java`

- Pre-analysis: classes 7, methods 8, loops 3, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: validateClass (line 127)
- Pattern: algorithmic-waste
- What was found: Loop at line 127 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 127
#### 2. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: line 228
- Pattern: data-movement-bloat
- What was found: Loop at line 228 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: params[i] = cause.toString();

### `android\guava\src\com\google\common\util\concurrent\Uninterruptibles.java`

- Pre-analysis: classes 4, methods 17, loops 12, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 278
- Pattern: algorithmic-waste
- What was found: Loop at line 278 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 278
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 351
- Pattern: algorithmic-waste
- What was found: Loop at line 351 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 351

### `android\guava-testlib\src\com\google\common\collect\testing\AbstractIteratorTester.java`

- Pre-analysis: classes 8, methods 22, loops 3, streams 0, synchronized blocks 0
#### 1. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: verify (line 360)
- Pattern: chatty-io
- What was found: Loop at line 360 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: stimuli[i].executeAndCompare(reference, target);
#### 2. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: verify (line 360)
- Pattern: allocation-pressure
- What was found: Loop at line 360 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw new AssertionError("failed with stimuli " + subListCopy(stimuli, i + 1), cause);

### `android\guava-testlib\src\com\google\common\collect\testing\features\FeatureUtil.java`

- Pre-analysis: classes 8, methods 7, loops 6, streams 0, synchronized blocks 3
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: impliedFeatures (line 86)
- Pattern: algorithmic-waste
- What was found: Loop at line 86 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 86
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: impliedFeatures (line 88)
- Pattern: algorithmic-waste
- What was found: Loop at line 88 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 88

### `android\guava-testlib\src\com\google\common\collect\testing\google\ListMultimapRemoveTester.java`

- Pre-analysis: classes 1, methods 4, loops 3, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testRemoveAtIndexFromAsMapPropagates (line 74)
- Pattern: algorithmic-waste
- What was found: Loop at line 74 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 74
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testRemoveAtIndexFromGetPropagates (line 58)
- Pattern: algorithmic-waste
- What was found: Loop at line 58 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 58

### `android\guava-testlib\src\com\google\common\collect\testing\google\MultimapClearTester.java`

- Pre-analysis: classes 1, methods 12, loops 3, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testClearPropagatesToAsMapGet (line 116)
- Pattern: algorithmic-waste
- What was found: Loop at line 116 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 116
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testClearPropagatesToGet (line 105)
- Pattern: algorithmic-waste
- What was found: Loop at line 105 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 105

### `android\guava-testlib\src\com\google\common\collect\testing\google\MultimapContainsEntryTester.java`

- Pre-analysis: classes 1, methods 7, loops 2, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testContainsEntryAgreesWithGet (line 53)
- Pattern: algorithmic-waste
- What was found: Loop at line 53 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 53
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testContainsEntryAgreesWithGet (line 54)
- Pattern: algorithmic-waste
- What was found: Loop at line 54 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 54

### `android\guava-testlib\src\com\google\common\collect\testing\google\MultimapContainsKeyTester.java`

- Pre-analysis: classes 1, methods 9, loops 4, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testContainsKeyAgreesWithGet (line 56)
- Pattern: algorithmic-waste
- What was found: Loop at line 56 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 56
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testContainsKeyAgreesWithKeySet (line 68)
- Pattern: algorithmic-waste
- What was found: Loop at line 68 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 68

### `android\guava-testlib\src\com\google\common\collect\testing\google\MultimapPutTester.java`

- Pre-analysis: classes 1, methods 13, loops 4, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testPutPresentKeyPropagatesToAsMapGet (line 179)
- Pattern: algorithmic-waste
- What was found: Loop at line 179 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 179
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testPutPresentKeyPropagatesToGet (line 160)
- Pattern: algorithmic-waste
- What was found: Loop at line 160 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 160

### `android\guava-testlib\src\com\google\common\collect\testing\google\MultimapRemoveEntryTester.java`

- Pre-analysis: classes 1, methods 11, loops 4, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testRemovePropagatesToAsMap (line 139)
- Pattern: algorithmic-waste
- What was found: Loop at line 139 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 139
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testRemovePropagatesToGet (line 118)
- Pattern: algorithmic-waste
- What was found: Loop at line 118 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 118

### `android\guava-testlib\src\com\google\common\collect\testing\MapTestSuiteBuilder.java`

- Pre-analysis: classes 3, methods 14, loops 2, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 216
- Pattern: algorithmic-waste
- What was found: Loop at line 216 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 216
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 222
- Pattern: algorithmic-waste
- What was found: Loop at line 222 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 222

### `android\guava-testlib\src\com\google\common\collect\testing\MinimalSet.java`

- Pre-analysis: classes 1, methods 3, loops 2, streams 0, synchronized blocks 0
#### 1. List membership checks inside loop
- Severity: Medium
- Confidence: Medium
- Location: line 54
- Pattern: algorithmic-waste
- What was found: Loop at line 54 performs `.contains(...)` checks that may scan collections repeatedly.
- Why it is wasteful: Repeated linear scans inside iteration can push runtime toward O(n^2) as data sets grow.
- Likely impact: Throughput degradation and elevated CPU time for larger inputs.
- Recommended remediation: Use a `Set` for membership lookups or pre-index data before the loop.
- Low-waste rationale: Indexing once avoids repeated scans and reduces wasted CPU work.
- Evidence: line 54
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 54
- Pattern: algorithmic-waste
- What was found: Loop at line 54 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 54

### `android\guava-testlib\src\com\google\common\collect\testing\testers\ListSubListTester.java`

- Pre-analysis: classes 1, methods 28, loops 3, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testSubList_get (line 232)
- Pattern: algorithmic-waste
- What was found: Loop at line 232 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 232
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testSubList_get (line 233)
- Pattern: algorithmic-waste
- What was found: Loop at line 233 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 233

### `android\guava-testlib\src\com\google\common\collect\testing\testers\MapReplaceAllTester.java`

- Pre-analysis: classes 1, methods 7, loops 2, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testReplaceAllPreservesOrder (line 83)
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
- Location: testReplaceAllRotate (line 65)
- Pattern: algorithmic-waste
- What was found: Loop at line 65 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 65

### `android\guava-testlib\src\com\google\common\testing\EqualsTester.java`

- Pre-analysis: classes 3, methods 4, loops 4, streams 0, synchronized blocks 0
#### 1. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: testItems (line 142)
- Pattern: data-movement-bloat
- What was found: Loop at line 142 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: !item.equals(item.toString()));
#### 2. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: addEqualityGroup (line 114)
- Pattern: allocation-pressure
- What was found: Loop at line 114 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw new NullPointerException("at index " + i);
#### 3. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: testItems (line 142)
- Pattern: allocation-pressure
- What was found: Loop at line 142 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: "the Object#hashCode of " + item + " must be consistent",

### `android\guava-testlib\src\com\google\common\testing\NullPointerTester.java`

- Pre-analysis: classes 8, methods 45, loops 13, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: containsNullable (line 543)
- Pattern: algorithmic-waste
- What was found: Loop at line 543 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 543
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 431
- Pattern: algorithmic-waste
- What was found: Loop at line 431 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 431

### `android\guava-testlib\src\com\google\common\testing\RelationshipTester.java`

- Pre-analysis: classes 3, methods 7, loops 5, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: test (line 76)
- Pattern: algorithmic-waste
- What was found: Loop at line 76 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 76
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: test (line 78)
- Pattern: algorithmic-waste
- What was found: Loop at line 78 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 78

### `android\guava-tests\benchmark\com\google\common\collect\ImmutableListCreationBenchmark.java`

- Pre-analysis: classes 1, methods 4, loops 8, streams 0, synchronized blocks 0
#### 1. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: copyArrayList (line 70)
- Pattern: allocation-pressure
- What was found: Loop at line 70 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: List<Object> builder = new ArrayList<>();
#### 2. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: copyArrayList (line 70)
- Pattern: repeated-work
- What was found: Loop at line 70 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: List<Object> builder = new ArrayList<>();

### `guava\src\com\google\common\base\CaseFormat.java`

- Pre-analysis: classes 4, methods 20, loops 1, streams 0, synchronized blocks 0
#### 1. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: convert (line 141)
- Pattern: allocation-pressure
- What was found: Loop at line 141 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: out = new StringBuilder(s.length() + 4 * format.wordSeparator.length());
#### 2. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: convert (line 141)
- Pattern: repeated-work
- What was found: Loop at line 141 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: out = new StringBuilder(s.length() + 4 * format.wordSeparator.length());

### `guava\src\com\google\common\base\Predicates.java`

- Pre-analysis: classes 13, methods 62, loops 4, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: apply (line 425)
- Pattern: algorithmic-waste
- What was found: Loop at line 425 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 425
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: apply (line 470)
- Pattern: algorithmic-waste
- What was found: Loop at line 470 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 470

### `guava\src\com\google\common\cache\CacheBuilderSpec.java`

- Pre-analysis: classes 18, methods 24, loops 1, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: parse (line 145)
- Pattern: algorithmic-waste
- What was found: Loop at line 145 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 145
#### 2. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: parse (line 145)
- Pattern: repeated-work
- What was found: Loop at line 145 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: valueParser.parse(spec, key, value);

### `guava\src\com\google\common\collect\Multisets.java`

- Pre-analysis: classes 10, methods 1, loops 13, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Multisets (line 461)
- Pattern: algorithmic-waste
- What was found: Loop at line 461 is nested at depth 6 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 461
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Multisets (line 593)
- Pattern: algorithmic-waste
- What was found: Loop at line 593 is nested at depth 6 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 593

### `guava\src\com\google\common\collect\SparseImmutableTable.java`

- Pre-analysis: classes 1, methods 6, loops 6, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 61
- Pattern: algorithmic-waste
- What was found: Loop at line 61 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 61
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: writeReplace (line 137)
- Pattern: algorithmic-waste
- What was found: Loop at line 137 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 137

### `guava\src\com\google\common\graph\EndpointPairIterator.java`

- Pre-analysis: classes 4, methods 5, loops 3, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 125
- Pattern: algorithmic-waste
- What was found: Loop at line 125 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 125
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 131
- Pattern: algorithmic-waste
- What was found: Loop at line 131 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 131

### `guava\src\com\google\common\net\InternetDomainName.java`

- Pre-analysis: classes 6, methods 25, loops 2, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: ancestor (line 561)
- Pattern: algorithmic-waste
- What was found: Loop at line 561 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 561
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: validateSyntax (line 240)
- Pattern: algorithmic-waste
- What was found: Loop at line 240 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 240

### `guava\src\com\google\common\util\concurrent\FuturesGetChecked.java`

- Pre-analysis: classes 9, methods 11, loops 3, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: validateClass (line 160)
- Pattern: algorithmic-waste
- What was found: Loop at line 160 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 160
#### 2. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: line 270
- Pattern: data-movement-bloat
- What was found: Loop at line 270 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: params[i] = cause.toString();

### `guava\src\com\google\common\util\concurrent\Uninterruptibles.java`

- Pre-analysis: classes 4, methods 17, loops 12, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
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
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 347
- Pattern: algorithmic-waste
- What was found: Loop at line 347 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 347

### `guava-testlib\src\com\google\common\collect\testing\features\FeatureUtil.java`

- Pre-analysis: classes 8, methods 7, loops 6, streams 0, synchronized blocks 3
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: impliedFeatures (line 86)
- Pattern: algorithmic-waste
- What was found: Loop at line 86 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 86
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: impliedFeatures (line 88)
- Pattern: algorithmic-waste
- What was found: Loop at line 88 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 88

### `guava-testlib\src\com\google\common\collect\testing\google\ListMultimapRemoveTester.java`

- Pre-analysis: classes 1, methods 4, loops 3, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testRemoveAtIndexFromAsMapPropagates (line 74)
- Pattern: algorithmic-waste
- What was found: Loop at line 74 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 74
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testRemoveAtIndexFromGetPropagates (line 58)
- Pattern: algorithmic-waste
- What was found: Loop at line 58 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 58

### `guava-testlib\src\com\google\common\collect\testing\google\MultimapClearTester.java`

- Pre-analysis: classes 1, methods 12, loops 3, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testClearPropagatesToAsMapGet (line 116)
- Pattern: algorithmic-waste
- What was found: Loop at line 116 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 116
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testClearPropagatesToGet (line 105)
- Pattern: algorithmic-waste
- What was found: Loop at line 105 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 105

### `guava-testlib\src\com\google\common\collect\testing\google\MultimapContainsEntryTester.java`

- Pre-analysis: classes 1, methods 7, loops 2, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testContainsEntryAgreesWithGet (line 53)
- Pattern: algorithmic-waste
- What was found: Loop at line 53 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 53
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testContainsEntryAgreesWithGet (line 54)
- Pattern: algorithmic-waste
- What was found: Loop at line 54 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 54

### `guava-testlib\src\com\google\common\collect\testing\google\MultimapContainsKeyTester.java`

- Pre-analysis: classes 1, methods 9, loops 4, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testContainsKeyAgreesWithGet (line 56)
- Pattern: algorithmic-waste
- What was found: Loop at line 56 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 56
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testContainsKeyAgreesWithKeySet (line 68)
- Pattern: algorithmic-waste
- What was found: Loop at line 68 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 68

### `guava-testlib\src\com\google\common\collect\testing\google\MultimapPutTester.java`

- Pre-analysis: classes 1, methods 13, loops 4, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testPutPresentKeyPropagatesToAsMapGet (line 179)
- Pattern: algorithmic-waste
- What was found: Loop at line 179 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 179
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testPutPresentKeyPropagatesToGet (line 160)
- Pattern: algorithmic-waste
- What was found: Loop at line 160 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 160

### `guava-testlib\src\com\google\common\collect\testing\google\MultimapRemoveEntryTester.java`

- Pre-analysis: classes 1, methods 11, loops 4, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testRemovePropagatesToAsMap (line 139)
- Pattern: algorithmic-waste
- What was found: Loop at line 139 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 139
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testRemovePropagatesToGet (line 118)
- Pattern: algorithmic-waste
- What was found: Loop at line 118 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 118

### `guava-testlib\src\com\google\common\collect\testing\MapTestSuiteBuilder.java`

- Pre-analysis: classes 3, methods 14, loops 2, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 238
- Pattern: algorithmic-waste
- What was found: Loop at line 238 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 238
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 244
- Pattern: algorithmic-waste
- What was found: Loop at line 244 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 244

### `guava-testlib\src\com\google\common\collect\testing\MinimalSet.java`

- Pre-analysis: classes 1, methods 3, loops 2, streams 0, synchronized blocks 0
#### 1. List membership checks inside loop
- Severity: Medium
- Confidence: Medium
- Location: line 54
- Pattern: algorithmic-waste
- What was found: Loop at line 54 performs `.contains(...)` checks that may scan collections repeatedly.
- Why it is wasteful: Repeated linear scans inside iteration can push runtime toward O(n^2) as data sets grow.
- Likely impact: Throughput degradation and elevated CPU time for larger inputs.
- Recommended remediation: Use a `Set` for membership lookups or pre-index data before the loop.
- Low-waste rationale: Indexing once avoids repeated scans and reduces wasted CPU work.
- Evidence: line 54
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 54
- Pattern: algorithmic-waste
- What was found: Loop at line 54 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 54

### `guava-testlib\src\com\google\common\collect\testing\testers\ListSubListTester.java`

- Pre-analysis: classes 1, methods 28, loops 3, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testSubList_get (line 232)
- Pattern: algorithmic-waste
- What was found: Loop at line 232 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 232
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testSubList_get (line 233)
- Pattern: algorithmic-waste
- What was found: Loop at line 233 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 233

### `guava-testlib\src\com\google\common\collect\testing\testers\MapReplaceAllTester.java`

- Pre-analysis: classes 1, methods 7, loops 2, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testReplaceAllPreservesOrder (line 82)
- Pattern: algorithmic-waste
- What was found: Loop at line 82 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 82
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testReplaceAllRotate (line 64)
- Pattern: algorithmic-waste
- What was found: Loop at line 64 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 64

### `guava-testlib\src\com\google\common\testing\EqualsTester.java`

- Pre-analysis: classes 3, methods 4, loops 4, streams 0, synchronized blocks 0
#### 1. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: testItems (line 142)
- Pattern: data-movement-bloat
- What was found: Loop at line 142 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: !item.equals(item.toString()));
#### 2. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: addEqualityGroup (line 114)
- Pattern: allocation-pressure
- What was found: Loop at line 114 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw new NullPointerException("at index " + i);
#### 3. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: testItems (line 142)
- Pattern: allocation-pressure
- What was found: Loop at line 142 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: "the Object#hashCode of " + item + " must be consistent",

### `guava-testlib\src\com\google\common\testing\NullPointerTester.java`

- Pre-analysis: classes 8, methods 46, loops 14, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: containsNullable (line 538)
- Pattern: algorithmic-waste
- What was found: Loop at line 538 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 538
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

### `guava-testlib\src\com\google\common\testing\RelationshipTester.java`

- Pre-analysis: classes 3, methods 7, loops 5, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: test (line 76)
- Pattern: algorithmic-waste
- What was found: Loop at line 76 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 76
#### 2. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: test (line 78)
- Pattern: algorithmic-waste
- What was found: Loop at line 78 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 78

### `guava-tests\benchmark\com\google\common\collect\ImmutableListCreationBenchmark.java`

- Pre-analysis: classes 1, methods 4, loops 8, streams 0, synchronized blocks 0
#### 1. Allocation-heavy loop body
- Severity: Medium
- Confidence: High
- Location: copyArrayList (line 70)
- Pattern: allocation-pressure
- What was found: Loop at line 70 allocates new collections, builders, or mapping helpers during iteration.
- Why it is wasteful: Frequent temporary allocations increase GC activity and memory traffic without adding durable value.
- Likely impact: Higher heap pressure, more garbage collection, and reduced steady-state performance.
- Recommended remediation: Reuse mutable helpers where safe, pre-size collections, or move allocations outside the loop.
- Low-waste rationale: Cutting temporary objects reduces bytes allocated and the CPU spent reclaiming them.
- Evidence: List<Object> builder = new ArrayList<>();
#### 2. Repeated setup or parsing inside loop
- Severity: Medium
- Confidence: High
- Location: copyArrayList (line 70)
- Pattern: repeated-work
- What was found: Loop at line 70 recreates parsers, formatters, mappers, regexes, or other setup-heavy objects.
- Why it is wasteful: Rebuilding invariant helpers during each iteration spends CPU cycles and allocations on work that can usually be reused.
- Likely impact: Higher latency, avoidable GC churn, and lower throughput on larger collections.
- Recommended remediation: Hoist reusable helpers outside the loop and cache invariant computations.
- Low-waste rationale: Reusing expensive helpers reduces instructions executed and memory churn per item processed.
- Evidence: List<Object> builder = new ArrayList<>();

### `android\guava\src\com\google\common\base\internal\Finalizer.java`

- Pre-analysis: classes 16, methods 4, loops 2, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 90
- Pattern: concurrency-misuse
- What was found: Line 90 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: thread = new Thread((ThreadGroup) null, finalizer, threadName);

### `android\guava\src\com\google\common\base\Suppliers.java`

- Pre-analysis: classes 9, methods 1, loops 0, streams 0, synchronized blocks 6
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: Suppliers (line 403)
- Pattern: concurrency-misuse
- What was found: Line 403 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: return new ThreadSafeSupplier<>(delegate);

### `android\guava\src\com\google\common\collect\ImmutableRangeMap.java`

- Pre-analysis: classes 4, methods 24, loops 4, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: build (line 158)
- Pattern: algorithmic-waste
- What was found: Loop at line 158 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 158
#### 2. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: build (line 158)
- Pattern: allocation-pressure
- What was found: Loop at line 158 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: "Overlapping ranges: range " + prevRange + " overlaps with entry " + range);

### `android\guava\src\com\google\common\escape\Platform.java`

- Pre-analysis: classes 1, methods 1, loops 0, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: Platform (line 42)
- Pattern: concurrency-misuse
- What was found: Line 42 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: new ThreadLocal<char[]>() {

### `android\guava\src\com\google\common\graph\Traverser.java`

- Pre-analysis: classes 3, methods 19, loops 4, streams 0, synchronized blocks 0
#### 1. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: inGraph (line 370)
- Pattern: chatty-io
- What was found: Loop at line 370 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: * TODO(cpovirk): Replace these two statements with one (`N element =

### `android\guava\src\com\google\common\io\MoreFiles.java`

- Pre-analysis: classes 6, methods 1, loops 4, streams 0, synchronized blocks 0
#### 1. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: MoreFiles (line 697)
- Pattern: chatty-io
- What was found: Loop at line 697 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: exceptions = concat(exceptions, deleteRecursivelyInsecure(entry));

### `android\guava\src\com\google\common\util\concurrent\ExecutionList.java`

- Pre-analysis: classes 3, methods 1, loops 2, streams 0, synchronized blocks 3
#### 1. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: ExecutionList (line 130)
- Pattern: chatty-io
- What was found: Loop at line 130 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: executeListener(reversedList.runnable, reversedList.executor);

### `android\guava\src\com\google\common\util\concurrent\RateLimiter.java`

- Pre-analysis: classes 2, methods 21, loops 1, streams 0, synchronized blocks 5
#### 1. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: line 66
- Pattern: chatty-io
- What was found: Loop at line 66 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: *     executor.execute(task);

### `android\guava-testlib\src\com\google\common\collect\testing\FeatureSpecificTestSuiteBuilder.java`

- Pre-analysis: classes 5, methods 23, loops 5, streams 0, synchronized blocks 0
#### 1. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: formatFeatureSet (line 310)
- Pattern: data-movement-bloat
- What was found: Loop at line 310 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: temp.add(feature.toString());
#### 2. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: formatFeatureSet (line 310)
- Pattern: allocation-pressure
- What was found: Loop at line 310 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: temp.add(f.getDeclaringClass().getSimpleName() + "." + feature);

### `android\guava-testlib\src\com\google\common\collect\testing\testers\AbstractListTester.java`

- Pre-analysis: classes 2, methods 3, loops 1, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: expectContents (line 63)
- Pattern: algorithmic-waste
- What was found: Loop at line 63 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 63
#### 2. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: expectContents (line 63)
- Pattern: allocation-pressure
- What was found: Loop at line 63 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: fail("mismatch at index " + i + ": " + reportContext(expectedList));

### `android\guava-tests\benchmark\com\google\common\base\StringsRepeatBenchmark.java`

- Pre-analysis: classes 1, methods 7, loops 6, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: martinRepeat (line 102)
- Pattern: allocation-pressure
- What was found: Loop at line 102 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw new RuntimeException("Wrong length: " + x);
#### 2. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: mikeRepeat (line 69)
- Pattern: allocation-pressure
- What was found: Loop at line 69 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw new RuntimeException("Wrong length: " + x);
#### 3. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: oldRepeat (line 47)
- Pattern: allocation-pressure
- What was found: Loop at line 47 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw new RuntimeException("Wrong length: " + x);

### `guava\src\com\google\common\base\internal\Finalizer.java`

- Pre-analysis: classes 16, methods 4, loops 2, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: line 90
- Pattern: concurrency-misuse
- What was found: Line 90 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: thread = new Thread((ThreadGroup) null, finalizer, threadName);

### `guava\src\com\google\common\base\Suppliers.java`

- Pre-analysis: classes 9, methods 1, loops 0, streams 0, synchronized blocks 6
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: Suppliers (line 403)
- Pattern: concurrency-misuse
- What was found: Line 403 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: return new ThreadSafeSupplier<>(delegate);

### `guava\src\com\google\common\collect\ImmutableRangeMap.java`

- Pre-analysis: classes 4, methods 24, loops 4, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: build (line 158)
- Pattern: algorithmic-waste
- What was found: Loop at line 158 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 158
#### 2. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: build (line 158)
- Pattern: allocation-pressure
- What was found: Loop at line 158 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: "Overlapping ranges: range " + prevRange + " overlaps with entry " + range);

### `guava\src\com\google\common\collect\RegularImmutableMap.java`

- Pre-analysis: classes 8, methods 25, loops 5, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 189
- Pattern: algorithmic-waste
- What was found: Loop at line 189 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 189
#### 2. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 243
- Pattern: allocation-pressure
- What was found: Loop at line 243 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: checkNoConflict(/* safe= */ false, "key", keyBucketHead, key + "=" + newValue);

### `guava\src\com\google\common\escape\Platform.java`

- Pre-analysis: classes 1, methods 1, loops 0, streams 0, synchronized blocks 0
#### 1. Direct thread creation
- Severity: High
- Confidence: High
- Location: Platform (line 42)
- Pattern: concurrency-misuse
- What was found: Line 42 creates a thread directly.
- Why it is wasteful: Unmanaged thread creation scales poorly and can waste CPU and memory through excess context switching.
- Likely impact: Thread proliferation, unstable latency, and reduced machine efficiency under load.
- Recommended remediation: Route work through bounded executors or structured concurrency instead of raw thread creation.
- Low-waste rationale: Bounding concurrency avoids excess parallel overhead and keeps CPU use closer to useful work.
- Evidence: new ThreadLocal<char[]>() {

### `guava\src\com\google\common\graph\Traverser.java`

- Pre-analysis: classes 3, methods 19, loops 4, streams 0, synchronized blocks 0
#### 1. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: inGraph (line 370)
- Pattern: chatty-io
- What was found: Loop at line 370 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: * TODO(cpovirk): Replace these two statements with one (`N element =

### `guava\src\com\google\common\io\MoreFiles.java`

- Pre-analysis: classes 6, methods 1, loops 4, streams 0, synchronized blocks 0
#### 1. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: MoreFiles (line 694)
- Pattern: chatty-io
- What was found: Loop at line 694 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: exceptions = concat(exceptions, deleteRecursivelyInsecure(entry));

### `guava\src\com\google\common\util\concurrent\ExecutionList.java`

- Pre-analysis: classes 3, methods 1, loops 2, streams 0, synchronized blocks 3
#### 1. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: ExecutionList (line 130)
- Pattern: chatty-io
- What was found: Loop at line 130 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: executeListener(reversedList.runnable, reversedList.executor);

### `guava\src\com\google\common\util\concurrent\RateLimiter.java`

- Pre-analysis: classes 2, methods 21, loops 1, streams 0, synchronized blocks 5
#### 1. Remote or service call inside loop
- Severity: High
- Confidence: Medium
- Location: line 66
- Pattern: chatty-io
- What was found: Loop at line 66 contains calls that look like repository, client, network, or database access.
- Why it is wasteful: Repeated external calls inside iteration amplify latency and often create N+1 style traffic.
- Likely impact: Slower batch processing, more round trips, and higher infrastructure cost.
- Recommended remediation: Batch external calls, prefetch data before iterating, or aggregate writes after the loop.
- Low-waste rationale: Fewer round trips and fewer bytes moved per useful action reduce time and energy spent waiting on I/O.
- Evidence: *     executor.execute(task);

### `guava-testlib\src\com\google\common\collect\testing\FeatureSpecificTestSuiteBuilder.java`

- Pre-analysis: classes 5, methods 23, loops 5, streams 0, synchronized blocks 0
#### 1. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: formatFeatureSet (line 310)
- Pattern: data-movement-bloat
- What was found: Loop at line 310 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: temp.add(feature.toString());
#### 2. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: formatFeatureSet (line 310)
- Pattern: allocation-pressure
- What was found: Loop at line 310 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: temp.add(f.getDeclaringClass().getSimpleName() + "." + feature);

### `guava-testlib\src\com\google\common\collect\testing\testers\AbstractListTester.java`

- Pre-analysis: classes 2, methods 3, loops 1, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: expectContents (line 63)
- Pattern: algorithmic-waste
- What was found: Loop at line 63 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 63
#### 2. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: expectContents (line 63)
- Pattern: allocation-pressure
- What was found: Loop at line 63 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: fail("mismatch at index " + i + ": " + reportContext(expectedList));

### `guava-tests\benchmark\com\google\common\base\StringsRepeatBenchmark.java`

- Pre-analysis: classes 1, methods 7, loops 6, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: martinRepeat (line 102)
- Pattern: allocation-pressure
- What was found: Loop at line 102 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw new RuntimeException("Wrong length: " + x);
#### 2. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: mikeRepeat (line 69)
- Pattern: allocation-pressure
- What was found: Loop at line 69 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw new RuntimeException("Wrong length: " + x);
#### 3. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: oldRepeat (line 47)
- Pattern: allocation-pressure
- What was found: Loop at line 47 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw new RuntimeException("Wrong length: " + x);

### `android\guava\src\com\google\common\base\Optional.java`

- Pre-analysis: classes 11, methods 3, loops 2, streams 3, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 356
- Pattern: algorithmic-waste
- What was found: Loop at line 356 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 356

### `android\guava\src\com\google\common\base\Splitter.java`

- Pre-analysis: classes 5, methods 23, loops 8, streams 1, synchronized blocks 0
#### 1. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: line 556
- Pattern: data-movement-bloat
- What was found: Loop at line 556 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: return toSplit.subSequence(start, end).toString();

### `android\guava\src\com\google\common\base\Strings.java`

- Pre-analysis: classes 2, methods 1, loops 7, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Strings (line 272)
- Pattern: algorithmic-waste
- What was found: Loop at line 272 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 272

### `android\guava\src\com\google\common\collect\AbstractMultimap.java`

- Pre-analysis: classes 4, methods 25, loops 2, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: containsValue (line 48)
- Pattern: algorithmic-waste
- What was found: Loop at line 48 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 48

### `android\guava\src\com\google\common\collect\DenseImmutableTable.java`

- Pre-analysis: classes 6, methods 31, loops 2, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 68
- Pattern: algorithmic-waste
- What was found: Loop at line 68 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 68

### `android\guava\src\com\google\common\collect\ImmutableMap.java`

- Pre-analysis: classes 7, methods 56, loops 8, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 685
- Pattern: algorithmic-waste
- What was found: Loop at line 685 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 685

### `android\guava\src\com\google\common\collect\ImmutableRangeSet.java`

- Pre-analysis: classes 6, methods 58, loops 7, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: indexOf (line 700)
- Pattern: algorithmic-waste
- What was found: Loop at line 700 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 700

### `android\guava\src\com\google\common\collect\Range.java`

- Pre-analysis: classes 4, methods 41, loops 2, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: containsAll (line 442)
- Pattern: algorithmic-waste
- What was found: Loop at line 442 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 442

### `android\guava\src\com\google\common\collect\Serialization.java`

- Pre-analysis: classes 3, methods 1, loops 8, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Serialization (line 163)
- Pattern: algorithmic-waste
- What was found: Loop at line 163 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 163

### `android\guava\src\com\google\common\collect\Streams.java`

- Pre-analysis: classes 17, methods 40, loops 8, streams 12, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 900
- Pattern: algorithmic-waste
- What was found: Loop at line 900 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 900

### `android\guava\src\com\google\common\escape\ArrayBasedEscaperMap.java`

- Pre-analysis: classes 3, methods 4, loops 1, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: createReplacementArray (line 74)
- Pattern: algorithmic-waste
- What was found: Loop at line 74 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 74

### `android\guava\src\com\google\common\hash\AbstractByteHasher.java`

- Pre-analysis: classes 1, methods 13, loops 2, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: update (line 59)
- Pattern: algorithmic-waste
- What was found: Loop at line 59 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 59

### `android\guava\src\com\google\common\hash\AbstractHasher.java`

- Pre-analysis: classes 1, methods 12, loops 4, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: putBytes (line 86)
- Pattern: algorithmic-waste
- What was found: Loop at line 86 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 86

### `android\guava\src\com\google\common\hash\AbstractStreamingHasher.java`

- Pre-analysis: classes 3, methods 14, loops 4, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: putBytesInternal (line 121)
- Pattern: algorithmic-waste
- What was found: Loop at line 121 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 121

### `android\guava\src\com\google\common\hash\Crc32cHashFunction.java`

- Pre-analysis: classes 3, methods 9, loops 3, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: processRemaining (line 108)
- Pattern: algorithmic-waste
- What was found: Loop at line 108 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 108

### `android\guava\src\com\google\common\hash\LittleEndianByteArray.java`

- Pre-analysis: classes 6, methods 16, loops 3, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: getUnsafe (line 198)
- Pattern: algorithmic-waste
- What was found: Loop at line 198 is nested at depth 5 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 198

### `android\guava\src\com\google\common\hash\SipHashFunction.java`

- Pre-analysis: classes 2, methods 11, loops 2, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: processRemaining (line 140)
- Pattern: algorithmic-waste
- What was found: Loop at line 140 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 140

### `android\guava\src\com\google\common\io\ByteSource.java`

- Pre-analysis: classes 7, methods 1, loops 4, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: ByteSource (line 707)
- Pattern: algorithmic-waste
- What was found: Loop at line 707 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 707

### `android\guava\src\com\google\common\io\CharSource.java`

- Pre-analysis: classes 6, methods 1, loops 6, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: CharSource (line 722)
- Pattern: algorithmic-waste
- What was found: Loop at line 722 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 722

### `android\guava\src\com\google\common\io\Files.java`

- Pre-analysis: classes 4, methods 1, loops 2, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Files (line 744)
- Pattern: algorithmic-waste
- What was found: Loop at line 744 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 744

### `android\guava\src\com\google\common\primitives\ImmutableDoubleArray.java`

- Pre-analysis: classes 3, methods 54, loops 9, streams 1, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: equals (line 593)
- Pattern: algorithmic-waste
- What was found: Loop at line 593 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 593

### `android\guava\src\com\google\common\primitives\ImmutableIntArray.java`

- Pre-analysis: classes 3, methods 54, loops 9, streams 1, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: equals (line 588)
- Pattern: algorithmic-waste
- What was found: Loop at line 588 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 588

### `android\guava\src\com\google\common\primitives\ImmutableLongArray.java`

- Pre-analysis: classes 3, methods 54, loops 9, streams 1, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: equals (line 590)
- Pattern: algorithmic-waste
- What was found: Loop at line 590 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 590

### `android\guava\src\com\google\common\primitives\UnsignedBytes.java`

- Pre-analysis: classes 8, methods 1, loops 12, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: UnsignedBytes (line 383)
- Pattern: algorithmic-waste
- What was found: Loop at line 383 is nested at depth 6 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 383

### `android\guava\src\com\google\common\reflect\ClassPath.java`

- Pre-analysis: classes 38, methods 36, loops 11, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: getClassPathFromManifest (line 586)
- Pattern: allocation-pressure
- What was found: Loop at line 586 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: logger.warning("Invalid Class-Path entry: " + path);
#### 2. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: parseJavaClassPath (line 639)
- Pattern: allocation-pressure
- What was found: Loop at line 639 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: logger.log(WARNING, "malformed classpath entry: " + entry, e);

### `android\guava\src\com\google\common\reflect\TypeResolver.java`

- Pre-analysis: classes 10, methods 37, loops 10, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: map (line 445)
- Pattern: algorithmic-waste
- What was found: Loop at line 445 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 445

### `android\guava\src\com\google\common\util\concurrent\AbstractExecutionThreadService.java`

- Pre-analysis: classes 3, methods 2, loops 1, streams 0, synchronized blocks 0
#### 1. Executor created in application code path
- Severity: Medium
- Confidence: High
- Location: line 17
- Pattern: concurrency-misuse
- What was found: Line 17 creates a new executor instance.
- Why it is wasteful: Creating executors per call can fragment thread pools and increase context switching and idle threads.
- Likely impact: Higher memory use, poorer scheduling efficiency, and harder concurrency control.
- Recommended remediation: Reuse a bounded shared executor sized to the workload.
- Low-waste rationale: Bounded executor reuse reduces idle threads and CPU overhead without reducing useful throughput.
- Evidence: import static com.google.common.util.concurrent.MoreExecutors.newThread;

### `android\guava\src\com\google\common\util\concurrent\AbstractFutureState.java`

- Pre-analysis: classes 13, methods 26, loops 12, streams 0, synchronized blocks 7
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 598
- Pattern: algorithmic-waste
- What was found: Loop at line 598 is nested at depth 6 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 598

### `android\guava\src\com\google\common\util\concurrent\Futures.java`

- Pre-analysis: classes 7, methods 1, loops 4, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Futures (line 1024)
- Pattern: algorithmic-waste
- What was found: Loop at line 1024 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1024

### `android\guava\src\com\google\thirdparty\publicsuffix\PublicSuffixTrie.java`

- Pre-analysis: classes 2, methods 10, loops 5, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: findSuffixIndex (line 118)
- Pattern: algorithmic-waste
- What was found: Loop at line 118 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 118

### `android\guava-testlib\src\com\google\common\collect\testing\DerivedCollectionGenerators.java`

- Pre-analysis: classes 10, methods 50, loops 7, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: order (line 267)
- Pattern: algorithmic-waste
- What was found: Loop at line 267 is nested at depth 5 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 267

### `android\guava-testlib\src\com\google\common\collect\testing\google\ListMultimapAsMapTester.java`

- Pre-analysis: classes 1, methods 6, loops 3, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testAsMapGetImplementsList (line 61)
- Pattern: algorithmic-waste
- What was found: Loop at line 61 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 61

### `android\guava-testlib\src\com\google\common\collect\testing\google\ListMultimapPutAllTester.java`

- Pre-analysis: classes 1, methods 1, loops 1, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testPutAllAddsAtEndInOrder (line 41)
- Pattern: algorithmic-waste
- What was found: Loop at line 41 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 41

### `android\guava-testlib\src\com\google\common\collect\testing\google\MultimapKeySetTester.java`

- Pre-analysis: classes 1, methods 5, loops 2, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testKeySet (line 43)
- Pattern: algorithmic-waste
- What was found: Loop at line 43 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 43

### `android\guava-testlib\src\com\google\common\collect\testing\google\MultimapReplaceValuesTester.java`

- Pre-analysis: classes 1, methods 9, loops 1, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testReplaceNonEmptyValues (line 102)
- Pattern: algorithmic-waste
- What was found: Loop at line 102 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 102

### `android\guava-testlib\src\com\google\common\collect\testing\google\SetGenerators.java`

- Pre-analysis: classes 31, methods 35, loops 6, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: checkedCreate (line 421)
- Pattern: algorithmic-waste
- What was found: Loop at line 421 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 421

### `android\guava-testlib\src\com\google\common\collect\testing\google\SetMultimapAsMapTester.java`

- Pre-analysis: classes 1, methods 6, loops 3, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testAsMapGetImplementsSet (line 62)
- Pattern: algorithmic-waste
- What was found: Loop at line 62 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 62

### `android\guava-testlib\src\com\google\common\collect\testing\google\SetMultimapPutAllTester.java`

- Pre-analysis: classes 1, methods 1, loops 1, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testPutAllHandlesDuplicates (line 43)
- Pattern: algorithmic-waste
- What was found: Loop at line 43 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 43

### `android\guava-testlib\src\com\google\common\collect\testing\google\SetMultimapPutTester.java`

- Pre-analysis: classes 1, methods 3, loops 1, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testPutDuplicateValue (line 55)
- Pattern: algorithmic-waste
- What was found: Loop at line 55 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 55

### `android\guava-testlib\src\com\google\common\collect\testing\google\SortedSetMultimapAsMapTester.java`

- Pre-analysis: classes 1, methods 3, loops 3, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testAsMapGetImplementsSortedSet (line 49)
- Pattern: algorithmic-waste
- What was found: Loop at line 49 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 49

### `android\guava-testlib\src\com\google\common\collect\testing\PerCollectionSizeTestSuiteBuilder.java`

- Pre-analysis: classes 7, methods 3, loops 2, streams 0, synchronized blocks 0
#### 1. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: createTestSuite (line 87)
- Pattern: data-movement-bloat
- What was found: Loop at line 87 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: "%s [collection size: %s]", name, collectionSize.toString().toLowerCase());

### `android\guava-testlib\src\com\google\common\testing\DummyProxy.java`

- Pre-analysis: classes 5, methods 7, loops 3, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 97
- Pattern: algorithmic-waste
- What was found: Loop at line 97 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 97

### `android\guava-testlib\src\com\google\common\util\concurrent\testing\SameThreadScheduledExecutorService.java`

- Pre-analysis: classes 2, methods 12, loops 0, streams 0, synchronized blocks 0
#### 1. Executor created in application code path
- Severity: Medium
- Confidence: High
- Location: line 19
- Pattern: concurrency-misuse
- What was found: Line 19 creates a new executor instance.
- Why it is wasteful: Creating executors per call can fragment thread pools and increase context switching and idle threads.
- Likely impact: Higher memory use, poorer scheduling efficiency, and harder concurrency control.
- Recommended remediation: Reuse a bounded shared executor sized to the workload.
- Low-waste rationale: Bounded executor reuse reduces idle threads and CPU overhead without reducing useful throughput.
- Evidence: import static com.google.common.util.concurrent.MoreExecutors.newDirectExecutorService;

### `android\guava-tests\benchmark\com\google\common\base\CharMatcherBenchmark.java`

- Pre-analysis: classes 3, methods 10, loops 6, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 139
- Pattern: algorithmic-waste
- What was found: Loop at line 139 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 139

### `android\guava-tests\benchmark\com\google\common\base\ToStringHelperBenchmark.java`

- Pre-analysis: classes 2, methods 5, loops 2, streams 0, synchronized blocks 0
#### 1. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: toString (line 135)
- Pattern: data-movement-bloat
- What was found: Loop at line 135 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: dummy ^= helper.toString().hashCode();

### `android\guava-tests\benchmark\com\google\common\base\WhitespaceMatcherBenchmark.java`

- Pre-analysis: classes 1, methods 6, loops 6, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: newTestString (line 107)
- Pattern: algorithmic-waste
- What was found: Loop at line 107 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 107

### `android\guava-tests\benchmark\com\google\common\cache\MapMakerComparisonBenchmark.java`

- Pre-analysis: classes 1, methods 4, loops 3, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: concurrentHashMap (line 49)
- Pattern: algorithmic-waste
- What was found: Loop at line 49 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 49

### `android\guava-tests\benchmark\com\google\common\collect\HashMultisetAddPresentBenchmark.java`

- Pre-analysis: classes 1, methods 2, loops 2, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: add (line 51)
- Pattern: algorithmic-waste
- What was found: Loop at line 51 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 51

### `android\guava-tests\benchmark\com\google\common\collect\MultipleSetContainsBenchmark.java`

- Pre-analysis: classes 1, methods 2, loops 2, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: contains (line 76)
- Pattern: algorithmic-waste
- What was found: Loop at line 76 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 76

### `android\guava-tests\benchmark\com\google\common\collect\SetContainsBenchmark.java`

- Pre-analysis: classes 1, methods 2, loops 1, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: contains (line 76)
- Pattern: algorithmic-waste
- What was found: Loop at line 76 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 76

### `android\guava-tests\benchmark\com\google\common\io\CharStreamsCopyBenchmark.java`

- Pre-analysis: classes 3, methods 3, loops 3, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 108
- Pattern: algorithmic-waste
- What was found: Loop at line 108 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 108

### `android\guava-tests\benchmark\com\google\common\util\concurrent\FuturesGetCheckedBenchmark.java`

- Pre-analysis: classes 6, methods 9, loops 3, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 128
- Pattern: algorithmic-waste
- What was found: Loop at line 128 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 128

### `android\guava-tests\benchmark\com\google\common\util\concurrent\StripedBenchmark.java`

- Pre-analysis: classes 2, methods 10, loops 5, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: timeConstruct (line 119)
- Pattern: algorithmic-waste
- What was found: Loop at line 119 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 119

### `guava\src\com\google\common\base\Optional.java`

- Pre-analysis: classes 11, methods 3, loops 2, streams 3, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 351
- Pattern: algorithmic-waste
- What was found: Loop at line 351 is nested at depth 4 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 351

### `guava\src\com\google\common\base\Splitter.java`

- Pre-analysis: classes 5, methods 23, loops 8, streams 1, synchronized blocks 0
#### 1. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: line 554
- Pattern: data-movement-bloat
- What was found: Loop at line 554 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: return toSplit.subSequence(start, end).toString();

### `guava\src\com\google\common\base\Strings.java`

- Pre-analysis: classes 2, methods 1, loops 7, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Strings (line 278)
- Pattern: algorithmic-waste
- What was found: Loop at line 278 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 278

### `guava\src\com\google\common\collect\AbstractMultimap.java`

- Pre-analysis: classes 4, methods 29, loops 2, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: containsValue (line 50)
- Pattern: algorithmic-waste
- What was found: Loop at line 50 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 50

### `guava\src\com\google\common\collect\DenseImmutableTable.java`

- Pre-analysis: classes 6, methods 31, loops 2, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 68
- Pattern: algorithmic-waste
- What was found: Loop at line 68 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 68

### `guava\src\com\google\common\collect\ImmutableMap.java`

- Pre-analysis: classes 6, methods 61, loops 7, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 666
- Pattern: algorithmic-waste
- What was found: Loop at line 666 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 666

### `guava\src\com\google\common\collect\ImmutableRangeSet.java`

- Pre-analysis: classes 6, methods 58, loops 7, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: indexOf (line 699)
- Pattern: algorithmic-waste
- What was found: Loop at line 699 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 699

### `guava\src\com\google\common\collect\ImmutableSortedMap.java`

- Pre-analysis: classes 6, methods 47, loops 3, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: forEach (line 820)
- Pattern: algorithmic-waste
- What was found: Loop at line 820 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 820

### `guava\src\com\google\common\collect\Range.java`

- Pre-analysis: classes 4, methods 42, loops 2, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: containsAll (line 454)
- Pattern: algorithmic-waste
- What was found: Loop at line 454 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 454

### `guava\src\com\google\common\collect\RegularImmutableSortedMultiset.java`

- Pre-analysis: classes 1, methods 11, loops 1, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: forEachEntry (line 74)
- Pattern: algorithmic-waste
- What was found: Loop at line 74 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 74

### `guava\src\com\google\common\collect\Serialization.java`

- Pre-analysis: classes 3, methods 1, loops 8, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Serialization (line 163)
- Pattern: algorithmic-waste
- What was found: Loop at line 163 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 163

### `guava\src\com\google\common\collect\Streams.java`

- Pre-analysis: classes 16, methods 40, loops 8, streams 12, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 888
- Pattern: algorithmic-waste
- What was found: Loop at line 888 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 888

### `guava\src\com\google\common\escape\ArrayBasedEscaperMap.java`

- Pre-analysis: classes 3, methods 4, loops 1, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: createReplacementArray (line 74)
- Pattern: algorithmic-waste
- What was found: Loop at line 74 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 74

### `guava\src\com\google\common\hash\AbstractByteHasher.java`

- Pre-analysis: classes 1, methods 13, loops 2, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: update (line 59)
- Pattern: algorithmic-waste
- What was found: Loop at line 59 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 59

### `guava\src\com\google\common\hash\AbstractHasher.java`

- Pre-analysis: classes 1, methods 12, loops 4, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: putBytes (line 86)
- Pattern: algorithmic-waste
- What was found: Loop at line 86 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 86

### `guava\src\com\google\common\hash\AbstractStreamingHasher.java`

- Pre-analysis: classes 3, methods 14, loops 4, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: putBytesInternal (line 121)
- Pattern: algorithmic-waste
- What was found: Loop at line 121 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 121

### `guava\src\com\google\common\hash\Crc32cHashFunction.java`

- Pre-analysis: classes 3, methods 9, loops 3, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: processRemaining (line 108)
- Pattern: algorithmic-waste
- What was found: Loop at line 108 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 108

### `guava\src\com\google\common\hash\LittleEndianByteArray.java`

- Pre-analysis: classes 9, methods 19, loops 3, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: getUnsafe (line 233)
- Pattern: algorithmic-waste
- What was found: Loop at line 233 is nested at depth 5 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 233

### `guava\src\com\google\common\hash\SipHashFunction.java`

- Pre-analysis: classes 2, methods 11, loops 2, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: processRemaining (line 140)
- Pattern: algorithmic-waste
- What was found: Loop at line 140 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 140

### `guava\src\com\google\common\io\ByteSource.java`

- Pre-analysis: classes 7, methods 1, loops 4, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: ByteSource (line 707)
- Pattern: algorithmic-waste
- What was found: Loop at line 707 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 707

### `guava\src\com\google\common\io\CharSource.java`

- Pre-analysis: classes 6, methods 1, loops 6, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: CharSource (line 713)
- Pattern: algorithmic-waste
- What was found: Loop at line 713 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 713

### `guava\src\com\google\common\io\Files.java`

- Pre-analysis: classes 4, methods 1, loops 2, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Files (line 744)
- Pattern: algorithmic-waste
- What was found: Loop at line 744 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 744

### `guava\src\com\google\common\primitives\ImmutableDoubleArray.java`

- Pre-analysis: classes 3, methods 54, loops 9, streams 1, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: equals (line 588)
- Pattern: algorithmic-waste
- What was found: Loop at line 588 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 588

### `guava\src\com\google\common\primitives\ImmutableIntArray.java`

- Pre-analysis: classes 3, methods 54, loops 9, streams 1, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: equals (line 583)
- Pattern: algorithmic-waste
- What was found: Loop at line 583 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 583

### `guava\src\com\google\common\primitives\ImmutableLongArray.java`

- Pre-analysis: classes 3, methods 54, loops 9, streams 1, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: equals (line 585)
- Pattern: algorithmic-waste
- What was found: Loop at line 585 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 585

### `guava\src\com\google\common\primitives\UnsignedBytes.java`

- Pre-analysis: classes 11, methods 1, loops 12, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: UnsignedBytes (line 384)
- Pattern: algorithmic-waste
- What was found: Loop at line 384 is nested at depth 6 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 384

### `guava\src\com\google\common\reflect\ClassPath.java`

- Pre-analysis: classes 38, methods 36, loops 11, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: getClassPathFromManifest (line 586)
- Pattern: allocation-pressure
- What was found: Loop at line 586 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: logger.warning("Invalid Class-Path entry: " + path);
#### 2. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: parseJavaClassPath (line 639)
- Pattern: allocation-pressure
- What was found: Loop at line 639 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: logger.log(WARNING, "malformed classpath entry: " + entry, e);

### `guava\src\com\google\common\reflect\TypeResolver.java`

- Pre-analysis: classes 10, methods 37, loops 10, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: map (line 445)
- Pattern: algorithmic-waste
- What was found: Loop at line 445 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 445

### `guava\src\com\google\common\util\concurrent\AbstractExecutionThreadService.java`

- Pre-analysis: classes 3, methods 2, loops 1, streams 0, synchronized blocks 0
#### 1. Executor created in application code path
- Severity: Medium
- Confidence: High
- Location: line 17
- Pattern: concurrency-misuse
- What was found: Line 17 creates a new executor instance.
- Why it is wasteful: Creating executors per call can fragment thread pools and increase context switching and idle threads.
- Likely impact: Higher memory use, poorer scheduling efficiency, and harder concurrency control.
- Recommended remediation: Reuse a bounded shared executor sized to the workload.
- Low-waste rationale: Bounded executor reuse reduces idle threads and CPU overhead without reducing useful throughput.
- Evidence: import static com.google.common.util.concurrent.MoreExecutors.newThread;

### `guava\src\com\google\common\util\concurrent\AbstractFutureState.java`

- Pre-analysis: classes 17, methods 30, loops 10, streams 0, synchronized blocks 7
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 678
- Pattern: algorithmic-waste
- What was found: Loop at line 678 is nested at depth 6 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 678

### `guava\src\com\google\common\util\concurrent\Futures.java`

- Pre-analysis: classes 7, methods 1, loops 4, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: Futures (line 1022)
- Pattern: algorithmic-waste
- What was found: Loop at line 1022 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 1022

### `guava\src\com\google\thirdparty\publicsuffix\PublicSuffixTrie.java`

- Pre-analysis: classes 2, methods 10, loops 5, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: findSuffixIndex (line 118)
- Pattern: algorithmic-waste
- What was found: Loop at line 118 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 118

### `guava-gwt\test-super\com\google\common\collect\testing\super\com\google\common\collect\testing\Platform.java`

- Pre-analysis: classes 1, methods 1, loops 2, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: checkCast (line 42)
- Pattern: algorithmic-waste
- What was found: Loop at line 42 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 42

### `guava-gwt\test-super\com\google\common\collect\testing\super\com\google\common\collect\testing\testers\Platform.java`

- Pre-analysis: classes 1, methods 4, loops 2, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: format (line 48)
- Pattern: algorithmic-waste
- What was found: Loop at line 48 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 48

### `guava-testlib\src\com\google\common\collect\testing\DerivedCollectionGenerators.java`

- Pre-analysis: classes 10, methods 50, loops 7, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: order (line 267)
- Pattern: algorithmic-waste
- What was found: Loop at line 267 is nested at depth 5 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 267

### `guava-testlib\src\com\google\common\collect\testing\google\ListMultimapAsMapTester.java`

- Pre-analysis: classes 1, methods 6, loops 3, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testAsMapGetImplementsList (line 61)
- Pattern: algorithmic-waste
- What was found: Loop at line 61 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 61

### `guava-testlib\src\com\google\common\collect\testing\google\ListMultimapPutAllTester.java`

- Pre-analysis: classes 1, methods 1, loops 1, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testPutAllAddsAtEndInOrder (line 41)
- Pattern: algorithmic-waste
- What was found: Loop at line 41 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 41

### `guava-testlib\src\com\google\common\collect\testing\google\MultimapKeySetTester.java`

- Pre-analysis: classes 1, methods 5, loops 2, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testKeySet (line 43)
- Pattern: algorithmic-waste
- What was found: Loop at line 43 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 43

### `guava-testlib\src\com\google\common\collect\testing\google\MultimapReplaceValuesTester.java`

- Pre-analysis: classes 1, methods 9, loops 1, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testReplaceNonEmptyValues (line 102)
- Pattern: algorithmic-waste
- What was found: Loop at line 102 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 102

### `guava-testlib\src\com\google\common\collect\testing\google\SetGenerators.java`

- Pre-analysis: classes 31, methods 35, loops 6, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: checkedCreate (line 421)
- Pattern: algorithmic-waste
- What was found: Loop at line 421 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 421

### `guava-testlib\src\com\google\common\collect\testing\google\SetMultimapAsMapTester.java`

- Pre-analysis: classes 1, methods 6, loops 3, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testAsMapGetImplementsSet (line 62)
- Pattern: algorithmic-waste
- What was found: Loop at line 62 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 62

### `guava-testlib\src\com\google\common\collect\testing\google\SetMultimapPutAllTester.java`

- Pre-analysis: classes 1, methods 1, loops 1, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testPutAllHandlesDuplicates (line 43)
- Pattern: algorithmic-waste
- What was found: Loop at line 43 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 43

### `guava-testlib\src\com\google\common\collect\testing\google\SetMultimapPutTester.java`

- Pre-analysis: classes 1, methods 3, loops 1, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testPutDuplicateValue (line 55)
- Pattern: algorithmic-waste
- What was found: Loop at line 55 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 55

### `guava-testlib\src\com\google\common\collect\testing\google\SortedSetMultimapAsMapTester.java`

- Pre-analysis: classes 1, methods 3, loops 3, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: testAsMapGetImplementsSortedSet (line 49)
- Pattern: algorithmic-waste
- What was found: Loop at line 49 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 49

### `guava-testlib\src\com\google\common\collect\testing\PerCollectionSizeTestSuiteBuilder.java`

- Pre-analysis: classes 7, methods 3, loops 2, streams 0, synchronized blocks 0
#### 1. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: createTestSuite (line 87)
- Pattern: data-movement-bloat
- What was found: Loop at line 87 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: "%s [collection size: %s]", name, collectionSize.toString().toLowerCase());

### `guava-testlib\src\com\google\common\testing\DummyProxy.java`

- Pre-analysis: classes 5, methods 7, loops 3, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 97
- Pattern: algorithmic-waste
- What was found: Loop at line 97 is nested at depth 3 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 97

### `guava-testlib\src\com\google\common\util\concurrent\testing\SameThreadScheduledExecutorService.java`

- Pre-analysis: classes 2, methods 12, loops 0, streams 0, synchronized blocks 0
#### 1. Executor created in application code path
- Severity: Medium
- Confidence: High
- Location: line 19
- Pattern: concurrency-misuse
- What was found: Line 19 creates a new executor instance.
- Why it is wasteful: Creating executors per call can fragment thread pools and increase context switching and idle threads.
- Likely impact: Higher memory use, poorer scheduling efficiency, and harder concurrency control.
- Recommended remediation: Reuse a bounded shared executor sized to the workload.
- Low-waste rationale: Bounded executor reuse reduces idle threads and CPU overhead without reducing useful throughput.
- Evidence: import static com.google.common.util.concurrent.MoreExecutors.newDirectExecutorService;

### `guava-tests\benchmark\com\google\common\base\CharMatcherBenchmark.java`

- Pre-analysis: classes 3, methods 10, loops 6, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 139
- Pattern: algorithmic-waste
- What was found: Loop at line 139 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 139

### `guava-tests\benchmark\com\google\common\base\ToStringHelperBenchmark.java`

- Pre-analysis: classes 2, methods 5, loops 2, streams 0, synchronized blocks 0
#### 1. Payload construction inside loop
- Severity: Medium
- Confidence: Medium
- Location: toString (line 135)
- Pattern: data-movement-bloat
- What was found: Loop at line 135 serializes, materializes, or expands payload-like objects during iteration.
- Why it is wasteful: Building full payloads before filtering or aggregating moves more bytes and allocates more intermediate state than needed.
- Likely impact: Higher memory use, longer serialization time, and avoidable network or logging overhead.
- Recommended remediation: Filter earlier, narrow the fields being built, or batch serialization closer to the sink.
- Low-waste rationale: Constructing only the bytes that are actually needed reduces memory traffic and output overhead.
- Evidence: dummy ^= helper.toString().hashCode();

### `guava-tests\benchmark\com\google\common\base\WhitespaceMatcherBenchmark.java`

- Pre-analysis: classes 1, methods 6, loops 6, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: newTestString (line 107)
- Pattern: algorithmic-waste
- What was found: Loop at line 107 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 107

### `guava-tests\benchmark\com\google\common\cache\MapMakerComparisonBenchmark.java`

- Pre-analysis: classes 1, methods 4, loops 3, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: concurrentHashMap (line 50)
- Pattern: algorithmic-waste
- What was found: Loop at line 50 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 50

### `guava-tests\benchmark\com\google\common\collect\HashMultisetAddPresentBenchmark.java`

- Pre-analysis: classes 1, methods 2, loops 2, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: add (line 51)
- Pattern: algorithmic-waste
- What was found: Loop at line 51 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 51

### `guava-tests\benchmark\com\google\common\collect\MultipleSetContainsBenchmark.java`

- Pre-analysis: classes 1, methods 2, loops 2, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: contains (line 76)
- Pattern: algorithmic-waste
- What was found: Loop at line 76 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 76

### `guava-tests\benchmark\com\google\common\collect\SetContainsBenchmark.java`

- Pre-analysis: classes 1, methods 2, loops 1, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: contains (line 76)
- Pattern: algorithmic-waste
- What was found: Loop at line 76 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 76

### `guava-tests\benchmark\com\google\common\collect\StreamsBenchmark.java`

- Pre-analysis: classes 3, methods 8, loops 2, streams 1, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: runOperation (line 112)
- Pattern: algorithmic-waste
- What was found: Loop at line 112 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 112

### `guava-tests\benchmark\com\google\common\io\CharStreamsCopyBenchmark.java`

- Pre-analysis: classes 3, methods 3, loops 3, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 108
- Pattern: algorithmic-waste
- What was found: Loop at line 108 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 108

### `guava-tests\benchmark\com\google\common\util\concurrent\FuturesGetCheckedBenchmark.java`

- Pre-analysis: classes 6, methods 9, loops 3, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: line 130
- Pattern: algorithmic-waste
- What was found: Loop at line 130 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 130

### `guava-tests\benchmark\com\google\common\util\concurrent\StripedBenchmark.java`

- Pre-analysis: classes 2, methods 10, loops 5, streams 0, synchronized blocks 0
#### 1. Nested loop with repeated lookup work
- Severity: Medium
- Confidence: Medium
- Location: timeConstruct (line 119)
- Pattern: algorithmic-waste
- What was found: Loop at line 119 is nested at depth 2 and also performs repeated lookup or transformation work.
- Why it is wasteful: Nested iteration plus repeated lookup operations multiplies work and can become expensive quickly as data grows.
- Likely impact: Poor scalability, longer batch runtimes, and excess CPU consumption.
- Recommended remediation: Pre-index shared data, reduce nested scans, or collapse passes where possible.
- Low-waste rationale: Lowering algorithmic complexity reduces operations and energy for the same user-visible result.
- Evidence: line 119

### `android\guava\src\com\google\common\collect\DiscreteDomain.java`

- Pre-analysis: classes 4, methods 29, loops 1, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: offset (line 266)
- Pattern: allocation-pressure
- What was found: Loop at line 266 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: "overflowed computing offset(" + origin + ", " + distance + ")");

### `android\guava\src\com\google\common\collect\ImmutableListMultimap.java`

- Pre-analysis: classes 2, methods 13, loops 5, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 540
- Pattern: allocation-pressure
- What was found: Loop at line 540 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw new InvalidObjectException("Invalid value count " + valueCount);

### `android\guava\src\com\google\common\collect\ImmutableSetMultimap.java`

- Pre-analysis: classes 3, methods 21, loops 6, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 709
- Pattern: allocation-pressure
- What was found: Loop at line 709 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw new InvalidObjectException("Invalid value count " + valueCount); | throw new InvalidObjectException("Duplicate key-value pairs exist for key " + key);

### `android\guava\src\com\google\common\collect\Multimap.java`

- Pre-analysis: classes 3, methods 0, loops 3, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 64
- Pattern: allocation-pressure
- What was found: Loop at line 64 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: *   out.println(firstName + ": " + lastNames);

### `android\guava\src\com\google\common\primitives\UnsignedLongs.java`

- Pre-analysis: classes 5, methods 1, loops 12, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: UnsignedLongs (line 351)
- Pattern: allocation-pressure
- What was found: Loop at line 351 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw new NumberFormatException("Too large for unsigned long: " + string);

### `android\guava\src\com\google\common\reflect\TypeVisitor.java`

- Pre-analysis: classes 2, methods 2, loops 1, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: visit (line 66)
- Pattern: allocation-pressure
- What was found: Loop at line 66 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw new AssertionError("Unknown type: " + type);

### `android\guava-testlib\src\com\google\common\testing\EquivalenceTester.java`

- Pre-analysis: classes 2, methods 6, loops 2, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: testItems (line 102)
- Pattern: allocation-pressure
- What was found: Loop at line 102 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertTrue("null must be inequivalent to " + item, !equivalence.equivalent(null, item)); | "the hash of " + item + " must be consistent",

### `android\guava-testlib\src\com\google\common\testing\ForwardingWrapperTester.java`

- Pre-analysis: classes 3, methods 6, loops 4, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 211
- Pattern: allocation-pressure
- What was found: Loop at line 211 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: "Parameter #" + i + " of " + method + " not forwarded", passedArgs[i], args[i]);

### `android\guava-tests\benchmark\com\google\common\primitives\UnsignedLongsBenchmark.java`

- Pre-analysis: classes 1, methods 9, loops 7, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: setUp (line 43)
- Pattern: allocation-pressure
- What was found: Loop at line 43 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: prefixedHexStrings[i] = "0x" + hexStrings[i];

### `android\guava-tests\benchmark\com\google\common\util\concurrent\CycleDetectingLockFactoryBenchmark.java`

- Pre-analysis: classes 1, methods 6, loops 6, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 49
- Pattern: allocation-pressure
- What was found: Loop at line 49 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: detectingLocks[i] = factory.newReentrantLock("Lock" + i);

### `guava\src\com\google\common\collect\DiscreteDomain.java`

- Pre-analysis: classes 4, methods 29, loops 1, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: offset (line 266)
- Pattern: allocation-pressure
- What was found: Loop at line 266 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: "overflowed computing offset(" + origin + ", " + distance + ")");

### `guava\src\com\google\common\collect\ImmutableListMultimap.java`

- Pre-analysis: classes 2, methods 13, loops 5, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 538
- Pattern: allocation-pressure
- What was found: Loop at line 538 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw new InvalidObjectException("Invalid value count " + valueCount);

### `guava\src\com\google\common\collect\ImmutableSetMultimap.java`

- Pre-analysis: classes 3, methods 21, loops 6, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 707
- Pattern: allocation-pressure
- What was found: Loop at line 707 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw new InvalidObjectException("Invalid value count " + valueCount); | throw new InvalidObjectException("Duplicate key-value pairs exist for key " + key);

### `guava\src\com\google\common\collect\ImmutableSortedSet.java`

- Pre-analysis: classes 4, methods 47, loops 4, streams 0, synchronized blocks 3
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: sortAndDedup (line 475)
- Pattern: allocation-pressure
- What was found: Loop at line 475 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: "Comparator " + comparator + " compare method violates its contract");

### `guava\src\com\google\common\collect\JdkBackedImmutableBiMap.java`

- Pre-analysis: classes 2, methods 13, loops 1, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: create (line 38)
- Pattern: allocation-pressure
- What was found: Loop at line 38 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw conflictException("key", e.getKey() + "=" + oldValue, entryArray[i]); | throw conflictException("value", oldKey + "=" + e.getValue(), entryArray[i]);

### `guava\src\com\google\common\collect\Multimap.java`

- Pre-analysis: classes 3, methods 1, loops 3, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 67
- Pattern: allocation-pressure
- What was found: Loop at line 67 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: *   out.println(firstName + ": " + lastNames);

### `guava\src\com\google\common\collect\Synchronized.java`

- Pre-analysis: classes 27, methods 1, loops 0, streams 2, synchronized blocks 217
#### 1. Parallel stream usage requires workload validation
- Severity: Low
- Confidence: Medium
- Location: Synchronized (line 201)
- Pattern: concurrency-misuse
- What was found: Line 201 uses `parallelStream()`.
- Why it is wasteful: Parallel streams can add splitting, synchronization, and scheduling overhead when workloads are small or blocking.
- Likely impact: Higher CPU use and worse latency instead of better throughput.
- Recommended remediation: Validate collection size and workload type, or prefer explicit bounded executors for heavy tasks.
- Low-waste rationale: Concurrency should only add parallel work when it reduces total operations per useful result.
- Evidence: return delegate().parallelStream();

### `guava\src\com\google\common\primitives\UnsignedLongs.java`

- Pre-analysis: classes 5, methods 1, loops 12, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: UnsignedLongs (line 351)
- Pattern: allocation-pressure
- What was found: Loop at line 351 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw new NumberFormatException("Too large for unsigned long: " + string);

### `guava\src\com\google\common\reflect\TypeVisitor.java`

- Pre-analysis: classes 2, methods 2, loops 1, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: visit (line 66)
- Pattern: allocation-pressure
- What was found: Loop at line 66 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw new AssertionError("Unknown type: " + type);

### `guava-gwt\src-super\com\google\common\collect\super\com\google\common\collect\ForwardingImmutableMap.java`

- Pre-analysis: classes 1, methods 11, loops 1, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 42
- Pattern: allocation-pressure
- What was found: Loop at line 42 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw new IllegalArgumentException("duplicate key: " + key);

### `guava-gwt\src-super\com\google\common\collect\super\com\google\common\collect\ImmutableList.java`

- Pre-analysis: classes 2, methods 46, loops 1, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: nullCheckedList (line 214)
- Pattern: allocation-pressure
- What was found: Loop at line 214 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: throw new NullPointerException("at index " + i);

### `guava-testlib\src\com\google\common\testing\EquivalenceTester.java`

- Pre-analysis: classes 2, methods 6, loops 2, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: testItems (line 102)
- Pattern: allocation-pressure
- What was found: Loop at line 102 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: assertTrue("null must be inequivalent to " + item, !equivalence.equivalent(null, item)); | "the hash of " + item + " must be consistent",

### `guava-testlib\src\com\google\common\testing\ForwardingWrapperTester.java`

- Pre-analysis: classes 3, methods 6, loops 4, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 211
- Pattern: allocation-pressure
- What was found: Loop at line 211 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: "Parameter #" + i + " of " + method + " not forwarded", passedArgs[i], args[i]);

### `guava-tests\benchmark\com\google\common\primitives\UnsignedLongsBenchmark.java`

- Pre-analysis: classes 1, methods 9, loops 7, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: setUp (line 43)
- Pattern: allocation-pressure
- What was found: Loop at line 43 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: prefixedHexStrings[i] = "0x" + hexStrings[i];

### `guava-tests\benchmark\com\google\common\util\concurrent\CycleDetectingLockFactoryBenchmark.java`

- Pre-analysis: classes 1, methods 6, loops 6, streams 0, synchronized blocks 0
#### 1. String concatenation in loop
- Severity: Low
- Confidence: Medium
- Location: line 49
- Pattern: allocation-pressure
- What was found: Loop at line 49 builds strings through repeated concatenation.
- Why it is wasteful: Repeated concatenation can allocate many intermediate strings in hot iteration paths.
- Likely impact: Extra allocation churn and slower formatting-heavy paths.
- Recommended remediation: Use a shared `StringBuilder` or defer formatting until it is needed.
- Low-waste rationale: Reducing intermediate strings lowers heap churn and CPU spent copying characters.
- Evidence: detectingLocks[i] = factory.newReentrantLock("Lock" + i);

## Cautions
- This is static analysis only; findings indicate likely waste patterns, not measured bottlenecks.
- Method extraction and loop classification are heuristic and may miss unconventional Java syntax.