# Protein Dossier — CST5 (Cystatin-D)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Serum cystatin C (eGFRcys) | 0.0209 | 0.00348 | 1.97e-09 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: mania or bipolar disorder or manic depression | 0.192 | 0.0707 | 0.00664 | Wald ratio | 1 | cis | NA |
| Paget's disease | -0.289 | 0.117 | 0.0132 | Wald ratio | 1 | cis | NA |
| HDL cholesterol | 0.0213 | 0.00892 | 0.0168 | Wald ratio | 1 | cis | NA |
| Mean cell volume | -0.105 | 0.0463 | 0.0235 | Wald ratio | 1 | cis | NA |
| Depressive symptoms | -0.0125 | 0.00557 | 0.0244 | Wald ratio | 1 | cis | NA |
| Neuroticism | -0.0153 | 0.00697 | 0.0278 | Wald ratio | 1 | cis | NA |
| Body fat | 0.0203 | 0.00975 | 0.037 | Wald ratio | 1 | cis | NA |
| Transferrin | -0.0379 | 0.0188 | 0.0439 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R04 Haemorrhage from respiratory passages | 0.108 | 0.0544 | 0.0464 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: uterine fibroids | 0.0611 | 0.0331 | 0.0649 | Wald ratio | 1 | cis | NA |
| Anorexia nervosa | -0.0903 | 0.0498 | 0.0699 | Wald ratio | 1 | cis | NA |
| _...and 84 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3803_10_2` | CYTD | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_57 association rows across 19 traits (51 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating CST5 levels | 2e-3604 | rs4239743 | 3 | GCST90859850 | no MR -> candidate analysis |
| Cystatin D levels | 2e-541 | rs4815244 | 2 | GCST90274777 | no MR -> candidate analysis |
| Cystatin-D levels | 8e-500 | rs4642010 | 9 | GCST90247217 | no MR -> candidate analysis |
| CST5 protein levels | 2e-251 | rs150230325 | 23 | GCST90468895 | no MR -> candidate analysis |
| Blood protein levels | 7e-186 | rs2071444 | 1 | GCST006585 | no MR -> candidate analysis |
| Cystatin C levels | 4e-115 | rs8184710 | 3 | GCST90019504 | no MR -> candidate analysis |
| CST1 protein levels | 6e-68 | rs73093347 | 4 | GCST90468893 | no MR -> candidate analysis |
| Protein quantitative trait loci | 3e-19 | rs4387871 | 1 | GCST010900 | no MR -> candidate analysis |
| Serum levels of protein CST5 | 8e-14 | rs4815243 | 1 | GCST90088518 | no MR -> candidate analysis |
| Cystatin-SN levels | 2e-13 | rs6036565 | 1 | GCST90162410 | no MR -> candidate analysis |
| Cystatin-SA levels | 9e-13 | rs4813509 | 1 | GCST90162049 | no MR -> candidate analysis |
| Carbonic anhydrase 12 protein levels (SomaScan ID:3803-10) | 9e-10 | rs6049191 | 1 | GCST90442950 | no MR -> candidate analysis |
| _...and 7 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 585 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| alcohol drinking | 0.576 | — | common-variant locus | no MR -> candidate analysis |
| urolithiasis | 0.429 | — | common-variant locus | no MR -> candidate analysis |
| response to antihypertensive drug | 0.429 | — | common-variant locus | no MR -> candidate analysis |
| stroke disorder | 0.355 | — | common-variant locus | no MR -> candidate analysis |
| arthropathy | 0.285 | — | common-variant locus | no MR -> candidate analysis |
| movement disorder | 0.244 | — | common-variant locus | no MR -> candidate analysis |

> Of the 6 rows above, **6 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1.1e-05, LOEUF=1.79 — LoF-tolerant |
| GWAS Catalog | 88 unique SNPs / 175 rows |
| ClinVar | 54 records; 3 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 1 clinical annotations across 1 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 585 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'CST5'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 54 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 19 of 19 traits by best p-value, aggregated from 57 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P28325 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000170367/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CST5 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CST5 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CST5%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=CST5 — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CST5 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:07:53  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
