# Theoretical Model For The Talk

This note is an inference from the local talk materials and the `green-java-pr-report` skill rules, because `SKILL.md` does not define a formal mathematical model by itself.

## Model

1. Identify the focal helper, loop, parser, writer, or copy path from the real source code.
2. Estimate the repeated work at the line level in theoretical terms: branches, allocations, buffer growth, copies, wakeups, hash puts, or decode steps.
3. Express that work as relative micro-op style cost (`uOps`) per call or per iteration.
4. Convert the relative work reduction into a directional energy reduction estimate (`mWh`) for the same workload shape.
5. Multiply by call frequency or iteration count to explain why a small per-call saving can plausibly become a double-digit latency and energy improvement in aggregate.

## Interpretation Rules

- This is a comparative model, not a hardware measurement.
- The strongest evidence comes from PR-backed code diffs plus hotspot-shaped call paths.
- Use `100k` aggregate numbers only for repeated loops or repeated helper paths.
- Treat percentages as plausible ranges tied to workload shape, not benchmark claims.

## Story Formula

- Before: identify where repeated work happens.
- Change: show the exact commit hunk that removes, batches, pre-sizes, or reuses work.
- Functional effect: explain what stays semantically the same.
- Performance effect: explain why fewer repeated operations should reduce wall time.
- Energy effect: explain why less repeated CPU and allocation work should also reduce energy.
