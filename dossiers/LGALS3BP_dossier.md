# Protein Dossier — LGALS3BP (Galectin-3-binding protein)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| PGC cross-disorder traits | -0.225 | 0.0888 | 0.0114 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: psoriasis | 0.288 | 0.116 | 0.0134 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: asthma | -0.122 | 0.0515 | 0.0179 | Wald ratio | 1 | cis | NA |
| Autism | -0.435 | 0.199 | 0.0288 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R35 Polyuria | 0.387 | 0.184 | 0.0356 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | -0.0275 | 0.0133 | 0.0387 | Wald ratio | 1 | cis | NA |
| Major depressive disorder | -0.317 | 0.156 | 0.042 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: L03 Cellulitis | 0.274 | 0.141 | 0.0516 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Ankle | 0.215 | 0.113 | 0.0577 | Wald ratio | 1 | cis | NA |
| Sleep duration | 0.0233 | 0.0127 | 0.0662 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: prostate cancer | 0.264 | 0.15 | 0.0789 | Wald ratio | 1 | cis | NA |
| Vascular or heart problems diagnosed by doctor: Angina | 0.139 | 0.0798 | 0.0818 | Wald ratio | 1 | cis | NA |
| _...and 71 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-5000_52_1` | LG3BP | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_26 association rows across 15 traits (23 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| LGALS3BP protein levels | 1e-77 | rs111526614 | 3 | GCST90469760 | no MR -> candidate analysis |
| CANT1 protein levels | 1e-58 | rs112832453 | 1 | GCST90468536 | no MR -> candidate analysis |
| Galectin-3-binding protein levels | 4e-35 | rs111526614 | 5 | GCST90247672 | no MR -> candidate analysis |
| Circulating DSG4 levels | 3e-30 | rs55842605 | 1 | GCST90860253 | no MR -> candidate analysis |
| DSG4 protein levels | 3e-29 | rs55842605 | 1 | GCST90469044 | no MR -> candidate analysis |
| DSG3/DSG4 protein level ratio | 2e-27 | rs7220336 | 1 | GCST90314558 | no MR -> candidate analysis |
| Height | 7e-17 | rs4789915 | 3 | GCST90245848 | no MR -> candidate analysis |
| Serum levels of protein LGALS3BP | 2e-12 | rs3826311 | 1 | GCST90088859 | no MR -> candidate analysis |
| Total PHF-tau (SNP x SNP interaction) | 2e-12 | rs4789907 x rs1124952 | 3 | GCST010340 | no MR -> candidate analysis |
| Physical function (baseline) | 2e-10 | rs56352914 | 1 | GCST90565837 | no MR -> candidate analysis |
| Metalloproteinase inhibitor 2 levels | 4e-10 | rs4789927 | 1 | GCST90424491 | no MR -> candidate analysis |
| Protein quantitative trait loci (liver) | 2e-8 | rs58996443 | 1 | GCST011427 | no MR -> candidate analysis |
| _...and 3 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 339 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| metabolic disease | 0.457 | — | common-variant locus | no MR -> candidate analysis |

> Of the 1 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Galectin-3-binding protein) |
| gnomAD constraint | pLI=7.6e-10, LOEUF=1.53 — LoF-tolerant |
| GWAS Catalog | 65 unique SNPs / 130 rows |
| ClinVar | 131 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 339 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'LGALS3BP' and resolved to 'Galectin-3-binding protein' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 131 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 15 of 15 traits by best p-value, aggregated from 26 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q08380 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000108679/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL6067101/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/LGALS3BP — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/LGALS3BP — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=LGALS3BP%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/LGALS3BP — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:31:00  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
