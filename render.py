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
    ("get_clinical_evidence", "Clinical development record"),
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
    if tool == "get_clinical_evidence":
        m = r.get("drugs_for_this_disease") or []
        if m:
            top = m[0]
            # Counts and denominators from the SAME universe: this-disease reports only.
            # A drug's all-indication stop count next to a this-disease report count is
            # exactly the mixed-denominator cell this project treats as a cardinal sin.
            head = (f"max stage for THIS disease: **{r.get('max_stage_this_disease') or 'none on record'}** "
                    f"— e.g. {top.get('drug')} ({top.get('max_stage_this_disease') or 'no stage on record'}, "
                    f"{top.get('n_reports_this_disease')} trial report(s) for this disease"
                    + (f", {top.get('n_stop_this_disease')} of them with a stop reason"
                       if top.get("n_stop_this_disease") else "")
                    + ")")
            extra = f"; +{len(m) - 1} more drug(s) for this disease" if len(m) > 1 else ""
            return (head + extra +
                    "  \n_stages mean trials exist, not that they worked_")
        n = r.get("n_drug_programmes") or 0
        return (f"**no programme for this disease on record** — {n} drug programme(s) "
                f"against this target for other diseases (max stage "
                f"{r.get('max_stage_any_disease')}); context, not evidence about this disease")
    if tool == "get_pharmgkb_drug_gene":
        # Render the CONTENT, not just the counts. An earlier version printed
        # "2 clinical annotations across 6 drugs (level 3: 2)", which is accurate and
        # tells a reader nothing: it names no drug and never says what the level scale
        # means. The tool returns the drug names and the full annotation strings — the
        # renderer was discarding them. "Rendered mechanically" must not come to mean
        # "rendered as counts"; it means the reader sees what the tool actually said.
        n = r.get("n_clinical_annotations")
        drugs = [d for d in (r.get("drugs") or []) if d]
        shown = ", ".join(drugs[:4]) + (f" +{len(drugs) - 4} more" if len(drugs) > 4 else "")
        lv = r.get("evidence_level_counts") or {}
        # ClinPGx levels run 1A (strongest) to 4 (weakest); saying "level 3" without
        # that anchor is jargon the reader cannot weigh.
        lvs = "/".join(str(k) for k in lv) if lv else None
        parts = [f"{n} clinical annotation(s) over {len(drugs)} drug(s): {shown}"] if drugs             else [f"{n} clinical annotation(s)"]
        if lvs:
            parts.append(f"ClinPGx evidence level {lvs} (scale 1A strongest to 4 weakest)")
        ex = (r.get("examples") or [{}])[0].get("annotation")
        if ex:
            parts.append(f"e.g. {ex[:110]}")
        return " — ".join(parts)
    return str(r)[:160]


def _direction_block(protein: str, results: dict) -> list:
    """State the MR direction MECHANICALLY, from the sign of beta.

    This block exists because of a real failure. For IL6R x coronary heart disease the
    ledger holds beta = -0.0442 with the plasma IL6R protein as the exposure, i.e. higher
    protein -> lower disease. The model nonetheless wrote that the evidence supported
    IL6R *inhibition* — the opposite intervention — because that is the conclusion in the
    literature it had memorised. The number it quoted was correct; the direction was not,
    and no token-level check can see that.

    So the direction sentence is no longer the model's to write.
    """
    mr = results.get("get_mr_result") or {}
    ms = (mr.get("matched_disease_estimates") or []) if isinstance(mr, dict) else []
    if not ms:
        return []
    out = ["## MR direction — rendered from the ledger, not written by the model", ""]
    for m in ms[:3]:
        beta = m.get("beta")
        if beta is None:
            continue
        way = "HIGHER" if beta > 0 else "LOWER"
        out.append(
            f"- Genetically-predicted **higher plasma {protein}** is associated with "
            f"**{way} {m.get('outcome')}** "
            f"(beta {beta:+.4g}, se {_num(m.get('se'))}, {_fmt_p(m.get('p_value'))}; "
            f"{m.get('method')}, n_snp {m.get('n_snp')}, instrument "
            f"{m.get('instrument_rsid')}, {m.get('cis_or_trans')})."
        )
        weak = [k for k, v in (("Steiger direction", m.get("steiger_direction_ok")),
                               ("colocalization", m.get("coloc_prob")),
                               ("LD check", m.get("ld_check")))
                if v in (None, "NA", "")]
        if weak:
            out.append(f"  - Not available for this estimate: {', '.join(weak)}.")
        if m.get("n_snp") == 1:
            out.append("  - Single-instrument Wald ratio: no heterogeneity or pleiotropy "
                       "test is possible.")
    out += [
        "",
        f"> **The exposure is {protein} protein abundance, not a drug.** This run retrieved "
        f"no evidence about what pharmacological inhibition or activation of {protein} does. "
        f"Turning the direction above into a drug direction needs a mechanism this run did "
        f"not retrieve.",
        "",
    ]
    return out


def _concordance_block(results: dict) -> list:
    """Summarize the source-coverage / concordance classification, mechanically.

    Renders only when the classifier ran. Its job on the card is to stop two specific
    misreadings before they start: "two estimates agree" being read as replication when
    both come from one study, and a source that was never queried being read as a source
    that came back empty.
    """
    conc = results.get("classify_evidence_concordance") or {}
    if not isinstance(conc, dict) or not conc.get("retrieval_coverage"):
        return []
    cov = conc["retrieval_coverage"]
    ec = conc.get("estimate_concordance") or {}
    out = ["## Evidence concordance — classified by rule, not written by the model", ""]
    pretty = {"pair_matched": "estimate found",
              "instrument_exists_disease_unmatched":
                  "protein present, no estimate for THIS disease",
              "no_instrument": "no pQTL instrument", "error": "request failed",
              "present": "returned records", "queried_empty": "queried, nothing found",
              "not_checked": "NOT checked in this run"}
    out.append("- Sources: " + " · ".join(
        f"{name} — {pretty.get(state, state)}"
        for name, state in (("EpiGraphDB", cov.get("epigraphdb")),
                            ("Europe PMC", cov.get("europe_pmc")),
                            ("Semantic Scholar", cov.get("semantic_scholar")),
                            ("MR-KG", cov.get("mr_kg")))))
    n = ec.get("n_estimates_compared", 0)
    if n >= 2:
        label = {"agree": "estimates AGREE in sign",
                 "sign_consistent_non_independent":
                     "estimates agree in sign but are NOT independent (shared study/outcome "
                     "GWAS) — this is not replication",
                 "conflict": "estimates CONFLICT in sign — check what each analyte "
                             "actually measures before explaining why",
                 "not_assessable": "direction agreement NOT assessable — at least one "
                                   "estimate carries no usable beta"}.get(
            ec.get("label") or ec.get("direction"), ec.get("direction"))
        out.append(f"- {n} matched estimates: {label}. Validation depth per estimate "
                   f"(0-4): {ec.get('validation_depth_per_estimate')}.")
    elif n == 1:
        out.append(f"- Single matched estimate; validation depth "
                   f"{ec.get('best_validation_depth', 0)} of 4 "
                   f"(multi-SNP / Steiger / coloc / LD check).")
    out.append("")
    return out


def _banner_block(results: dict, disease: str = "") -> list:
    """Promote silent resolution steps to the top of the card, where they are visible.

    Shows BOTH sides of every substitution. An earlier version printed only what the text
    was resolved TO, which cannot be audited: a reader who does not already know what was
    typed has no way to see that "high cholesterol" became an HPO phenotype term rather
    than a disease term. Naming the input next to the output is the whole point.
    """
    out = []
    ot = results.get("get_target_disease_evidence") or {}
    if isinstance(ot, dict):
        res = ot.get("resolved") or {}
        efo = ot.get("efo_id") or res.get("efo_id")
        dname = ot.get("resolved_disease_name") or res.get("disease_name")
        if efo:
            asked = f'"{disease}"' if disease else "the disease you gave"
            out.append(f"> **You asked about {asked}. This card scored {efo} — {dname}.** "
                       f"If those are not the same thing, every number below answers a "
                       f"different question.")
    ch = results.get("get_chembl_modulators") or {}
    if isinstance(ch, dict) and ch.get("found") and ch.get("target_name"):
        out.append(f"> **The druggability row is about ChEMBL target "
                   f"\"{ch.get('target_name')}\" ({ch.get('target_chembl_id')}),** matched by "
                   f"text search. If that is not the molecular target you meant, that row is "
                   f"about something else.")
    return (out + [""]) if out else []


def render_card(protein: str, disease: str, ledger, reasoning_md: str,
                verdict_line: str, model: str) -> str:
    results = ledger.results_by_tool()
    now = datetime.datetime.now().isoformat(timespec="seconds")

    lines = [f"# Target Evidence Card — {protein} × {disease}", ""]
    lines += [f"**Verdict:** {verdict_line.strip()}", ""]
    lines += _banner_block(results, disease)
    lines += _direction_block(protein, results)
    lines += _concordance_block(results)

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
