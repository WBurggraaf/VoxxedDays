# Flamegraph Harness

This folder contains a repeatable profiling harness for the four library codebases referenced in the talk:

- `stleary/JSON-java`
- `apache/commons-io`
- `FasterXML/jackson-core`
- `apache/logging-log4j2`

The runner executes representative batches of each library's existing tests, records Java Flight Recorder samples for the test JVMs, converts those samples into folded stacks, and renders a self-contained SVG flamegraph per library.

## Output layout

Running the harness writes artifacts under `flamegraph/output/<repo-id>/`:

- `<repo-id>.svg`: generated flamegraph
- `<repo-id>.folded.txt`: folded stack format
- `<repo-id>.meta.json`: run metadata, commands, recordings, and sample counts
- `*.jfr`: raw JFR recordings for each command batch
- `*.log`: command logs

An index is also generated at `flamegraph/output/index.html`.

## Usage

From `C:\VoxxedDays`:

```powershell
python .\flamegraph\run_flamegraphs.py
```

Run a subset:

```powershell
python .\flamegraph\run_flamegraphs.py --repos json-java,commons-io
```

Dry-run the commands:

```powershell
python .\flamegraph\run_flamegraphs.py --dry-run
```

Continue past a failing repo:

```powershell
python .\flamegraph\run_flamegraphs.py --continue-on-error
```

## Prerequisites

- Java 17+ with `jfr.exe` on `PATH`
- Maven on `PATH`
- Python 3.10+
- Network access if Maven or Gradle dependencies are not already present in the local caches

## Notes

- The workload uses multiple existing tests per library so the profile covers major public functionality instead of a synthetic microbenchmark.
- JSON-java is launched through its Gradle wrapper with a temporary init script so the upstream build does not need to be edited.
- The other repositories are launched through Maven with JFR injected via test JVM arguments.
