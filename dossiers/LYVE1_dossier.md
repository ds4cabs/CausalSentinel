# Protein Dossier — LYVE1 (Lymphatic vessel endothelial hyaluronic acid receptor 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: N40 Hyperplasia of prostate | 0.488 | 0.105 | 3.63e-06 | Wald ratio | 1 | cis | NA |
| Hippocampus volume | 77.7 | 30.5 | 0.011 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: uterine fibroids | 0.251 | 0.104 | 0.0155 | Wald ratio | 1 | cis | NA |
| Height | 0.0542 | 0.0233 | 0.02 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: iron deficiency anaemia | 0.368 | 0.159 | 0.0208 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I83 Varicose veins of lower extremities | 0.209 | 0.0932 | 0.0248 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: bladder problem (not cancer) | 0.338 | 0.157 | 0.0311 | Wald ratio | 1 | cis | NA |
| Forearm bone mineral density | -0.217 | 0.107 | 0.0423 | Wald ratio | 1 | cis | NA |
| HbA1C | -0.0607 | 0.0309 | 0.0494 | Wald ratio | 1 | cis | NA |
| Birth weight | -0.0485 | 0.0252 | 0.0543 | Wald ratio | 1 | cis | NA |
| Primary sclerosing cholangitis  | -0.388 | 0.209 | 0.0629 | Wald ratio | 1 | cis | NA |
| Cough on most days | 0.136 | 0.0735 | 0.0634 | Wald ratio | 1 | cis | NA |
| _...and 64 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3206_4_2` | LYVE1 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_18 association rows across 16 traits (9 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| LYVE1 protein levels | 8e-88 | rs114708736 | 3 | GCST90469832 | no MR -> candidate analysis |
| Serum levels of protein LYVE1 | 1e-19 | rs116573529 | 1 | GCST90088269 | no MR -> candidate analysis |
| Lymphatic vessel endothelial hyaluronic acid receptor 1 leve | 7e-12 | rs11042892 | 1 | GCST90248369 | no MR -> candidate analysis |
| Blood protein levels | 3e-11 | rs114527818 | 1 | GCST006585 | no MR -> candidate analysis |
| Forced expiratory volume in 1 second (FEV1) | 5e-11 | rs7115735 | 1 | GCST90705070 | no MR -> candidate analysis |
| Peak expiratory flow | 2e-9 | rs7115735 | 1 | GCST90244095 | no MR -> candidate analysis |
| White blood cell count (monocyte) | 3e-8 | rs76224505 | 1 | GCST90026507 | no MR -> candidate analysis |
| Gut microbiome abundance (class Bifidobacterium animalis (at | 5e-8 | rs17403942 | 1 | GCST90568939 | no MR -> candidate analysis |
| Gut microbial network clusters (Salmon (at 1 year) x Any Bre | 1e-7 | rs17403620 | 1 | GCST90569450 | no MR -> candidate analysis |
| Suicide behavior | 9e-7 | rs3741042 | 1 | GCST90244689 | no MR -> candidate analysis |
| Crohn's disease (Tractor method with European ancestry) | 1e-6 | rs117479720 | 1 | GCST90825978 | no MR -> candidate analysis |
| Suicide | 3e-6 | rs3741042 | 1 | GCST90244688 | no MR -> candidate analysis |
| _...and 4 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 479 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| hypothyroidism | 0.316 | — | common-variant locus | MR: beta=-0.108, p=0.186 (cis) |
| thyroid gland disorder | 0.289 | — | common-variant locus | no MR -> candidate analysis |
| Hashimoto thyroiditis | 0.289 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.239 | — | common-variant locus | no MR -> candidate analysis |
| heart disorder | 0.076 | — | common-variant locus | no MR -> candidate analysis |
| gallbladder disorder | 0.069 | — | common-variant locus | no MR -> candidate analysis |

> Of the 6 rows above, **5 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | not available |
| GWAS Catalog | 93 unique SNPs / 173 rows |
| ClinVar | 69 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 479 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'LYVE1'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 69 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 16 of 16 traits by best p-value, aggregated from 18 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9Y5Y7 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000133800/associations — _Open Targets data release 26.06_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/LYVE1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=LYVE1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/LYVE1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:40:16  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: gnomad
