# Protein Dossier — KYNU (Kynureninase)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Forced vital capacity (FVC) | -0.0105 | 0.00246 | 1.87e-05 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | -0.0102 | 0.0026 | 8.52e-05 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | -0.0144 | 0.00389 | 2.22e-04 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: asthma | 0.0301 | 0.00816 | 2.27e-04 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hayfever or allergic rhinitis | 0.041 | 0.0118 | 5.37e-04 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K44 Diaphragmatic hernia | 0.0726 | 0.0223 | 0.00116 | Wald ratio | 1 | cis | NA |
| Weight | -0.0079 | 0.00265 | 0.00288 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Cataract | 0.0425 | 0.0158 | 0.00703 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | 0.0344 | 0.0129 | 0.00754 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: depression | 0.0281 | 0.012 | 0.0194 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R35 Polyuria | 0.101 | 0.0435 | 0.0198 | Wald ratio | 1 | cis | NA |
| Alcohol intake frequency | 0.0102 | 0.00444 | 0.0217 | Wald ratio | 1 | cis | NA |
| _...and 98 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-4559_64_2` | KYNU | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_99 association rows across 44 traits (91 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Kynureninase levels | 1e-519 | rs73961713 | 7 | GCST90248219 | no MR -> candidate analysis |
| Circulating KYNU levels | 1e-372 | rs6711280 | 5 | GCST90859740 | no MR -> candidate analysis |
| Bone mineral density mean | 1e-300 | rs71423227 | 21 | GCST90321120 | no MR -> candidate analysis |
| Serum levels of protein KYNU | 1e-145 | rs12477146 | 1 | GCST90088740 | no MR -> candidate analysis |
| DCXR/KYNU protein level ratio | 2e-124 | rs17808482 | 1 | GCST90314438 | no MR -> candidate analysis |
| KYNU protein levels | 4e-123 | rs17808482 | 3 | GCST90469722 | no MR -> candidate analysis |
| Blood protein levels | 7e-83 | rs3768844 | 1 | GCST006585 | no MR -> candidate analysis |
| Kynureninase levels (KYNU.4559.64.2) | 2e-58 | rs3816193 | 1 | GCST90241721 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 2e-57 | rs7607734 | 3 | GCST90838671 | no MR -> candidate analysis |
| Protein quantitative trait loci | 5e-41 | rs3768844 | 1 | GCST010900 | no MR -> candidate analysis |
| X-15503 levels | 1e-40 | rs354687 | 6 | GCST90245602 | no MR -> candidate analysis |
| Lymphocyte count (UKB data field 30120) | 2e-39 | rs74847330 | 1 | GCST90468082 | no MR -> candidate analysis |
| _...and 32 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1349 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| vertebral, cardiac, renal, and limb defects syndrome 2 | 0.837 | — | established (curated) | no MR -> candidate analysis |
| congenital vertebral-cardiac-renal anomalies syndrome | 0.804 | — | established (curated) | no MR -> candidate analysis |
| encephalopathy due to hydroxykynureninuria | 0.669 | — | established (curated) | no MR -> candidate analysis |
| Catel-Manzke syndrome | 0.796 | — | established (curated) | no MR -> candidate analysis |
| cataract | 0.66 | — | common-variant locus | MR: beta=0.0425, p=0.00703 (cis) |
| pulmonary vascular congestion | 0.536 | — | common-variant locus | no MR -> candidate analysis |
| macular degeneration | 0.501 | — | common-variant locus | no MR -> candidate analysis |
| respiratory system disorder | 0.447 | — | common-variant locus | no MR -> candidate analysis |
| malunion fracture | 0.427 | — | common-variant locus | no MR -> candidate analysis |
| placental abruption | 0.419 | — | common-variant locus | no MR -> candidate analysis |
| transient ischemic attack | 0.408 | — | common-variant locus | no MR -> candidate analysis |
| lens disorder | 0.409 | — | common-variant locus | no MR -> candidate analysis |
| Age-related cataract | 0.409 | — | common-variant locus | no MR -> candidate analysis |
| injury | 0.396 | — | common-variant locus | no MR -> candidate analysis |
| ovarian neoplasm | 0.396 | — | common-variant locus | no MR -> candidate analysis |

> Of the 15 rows above, **14 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Kynureninase) |
| gnomAD constraint | pLI=2.8e-17, LOEUF=1.14 — LoF-tolerant |
| GWAS Catalog | 93 unique SNPs / 186 rows |
| ClinVar | 162 records; 3 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1349 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'KYNU' and resolved to 'Kynureninase' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 162 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 44 traits by best p-value, aggregated from 99 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q16719 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000115919/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL5100/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/KYNU — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/KYNU — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=KYNU%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/KYNU — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:26:48  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
