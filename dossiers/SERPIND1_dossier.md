# Protein Dossier — SERPIND1 (Heparin cofactor 2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| LDL cholesterol | -0.142 | 0.01 | 2.47e-45 | Wald ratio | 1 | trans | NA |
| Total cholesterol | -0.135 | 0.0096 | 1.13e-44 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: high cholesterol | -0.169 | 0.0214 | 3.44e-15 | Wald ratio | 1 | trans | NA |
| Weight | -0.0263 | 0.00591 | 8.87e-06 | Wald ratio | 1 | trans | NA |
| Triglycerides | -0.0404 | 0.00916 | 1.06e-05 | Wald ratio | 1 | trans | NA |
| Body mass index (BMI) | -0.0272 | 0.00669 | 4.88e-05 | Wald ratio | 1 | trans | NA |
| Myocardial infarction | -0.0971 | 0.0265 | 2.50e-04 | Wald ratio | 1 | trans | NA |
| Coronary heart disease | -0.0809 | 0.0239 | 7.15e-04 | Wald ratio | 1 | trans | NA |
| Childhood intelligence | 0.115 | 0.0356 | 0.00128 | Wald ratio | 1 | trans | NA |
| Red blood cell count | -0.0161 | 0.00589 | 0.00613 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: C61 Malignant neoplasm of prostate | 0.178 | 0.0692 | 0.0103 | Wald ratio | 1 | trans | NA |
| Transferrin | -0.0716 | 0.0281 | 0.011 | Wald ratio | 1 | trans | NA |
| _...and 104 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3316_58_1` | Heparin cofactor II | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_12 association rows across 12 traits (11 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| CRKL/DBNL protein level ratio | 2e-35 | rs117858197 | 1 | GCST90314263 | no MR -> candidate analysis |
| CRKL/IRAK4 protein level ratio | 3e-33 | rs117858197 | 1 | GCST90314268 | no MR -> candidate analysis |
| CASP3/CRKL protein level ratio | 2e-31 | rs117858197 | 1 | GCST90313631 | no MR -> candidate analysis |
| CRKL/GRAP2 protein level ratio | 2e-23 | rs117858197 | 1 | GCST90314267 | no MR -> candidate analysis |
| CRKL/PLA2G4A protein level ratio | 1e-21 | rs117858197 | 1 | GCST90314271 | no MR -> candidate analysis |
| CRKL/MGLL protein level ratio | 3e-21 | rs117858197 | 1 | GCST90314270 | no MR -> candidate analysis |
| CRKL/DOK2 protein level ratio | 2e-19 | rs117858197 | 1 | GCST90314264 | no MR -> candidate analysis |
| CRKL/SERPINB1 protein level ratio | 3e-18 | rs117858197 | 1 | GCST90314272 | no MR -> candidate analysis |
| CRKL/MANF protein level ratio | 2e-17 | rs117858197 | 1 | GCST90314269 | no MR -> candidate analysis |
| CRKL/YES1 protein level ratio | 5e-17 | rs117858197 | 1 | GCST90314273 | no MR -> candidate analysis |
| O-acetyl-ADP-ribose deacetylase MACROD2 level in Chronic kid | 1e-12 | rs116401176 | 1 | GCST90236940 | no MR -> candidate analysis |
| Monocyte count | 5e-8 | rs361993 | 1 | GCST90018967 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 265 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| heparin cofactor 2 deficiency | 0.819 | — | established (curated) | no MR -> candidate analysis |
| Venous thrombosis | 0.701 | — | established (curated) | MR: beta=-0.0399, p=0.42 (trans) |
| hemorrhage | 0.438 | — | established (curated) | no MR -> candidate analysis |
| thrombotic disease | 0.195 | — | established (curated) | no MR -> candidate analysis |
| Varicose veins | 0.118 | — | common-variant locus | MR: beta=-0.0667, p=0.183 (trans) |
| COVID-19 | 0.066 | — | common-variant locus | no MR -> candidate analysis |

> Of the 6 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=6.8e-12, LOEUF=1.29 — LoF-tolerant |
| GWAS Catalog | 44 unique SNPs / 88 rows |
| ClinVar | 548 records; 20 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 265 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'SERPIND1'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 548 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 12 of 12 traits by best p-value, aggregated from 12 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P05546 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000099937/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/SERPIND1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/SERPIND1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=SERPIND1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/SERPIND1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:02:32  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
