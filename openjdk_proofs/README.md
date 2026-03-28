# OpenJDK Proof Harness

This folder adds a local proof path for the OpenJDK examples already referenced in `talk_examples_overview.html`.

The goal is not to replace the published OpenJDK review-thread or article numbers. The goal is to let you run the same public API workload against two JDK homes:

- `before` JDK image or installed JDK
- `after` JDK image or installed JDK

That gives you:

- one workload per talk point
- a before/after wall-clock comparison
- one JFR recording per side
- a machine-readable summary file

## Covered cases

- `threadmxbean-current-user-time`
  Exercises `ThreadMXBean.getCurrentThreadUserTime()` under contention.
- `formatter-simple-fastpath`
  Exercises `String.format` with simple and width-based specifiers.
- `formatter-localized-numbers`
  Exercises locale-sensitive formatting that flows through `Formatter`.
- `collections-bulk-copy`
  Exercises `ArrayList.addAll` from `ArrayList` and singleton inputs.

## What this proves

These probes are public-API reproductions, not in-tree OpenJDK JMH runs.

That means:

- they are valid for building a before/after story on two JDK builds
- they are good inputs for JFR and flamegraph comparison
- they are not a substitute for official OpenJDK benchmark numbers

## Prerequisites

- Windows PowerShell
- one or two JDK homes
- `javac` available for compilation
- JFR support in the JDKs you want to compare

## Compile and run

Example:

```powershell
powershell -ExecutionPolicy Bypass -File .\openjdk_proofs\run_openjdk_proofs.ps1 `
  -BeforeJavaHome 'C:\jdks\jdk-before' `
  -AfterJavaHome 'C:\jdks\jdk-after' `
  -Case all `
  -Iterations 300000 `
  -Threads 16
```

Outputs are written to:

- `openjdk_proofs\output\<case>\before\`
- `openjdk_proofs\output\<case>\after\`

Each side gets:

- `stdout.txt`
- `profile.jfr`
- parsed `summary.json`

## Suggested mapping to the report

- ThreadMXBean example:
  Use `threadmxbean-current-user-time`
- Formatter regex-free parsing:
  Use `formatter-simple-fastpath`
- Formatter locale-symbol caching:
  Use `formatter-localized-numbers`
- Collections bulk-copy fast paths:
  Use `collections-bulk-copy`

## Notes

- The probe classes are intentionally simple so they can run on different JDK builds without extra dependencies.
- The script can also run with the same JDK on both sides as a smoke test, but that is only a harness verification step, not proof of a performance change.
