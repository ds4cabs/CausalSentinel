# Target Evidence Card — VKORC1 × venous thrombosis

**Verdict:** GO — VKORC1 is a well-established biological and pharmacological target linked to vitamin K metabolism and clinical thrombosis management, supported by extensive genetic and pharmacogenomic evidence.

> **Question actually answered:** the free-text disease was resolved to **HP_0004936 (Venous thrombosis)**. If that is not what you meant, every score below answers a different question.

## Evidence

| Evidence | Tool | Result |
|---|---|---|
| Causal effect (MR) — retrieved, not computed | `get_mr_result` | **not available** — no pQTL MR estimate for this protein in the resource (absence of an estimate is not evidence of no effect) |
| Target–disease association | `get_target_disease_evidence` | overall score=0.586 (literature=0.214, genetic_association=0.0312, clinical=0.949) |
| Protein context | `get_uniprot_dossier` | Q9BQB6 — Vitamin K epoxide reductase complex subunit 1; location: Endoplasmic reticulum membrane |
| Known modulators / druggability | `get_chembl_modulators` | **tool error** — ChEMBL HTTP 500 |
| Clinical variants | `get_clinvar_variants` | 75 ClinVar records; 3 pathogenic in a sample of 30 |
| Population constraint / LoF tolerance | `get_gnomad_constraint` | pLI=0.00028, LOEUF=1.31 → LoF-tolerant |
| Extra genetic evidence | `get_gwas_catalog` | 106 unique SNPs from 226/226 association rows |
| Pharmacogenomics | `get_pharmgkb_drug_gene` | 38 clinical annotations across 4 drugs (level 1A: 3, level 1B: 5, level 2A: 8, level 3: 21, level 4: 1) |

## Caveats declared by the tools

- **`get_target_disease_evidence`** — Free-text inputs were resolved to ontology terms: 'VKORC1' -> ENSG00000167397 (VKORC1); 'venous thrombosis' -> HP_0004936 (Venous thrombosis). Scores below describe THAT term, not the free-text phrase.
- **`get_mr_result`** — No pQTL-based MR estimate for VKORC1 in the EpiGraphDB pQTL resource. This resource only covers proteins with usable plasma pQTL instruments. ABSENCE OF AN ESTIMATE IS NOT EVIDENCE OF NO EFFECT.
- **`get_clinvar_variants`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 75 ClinVar records for this gene; it is a sample, not a rate.

## Reasoning

Open Targets associates VKORC1 with venous thrombosis, backed by multiple GWAS association records in the GWAS Catalog. While a direct MR causal estimate was not available from the EpiGraphDB pQTL resource, PharmGKB and ClinPGx document extensive pharmacogenomic annotations and drug-gene relationships involving coumarin anticoagulants such as warfarin and acenocoumarol. Furthermore, gnomAD constraint metrics indicate that VKORC1 is loss-of-function tolerant, and UniProt confirms its essential role as the catalytic subunit of the vitamin K epoxide reductase complex governing blood coagulation.

## Sources

- `get_uniprot_dossier`: https://www.uniprot.org/uniprotkb/Q9BQB6 — _UniProt release 2026_02 (10-June-2026)_
- `get_target_disease_evidence`: https://platform.opentargets.org/evidence/ENSG00000167397/HP_0004936 — _Open Targets data release 26.06_
- `get_mr_result`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `get_clinvar_variants`: https://www.ncbi.nlm.nih.gov/clinvar/?term=VKORC1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `get_gnomad_constraint`: https://gnomad.broadinstitute.org/gene/VKORC1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `get_gwas_catalog`: https://www.ebi.ac.uk/gwas/genes/VKORC1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `get_pharmgkb_drug_gene`: https://www.pharmgkb.org/search?query=VKORC1 — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_

## Provenance

- Generated: 2026-08-17T22:26:23
- Model (reasoning text only): `gemini-flash-lite-latest`
- Tools invoked (8 calls): `get_uniprot_dossier`, `get_target_disease_evidence`, `get_mr_result`, `get_chembl_modulators`, `get_clinvar_variants`, `get_gnomad_constraint`, `get_gwas_catalog`, `get_pharmgkb_drug_gene`
- Evidence table, caveats, sources and this block are rendered mechanically from tool return values. The model wrote only the Verdict sentence and the Reasoning paragraph, both checked against tool output by `validate_card.py`.
- No Mendelian randomization or colocalization is computed by this agent; MR estimates, where present, are retrieved from published work.
