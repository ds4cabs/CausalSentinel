"""Deterministic card rendering — every number and every caveat comes from tool output.

The division of labour this file enforces:

    tool JSON  ->  evidence table, caveats, sources, provenance    (THIS FILE, mechanical)
    model      ->  the Reasoning paragraph only                    (prose, then validated)

Nothing the model writes can change a number in the table, and no tool-declared `note`
can be dropped, because the model is never in that path.
"""
import datetime

# One row per tool, in the order a target is actually reasoned about.
ROWS = [
    ("get_mr_result", "Causal effect (MR) — retrieved, not computed"),
    ("get_target_disease_evidence", "Target–disease association"),
    ("get_uniprot_dossier", "Protein context"),
    ("get_chembl_modulators", "Known modulators / druggability"),
    ("get_clinvar_variants", "Clinical variants"),
    ("get_gnomad_constraint", "Population constraint / LoF tolerance"),
    ("get_gwas_catalog", "Extra genetic evidence"),
    ("get_pharmgkb_drug_gene", "Pharmacogenomics"),
]


def _fmt_p(p):
    if p is None:
        return "p=NA"
    try:
        return f"p={p:.2e}" if p < 0.001 else f"p={p:.3g}"
    except (TypeError, ValueError):
        return f"p={p}"


def _num(x, nd=3):
    if x is None:
        return "NA"
    if isinstance(x, (int, float)):
        return f"{x:.{nd}g}"
    return str(x)


def _cell_mr(r: dict) -> str:
    if r.get("error"):
        return f"**tool error** — {r['error'][:120]}"
    if not r.get("found"):
        return ("**not available** — no pQTL MR estimate for this protein in the resource "
                "(absence of an estimate is not evidence of no effect)")
    ms = r.get("matched_disease_estimates") or []
    if not ms:
        return (f"**no estimate for this disease** — protein has "
                f"{r.get('n_outcomes_available')} outcomes in the resource, none matching")
    m = ms[0]
    bits = [
        f"beta={_num(m.get('beta'))}",
        f"se={_num(m.get('se'))}",
        _fmt_p(m.get("p_value")),
        f"{m.get('method')}",
        f"n_snp={m.get('n_snp')}",
        f"{m.get('cis_or_trans')} instrument",
    ]
    coloc = m.get("coloc_prob")
    bits.append(f"coloc={_num(coloc)}" if coloc is not None else "coloc=not available")
    extra = f" (+{len(ms)-1} more matched)" if len(ms) > 1 else ""
    return f"outcome: {m.get('outcome')} — " + ", ".join(bits) + extra + \
           "  \n_retrieved from published MR; not computed here_"


def _cell_generic(tool: str, r: dict) -> str:
    if not isinstance(r, dict):
        return f"unexpected result type: {type(r).__name__}"
    if r.get("error"):
        return f"**tool error** — {str(r['error'])[:140]}"
    if r.get("found") is False:
        return "**not available** — " + (r.get("note") or "no record returned")

    if tool == "get_target_disease_evidence":
        ds = r.get("datatype_scores") or {}
        top = ", ".join(f"{k}={_num(v)}" for k, v in list(ds.items())[:4])
        return f"overall score={_num(r.get('overall_score'))} ({top})"
    if tool == "get_uniprot_dossier":
        loc = ", ".join(r.get("subcellular_location") or [])[:60]
        return f"{r.get('accession')} — {str(r.get('protein_name'))[:70]}" + (f"; location: {loc}" if loc else "")
    if tool == "get_chembl_modulators":
        n = r.get("n_modulators", 0)
        if not n:
            return f"target {r.get('target_chembl_id')} — **0 known modulators in ChEMBL**"
        acts = {m.get("action") for m in (r.get("modulators") or []) if m.get("action")}
        return f"{n} known modulators ({', '.join(sorted(a for a in acts if a))[:70]})"
    if tool == "get_clinvar_variants":
        return (f"{r.get('total_records')} ClinVar records; "
                f"{r.get('pathogenic_in_sample')} pathogenic in a sample of {r.get('sample_size')}")
    if tool == "get_gnomad_constraint":
        pli, loeuf = r.get("pLI"), r.get("LOEUF")
        verdict = "LoF-INTOLERANT (handle with care)" if (
            (pli is not None and pli > 0.9) or (loeuf is not None and loeuf < 0.35)
        ) else "LoF-tolerant"
        return f"pLI={_num(pli, 2)}, LOEUF={_num(loeuf, 3)} → {verdict}"
    if tool == "get_gwas_catalog":
        tot = r.get("total_association_rows_reported")
        done = r.get("sweep_complete")
        return (f"{r.get('n_unique_snps')} unique SNPs from {r.get('n_association_rows')}"
                f"/{tot} association rows"
                + ("" if done else " — **incomplete sweep, lower bound**"))
    if tool == "get_pharmgkb_drug_gene":
        lv = r.get("evidence_level_counts") or {}
        lvs = ", ".join(f"level {k}: {v}" for k, v in lv.items())
        return (f"{r.get('n_clinical_annotations')} clinical annotations across "
                f"{r.get('n_drugs')} drugs" + (f" ({lvs})" if lvs else ""))
    return str(r)[:160]


def render_card(protein: str, disease: str, ledger, reasoning_md: str,
                verdict_line: str, model: str) -> str:
    results = ledger.results_by_tool()
    now = datetime.datetime.now().isoformat(timespec="seconds")

    lines = [f"# Target Evidence Card — {protein} × {disease}", ""]
    lines += [f"**Verdict:** {verdict_line.strip()}", ""]

    # ---- evidence table (mechanical) ----
    lines += ["## Evidence", "", "| Evidence | Tool | Result |", "|---|---|---|"]
    for tool, label in ROWS:
        r = results.get(tool)
        if r is None:
            cell = "_tool not called by the agent in this run_"
        elif tool == "get_mr_result":
            cell = _cell_mr(r)
        else:
            cell = _cell_generic(tool, r)
        lines.append(f"| {label} | `{tool}` | {cell} |")
    lines.append("")

    # ---- caveats (mechanical: every tool-declared note, verbatim) ----
    notes = ledger.notes()
    lines += ["## Caveats declared by the tools", ""]
    if notes:
        for tool, note in notes:
            lines.append(f"- **`{tool}`** — {note}")
    else:
        lines.append("- _No tool declared a caveat in this run._")
    lines.append("")

    # ---- reasoning (the model's only writing surface) ----
    lines += ["## Reasoning", "", reasoning_md.strip(), ""]

    # ---- sources (mechanical) ----
    lines += ["## Sources", ""]
    srcs = ledger.sources()
    if srcs:
        for tool, url, release in srcs:
            rel = f" — _{release}_" if release else ""
            lines.append(f"- `{tool}`: {url}{rel}")
    else:
        lines.append("- _No tool returned a source URL._")
    lines.append("")

    # ---- provenance (mechanical) ----
    called = ledger.called()
    lines += [
        "## Provenance",
        "",
        f"- Generated: {now}",
        f"- Model (reasoning text only): `{model}`",
        f"- Tools invoked ({len(called)} calls): {', '.join(f'`{c}`' for c in called) or 'none'}",
        "- Evidence table, caveats, sources and this block are rendered mechanically from "
        "tool return values. The model wrote only the Verdict sentence and the Reasoning "
        "paragraph, both checked against tool output by `validate_card.py`.",
        "- No Mendelian randomization or colocalization is computed by this agent; MR "
        "estimates, where present, are retrieved from published work.",
        "",
    ]
    return "\n".join(lines)
