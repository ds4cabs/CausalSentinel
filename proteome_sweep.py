"""Proteome sweep — build MR-feasibility dossiers for every searchable protein. No LLM,
no API key: every section is rendered mechanically from live public databases.

Run:
    python proteome_sweep.py --pilot            # 8 proteins chosen to hit all three tiers
    python proteome_sweep.py --proteins IL6R,LPA,HMGCR
    python proteome_sweep.py --all              # the full Tier-A universe (989 proteins)

THE THREE TIERS (the product's core idea)
-----------------------------------------
    Tier A  published pQTL-MR estimates exist (EpiGraphDB / Zheng 2020)  -> shown
    Tier B  a pQTL GWAS exists but no MR estimate here                   -> "you could run
            (instruments are derivable: prot-* datasets in IEU/EpiGraphDB)   this MR yourself"
    Tier C  no plasma pQTL found -> gene-level genetic evidence only, as an
            honest preview of what upstream signal exists

Each dossier also carries a PHENOME MAP: the diseases where this gene is a genetic locus
(Open Targets genetic_association, which aggregates GWAS common-variant and rare-variant
evidence), overlaid with the MR status of each disease. Rows with genetic signal and NO
MR estimate are the research-opportunity / comorbidity-hypothesis space.

Outputs (all under --outdir, default dossiers/):
    {PROTEIN}_dossier.md      human-readable dossier
    _cache/{PROTEIN}.json     verbatim tool returns (resume: cached proteins are skipped)
    master_index.csv          one row per protein - the cross-check table
"""
import argparse
import csv
import datetime
import json
import re
import sys
import time
from pathlib import Path

# The Windows console defaults to cp1252, which cannot print this repo's path (it contains
# Chinese characters) — the sweep once finished fine and then crashed on its own summary
# line. Force UTF-8 for stdout regardless of console codepage.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import requests

from tools.uniprot import get_uniprot_dossier
from tools.mr import get_mr_outcomes, _disease_match
from tools.opentargets import get_gene_phenome
from tools.chembl import get_chembl_modulators
from tools.clinvar import get_clinvar_variants
from tools.gnomad import get_gnomad_constraint
from tools.gwas import get_gwas_catalog, get_gwas_associations
from tools.pharmgkb import get_pharmgkb_drug_gene

HERE = Path(__file__).resolve().parent
EPI = "https://api.epigraphdb.org"
SLEEP = 0.25          # politeness between API-bearing steps
SAFE = re.compile(r"^[A-Za-z0-9_.-]+$")

PILOT = ["PCSK9", "IL6R", "LPA", "HMGCR", "PNPLA3", "TREM2", "ADAMTS13", "IL1RN"]


# ---------------------------------------------------------------- tier probes
def tier_a_universe() -> list:
    r = requests.get(f"{EPI}/pqtl/list/", params={"flag": "exposures"}, timeout=60)
    r.raise_for_status()
    return sorted({x["expID"] for x in r.json().get("results", [])})


def pqtl_datasets(symbol: str, accession: str | None) -> list:
    """Tier-B probe: prot-* pQTL GWAS datasets for this protein, matched by UniProt
    accession (trait names in the panels are protein names, not gene symbols) and by
    symbol as a fallback."""
    clauses = []
    if accession and SAFE.match(accession):
        clauses.append(f"g.note CONTAINS 'uniprot={accession}'")
    if SAFE.match(symbol):
        clauses.append(f"toLower(g.trait) = toLower('{symbol}')")
    if not clauses:
        return []
    q = ("MATCH (g:Gwas) WHERE g.id STARTS WITH 'prot-' AND (" + " OR ".join(clauses) +
         ") RETURN g.id AS id, g.trait AS trait, g.author AS author, g.year AS year LIMIT 10")
    try:
        r = requests.post(f"{EPI}/cypher", json={"query": q}, timeout=60)
        r.raise_for_status()
        return r.json().get("results", [])
    except requests.RequestException:
        return [{"error": "EpiGraphDB cypher probe failed"}]


# ---------------------------------------------------------------- formatting
def _p(x):
    if x is None:
        return "NA"
    try:
        return f"{x:.2e}" if x < 0.001 else f"{x:.3g}"
    except (TypeError, ValueError):
        return str(x)


def _n(x, nd=3):
    return "NA" if x is None else (f"{x:.{nd}g}" if isinstance(x, (int, float)) else str(x))


def mr_status_for(disease_name: str, outcomes: list) -> str:
    """Overlay: does any retrieved MR outcome match this phenome disease?"""
    best, best_m = None, 0.0
    for o in outcomes:
        m = _disease_match(disease_name, o.get("outcome") or "")
        if m > best_m:
            best_m, best = m, o
    if best and best_m >= 0.6:
        return (f"MR: beta={_n(best.get('beta'))}, p={_p(best.get('p_value'))} "
                f"({best.get('cis_or_trans')})")
    return "no MR -> candidate analysis"


# ---------------------------------------------------------------- per-protein
def sweep_one(symbol: str) -> dict:
    res, errors = {}, []

    def step(name, fn, *a, **k):
        try:
            out = fn(*a, **k)
        except Exception as e:                      # noqa: BLE001 - a sweep must not die
            out = {"error": f"{type(e).__name__}: {e}"}
        if isinstance(out, dict) and out.get("error"):
            errors.append(name)
        res[name] = out
        time.sleep(SLEEP)
        return out

    uni = step("uniprot", get_uniprot_dossier, symbol)
    accession = uni.get("accession") if uni.get("found") else None
    mr = step("mr_outcomes", get_mr_outcomes, symbol)
    res["pqtl_datasets"] = pqtl_datasets(symbol, accession)
    time.sleep(SLEEP)
    step("phenome", get_gene_phenome, symbol)
    step("chembl", get_chembl_modulators, symbol)
    step("gnomad", get_gnomad_constraint, symbol)
    step("gwas", get_gwas_catalog, symbol)
    step("gwas_traits", get_gwas_associations, symbol)
    step("clinvar", get_clinvar_variants, symbol)
    step("pharmgkb", get_pharmgkb_drug_gene, symbol)

    n_mr = mr.get("n_outcomes", 0) if isinstance(mr, dict) else 0
    has_pqtl = any("id" in d for d in res["pqtl_datasets"])
    tier = "A" if n_mr else ("B" if has_pqtl else "C")

    res["_meta"] = {
        "protein": symbol,
        "tier": tier,
        "errors": errors,
        "generated_at": datetime.datetime.now().isoformat(timespec="seconds"),
    }
    return res


TIER_TEXT = {
    "A": "Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).",
    "B": "No published MR estimate in this resource, BUT a pQTL GWAS exists - instruments are "
         "derivable, so a two-sample MR could be run. The upstream is waiting.",
    "C": "No plasma pQTL found (accession + symbol match). Standard plasma pQTL MR is not "
         "currently feasible; gene-level genetic evidence below is the honest preview.",
}


def render_dossier(res: dict) -> str:
    m = res["_meta"]
    sym, tier = m["protein"], m["tier"]
    uni = res.get("uniprot", {})
    mr = res.get("mr_outcomes", {})
    phen = res.get("phenome", {})
    L = [f"# Protein Dossier — {sym}" +
         (f" ({uni.get('protein_name')})" if uni.get("found") else ""), ""]
    L += [f"**MR feasibility tier: {tier}** — {TIER_TEXT[tier]}", ""]

    # 1 - published MR
    L += ["## 1. Published MR estimates (retrieved, not computed)", ""]
    outs = mr.get("outcomes") or []
    if outs:
        L += ["| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |", "|---|---|---|---|---|---|---|---|"]
        for o in outs[:12]:
            L.append(f"| {o.get('outcome')} | {_n(o.get('beta'))} | {_n(o.get('se'))} | "
                     f"{_p(o.get('p_value'))} | {o.get('method')} | {o.get('n_snp')} | "
                     f"{o.get('cis_or_trans')} | {_n(o.get('coloc_prob'))} |")
        if len(outs) > 12:
            L.append(f"| _...and {len(outs)-12} more outcomes (see JSON)_ | | | | | | | |")
    else:
        L.append("_None in the EpiGraphDB pQTL resource. Absence of an estimate is not "
                 "evidence of no effect._")
    L.append("")

    # 2 - instrument availability
    L += ["## 2. pQTL instrument availability (Tier-B probe)", ""]
    ds = [d for d in res.get("pqtl_datasets", []) if "id" in d]
    if ds:
        L += ["| Dataset | Trait | Author | Year |", "|---|---|---|---|"]
        for d in ds:
            L.append(f"| `{d['id']}` | {d.get('trait')} | {d.get('author')} | {str(d.get('year','')).split('.')[0]} |")
        if not outs:
            L.append("")
            L.append("> Instruments exist but no MR estimate is in this resource — "
                     "**a two-sample MR here is un-run work.**")
    else:
        L.append("_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt "
                 "accession and symbol)._")
    L.append("")

    # 3 - actual GWAS results (traits), the table a locus-hunter scans first
    gt = res.get("gwas_traits", {})
    L += ["## 3. GWAS Catalog results — traits with signal at this locus", ""]
    ttop = (gt.get("top_traits") or []) if isinstance(gt, dict) else []
    if ttop:
        L += [f"_{gt.get('n_associations_total')} association rows across "
              f"{gt.get('n_traits_total')} traits "
              f"({gt.get('n_genome_wide_significant')} genome-wide significant rows). "
              f"**Associations are loci, not causal claims**; the mapped gene at a locus "
              f"is not necessarily the effector gene._", "",
              "| Trait | best p | lead SNP | n assoc | study | MR status |",
              "|---|---|---|---|---|---|"]
        for t in ttop[:12]:
            L.append(f"| {t['trait'][:60]} | {t.get('best_p')} | {t.get('lead_snp')} | "
                     f"{t['n_associations']} | {t.get('study')} | "
                     f"{mr_status_for(t['trait'], outs)} |")
        if len(ttop) > 12:
            L.append(f"| _...and {gt.get('n_traits_total', 0)-12} more traits (see JSON)_ | | | | | |")
    else:
        L.append("_No GWAS Catalog associations mapped to this gene._")
    L.append("")

    # 4 - phenome map
    L += ["## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists", ""]
    rows = (phen.get("top_diseases") or []) if isinstance(phen, dict) else []
    grows = [r for r in rows if r.get("genetic_association")]
    if grows:
        L += [f"_Top diseases by Open Targets association "
              f"(of {phen.get('n_associated_diseases_total')} total); genetic_association "
              f"aggregates GWAS common-variant AND rare-variant evidence. "
              f"**Associations are loci, not causal claims.**_", "",
              "| Disease | genetic assoc. | overall | MR status |", "|---|---|---|---|"]
        for r in grows[:15]:
            L.append(f"| {r['disease']} | {r['genetic_association']} | {r['overall_score']} | "
                     f"{mr_status_for(r['disease'], outs)} |")
        n_opp = sum(1 for r in grows[:15]
                    if mr_status_for(r["disease"], outs).startswith("no MR"))
        L += ["", f"> **{n_opp} of the {min(len(grows),15)} genetically-supported diseases "
              f"above have no MR estimate in this resource** — that gap is the candidate-"
              f"analysis / comorbidity-hypothesis space."]
    else:
        L.append("_No genetically-associated diseases retrieved from Open Targets._")
    L.append("")

    # 5 - downstream annotation
    L += ["## 5. Downstream annotation (druggability & safety preview)", ""]
    ch, gn, gw, cv, pk = (res.get(k, {}) for k in ("chembl", "gnomad", "gwas", "clinvar", "pharmgkb"))
    L += ["| Layer | Result |", "|---|---|"]
    L.append("| ChEMBL druggability | " + (
        f"{ch.get('n_modulators')} known modulators ({ch.get('target_name')})" if ch.get("found")
        else "**not available** — no ChEMBL target (undrugged)") + " |")
    L.append("| gnomAD constraint | " + (
        f"pLI={_n(gn.get('pLI'),2)}, LOEUF={_n(gn.get('LOEUF'))} — {str(gn.get('interpretation','')).split(':')[0]}"
        if gn.get("found") else "not available") + " |")
    L.append("| GWAS Catalog | " + (
        f"{gw.get('n_unique_snps')} unique SNPs / {gw.get('total_association_rows_reported')} rows"
        + ("" if gw.get("sweep_complete") else " (LOWER BOUND)") if gw.get("found")
        else "no mapped SNPs") + " |")
    L.append("| ClinVar | " + (
        f"{cv.get('total_records')} records; {cv.get('pathogenic_in_sample')} pathogenic in sample of {cv.get('sample_size')}"
        if cv.get("found") else "no records") + " |")
    L.append("| PharmGKB/ClinPGx | " + (
        f"{pk.get('n_clinical_annotations')} clinical annotations across {pk.get('n_drugs')} drugs"
        if pk.get("found") else "no annotations") + " |")
    L.append("")

    # caveats + sources + provenance
    notes = [(k, v.get("note")) for k, v in res.items()
             if isinstance(v, dict) and v.get("note")]
    L += ["## Caveats declared by the tools", ""]
    L += [f"- **`{k}`** — {n}" for k, n in notes] or ["- _none_"]
    L += ["", "## Sources", ""]
    for k, v in res.items():
        if isinstance(v, dict) and v.get("url"):
            rel = f" — _{v.get('source_release')}_" if v.get("source_release") else ""
            L.append(f"- `{k}`: {v['url']}{rel}")
    L += ["", "## Provenance", "",
          f"- Generated: {m['generated_at']}  ·  Tier: {tier}",
          "- Fully mechanical: every cell above is rendered from tool return values. "
          "No language model wrote any part of this dossier.",
          "- MR estimates, where present, are retrieved from published work "
          "(EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.",
          f"- Tool errors this run: {', '.join(m['errors']) or 'none'}", ""]
    return "\n".join(L)


CSV_COLS = ["protein", "tier", "accession", "n_mr_outcomes", "top_mr_outcome", "top_mr_beta",
            "top_mr_p", "n_pqtl_datasets", "pqtl_ids", "n_genetic_diseases",
            "top_genetic_disease", "top_genetic_score", "n_opportunity_rows",
            "chembl_target", "n_modulators", "pLI", "LOEUF", "gwas_unique_snps",
            "n_gwas_traits", "n_gw_significant", "top_gwas_trait", "top_gwas_p",
            "clinvar_records", "pgx_annotations", "errors", "generated_at"]


def index_row(res: dict) -> dict:
    m, uni = res["_meta"], res.get("uniprot", {})
    mr, phen = res.get("mr_outcomes", {}), res.get("phenome", {})
    outs = mr.get("outcomes") or []
    top = outs[0] if outs else {}
    ds = [d for d in res.get("pqtl_datasets", []) if "id" in d]
    grows = [r for r in (phen.get("top_diseases") or []) if r.get("genetic_association")]
    n_opp = sum(1 for r in grows[:15] if mr_status_for(r["disease"], outs).startswith("no MR"))
    ch, gn = res.get("chembl", {}), res.get("gnomad", {})
    return {
        "protein": m["protein"], "tier": m["tier"],
        "accession": uni.get("accession"),
        "n_mr_outcomes": len(outs),
        "top_mr_outcome": top.get("outcome"), "top_mr_beta": top.get("beta"),
        "top_mr_p": top.get("p_value"),
        "n_pqtl_datasets": len(ds), "pqtl_ids": ";".join(d["id"] for d in ds),
        "n_genetic_diseases": len(grows),
        "top_genetic_disease": grows[0]["disease"] if grows else None,
        "top_genetic_score": grows[0]["genetic_association"] if grows else None,
        "n_opportunity_rows": n_opp,
        "chembl_target": ch.get("target_chembl_id"), "n_modulators": ch.get("n_modulators"),
        "pLI": gn.get("pLI"), "LOEUF": gn.get("LOEUF"),
        "gwas_unique_snps": res.get("gwas", {}).get("n_unique_snps"),
        "n_gwas_traits": res.get("gwas_traits", {}).get("n_traits_total"),
        "n_gw_significant": res.get("gwas_traits", {}).get("n_genome_wide_significant"),
        "top_gwas_trait": (res.get("gwas_traits", {}).get("top_traits") or [{}])[0].get("trait"),
        "top_gwas_p": (res.get("gwas_traits", {}).get("top_traits") or [{}])[0].get("best_p"),
        "clinvar_records": res.get("clinvar", {}).get("total_records"),
        "pgx_annotations": res.get("pharmgkb", {}).get("n_clinical_annotations"),
        "errors": ";".join(m["errors"]), "generated_at": m["generated_at"],
    }


def main() -> None:
    ap = argparse.ArgumentParser(description="Proteome sweep - 3-tier MR-feasibility dossiers")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--pilot", action="store_true", help="8 proteins covering all tiers")
    g.add_argument("--proteins", help="comma-separated symbols")
    g.add_argument("--file", help="file with one symbol per line")
    g.add_argument("--all", action="store_true", help="full Tier-A universe (989)")
    ap.add_argument("--outdir", default="dossiers")
    args = ap.parse_args()

    if args.pilot:
        targets = PILOT
    elif args.proteins:
        targets = [s.strip() for s in args.proteins.split(",") if s.strip()]
    elif args.file:
        targets = [l.strip() for l in Path(args.file).read_text(encoding="utf-8").splitlines()
                   if l.strip() and not l.startswith("#")]
    else:
        print("[sweep] fetching Tier-A universe from EpiGraphDB ...")
        targets = tier_a_universe()

    outdir = HERE / args.outdir
    cache = outdir / "_cache"
    cache.mkdir(parents=True, exist_ok=True)
    csv_path = outdir / "master_index.csv"
    seen_rows = {}
    if csv_path.exists():
        with open(csv_path, encoding="utf-8-sig", newline="") as fh:
            for row in csv.DictReader(fh):
                seen_rows[row["protein"]] = row

    t0 = time.time()
    tiers = {"A": 0, "B": 0, "C": 0}
    for i, sym in enumerate(targets, 1):
        cpath = cache / f"{sym}.json"
        if cpath.exists():
            res = json.loads(cpath.read_text(encoding="utf-8"))
        else:
            print(f"[{i}/{len(targets)}] {sym} ...", flush=True)
            res = sweep_one(sym)
            cpath.write_text(json.dumps(res, indent=1, ensure_ascii=False, default=str),
                             encoding="utf-8")
        (outdir / f"{sym}_dossier.md").write_text(render_dossier(res), encoding="utf-8")
        seen_rows[sym] = {k: ("" if v is None else v) for k, v in index_row(res).items()}
        tiers[res["_meta"]["tier"]] += 1
        if i % 10 == 0 or i == len(targets):
            with open(csv_path, "w", encoding="utf-8-sig", newline="") as fh:
                w = csv.DictWriter(fh, fieldnames=CSV_COLS)
                w.writeheader()
                for row in seen_rows.values():
                    w.writerow({k: row.get(k, "") for k in CSV_COLS})

    dt = time.time() - t0
    print(f"\n[sweep] done: {len(targets)} proteins in {dt/60:.1f} min "
          f"| Tier A={tiers['A']}  B={tiers['B']}  C={tiers['C']}")
    print(f"[sweep] dossiers: {outdir}  |  index: {csv_path}")


if __name__ == "__main__":
    main()
