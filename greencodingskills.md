\---

name: java-green-code-analyzer

description: analyze a single java source file for low-waste and green-coding inefficiency patterns, then produce a ranked findings report. use when chatgpt or codex needs to review java code for static signs of idle compute, waiting patterns, unnecessary cpu work, avoidable memory pressure, chatty io, repeated work in loops, oversized data handling, unbounded concurrency, or likely bottlenecks using a sustainability and efficiency lens.

\---



\# Analyze Java files for low-waste software patterns



Treat this skill as a \*\*static-analysis-first review workflow\*\* for a \*\*single Java source file\*\*.



The goal is not generic code review. The goal is to identify code structures that likely waste compute, memory, I/O, or concurrency headroom, and to explain those findings in terms of \*\*low-waste engineering\*\* and \*\*green coding\*\*.



Use this skill to produce a \*\*ranked findings report\*\* with emphasis on:

\- idle compute

\- avoidable waiting

\- unnecessary CPU work

\- excessive allocation or copying

\- repeated work

\- chatty I/O or likely N+1 behavior

\- oversized payload construction

\- lockstep / serialized flow

\- unbounded or poorly controlled concurrency

\- algorithmic structures that scale wastefully



\## Operating model



Follow this sequence:



1\. Inspect one Java source file only.

2\. Perform deterministic pre-analysis first.

3\. Extract candidate inefficiency patterns.

4\. Evaluate severity and confidence.

5\. Produce a ranked findings report.

6\. For each finding, explain:

&#x20;  - what pattern is present

&#x20;  - why it is wasteful

&#x20;  - what user/system impact it can create

&#x20;  - what concrete code-level remediation to consider



Do not claim runtime proof. This skill is \*\*static analysis only\*\*.

Frame findings as:

\- \*\*Observed pattern\*\*

\- \*\*Likely impact\*\*

\- \*\*Why it matters for low-waste software\*\*

\- \*\*Recommended remediation\*\*

\- \*\*Confidence\*\*



\## What to look for



\### 1. Idle compute and waiting patterns

Flag constructs that keep CPU active without proportional value:

\- polling loops

\- spin-wait style loops

\- retry loops with short fixed sleeps

\- repeated condition checking in tight loops

\- busy waiting around shared state

\- loops that repeatedly scan collections while waiting for external state



Examples of suspicious signals:

\- `while (...) {}` with no blocking primitive

\- repeated `Thread.sleep(...)` used as coordination

\- repeated status checks instead of callback/event/completion mechanism

\- manual backoff missing or poorly bounded



\### 2. Blind or chatty I/O patterns

Flag code that likely shifts latency and energy cost into unnecessary I/O:

\- repeated remote/database/file calls inside loops

\- small repeated reads/writes instead of batching

\- repeated serialization/deserialization

\- request-per-item patterns

\- logging inside hot loops

\- repeated config or metadata fetches inside execution paths



If the file suggests repository/service/network usage inside loops, call out likely chatty behavior even if the callee implementation is not present.



\### 3. Repeated expensive work

Flag repeated computation that should be hoisted, cached, memoized, or precomputed:

\- invariant computation inside loops

\- repeated regex compilation

\- repeated parsing of the same value

\- repeated object mapper creation

\- repeated date/time formatter creation

\- repeated stream transformations over the same data

\- nested loops with repeated scans or lookups



\### 4. Algorithmic waste and scaling risk

Flag structures with likely poor complexity or avoidable work:

\- nested loops over growing collections

\- repeated `.contains()` on lists in loops where a set is more appropriate

\- repeated sorting

\- repeated full scans for each item

\- avoidable `O(n²)` or worse behavior

\- duplicate transformations on large collections



\### 5. Allocation and memory pressure

Flag allocation-heavy patterns that likely increase GC churn or memory waste:

\- excessive temporary object creation in loops

\- repeated string concatenation in loops where builders are appropriate

\- unnecessary copying of collections

\- oversized DTO/entity mapping

\- loading more data than needed

\- building large intermediate collections when streaming/filtering earlier would suffice

\- converting between collection types repeatedly



\### 6. Concurrency and parallelism misuse

Flag static signs of wasteful concurrency:

\- unbounded thread creation

\- broad parallelization without workload sizing

\- parallel streams on likely small or blocking workloads

\- executor creation per call

\- futures created but joined immediately in sequence

\- contention-prone synchronized regions around expensive work

\- serialized flow disguised as async



Do not praise concurrency by default. Assess whether the structure likely increases waste, context switching, lock contention, or thermal/CPU pressure without corresponding value.



\### 7. Data movement and payload bloat

Flag signs of moving or constructing more data than needed:

\- fetching or assembling full objects where narrow fields would do

\- verbose DTO mapping chains

\- repeated JSON/XML conversion

\- large payload construction before filtering

\- logging entire objects or payloads on normal paths

\- broad collection materialization before small downstream use



\## Severity model



Rank findings using this priority order:



\### High

Use for patterns that likely create substantial waste or bottlenecks:

\- likely busy-waiting

\- likely repeated remote/database/file access in loops

\- likely `O(n²)` behavior on meaningful collections

\- unbounded concurrency

\- synchronization around expensive work

\- large avoidable allocation churn in hot paths



\### Medium

Use for patterns that are clearly suboptimal but context-sensitive:

\- repeated object creation

\- repeated parsing or formatter construction

\- logging in loops

\- unnecessary copying

\- sequential operations that appear batchable

\- parallel stream misuse with unclear impact



\### Low

Use for localized or style-adjacent inefficiencies:

\- minor redundant checks

\- small temporary allocations outside loops

\- local cleanup opportunities with limited likely impact



\## Confidence model



Use:

\- \*\*High confidence\*\* when the waste pattern is directly visible in the file.

\- \*\*Medium confidence\*\* when the pattern is strongly suggested by method names, APIs, or surrounding structure.

\- \*\*Low confidence\*\* when the concern depends heavily on unseen code or production context.



Never present speculative runtime claims as certain.



\## Pre-analysis requirements



Before writing the report, perform lightweight deterministic analysis on the file and capture:



\- classes and methods

\- loops and nesting depth

\- stream pipelines

\- synchronized blocks / locks

\- thread / executor / future / parallel stream usage

\- sleep, wait, retry, polling patterns

\- collection operations inside loops

\- object creation inside loops

\- logging inside loops

\- likely I/O callsites based on names and imports

\- serialization, parsing, mapping, regex, formatting calls

\- large string / payload construction patterns



If a bundled script is available, run it first and use its output as supporting evidence. Then refine with model judgment.



\## Reporting format



Always return a \*\*ranked findings report\*\* in this structure:



\### Summary

\- File reviewed

\- Overall risk level: High / Medium / Low

\- Top efficiency themes

\- Count of findings by severity



\### Ranked findings

For each finding, use this template:



\#### \[Rank]. \[Short finding title]

\- \*\*Severity:\*\* High | Medium | Low

\- \*\*Confidence:\*\* High | Medium | Low

\- \*\*Location:\*\* class/method/line range if available

\- \*\*Pattern:\*\* one of:

&#x20; - idle-compute

&#x20; - waiting-pattern

&#x20; - chatty-io

&#x20; - repeated-work

&#x20; - algorithmic-waste

&#x20; - allocation-pressure

&#x20; - concurrency-misuse

&#x20; - data-movement-bloat

\- \*\*What was found:\*\* concise description of the code structure

\- \*\*Why it is wasteful:\*\* explain compute, memory, I/O, or coordination waste

\- \*\*Likely impact:\*\* latency, throughput, GC churn, lock contention, cost, energy, thermal pressure, scalability

\- \*\*Recommended remediation:\*\* specific code-level change

\- \*\*Low-waste rationale:\*\* connect remediation to reducing operations, waiting, bytes moved, or excess parallel overhead



\### Quick wins

Give 3 to 5 short, practical fixes ordered by expected payoff.



\### Cautions

State what cannot be proven from static analysis alone.



\## Review stance



Prefer findings that connect to \*\*value per watt\*\* and \*\*operations per useful action\*\*, not generic “code smell” commentary.



Good findings explain wasted work in these terms:

\- more operations than necessary

\- more bytes moved than necessary

\- more waiting than necessary

\- more allocation than necessary

\- more concurrency than useful

\- more heat/CPU pressure without more user value



Avoid weak comments like:

\- “this might be cleaner”

\- “consider refactoring”

\- “use best practices”



Instead, be concrete:

\- hoist invariant work out of the loop

\- replace list membership checks with a set

\- batch repository calls outside per-item iteration

\- replace polling with blocking/event-driven coordination

\- reuse formatter/parser/mapper instances

\- bound executor concurrency

\- remove immediate-join async patterns

\- narrow fetched or constructed payloads



\## Constraints



\- Analyze exactly one Java source file.

\- Do not require runtime traces, profilers, or benchmarks.

\- Do not invent unavailable classes or method bodies.

\- Do not overstate energy or carbon numbers.

\- Do not claim measured bottlenecks.

\- Do not rewrite the whole file unless explicitly requested.

\- Focus on the highest-value inefficiency findings first.



\## Optional follow-up modes



If the user asks, provide one of these follow-ups after the report:

\- a minimal remediation patch plan

\- a refactoring sketch

\- a prioritized backlog list

\- a JSON version of the findings

