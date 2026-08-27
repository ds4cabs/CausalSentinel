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


def constraint_plot(protein: str, outdir: Path):
    """Constraint as the counting experiment it actually is, then where that lands.

    The previous version of this figure was a single dot on a bare 0-2 LOEUF axis. It was
    unreadable for two reasons and wrong for a third:

      1. It promised "where this gene sits in the distribution" and drew no distribution,
         so a reader had no way to tell an ordinary LOEUF from an extreme one.
      2. LOEUF is an unfamiliar scale. The thing underneath it — how many loss-of-function
         variants were expected in this gene versus how many were seen — is immediately
         understandable, and was not shown at all.
      3. It recomputed the LoF verdict from LOEUF alone, while `get_gnomad_constraint`
         decides it from `pLI > 0.9 OR LOEUF < 0.35`. For HMGCR (LOEUF 0.43, pLI 1.00) the
         two disagreed: the card said LoF-INTOLERANT while the figure drew the statin
         target in the green "tolerant" zone with a title to match. A figure that
         contradicts its own card is worse than no figure.

    So: panel A is the count comparison, panel B is the percentile, and the verdict is
    taken from the tool rather than re-derived here.
    """
    g = get_gnomad_constraint(protein)
    if not g.get("found") or g.get("LOEUF") is None:
        print(f"[constraint] {protein}: no gnomAD constraint — nothing to plot")
        return None

    loeuf, pli = float(g["LOEUF"]), g.get("pLI")
    obs, exp = g.get("obs_lof"), g.get("exp_lof")
    pct = g.get("LOEUF_percentile")
    # Single source of truth for the verdict: whatever the tool concluded.
    intolerant = "INTOLERANT" in (g.get("interpretation") or "")
    verdict = "LoF-INTOLERANT" if intolerant else "LoF-tolerant"
    vcolor = WARN if intolerant else "#3d6b52"

    fig, (axA, axB) = plt.subplots(
        1, 2, figsize=(10.6, 3.5), gridspec_kw={"width_ratios": [1, 2.15]})

    # --- Panel A: the experiment nature already ran -------------------------------
    if obs is not None and exp:
        bars = axA.bar(["expected", "observed"], [exp, obs],
                       color=["#c9d3dd", vcolor], width=0.6, zorder=3)
        for b, v in zip(bars, [exp, obs]):
            axA.text(b.get_x() + b.get_width() / 2, v, f"{v:.0f}", ha="center",
                     va="bottom", fontsize=10, color=INK)
        axA.set_ylim(0, max(exp, obs) * 1.28)
        axA.set_ylabel("loss-of-function variants", fontsize=9.5)
        axA.set_title("A · what the population already tested", fontsize=10,
                      color=INK, loc="left", pad=8)
        pctg = 100 * (1 - obs / exp) if exp else 0
        axA.text(0.5, 0.94, f"{pctg:.0f}% fewer than expected",
                 transform=axA.transAxes, ha="center", fontsize=9, color=vcolor)
    else:
        axA.text(0.5, 0.5, "obs/exp counts\nnot returned", ha="center", va="center",
                 fontsize=9, color="#57606a", transform=axA.transAxes)
        axA.set_xticks([])
    _style(axA)

    # --- Panel B: where that lands among all genes ---------------------------------
    # A continuous gradient, NOT a red/green split at a drawn line. An earlier version put
    # a boundary at the 35th percentile to represent the LOEUF < 0.35 rule; those are
    # different quantities and the band was simply in the wrong place — HMGCR's LOEUF of
    # 0.433 already sits at the 10th percentile, so LOEUF 0.35 is far below the 35th.
    # Rather than guess the crossing point, the axis shows the continuum it really is and
    # the threshold rule stays in the footer where it can be stated exactly.
    grad = np.linspace(0, 1, 256).reshape(1, -1)
    axB.imshow(grad, extent=(0, 100, 0, 1), aspect="auto", zorder=0, alpha=0.5,
               cmap=matplotlib.colors.LinearSegmentedColormap.from_list(
                   "c", ["#f7c9c4", "#fdf3e7", "#e8f1ea"]))

    if pct is not None:
        axB.scatter([pct], [0.52], s=210, color=vcolor, zorder=5,
                    edgecolor="white", linewidth=1.7)
        # Genes at the extremes are exactly the interesting ones, so keep their label
        # inside the axes rather than letting it run off the edge.
        lx = min(max(pct, 16), 84)
        axB.annotate(f"{protein}\nLOEUF {loeuf:.3g} · {pct}th percentile",
                     xy=(pct, 0.52), xytext=(lx, 0.82), ha="center", fontsize=10,
                     color=INK, arrowprops=dict(arrowstyle="-", color="#888", lw=1))
    else:
        axB.text(0.5, 0.52, f"LOEUF {loeuf:.3g} (percentile not returned)",
                 ha="center", transform=axB.transAxes, fontsize=10, color=INK)

    axB.text(2, 0.10, "more constrained\nsafety warning for inhibition",
             ha="left", fontsize=8.5, color=WARN)
    axB.text(98, 0.10, "less constrained — reassuring about inhibition,\n"
                       "but NOT evidence of efficacy",
             ha="right", fontsize=8.5, color="#3d6b52")
    axB.set_xlim(0, 100)
    axB.set_ylim(0, 1.0)
    axB.set_yticks([])
    axB.set_xlabel("LOEUF percentile across all genes  (0 = most constrained)", fontsize=9.5)
    axB.set_title("B · where this gene ranks", fontsize=10, color=INK, loc="left", pad=8)
    _style(axB)

    pli_txt = "pLI ~ 0" if isinstance(pli, (int, float)) and pli < 0.01 else \
              (f"pLI = {pli:.2f}" if isinstance(pli, (int, float)) else "pLI = NA")
    fig.suptitle(f"{protein} — population constraint: {verdict}   ·   {pli_txt}",
                 fontsize=12.5, color=INK, x=0.012, ha="left", y=0.985)
    fig.text(0.012, 0.055,
             f"Verdict rule: {g.get('thresholds_used', '')}. Constraint is a SAFETY signal "
             f"about inhibiting the target — never evidence that inhibiting it would work.",
             fontsize=7.4, color="#57606a")
    fig.text(0.012, 0.014, f"Source: {g.get('source_release', 'gnomAD')}",
             fontsize=7.4, color="#57606a")
    fig.tight_layout(rect=[0, 0.09, 1, 0.93])
    out = outdir / f"{protein}_constraint.png"
    fig.savefig(out, dpi=200)
    plt.close(fig)
    print(f"[constraint] wrote {out.name}  (LOEUF={loeuf:.3g}, pct={pct} -> {verdict})")
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
