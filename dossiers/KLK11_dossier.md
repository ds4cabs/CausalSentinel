# Protein Dossier — KLK11 (Kallikrein-11)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Sodium in urine | -0.0101 | 0.00364 | 0.00554 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: high cholesterol | -0.0252 | 0.0103 | 0.014 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Diabetes related eye disease | 0.0979 | 0.043 | 0.0229 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: G47 Sleep disorders | -0.124 | 0.0549 | 0.0233 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: uterine fibroids | -0.0729 | 0.0322 | 0.0235 | Wald ratio | 1 | cis | NA |
| Microalbuminuria | -0.0918 | 0.0434 | 0.0344 | Wald ratio | 1 | cis | NA |
| Urinary albumin-to-creatinine ratio | -0.0309 | 0.015 | 0.0398 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: gout | -0.0671 | 0.0332 | 0.0434 | Wald ratio | 1 | cis | NA |
| Serum cystatin C (eGFRcys) | 0.0076 | 0.00384 | 0.0479 | Wald ratio | 1 | cis | NA |
| Creatinine (enzymatic) in urine | -0.00689 | 0.00354 | 0.0521 | Wald ratio | 1 | cis | NA |
| Potassium in urine | -0.00704 | 0.00376 | 0.0612 | Wald ratio | 1 | cis | NA |
| Rheumatoid arthritis | -0.0486 | 0.026 | 0.0616 | Wald ratio | 1 | cis | NA |
| _...and 89 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2831_29_1` | Kallikrein 11 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_33 association rows across 22 traits (32 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| kallikrein-11 levels | 2e-1041 | rs1048328 | 9 | GCST90248156 | no MR -> candidate analysis |
| Circulating KLK10 levels | 1e-777 | rs2691208 | 1 | GCST90860356 | no MR -> candidate analysis |
| Kallikrein-11 (analyte X2831.29) levels | 1e-394 | rs1048328 | 1 | GCST90425490 | no MR -> candidate analysis |
| Kallikrein-11 (analyte X7775.15) levels | 5e-379 | rs1048328 | 1 | GCST90427060 | no MR -> candidate analysis |
| Blood protein levels | 1e-261 | rs1048328 | 2 | GCST006585 | no MR -> candidate analysis |
| Circulating KLK11 levels | 5e-186 | rs62117662 | 1 | GCST90860017 | no MR -> candidate analysis |
| Kallikrein-11 levels (KLK11.2831.29.1) | 6e-186 | rs1048328 | 1 | GCST90241670 | no MR -> candidate analysis |
| KLK11 protein levels | 2e-178 | rs62117662 | 2 | GCST90469697 | no MR -> candidate analysis |
| Serum levels of protein KLK11 | 6e-153 | rs1048328 | 1 | GCST90089823 | no MR -> candidate analysis |
| Protein S100-P levels | 7e-56 | rs1048328 | 1 | GCST90427997 | no MR -> candidate analysis |
| Kallikrein-10 levels | 2e-33 | rs3745539 | 1 | GCST90179343 | no MR -> candidate analysis |
| KLK7 protein levels | 9e-29 | rs143406762 | 1 | GCST90469706 | no MR -> candidate analysis |
| _...and 10 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 412 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| ichthyosis with erythrokeratoderma | 0.745 | — | established (curated) | no MR -> candidate analysis |
| hereditary disease | 0.315 | — | established (curated) | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Kallikrein-11) |
| gnomAD constraint | pLI=0.22, LOEUF=0.725 — LoF-tolerant |
| GWAS Catalog | 172 unique SNPs / 454 rows |
| ClinVar | 78 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 412 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'KLK11' and resolved to 'Kallikrein-11' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 78 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 22 traits by best p-value, aggregated from 33 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9UBX7 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000167757/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3031/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/KLK11 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/KLK11 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=KLK11%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/KLK11 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:23:05  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
