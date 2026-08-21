# Protein Dossier — LY9 (T-lymphocyte surface antigen Ly-9)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Inflammatory bowel disease | 0.105 | 0.0256 | 4.04e-05 | Wald ratio | 1 | cis | NA |
| Ulcerative colitis | 0.125 | 0.0321 | 9.83e-05 | Wald ratio | 1 | cis | NA |
| Clear cell ovarian cancer | -0.392 | 0.107 | 2.57e-04 | Wald ratio | 1 | cis | NA |
| Multiple sclerosis | 0.128 | 0.0411 | 0.00182 | Wald ratio | 1 | cis | NA |
| Crohn's disease | 0.0906 | 0.031 | 0.00343 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: psoriasis | 0.137 | 0.0501 | 0.00615 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: high cholesterol | 0.0358 | 0.0159 | 0.0244 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: Z09 Follow-up examination after treatment for conditions other than malignant neoplasms | 0.0993 | 0.045 | 0.0273 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Other bones | -0.0559 | 0.0281 | 0.0465 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hayfever or allergic rhinitis | -0.0513 | 0.0264 | 0.0519 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: depression | 0.0464 | 0.024 | 0.0532 | Wald ratio | 1 | cis | NA |
| Putamen volume | 27.4 | 15 | 0.0688 | Wald ratio | 1 | cis | NA |
| _...and 64 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3324_51_1` | LY9 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_70 association rows across 27 traits (68 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating LY9 levels | 2e-1425 | rs12405457 | 5 | GCST90860013 | no MR -> candidate analysis |
| ICAM3/LY9 protein level ratio | 4e-781 | rs535241 | 1 | GCST90315121 | no MR -> candidate analysis |
| Circulating SLAMF7 levels | 8e-686 | rs67841898 | 1 | GCST90859745 | no MR -> candidate analysis |
| LY9 protein levels | 9e-214 | rs35759983 | 10 | GCST90469824 | no MR -> candidate analysis |
| T-lymphocyte surface antigen Ly-9 levels | 3e-161 | rs12128261 | 6 | GCST90249898 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 2e-92 | rs556753 | 3 | GCST90838667 | no MR -> candidate analysis |
| Serum levels of protein LY9 | 4e-51 | rs6659569 | 1 | GCST90088316 | no MR -> candidate analysis |
| SLAMF7 protein levels | 7e-49 | rs139428867 | 6 | GCST90470651 | no MR -> candidate analysis |
| Lymphocyte count | 6e-46 | rs494091 | 6 | GCST90002316 | no MR -> candidate analysis |
| CD48 protein levels | 2e-43 | rs41266925 | 7 | GCST90468635 | no MR -> candidate analysis |
| Lymphocyte count (UKB data field 30120) | 6e-39 | rs494091 | 1 | GCST90468082 | no MR -> candidate analysis |
| Blood protein levels | 5e-34 | rs540254 | 2 | GCST006585 | no MR -> candidate analysis |
| _...and 15 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 147 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| CINCA syndrome | 0.304 | — | established (curated) | no MR -> candidate analysis |

> Of the 1 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 2 known modulators (SLAM family member 7) |
| gnomAD constraint | pLI=8.3e-19, LOEUF=1.13 — LoF-tolerant |
| GWAS Catalog | 135 unique SNPs / 320 rows |
| ClinVar | 135 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 147 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'LY9' and resolved to 'SLAM family member 7' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 135 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 27 traits by best p-value, aggregated from 70 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9HBG7 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000122224/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3559386/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/LY9 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/LY9 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=LY9%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/LY9 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:39:23  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
