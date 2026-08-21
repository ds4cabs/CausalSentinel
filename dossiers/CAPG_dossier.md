# Protein Dossier — CAPG (Condensin complex subunit 3)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Hearing difficulty or problems: Yes | -0.0544 | 0.0141 | 1.18e-04 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | -0.0184 | 0.00636 | 0.00376 | Wald ratio | 1 | cis | NA |
| Pulse rate | 0.0381 | 0.0137 | 0.00542 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | 0.0215 | 0.00776 | 0.00558 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | -0.0171 | 0.00671 | 0.011 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N40 Hyperplasia of prostate | -0.252 | 0.105 | 0.0166 | Wald ratio | 1 | cis | NA |
| Amygdala volume | -22.8 | 10.1 | 0.0239 | Wald ratio | 1 | cis | NA |
| Pallidum volume | -15.5 | 7.59 | 0.0414 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertension | 0.0259 | 0.0129 | 0.0442 | Wald ratio | 1 | cis | NA |
| Nucleus accumbens volume | -9.21 | 4.66 | 0.0481 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K20 Oesophagitis | 0.132 | 0.069 | 0.0556 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: asthma | 0.039 | 0.0209 | 0.0626 | Wald ratio | 1 | cis | NA |
| _...and 72 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-4968_50_1` | CAPG | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_37 association rows across 13 traits (37 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| AMBP/CAPG protein level ratio | 2e-4277 | rs6886 | 1 | GCST90313252 | no MR -> candidate analysis |
| Circulating CAPG levels | 2e-789 | rs2002444 | 3 | GCST90860271 | no MR -> candidate analysis |
| CAPG protein levels | 7e-301 | rs75000263 | 7 | GCST90468537 | no MR -> candidate analysis |
| Macrophage-capping protein levels | 3e-207 | rs62623452 | 4 | GCST90248382 | no MR -> candidate analysis |
| TGOLN2 protein levels | 2e-143 | rs11681965 | 14 | GCST90470850 | no MR -> candidate analysis |
| Cerebrospinal fluid protein CAPG levels | 9e-90 | rs6886 | 1 | GCST90943116 | no MR -> candidate analysis |
| platelet count (minimum, inv-norm transformed) | 2e-25 | rs62162752 | 1 | GCST90480652 | no MR -> candidate analysis |
| platelet count (mean, inv-norm transformed) | 3e-25 | rs62162752 | 1 | GCST90480651 | no MR -> candidate analysis |
| Platelet count | 7e-18 | rs3770102 | 1 | GCST90662907 | no MR -> candidate analysis |
| platelet count (maximum, inv-norm transformed) | 1e-17 | rs62162752 | 1 | GCST90480650 | no MR -> candidate analysis |
| Serum levels of protein CAPG | 1e-10 | rs35666320 | 1 | GCST90088833 | no MR -> candidate analysis |
| Diastolic blood pressure (MTAG) | 2e-9 | rs111384899 | 1 | GCST90449057 | no MR -> candidate analysis |
| _...and 1 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 207 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Sensorineural hearing impairment | 0.584 | — | common-variant locus | no MR -> candidate analysis |
| cerebral atherosclerosis | 0.041 | — | common-variant locus | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Macrophage-capping protein) |
| gnomAD constraint | pLI=2e-08, LOEUF=0.964 — LoF-tolerant |
| GWAS Catalog | 111 unique SNPs / 256 rows |
| ClinVar | 89 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 1 clinical annotations across 1 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 207 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'CAPG' and resolved to 'Macrophage-capping protein' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 89 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 13 of 13 traits by best p-value, aggregated from 37 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9BPX3 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000042493/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL6066906/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CAPG — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CAPG — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CAPG%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=CAPG — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CAPG — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:27:36  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
