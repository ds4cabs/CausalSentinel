# Target Evidence Card — LPA × coronary heart disease

**Verdict:** GO — LPA demonstrates strong causal genetic evidence, high LoF tolerance, and active phase 3 clinical development for coronary-related disorders.

> **You asked about "coronary heart disease". This card scored MONDO_0005010 — coronary artery disorder.** If those are not the same thing, every number below answers a different question.
> **The druggability row is about ChEMBL target "LPA mRNA" (CHEMBL4662965),** matched by text search. If that is not the molecular target you meant, that row is about something else.

## MR direction — rendered from the ledger, not written by the model

- Genetically-predicted **higher plasma LPA** is associated with **HIGHER Coronary heart disease** (beta +0.2523, se 0.0193, p=5.39e-39; Wald ratio, n_snp 1, instrument rs55730499, cis).
  - Not available for this estimate: colocalization.
  - Single-instrument Wald ratio: no heterogeneity or pleiotropy test is possible.

> **The exposure is LPA protein abundance, not a drug.** This run retrieved no evidence about what pharmacological inhibition or activation of LPA does. Turning the direction above into a drug direction needs a mechanism this run did not retrieve.

## Evidence concordance — classified by rule, not written by the model

- Sources: EpiGraphDB — estimate found · Europe PMC — NOT checked in this run · Semantic Scholar — NOT checked in this run · MR-KG — NOT checked in this run
- Single matched estimate; sensitivity checks reported: 2 of 3 (multi-SNP / Steiger / shared-variant [coloc or LD check]).

## Evidence

| Evidence | Tool | Result |
|---|---|---|
| Causal effect (MR) — retrieved, not computed | `get_mr_result` | outcome: Coronary heart disease — beta=0.252, se=0.0193, p=5.39e-39, Wald ratio, n_snp=1, cis instrument, coloc=not available  
_retrieved from published MR; not computed here_ |
| Target–disease association | `get_target_disease_evidence` | overall score=0.576 (literature=0.977, genetic_association=0.898, clinical=0.0061) |
| Protein context | `get_uniprot_dossier` | P08519 — Apolipoprotein(a); location: Not annotated. |
| Known modulators / druggability | `get_chembl_modulators` | 2 known modulators (ANTISENSE INHIBITOR, RNAI INHIBITOR) |
| Clinical variants | `get_clinvar_variants` | 365 ClinVar records; 2 pathogenic in a sample of 30 |
| Population constraint / LoF tolerance | `get_gnomad_constraint` | pLI=2.1e-68, LOEUF=1.13 → LoF-tolerant |
| Extra genetic evidence | `get_gwas_catalog` | 259 unique SNPs from 692/692 association rows |
| Pharmacogenomics | `get_pharmgkb_drug_gene` | 3 clinical annotation(s) over 2 drug(s): HMG-CoA reductase inhibitors, rosuvastatin — ClinPGx evidence level 3 (scale 1A strongest to 4 weakest) — e.g. rs10455872 (LPA); rosuvastatin (level 3 Efficacy) |
| Clinical development record | `get_clinical_evidence` | max stage for THIS disease: **PHASE_3** — e.g. PELACARSEN (PHASE_3, 9 trial report(s) for this disease, 1 of them with a stop reason); +1 more drug(s) for this disease  
_stages mean trials exist, not that they worked_ |

## Caveats declared by the tools

- **`get_target_disease_evidence`** — Free-text inputs were resolved to ontology terms: 'LPA' -> ENSG00000198670 (LPA); 'coronary heart disease' -> MONDO_0005010 (coronary artery disorder). Scores below describe THAT term, not the free-text phrase.
- **`get_mr_result`** — Estimates RETRIEVED from published pQTL MR, not computed by this agent. Check cis_or_trans (cis instruments are less pleiotropy-prone), steiger_direction_ok, and coloc_prob before treating this as causal; coloc_prob=null means colocalization was not available for this pair.
- **`get_chembl_modulators`** — ChEMBL target matched by text search on 'LPA' and resolved to 'LPA mRNA' — confirm this is the intended target.
- **`get_clinvar_variants`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 365 ClinVar records for this gene; it is a sample, not a rate.
- **`get_clinical_evidence`** — Phase and trial status mean trials EXIST, not that they worked — a COMPLETED phase-3 trial can be a failed one; only why-stopped fields carry failure information, and only approval carries a regulator's efficacy judgement. Registries lag press releases by a data release or more.
- **`classify_evidence_concordance`** — Nothing to compare: fewer than two matched estimates.

## Reasoning

Retrieved Mendelian randomization estimates link LPA to coronary heart disease with strong statistical support, corroborated by hundreds of GWAS associations and a high genetic association score in Open Targets. The gene exhibits loss-of-function tolerance in gnomAD, suggesting safety upon inhibition, and has active phase 3 clinical candidates such as pelacarsen and olpasiran targeted against it.

## Sources

- `get_uniprot_dossier`: https://www.uniprot.org/uniprotkb/P08519 — _UniProt release 2026_02 (10-June-2026)_
- `get_target_disease_evidence`: https://platform.opentargets.org/evidence/ENSG00000198670/MONDO_0005010 — _Open Targets data release 26.06_
- `get_mr_result`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `get_chembl_modulators`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4662965/ — _ChEMBL_37 (released 2026-05-01)_
- `get_clinvar_variants`: https://www.ncbi.nlm.nih.gov/clinvar/?term=LPA%5Bgene%5D — _ClinVar build Build260823-0900.1_
- `get_gnomad_constraint`: https://gnomad.broadinstitute.org/gene/LPA — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `get_gwas_catalog`: https://www.ebi.ac.uk/gwas/genes/LPA — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `get_pharmgkb_drug_gene`: https://www.pharmgkb.org/search?query=LPA — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `get_clinical_evidence`: https://platform.opentargets.org/target/ENSG00000198670 — _Open Targets data release 26.06; drugAndClinicalCandidates (ChEMBL + trial registries via Open Targets)_

## Provenance

- Generated: 2026-08-27T11:48:56
- Model (reasoning text only): `gemini-flash-lite-latest`
- Tools invoked (10 calls): `get_uniprot_dossier`, `get_target_disease_evidence`, `get_mr_result`, `get_chembl_modulators`, `get_clinvar_variants`, `get_gnomad_constraint`, `get_gwas_catalog`, `get_pharmgkb_drug_gene`, `get_clinical_evidence`, `classify_evidence_concordance`
- Evidence table, caveats, sources and this block are rendered mechanically from tool return values. The model wrote only the Verdict sentence and the Reasoning paragraph, both checked against tool output by `validate_card.py`.
- No Mendelian randomization or colocalization is computed by this agent; MR estimates, where present, are retrieved from published work.
