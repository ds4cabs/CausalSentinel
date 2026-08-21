# Protein Dossier — CSF1 (Macrophage colony-stimulating factor 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Forced vital capacity (FVC) | -0.0431 | 0.0132 | 0.0011 | Wald ratio | 1 | cis | NA |
| HDL cholesterol | -0.105 | 0.0333 | 0.00169 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: anxiety or panic attacks | 0.294 | 0.105 | 0.0051 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: malignant melanoma | 0.342 | 0.133 | 0.01 | Wald ratio | 1 | cis | NA |
| Systolic blood pressure  automated reading | 0.0406 | 0.0165 | 0.0138 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | -0.0338 | 0.0139 | 0.0154 | Wald ratio | 1 | cis | NA |
| Lumbar spine bone mineral density | -0.14 | 0.0581 | 0.0162 | Wald ratio | 1 | cis | NA |
| Femoral neck bone mineral density | -0.12 | 0.0499 | 0.0163 | Wald ratio | 1 | cis | NA |
| Neo-conscientiousness | -1.19 | 0.504 | 0.0187 | Wald ratio | 1 | cis | NA |
| Coronary heart disease | 0.145 | 0.0633 | 0.0225 | Wald ratio | 1 | cis | NA |
| Mean platelet volume | -0.018 | 0.008 | 0.0244 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I83 Varicose veins of lower extremities | 0.203 | 0.0928 | 0.0285 | Wald ratio | 1 | cis | NA |
| _...and 93 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3738_54_1` | CSF-1 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_244 association rows across 166 traits (236 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating CSF1 levels (id: OID00562_OID20719) | 2e-231 | rs17610659 | 2 | GCST90859911 | no MR -> candidate analysis |
| BTN2A1/CSF1 protein level ratio | 1e-211 | rs1058885 | 1 | GCST90313541 | no MR -> candidate analysis |
| CSF1/IFNGR1 protein level ratio | 6e-199 | rs1058885 | 1 | GCST90314283 | no MR -> candidate analysis |
| CSF1/LTBR protein level ratio | 7e-197 | rs1058885 | 1 | GCST90314287 | no MR -> candidate analysis |
| CSF1 protein levels | 9e-180 | rs17610659 | 4 | GCST90468881 | no MR -> candidate analysis |
| Circulating CSF1 levels (id: OID00843_OID20719) | 8e-179 | rs17610659 | 2 | GCST90860168 | no MR -> candidate analysis |
| CSF1/SEMA3F protein level ratio | 3e-140 | rs7540934 | 1 | GCST90314288 | no MR -> candidate analysis |
| Aspartate aminotransferase levels | 9e-115 | rs333948 | 11 | GCST90662897 | no MR -> candidate analysis |
| CSF1/IL10RB protein level ratio | 3e-95 | rs6675402 | 1 | GCST90314284 | no MR -> candidate analysis |
| Macrophage colony-stimulating factor 1 levels | 2e-61 | rs11579145 | 2 | GCST90012018 | no MR -> candidate analysis |
| Aspartate aminotransferase levels (UKB data field 30650) | 3e-54 | rs333947 | 1 | GCST90468063 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 4e-48 | rs333947 | 3 | GCST90838669 | no MR -> candidate analysis |
| _...and 154 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 2136 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| type 2 diabetes mellitus | 0.595 | — | common-variant locus | no MR -> candidate analysis |
| metabolic syndrome | 0.489 | — | common-variant locus | no MR -> candidate analysis |
| otosclerosis | 0.434 | — | common-variant locus | no MR -> candidate analysis |
| adult-onset Still disease | 0.378 | — | common-variant locus | no MR -> candidate analysis |
| secondary malignant neoplasm | 0.19 | — | common-variant locus | no MR -> candidate analysis |
| response to statin | 0.162 | — | common-variant locus | no MR -> candidate analysis |

> Of the 6 rows above, **6 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 2 known modulators (Macrophage colony-stimulating factor 1) |
| gnomAD constraint | pLI=1, LOEUF=0.321 — LoF-INTOLERANT |
| GWAS Catalog | 69 unique SNPs / 138 rows |
| ClinVar | 121 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 2136 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'CSF1' and resolved to 'Macrophage colony-stimulating factor 1' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 121 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 166 traits by best p-value, aggregated from 244 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P09603 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000184371/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3989382/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CSF1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CSF1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CSF1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CSF1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:05:32  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
