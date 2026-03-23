---
name: green-java-pr-report
description: Build or refine a talk-ready HTML report of mature Java code examples focused on CPU usage, waiting, and bottlenecks, using local GitRepos plus upstream GitHub PR or issue evidence. Use when the user wants slide-friendly examples, upstream before/after code diffs, uOps-style annotations, or a curated report for green software or performance talks.
metadata:
  short-description: Build strict PR-backed green-code talk examples
---

# Green Java PR Report

Use this skill when working on a report like `talk_examples_overview.html` for a green software or performance talk.

## Goal

Produce a small set of explainable Java examples that:
- are easy for a mixed audience to understand
- map to CPU usage, waiting, or bottlenecks
- use real source snippets from local repos
- prefer upstream PR-backed before/after diffs
- stay honest about provenance when evidence is weaker

## Primary Workflow

1. Inspect the local report and current example set.
2. Inspect local source files under `GitRepos`.
3. Verify upstream evidence before making claims.
4. Keep only examples that fit the current evidence bar.
5. Update the HTML so the report is readable, honest, and presentation-friendly.

## Evidence Rules

- Prefer examples with:
  - upstream PR link
  - PR files link
  - usable before/after code diff
- If an example has only:
  - issue context
  - advisory context
  - source-only architectural context
  then label it clearly and do not imply it is a fixed PR-backed example.
- If the user asks for strict proof, remove weaker examples instead of stretching the wording.

## Talk Fit Rules

- Favor mature Java libraries.
- Favor helpers, IO, logging, JSON, parser, serialization, cache, scheduling, and waiting patterns.
- Keep examples explainable to a general Java audience.
- Avoid examples that require too much framework-specific knowledge.
- Prefer low-risk improvements over spectacular claims.

## Code Example Rules

- Use only code found in the actual source files.
- For PR-backed examples, add:
  - `PR Commit Before / After`
  - real diff-backed snippets
- For main example snippets:
  - include enough surrounding lines to show call flow and context
  - place explanatory comments on the line below the relevant source line
  - keep comments short and concrete
- Use aggregate `100k` uOps numbers only for iterative paths like loops, polling, rescans, or repeated queue checks.

## Report Rules

- Use GitHub `blob` links, not local file links, inside the report itself.
- Make the repository obvious at first glance.
- Show estimated `before -> after improvement` both:
  - as a detail line
  - as a small header label
- For each example, keep:
  - source repository and file
  - upstream trail
  - PR/discussion summary
  - explainer
  - prediction signal
  - code clues with inline uOps

## UI Rules

- Keep the HTML readable for slides and screenshots.
- Use Materialize CDN styling already present in the report unless the user asks otherwise.
- Prefer clear hierarchy and readable code blocks over flashy UI.
- If header pills collide with text, stack pills below the subtitle.
- Highlight changed or focal lines with a light background that stays readable.

## Useful Local Paths

- Report: `C:\VoxxedDays\talk_examples_overview.html`
- Main repos:
  - `C:\VoxxedDays\GitRepos\JSON-java-master`
  - `C:\VoxxedDays\GitRepos\commons-io-master`
  - `C:\VoxxedDays\GitRepos\guava-master`
- Downloaded upstream patches:
  - `C:\VoxxedDays\pr_patches`

## Useful Commands

- Search report content:
  - `rg -n "example-title|PR Commit Before / After|Diff Availability" C:\VoxxedDays\talk_examples_overview.html`
- Search repo code:
  - `rg -n "needle" C:\VoxxedDays\GitRepos\<repo>`
- Inspect patch files:
  - `rg -n "diff --git|Subject:|needle" C:\VoxxedDays\pr_patches\<file>.patch`

## Patch Download Pattern

If local repos do not contain `.git` history, fetch PR patch files from GitHub and save them under `C:\VoxxedDays\pr_patches`, then extract before/after snippets from those patch files.

## Output Standard

When the user wants the report tightened:
- be explicit about what is fully proven
- be explicit about what is only issue-backed or context-backed
- prefer fewer examples with stronger evidence over more examples with weaker evidence
