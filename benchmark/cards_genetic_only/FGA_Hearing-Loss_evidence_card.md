# Target Evidence Card — FGA × Hearing Loss

**Verdict:** INSUFFICIENT EVIDENCE — there is no genetic or causal evidence linking FGA to hearing loss.

> **You asked about "Hearing Loss". This card scored MONDO_0005365 — hearing loss disorder.** If those are not the same thing, every number below answers a different question.
> **The druggability row is about ChEMBL target "Fibrinogen" (CHEMBL2364709),** matched by text search. If that is not the molecular target you meant, that row is about something else.

## Evidence concordance — classified by rule, not written by the model

- Sources: EpiGraphDB — no pQTL instrument · Europe PMC — NOT checked in this run · Semantic Scholar — NOT checked in this run · MR-KG — NOT checked in this run

## Evidence

| Evidence | Tool | Result |
|---|---|---|
| Causal effect (MR) — retrieved, not computed | `get_mr_result` | **not available** — no pQTL MR estimate for this protein in the resource (absence of an estimate is not evidence of no effect) |
| Target–disease association | `get_target_disease_evidence` | **not available** — FGA is not among the top 500 associated targets for MONDO_0005365 (hearing loss disorder). This is a TRUNCATED LOOKUP, not proof of no association. Free-text inputs were resolved to ontology terms: 'FGA' -> ENSG00000171560 (FGA); 'Hearing Loss' -> MONDO_0005365 (hearing loss disorder). Scores below describe THAT term, not the free-text phrase. |
| Protein context | `get_uniprot_dossier` | P02671 — Fibrinogen alpha chain; location: Secreted |
| Known modulators / druggability | `get_chembl_modulators` | 5 known modulators (EXOGENOUS PROTEIN, HYDROLYTIC ENZYME, INHIBITOR) |
| Clinical variants | `get_clinvar_variants` | 392 ClinVar records; 1 pathogenic in a sample of 30 |
| Population constraint / LoF tolerance | `get_gnomad_constraint` | pLI=1.6e-07, LOEUF=1.43 → LoF-tolerant |
| Extra genetic evidence | `get_gwas_catalog` | 62 unique SNPs from 124/124 association rows |
| Pharmacogenomics | `get_pharmgkb_drug_gene` | **not available** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene). |
| Clinical development record | `get_clinical_evidence` | _tool not called by the agent in this run_ |

## Caveats declared by the tools

- **`get_target_disease_evidence`** — FGA is not among the top 500 associated targets for MONDO_0005365 (hearing loss disorder). This is a TRUNCATED LOOKUP, not proof of no association. Free-text inputs were resolved to ontology terms: 'FGA' -> ENSG00000171560 (FGA); 'Hearing Loss' -> MONDO_0005365 (hearing loss disorder). Scores below describe THAT term, not the free-text phrase.
- **`get_mr_result`** — No pQTL-based MR estimate for FGA in the EpiGraphDB pQTL resource. This resource only covers proteins with usable plasma pQTL instruments. ABSENCE OF AN ESTIMATE IS NOT EVIDENCE OF NO EFFECT.
- **`get_chembl_modulators`** — ChEMBL target matched by text search on 'FGA' and resolved to 'Fibrinogen' — confirm this is the intended target.
- **`get_clinvar_variants`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 392 ClinVar records for this gene; it is a sample, not a rate.
- **`get_pharmgkb_drug_gene`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`classify_evidence_concordance`** — Nothing to compare: fewer than two matched estimates.

## Reasoning

Open Targets shows no strong association between FGA and hearing loss, and no Mendelian randomization estimate is available in the EpiGraphDB pQTL resource for this target-disease pair. Although FGA has known functional modulators in ChEMBL and is tolerant to loss-of-function variations in gnomAD, these factors do not establish a disease-specific rationale. Without genetic or causal support for hearing loss, the target cannot be prioritized.

## Sources

- `get_uniprot_dossier`: https://www.uniprot.org/uniprotkb/P02671 — _UniProt release 2026_02 (10-June-2026)_
- `get_mr_result`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `get_chembl_modulators`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2364709/ — _ChEMBL_37 (released 2026-05-01)_
- `get_clinvar_variants`: https://www.ncbi.nlm.nih.gov/clinvar/?term=FGA%5Bgene%5D — _ClinVar build Build260818-0035.1_
- `get_gnomad_constraint`: https://gnomad.broadinstitute.org/gene/FGA — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `get_gwas_catalog`: https://www.ebi.ac.uk/gwas/genes/FGA — _GWAS Catalog REST (live; release not exposed by this endpoint)_

## Provenance

- Generated: 2026-08-21T15:49:51
- Model (reasoning text only): `gemini-flash-lite-latest`
- Tools invoked (9 calls): `get_uniprot_dossier`, `get_target_disease_evidence`, `get_mr_result`, `get_chembl_modulators`, `get_clinvar_variants`, `get_gnomad_constraint`, `get_gwas_catalog`, `get_pharmgkb_drug_gene`, `classify_evidence_concordance`
- Evidence table, caveats, sources and this block are rendered mechanically from tool return values. The model wrote only the Verdict sentence and the Reasoning paragraph, both checked against tool output by `validate_card.py`.
- No Mendelian randomization or colocalization is computed by this agent; MR estimates, where present, are retrieved from published work.
