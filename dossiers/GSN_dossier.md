# Protein Dossier — GSN (Gelsolin)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: gastro-oesophageal reflux (gord)  or  gastric reflux | 0.154 | 0.0548 | 0.00483 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: ankylosing spondylitis | 0.431 | 0.168 | 0.0104 | Wald ratio | 1 | cis | NA |
| Lung adenocarcinoma | 0.365 | 0.143 | 0.0108 | Wald ratio | 1 | cis | NA |
| Schizophrenia | -0.157 | 0.0681 | 0.0215 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | -0.0381 | 0.0171 | 0.0264 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K80 Cholelithiasis | 0.164 | 0.0787 | 0.0372 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: enlarged prostate | 0.193 | 0.0943 | 0.041 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: deep venous thrombosis (dvt) | 0.163 | 0.0803 | 0.043 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | -0.0259 | 0.0132 | 0.0497 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: bone disorder | 0.378 | 0.203 | 0.0631 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: small intestine or small bowel cancer | 0.675 | 0.371 | 0.0689 | Wald ratio | 1 | cis | NA |
| Weight | -0.021 | 0.0117 | 0.0722 | Wald ratio | 1 | cis | NA |
| _...and 60 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-4775_34_3` | Gelsolin | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_34 association rows across 26 traits (29 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Bone mineral density mean | 1e-300 | rs117584126 | 1 | GCST90321120 | no MR -> candidate analysis |
| GSN protein levels | 2e-147 | rs116185403 | 3 | GCST90469409 | no MR -> candidate analysis |
| Gelsolin (analyte X4775.34) levels | 1e-45 | rs76098787 | 1 | GCST90426105 | no MR -> candidate analysis |
| Cerebrospinal fluid protein GSN levels | 1e-44 | rs41273422 | 1 | GCST90945002 | no MR -> candidate analysis |
| DNA repair protein RAD51 homolog 3 levels | 2e-37 | rs41273422 | 1 | GCST90424458 | no MR -> candidate analysis |
| Gelsolin levels | 3e-32 | rs10985196 | 3 | GCST90247716 | no MR -> candidate analysis |
| RNF41/WWP2 protein level ratio | 1e-28 | rs55932622 | 1 | GCST90315782 | no MR -> candidate analysis |
| Kinetochore protein NDC80 homolog levels | 4e-26 | rs41273422 | 1 | GCST90421913 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 5e-18 | rs9792437 | 2 | GCST90838669 | no MR -> candidate analysis |
| Hemoglobin A1c levels | 5e-16 | rs1560980 | 1 | GCST90018958 | no MR -> candidate analysis |
| Uncharacterized protein C10orf35 levels | 4e-13 | rs76098787 | 1 | GCST90427273 | no MR -> candidate analysis |
| Circulating HMOX1 levels (id: OID00432_OID20217) | 4e-12 | rs3747850 | 1 | GCST90859792 | no MR -> candidate analysis |
| _...and 14 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 742 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Finnish type amyloidosis | 0.838 | — | established (curated) | no MR -> candidate analysis |
| Familial amyloidosis, Finnish type | 0.73 | — | established (curated) | no MR -> candidate analysis |
| hereditary disease | 0.683 | — | established (curated) | no MR -> candidate analysis |
| cervical carcinoma | 0.421 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.368 | — | common-variant locus | no MR -> candidate analysis |

> Of the 5 rows above, **5 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Gelsolin) |
| gnomAD constraint | pLI=2.8e-12, LOEUF=0.816 — LoF-tolerant |
| GWAS Catalog | 49 unique SNPs / 98 rows |
| ClinVar | 1022 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 742 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'GSN' and resolved to 'Gelsolin' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 1022 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 26 traits by best p-value, aggregated from 34 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P06396 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000148180/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4295700/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/GSN — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/GSN — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=GSN%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/GSN — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:55:05  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
