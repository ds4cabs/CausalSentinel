# Protein Dossier — CXCL11 (C-X-C motif chemokine 11)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Alzheimer's disease | 0.22 | 0.0687 | 0.00137 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: psoriasis | 0.2 | 0.0804 | 0.0129 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: high cholesterol | -0.0724 | 0.0301 | 0.0161 | Wald ratio | 1 | cis | NA |
| Inflammatory bowel disease | 0.0983 | 0.0448 | 0.0281 | Wald ratio | 1 | cis | NA |
| Happiness | 0.0274 | 0.0128 | 0.0324 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertension | 0.0362 | 0.017 | 0.0333 | Wald ratio | 1 | cis | NA |
| Eczema | -0.153 | 0.0725 | 0.0353 | Wald ratio | 1 | cis | NA |
| Sleep duration | -0.0168 | 0.00807 | 0.0371 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: depression | 0.0811 | 0.0394 | 0.0395 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: mania or bipolar disorder or manic depression | 0.306 | 0.154 | 0.0464 | Wald ratio | 1 | cis | NA |
| Thalamus volume | -50.6 | 26.3 | 0.0546 | Wald ratio | 1 | cis | NA |
| Ulcerative colitis | 0.107 | 0.0559 | 0.0552 | Wald ratio | 1 | cis | NA |
| _...and 90 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3038_9_2` | I-TAC | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_6 association rows across 4 traits (5 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| CXCL11 protein levels | 3e-67 | rs190426994 | 2 | GCST90468924 | no MR -> candidate analysis |
| C-X-C motif chemokine 11 levels | 5e-32 | rs115354596 | 2 | GCST90247202 | no MR -> candidate analysis |
| C-X-C motif chemokine 11 level in Chronic kidney disease wit | 2e-22 | rs12509255 | 1 | GCST90237209 | no MR -> candidate analysis |
| N-acylethanolamine-hydrolyzing acid amidase levels | 1e-7 | rs56961181 | 1 | GCST90248592 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.01, LOEUF=1.36 — LoF-tolerant |
| GWAS Catalog | 101 unique SNPs / 211 rows |
| ClinVar | 51 records; 7 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 655 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'CXCL11'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 51 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 4 of 4 traits by best p-value, aggregated from 6 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O14625 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000169248/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CXCL11 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CXCL11 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CXCL11%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CXCL11 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:13:44  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
