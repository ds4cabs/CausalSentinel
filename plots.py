"""Figure generators for the evidence cards and dossiers.

Run:
    python plots.py --protein IL6R                 # both figures for one protein
    python plots.py --protein PCSK9 --outdir figs

Two figures, both rendered from live tool output — no hand-entered numbers:

    {PROTEIN}_mr_forest.png       retrieved MR estimates across outcomes, with CIs
    {PROTEIN}_constraint.png      where this gene sits in the gnomAD LOEUF distribution

A third figure was asked for in the project brief — a colocalization regional plot — and
is deliberately NOT produced. It needs per-SNP association statistics and an LD reference
across the locus; this project holds neither. Drawing one from the summary values we do
have would be a picture of nothing. Where a published regional plot exists, link to it
rather than redrawing it.

Design rule, same as the cards: every number on these axes comes from a tool return
value. Nothing is typed in, so a figure cannot drift from the data it claims to show.
"""
import argparse
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import matplotlib
matplotlib.use("Agg")                     # no display on a headless machine
import matplotlib.pyplot as plt
import numpy as np

from tools.mr import get_mr_outcomes
from tools.gnomad import get_gnomad_constraint

HERE = Path(__file__).resolve().parent
INK, ACCENT, WARN = "#1a1a1a", "#065A82", "#B03A2E"


def _style(ax):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.spines["left"].set_color("#bbb")
    ax.spines["bottom"].set_color("#bbb")
    ax.tick_params(colors="#444", labelsize=9)


def mr_forest(protein: str, outdir: Path, top_n: int = 15):
    """Forest plot of retrieved MR estimates: one row per outcome, 95% CI from beta/se.

    Sorted by p-value and truncated to the strongest `top_n`, which is stated on the
    figure — a silently truncated plot is the visual version of the pagination bug.
    """
    mr = get_mr_outcomes(protein)
    outs = [o for o in (mr.get("outcomes") or [])
            if o.get("beta") is not None and o.get("se") is not None]
    if not outs:
        print(f"[forest] {protein}: no retrieved MR estimates — nothing to plot")
        return None

    total = len(outs)
    rows = outs[:top_n][::-1]                       # strongest at the top of the axis
    y = np.arange(len(rows))
    beta = np.array([r["beta"] for r in rows], dtype=float)
    se = np.array([r["se"] for r in rows], dtype=float)
    lo, hi = beta - 1.96 * se, beta + 1.96 * se
    # cis instruments are less pleiotropy-prone; make that visible rather than a footnote
    is_cis = [str(r.get("cis_or_trans")).lower() == "cis" for r in rows]
    colors = [ACCENT if c else "#8b949e" for c in is_cis]

    fig, ax = plt.subplots(figsize=(9.5, 0.42 * len(rows) + 2.1))
    ax.axvline(0, color="#999", lw=1, ls="--", zorder=0)
    for i in range(len(rows)):
        ax.plot([lo[i], hi[i]], [y[i], y[i]], color=colors[i], lw=1.6, solid_capstyle="round")
    ax.scatter(beta, y, s=34, color=colors, zorder=3)

    labels = []
    for r in rows:
        t = str(r.get("outcome"))
        labels.append((t[:52] + "…") if len(t) > 53 else t)
    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=8.5)
    ax.set_xlabel("MR effect estimate (beta, 95% CI)", fontsize=10)
    shown = f"top {len(rows)} of {total} outcomes by p-value" if total > len(rows) \
            else f"all {total} outcomes"
    ax.set_title(f"{protein} — retrieved MR estimates\n{shown}",
                 fontsize=12, color=INK, loc="left", pad=12)
    _style(ax)

    handles = [plt.Line2D([], [], color=ACCENT, lw=2, marker="o", ls="-", label="cis instrument"),
               plt.Line2D([], [], color="#8b949e", lw=2, marker="o", ls="-", label="trans instrument")]
    ax.legend(handles=handles, fontsize=8.5, frameon=False, loc="lower right")
    fig.text(0.01, 0.01,
             "Estimates RETRIEVED from published MR (EpiGraphDB pQTL, Zheng et al. 2020) — "
             "not computed here. Exposure is protein abundance, not a drug.",
             fontsize=7.2, color="#57606a")
    fig.tight_layout(rect=[0, 0.035, 1, 1])
    out = outdir / f"{protein}_mr_forest.png"
    fig.savefig(out, dpi=200)
    plt.close(fig)
    print(f"[forest] wrote {out.name}  ({len(rows)}/{total} outcomes)")
    return out


# LOEUF deciles from gnomAD's constraint distribution, used only to place the gene in
# context. Approximate bin edges; the gene's own value is exact and comes from the tool.
_LOEUF_GRID = np.linspace(0, 2.0, 41)


def constraint_plot(protein: str, outdir: Path):
    """Where this gene sits on the LoF-constraint scale, with the intolerance line drawn.

    The point of the figure is the threshold, not the number: LoF-intolerance is a SAFETY
    WARNING about inhibiting a target, and it is routinely read backwards as a merit.
    """
    g = get_gnomad_constraint(protein)
    if not g.get("found") or g.get("LOEUF") is None:
        print(f"[constraint] {protein}: no gnomAD constraint — nothing to plot")
        return None
    loeuf, pli = float(g["LOEUF"]), g.get("pLI")

    fig, ax = plt.subplots(figsize=(9.0, 2.9))
    # a light reference band for the scale, then the two things that matter
    ax.axvspan(0, 0.35, color="#ffebe9", zorder=0)
    ax.axvspan(0.35, 2.0, color="#f2f7f4", zorder=0)
    ax.axvline(0.35, color=WARN, lw=1.6, ls="--", zorder=2)
    ax.scatter([loeuf], [0.5], s=190, color=ACCENT, zorder=4, edgecolor="white", linewidth=1.6)
    ax.annotate(f"{protein}\nLOEUF = {loeuf:.3g}",
                xy=(loeuf, 0.5), xytext=(loeuf, 0.78), ha="center", fontsize=10,
                color=INK, arrowprops=dict(arrowstyle="-", color="#888", lw=1))
    ax.text(0.175, 0.13, "LoF-INTOLERANT\n(LOEUF < 0.35)\nsafety warning for inhibition",
            ha="center", fontsize=8.5, color=WARN)
    ax.text(1.15, 0.13, "LoF-tolerant — reassuring about inhibition,\n"
                        "but NOT evidence of efficacy",
            ha="center", fontsize=8.5, color="#3d6b52")

    verdict = "LoF-INTOLERANT" if loeuf < 0.35 else "LoF-tolerant"
    pli_txt = f"pLI = {pli:.3g}" if isinstance(pli, (int, float)) else "pLI = NA"
    ax.set_xlim(0, 2.0)
    ax.set_ylim(0, 1.0)
    ax.set_yticks([])
    ax.set_xlabel("gnomAD LOEUF  (lower = more intolerant to loss of function)", fontsize=10)
    ax.set_title(f"{protein} — population constraint: {verdict}   ·   {pli_txt}",
                 fontsize=12, color=INK, loc="left", pad=10)
    _style(ax)
    fig.text(0.01, 0.02, f"Source: {g.get('source_release', 'gnomAD')} · "
                         f"threshold used: {g.get('thresholds_used', 'LOEUF < 0.35')}",
             fontsize=7.2, color="#57606a")
    fig.tight_layout(rect=[0, 0.06, 1, 1])
    out = outdir / f"{protein}_constraint.png"
    fig.savefig(out, dpi=200)
    plt.close(fig)
    print(f"[constraint] wrote {out.name}  (LOEUF={loeuf:.3g} -> {verdict})")
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description="Figures for CausalSentinel cards and dossiers")
    ap.add_argument("--protein", required=True, help="gene symbol, e.g. IL6R")
    ap.add_argument("--outdir", default="figs")
    ap.add_argument("--top-n", type=int, default=15, help="max outcomes on the forest plot")
    args = ap.parse_args()

    outdir = HERE / args.outdir
    outdir.mkdir(parents=True, exist_ok=True)
    mr_forest(args.protein, outdir, args.top_n)
    constraint_plot(args.protein, outdir)
    print(f"[plots] output directory: {outdir}")
    print("[plots] note: the coloc regional plot from the brief is NOT generated — it needs "
          "per-SNP statistics and an LD reference this project does not hold.")


if __name__ == "__main__":
    main()
