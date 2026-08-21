# Protein Dossier — KLK8 (Kallikrein-8)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Sodium in urine | 0.0218 | 0.00618 | 4.09e-04 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | -0.0152 | 0.00515 | 0.00315 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I84 Haemorrhoids | 0.105 | 0.0364 | 0.00373 | Wald ratio | 1 | cis | NA |
| Potassium in urine | 0.0178 | 0.00637 | 0.00536 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | -0.0148 | 0.00544 | 0.00635 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | 0.0168 | 0.00628 | 0.00739 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: high cholesterol | 0.0383 | 0.0164 | 0.0193 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hayfever or allergic rhinitis | 0.0568 | 0.0244 | 0.02 | Wald ratio | 1 | cis | NA |
| Creatinine (enzymatic) in urine | 0.0135 | 0.00601 | 0.0244 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: pernicious anaemia | -0.402 | 0.18 | 0.0256 | Wald ratio | 1 | cis | NA |
| Ovarian cancer | -0.0856 | 0.044 | 0.0518 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Cataract | 0.0605 | 0.0324 | 0.0624 | Wald ratio | 1 | cis | NA |
| _...and 53 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2834_54_1` | kallikrein 8 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_28 association rows across 15 traits (26 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| KLK8/NECTIN4 protein level ratio | 2e-1363 | rs74705037 | 1 | GCST90315258 | no MR -> candidate analysis |
| KLK11/KLK8 protein level ratio | 1e-1342 | rs74705037 | 1 | GCST90315254 | no MR -> candidate analysis |
| KLK8/LY6D protein level ratio | 1e-1166 | rs74705037 | 1 | GCST90315257 | no MR -> candidate analysis |
| Circulating KLK8 levels | 3e-1082 | rs74705037 | 4 | GCST90860020 | no MR -> candidate analysis |
| Kallikrein-8 levels | 4e-150 | rs74705037 | 3 | GCST90248164 | no MR -> candidate analysis |
| Kallikrein-8 levels (KLK8.13708.56.3) | 6e-58 | rs74705037 | 3 | GCST90241680 | no MR -> candidate analysis |
| kallikrein-11 levels | 2e-50 | rs1122466 | 1 | GCST90012012 | no MR -> candidate analysis |
| Kallikrein-8 (analyte X13708.56) levels | 8e-50 | rs1722546 | 1 | GCST90422316 | no MR -> candidate analysis |
| KLK12 protein levels | 5e-35 | rs74705037 | 4 | GCST90469698 | no MR -> candidate analysis |
| KLK7 protein levels | 7e-33 | rs1722547 | 1 | GCST90469706 | no MR -> candidate analysis |
| Serum levels of protein KLK8 | 9e-23 | rs10410942 | 1 | GCST90088093 | no MR -> candidate analysis |
| Blood protein levels | 2e-17 | rs10410942 | 2 | GCST006585 | no MR -> candidate analysis |
| _...and 3 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 263 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| actinic keratosis | 0.526 | — | common-variant locus | no MR -> candidate analysis |

> Of the 1 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Kallikrein-8) |
| gnomAD constraint | pLI=7.6e-05, LOEUF=1 — LoF-tolerant |
| GWAS Catalog | 185 unique SNPs / 442 rows |
| ClinVar | 72 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 263 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'KLK8' and resolved to 'Kallikrein-8' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 72 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 15 of 15 traits by best p-value, aggregated from 28 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O60259 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000129455/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4812/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/KLK8 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/KLK8 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=KLK8%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/KLK8 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:25:25  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
