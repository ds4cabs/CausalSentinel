# Protein Dossier — SELL (L-selectin)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Autism | 0.207 | 0.0625 | 9.33e-04 | Wald ratio | 1 | cis | NA |
| Lung adenocarcinoma | 0.135 | 0.0561 | 0.0161 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K43 Ventral hernia | -0.236 | 0.101 | 0.0192 | Wald ratio | 1 | cis | NA |
| Femoral neck bone mineral density | -0.0377 | 0.0164 | 0.0212 | Wald ratio | 1 | cis | NA |
| Lung cancer | 0.0866 | 0.0379 | 0.0223 | Wald ratio | 1 | cis | NA |
| Squamous cell lung cancer | 0.129 | 0.0568 | 0.0227 | Wald ratio | 1 | cis | NA |
| Childhood intelligence | -0.0639 | 0.0283 | 0.0238 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: D12 Benign neoplasm of colon  rectum  anus and anal canal | 0.0906 | 0.0404 | 0.025 | Wald ratio | 1 | cis | NA |
| Anorexia nervosa | -0.147 | 0.069 | 0.0329 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: Z09 Follow-up examination after treatment for conditions other than malignant neoplasms | 0.08 | 0.0394 | 0.0421 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I83 Varicose veins of lower extremities | -0.0803 | 0.0397 | 0.0428 | Wald ratio | 1 | cis | NA |
| Neo-neuroticism | -0.408 | 0.208 | 0.05 | Wald ratio | 1 | cis | NA |
| _...and 87 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-4831_4_2` | sL-Selectin | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_45 association rows across 32 traits (39 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| L-selectin levels | 2e-363 | rs4140655 | 10 | GCST90248341 | no MR -> candidate analysis |
| Cerebrospinal fluid protein SELL levels | 6e-134 | rs4987369 | 1 | GCST90944888 | no MR -> candidate analysis |
| L-Selectin levels (SELL.4831.4.2) | 7e-87 | rs4987358 | 1 | GCST90241725 | no MR -> candidate analysis |
| Serum levels of protein SELL | 2e-82 | rs4987358 | 1 | GCST90088779 | no MR -> candidate analysis |
| SELL protein levels | 8e-56 | rs2223286 | 2 | GCST90453181 | no MR -> candidate analysis |
| ICAM2/SELE protein level ratio | 3e-53 | rs2298900 | 1 | GCST90315120 | no MR -> candidate analysis |
| PTPRM/SELE protein level ratio | 2e-52 | rs2298900 | 1 | GCST90315753 | no MR -> candidate analysis |
| ICAM1/SELE protein level ratio | 5e-52 | rs2298900 | 1 | GCST90315116 | no MR -> candidate analysis |
| CD62L on monocyte | 4e-50 | rs4987369 | 1 | GCST90001834 | no MR -> candidate analysis |
| Blood protein levels | 6e-48 | rs4987358 | 1 | GCST006585 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 2e-31 | rs4987353 | 1 | GCST90838671 | no MR -> candidate analysis |
| ITGA5/SELE protein level ratio | 3e-30 | rs4987318 | 1 | GCST90315205 | no MR -> candidate analysis |
| _...and 20 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 900 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| type 2 diabetes mellitus | 0.565 | — | common-variant locus | no MR -> candidate analysis |
| lymphatic system disorder | 0.512 | — | common-variant locus | no MR -> candidate analysis |
| ankylosing spondylitis | 0.394 | — | common-variant locus | MR: beta=0.133, p=0.13 (cis) |
| phlebitis | 0.369 | — | common-variant locus | no MR -> candidate analysis |
| Thrombophlebitis | 0.369 | — | common-variant locus | no MR -> candidate analysis |
| atrial fibrillation | 0.275 | — | common-variant locus | MR: beta=0.0391, p=0.413 (cis) |
| aging | 0.174 | — | common-variant locus | no MR -> candidate analysis |
| Sepsis | 0.035 | — | common-variant locus | no MR -> candidate analysis |
| deep vein thrombosis | 0.141 | — | common-variant locus | no MR -> candidate analysis |
| thrombophilia | 0.139 | — | common-variant locus | no MR -> candidate analysis |
| venous thromboembolism | 0.133 | — | common-variant locus | no MR -> candidate analysis |

> Of the 11 rows above, **9 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 2 known modulators (L-selectin) |
| gnomAD constraint | pLI=1e-12, LOEUF=1.07 — LoF-tolerant |
| GWAS Catalog | 101 unique SNPs / 208 rows |
| ClinVar | 85 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 900 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'SELL' and resolved to 'L-selectin' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 85 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 32 traits by best p-value, aggregated from 45 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P14151 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000188404/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3161/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/SELL — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/SELL — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=SELL%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/SELL — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:57:28  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
