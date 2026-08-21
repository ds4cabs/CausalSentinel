# Protein Dossier — PF4V1 (Platelet factor 4 variant)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Forced expiratory volume in 1-second (FEV1) | 0.0138 | 0.00463 | 0.00295 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: enlarged prostate | 0.117 | 0.0407 | 0.00405 | Wald ratio | 1 | cis | NA |
| Fasting glucose | 0.0223 | 0.0083 | 0.0073 | Wald ratio | 1 | cis | NA |
| Hearing difficulty or problems: Yes | -0.0243 | 0.00946 | 0.0103 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: Z09 Follow-up examination after treatment for conditions other than malignant neoplasms | -0.111 | 0.0487 | 0.0229 | Wald ratio | 1 | cis | NA |
| Birth length | 0.0514 | 0.0229 | 0.0246 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: bladder problem (not cancer) | 0.138 | 0.0614 | 0.0249 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | 0.00952 | 0.00439 | 0.0302 | Wald ratio | 1 | cis | NA |
| Ferritin | -0.0454 | 0.0211 | 0.0313 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: C50 Malignant neoplasm of breast | 0.0745 | 0.0389 | 0.0553 | Wald ratio | 1 | cis | NA |
| Transferrin | 0.0413 | 0.0231 | 0.0735 | Wald ratio | 1 | cis | NA |
| Putamen volume | -23.5 | 13.3 | 0.0767 | Wald ratio | 1 | cis | NA |
| _...and 80 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_112 association rows across 55 traits (110 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating CXCL1 levels (id: OID00404_OID20762) | 1e-1222 | rs74544699 | 1 | GCST90859766 | no MR -> candidate analysis |
| Circulating CXCL1 levels (id: OID00496_OID20762) | 6e-1103 | rs74544699 | 1 | GCST90859853 | no MR -> candidate analysis |
| Circulating CXCL1 levels (id: OID00786_OID20762) | 5e-1070 | rs74544699 | 1 | GCST90860118 | no MR -> candidate analysis |
| Blood protein levels | 2e-250 | rs872914 | 49 | GCST006585 | no MR -> candidate analysis |
| C-X-C motif chemokine 1 levels | 9e-212 | rs3117604 | 2 | GCST90012019 | no MR -> candidate analysis |
| Growth-regulated alpha protein levels | 2e-204 | rs3117604 | 5 | GCST90161572 | no MR -> candidate analysis |
| Serum levels of protein SLC3A2 | 2e-169 | rs61360774 | 1 | GCST90089635 | no MR -> candidate analysis |
| Serum levels of protein PF4V1 | 2e-164 | rs61360774 | 1 | GCST90089132 | no MR -> candidate analysis |
| CXCL1 protein levels | 3e-133 | rs115711101 | 2 | GCST90468930 | no MR -> candidate analysis |
| Serum levels of protein EMC1 | 1e-125 | rs2233654 | 1 | GCST90086898 | no MR -> candidate analysis |
| Serum levels of protein TNFAIP8 | 5e-125 | rs2233654 | 1 | GCST90087071 | no MR -> candidate analysis |
| Growth-regulated alpha protein levels (CXCL1.2985.35.1) | 2e-101 | rs3117602 | 2 | GCST90241345 | no MR -> candidate analysis |
| _...and 43 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.093, LOEUF=1.34 — LoF-tolerant |
| GWAS Catalog | 100 unique SNPs / 220 rows |
| ClinVar | 52 records; 5 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 150 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'PF4V1'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 52 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 55 traits by best p-value, aggregated from 112 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P10720 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000109272/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PF4V1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PF4V1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PF4V1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/PF4V1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:18:15  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
