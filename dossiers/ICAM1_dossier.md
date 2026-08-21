# Protein Dossier — ICAM1 (Intercellular adhesion molecule 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diastolic blood pressure  automated reading | 0.00759 | 0.00204 | 2.02e-04 | Inverse variance weighted | 3 | cis | NA |
| Diastolic blood pressure  automated reading | 0.00759 | 0.00204 | 2.02e-04 | Inverse variance weighted | 3 | trans | NA |
| Diastolic blood pressure  automated reading | 0.00759 | 0.00204 | 2.02e-04 | Inverse variance weighted | 3 | trans | NA |
| Non-cancer illness code  self-reported: hypertension | 0.00324 | 0.000884 | 2.49e-04 | Inverse variance weighted | 3 | cis | NA |
| Non-cancer illness code  self-reported: hypertension | 0.00324 | 0.000884 | 2.49e-04 | Inverse variance weighted | 3 | trans | NA |
| Non-cancer illness code  self-reported: hypertension | 0.00324 | 0.000884 | 2.49e-04 | Inverse variance weighted | 3 | trans | NA |
| Neo-extraversion | 0.219 | 0.0683 | 0.00134 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hayfever or allergic rhinitis | -0.0015 | 0.00047 | 0.0014 | Inverse variance weighted | 3 | cis | NA |
| Non-cancer illness code  self-reported: hayfever or allergic rhinitis | -0.0015 | 0.00047 | 0.0014 | Inverse variance weighted | 3 | trans | NA |
| Non-cancer illness code  self-reported: hayfever or allergic rhinitis | -0.0015 | 0.00047 | 0.0014 | Inverse variance weighted | 3 | trans | NA |
| Body mass index (BMI) | 0.00561 | 0.00199 | 0.0049 | Inverse variance weighted | 3 | cis | NA |
| Body mass index (BMI) | 0.00561 | 0.00199 | 0.0049 | Inverse variance weighted | 3 | trans | NA |
| _...and 279 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-4342_10_3` | sICAM-1 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_88 association rows across 34 traits (84 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Intercellular adhesion molecule 1 levels | 2e-5507 | rs5498 | 15 | GCST90248103 | no MR -> candidate analysis |
| Intercellular adhesion molecule 1 levels (ICAM1.4342.10.3) | 8e-1683 | rs5498 | 1 | GCST90241537 | no MR -> candidate analysis |
| Circulating ICAM1 levels | 3e-919 | rs12462944 | 4 | GCST90860432 | no MR -> candidate analysis |
| ICAM1 protein levels | 2e-184 | rs139053442 | 10 | GCST90469498 | no MR -> candidate analysis |
| Soluble ICAM-1 | 1e-120 | rs1799969 | 6 | GCST001047 | no MR -> candidate analysis |
| Lymphocyte count | 6e-107 | rs5498 | 5 | GCST90002316 | no MR -> candidate analysis |
| ICAM4 protein levels | 2e-96 | rs5030377 | 1 | GCST90469501 | no MR -> candidate analysis |
| Intercellular adhesion molecule 5 levels (ICAM5.8245.27.3) | 8e-86 | rs75407602 | 1 | GCST90241541 | no MR -> candidate analysis |
| Lymphocyte count (UKB data field 30120) | 1e-77 | rs5498 | 1 | GCST90468082 | no MR -> candidate analysis |
| ICAM5 protein levels | 3e-76 | rs76923681 | 3 | GCST90469502 | no MR -> candidate analysis |
| Intercellular adhesion molecule 1 level in Chronic kidney di | 5e-64 | rs5498 | 1 | GCST90237630 | no MR -> candidate analysis |
| Intercellular adhesion molecule 5 levels | 3e-53 | rs923366 | 4 | GCST90137725 | no MR -> candidate analysis |
| _...and 22 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1944 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| atrial fibrillation | 0.641 | — | common-variant locus | MR: beta=0.000365, p=0.088 (cis) |
| vascular disorder | 0.556 | — | common-variant locus | no MR -> candidate analysis |
| chronic obstructive pulmonary disease | 0.494 | — | common-variant locus | no MR -> candidate analysis |
| cardiac arrhythmia | 0.494 | — | common-variant locus | no MR -> candidate analysis |
| atrial flutter | 0.491 | — | common-variant locus | MR: beta=0.000365, p=0.088 (cis) |
| lymphatic system disorder | 0.347 | 0.337 | multi-layer: burden+GWAS (allelic-series candidate) | no MR -> candidate analysis |
| Abnormality of the lymphatic system | 0.337 | 0.337 | exploratory rare-variant signal | no MR -> candidate analysis |
| inflammatory bowel disease | 0.141 | — | common-variant locus | MR: beta=-0.0142, p=0.108 (cis) |

> Of the 8 rows above, **5 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 1 exploratory rare-variant signal(s), 1 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 3 known modulators (Intercellular adhesion molecule 1) |
| gnomAD constraint | pLI=9.2e-07, LOEUF=0.907 — LoF-tolerant |
| GWAS Catalog | 163 unique SNPs / 406 rows |
| ClinVar | 118 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1944 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'ICAM1' and resolved to 'Intercellular adhesion molecule 1' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 118 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 34 traits by best p-value, aggregated from 88 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P05362 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000090339/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3070/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/ICAM1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/ICAM1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=ICAM1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/ICAM1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:04:13  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
