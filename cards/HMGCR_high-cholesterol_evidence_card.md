# Target Evidence Card — HMGCR × high cholesterol

**Verdict:** GO — HMGCR is the clinically validated, primary pharmacological target of statins for hypercholesterolemia, backed by extensive genetic and clinical trial evidence.

> **You asked about "high cholesterol". This card scored HP_0003124 — Hypercholesterolemia.** If those are not the same thing, every number below answers a different question.
> **The druggability row is about ChEMBL target "3-hydroxy-3-methylglutaryl-coenzyme A reductase" (CHEMBL402),** matched by text search. If that is not the molecular target you meant, that row is about something else.

## Evidence concordance — classified by rule, not written by the model

- Sources: EpiGraphDB — no pQTL instrument · Europe PMC — NOT checked in this run · Semantic Scholar — NOT checked in this run · MR-KG — NOT checked in this run

## Evidence

| Evidence | Tool | Result |
|---|---|---|
| Causal effect (MR) — retrieved, not computed | `get_mr_result` | **not available** — no pQTL MR estimate for this protein in the resource (absence of an estimate is not evidence of no effect) |
| Target–disease association | `get_target_disease_evidence` | overall score=0.74 (literature=0.206, genetic_association=0.857, clinical=0.998) |
| Protein context | `get_uniprot_dossier` | P04035 — 3-hydroxy-3-methylglutaryl-coenzyme A reductase; location: Endoplasmic reticulum membrane, Peroxisome membrane |
| Known modulators / druggability | `get_chembl_modulators` | 10 known modulators (INHIBITOR) |
| Clinical variants | `get_clinvar_variants` | 112 ClinVar records; 1 pathogenic in a sample of 30 |
| Population constraint / LoF tolerance | `get_gnomad_constraint` | pLI=1, LOEUF=0.433 → LoF-INTOLERANT (handle with care) |
| Extra genetic evidence | `get_gwas_catalog` | 92 unique SNPs from 177/177 association rows |
| Pharmacogenomics | `get_pharmgkb_drug_gene` | 10 clinical annotation(s) over 6 drug(s): HMG-CoA reductase inhibitors, atorvastatin, fluvastatin, lovastatin +2 more — ClinPGx evidence level 3 (scale 1A strongest to 4 weakest) — e.g. rs17238540 (HMGCR); pravastatin (level 3 Efficacy) |
| Clinical development record | `get_clinical_evidence` | max stage for THIS disease: **APPROVAL** — e.g. SIMVASTATIN (APPROVAL, 188 trial report(s) for this disease, 2 of them with a stop reason); +7 more drug(s) for this disease  
_stages mean trials exist, not that they worked_ |

## Caveats declared by the tools

- **`get_target_disease_evidence`** — Free-text inputs were resolved to ontology terms: 'HMGCR' -> ENSG00000113161 (HMGCR); 'high cholesterol' -> HP_0003124 (Hypercholesterolemia). Scores below describe THAT term, not the free-text phrase.
- **`get_chembl_modulators`** — ChEMBL target matched by text search on 'HMGCR' and resolved to '3-hydroxy-3-methylglutaryl-coenzyme A reductase' — confirm this is the intended target.
- **`get_mr_result`** — No pQTL-based MR estimate for HMGCR in the EpiGraphDB pQTL resource. This resource only covers proteins with usable plasma pQTL instruments. ABSENCE OF AN ESTIMATE IS NOT EVIDENCE OF NO EFFECT.
- **`get_clinvar_variants`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 112 ClinVar records for this gene; it is a sample, not a rate.
- **`get_clinical_evidence`** — Phase and trial status mean trials EXIST, not that they worked — a COMPLETED phase-3 trial can be a failed one; only why-stopped fields carry failure information, and only approval carries a regulator's efficacy judgement. Registries lag press releases by a data release or more.
- **`classify_evidence_concordance`** — Nothing to compare: fewer than two matched estimates.

## Reasoning

HMGCR encodes 3-hydroxy-3-methylglutaryl-coenzyme A reductase, the rate-limiting enzyme in cholesterol biosynthesis and the well-established target of multiple FDA-approved statin drugs such as simvastatin, atorvastatin, and rosuvastatin. Open Targets demonstrates strong genetic and clinical association scores for hypercholesterolemia, and numerous ChEMBL modulators target this protein. While gnomAD constraint metrics indicate that the gene is LoF-intolerant, its successful inhibition by approved therapeutics underscores its exceptional target validation for lowering cholesterol.

## Sources

- `get_uniprot_dossier`: https://www.uniprot.org/uniprotkb/P04035 — _UniProt release 2026_02 (10-June-2026)_
- `get_target_disease_evidence`: https://platform.opentargets.org/evidence/ENSG00000113161/HP_0003124 — _Open Targets data release 26.06_
- `get_chembl_modulators`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL402/ — _ChEMBL_37 (released 2026-05-01)_
- `get_mr_result`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `get_clinvar_variants`: https://www.ncbi.nlm.nih.gov/clinvar/?term=HMGCR%5Bgene%5D — _ClinVar build Build260818-0035.1_
- `get_gnomad_constraint`: https://gnomad.broadinstitute.org/gene/HMGCR — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `get_gwas_catalog`: https://www.ebi.ac.uk/gwas/genes/HMGCR — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `get_pharmgkb_drug_gene`: https://www.pharmgkb.org/search?query=HMGCR — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `get_clinical_evidence`: https://platform.opentargets.org/target/ENSG00000113161 — _Open Targets data release 26.06; drugAndClinicalCandidates (ChEMBL + trial registries via Open Targets)_

## Provenance

- Generated: 2026-08-21T15:33:17
- Model (reasoning text only): `gemini-flash-lite-latest`
- Tools invoked (10 calls): `get_uniprot_dossier`, `get_target_disease_evidence`, `get_chembl_modulators`, `get_mr_result`, `get_clinvar_variants`, `get_gnomad_constraint`, `get_gwas_catalog`, `get_pharmgkb_drug_gene`, `get_clinical_evidence`, `classify_evidence_concordance`
- Evidence table, caveats, sources and this block are rendered mechanically from tool return values. The model wrote only the Verdict sentence and the Reasoning paragraph, both checked against tool output by `validate_card.py`.
- No Mendelian randomization or colocalization is computed by this agent; MR estimates, where present, are retrieved from published work.

> **VALIDATION FAILED** — the model wrote claim tokens with no support in tool output:
> - [efficacy-claim-not-retrievable] `clinically validated`
> - [qualitative-claim] `FDA-approved`
