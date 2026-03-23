from pathlib import Path

parts = []

def add(text: str) -> None:
    parts.append(text)

add(r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Balanced GitHub Examples For Voxxed Days</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css">
  <style>
    body { background: radial-gradient(circle at top left, rgba(245,158,11,.12), transparent 24%), radial-gradient(circle at top right, rgba(13,148,136,.14), transparent 28%), #f7f3ec; color: #20312b; }
    header { padding: 32px 0 14px; }
    .hero { border-radius: 28px; padding: 32px; background: linear-gradient(135deg, #163d34 0%, #23584c 55%, #c26a07 140%); color: #fff; box-shadow: 0 18px 42px rgba(22,61,52,.18); }
    .hero p { color: rgba(255,255,255,.92); font-size: 1.04rem; }
    .chip-panel .chip { background: rgba(255,255,255,.12); color: #fff; border: 1px solid rgba(255,255,255,.14); margin-bottom: 8px; }
    .section-card, .repo-card { border-radius: 20px; box-shadow: 0 10px 26px rgba(32,42,37,.08); }
    .repo-card { padding: 20px; background: #fffaf2; min-height: 180px; }
    .repo-title { font-size: 1.35rem; font-weight: 700; margin-bottom: 8px; }
    .repo-band { margin: 32px 0 14px; padding: 14px 18px; border-left: 6px solid #c26a07; background: #fff8ef; border-radius: 16px; }
    .collapsible { border: none; box-shadow: 0 10px 26px rgba(32,42,37,.08); border-radius: 22px; overflow: hidden; }
    .collapsible-header { border-bottom: 1px solid #efe3d1; min-height: 96px; align-items: center; gap: 14px; padding: 20px 24px; background: #fffdfa; }
    .collapsible-body { border-bottom: 1px solid #efe3d1; background: #fff9f2; padding: 24px; }
    .example-title { font-size: 1.08rem; font-weight: 700; }
    .example-subtitle { margin-top: 4px; color: #5f6d67; }
    .tag-wrap { margin-left: auto; display: flex; flex-wrap: wrap; gap: 8px; justify-content: flex-end; }
    .pill { border-radius: 999px; padding: 6px 10px; font-size: .78rem; font-weight: 700; }
    .pill-cpu { background: #d1fae5; color: #065f46; }
    .pill-wait { background: #dbeafe; color: #1d4ed8; }
    .pill-bottle { background: #ffedd5; color: #c2410c; }
    .pill-strong { background: #dcfce7; color: #166534; }
    .pill-good { background: #fef3c7; color: #92400e; }
    .pill-context { background: #e5e7eb; color: #374151; }
    .mini-card { background: #fff; border-radius: 18px; padding: 18px; margin-bottom: 16px; box-shadow: inset 0 0 0 1px #f1e4d1; }
    .mini-card h6 { font-size: .98rem; font-weight: 700; margin-top: 0; margin-bottom: 10px; }
    .link-list a { display: inline-block; margin: 0 14px 10px 0; font-weight: 600; }
    pre[class*=language-] { border-radius: 14px; font-size: .87rem; }
    code[class*=language-] { white-space: pre-wrap; }
    footer { margin: 40px 0 30px; color: #5f6d67; }
  </style>
</head>
<body>
  <div class="container">
    <header>
      <div class="hero">
        <h3>Balanced GitHub Examples For The Talk</h3>
        <p>This report uses all three repositories and keeps the split explicit: 4 examples from JSON-java, 3 from Commons IO, and 3 from Guava. It keeps one <code>toString()</code> example, shows explicit before-to-after percentage estimates, and expands each example with upstream discussion context, a longer explainer, and larger code context.</p>
        <div class="chip-panel">
          <div class="chip">10 examples total</div>
          <div class="chip">Repo split: 4 / 3 / 3</div>
          <div class="chip">1 toString example</div>
          <div class="chip">PR summary + explainer + code context</div>
          <div class="chip">100k aggregate uOps view</div>
        </div>
      </div>
    </header>

    <div class="card section-card"><div class="card-content"><span class="card-title">How To Read This Report</span><p>Each example is grouped under its GitHub repository so a first-time reader immediately sees the project source. Every example now includes an explicit <strong>before -&gt; after estimated improvement</strong>, a short upstream summary of the PR, issue, or advisory discussion, and a longer explainer that combines the code shape, the likely trace or thread-dump signal, and the way the upstream change reduced work. The inline code comments use a 100,000-call or 100,000-iteration view to make instruction leaks visible instead of abstract.</p></div></div>

    <div class="row">
      <div class="col s12 m4"><div class="repo-card"><div class="repo-title">stleary/JSON-java</div><p>4 examples. Strongest PR and release trail. Best for parser CPU hotspots, bounded work, and one serialization case.</p><a href="https://github.com/stleary/JSON-java" target="_blank" rel="noopener">Open repository</a></div></div>
      <div class="col s12 m4"><div class="repo-card"><div class="repo-title">apache/commons-io</div><p>3 examples. Good for waiting patterns, reader loops, and hidden utility-code overhead.</p><a href="https://github.com/apache/commons-io" target="_blank" rel="noopener">Open repository</a></div></div>
      <div class="col s12 m4"><div class="repo-card"><div class="repo-title">google/guava</div><p>3 examples. Good for maintenance loops, scheduling cost, and background-thread design tradeoffs.</p><a href="https://github.com/google/guava" target="_blank" rel="noopener">Open repository</a></div></div>
    </div>
""")
