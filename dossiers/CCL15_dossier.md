# Protein Dossier — CCL15 (C-C motif chemokine 15)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Subjective well being | -0.0124 | 0.00414 | 0.0027 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: asthma | -0.0225 | 0.00769 | 0.00344 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: mania or bipolar disorder or manic depression | 0.13 | 0.0463 | 0.00501 | Wald ratio | 1 | cis | NA |
| Schizophrenia | -0.0294 | 0.011 | 0.00753 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | -0.0889 | 0.0349 | 0.0109 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: D12 Benign neoplasm of colon  rectum  anus and anal canal | 0.0542 | 0.0215 | 0.0115 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: gastro-oesophageal reflux (gord)  or  gastric reflux | 0.0314 | 0.0125 | 0.012 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: bladder problem (not cancer) | -0.0915 | 0.0386 | 0.0178 | Wald ratio | 1 | cis | NA |
| Sleep duration | -0.00481 | 0.00209 | 0.0216 | Wald ratio | 1 | cis | NA |
| Intracranial volume | -4.66e+03 | 2.11e+03 | 0.027 | Wald ratio | 1 | cis | NA |
| Height | 0.0195 | 0.00887 | 0.0278 | Wald ratio | 1 | cis | NA |
| Serum creatinine (eGFRcrea) | -0.00231 | 0.00106 | 0.0303 | Wald ratio | 1 | cis | NA |
| _...and 101 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3509_1_1` | MIP-5 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_135 association rows across 61 traits (130 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating CCL15 levels | 2e-5134 | rs854624 | 3 | GCST90859974 | no MR -> candidate analysis |
| CCL14/CCL23 protein level ratio | 8e-1578 | rs72830000 | 1 | GCST90313678 | no MR -> candidate analysis |
| C-C motif chemokine 15 levels | 3e-1432 | rs854628 | 11 | GCST90246903 | no MR -> candidate analysis |
| CCL15/CCL23 protein level ratio | 4e-1384 | rs75238886 | 1 | GCST90313681 | no MR -> candidate analysis |
| CCL14/CST3 protein level ratio | 1e-1319 | rs72830000 | 1 | GCST90313679 | no MR -> candidate analysis |
| Circulating CCL14 levels | 5e-1269 | rs9892586 | 2 | GCST90860489 | no MR -> candidate analysis |
| Circulating CCL23 levels (id: OID00530_OID20693) | 2e-1094 | rs712048 | 3 | GCST90859884 | no MR -> candidate analysis |
| Circulating CCL23 levels (id: OID00811_OID20693) | 2e-846 | rs712048 | 3 | GCST90860141 | no MR -> candidate analysis |
| C-C motif chemokine 14 levels | 2e-763 | rs7222922 | 10 | GCST90246902 | no MR -> candidate analysis |
| C-C motif chemokine 15 levels (CCL15.14109.15.3) | 3e-411 | rs854624 | 1 | GCST90240483 | no MR -> candidate analysis |
| Ck-beta-8-1 levels | 9e-326 | rs712048 | 3 | GCST90247039 | no MR -> candidate analysis |
| Serum levels of protein CCL15 | 3e-293 | rs41508645 | 1 | GCST90088428 | no MR -> candidate analysis |
| _...and 49 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.0047, LOEUF=1.36 — LoF-tolerant |
| GWAS Catalog | 165 unique SNPs / 400 rows |
| ClinVar | 25 records; 8 pathogenic in sample of 25 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 242 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'CCL15'.
- **`clinvar`** — Pathogenic count is over the 25 record(s) retrieved, NOT over all 25 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 61 traits by best p-value, aggregated from 135 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q16663 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000275718/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CCL15 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CCL15 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CCL15%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CCL15 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:31:16  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
