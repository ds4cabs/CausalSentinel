# Protein Dossier — SIGLEC7 (Sialic acid-binding Ig-like lectin 7)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: I84 Haemorrhoids | 0.146 | 0.0458 | 0.00147 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R55 Syncope and collapse | 0.207 | 0.0714 | 0.00371 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M54 Dorsalgia | -0.189 | 0.0778 | 0.015 | Wald ratio | 1 | cis | NA |
| High grade serous ovarian cancer | 0.153 | 0.0633 | 0.0158 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: C61 Malignant neoplasm of prostate | 0.184 | 0.0847 | 0.03 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: G47 Sleep disorders | 0.192 | 0.0894 | 0.0313 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: D12 Benign neoplasm of colon  rectum  anus and anal canal | 0.128 | 0.0614 | 0.0371 | Wald ratio | 1 | cis | NA |
| Endometrioid ovarian cancer | -0.226 | 0.109 | 0.0385 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I83 Varicose veins of lower extremities | 0.107 | 0.0518 | 0.0396 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K43 Ventral hernia | 0.208 | 0.102 | 0.0407 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R04 Haemorrhage from respiratory passages | 0.195 | 0.0952 | 0.0409 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: G56 Mononeuropathies of upper limb | 0.113 | 0.0561 | 0.0441 | Wald ratio | 1 | cis | NA |
| _...and 48 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2742_68_2` | Siglec-7 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_27 association rows across 9 traits (27 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating SIGLEC7 levels | 3e-594 | rs140185670 | 3 | GCST90860368 | no MR -> candidate analysis |
| CD33 protein levels | 4e-204 | rs140185670 | 7 | GCST90468625 | no MR -> candidate analysis |
| Sialic acid-binding Ig-like lectin 7 levels | 1e-126 | rs140185670 | 7 | GCST90249551 | no MR -> candidate analysis |
| SIGLEC7 protein levels | 2e-64 | rs77067043 | 2 | GCST90470635 | no MR -> candidate analysis |
| Sialic acid-binding Ig-like lectin 7 levels (SIGLEC7.2742.68 | 2e-36 | rs140185670 | 1 | GCST90242811 | no MR -> candidate analysis |
| SIGLEC9 protein levels | 1e-27 | rs141544900 | 4 | GCST90470637 | no MR -> candidate analysis |
| KLK13 protein levels | 9e-23 | rs3793436 | 1 | GCST90469699 | no MR -> candidate analysis |
| Serum levels of protein SIGLEC7 | 2e-16 | rs137953543 | 1 | GCST90088042 | no MR -> candidate analysis |
| Myeloid cell surface antigen CD33 levels | 2e-12 | rs117658654 | 1 | GCST90161642 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 88 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| benign urinary system neoplasm | 0.092 | — | common-variant locus | no MR -> candidate analysis |
| benign neoplasm | 0.086 | — | common-variant locus | MR: beta=0.128, p=0.0371 (cis) |

> Of the 2 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Sialic acid-binding Ig-like lectin 7) |
| gnomAD constraint | pLI=8.2e-10, LOEUF=1.08 — LoF-tolerant |
| GWAS Catalog | 155 unique SNPs / 396 rows |
| ClinVar | 93 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 88 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'SIGLEC7' and resolved to 'Sialic acid-binding Ig-like lectin 7' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 93 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 9 of 9 traits by best p-value, aggregated from 27 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9Y286 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000168995/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3603730/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/SIGLEC7 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/SIGLEC7 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=SIGLEC7%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/SIGLEC7 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:06:18  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
