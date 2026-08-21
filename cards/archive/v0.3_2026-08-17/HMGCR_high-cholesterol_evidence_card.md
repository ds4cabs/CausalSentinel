# Target Evidence Card — HMGCR × high cholesterol

**Verdict:** GO — HMGCR shows strong genetic association, extensive GWAS mapping, and extensive pharmacogenomic and clinical evidence linking it to high cholesterol.

> **Question actually answered:** the free-text disease was resolved to **HP_0003124 (Hypercholesterolemia)**. If that is not what you meant, every score below answers a different question.

## Evidence

| Evidence | Tool | Result |
|---|---|---|
| Causal effect (MR) — retrieved, not computed | `get_mr_result` | **not available** — no pQTL MR estimate for this protein in the resource (absence of an estimate is not evidence of no effect) |
| Target–disease association | `get_target_disease_evidence` | overall score=0.74 (literature=0.206, genetic_association=0.857, clinical=0.998) |
| Protein context | `get_uniprot_dossier` | P04035 — 3-hydroxy-3-methylglutaryl-coenzyme A reductase; location: Endoplasmic reticulum membrane, Peroxisome membrane |
| Known modulators / druggability | `get_chembl_modulators` | **tool error** — ChEMBL HTTP 500 |
| Clinical variants | `get_clinvar_variants` | 112 ClinVar records; 1 pathogenic in a sample of 30 |
| Population constraint / LoF tolerance | `get_gnomad_constraint` | pLI=1, LOEUF=0.433 → LoF-INTOLERANT (handle with care) |
| Extra genetic evidence | `get_gwas_catalog` | 92 unique SNPs from 177/177 association rows |
| Pharmacogenomics | `get_pharmgkb_drug_gene` | 10 clinical annotations across 6 drugs (level 3: 10) |

## Caveats declared by the tools

- **`get_target_disease_evidence`** — Free-text inputs were resolved to ontology terms: 'HMGCR' -> ENSG00000113161 (HMGCR); 'high cholesterol' -> HP_0003124 (Hypercholesterolemia). Scores below describe THAT term, not the free-text phrase.
- **`get_mr_result`** — No pQTL-based MR estimate for HMGCR in the EpiGraphDB pQTL resource. This resource only covers proteins with usable plasma pQTL instruments. ABSENCE OF AN ESTIMATE IS NOT EVIDENCE OF NO EFFECT.
- **`get_clinvar_variants`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 112 ClinVar records for this gene; it is a sample, not a rate.

## Reasoning

Open Targets demonstrates a robust association score between HMGCR and hypercholesterolemia, reinforced by numerous GWAS associations. PharmGKB records multiple clinical annotations involving statins and HMG-CoA reductase inhibitors, reflecting established pharmacological modulation. Although gnomAD constraint metrics indicate loss-of-function intolerance and no MR estimate was retrieved, the vast genetic, clinical, and pharmacological evidence supports its target validity.
```

## Sources

- `get_uniprot_dossier`: https://www.uniprot.org/uniprotkb/P04035 — _UniProt release 2026_02 (10-June-2026)_
- `get_target_disease_evidence`: https://platform.opentargets.org/evidence/ENSG00000113161/HP_0003124 — _Open Targets data release 26.06_
- `get_mr_result`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `get_clinvar_variants`: https://www.ncbi.nlm.nih.gov/clinvar/?term=HMGCR%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `get_gnomad_constraint`: https://gnomad.broadinstitute.org/gene/HMGCR — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `get_gwas_catalog`: https://www.ebi.ac.uk/gwas/genes/HMGCR — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `get_pharmgkb_drug_gene`: https://www.pharmgkb.org/search?query=HMGCR — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_

## Provenance

- Generated: 2026-08-17T22:23:30
- Model (reasoning text only): `gemini-flash-lite-latest`
- Tools invoked (8 calls): `get_uniprot_dossier`, `get_target_disease_evidence`, `get_mr_result`, `get_chembl_modulators`, `get_clinvar_variants`, `get_gnomad_constraint`, `get_gwas_catalog`, `get_pharmgkb_drug_gene`
- Evidence table, caveats, sources and this block are rendered mechanically from tool return values. The model wrote only the Verdict sentence and the Reasoning paragraph, both checked against tool output by `validate_card.py`.
- No Mendelian randomization or colocalization is computed by this agent; MR estimates, where present, are retrieved from published work.
