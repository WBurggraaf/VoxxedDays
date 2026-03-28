from pathlib import Path
from html import escape
import json


def load_proof_index(root: Path) -> dict:
    single = {}
    output_root = root / 'flamegraph' / 'output'
    if output_root.exists():
        for repo_dir in output_root.iterdir():
            if not repo_dir.is_dir():
                continue
            meta_path = repo_dir / f'{repo_dir.name}.meta.json'
            if not meta_path.exists():
                continue
            data = json.loads(meta_path.read_text(encoding='utf-8'))
            for command in data.get('commands', []):
                for proof in command.get('proofs', []):
                    single[(data['repo_id'], command['id'], proof['id'])] = {
                        'repo': data,
                        'command': command,
                        'proof': proof,
                    }

    pairs = {}
    pair_root = root / 'flamegraph' / 'output_pairs'
    if pair_root.exists():
        for example_dir in pair_root.iterdir():
            if not example_dir.is_dir():
                continue
            meta_path = example_dir / 'pair.meta.json'
            if not meta_path.exists():
                continue
            data = json.loads(meta_path.read_text(encoding='utf-8'))
            pairs[(data['repo_id'], data['command_id'], data['proof_id'])] = data

    return {'single': single, 'pairs': pairs}


def _rel(root: Path, path_str: str) -> str:
    path = Path(path_str)
    if path.exists():
        try:
            return path.relative_to(root).as_posix()
        except ValueError:
            return str(path).replace('\\', '/')
    return path_str.replace('\\', '/')


def render_pair_proof_card(root: Path, pair: dict) -> str:
    before_svg_path = Path(pair['before']['focused_svg'])
    after_svg_path = Path(pair['after']['focused_svg'])
    before_svg = before_svg_path.read_text(encoding='utf-8') if before_svg_path.exists() else ''
    after_svg = after_svg_path.read_text(encoding='utf-8') if after_svg_path.exists() else ''
    delta = pair['delta']
    before_ms = delta['average_ms_before']
    after_ms = delta['average_ms_after']
    saved_ms = delta['average_ms_saved']
    saved_pct = delta['average_ms_saved_pct']
    before_samples = pair['before']['samples']
    after_samples = pair['after']['samples']
    before_focused = pair['before']['focused_samples']
    after_focused = pair['after']['focused_samples']
    before_share = (before_focused / before_samples * 100.0) if before_samples else 0.0
    after_share = (after_focused / after_samples * 100.0) if after_samples else 0.0
    share_delta = before_share - after_share
    focus_terms = ''.join(f"<span class='proof-chip'>{escape(term)}</span>" for term in pair['focus_terms'])
    before_artifacts = f"<code>{escape(_rel(root, pair['before']['focused_svg']))}</code> and <code>{escape(_rel(root, pair['before']['focused_folded']))}</code>"
    after_artifacts = f"<code>{escape(_rel(root, pair['after']['focused_svg']))}</code> and <code>{escape(_rel(root, pair['after']['focused_folded']))}</code>"
    verdict = 'Below 10% in this proof run' if saved_pct < 10 else 'Meets 10% threshold in this proof run'
    if before_samples and after_samples:
        share_text = (
            f"The focal method family accounted for <strong>{before_share:.1f}%</strong> of sampled execution before the change "
            f"and <strong>{after_share:.1f}%</strong> after it, a <strong>{share_delta:.1f} point</strong> shift."
        )
        if share_delta > 0:
            share_explainer = "This is the visual proof story: the hot block is a smaller share of total execution after the change, so the runtime spends less time in that helper path."
        elif share_delta < 0:
            share_explainer = "In this harness the focused block grew as a share of samples, so the flamegraph does not support the claimed hotspot reduction even if wall-clock time moved slightly."
        else:
            share_explainer = "In this harness the focused block kept the same sample share, so the wall-clock delta is not backed by a visible hotspot-share shift."
    else:
        share_text = "No JFR execution samples were captured for this before/after pair, so the proof falls back to timing-only evidence." 
        share_explainer = "The SVG placeholders are still shown for traceability, but they are not usable as hotspot-share proof for this run."
    return (
        "<div class='mini-card'><h6>Flamegraph Proof</h6>"
        "<p>This proof compares the exact focal optimization patch by reversing that patch for the before side and running the current code for the after side. The SVGs below are filtered down to the hotspot family used in the talk point.</p>"
        f"<p><strong>Measured timing:</strong> before <strong>{before_ms:.3f} ms</strong>, after <strong>{after_ms:.3f} ms</strong>, delta <strong>{saved_ms:.3f} ms</strong> ({saved_pct:.2f}%). {verdict}.</p>"
        f"<p><strong>Focused samples:</strong> before <strong>{before_focused}</strong> of <strong>{before_samples}</strong>, after <strong>{after_focused}</strong> of <strong>{after_samples}</strong>.</p>"
        f"<p><strong>Hotspot share:</strong> {share_text}</p>"
        f"<p>{share_explainer}</p>"
        f"<div class='proof-chip-wrap'>{focus_terms}</div>"
        "<div class='proof-pair'>"
        f"<div class='proof-side'><div class='proof-side-title'>Before commit state</div><p class='proof-artifacts'>Artifacts: {before_artifacts}</p><div class='flameproof'>{before_svg}</div></div>"
        f"<div class='proof-side'><div class='proof-side-title'>After commit state</div><p class='proof-artifacts'>Artifacts: {after_artifacts}</p><div class='flameproof'>{after_svg}</div></div>"
        "</div></div>"
    )


def render_single_proof_card(root: Path, info: dict) -> str:
    command = info['command']
    proof = info['proof']
    svg_path = Path(proof['svg'])
    svg_markup = svg_path.read_text(encoding='utf-8') if svg_path.exists() else ''
    sample_summary = (
        f"Focused samples: <strong>{proof['samples']}</strong> from command total <strong>{command['samples']}</strong> "
        f"across <strong>{command['iterations']}</strong> iterations."
    )
    focus_terms = ''.join(f"<span class='proof-chip'>{escape(term)}</span>" for term in proof['focus_terms'])
    artifact_path = _rel(root, proof['svg'])
    folded_rel = _rel(root, proof['folded'])
    return (
        "<div class='mini-card'><h6>Flamegraph Proof</h6>"
        "<p>This partial is filtered down to stack traces that match the focal method family for the report point instead of showing the whole repo run.</p>"
        f"<p>{sample_summary}</p>"
        f"<div class='proof-chip-wrap'>{focus_terms}</div>"
        f"<p class='proof-artifacts'>Artifacts: <code>{escape(artifact_path)}</code> and <code>{escape(folded_rel)}</code></p>"
        f"<div class='flameproof'>{svg_markup}</div>"
        "</div>"
    )


def render_proof_card(root: Path, example: dict, proof_index: dict) -> str:
    if example.get('manual_proof_html'):
        return example['manual_proof_html']
    key = (example['repo_id'], example['command_id'], example['proof_id'])
    pair = proof_index.get('pairs', {}).get(key)
    if pair:
        return render_pair_proof_card(root, pair)
    info = proof_index.get('single', {}).get(key)
    if info:
        return render_single_proof_card(root, info)
    return "<div class='mini-card'><h6>Flamegraph Proof</h6><p>No focused flamegraph proof has been generated for this example yet.</p></div>"
