# Protein Dossier — PENK (Proenkephalin-A)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Height | -0.0322 | 0.00623 | 2.31e-07 | Wald ratio | 1 | cis | 3.2e-32 |
| Sodium in urine | 0.0162 | 0.0051 | 0.00145 | Wald ratio | 1 | cis | NA |
| Platelet count | 2.62 | 0.856 | 0.00225 | Wald ratio | 1 | cis | NA |
| Happiness | 0.019 | 0.00641 | 0.00299 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | -0.0132 | 0.00448 | 0.00318 | Wald ratio | 1 | cis | NA |
| Diastolic blood pressure  automated reading | 0.0148 | 0.0053 | 0.00518 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K29 Gastritis and duodenitis | 0.0848 | 0.0308 | 0.00588 | Wald ratio | 1 | cis | NA |
| Bulimia nervosa | -0.0473 | 0.0172 | 0.00596 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: enlarged prostate | 0.106 | 0.0399 | 0.00784 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | -0.0102 | 0.00425 | 0.0162 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R04 Haemorrhage from respiratory passages | 0.149 | 0.0622 | 0.0163 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | 0.0111 | 0.00518 | 0.0313 | Wald ratio | 1 | cis | NA |
| _...and 101 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_58 association rows across 34 traits (56 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Proenkephalin-A levels | 1e-236 | rs34217211 | 2 | GCST90248943 | no MR -> candidate analysis |
| Height | 1e-141 | rs2609996 | 5 | GCST90245848 | MR: beta=-0.0322, p=2.31e-07 (cis) |
| Serum levels of protein PENK | 2e-128 | rs2576575 | 1 | GCST90090491 | no MR -> candidate analysis |
| Proenkephalin-A levels (PENK.9076.25.3) | 1e-87 | rs2670014 | 2 | GCST90242379 | no MR -> candidate analysis |
| Blood protein levels | 8e-70 | rs2670014 | 1 | GCST006585 | no MR -> candidate analysis |
| Height (baseline) | 1e-51 | rs34242338 | 4 | GCST90565843 | no MR -> candidate analysis |
| Physical function (baseline) | 9e-30 | rs34242338 | 4 | GCST90565837 | no MR -> candidate analysis |
| Educational attainment | 8e-24 | rs1866823 | 2 | GCST90105038 | no MR -> candidate analysis |
| Whole body fat free mass (UKB data field 23101) | 3e-15 | rs34242338 | 2 | GCST90428120 | no MR -> candidate analysis |
| Educational attainment (years of education) | 3e-14 | rs2246873 | 2 | GCST006442 | no MR -> candidate analysis |
| Smoking initiation | 3e-14 | rs2670012 | 2 | GCST90243985 | no MR -> candidate analysis |
| Educational attainment (MTAG) | 5e-14 | rs1866823 | 1 | GCST006571 | no MR -> candidate analysis |
| _...and 22 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 327 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| type 2 diabetes mellitus | 0.744 | — | common-variant locus | no MR -> candidate analysis |
| diabetes mellitus | 0.477 | — | common-variant locus | no MR -> candidate analysis |
| smoking initiation | 0.438 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.42 | — | common-variant locus | no MR -> candidate analysis |
| urolithiasis | 0.411 | — | common-variant locus | no MR -> candidate analysis |
| brain aneurysm | 0.387 | — | common-variant locus | no MR -> candidate analysis |
| substance-related disorder | 0.35 | — | common-variant locus | no MR -> candidate analysis |
| diabetic ketoacidosis | 0.334 | — | common-variant locus | no MR -> candidate analysis |

> Of the 8 rows above, **8 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1.7e-09, LOEUF=1.45 — LoF-tolerant |
| GWAS Catalog | 49 unique SNPs / 98 rows |
| ClinVar | 89 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 327 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'PENK'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 89 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 34 traits by best p-value, aggregated from 58 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P01210 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000181195/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PENK — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PENK — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PENK%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/PENK — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:17:46  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
