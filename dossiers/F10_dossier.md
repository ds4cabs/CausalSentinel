# Protein Dossier — F10 (Coagulation factor X)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: K35 Acute appendicitis | 0.38 | 0.0967 | 8.35e-05 | Wald ratio | 1 | cis | NA |
| Potassium in urine | -0.0294 | 0.00988 | 0.00291 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | -0.0276 | 0.00973 | 0.00454 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: joint disorder | 0.276 | 0.109 | 0.0116 | Wald ratio | 1 | cis | NA |
| Neuroticism | 0.0219 | 0.00947 | 0.0207 | Inverse variance weighted | 2 | trans | NA |
| Neuroticism | 0.0219 | 0.00947 | 0.0207 | Inverse variance weighted | 2 | cis | NA |
| Diagnoses - main ICD10: N81 Female genital prolapse | -0.211 | 0.102 | 0.0381 | Wald ratio | 1 | cis | NA |
| Weight | -0.0178 | 0.0086 | 0.0382 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: retinal detachment | 0.272 | 0.132 | 0.0392 | Wald ratio | 1 | cis | NA |
| Triglycerides | -0.0302 | 0.0159 | 0.0571 | Wald ratio | 1 | cis | NA |
| Amygdala volume | -17.1 | 9.33 | 0.0664 | Wald ratio | 1 | trans | NA |
| HOMA-B | -0.0325 | 0.0186 | 0.0801 | Wald ratio | 1 | cis | NA |
| _...and 98 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3077_66_2` | Coagulation Factor Xa | Suhre K | 2019 |
| `prot-c-4878_3_1` | Coagulation Factor X | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_59 association rows across 28 traits (52 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Protein Z-dependent protease inhibitor levels | 4e-370 | rs559054 | 2 | GCST90249198 | no MR -> candidate analysis |
| Dual specificity mitogen-activated protein kinase kinase 2 l | 6e-259 | rs559054 | 2 | GCST90247301 | no MR -> candidate analysis |
| F7 protein levels | 7e-177 | rs9549675 | 5 | GCST90469171 | no MR -> candidate analysis |
| F10 protein levels | 2e-146 | rs547138 | 5 | GCST90469163 | no MR -> candidate analysis |
| PROZ protein levels | 1e-110 | rs559054 | 3 | GCST90453206 | no MR -> candidate analysis |
| Protein Z-dependent protease inhibitor levels (SERPINA10.131 | 6e-100 | rs559054 | 2 | GCST90242530 | no MR -> candidate analysis |
| Coagulation Factor VII levels | 6e-65 | rs474671 | 4 | GCST90100839 | no MR -> candidate analysis |
| Circulating F7 levels | 2e-63 | rs3212991 | 1 | GCST90860440 | no MR -> candidate analysis |
| Coagulation Factor X levels | 2e-51 | rs547138 | 2 | GCST90247101 | no MR -> candidate analysis |
| Coagulation factor Xa levels | 8e-50 | rs547138 | 5 | GCST90247102 | no MR -> candidate analysis |
| SERPINA10 protein levels | 1e-38 | rs559054 | 2 | GCST90453399 | no MR -> candidate analysis |
| Prothrombin time | 7e-30 | rs563964 | 4 | GCST90104196 | no MR -> candidate analysis |
| _...and 16 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 628 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| factor X deficiency | 0.96 | — | established (curated) | no MR -> candidate analysis |
| congenital factor X deficiency | 0.819 | — | established (curated) | no MR -> candidate analysis |
| venous thromboembolism | 0.832 | — | common-variant locus | no MR -> candidate analysis |
| pulmonary embolism | 0.566 | — | common-variant locus | MR: beta=0.136, p=0.154 (cis) |
| atrial fibrillation | 0.053 | — | common-variant locus | no MR -> candidate analysis |
| Thrombocytopenia | 0.491 | — | established (curated) | no MR -> candidate analysis |
| Thromboembolism | 0.317 | — | common-variant locus | no MR -> candidate analysis |
| blood coagulation disease | 0.055 | — | common-variant locus | no MR -> candidate analysis |
| Abnormal bleeding | 0.584 | — | established (curated) | no MR -> candidate analysis |

> Of the 9 rows above, **8 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 13 known modulators (Coagulation factor X) |
| gnomAD constraint | pLI=1.8e-08, LOEUF=1.07 — LoF-tolerant |
| GWAS Catalog | 111 unique SNPs / 260 rows |
| ClinVar | 303 records; 8 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 628 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'F10' and resolved to 'Coagulation factor X' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 303 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 28 traits by best p-value, aggregated from 59 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P00742 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000126218/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL244/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/F10 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/F10 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=F10%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/F10 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:30:32  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
