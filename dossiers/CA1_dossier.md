# Protein Dossier — CA1 (Carbonic anhydrase 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Fractured bone site(s): Other bones | 0.181 | 0.0604 | 0.00271 | Wald ratio | 1 | cis | NA |
| Fractured or broken bones in last 5 years | 0.134 | 0.0453 | 0.003 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | 0.0374 | 0.0136 | 0.00596 | Wald ratio | 1 | cis | NA |
| Serum creatinine (eGFRcrea) | -0.0156 | 0.00626 | 0.0124 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K35 Acute appendicitis | 0.401 | 0.165 | 0.0148 | Wald ratio | 1 | cis | NA |
| Potassium in urine | -0.0406 | 0.0168 | 0.0157 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | 0.0345 | 0.0143 | 0.016 | Wald ratio | 1 | cis | NA |
| Birth length | -0.166 | 0.0701 | 0.0178 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: small intestine or small bowel cancer | 0.871 | 0.387 | 0.0246 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | 0.0361 | 0.0166 | 0.0292 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: chronic obstructive airways disease or copd | 0.412 | 0.197 | 0.0365 | Wald ratio | 1 | cis | NA |
| Neuroblastoma | 0.63 | 0.303 | 0.0379 | Wald ratio | 1 | cis | NA |
| _...and 104 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-4969_2_1` | Carbonic anhydrase I | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_61 association rows across 38 traits (60 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating CA13 levels | 5e-637 | rs56072918 | 2 | GCST90860354 | no MR -> candidate analysis |
| Carbonic anhydrase 13 levels | 2e-220 | rs73688702 | 2 | GCST90246861 | no MR -> candidate analysis |
| CA1/HMBS protein level ratio | 4e-114 | rs1496532 | 1 | GCST90313573 | no MR -> candidate analysis |
| BLVRB/CA1 protein level ratio | 1e-91 | rs1496532 | 1 | GCST90313521 | no MR -> candidate analysis |
| CA1/TGM2 protein level ratio | 1e-52 | rs1496532 | 1 | GCST90313575 | no MR -> candidate analysis |
| mean corpuscular hemoglobin concentration (MCHC, mean, inv-n | 3e-47 | rs142714972 | 1 | GCST90479670 | no MR -> candidate analysis |
| Circulating CA1 levels | 5e-44 | rs12544332 | 2 | GCST90860427 | no MR -> candidate analysis |
| CA1 protein levels | 2e-43 | rs12544332 | 1 | GCST90468510 | no MR -> candidate analysis |
| mean corpuscular hemoglobin concentration (MCHC, maximum, in | 6e-43 | rs142714972 | 1 | GCST90479669 | no MR -> candidate analysis |
| Carbonic anhydrase 1 levels | 2e-42 | rs116866430 | 1 | GCST90162208 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 4e-39 | rs12544332 | 2 | GCST90838669 | no MR -> candidate analysis |
| High light scatter reticulocyte count | 4e-37 | rs12544332 | 3 | GCST90002385 | no MR -> candidate analysis |
| _...and 26 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 6 known modulators (Carbonic anhydrase 1) |
| gnomAD constraint | pLI=2.2e-09, LOEUF=1.29 — LoF-tolerant |
| GWAS Catalog | 57 unique SNPs / 114 rows |
| ClinVar | 80 records; 4 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 401 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'CA1' and resolved to 'Carbonic anhydrase 1' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 80 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 38 traits by best p-value, aggregated from 61 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P00915 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000133742/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL261/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CA1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CA1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CA1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CA1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:24:12  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
