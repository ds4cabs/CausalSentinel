# Protein Dossier — CD33 (Myeloid cell surface antigen CD33)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Alzheimer's disease | 0.1 | 0.0185 | 6.66e-08 | Wald ratio | 1 | cis | 0.998 |
| Non-cancer illness code  self-reported: asthma | 0.0271 | 0.00739 | 2.50e-04 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I84 Haemorrhoids | 0.0479 | 0.0166 | 0.00391 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I30 Acute pericarditis | 0.31 | 0.115 | 0.00717 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: basal cell carcinoma | 0.0709 | 0.0264 | 0.00718 | Wald ratio | 1 | cis | NA |
| Platelet count | 1.19 | 0.467 | 0.0109 | Wald ratio | 1 | cis | NA |
| HbA1C | 0.00996 | 0.00403 | 0.0134 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | 0.00669 | 0.00271 | 0.0136 | Wald ratio | 1 | cis | NA |
| Diastolic blood pressure  automated reading | 0.00635 | 0.00278 | 0.0221 | Wald ratio | 1 | cis | NA |
| Weight | 0.00503 | 0.00239 | 0.0355 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Injury or trauma resulting in loss of vision | 0.0673 | 0.0331 | 0.0424 | Wald ratio | 1 | cis | NA |
| Pancreatic cancer | -0.11 | 0.0548 | 0.0438 | Wald ratio | 1 | cis | NA |
| _...and 101 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3166_92_1` | Siglec-3 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_201 association rows across 105 traits (189 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating CD33 levels | 2e-9500 | rs2455069 | 1 | GCST90860706 | no MR -> candidate analysis |
| Myeloid cell surface antigen CD33 levels | 3e-1638 | rs12459419 | 11 | GCST90248431 | no MR -> candidate analysis |
| Cerebrospinal fluid protein CD33 levels | 2e-524 | rs2455069 | 1 | GCST90944163 | no MR -> candidate analysis |
| Myeloid cell surface antigen CD33 levels (CD33.3166.92.1) | 9e-445 | rs12459419 | 2 | GCST90241989 | no MR -> candidate analysis |
| Blood protein levels | 6e-372 | rs1354106 | 1 | GCST006585 | no MR -> candidate analysis |
| CD33 protein levels | 4e-214 | rs117533019 | 12 | GCST90468625 | no MR -> candidate analysis |
| CD33 on CD33dim HLA DR+ CD11b+ | 2e-191 | rs3865444 | 2 | GCST90001948 | no MR -> candidate analysis |
| CD33 on CD14+ monocyte | 1e-190 | rs3865444 | 3 | GCST90001946 | no MR -> candidate analysis |
| CD33 on CD33+ HLA DR+ CD14- | 9e-189 | rs3865444 | 3 | GCST90001957 | no MR -> candidate analysis |
| CD33 on CD33+ HLA DR+ | 3e-187 | rs3865444 | 3 | GCST90001956 | no MR -> candidate analysis |
| CD33 on CD33+ HLA DR+ CD14dim | 8e-184 | rs3865444 | 2 | GCST90001947 | no MR -> candidate analysis |
| CD33 on CD33dim HLA DR+ CD11b- | 2e-183 | rs3865444 | 2 | GCST90001949 | no MR -> candidate analysis |
| _...and 93 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 633 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Alzheimer disease | 0.724 | — | common-variant locus | no MR -> candidate analysis |
| late-onset Alzheimers disease | 0.576 | — | common-variant locus | no MR -> candidate analysis |
| smoking initiation | 0.549 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 6 known modulators (Myeloid cell surface antigen CD33) |
| gnomAD constraint | pLI=1.3e-07, LOEUF=1.11 — LoF-tolerant |
| GWAS Catalog | 142 unique SNPs / 330 rows |
| ClinVar | 89 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 1 clinical annotations across 1 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 633 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'CD33' and resolved to 'Myeloid cell surface antigen CD33' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 89 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 20 of 105 traits by best p-value, aggregated from 201 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P20138 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000105383/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL1842/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CD33 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CD33 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CD33%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=CD33 — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CD33 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:42:18  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
