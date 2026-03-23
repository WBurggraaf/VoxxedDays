# GitRepos Analyzer

This workspace includes a local batch analyzer that applies the green-coding review rules from `greencodingskills.md` across every Java project under `GitRepos`.

## Run

```powershell
python .\scripts\analyze_gitrepos.py
```

Optional arguments:

```powershell
python .\scripts\analyze_gitrepos.py --repos-root .\GitRepos --output-root .\analysis_reports
python .\scripts\analyze_gitrepos.py --include-tests --output-root .\analysis_reports_full
```

## Output

- `analysis_reports/README.md`: project rollup
- `analysis_reports/rollup.csv`: tabular project summary
- `analysis_reports/<project>/analysis.json`: machine-readable file-level results
- `analysis_reports/<project>/report.md`: readable project report with hotspots and ranked findings
- `analysis_reports/<project>/findings.csv`: tabular finding export per project

## Scope

- By default analyzes production `*.java` files in each project folder under `GitRepos`
- Optional full sweep mode includes test sources with `--include-tests`
- Uses deterministic pre-analysis data: classes, methods, loops, streams, synchronized usage, concurrency markers
- Flags likely waste patterns from the markdown spec: idle compute, waiting, chatty I/O, repeated work, algorithmic waste, allocation pressure, concurrency misuse, and payload bloat

## Notes

- The analyzer is heuristic static analysis only
- It does not compile projects or require external dependencies
- Findings are intended for project triage and hotspot discovery, not runtime proof
