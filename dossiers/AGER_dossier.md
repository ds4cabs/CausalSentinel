# Protein Dossier — AGER (Advanced glycation end product-specific receptor)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Age at menarche | 0.112 | 0.0244 | 4.40e-06 | Wald ratio | 1 | trans | NA |
| Body mass index (BMI) | -0.0414 | 0.0103 | 6.09e-05 | Wald ratio | 1 | trans | NA |
| Forced vital capacity (FVC) | 0.0317 | 0.00847 | 1.82e-04 | Wald ratio | 1 | trans | NA |
| Alcohol intake frequency | -0.0566 | 0.0153 | 2.04e-04 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: M23 Internal derangement of knee | 0.197 | 0.0572 | 5.74e-04 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: N81 Female genital prolapse | 0.234 | 0.0686 | 6.64e-04 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: hypertrophic cardiomyopathy (hcm  or  hocm) | 0.959 | 0.31 | 0.00196 | Wald ratio | 1 | trans | NA |
| Haemoglobin concentration | 0.0665 | 0.0229 | 0.00362 | Wald ratio | 1 | trans | NA |
| Weight | -0.0243 | 0.00911 | 0.00754 | Wald ratio | 1 | trans | NA |
| Type 2 diabetes | -0.163 | 0.0612 | 0.00772 | Wald ratio | 1 | trans | NA |
| HOMA-B | -0.0357 | 0.0137 | 0.00916 | Wald ratio | 1 | trans | NA |
| Neo-agreeableness | 0.669 | 0.258 | 0.00953 | Wald ratio | 1 | trans | NA |
| _...and 100 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-4125_52_2` | sRAGE | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_58 association rows across 47 traits (56 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| FEV1 FVC ratio Z score (UKB data field 20258) | 3e-239 | rs2070600 | 1 | GCST90468165 | no MR -> candidate analysis |
| Lung function (FEV1/FVC) | 2e-227 | rs2070600 | 5 | GCST90244094 | no MR -> candidate analysis |
| Neonatal circulating Complement Component 4 (C4) protein con | 5e-189 | rs35795092 | 1 | GCST90281042 | no MR -> candidate analysis |
| SFTPD protein levels | 3e-171 | rs2070600 | 2 | GCST90470614 | no MR -> candidate analysis |
| Advanced glycosylation end product-specific receptor, solubl | 1e-113 | rs2070600 | 2 | GCST90246455 | no MR -> candidate analysis |
| Chronic obstructive pulmonary disease liability (machine lea | 3e-83 | rs9391855 | 1 | GCST90244098 | no MR -> candidate analysis |
| MICB or MICA protein levels | 1e-74 | rs35795092 | 1 | GCST90469905 | no MR -> candidate analysis |
| Hypothyroidism or rheumatoid arthritis (pleiotropy) | 1e-57 | rs1800684 | 2 | GCST90428109 | no MR -> candidate analysis |
| Peak expiratory flow | 2e-45 | rs2070600 | 1 | GCST007430 | no MR -> candidate analysis |
| Physical function (baseline) | 2e-35 | rs1035798 | 1 | GCST90565837 | no MR -> candidate analysis |
| Advanced glycosylation end product-specific receptor, solubl | 4e-33 | rs2070600 | 1 | GCST90240215 | no MR -> candidate analysis |
| Serum levels of protein AGER | 1e-31 | rs2070600 | 1 | GCST90088583 | no MR -> candidate analysis |
| _...and 35 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 1 known modulators (Advanced glycosylation end product-specific receptor) |
| gnomAD constraint | pLI=2.5e-15, LOEUF=1.2 — LoF-tolerant |
| GWAS Catalog | 414 unique SNPs / 1116 rows |
| ClinVar | 117 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1171 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'AGER' and resolved to 'Advanced glycosylation end product-specific receptor' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 117 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 47 traits by best p-value, aggregated from 58 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q15109 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000204305/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2176846/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/AGER — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/AGER — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=AGER%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/AGER — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T00:58:00  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
