# Protein Dossier — SERPINA3 (Alpha-1-antichymotrypsin)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: M54 Dorsalgia | 0.181 | 0.0473 | 1.28e-04 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: basal cell carcinoma | -0.302 | 0.104 | 0.00379 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | -0.0167 | 0.0063 | 0.00808 | Wald ratio | 1 | cis | NA |
| Urinary albumin-to-creatinine ratio | -0.0463 | 0.0178 | 0.00939 | Wald ratio | 1 | cis | NA |
| Height | -0.0213 | 0.00902 | 0.0183 | Wald ratio | 1 | cis | NA |
| Caudate volume | -32.9 | 14.5 | 0.0234 | Wald ratio | 1 | cis | NA |
| Anorexia nervosa | -0.215 | 0.0951 | 0.0236 | Wald ratio | 1 | cis | NA |
| Microalbuminuria | -0.139 | 0.0625 | 0.0263 | Wald ratio | 1 | cis | NA |
| Red blood cell count | -0.0148 | 0.00671 | 0.0273 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R11 Nausea and vomiting | 0.203 | 0.0957 | 0.0343 | Wald ratio | 1 | cis | NA |
| Myocardial infarction | 0.0702 | 0.0336 | 0.0366 | Wald ratio | 1 | cis | NA |
| Alcohol intake frequency | -0.0222 | 0.0108 | 0.0392 | Wald ratio | 1 | cis | NA |
| _...and 99 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2879_9_2` | a1-Antichymotrypsin | Suhre K | 2019 |
| `prot-c-4153_11_2` | alpha-1-antichymotrypsin complex | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_55 association rows across 24 traits (52 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| alpha-1-antichymotrypsin complex levels | 7e-200 | rs8023057 | 6 | GCST90246389 | no MR -> candidate analysis |
| SERPINA5 protein levels | 2e-187 | rs1130267 | 7 | GCST90470585 | no MR -> candidate analysis |
| Circulating CTSL levels | 3e-106 | rs6575449 | 2 | GCST90859820 | no MR -> candidate analysis |
| SERPINA3 protein levels | 1e-94 | rs10129374 | 2 | GCST90470583 | no MR -> candidate analysis |
| SERPINA4 protein levels | 3e-78 | rs61976079 | 3 | GCST90470584 | no MR -> candidate analysis |
| Cathepsin L1 levels | 2e-64 | rs6575449 | 1 | GCST90012073 | no MR -> candidate analysis |
| SERPINA12 protein levels | 1e-62 | rs61976121 | 10 | GCST90470581 | no MR -> candidate analysis |
| SERPINA11 protein levels | 2e-58 | rs11622033 | 1 | GCST90470580 | no MR -> candidate analysis |
| CELA3A protein levels | 8e-47 | rs6575449 | 1 | GCST90468702 | no MR -> candidate analysis |
| Plasma serine protease inhibitor levels | 7e-35 | rs4062 | 1 | GCST90248892 | no MR -> candidate analysis |
| Alpha-1-antichymotrypsin levels | 2e-21 | rs8023057 | 3 | GCST90246388 | no MR -> candidate analysis |
| Prostate-specific antigen levels | 1e-20 | rs58643524 | 2 | GCST90461907 | no MR -> candidate analysis |
| _...and 12 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 640 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| prostate carcinoma | 0.543 | — | common-variant locus | no MR -> candidate analysis |
| peripheral arterial occlusive disease 1 | 0.195 | — | established (curated) | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Alpha-1-antichymotrypsin) |
| gnomAD constraint | pLI=3.6e-13, LOEUF=1.61 — LoF-tolerant |
| GWAS Catalog | 134 unique SNPs / 340 rows |
| ClinVar | 148 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 1 clinical annotations across 1 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 640 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'SERPINA3' and resolved to 'Alpha-1-antichymotrypsin' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 148 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 20 of 24 traits by best p-value, aggregated from 55 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P01011 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000196136/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL5960/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/SERPINA3 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/SERPINA3 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=SERPINA3%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=SERPINA3 — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/SERPINA3 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:01:41  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
