# Target Evidence Card — AGTR1 × Pneumonia

**Verdict:** INSUFFICIENT EVIDENCE — while AGTR1 has modulators and genetic associations, there is no causal Mendelian randomization estimate for pneumonia and overall genetic association is weak.

> **You asked about "Pneumonia". This card scored MONDO_0005249 — pneumonia.** If those are not the same thing, every number below answers a different question.
> **The druggability row is about ChEMBL target "Type-1 angiotensin II receptor" (CHEMBL227),** matched by text search. If that is not the molecular target you meant, that row is about something else.

## Evidence concordance — classified by rule, not written by the model

- Sources: EpiGraphDB — no pQTL instrument · Europe PMC — NOT checked in this run · Semantic Scholar — NOT checked in this run · MR-KG — NOT checked in this run

## Evidence

| Evidence | Tool | Result |
|---|---|---|
| Causal effect (MR) — retrieved, not computed | `get_mr_result` | **not available** — no pQTL MR estimate for this protein in the resource (absence of an estimate is not evidence of no effect) |
| Target–disease association | `get_target_disease_evidence` | overall score=0.289 (literature=0.279, animal_model=0.252, clinical=0.456) |
| Protein context | `get_uniprot_dossier` | P30556 — Type-1 angiotensin II receptor; location: Cell membrane |
| Known modulators / druggability | `get_chembl_modulators` | 19 known modulators (ANTAGONIST) |
| Clinical variants | `get_clinvar_variants` | 203 ClinVar records; 3 pathogenic in a sample of 30 |
| Population constraint / LoF tolerance | `get_gnomad_constraint` | pLI=2.1e-05, LOEUF=1.25 → LoF-tolerant |
| Extra genetic evidence | `get_gwas_catalog` | 17 unique SNPs from 34/34 association rows |
| Pharmacogenomics | `get_pharmgkb_drug_gene` | 15 clinical annotation(s) over 10 drug(s): Ace Inhibitors, Plain, Thiazides, plain, angiotensin II, atorvastatin +6 more — ClinPGx evidence level 3 (scale 1A strongest to 4 weakest) — e.g. rs5186 (AGTR1); Ace Inhibitors, Plain; Coronary Artery Disease (level 3 Efficacy, Toxicity) |
| Clinical development record | `get_clinical_evidence` | _tool not called by the agent in this run_ |

## Caveats declared by the tools

- **`get_target_disease_evidence`** — Free-text inputs were resolved to ontology terms: 'AGTR1' -> ENSG00000144891 (AGTR1); 'Pneumonia' -> MONDO_0005249 (pneumonia). Scores below describe THAT term, not the free-text phrase.
- **`get_chembl_modulators`** — ChEMBL target matched by text search on 'AGTR1' and resolved to 'Type-1 angiotensin II receptor' — confirm this is the intended target.
- **`get_mr_result`** — No pQTL-based MR estimate for AGTR1 in the EpiGraphDB pQTL resource. This resource only covers proteins with usable plasma pQTL instruments. ABSENCE OF AN ESTIMATE IS NOT EVIDENCE OF NO EFFECT.
- **`get_clinvar_variants`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 203 ClinVar records for this gene; it is a sample, not a rate.
- **`classify_evidence_concordance`** — Nothing to compare: fewer than two matched estimates.

## Reasoning

The target AGTR1 has multiple known modulators listed in ChEMBL and is tolerant to loss-of-function variants according to gnomAD. However, Open Targets shows only a modest association score for pneumonia, and no published Mendelian randomization estimate was available to establish a causal link with the disease. Although pharmacogenomic annotations and GWAS associations exist for the locus, they largely relate to cardiovascular and related traits rather than direct causal evidence for pneumonia. Therefore, additional mechanistic and clinical validation is required to support AGTR1 as a therapeutic target for this indication.

## Sources

- `get_uniprot_dossier`: https://www.uniprot.org/uniprotkb/P30556 — _UniProt release 2026_02 (10-June-2026)_
- `get_target_disease_evidence`: https://platform.opentargets.org/evidence/ENSG00000144891/MONDO_0005249 — _Open Targets data release 26.06_
- `get_chembl_modulators`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL227/ — _ChEMBL_37 (released 2026-05-01)_
- `get_mr_result`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `get_clinvar_variants`: https://www.ncbi.nlm.nih.gov/clinvar/?term=AGTR1%5Bgene%5D — _ClinVar build Build260818-0035.1_
- `get_gnomad_constraint`: https://gnomad.broadinstitute.org/gene/AGTR1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `get_gwas_catalog`: https://www.ebi.ac.uk/gwas/genes/AGTR1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `get_pharmgkb_drug_gene`: https://www.pharmgkb.org/search?query=AGTR1 — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_

## Provenance

- Generated: 2026-08-21T15:51:24
- Model (reasoning text only): `gemini-flash-lite-latest`
- Tools invoked (9 calls): `get_uniprot_dossier`, `get_target_disease_evidence`, `get_chembl_modulators`, `get_mr_result`, `get_clinvar_variants`, `get_gnomad_constraint`, `get_gwas_catalog`, `get_pharmgkb_drug_gene`, `classify_evidence_concordance`
- Evidence table, caveats, sources and this block are rendered mechanically from tool return values. The model wrote only the Verdict sentence and the Reasoning paragraph, both checked against tool output by `validate_card.py`.
- No Mendelian randomization or colocalization is computed by this agent; MR estimates, where present, are retrieved from published work.
