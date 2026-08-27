# Target Evidence Card — VKORC1 × venous thrombosis

**Verdict:** GO — VKORC1 is the established molecular target of approved coumarin anticoagulant drugs used clinically for venous thrombosis and related thromboembolic conditions.

> **You asked about "venous thrombosis". This card scored HP_0004936 — Venous thrombosis.** If those are not the same thing, every number below answers a different question.
> **The druggability row is about ChEMBL target "Vitamin K epoxide reductase complex subunit 1" (CHEMBL1930),** matched by text search. If that is not the molecular target you meant, that row is about something else.

## Evidence concordance — classified by rule, not written by the model

- Sources: EpiGraphDB — no pQTL instrument · Europe PMC — NOT checked in this run · Semantic Scholar — NOT checked in this run · MR-KG — NOT checked in this run

## Evidence

| Evidence | Tool | Result |
|---|---|---|
| Causal effect (MR) — retrieved, not computed | `get_mr_result` | **not available** — no pQTL MR estimate for this protein in the resource (absence of an estimate is not evidence of no effect) |
| Target–disease association | `get_target_disease_evidence` | overall score=0.586 (literature=0.214, genetic_association=0.0312, clinical=0.949) |
| Protein context | `get_uniprot_dossier` | Q9BQB6 — Vitamin K epoxide reductase complex subunit 1; location: Endoplasmic reticulum membrane |
| Known modulators / druggability | `get_chembl_modulators` | 7 known modulators (INHIBITOR) |
| Clinical variants | `get_clinvar_variants` | 77 ClinVar records; 3 pathogenic in a sample of 30 |
| Population constraint / LoF tolerance | `get_gnomad_constraint` | pLI=0.00028, LOEUF=1.31 → LoF-tolerant |
| Extra genetic evidence | `get_gwas_catalog` | 109 unique SNPs from 226/226 association rows |
| Pharmacogenomics | `get_pharmgkb_drug_gene` | 38 clinical annotation(s) over 4 drug(s): acenocoumarol, fluindione, phenprocoumon, warfarin — ClinPGx evidence level 1A/1B/2A/3/4 (scale 1A strongest to 4 weakest) — e.g. rs9923231 (VKORC1); warfarin; Hemorrhage (level 2A Toxicity) |
| Clinical development record | `get_clinical_evidence` | max stage for THIS disease: **APPROVAL** — e.g. WARFARIN SODIUM (APPROVAL, 2 trial report(s) for this disease); +1 more drug(s) for this disease  
_stages mean trials exist, not that they worked_ |

## Caveats declared by the tools

- **`get_target_disease_evidence`** — Free-text inputs were resolved to ontology terms: 'VKORC1' -> ENSG00000167397 (VKORC1); 'venous thrombosis' -> HP_0004936 (Venous thrombosis). Scores below describe THAT term, not the free-text phrase.
- **`get_mr_result`** — No pQTL-based MR estimate for VKORC1 in the EpiGraphDB pQTL resource. This resource only covers proteins with usable plasma pQTL instruments. ABSENCE OF AN ESTIMATE IS NOT EVIDENCE OF NO EFFECT.
- **`get_chembl_modulators`** — ChEMBL target matched by text search on 'VKORC1' and resolved to 'Vitamin K epoxide reductase complex subunit 1' — confirm this is the intended target.
- **`get_clinvar_variants`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 77 ClinVar records for this gene; it is a sample, not a rate.
- **`get_clinical_evidence`** — Phase and trial status mean trials EXIST, not that they worked — a COMPLETED phase-3 trial can be a failed one; only why-stopped fields carry failure information, and only approval carries a regulator's efficacy judgement. Registries lag press releases by a data release or more.
- **`classify_evidence_concordance`** — Nothing to compare: fewer than two matched estimates.

## Reasoning

The target VKORC1 encodes vitamin K epoxide reductase, which is directly inhibited by approved therapeutic agents such as warfarin sodium and other coumarins that have reached regulatory approval for venous thrombosis. Clinical evidence and extensive pharmacogenomic annotations link VKORC1 variants directly to anticoagulant response, dosage requirements, and bleeding risks. Open Targets shows strong clinical evidence supporting the target-disease relationship. Furthermore, the gene exhibits robust genetic support with hundreds of associated GWAS catalog entries.

## Sources

- `get_uniprot_dossier`: https://www.uniprot.org/uniprotkb/Q9BQB6 — _UniProt release 2026_02 (10-June-2026)_
- `get_target_disease_evidence`: https://platform.opentargets.org/evidence/ENSG00000167397/HP_0004936 — _Open Targets data release 26.06_
- `get_mr_result`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `get_chembl_modulators`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL1930/ — _ChEMBL_37 (released 2026-05-01)_
- `get_clinvar_variants`: https://www.ncbi.nlm.nih.gov/clinvar/?term=VKORC1%5Bgene%5D — _ClinVar build Build260823-0900.1_
- `get_gnomad_constraint`: https://gnomad.broadinstitute.org/gene/VKORC1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `get_gwas_catalog`: https://www.ebi.ac.uk/gwas/genes/VKORC1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `get_pharmgkb_drug_gene`: https://www.pharmgkb.org/search?query=VKORC1 — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `get_clinical_evidence`: https://platform.opentargets.org/target/ENSG00000167397 — _Open Targets data release 26.06; drugAndClinicalCandidates (ChEMBL + trial registries via Open Targets)_

## Provenance

- Generated: 2026-08-27T11:50:47
- Model (reasoning text only): `gemini-flash-lite-latest`
- Tools invoked (10 calls): `get_uniprot_dossier`, `get_target_disease_evidence`, `get_mr_result`, `get_chembl_modulators`, `get_clinvar_variants`, `get_gnomad_constraint`, `get_gwas_catalog`, `get_pharmgkb_drug_gene`, `get_clinical_evidence`, `classify_evidence_concordance`
- Evidence table, caveats, sources and this block are rendered mechanically from tool return values. The model wrote only the Verdict sentence and the Reasoning paragraph, both checked against tool output by `validate_card.py`.
- No Mendelian randomization or colocalization is computed by this agent; MR estimates, where present, are retrieved from published work.
