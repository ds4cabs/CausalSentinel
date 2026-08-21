# Protein Dossier — DYNLL2 (Dynein light chain 2, cytoplasmic)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Body mass index (BMI) | -0.0805 | 0.0162 | 6.84e-07 | Wald ratio | 1 | cis | NA |
| Weight | -0.0468 | 0.0143 | 0.00109 | Wald ratio | 1 | cis | NA |
| Intracranial volume | 4.34e+04 | 1.33e+04 | 0.00111 | Wald ratio | 1 | cis | NA |
| Diastolic blood pressure  automated reading | -0.0516 | 0.0166 | 0.00191 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K80 Cholelithiasis | 0.265 | 0.0875 | 0.00247 | Wald ratio | 1 | cis | NA |
| Amyotrophic lateral sclerosis | -0.347 | 0.122 | 0.00441 | Wald ratio | 1 | cis | NA |
| Coronary heart disease | -0.185 | 0.0701 | 0.00833 | Wald ratio | 1 | cis | NA |
| Systolic blood pressure  automated reading | -0.0418 | 0.0166 | 0.0118 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M72 Fibroblastic disorders | 0.357 | 0.159 | 0.0248 | Wald ratio | 1 | cis | NA |
| Myocardial infarction | -0.161 | 0.0774 | 0.0374 | Wald ratio | 1 | cis | NA |
| Endometrioid ovarian cancer | -0.407 | 0.201 | 0.0426 | Wald ratio | 1 | cis | NA |
| Sleep duration | 0.0256 | 0.0127 | 0.0429 | Wald ratio | 1 | cis | NA |
| _...and 55 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_23 association rows across 12 traits (22 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Height | 1e-32 | rs181222 | 3 | GCST90245848 | no MR -> candidate analysis |
| Serum levels of protein RAB26 | 8e-30 | rs35552706 | 1 | GCST90089610 | no MR -> candidate analysis |
| Serum levels of protein DYNLL2 | 1e-13 | rs9896162 | 1 | GCST90086769 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 3e-12 | rs12951118 | 1 | GCST90838669 | no MR -> candidate analysis |
| Educational attainment | 4e-12 | rs12602072 | 1 | GCST90105038 | no MR -> candidate analysis |
| Educational attainment (MTAG) | 1e-10 | rs8071798 | 1 | GCST006571 | no MR -> candidate analysis |
| Blood protein levels | 3e-10 | rs35729384 | 1 | GCST006585 | no MR -> candidate analysis |
| Body mass index | 3e-10 | rs11649864 | 9 | GCST009003 | MR: beta=-0.0805, p=6.84e-07 (cis) |
| Body mass index (MTAG) | 4e-10 | rs11649864 | 1 | GCST90179150 | no MR -> candidate analysis |
| Educational attainment (years of education) | 8e-10 | rs181214 | 2 | GCST006442 | no MR -> candidate analysis |
| Body shape phenotype PC4 | 2e-8 | rs35552706 | 1 | GCST90832992 | no MR -> candidate analysis |
| S-warfarin levels | 6e-6 | rs150622867 | 1 | GCST90129562 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 48 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| prostate carcinoma | 0.441 | — | common-variant locus | no MR -> candidate analysis |
| paroxysmal tachycardia | 0.216 | — | common-variant locus | no MR -> candidate analysis |
| frozen shoulder | 0.072 | — | common-variant locus | no MR -> candidate analysis |
| cervical carcinoma | 0.065 | — | common-variant locus | no MR -> candidate analysis |
| hypertensive disorder | 0.047 | — | common-variant locus | no MR -> candidate analysis |

> Of the 5 rows above, **5 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Dynein light chain 2, cytoplasmic) |
| gnomAD constraint | pLI=0.95, LOEUF=0.488 — LoF-INTOLERANT |
| GWAS Catalog | 30 unique SNPs / 60 rows |
| ClinVar | 24 records; 16 pathogenic in sample of 24 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 48 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'DYNLL2' and resolved to 'Dynein light chain 2, cytoplasmic' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 24 record(s) retrieved, NOT over all 24 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 12 of 12 traits by best p-value, aggregated from 23 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q96FJ2 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000264364/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL6067226/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/DYNLL2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/DYNLL2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=DYNLL2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/DYNLL2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:21:52  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
