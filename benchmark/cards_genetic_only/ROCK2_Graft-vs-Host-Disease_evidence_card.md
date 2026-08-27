# Target Evidence Card — ROCK2 × Graft vs Host Disease

**Verdict:** GO — Strong clinical evidence linking ROCK2 to graft versus host disease supports its pursuit as a therapeutic target.

> **You asked about "Graft vs Host Disease". This card scored MONDO_0013730 — graft versus host disease.** If those are not the same thing, every number below answers a different question.
> **The druggability row is about ChEMBL target "Rho-associated protein kinase 2" (CHEMBL2973),** matched by text search. If that is not the molecular target you meant, that row is about something else.

## Evidence concordance — classified by rule, not written by the model

- Sources: EpiGraphDB — no pQTL instrument · Europe PMC — NOT checked in this run · Semantic Scholar — NOT checked in this run · MR-KG — NOT checked in this run

## Evidence

| Evidence | Tool | Result |
|---|---|---|
| Causal effect (MR) — retrieved, not computed | `get_mr_result` | **not available** — no pQTL MR estimate for this protein in the resource (absence of an estimate is not evidence of no effect) |
| Target–disease association | `get_target_disease_evidence` | overall score=0.559 (literature=0.135, clinical=0.912) |
| Protein context | `get_uniprot_dossier` | O75116 — Rho-associated protein kinase 2; location: Cytoplasm, Cell membrane, Nucleus, Cytoplasm, cytoskeleton,  |
| Known modulators / druggability | `get_chembl_modulators` | 1 known modulators (INHIBITOR) |
| Clinical variants | `get_clinvar_variants` | 210 ClinVar records; 1 pathogenic in a sample of 30 |
| Population constraint / LoF tolerance | `get_gnomad_constraint` | pLI=1, LOEUF=0.387 → LoF-INTOLERANT (handle with care) |
| Extra genetic evidence | `get_gwas_catalog` | 54 unique SNPs from 106/106 association rows |
| Pharmacogenomics | `get_pharmgkb_drug_gene` | **not available** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene). |
| Clinical development record | `get_clinical_evidence` | _tool not called by the agent in this run_ |

## Caveats declared by the tools

- **`get_target_disease_evidence`** — Free-text inputs were resolved to ontology terms: 'ROCK2' -> ENSG00000134318 (ROCK2); 'Graft vs Host Disease' -> MONDO_0013730 (graft versus host disease). Scores below describe THAT term, not the free-text phrase.
- **`get_mr_result`** — No pQTL-based MR estimate for ROCK2 in the EpiGraphDB pQTL resource. This resource only covers proteins with usable plasma pQTL instruments. ABSENCE OF AN ESTIMATE IS NOT EVIDENCE OF NO EFFECT.
- **`get_chembl_modulators`** — ChEMBL target matched by text search on 'ROCK2' and resolved to 'Rho-associated protein kinase 2' — confirm this is the intended target.
- **`get_clinvar_variants`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 210 ClinVar records for this gene; it is a sample, not a rate.
- **`get_pharmgkb_drug_gene`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`classify_evidence_concordance`** — Nothing to compare: fewer than two matched estimates.

## Reasoning

Open Targets shows a substantial overall association score for ROCK2 with graft versus host disease, driven heavily by clinical evidence. ChEMBL identifies known modulators against the target, confirming its pharmacological tractability. However, gnomAD constraint metrics indicate that ROCK2 is highly intolerant to loss-of-function variants, signaling potential safety considerations for inhibition. No Mendelian randomization estimate or PharmGKB annotation was available for this gene-disease pair.

## Sources

- `get_uniprot_dossier`: https://www.uniprot.org/uniprotkb/O75116 — _UniProt release 2026_02 (10-June-2026)_
- `get_target_disease_evidence`: https://platform.opentargets.org/evidence/ENSG00000134318/MONDO_0013730 — _Open Targets data release 26.06_
- `get_mr_result`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `get_chembl_modulators`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2973/ — _ChEMBL_37 (released 2026-05-01)_
- `get_clinvar_variants`: https://www.ncbi.nlm.nih.gov/clinvar/?term=ROCK2%5Bgene%5D — _ClinVar build Build260818-0035.1_
- `get_gnomad_constraint`: https://gnomad.broadinstitute.org/gene/ROCK2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `get_gwas_catalog`: https://www.ebi.ac.uk/gwas/genes/ROCK2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_

## Provenance

- Generated: 2026-08-21T15:48:54
- Model (reasoning text only): `gemini-flash-lite-latest`
- Tools invoked (9 calls): `get_uniprot_dossier`, `get_target_disease_evidence`, `get_mr_result`, `get_chembl_modulators`, `get_clinvar_variants`, `get_gnomad_constraint`, `get_gwas_catalog`, `get_pharmgkb_drug_gene`, `classify_evidence_concordance`
- Evidence table, caveats, sources and this block are rendered mechanically from tool return values. The model wrote only the Verdict sentence and the Reasoning paragraph, both checked against tool output by `validate_card.py`.
- No Mendelian randomization or colocalization is computed by this agent; MR estimates, where present, are retrieved from published work.
