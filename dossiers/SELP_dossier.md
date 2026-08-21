# Protein Dossier — SELP (P-selectin)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Height | -0.0136 | 0.00657 | 0.0379 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Wrist | -0.00121 | 0.000681 | 0.0763 | Inverse variance weighted | 2 | trans | NA |
| Fractured bone site(s): Wrist | -0.00121 | 0.000681 | 0.0763 | Inverse variance weighted | 2 | cis | NA |
| Serum creatinine (eGFRcrea) | 0.00347 | 0.00198 | 0.0801 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K80 Cholelithiasis | -0.00109 | 0.000638 | 0.0862 | Inverse variance weighted | 2 | trans | NA |
| Diagnoses - main ICD10: K80 Cholelithiasis | -0.00109 | 0.000638 | 0.0862 | Inverse variance weighted | 2 | cis | NA |
| Non-cancer illness code  self-reported: emphysema or chronic bronchitis | -0.000882 | 0.000519 | 0.0891 | Inverse variance weighted | 2 | trans | NA |
| Non-cancer illness code  self-reported: emphysema or chronic bronchitis | -0.000882 | 0.000519 | 0.0891 | Inverse variance weighted | 2 | cis | NA |
| Hippocampus volume | 16.7 | 9.96 | 0.0939 | Inverse variance weighted | 2 | trans | NA |
| Hippocampus volume | 16.7 | 9.96 | 0.0939 | Inverse variance weighted | 2 | cis | NA |
| Diastolic blood pressure  automated reading | -0.00749 | 0.00453 | 0.0984 | Inverse variance weighted | 2 | trans | NA |
| Diastolic blood pressure  automated reading | -0.00749 | 0.00453 | 0.0984 | Inverse variance weighted | 2 | cis | NA |
| _...and 135 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-4154_57_2` | P-Selectin | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_112 association rows across 83 traits (68 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating SELP levels | 2e-806 | rs6136 | 4 | GCST90859923 | no MR -> candidate analysis |
| SELP/VSIR protein level ratio | 7e-662 | rs6136 | 1 | GCST90315822 | no MR -> candidate analysis |
| GP1BA/SELP protein level ratio | 3e-541 | rs6136 | 1 | GCST90314958 | no MR -> candidate analysis |
| CD46/SELP protein level ratio | 1e-532 | rs6136 | 1 | GCST90313834 | no MR -> candidate analysis |
| SDC4/SELP protein level ratio | 4e-437 | rs6136 | 1 | GCST90315817 | no MR -> candidate analysis |
| ITGB1/SELP protein level ratio | 1e-385 | rs6136 | 1 | GCST90315230 | no MR -> candidate analysis |
| Bone mineral density mean | 1e-300 | rs140704427 | 2 | GCST90321120 | no MR -> candidate analysis |
| SELL protein levels | 1e-295 | rs3917775 | 4 | GCST90470567 | no MR -> candidate analysis |
| Blood protein levels | 2e-184 | rs6136 | 2 | GCST006585 | no MR -> candidate analysis |
| Serum levels of protein SELP | 5e-162 | rs6128 | 2 | GCST90088610 | no MR -> candidate analysis |
| L-selectin levels | 9e-118 | rs3917775 | 3 | GCST90248341 | no MR -> candidate analysis |
| P-selectin levels (SELP.4154.57.2) | 3e-105 | rs6136 | 2 | GCST90242187 | no MR -> candidate analysis |
| _...and 71 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1435 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| atrial fibrillation | 0.542 | — | common-variant locus | MR: beta=-0.000456, p=0.336 (trans) |
| deep vein thrombosis | 0.487 | — | common-variant locus | no MR -> candidate analysis |
| aging | 0.524 | — | common-variant locus | no MR -> candidate analysis |
| Abnormality of the skeletal system | 0.522 | — | common-variant locus | no MR -> candidate analysis |
| thrombophilia | 0.493 | — | common-variant locus | no MR -> candidate analysis |
| Thromboembolism | 0.481 | — | common-variant locus | no MR -> candidate analysis |
| Premature coronary artery atherosclerosis | 0.426 | — | established (curated) | no MR -> candidate analysis |
| viral pneumonia | 0.414 | — | common-variant locus | no MR -> candidate analysis |
| acne | 0.138 | — | common-variant locus | no MR -> candidate analysis |
| cancer | 0.078 | — | common-variant locus | MR: beta=-0.000882, p=0.0891 (trans) |

> Of the 10 rows above, **8 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 4 known modulators (P-selectin) |
| gnomAD constraint | pLI=8.7e-28, LOEUF=1.05 — LoF-tolerant |
| GWAS Catalog | 137 unique SNPs / 366 rows |
| ClinVar | 162 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1435 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'SELP' and resolved to 'P-selectin' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 162 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 83 traits by best p-value, aggregated from 112 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P16109 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000174175/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL5378/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/SELP — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/SELP — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=SELP%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/SELP — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:57:46  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
