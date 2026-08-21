# Protein Dossier — SERPINF2 (Alpha-2-antiplasmin)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Heel bone mineral density (BMD) T-score  automated | 0.0514 | 0.017 | 0.00255 | Wald ratio | 1 | cis | NA |
| Creatinine (enzymatic) in urine | 0.0375 | 0.0126 | 0.00291 | Wald ratio | 1 | cis | NA |
| Potassium in urine | 0.0392 | 0.0134 | 0.00334 | Wald ratio | 1 | cis | NA |
| Weight | 0.0285 | 0.0116 | 0.0142 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M54 Dorsalgia | 0.204 | 0.084 | 0.015 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Cataract | -0.219 | 0.0903 | 0.0153 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: vaginal prolapse or uterine prolapse | 0.312 | 0.133 | 0.0192 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K60 Fissure and fistula of anal and rectal regions | 0.334 | 0.143 | 0.0194 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | 0.0307 | 0.0132 | 0.0196 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I80 Phlebitis and thrombophlebitis | 0.329 | 0.142 | 0.0207 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K57 Diverticular disease of intestine | -0.268 | 0.123 | 0.0296 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I83 Varicose veins of lower extremities | 0.167 | 0.0783 | 0.0327 | Wald ratio | 1 | cis | NA |
| _...and 63 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3024_18_2` | a2-Antiplasmin | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_50 association rows across 37 traits (45 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Albumin (maximum, inv-norm transformed) | 1e-60 | rs2070863 | 1 | GCST90479503 | no MR -> candidate analysis |
| Serum albumin levels | 9e-53 | rs1057335 | 3 | GCST90019493 | no MR -> candidate analysis |
| Albumin (mean, inv-norm transformed) | 2e-50 | rs2070863 | 2 | GCST90479504 | no MR -> candidate analysis |
| Albumin levels | 3e-40 | rs4790286 | 2 | GCST90662867 | no MR -> candidate analysis |
| Calcium levels | 4e-34 | rs1057335 | 1 | GCST90019500 | no MR -> candidate analysis |
| Albumin (minimum, inv-norm transformed) | 6e-31 | rs2070863 | 1 | GCST90479505 | no MR -> candidate analysis |
| Calcium (mean, inv-norm transformed) | 5e-30 | rs2070863 | 1 | GCST90479530 | no MR -> candidate analysis |
| Triglyceride levels | 9e-29 | rs7501750 | 1 | GCST90662893 | no MR -> candidate analysis |
| Calcium (maximum, inv-norm transformed) | 1e-26 | rs2070863 | 1 | GCST90479529 | no MR -> candidate analysis |
| Alzheimer's disease or family history of Alzheimer's disease | 5e-23 | rs1306536849 | 1 | GCST90624094 | no MR -> candidate analysis |
| Testosterone levels | 2e-20 | rs3976 | 3 | GCST90483498 | no MR -> candidate analysis |
| Total testosterone levels | 3e-20 | rs4525526 | 4 | GCST90012113 | no MR -> candidate analysis |
| _...and 25 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 285 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| alpha-2-plasmin inhibitor deficiency | 0.759 | — | established (curated) | no MR -> candidate analysis |
| Congenital alpha2 antiplasmin deficiency | 0.608 | — | established (curated) | no MR -> candidate analysis |
| Abnormal bleeding | 0.608 | — | established (curated) | no MR -> candidate analysis |
| hypogonadism | 0.55 | — | common-variant locus | no MR -> candidate analysis |
| Hodgkins lymphoma | 0.545 | — | common-variant locus | no MR -> candidate analysis |
| metabolic disease | 0.456 | — | common-variant locus | no MR -> candidate analysis |
| hyperlipidemia | 0.444 | — | common-variant locus | no MR -> candidate analysis |
| adolescent idiopathic scoliosis | 0.204 | — | common-variant locus | no MR -> candidate analysis |
| Abnormality of the skeletal system | 0.091 | — | common-variant locus | no MR -> candidate analysis |
| Alzheimer disease | 0.042 | — | common-variant locus | no MR -> candidate analysis |
| gout | 0.054 | — | common-variant locus | MR: beta=-0.104, p=0.403 (cis) |

> Of the 11 rows above, **10 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.97, LOEUF=0.513 — LoF-INTOLERANT |
| GWAS Catalog | 106 unique SNPs / 212 rows |
| ClinVar | 209 records; 4 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 285 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'SERPINF2'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 209 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 37 traits by best p-value, aggregated from 50 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P08697 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000167711/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/SERPINF2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/SERPINF2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=SERPINF2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/SERPINF2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:03:15  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
