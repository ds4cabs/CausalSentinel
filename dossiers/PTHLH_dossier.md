# Protein Dossier — PTHLH (Parathyroid hormone-related protein)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Height | 0.113 | 0.0177 | 1.97e-10 | Wald ratio | 1 | cis | 6.8e-06 |
| Heel bone mineral density (BMD) T-score  automated | 0.115 | 0.0189 | 1.26e-09 | Wald ratio | 1 | cis | 0.21 |
| Forced vital capacity (FVC) | 0.0625 | 0.012 | 1.80e-07 | Wald ratio | 1 | cis | 0.0463 |
| Weight | 0.0664 | 0.0129 | 2.54e-07 | Wald ratio | 1 | cis | 0.603 |
| Forced expiratory volume in 1-second (FEV1) | 0.0461 | 0.0126 | 2.58e-04 | Wald ratio | 1 | cis | NA |
| Birth weight | 0.0725 | 0.0215 | 7.38e-04 | Wald ratio | 1 | cis | NA |
| Creatinine (enzymatic) in urine | 0.0447 | 0.014 | 0.00136 | Wald ratio | 1 | cis | NA |
| Birth length | 0.164 | 0.0612 | 0.00727 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K80 Cholelithiasis | 0.22 | 0.0822 | 0.00743 | Wald ratio | 1 | cis | NA |
| Femoral neck bone mineral density | 0.122 | 0.0457 | 0.00747 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M16 Coxarthrosis [arthrosis of hip] | 0.252 | 0.0954 | 0.00813 | Wald ratio | 1 | cis | NA |
| Potassium in urine | 0.037 | 0.0148 | 0.0125 | Wald ratio | 1 | cis | NA |
| _...and 112 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2962_50_2` | PTHrP | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_290 association rows across 130 traits (249 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| MANSC4 protein levels | 4e-215 | rs12425609 | 11 | GCST90469848 | no MR -> candidate analysis |
| Height | 4e-176 | rs10843078 | 35 | GCST90245848 | MR: beta=0.113, p=1.97e-10 (cis) |
| Breast cancer | 6e-72 | rs7297051 | 16 | GCST90090980 | no MR -> candidate analysis |
| Type 2 diabetes | 1e-69 | rs10842991 | 22 | GCST90492734 | MR: beta=0.202, p=0.199 (cis) |
| Osteoarthritis (with total hip replacement) | 5e-57 | rs10843013 | 2 | GCST90566802 | no MR -> candidate analysis |
| Standing height (UKB data field 50) | 4e-49 | rs180958337 | 4 | GCST90468178 | no MR -> candidate analysis |
| Whole brain restricted isotropic diffusion (multivariate ana | 2e-44 | rs10843091 | 1 | GCST90131904 | no MR -> candidate analysis |
| Osteoarthritis (hip) | 1e-41 | rs10843013 | 4 | GCST90566798 | MR: beta=0.313, p=0.0271 (cis) |
| Unsupervised deep imaging phenotypes (UDIP-FA) | 3e-31 | rs2054474 | 6 | GCST90860937 | no MR -> candidate analysis |
| Whole brain free water diffusion (multivariate analysis) | 7e-31 | rs10843091 | 1 | GCST90131906 | no MR -> candidate analysis |
| Vertex-wise cortical surface area | 1e-30 | rs10843104 | 2 | GCST90095130 | no MR -> candidate analysis |
| Fasting blood glucose | 2e-30 | rs10771370 | 2 | GCST90662896 | no MR -> candidate analysis |
| _...and 118 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 2581 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| brachydactyly type E | 0.81 | — | established (curated) | no MR -> candidate analysis |
| Abnormality of the skeletal system | 0.775 | — | common-variant locus | no MR -> candidate analysis |
| breast carcinoma | 0.667 | — | common-variant locus | no MR -> candidate analysis |
| breast neoplasm | 0.63 | — | common-variant locus | MR: beta=0.161, p=0.101 (cis) |
| breast cancer | 0.602 | — | common-variant locus | no MR -> candidate analysis |
| androgenetic alopecia | 0.636 | — | common-variant locus | no MR -> candidate analysis |
| cancer | 0.525 | — | common-variant locus | MR: beta=1.01, p=0.0335 (cis) |
| open-angle glaucoma | 0.555 | — | common-variant locus | no MR -> candidate analysis |
| hereditary disease | 0.553 | — | established (curated) | no MR -> candidate analysis |
| breast disorder | 0.537 | — | common-variant locus | no MR -> candidate analysis |
| Abnormality of the breast | 0.52 | — | common-variant locus | no MR -> candidate analysis |
| alopecia | 0.511 | — | common-variant locus | no MR -> candidate analysis |
| estrogen-receptor negative breast cancer | 0.5 | — | common-variant locus | no MR -> candidate analysis |
| Breast hypertrophy | 0.472 | — | common-variant locus | no MR -> candidate analysis |
| spinal stenosis | 0.473 | — | common-variant locus | no MR -> candidate analysis |

> Of the 15 rows above, **13 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 1 known modulators (Parathyroid hormone-related protein) |
| gnomAD constraint | pLI=0.92, LOEUF=0.564 — LoF-INTOLERANT |
| GWAS Catalog | 149 unique SNPs / 354 rows |
| ClinVar | 167 records; 6 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 2581 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'PTHLH' and resolved to 'Parathyroid hormone-related protein' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 167 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 130 traits by best p-value, aggregated from 290 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P12272 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000087494/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3712869/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PTHLH — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PTHLH — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PTHLH%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/PTHLH — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:41:36  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
