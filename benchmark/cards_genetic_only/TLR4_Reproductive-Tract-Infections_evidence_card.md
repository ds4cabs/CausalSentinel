# Target Evidence Card — TLR4 × Reproductive Tract Infections

**Verdict:** INSUFFICIENT EVIDENCE — there is no direct genetic or causal evidence linking TLR4 to reproductive tract infections.

> **You asked about "Reproductive Tract Infections". This card scored MONDO_0006845 — male genital tuberculosis.** If those are not the same thing, every number below answers a different question.
> **The druggability row is about ChEMBL target "TLR4-MD2" (CHEMBL4106126),** matched by text search. If that is not the molecular target you meant, that row is about something else.

## Evidence concordance — classified by rule, not written by the model

- Sources: EpiGraphDB — no pQTL instrument · Europe PMC — NOT checked in this run · Semantic Scholar — NOT checked in this run · MR-KG — NOT checked in this run

## Evidence

| Evidence | Tool | Result |
|---|---|---|
| Causal effect (MR) — retrieved, not computed | `get_mr_result` | **not available** — no pQTL MR estimate for this protein in the resource (absence of an estimate is not evidence of no effect) |
| Target–disease association | `get_target_disease_evidence` | **not available** — TLR4 is not among the top 500 associated targets for MONDO_0006845 (male genital tuberculosis). This is a TRUNCATED LOOKUP, not proof of no association. Free-text inputs were resolved to ontology terms: 'TLR4' -> ENSG00000136869 (TLR4); 'Reproductive Tract Infections' -> MONDO_0006845 (male genital tuberculosis). Scores below describe THAT term, not the free-text phrase. |
| Protein context | `get_uniprot_dossier` | O00206 — Toll-like receptor 4; location: Cell membrane, Early endosome, Cell projection, ruffle |
| Known modulators / druggability | `get_chembl_modulators` | target CHEMBL4106126 — **0 known modulators in ChEMBL** |
| Clinical variants | `get_clinvar_variants` | 175 ClinVar records; 1 pathogenic in a sample of 30 |
| Population constraint / LoF tolerance | `get_gnomad_constraint` | pLI=0.00038, LOEUF=0.931 → LoF-tolerant |
| Extra genetic evidence | `get_gwas_catalog` | 110 unique SNPs from 196/196 association rows |
| Pharmacogenomics | `get_pharmgkb_drug_gene` | 6 clinical annotation(s) over 6 drug(s): Pertussis vaccines, Tumor necrosis factor alpha (TNF-alpha) inhibitors, folic acid, methotrexate +2 more — ClinPGx evidence level 3 (scale 1A strongest to 4 weakest) — e.g. rs5030728 (TLR4); Tumor necrosis factor alpha (TNF-alpha) inhibitors; Inflammatory Bowel Diseases (level 3 Eff |
| Clinical development record | `get_clinical_evidence` | _tool not called by the agent in this run_ |

## Caveats declared by the tools

- **`get_target_disease_evidence`** — TLR4 is not among the top 500 associated targets for MONDO_0006845 (male genital tuberculosis). This is a TRUNCATED LOOKUP, not proof of no association. Free-text inputs were resolved to ontology terms: 'TLR4' -> ENSG00000136869 (TLR4); 'Reproductive Tract Infections' -> MONDO_0006845 (male genital tuberculosis). Scores below describe THAT term, not the free-text phrase.
- **`get_mr_result`** — No pQTL-based MR estimate for TLR4 in the EpiGraphDB pQTL resource. This resource only covers proteins with usable plasma pQTL instruments. ABSENCE OF AN ESTIMATE IS NOT EVIDENCE OF NO EFFECT.
- **`get_chembl_modulators`** — ChEMBL target matched by text search on 'TLR4' and resolved to 'TLR4-MD2' — confirm this is the intended target.
- **`get_clinvar_variants`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 175 ClinVar records for this gene; it is a sample, not a rate.
- **`classify_evidence_concordance`** — Nothing to compare: fewer than two matched estimates.

## Reasoning

TLR4 encodes a well-characterized pattern recognition receptor involved in innate immunity and inflammatory signaling, but open targets evidence for reproductive tract infections resolved specifically to male genital tuberculosis with no recorded top-tier associations. No Mendelian randomization estimate is available for TLR4 on this disease, and ChEMBL lists no approved small-molecule modulators targeting the TLR4-MD2 complex. Furthermore, gnomAD constraint data indicates the gene is loss-of-function tolerant and GWAS associations map to various immune and inflammatory traits rather than direct reproductive pathogen outcomes.
```

## Sources

- `get_uniprot_dossier`: https://www.uniprot.org/uniprotkb/O00206 — _UniProt release 2026_02 (10-June-2026)_
- `get_mr_result`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `get_chembl_modulators`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4106126/ — _ChEMBL_37 (released 2026-05-01)_
- `get_clinvar_variants`: https://www.ncbi.nlm.nih.gov/clinvar/?term=TLR4%5Bgene%5D — _ClinVar build Build260818-0035.1_
- `get_gnomad_constraint`: https://gnomad.broadinstitute.org/gene/TLR4 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `get_gwas_catalog`: https://www.ebi.ac.uk/gwas/genes/TLR4 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `get_pharmgkb_drug_gene`: https://www.pharmgkb.org/search?query=TLR4 — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_

## Provenance

- Generated: 2026-08-21T15:50:20
- Model (reasoning text only): `gemini-flash-lite-latest`
- Tools invoked (9 calls): `get_uniprot_dossier`, `get_target_disease_evidence`, `get_mr_result`, `get_chembl_modulators`, `get_clinvar_variants`, `get_gnomad_constraint`, `get_gwas_catalog`, `get_pharmgkb_drug_gene`, `classify_evidence_concordance`
- Evidence table, caveats, sources and this block are rendered mechanically from tool return values. The model wrote only the Verdict sentence and the Reasoning paragraph, both checked against tool output by `validate_card.py`.
- No Mendelian randomization or colocalization is computed by this agent; MR estimates, where present, are retrieved from published work.
