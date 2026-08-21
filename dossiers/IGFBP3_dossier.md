# Protein Dossier — IGFBP3 (Insulin-like growth factor-binding protein 3)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diastolic blood pressure  automated reading | 0.0366 | 0.00636 | 8.67e-09 | Wald ratio | 1 | cis | NA |
| Systolic blood pressure  automated reading | -0.0316 | 0.00636 | 6.69e-07 | Wald ratio | 1 | cis | NA |
| Height | -0.028 | 0.00794 | 4.16e-04 | Wald ratio | 1 | cis | NA |
| Squamous cell lung cancer | -0.198 | 0.0663 | 0.00285 | Wald ratio | 1 | cis | NA |
| Potassium in urine | -0.0172 | 0.00631 | 0.00638 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: asthma | 0.0431 | 0.0167 | 0.00979 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | -0.0131 | 0.0051 | 0.00994 | Wald ratio | 1 | cis | NA |
| Creatinine (enzymatic) in urine | -0.015 | 0.00595 | 0.0118 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | -0.0134 | 0.00538 | 0.0128 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: small intestine or small bowel cancer | 0.472 | 0.191 | 0.0136 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: chronic obstructive airways disease or copd | -0.395 | 0.163 | 0.0156 | Wald ratio | 1 | cis | NA |
| Ischemic stroke | -0.101 | 0.0435 | 0.0202 | Wald ratio | 1 | cis | NA |
| _...and 108 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2571_12_3` | IGFBP-3 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_169 association rows across 71 traits (155 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating IGFBP3 levels | 3e-1029 | rs2854744 | 2 | GCST90860453 | no MR -> candidate analysis |
| IGF-1 and IGFBP-3 levels (bivariate analysis) | 3e-195 | rs11977526 | 1 | GCST90102625 | no MR -> candidate analysis |
| Serum levels of protein IGFALS | 2e-189 | rs2854746 | 1 | GCST90089525 | no MR -> candidate analysis |
| Nutritionally-regulated adipose and cardiac enriched protein | 1e-182 | rs2854746 | 1 | GCST90248727 | no MR -> candidate analysis |
| Serum levels of protein IGFBP3 | 4e-161 | rs11977526 | 4 | GCST90102624 | no MR -> candidate analysis |
| Pulse pressure | 5e-139 | rs11977526 | 27 | GCST90310296 | no MR -> candidate analysis |
| Insulin-like growth factor-binding protein 3 levels | 1e-116 | rs145188037 | 6 | GCST90248011 | no MR -> candidate analysis |
| IGF 1 (UKB data field 30770) | 1e-104 | rs2854746 | 3 | GCST90468078 | no MR -> candidate analysis |
| Insulin-like growth factors | 3e-101 | rs11977526 | 1 | GCST000937 | no MR -> candidate analysis |
| IGFBP3 protein levels | 7e-59 | rs1722116 | 8 | GCST90469529 | no MR -> candidate analysis |
| Height | 1e-49 | rs6953668 | 11 | GCST90245848 | MR: beta=-0.028, p=4.16e-04 (cis) |
| IGF2 protein levels | 2e-49 | rs2854746 | 3 | GCST90453055 | no MR -> candidate analysis |
| _...and 59 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1530 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Abnormality of the skeletal system | 0.786 | — | common-variant locus | no MR -> candidate analysis |
| lymphatic system disorder | 0.594 | — | common-variant locus | no MR -> candidate analysis |
| cataract | 0.575 | — | common-variant locus | MR: beta=-0.168, p=0.047 (cis) |
| open-angle glaucoma | 0.563 | — | common-variant locus | no MR -> candidate analysis |
| Alzheimer disease | 0.52 | — | common-variant locus | no MR -> candidate analysis |
| prostate cancer | 0.526 | — | common-variant locus | no MR -> candidate analysis |
| colorectal cancer | 0.526 | — | common-variant locus | no MR -> candidate analysis |
| cancer | 0.512 | — | common-variant locus | MR: beta=-0.198, p=0.00285 (cis) |
| hypertensive disorder | 0.506 | — | common-variant locus | no MR -> candidate analysis |
| heart disorder | 0.522 | — | common-variant locus | no MR -> candidate analysis |
| tenosynovitis | 0.486 | — | common-variant locus | no MR -> candidate analysis |
| hypospadias | 0.468 | — | common-variant locus | no MR -> candidate analysis |
| senile cataract | 0.46 | — | common-variant locus | MR: beta=-0.168, p=0.047 (cis) |
| Age-related cataract | 0.453 | — | common-variant locus | no MR -> candidate analysis |
| Back pain | 0.448 | — | common-variant locus | no MR -> candidate analysis |

> Of the 15 rows above, **12 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Insulin-like growth factor-binding protein 3) |
| gnomAD constraint | pLI=0.93, LOEUF=0.549 — LoF-INTOLERANT |
| GWAS Catalog | 94 unique SNPs / 187 rows |
| ClinVar | 68 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 1 clinical annotations across 1 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1530 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'IGFBP3' and resolved to 'Insulin-like growth factor-binding protein 3' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 68 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 20 of 71 traits by best p-value, aggregated from 169 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P17936 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000146674/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3997/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/IGFBP3 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/IGFBP3 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=IGFBP3%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=IGFBP3 — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/IGFBP3 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:08:38  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
