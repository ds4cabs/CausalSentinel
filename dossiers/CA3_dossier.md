# Protein Dossier — CA3 (Carbonic anhydrase 3)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: R11 Nausea and vomiting | 0.451 | 0.134 | 7.69e-04 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | -0.0336 | 0.0106 | 0.00158 | Wald ratio | 1 | cis | NA |
| Subjective well being | -0.0507 | 0.0184 | 0.00596 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M72 Fibroblastic disorders | 0.292 | 0.135 | 0.0301 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Ankle | 0.198 | 0.0917 | 0.031 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | -0.0242 | 0.0112 | 0.0312 | Wald ratio | 1 | cis | NA |
| Alcohol intake frequency | -0.0402 | 0.0192 | 0.0359 | Wald ratio | 1 | cis | NA |
| Pulse rate | 0.0477 | 0.0228 | 0.0364 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertension | -0.0472 | 0.0232 | 0.0415 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: basal cell carcinoma | 0.223 | 0.11 | 0.0421 | Wald ratio | 1 | cis | NA |
| Hippocampus volume | 50.5 | 25.8 | 0.0505 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: J33 Nasal polyp | 0.282 | 0.146 | 0.0524 | Wald ratio | 1 | cis | NA |
| _...and 80 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3799_11_2` | Carbonic anhydrase III | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_30 association rows across 23 traits (29 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| CA1/CA3 protein level ratio | 9e-287 | rs11781220 | 1 | GCST90313572 | no MR -> candidate analysis |
| CA3/HMBS protein level ratio | 4e-143 | rs11781220 | 1 | GCST90313584 | no MR -> candidate analysis |
| Circulating CA3 levels | 1e-134 | rs2072696 | 2 | GCST90860436 | no MR -> candidate analysis |
| BLVRB/CA3 protein level ratio | 1e-130 | rs11781220 | 1 | GCST90313523 | no MR -> candidate analysis |
| CA3 protein levels | 5e-125 | rs2072696 | 3 | GCST90468512 | no MR -> candidate analysis |
| ALDH1A1/CA3 protein level ratio | 1e-103 | rs11781220 | 1 | GCST90313244 | no MR -> candidate analysis |
| Carbonic anhydrase 3 levels | 7e-44 | rs2072696 | 2 | GCST90246863 | no MR -> candidate analysis |
| Bone mineral density mean | 4e-39 | rs72682966 | 2 | GCST90321120 | no MR -> candidate analysis |
| Carbonic anhydrase 1 levels | 5e-32 | rs7837972 | 1 | GCST90137710 | no MR -> candidate analysis |
| Mean corpuscular hemoglobin concentration | 7e-27 | rs13273654 | 3 | GCST90002328 | no MR -> candidate analysis |
| Mean reticulocyte volume (UKB data field 30260) | 4e-19 | rs11261474 | 1 | GCST90468088 | no MR -> candidate analysis |
| Immature fraction of reticulocytes | 6e-19 | rs1390712 | 1 | GCST90002387 | no MR -> candidate analysis |
| _...and 11 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 227 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| essential tremor | 0.386 | — | common-variant locus | no MR -> candidate analysis |

> Of the 1 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Carbonic anhydrase 3) |
| gnomAD constraint | pLI=2.3e-09, LOEUF=1.14 — LoF-tolerant |
| GWAS Catalog | 57 unique SNPs / 103 rows |
| ClinVar | 66 records; 4 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 227 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'CA3' and resolved to 'Carbonic anhydrase 3' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 66 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 23 traits by best p-value, aggregated from 30 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P07451 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000164879/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2885/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CA3 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CA3 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CA3%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CA3 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:25:05  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
