# Protein Dossier — CHI3L1 (Chitinase-3-like protein 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: asthma | -0.0195 | 0.00674 | 0.00386 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: retinal detachment | 0.081 | 0.0379 | 0.0328 | Wald ratio | 1 | cis | NA |
| Fracture resulting from simple fall | 0.0131 | 0.00616 | 0.0337 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: joint disorder | -0.0777 | 0.0373 | 0.037 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: kidney stone or ureter stone or bladder stone | 0.0509 | 0.0253 | 0.0447 | Wald ratio | 1 | cis | NA |
| Sodium in urine | 0.00451 | 0.00232 | 0.052 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | 0.00385 | 0.00204 | 0.0591 | Wald ratio | 1 | cis | NA |
| Intracranial volume | -3.3e+03 | 1.86e+03 | 0.0762 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hayfever or allergic rhinitis | -0.0169 | 0.00987 | 0.0872 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Glaucoma | 0.0311 | 0.0191 | 0.104 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: B37 Candidiasis | 0.156 | 0.0972 | 0.108 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: S76 Injury of muscle and tendon at hip and thigh level | 0.151 | 0.0974 | 0.121 | Wald ratio | 1 | cis | NA |
| _...and 45 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_60 association rows across 27 traits (56 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating CHI3L1 levels | 8e-2951 | rs10920579 | 2 | GCST90859978 | no MR -> candidate analysis |
| Chitinase-3-like protein 1 levels | 1e-2203 | rs2071579 | 13 | GCST90247006 | no MR -> candidate analysis |
| CHI3L1/HSPG2 protein level ratio | 2e-1839 | rs4950928 | 1 | GCST90314043 | no MR -> candidate analysis |
| CHI3L1/PRSS8 protein level ratio | 2e-1731 | rs4950928 | 1 | GCST90314044 | no MR -> candidate analysis |
| CD55/CHI3L1 protein level ratio | 1e-1726 | rs4950928 | 1 | GCST90313845 | no MR -> candidate analysis |
| Chitinase-3-like protein 1 levels (CHI3L1.11104.13.3) | 7e-746 | rs10920578 | 4 | GCST90240682 | no MR -> candidate analysis |
| Blood protein levels | 2e-426 | rs903357 | 2 | GCST006585 | no MR -> candidate analysis |
| Blood protein levels in cardiovascular risk | 2e-236 | rs2153101 | 1 | GCST009731 | no MR -> candidate analysis |
| Chitotriosidase-1 levels | 3e-196 | rs2494297 | 5 | GCST90425825 | no MR -> candidate analysis |
| CHI3L1 protein levels | 1e-173 | rs12410110 | 9 | GCST90468743 | no MR -> candidate analysis |
| Circulating CHIT1 levels | 4e-123 | rs183979623 | 2 | GCST90859952 | no MR -> candidate analysis |
| CH3L1 protein level (protein group normalized intensity) | 2e-93 | rs880633 | 1 | GCST90570726 | no MR -> candidate analysis |
| _...and 15 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 977 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| schizophrenia | 0.195 | — | established (curated) | no MR -> candidate analysis |
| asthma | 0.355 | — | established (curated) | MR: beta=-0.0195, p=0.00386 (cis) |
| childhood onset asthma | 0.276 | — | common-variant locus | no MR -> candidate analysis |
| lower respiratory tract disorder | 0.237 | — | common-variant locus | no MR -> candidate analysis |
| chronic obstructive pulmonary disease | 0.053 | — | common-variant locus | no MR -> candidate analysis |

> Of the 5 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Chitinase-3-like protein 1) |
| gnomAD constraint | pLI=3.4e-08, LOEUF=0.999 — LoF-tolerant |
| GWAS Catalog | 123 unique SNPs / 268 rows |
| ClinVar | 124 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 977 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'CHI3L1' and resolved to 'Chitinase-3-like protein 1' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 124 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 27 traits by best p-value, aggregated from 60 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P36222 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000133048/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL5724768/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CHI3L1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CHI3L1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CHI3L1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CHI3L1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:50:09  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
