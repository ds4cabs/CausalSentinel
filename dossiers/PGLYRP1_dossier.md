# Protein Dossier — PGLYRP1 (Peptidoglycan recognition protein 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Forced vital capacity (FVC) | -0.0264 | 0.00967 | 0.00637 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: vitiligo | 0.897 | 0.329 | 0.00648 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | -0.0259 | 0.0102 | 0.011 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: gout | 0.181 | 0.0831 | 0.0292 | Wald ratio | 1 | cis | NA |
| Alzheimer's disease | -0.167 | 0.0793 | 0.0358 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R35 Polyuria | 0.298 | 0.144 | 0.0376 | Wald ratio | 1 | cis | NA |
| Diastolic blood pressure  automated reading | 0.0251 | 0.0121 | 0.0379 | Wald ratio | 1 | cis | NA |
| Fracture resulting from simple fall | -0.0684 | 0.0333 | 0.0402 | Wald ratio | 1 | cis | NA |
| Sleep duration | -0.0186 | 0.0092 | 0.0431 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | -0.0306 | 0.0152 | 0.0448 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: osteoporosis | 0.152 | 0.0819 | 0.064 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: joint disorder | -0.507 | 0.322 | 0.116 | Wald ratio | 1 | cis | NA |
| _...and 60 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3329_14_2` | PGRP-S | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_12 association rows across 11 traits (11 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| LCN2/PGLYRP1 protein level ratio | 1e-819 | rs12980641 | 1 | GCST90315306 | no MR -> candidate analysis |
| Circulating PGLYRP1 levels | 3e-571 | rs35247686 | 1 | GCST90859968 | no MR -> candidate analysis |
| Peptidoglycan recognition protein 1 levels | 1e-39 | rs12462367 | 1 | GCST90248985 | no MR -> candidate analysis |
| Serum levels of protein PGLYRP1 | 2e-22 | rs12973391 | 1 | GCST90088320 | no MR -> candidate analysis |
| Blood protein levels | 1e-17 | rs12980641 | 1 | GCST006585 | no MR -> candidate analysis |
| Peptidoglycan recognition protein 1 levels (PGLYRP1.3329.14. | 5e-17 | rs8102493 | 1 | GCST90242213 | no MR -> candidate analysis |
| GLIPR1 protein levels | 1e-15 | rs191272469 | 1 | GCST90469357 | no MR -> candidate analysis |
| Total PHF-tau (SNP x SNP interaction) | 4e-14 | rs12663388 x rs12982353 | 2 | GCST010340 | no MR -> candidate analysis |
| Peptidoglycan recognition protein 1 (analyte X3329.14) level | 4e-11 | rs12980641 | 1 | GCST90425701 | no MR -> candidate analysis |
| Cerebrospinal fluid protein PGLYRP1 levels | 5e-10 | rs8102493 | 1 | GCST90944855 | no MR -> candidate analysis |
| Whole brain grey matter density | 3e-6 | rs2005893 | 1 | GCST009200 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 319 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| dementia | 0.29 | — | common-variant locus | no MR -> candidate analysis |
| neurodegenerative disease | 0.213 | — | common-variant locus | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=2e-07, LOEUF=1.64 — LoF-tolerant |
| GWAS Catalog | 40 unique SNPs / 80 rows |
| ClinVar | 58 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 319 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'PGLYRP1'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 58 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 11 of 11 traits by best p-value, aggregated from 12 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O75594 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000008438/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PGLYRP1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PGLYRP1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PGLYRP1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/PGLYRP1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:19:02  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
