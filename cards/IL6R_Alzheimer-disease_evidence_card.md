# Target Evidence Card — IL6R × Alzheimer disease

**Verdict:** NO-GO — No causal estimate or clinical trial evidence supports IL6R as a target for Alzheimer disease.

> **You asked about "Alzheimer disease". This card scored MONDO_0004975 — Alzheimer disease.** If those are not the same thing, every number below answers a different question.
> **The druggability row is about ChEMBL target "Interleukin-6 receptor subunit alpha" (CHEMBL2364155),** matched by text search. If that is not the molecular target you meant, that row is about something else.

## Evidence concordance — classified by rule, not written by the model

- Sources: EpiGraphDB — protein present, no estimate for THIS disease · Europe PMC — NOT checked in this run · Semantic Scholar — NOT checked in this run · MR-KG — NOT checked in this run

## Evidence

| Evidence | Tool | Result |
|---|---|---|
| Causal effect (MR) — retrieved, not computed | `get_mr_result` | **not available** — no pQTL MR estimate for this protein in the resource (absence of an estimate is not evidence of no effect) |
| Target–disease association | `get_target_disease_evidence` | overall score=0.369 (literature=0.482, genetic_association=0.583) |
| Protein context | `get_uniprot_dossier` | P08887 — Interleukin-6 receptor subunit alpha; location: Cell membrane, Secreted, Secreted |
| Known modulators / druggability | `get_chembl_modulators` | 4 known modulators (ANTAGONIST, INHIBITOR) |
| Clinical variants | `get_clinvar_variants` | 366 ClinVar records; 1 pathogenic in a sample of 30 |
| Population constraint / LoF tolerance | `get_gnomad_constraint` | pLI=7.9e-11, LOEUF=1.03 → LoF-tolerant |
| Extra genetic evidence | `get_gwas_catalog` | 150 unique SNPs from 368/368 association rows |
| Pharmacogenomics | `get_pharmgkb_drug_gene` | 3 clinical annotation(s) over 1 drug(s): tocilizumab — ClinPGx evidence level 3/4 (scale 1A strongest to 4 weakest) — e.g. rs12083537 (IL6R); tocilizumab; Arthritis, Rheumatoid (level 3 Efficacy) |
| Clinical development record | `get_clinical_evidence` | **no programme for this disease on record** — 5 drug programme(s) against this target for other diseases (max stage APPROVAL); context, not evidence about this disease |

## Caveats declared by the tools

- **`get_target_disease_evidence`** — Free-text inputs were resolved to ontology terms: 'IL6R' -> ENSG00000160712 (IL6R); 'Alzheimer disease' -> MONDO_0004975 (Alzheimer disease). Scores below describe THAT term, not the free-text phrase.
- **`get_mr_result`** — IL6R HAS pQTL MR estimates in this resource, but NONE matched the requested disease 'Alzheimer disease'. The other outcomes are listed for context only — do not present them as evidence about 'Alzheimer disease'.
- **`get_chembl_modulators`** — ChEMBL target matched by text search on 'IL6R' and resolved to 'Interleukin-6 receptor subunit alpha' — confirm this is the intended target.
- **`get_clinvar_variants`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 366 ClinVar records for this gene; it is a sample, not a rate.
- **`get_clinical_evidence`** — Phase and trial status mean trials EXIST, not that they worked — a COMPLETED phase-3 trial can be a failed one; only why-stopped fields carry failure information, and only approval carries a regulator's efficacy judgement. Registries lag press releases by a data release or more. All 5 drug programme(s) target OTHER diseases — their clinical stages are context about the drugs, not evidence about 'Alzheimer disease'.
- **`classify_evidence_concordance`** — Nothing to compare: fewer than two matched estimates.

## Reasoning

Open Targets shows only modest genetic and literature association scores for IL6R in Alzheimer disease, and no Mendelian randomization estimates were available for this specific disease outcome. Although multiple modulators and approved drugs exist for IL6R in other immune-mediated and inflammatory indications, none have advanced in clinical development for Alzheimer disease. Furthermore, the gene displays high tolerance to loss-of-function variants in gnomAD, but the absence of causal or clinical evidence in this indication precludes pursuit.

## Sources

- `get_uniprot_dossier`: https://www.uniprot.org/uniprotkb/P08887 — _UniProt release 2026_02 (10-June-2026)_
- `get_target_disease_evidence`: https://platform.opentargets.org/evidence/ENSG00000160712/MONDO_0004975 — _Open Targets data release 26.06_
- `get_mr_result`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `get_chembl_modulators`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2364155/ — _ChEMBL_37 (released 2026-05-01)_
- `get_clinvar_variants`: https://www.ncbi.nlm.nih.gov/clinvar/?term=IL6R%5Bgene%5D — _ClinVar build Build260818-0035.1_
- `get_gnomad_constraint`: https://gnomad.broadinstitute.org/gene/IL6R — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `get_gwas_catalog`: https://www.ebi.ac.uk/gwas/genes/IL6R — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `get_pharmgkb_drug_gene`: https://www.pharmgkb.org/search?query=IL6R — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `get_clinical_evidence`: https://platform.opentargets.org/target/ENSG00000160712 — _Open Targets data release 26.06; drugAndClinicalCandidates (ChEMBL + trial registries via Open Targets)_

## Provenance

- Generated: 2026-08-21T15:35:13
- Model (reasoning text only): `gemini-flash-lite-latest`
- Tools invoked (10 calls): `get_uniprot_dossier`, `get_target_disease_evidence`, `get_mr_result`, `get_chembl_modulators`, `get_clinvar_variants`, `get_gnomad_constraint`, `get_gwas_catalog`, `get_pharmgkb_drug_gene`, `get_clinical_evidence`, `classify_evidence_concordance`
- Evidence table, caveats, sources and this block are rendered mechanically from tool return values. The model wrote only the Verdict sentence and the Reasoning paragraph, both checked against tool output by `validate_card.py`.
- No Mendelian randomization or colocalization is computed by this agent; MR estimates, where present, are retrieved from published work.
