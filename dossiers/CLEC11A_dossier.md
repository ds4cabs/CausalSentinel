# Protein Dossier — CLEC11A (C-type lectin domain family 11 member A)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: K40 Inguinal hernia | 0.292 | 0.082 | 3.67e-04 | Wald ratio | 1 | cis | NA |
| Ovarian cancer | 0.28 | 0.101 | 0.00568 | Wald ratio | 1 | cis | NA |
| Endometrioid ovarian cancer | 0.534 | 0.22 | 0.0151 | Wald ratio | 1 | cis | NA |
| Putamen volume | 113 | 46.9 | 0.0155 | Wald ratio | 1 | cis | NA |
| High grade serous ovarian cancer | 0.27 | 0.12 | 0.0243 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: basal cell carcinoma | 0.297 | 0.142 | 0.0358 | Wald ratio | 1 | cis | NA |
| Subjective well being | 0.0519 | 0.026 | 0.0455 | Wald ratio | 1 | cis | NA |
| Mean cell haemoglobin concentration | 0.0513 | 0.026 | 0.0483 | Wald ratio | 1 | cis | NA |
| Schizophrenia | -0.16 | 0.0818 | 0.0499 | Wald ratio | 1 | cis | NA |
| Weight | -0.0303 | 0.0157 | 0.0545 | Wald ratio | 1 | cis | NA |
| Clear cell ovarian cancer | 0.58 | 0.307 | 0.0591 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R11 Nausea and vomiting | 0.381 | 0.204 | 0.0616 | Wald ratio | 1 | cis | NA |
| _...and 80 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2966_65_2` | SCGF-beta | Suhre K | 2019 |
| `prot-c-4500_50_2` | SCGF-alpha | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_39 association rows across 18 traits (35 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating CLEC11A levels | 7e-404 | rs141369989 | 5 | GCST90860601 | no MR -> candidate analysis |
| CLEC11A protein levels | 2e-184 | rs562569155 | 3 | GCST90468764 | no MR -> candidate analysis |
| Stem Cell Growth Factor-alpha levels | 1e-177 | rs116924815 | 4 | GCST90249448 | no MR -> candidate analysis |
| Stem Cell Growth Factor-beta levels | 9e-149 | rs116924815 | 5 | GCST90249449 | no MR -> candidate analysis |
| KLK15 protein levels | 2e-63 | rs8104100 | 2 | GCST90469701 | no MR -> candidate analysis |
| Serum levels of protein CLEC11A | 9e-37 | rs142930583 | 3 | GCST90088721 | no MR -> candidate analysis |
| Stem Cell Growth Factor-beta levels (CLEC11A.2966.65.2) | 2e-16 | rs182722517 | 1 | GCST90242896 | no MR -> candidate analysis |
| Stem cell growth factor beta levels | 2e-16 | rs116924815 | 1 | GCST004428 | no MR -> candidate analysis |
| Cerebrospinal fluid protein CLEC11A levels | 3e-15 | rs11084024 | 1 | GCST90944712 | no MR -> candidate analysis |
| Height | 9e-15 | rs562569155 | 5 | GCST90025949 | no MR -> candidate analysis |
| Standing height (UKB data field 50) | 2e-12 | rs562569155 | 1 | GCST90468178 | no MR -> candidate analysis |
| Blood protein levels | 4e-9 | rs13866 | 2 | GCST006585 | no MR -> candidate analysis |
| _...and 6 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=7.3e-13, LOEUF=1.37 — LoF-tolerant |
| GWAS Catalog | 61 unique SNPs / 122 rows |
| ClinVar | 80 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 517 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'CLEC11A'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 80 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 18 of 18 traits by best p-value, aggregated from 39 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9Y240 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000105472/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CLEC11A — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CLEC11A — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CLEC11A%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CLEC11A — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:52:19  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
