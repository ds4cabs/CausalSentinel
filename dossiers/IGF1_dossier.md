# Protein Dossier — IGF1 (Insulin-like growth factor 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diastolic blood pressure  automated reading | 0.0489 | 0.0085 | 8.67e-09 | Wald ratio | 1 | trans | NA |
| Systolic blood pressure  automated reading | -0.0422 | 0.00849 | 6.69e-07 | Wald ratio | 1 | trans | NA |
| Height | -0.0375 | 0.0106 | 4.16e-04 | Wald ratio | 1 | trans | NA |
| Squamous cell lung cancer | -0.264 | 0.0886 | 0.00285 | Wald ratio | 1 | trans | NA |
| Potassium in urine | -0.023 | 0.00843 | 0.00638 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: asthma | 0.0572 | 0.022 | 0.00931 | Wald ratio | 1 | trans | NA |
| Forced vital capacity (FVC) | -0.0176 | 0.00681 | 0.00994 | Wald ratio | 1 | trans | NA |
| Cancer code  self-reported: small intestine or small bowel cancer | 0.591 | 0.231 | 0.0107 | Wald ratio | 1 | trans | NA |
| Creatinine (enzymatic) in urine | -0.02 | 0.00795 | 0.0118 | Wald ratio | 1 | trans | NA |
| Forced expiratory volume in 1-second (FEV1) | -0.0179 | 0.00718 | 0.0128 | Wald ratio | 1 | trans | NA |
| Ischemic stroke | -0.135 | 0.0581 | 0.0202 | Wald ratio | 1 | trans | NA |
| Triglycerides | -0.0393 | 0.0172 | 0.022 | Wald ratio | 1 | trans | NA |
| _...and 108 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2952_75_2` | IGF-I | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_311 association rows across 130 traits (268 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Height | 1e-300 | rs5742692 | 55 | GCST90245848 | MR: beta=-0.0375, p=4.16e-04 (trans) |
| Bone mineral density mean | 1e-300 | rs151181954 | 2 | GCST90321120 | no MR -> candidate analysis |
| IGF 1 (UKB data field 30770) | 5e-239 | rs11111274 | 5 | GCST90468078 | no MR -> candidate analysis |
| Standing height (UKB data field 50) | 2e-43 | rs142187070 | 4 | GCST90468178 | no MR -> candidate analysis |
| Height (baseline) | 2e-38 | rs703593 | 18 | GCST90565843 | no MR -> candidate analysis |
| Insulin-like growth factor 1 levels | 6e-35 | rs1457596 | 6 | GCST90019511 | no MR -> candidate analysis |
| Appendicular lean mass | 3e-31 | rs142187070 | 4 | GCST90000025 | no MR -> candidate analysis |
| Body shape phenotype PC2 | 7e-28 | rs703593 | 2 | GCST90832990 | no MR -> candidate analysis |
| Unsupervised deep imaging phenotypes (UDIP-FA) | 1e-25 | rs11111278 | 1 | GCST90860937 | no MR -> candidate analysis |
| Sex hormone-binding globulin levels adjusted for BMI | 3e-25 | rs11111274 | 2 | GCST90012110 | no MR -> candidate analysis |
| Peak expiratory flow | 5e-25 | rs10860865 | 3 | GCST90244095 | no MR -> candidate analysis |
| Total cerebellar volume | 2e-24 | rs11111278 | 2 | GCST90105075 | no MR -> candidate analysis |
| _...and 118 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 3944 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| growth delay due to insulin-like growth factor type 1 deficiency | 0.761 | — | established (curated) | no MR -> candidate analysis |
| Abnormality of the skeletal system | 0.717 | — | common-variant locus | no MR -> candidate analysis |
| COVID-19 | 0.555 | — | common-variant locus | no MR -> candidate analysis |
| preeclampsia | 0.509 | — | common-variant locus | no MR -> candidate analysis |
| Uterine leiomyoma | 0.472 | — | common-variant locus | no MR -> candidate analysis |
| Tietze syndrome | 0.484 | — | common-variant locus | no MR -> candidate analysis |
| nodular goiter | 0.484 | — | common-variant locus | no MR -> candidate analysis |
| upper respiratory tract disorder | 0.484 | — | common-variant locus | no MR -> candidate analysis |
| breast cancer | 0.41 | — | common-variant locus | MR: beta=-0.0815, p=0.0368 (trans) |
| Abnormality of refraction | 0.455 | — | common-variant locus | no MR -> candidate analysis |
| breast neoplasm | 0.41 | — | common-variant locus | MR: beta=0.0805, p=0.181 (trans) |
| estrogen-receptor positive breast cancer | 0.41 | — | common-variant locus | no MR -> candidate analysis |
| acquired thrombocytopenia | 0.396 | — | common-variant locus | no MR -> candidate analysis |
| obstructive sleep apnea syndrome | 0.347 | — | common-variant locus | no MR -> candidate analysis |
| breast disorder | 0.386 | — | common-variant locus | no MR -> candidate analysis |

> Of the 15 rows above, **13 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 2 known modulators (Insulin-like growth factor 1) |
| gnomAD constraint | pLI=0.78, LOEUF=0.664 — LoF-tolerant |
| GWAS Catalog | 167 unique SNPs / 402 rows |
| ClinVar | 213 records; 8 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 3944 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'IGF1' and resolved to 'Insulin-like growth factor 1' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 213 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 130 traits by best p-value, aggregated from 311 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P05019 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000017427/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3217394/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/IGF1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/IGF1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=IGF1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/IGF1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:07:32  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
