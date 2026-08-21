# Protein Dossier — PDE5A (cGMP-specific 3',5'-cyclic phosphodiesterase)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: uterine fibroids | 0.181 | 0.0523 | 5.29e-04 | Wald ratio | 1 | cis | NA |
| Height | -0.0312 | 0.00924 | 7.27e-04 | Wald ratio | 1 | cis | NA |
| Vascular or heart problems diagnosed by doctor: Angina | -0.126 | 0.0493 | 0.0108 | Wald ratio | 1 | cis | NA |
| Lumbar spine bone mineral density | 0.0718 | 0.0282 | 0.0108 | Wald ratio | 1 | cis | NA |
| Alcohol intake frequency | 0.0282 | 0.0114 | 0.0136 | Wald ratio | 1 | cis | NA |
| Coronary heart disease | -0.0709 | 0.0293 | 0.0156 | Wald ratio | 1 | cis | NA |
| Chronic kidney disease | 0.115 | 0.0478 | 0.0164 | Wald ratio | 1 | cis | NA |
| Myocardial infarction | -0.0699 | 0.0324 | 0.0313 | Wald ratio | 1 | cis | NA |
| Body fat | -0.0369 | 0.0172 | 0.0317 | Wald ratio | 1 | cis | NA |
| Birth weight | 0.0245 | 0.0115 | 0.0324 | Wald ratio | 1 | cis | NA |
| High grade serous ovarian cancer | 0.109 | 0.0512 | 0.0341 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N81 Female genital prolapse | -0.16 | 0.0764 | 0.0364 | Wald ratio | 1 | cis | NA |
| _...and 101 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-5256_86_3` | PDE5A | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_102 association rows across 55 traits (92 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| cGMP-specific 3,5-cyclic phosphodiesterase levels | 1e-162 | rs59867181 | 4 | GCST90248907 | no MR -> candidate analysis |
| PDE5A protein levels | 2e-108 | rs58583086 | 3 | GCST90470187 | no MR -> candidate analysis |
| Height | 7e-90 | rs17051339 | 16 | GCST90245848 | MR: beta=-0.0312, p=7.27e-04 (cis) |
| FABP2 protein levels | 6e-37 | rs4452411 | 1 | GCST90469174 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 2e-31 | rs13122709 | 2 | GCST90838669 | no MR -> candidate analysis |
| Platelet count | 1e-28 | rs7672519 | 4 | GCST90662907 | MR: beta=-2.11, p=0.0953 (cis) |
| Diastolic blood pressure | 3e-21 | rs66887589 | 7 | GCST90310295 | MR: beta=-0.01, p=0.205 (cis) |
| Refractive error | 1e-19 | rs7666824 | 2 | GCST90841193 | no MR -> candidate analysis |
| Diastolic blood pressure (MTAG) | 9e-19 | rs66887589 | 1 | GCST90449057 | no MR -> candidate analysis |
| Impedance of arm left (UKB data field 23110) | 1e-16 | rs749526 | 1 | GCST90468171 | no MR -> candidate analysis |
| cGMP-specific 3',5'-cyclic phosphodiesterase levels | 3e-15 | rs151102303 | 1 | GCST90162352 | no MR -> candidate analysis |
| Waist circumference adjusted for body mass index | 2e-14 | rs62321172 | 4 | GCST90020029 | no MR -> candidate analysis |
| _...and 43 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 723 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| coronary artery disorder | 0.715 | — | common-variant locus | no MR -> candidate analysis |
| cardiovascular disorder | 0.389 | — | common-variant locus | no MR -> candidate analysis |
| obesity disorder | 0.498 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (PDE5A/PDE6C) |
| gnomAD constraint | pLI=7.9e-13, LOEUF=0.745 — LoF-tolerant |
| GWAS Catalog | 94 unique SNPs / 170 rows |
| ClinVar | 167 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 723 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'PDE5A' and resolved to 'PDE5A/PDE6C' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 167 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 55 traits by best p-value, aggregated from 102 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O76074 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000138735/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4523626/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PDE5A — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PDE5A — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PDE5A%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/PDE5A — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:14:48  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
