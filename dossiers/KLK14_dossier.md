# Protein Dossier — KLK14 (Kallikrein-14)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: S76 Injury of muscle and tendon at hip and thigh level | 0.432 | 0.144 | 0.0027 | Wald ratio | 1 | cis | NA |
| ER-negative Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | 0.0541 | 0.021 | 0.0102 | Wald ratio | 1 | cis | NA |
| Squamous cell lung cancer | -0.123 | 0.0479 | 0.0104 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: retinal detachment | 0.167 | 0.0675 | 0.0131 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | 0.0112 | 0.00455 | 0.0142 | Wald ratio | 1 | cis | NA |
| Small vessel disease | -0.155 | 0.0663 | 0.0194 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: D25 Leiomyoma of uterus | -0.102 | 0.0446 | 0.0226 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: L03 Cellulitis | 0.103 | 0.0458 | 0.0246 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K40 Inguinal hernia | -0.066 | 0.0298 | 0.0266 | Wald ratio | 1 | cis | NA |
| Mean platelet volume | -0.00435 | 0.00209 | 0.0372 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: C61 Malignant neoplasm of prostate | 0.104 | 0.0505 | 0.0396 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: joint disorder | -0.158 | 0.0784 | 0.0446 | Wald ratio | 1 | cis | NA |
| _...and 96 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3681_87_3` | kallikrein 14 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_71 association rows across 28 traits (69 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating KLK14 levels | 3e-856 | rs2569491 | 5 | GCST90860034 | no MR -> candidate analysis |
| Circulating KLK13 levels | 1e-322 | rs2569476 | 2 | GCST90860002 | no MR -> candidate analysis |
| KLK14 protein levels | 8e-231 | rs34093024 | 12 | GCST90469700 | no MR -> candidate analysis |
| Kallikrein-14 levels (KLK14.8620.56.3) | 4e-119 | rs2569491 | 2 | GCST90241672 | no MR -> candidate analysis |
| Serum levels of protein KLK14 | 9e-114 | rs2569491 | 2 | GCST90090240 | no MR -> candidate analysis |
| KLK13 protein levels | 2e-110 | rs7253072 | 4 | GCST90469699 | no MR -> candidate analysis |
| CD33 protein levels | 2e-106 | rs867191 | 3 | GCST90468625 | no MR -> candidate analysis |
| Blood protein levels | 3e-86 | rs2569491 | 2 | GCST006585 | no MR -> candidate analysis |
| Sialic acid-binding Ig-like lectin 9 levels | 3e-73 | rs2691273 | 5 | GCST90101552 | no MR -> candidate analysis |
| KLK12 protein levels | 1e-68 | rs2569495 | 9 | GCST90469698 | no MR -> candidate analysis |
| SIGLEC9 protein levels | 3e-53 | rs73051055 | 5 | GCST90470637 | no MR -> candidate analysis |
| Circulating SIGLEC7 levels | 2e-47 | rs2569495 | 1 | GCST90860368 | no MR -> candidate analysis |
| _...and 16 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 117 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| alcohol drinking | 0.191 | — | common-variant locus | no MR -> candidate analysis |
| male infertility | 0.182 | — | established (curated) | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Kallikrein-14) |
| gnomAD constraint | pLI=5.5e-07, LOEUF=1.23 — LoF-tolerant |
| GWAS Catalog | 175 unique SNPs / 448 rows |
| ClinVar | 56 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 117 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'KLK14' and resolved to 'Kallikrein-14' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 56 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 28 traits by best p-value, aggregated from 71 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9P0G3 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000129437/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2641/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/KLK14 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/KLK14 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=KLK14%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/KLK14 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:24:17  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
