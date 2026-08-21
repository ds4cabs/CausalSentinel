# Protein Dossier — OBP2B (Odorant-binding protein 2b)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: D12 Benign neoplasm of colon  rectum  anus and anal canal | 0.084 | 0.0272 | 0.00201 | Inverse variance weighted | 2 | trans | NA |
| Diagnoses - main ICD10: D12 Benign neoplasm of colon  rectum  anus and anal canal | 0.084 | 0.0272 | 0.00201 | Inverse variance weighted | 2 | cis | NA |
| Clear cell ovarian cancer | 0.166 | 0.0585 | 0.00452 | Inverse variance weighted | 2 | trans | NA |
| Clear cell ovarian cancer | 0.166 | 0.0585 | 0.00452 | Inverse variance weighted | 2 | cis | NA |
| HDL cholesterol | -0.0192 | 0.00699 | 0.00598 | Inverse variance weighted | 2 | trans | NA |
| HDL cholesterol | -0.0192 | 0.00699 | 0.00598 | Inverse variance weighted | 2 | cis | NA |
| Cancer code  self-reported: malignant melanoma | 0.097 | 0.0361 | 0.00711 | Inverse variance weighted | 2 | trans | NA |
| Cancer code  self-reported: malignant melanoma | 0.097 | 0.0361 | 0.00711 | Inverse variance weighted | 2 | cis | NA |
| Non-cancer illness code  self-reported: depression | 0.0354 | 0.0139 | 0.011 | Inverse variance weighted | 2 | trans | NA |
| Non-cancer illness code  self-reported: depression | 0.0354 | 0.0139 | 0.011 | Inverse variance weighted | 2 | cis | NA |
| Gallbladder cancer | 1.8 | 0.709 | 0.0112 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M16 Coxarthrosis [arthrosis of hip] | -0.0797 | 0.0316 | 0.0116 | Inverse variance weighted | 2 | trans | NA |
| _...and 155 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_182 association rows across 89 traits (177 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Serum alkaline phosphatase levels | 3e-665 | rs11244035 | 6 | GCST90019494 | no MR -> candidate analysis |
| CDH5/NOTCH1 protein level ratio | 2e-463 | rs7864821 | 1 | GCST90313957 | no MR -> candidate analysis |
| OBP2B protein levels | 4e-225 | rs147487194 | 8 | GCST90470113 | no MR -> candidate analysis |
| PTPRM protein levels | 9e-206 | rs10901241 | 5 | GCST90470384 | no MR -> candidate analysis |
| ABO protein levels | 5e-185 | rs7044834 | 8 | GCST90468191 | no MR -> candidate analysis |
| CDH5 protein levels | 1e-183 | rs10901241 | 6 | GCST90468676 | no MR -> candidate analysis |
| Serum levels of protein CEL | 3e-115 | rs146984623 | 1 | GCST90090829 | no MR -> candidate analysis |
| Odorant-binding protein 2b levels | 8e-103 | rs4962104 | 1 | GCST90248773 | no MR -> candidate analysis |
| Alkaline phosphatase (UKB data field 30610) | 6e-101 | rs189043092 | 8 | GCST90468060 | no MR -> candidate analysis |
| SELE protein levels | 7e-99 | rs189043092 | 5 | GCST90470566 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 3e-92 | rs6597608 | 1 | GCST90838669 | no MR -> candidate analysis |
| TIE1 protein levels | 2e-89 | rs140728646 | 3 | GCST90470863 | no MR -> candidate analysis |
| _...and 77 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.11, LOEUF=0.783 — LoF-tolerant |
| GWAS Catalog | 322 unique SNPs / 816 rows |
| ClinVar | 79 records; 5 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 85 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'OBP2B'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 79 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 89 traits by best p-value, aggregated from 182 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9NPH6 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000171102/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/OBP2B — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/OBP2B — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=OBP2B%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/OBP2B — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:08:34  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
