# Protein Dossier — CD14 (Monocyte differentiation antigen CD14)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Systolic blood pressure  automated reading | -0.0216 | 0.00738 | 0.00335 | Inverse variance weighted | 2 | trans | NA |
| Systolic blood pressure  automated reading | -0.0216 | 0.00738 | 0.00335 | Inverse variance weighted | 2 | cis | NA |
| IgA nephropathy | -0.585 | 0.235 | 0.0126 | Inverse variance weighted | 2 | trans | NA |
| IgA nephropathy | -0.585 | 0.235 | 0.0126 | Inverse variance weighted | 2 | cis | NA |
| Diagnoses - main ICD10: R07 Pain in throat and chest | -0.132 | 0.0568 | 0.0201 | Inverse variance weighted | 2 | trans | NA |
| Diagnoses - main ICD10: R07 Pain in throat and chest | -0.132 | 0.0568 | 0.0201 | Inverse variance weighted | 2 | cis | NA |
| Diagnoses - main ICD10: R11 Nausea and vomiting | 0.212 | 0.0938 | 0.0238 | Inverse variance weighted | 2 | trans | NA |
| Diagnoses - main ICD10: R11 Nausea and vomiting | 0.212 | 0.0938 | 0.0238 | Inverse variance weighted | 2 | cis | NA |
| Lumbar spine bone mineral density | -0.0586 | 0.0264 | 0.0265 | Inverse variance weighted | 2 | trans | NA |
| Lumbar spine bone mineral density | -0.0586 | 0.0264 | 0.0265 | Inverse variance weighted | 2 | cis | NA |
| Parkinson's disease | -0.518 | 0.234 | 0.0272 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: K29 Gastritis and duodenitis | 0.0933 | 0.0426 | 0.0285 | Inverse variance weighted | 2 | trans | NA |
| _...and 193 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_45 association rows across 27 traits (43 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Soluble CD14 levels | 7e-124 | rs75652866 | 3 | GCST90093300 | no MR -> candidate analysis |
| Monocyte differentiation antigen CD14 levels | 2e-73 | rs5744441 | 3 | GCST90246929 | no MR -> candidate analysis |
| CD14 protein levels | 3e-68 | rs190828983 | 4 | GCST90468598 | no MR -> candidate analysis |
| Height | 2e-63 | rs2569193 | 2 | GCST90245848 | MR: beta=-0.0593, p=0.11 (trans) |
| Monocyte differentiation antigen CD14, soluble levels | 2e-52 | rs5744454 | 3 | GCST90249440 | no MR -> candidate analysis |
| Cerebrospinal fluid protein CD14 levels | 2e-46 | rs2569193 | 1 | GCST90944962 | no MR -> candidate analysis |
| CPXM1/HBEGF protein level ratio | 1e-27 | rs778582 | 1 | GCST90314219 | no MR -> candidate analysis |
| Serum levels of protein CD14 | 6e-20 | rs60745418 | 1 | GCST90090416 | no MR -> candidate analysis |
| HLA class II histocompatibility antigen, DR beta 3 chain lev | 3e-16 | rs778583 | 1 | GCST90426852 | no MR -> candidate analysis |
| Monocyte differentiation antigen CD14, soluble level in Chro | 1e-15 | rs75652866 | 1 | GCST90234613 | no MR -> candidate analysis |
| Monocyte differentiation antigen CD14 level in Chronic kidne | 4e-14 | rs5744451 | 1 | GCST90239125 | no MR -> candidate analysis |
| Body shape phenotype PC2 | 5e-14 | rs2569178 | 1 | GCST90832990 | no MR -> candidate analysis |
| _...and 15 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1347 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| gout | 0.249 | — | common-variant locus | no MR -> candidate analysis |
| Back pain | 0.223 | — | common-variant locus | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 2 known modulators (Monocyte differentiation antigen CD14) |
| gnomAD constraint | pLI=0.0085, LOEUF=3.72 — LoF-tolerant |
| GWAS Catalog | 72 unique SNPs / 144 rows |
| ClinVar | 74 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 1 clinical annotations across 1 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1347 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'CD14' and resolved to 'Monocyte differentiation antigen CD14' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 74 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 20 of 27 traits by best p-value, aggregated from 45 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P08571 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000170458/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2384897/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CD14 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CD14 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CD14%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=CD14 — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CD14 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:40:25  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
