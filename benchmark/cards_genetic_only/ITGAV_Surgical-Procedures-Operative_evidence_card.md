# Target Evidence Card — ITGAV × Surgical Procedures, Operative

**Verdict:** INSUFFICIENT EVIDENCE — there is no direct genetic or causal evidence linking ITGAV to surgical procedures.

> **The druggability row is about ChEMBL target "Integrin alpha-V" (CHEMBL3660),** matched by text search. If that is not the molecular target you meant, that row is about something else.

## Evidence concordance — classified by rule, not written by the model

- Sources: EpiGraphDB — no pQTL instrument · Europe PMC — NOT checked in this run · Semantic Scholar — NOT checked in this run · MR-KG — NOT checked in this run

## Evidence

| Evidence | Tool | Result |
|---|---|---|
| Causal effect (MR) — retrieved, not computed | `get_mr_result` | **not available** — no pQTL MR estimate for this protein in the resource (absence of an estimate is not evidence of no effect) |
| Target–disease association | `get_target_disease_evidence` | **not available** — Could not resolve target 'ITGAV' or disease 'Surgical Procedures, Operative'. |
| Protein context | `get_uniprot_dossier` | P06756 — Integrin alpha-V; location: Cell membrane, Cell junction, focal adhesion |
| Known modulators / druggability | `get_chembl_modulators` | 1 known modulators (BINDING AGENT) |
| Clinical variants | `get_clinvar_variants` | 237 ClinVar records; 3 pathogenic in a sample of 30 |
| Population constraint / LoF tolerance | `get_gnomad_constraint` | pLI=2.4e-10, LOEUF=0.64 → LoF-tolerant |
| Extra genetic evidence | `get_gwas_catalog` | 37 unique SNPs from 74/74 association rows |
| Pharmacogenomics | `get_pharmgkb_drug_gene` | **not available** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene). |
| Clinical development record | `get_clinical_evidence` | _tool not called by the agent in this run_ |

## Caveats declared by the tools

- **`get_target_disease_evidence`** — Could not resolve target 'ITGAV' or disease 'Surgical Procedures, Operative'.
- **`get_chembl_modulators`** — ChEMBL target matched by text search on 'ITGAV' and resolved to 'Integrin alpha-V' — confirm this is the intended target.
- **`get_mr_result`** — No pQTL-based MR estimate for ITGAV in the EpiGraphDB pQTL resource. This resource only covers proteins with usable plasma pQTL instruments. ABSENCE OF AN ESTIMATE IS NOT EVIDENCE OF NO EFFECT.
- **`get_clinvar_variants`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 237 ClinVar records for this gene; it is a sample, not a rate.
- **`get_pharmgkb_drug_gene`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`classify_evidence_concordance`** — Nothing to compare: fewer than two matched estimates.

## Reasoning

The target ITGAV (Integrin alpha-V) has no available Mendelian randomization estimate or Open Targets disease evidence for surgical procedures. Although GWAS catalog associations and ClinVar variants are documented for the gene, no pharmacogenomic annotations are present in PharmGKB, and disease association specific to this outcome is absent. Therefore, current data are insufficient to evaluate ITGAV as a target for this indication.

## Sources

- `get_uniprot_dossier`: https://www.uniprot.org/uniprotkb/P06756 — _UniProt release 2026_02 (10-June-2026)_
- `get_chembl_modulators`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3660/ — _ChEMBL_37 (released 2026-05-01)_
- `get_mr_result`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `get_clinvar_variants`: https://www.ncbi.nlm.nih.gov/clinvar/?term=ITGAV%5Bgene%5D — _ClinVar build Build260818-0035.1_
- `get_gnomad_constraint`: https://gnomad.broadinstitute.org/gene/ITGAV — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `get_gwas_catalog`: https://www.ebi.ac.uk/gwas/genes/ITGAV — _GWAS Catalog REST (live; release not exposed by this endpoint)_

## Provenance

- Generated: 2026-08-21T15:48:00
- Model (reasoning text only): `gemini-flash-lite-latest`
- Tools invoked (9 calls): `get_uniprot_dossier`, `get_target_disease_evidence`, `get_chembl_modulators`, `get_mr_result`, `get_clinvar_variants`, `get_gnomad_constraint`, `get_gwas_catalog`, `get_pharmgkb_drug_gene`, `classify_evidence_concordance`
- Evidence table, caveats, sources and this block are rendered mechanically from tool return values. The model wrote only the Verdict sentence and the Reasoning paragraph, both checked against tool output by `validate_card.py`.
- No Mendelian randomization or colocalization is computed by this agent; MR estimates, where present, are retrieved from published work.
