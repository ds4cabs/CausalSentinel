# Protein Dossier — SLAMF7 (SLAM family member 7)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Ulcerative colitis | 0.0621 | 0.0157 | 7.35e-05 | Wald ratio | 1 | cis | NA |
| Multiple sclerosis | 0.0633 | 0.0196 | 0.00126 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: bladder problem (not cancer) | -0.109 | 0.0416 | 0.00893 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | 0.00588 | 0.00233 | 0.0116 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: depression | 0.0282 | 0.0114 | 0.0133 | Wald ratio | 1 | cis | NA |
| Inflammatory bowel disease | 0.0284 | 0.0123 | 0.0206 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: vaginal prolapse or uterine prolapse | -0.0933 | 0.0423 | 0.0275 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: mania or bipolar disorder or manic depression | -0.131 | 0.0637 | 0.0402 | Wald ratio | 1 | cis | NA |
| Pulse rate | -0.00994 | 0.00501 | 0.0472 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertrophic cardiomyopathy (hcm  or  hocm) | 0.295 | 0.152 | 0.0523 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hyperthyroidism or thyrotoxicosis | 0.0584 | 0.0311 | 0.0606 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R55 Syncope and collapse | -0.0553 | 0.0319 | 0.0827 | Wald ratio | 1 | cis | NA |
| _...and 50 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-5487_7_3` | SLAF7 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_82 association rows across 38 traits (79 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating SLAMF7 levels | 2e-3149 | rs11581248 | 8 | GCST90859745 | no MR -> candidate analysis |
| ICAM3/SLAMF7 protein level ratio | 3e-1976 | rs11265473 | 1 | GCST90315123 | no MR -> candidate analysis |
| LY96/SLAMF7 protein level ratio | 5e-1884 | rs11265473 | 1 | GCST90315347 | no MR -> candidate analysis |
| CD48/SLAMF7 protein level ratio | 7e-1715 | rs11265473 | 1 | GCST90313842 | no MR -> candidate analysis |
| SLAMF7/TXNDC15 protein level ratio | 2e-1641 | rs11265473 | 1 | GCST90315850 | no MR -> candidate analysis |
| Circulating LY9 levels | 2e-1425 | rs12405457 | 1 | GCST90860013 | no MR -> candidate analysis |
| SLAM family member 7 levels | 2e-1362 | rs11581248 | 12 | GCST90249565 | no MR -> candidate analysis |
| ICAM3/LY9 protein level ratio | 4e-781 | rs535241 | 1 | GCST90315121 | no MR -> candidate analysis |
| Circulating CD48 levels | 3e-534 | rs352684 | 1 | GCST90860011 | no MR -> candidate analysis |
| SLAM family member 7 levels (SLAMF7.5487.7.3) | 2e-397 | rs11581248 | 2 | GCST90242832 | no MR -> candidate analysis |
| SLAM family member 7 (analyte X5487.7) levels | 9e-213 | rs11581248 | 1 | GCST90426368 | no MR -> candidate analysis |
| Blood protein levels | 4e-208 | rs11581248 | 1 | GCST006585 | no MR -> candidate analysis |
| _...and 26 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 257 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| multiple sclerosis | 0.57 | — | common-variant locus | MR: beta=0.0633, p=0.00126 (cis) |
| Epstein-Barr virus infection | 0.532 | — | common-variant locus | no MR -> candidate analysis |
| rotator cuff syndrome | 0.459 | — | common-variant locus | no MR -> candidate analysis |
| Delayed puberty | 0.36 | — | common-variant locus | no MR -> candidate analysis |
| autism | 0.182 | — | established (curated) | no MR -> candidate analysis |

> Of the 5 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 2 known modulators (SLAM family member 7) |
| gnomAD constraint | pLI=1.6e-07, LOEUF=1.06 — LoF-tolerant |
| GWAS Catalog | 120 unique SNPs / 296 rows |
| ClinVar | 47 records; 3 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 257 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'SLAMF7' and resolved to 'SLAM family member 7' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 47 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 38 traits by best p-value, aggregated from 82 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9NQ25 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000026751/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3559386/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/SLAMF7 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/SLAMF7 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=SLAMF7%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/SLAMF7 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:08:14  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
