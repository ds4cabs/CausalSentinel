# Protein Dossier — PPA1 (Inorganic pyrophosphatase)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Age at menopause | -0.199 | 0.0498 | 6.33e-05 | Wald ratio | 1 | cis | NA |
| Age at menarche | 0.0548 | 0.0146 | 1.80e-04 | Wald ratio | 1 | cis | NA |
| HDL cholesterol | -0.0314 | 0.00872 | 3.18e-04 | Wald ratio | 1 | cis | NA |
| Cough on most days | 0.101 | 0.0288 | 4.63e-04 | Wald ratio | 1 | cis | NA |
| Fractured or broken bones in last 5 years | -0.0578 | 0.0205 | 0.00489 | Wald ratio | 1 | cis | NA |
| Internalizing problems | 0.157 | 0.0576 | 0.00622 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | 0.166 | 0.0629 | 0.0084 | Wald ratio | 1 | cis | NA |
| Lumbar spine bone mineral density | -0.0594 | 0.0227 | 0.00895 | Wald ratio | 1 | cis | NA |
| Neo-conscientiousness | 0.484 | 0.19 | 0.0109 | Wald ratio | 1 | cis | NA |
| 2hr glucose | 0.0947 | 0.0473 | 0.0455 | Wald ratio | 1 | cis | NA |
| Thalamus volume | -30.9 | 15.9 | 0.0528 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | 0.0101 | 0.00537 | 0.0599 | Wald ratio | 1 | cis | NA |
| _...and 107 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-5021_13_1` | PPase | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_6 association rows across 4 traits (5 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Inorganic pyrophosphatase levels | 2e-103 | rs10823500 | 3 | GCST90248117 | no MR -> candidate analysis |
| LYVE1 protein levels | 1e-17 | rs7077538 | 1 | GCST90469832 | no MR -> candidate analysis |
| ITGAM protein levels | 1e-13 | rs76809526 | 1 | GCST90469638 | no MR -> candidate analysis |
| Red blood cell count | 5e-8 | rs12771902 | 1 | GCST007069 | MR: beta=-0.00772, p=0.196 (cis) |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 184 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| frozen shoulder | 0.093 | — | common-variant locus | no MR -> candidate analysis |

> Of the 1 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Inorganic pyrophosphatase) |
| gnomAD constraint | pLI=0.00033, LOEUF=0.78 — LoF-tolerant |
| GWAS Catalog | 43 unique SNPs / 86 rows |
| ClinVar | 74 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 184 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'PPA1' and resolved to 'Inorganic pyrophosphatase' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 74 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 4 of 4 traits by best p-value, aggregated from 6 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q15181 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000180817/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL6067227/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PPA1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PPA1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PPA1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/PPA1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:33:19  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: pharmgkb
