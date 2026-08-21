# Protein Dossier — KLK6 (Kallikrein-6)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: N40 Hyperplasia of prostate | 0.276 | 0.0659 | 2.75e-05 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I80 Phlebitis and thrombophlebitis | 0.268 | 0.0939 | 0.0044 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | 0.0225 | 0.0083 | 0.00662 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: G47 Sleep disorders | 0.234 | 0.0864 | 0.00664 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K60 Fissure and fistula of anal and rectal regions | 0.259 | 0.0959 | 0.00695 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: asthma | 0.0525 | 0.0221 | 0.0173 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: D12 Benign neoplasm of colon  rectum  anus and anal canal | -0.202 | 0.0865 | 0.0198 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | -0.0163 | 0.00719 | 0.0231 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | -0.0148 | 0.00681 | 0.0298 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R14 Flatulence and related conditions | 0.464 | 0.231 | 0.0446 | Wald ratio | 1 | cis | NA |
| Thalamus volume | -42.6 | 23.6 | 0.0705 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K40 Inguinal hernia | -0.102 | 0.0564 | 0.0708 | Wald ratio | 1 | cis | NA |
| _...and 61 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3450_4_2` | Kallikrein 6 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_29 association rows across 19 traits (27 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating KLK10 levels | 2e-587 | rs1654530 | 2 | GCST90860356 | no MR -> candidate analysis |
| KLK6/MOG protein level ratio | 6e-258 | rs1654535 | 1 | GCST90315255 | no MR -> candidate analysis |
| Circulating KLK6 levels | 3e-241 | rs268891 | 3 | GCST90859992 | no MR -> candidate analysis |
| KLK6/PTPRN2 protein level ratio | 5e-214 | rs1654535 | 1 | GCST90315256 | no MR -> candidate analysis |
| KLK6 protein levels | 5e-191 | rs268891 | 2 | GCST90469705 | no MR -> candidate analysis |
| Kallikrein-6 levels | 3e-99 | rs268891 | 1 | GCST90012008 | no MR -> candidate analysis |
| KLK7 protein levels | 1e-80 | rs56031098 | 2 | GCST90469706 | no MR -> candidate analysis |
| KLK10 protein levels | 2e-59 | rs60850416 | 3 | GCST90469696 | no MR -> candidate analysis |
| Serum levels of protein KLK10 | 2e-57 | rs57392237 | 1 | GCST90089306 | no MR -> candidate analysis |
| KLK12 protein levels | 3e-37 | rs12461147 | 2 | GCST90469698 | no MR -> candidate analysis |
| KLK4 protein levels | 2e-29 | rs57392237 | 1 | GCST90469704 | no MR -> candidate analysis |
| Erythematosquamous dermatosis (PheCode 690) | 4e-22 | rs268890 | 2 | GCST90480446 | no MR -> candidate analysis |
| _...and 7 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 280 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| seborrheic dermatitis | 0.277 | — | common-variant locus | no MR -> candidate analysis |
| erythematosquamous dermatosis | 0.274 | — | common-variant locus | no MR -> candidate analysis |
| placenta praevia | 0.22 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.21 | — | common-variant locus | no MR -> candidate analysis |

> Of the 4 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Kallikrein-6) |
| gnomAD constraint | pLI=6.9e-05, LOEUF=1.12 — LoF-tolerant |
| GWAS Catalog | 163 unique SNPs / 424 rows |
| ClinVar | 52 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 280 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'KLK6' and resolved to 'Kallikrein-6' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 52 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 19 of 19 traits by best p-value, aggregated from 29 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q92876 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000167755/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4448/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/KLK6 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/KLK6 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=KLK6%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/KLK6 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:24:42  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
