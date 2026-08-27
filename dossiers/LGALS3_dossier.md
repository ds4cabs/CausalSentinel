# Protein Dossier — LGALS3 (Galectin-3)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: R07 Pain in throat and chest | 0.00409 | 0.00108 | 1.56e-04 | Inverse variance weighted | 3 | cis | NA |
| Diagnoses - main ICD10: R07 Pain in throat and chest | 0.00409 | 0.00108 | 1.56e-04 | Inverse variance weighted | 3 | trans | NA |
| Diagnoses - main ICD10: R07 Pain in throat and chest | 0.00409 | 0.00108 | 1.56e-04 | Inverse variance weighted | 3 | trans | NA |
| Body mass index (BMI) | 0.0152 | 0.00494 | 0.00202 | Inverse variance weighted | 3 | cis | NA |
| Body mass index (BMI) | 0.0152 | 0.00494 | 0.00202 | Inverse variance weighted | 3 | trans | NA |
| Body mass index (BMI) | 0.0152 | 0.00494 | 0.00202 | Inverse variance weighted | 3 | trans | NA |
| Ulcerative colitis | 0.293 | 0.0956 | 0.00218 | Wald ratio | 1 | trans | NA |
| Pulse rate | 0.0248 | 0.00866 | 0.00417 | Inverse variance weighted | 3 | cis | NA |
| Pulse rate | 0.0248 | 0.00866 | 0.00417 | Inverse variance weighted | 3 | trans | NA |
| Pulse rate | 0.0248 | 0.00866 | 0.00417 | Inverse variance weighted | 3 | trans | NA |
| Diagnoses - main ICD10: M17 Gonarthrosis [arthrosis of knee] | 0.00213 | 0.000764 | 0.00533 | Inverse variance weighted | 3 | cis | NA |
| Diagnoses - main ICD10: M17 Gonarthrosis [arthrosis of knee] | 0.00213 | 0.000764 | 0.00533 | Inverse variance weighted | 3 | trans | NA |
| _...and 281 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3066_12_1` | Galectin-3 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_28 association rows across 16 traits (26 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating LGALS3 levels | 8e-2158 | rs2075601 | 3 | GCST90859927 | no MR -> candidate analysis |
| LGALS3 protein levels | 5e-278 | rs78001930 | 8 | GCST90469761 | no MR -> candidate analysis |
| Galectin-3 levels | 3e-272 | rs76424323 | 4 | GCST90247671 | no MR -> candidate analysis |
| Protein biomarker | 2e-188 | rs2274273 | 1 | GCST001711 | no MR -> candidate analysis |
| Serum levels of protein LGALS3 | 8e-84 | rs112796738 | 1 | GCST90088218 | no MR -> candidate analysis |
| Blood protein levels | 3e-45 | rs76426991 | 1 | GCST006585 | no MR -> candidate analysis |
| DAAM1 protein levels | 4e-13 | rs7160523 | 1 | GCST90468941 | no MR -> candidate analysis |
| Red cell distribution width | 8e-11 | rs8012156 | 1 | GCST90002404 | no MR -> candidate analysis |
| Triglycerides to total lipids ratio in chylomicrons and extr | 2e-9 | rs750614951 | 1 | GCST90093051 | no MR -> candidate analysis |
| Galectin 3 plasma levels | 1e-8 | rs6573005 | 1 | GCST90085736 | no MR -> candidate analysis |
| Cholesteryl esters to total lipids ratio in chylomicrons and | 2e-8 | rs750614951 | 1 | GCST90093043 | no MR -> candidate analysis |
| T-cell surface glycoprotein CD3 epsilon chain protein levels | 2e-8 | rs112756125 | 1 | GCST90443215 | no MR -> candidate analysis |
| _...and 4 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 2160 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Hypercholesterolemia | 0.365 | — | common-variant locus | MR: beta=0.00759, p=0.308 (cis) |
| osteoarthritis | 0.263 | — | common-variant locus | MR: beta=0.0935, p=0.124 (cis) |
| arthropathy | 0.256 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 3 known modulators (Galectin-3) |
| gnomAD constraint | pLI=3.1e-06, LOEUF=1.29 — LoF-tolerant |
| GWAS Catalog | 42 unique SNPs / 82 rows |
| ClinVar | 73 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 1 clinical annotations across 1 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 2160 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'LGALS3' and resolved to 'Galectin-3' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 73 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 16 of 16 traits by best p-value, aggregated from 28 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P17931 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000131981/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4531/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/LGALS3 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/LGALS3 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=LGALS3%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=LGALS3 — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/LGALS3 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:30:41  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
