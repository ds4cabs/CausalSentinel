# Protein Dossier — CX3CL1 (Fractalkine)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Body mass index (BMI) | 0.0465 | 0.0135 | 5.66e-04 | Wald ratio | 1 | cis | NA |
| Weight | 0.0377 | 0.0119 | 0.00154 | Wald ratio | 1 | cis | NA |
| Fractured or broken bones in last 5 years | 0.113 | 0.0376 | 0.00269 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I83 Varicose veins of lower extremities | 0.202 | 0.0774 | 0.0091 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertension | 0.0565 | 0.0217 | 0.00928 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Other bones | 0.123 | 0.052 | 0.0182 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: uterine fibroids | -0.38 | 0.165 | 0.021 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M23 Internal derangement of knee | 0.171 | 0.0769 | 0.0259 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: C50 Malignant neoplasm of breast | 0.194 | 0.0875 | 0.0264 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Glaucoma | -0.358 | 0.166 | 0.0314 | Wald ratio | 1 | cis | NA |
| Vascular or heart problems diagnosed by doctor: Angina | 0.138 | 0.0662 | 0.0377 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R10 Abdominal and pelvic pain | 0.111 | 0.0585 | 0.0585 | Wald ratio | 1 | cis | NA |
| _...and 62 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2827_23_2` | Fractalkine/CX3CL-1 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_28 association rows across 22 traits (25 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating CX3CL1 levels (id: OID00552_OID20976) | 4e-311 | rs671623 | 2 | GCST90859902 | no MR -> candidate analysis |
| CX3CL1 protein levels | 8e-248 | rs781264602 | 2 | GCST90468921 | no MR -> candidate analysis |
| Circulating CX3CL1 levels (id: OID00806_OID20976) | 4e-224 | rs671623 | 2 | GCST90860136 | no MR -> candidate analysis |
| CX3CL1/EPHB6 protein level ratio | 6e-147 | rs170361 | 1 | GCST90314324 | no MR -> candidate analysis |
| CX3CL1/LAYN protein level ratio | 5e-140 | rs170361 | 1 | GCST90314325 | no MR -> candidate analysis |
| CCL17/CCL22 protein level ratio | 3e-133 | rs801506 | 1 | GCST90313682 | no MR -> candidate analysis |
| CCL17 protein levels | 1e-113 | rs8102 | 1 | GCST90468569 | no MR -> candidate analysis |
| CX3CL1 levels | 3e-86 | rs683544 | 1 | GCST90012074 | no MR -> candidate analysis |
| CCL17/CXCL3 protein level ratio | 4e-70 | rs62037082 | 1 | GCST90313685 | no MR -> candidate analysis |
| CCL17/CD69 protein level ratio | 6e-70 | rs62037082 | 1 | GCST90313684 | no MR -> candidate analysis |
| Fractalkine levels | 1e-66 | rs671623 | 3 | GCST90274778 | no MR -> candidate analysis |
| C-C motif chemokine 22 levels | 2e-38 | rs170364 | 1 | GCST90246911 | no MR -> candidate analysis |
| _...and 10 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 1 known modulators (Fractalkine) |
| gnomAD constraint | not available |
| GWAS Catalog | 72 unique SNPs / 144 rows |
| ClinVar | 121 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 817 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'CX3CL1' and resolved to 'Fractalkine' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 121 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 22 traits by best p-value, aggregated from 28 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P78423 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000006210/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4630883/ — _ChEMBL_37 (released 2026-05-01)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CX3CL1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CX3CL1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CX3CL1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:12:59  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: gnomad
