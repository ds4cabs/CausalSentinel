# Protein Dossier — HGFAC (Hepatocyte growth factor activator serine protease)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Forced vital capacity (FVC) | 0.0168 | 0.00403 | 3.17e-05 | Wald ratio | 1 | cis | NA |
| Height | 0.0304 | 0.00792 | 1.20e-04 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | 0.016 | 0.00425 | 1.75e-04 | Wald ratio | 1 | cis | NA |
| Endometrioid ovarian cancer | -0.164 | 0.0594 | 0.00564 | Wald ratio | 1 | cis | NA |
| Alzheimer's disease | 0.084 | 0.0341 | 0.0137 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R11 Nausea and vomiting | -0.21 | 0.0976 | 0.0316 | Wald ratio | 1 | cis | NA |
| Ovarian cancer | -0.06 | 0.0281 | 0.0329 | Wald ratio | 1 | cis | NA |
| Red blood cell count | 0.0136 | 0.00639 | 0.0334 | Wald ratio | 1 | cis | NA |
| Weight | 0.00922 | 0.00434 | 0.0337 | Wald ratio | 1 | cis | NA |
| High grade serous ovarian cancer | -0.0702 | 0.0334 | 0.0354 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: G47 Sleep disorders | 0.12 | 0.057 | 0.0356 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: high cholesterol | -0.0285 | 0.0137 | 0.0372 | Wald ratio | 1 | cis | NA |
| _...and 87 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3617_80_4` | HGFA | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_958 association rows across 540 traits (946 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Hepatocyte growth factor activator levels | 6e-1632 | rs2498323 | 8 | GCST90247876 | no MR -> candidate analysis |
| Blood protein levels | 2e-476 | rs2498323 | 2 | GCST006585 | no MR -> candidate analysis |
| Albumin levels | 4e-231 | rs13108218 | 13 | GCST90662901 | no MR -> candidate analysis |
| Hepatocyte growth factor activator (analyte X3617.80) levels | 1e-226 | rs2498323 | 1 | GCST90425833 | no MR -> candidate analysis |
| HGFAC protein levels | 4e-225 | rs34491545 | 10 | GCST90469448 | no MR -> candidate analysis |
| Hepatocyte growth factor activator (analyte X8385.248) level | 2e-187 | rs2498323 | 1 | GCST90427369 | no MR -> candidate analysis |
| Sex hormone-binding globulin levels adjusted for BMI | 3e-172 | rs13108218 | 3 | GCST90012110 | no MR -> candidate analysis |
| Triglyceride levels | 1e-163 | rs13108218 | 17 | GCST90662893 | no MR -> candidate analysis |
| Sex hormone-binding globulin levels | 9e-129 | rs13108218 | 16 | GCST90012111 | no MR -> candidate analysis |
| Circulating HGF levels (id: OID00522_OID20656) | 2e-119 | rs59950280 | 4 | GCST90859878 | no MR -> candidate analysis |
| C1QTNF1/COL4A1 protein level ratio | 6e-100 | rs2498323 | 1 | GCST90313552 | no MR -> candidate analysis |
| Serum levels of protein HGFAC | 7e-97 | rs3752440 | 2 | GCST90088461 | no MR -> candidate analysis |
| _...and 528 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 216 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Hypercholesterolemia | 0.825 | — | common-variant locus | MR: beta=-0.0285, p=0.0372 (cis) |
| metabolic disease | 0.8 | — | common-variant locus | no MR -> candidate analysis |
| hyperlipidemia | 0.717 | — | common-variant locus | no MR -> candidate analysis |
| coronary artery disorder | 0.682 | — | common-variant locus | no MR -> candidate analysis |
| inflammatory bowel disease | 0.594 | — | common-variant locus | no MR -> candidate analysis |
| Crohn disease | 0.594 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.594 | — | common-variant locus | no MR -> candidate analysis |
| cholelithiasis | 0.587 | — | common-variant locus | MR: beta=-0.0541, p=0.135 (cis) |
| familial hypercholesterolemia | 0.584 | — | common-variant locus | no MR -> candidate analysis |
| Disorder of lipid metabolism | 0.542 | — | common-variant locus | no MR -> candidate analysis |
| familial hyperlipidemia | 0.512 | — | common-variant locus | no MR -> candidate analysis |
| ischemic stroke | 0.506 | — | common-variant locus | MR: beta=0.0666, p=0.12 (cis) |
| gallstones | 0.479 | — | common-variant locus | no MR -> candidate analysis |
| cardiovascular disorder | 0.476 | — | common-variant locus | no MR -> candidate analysis |
| venous thromboembolism | 0.476 | — | common-variant locus | no MR -> candidate analysis |

> Of the 15 rows above, **12 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 1 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Hepatocyte growth factor activator serine protease) |
| gnomAD constraint | pLI=4.2e-28, LOEUF=1.3 — LoF-tolerant |
| GWAS Catalog | 129 unique SNPs / 324 rows |
| ClinVar | 324 records; 11 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 216 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'HGFAC' and resolved to 'Hepatocyte growth factor activator serine protease' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 324 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 540 traits by best p-value, aggregated from 958 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q04756 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000109758/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3351190/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/HGFAC — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/HGFAC — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=HGFAC%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/HGFAC — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:00:20  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
