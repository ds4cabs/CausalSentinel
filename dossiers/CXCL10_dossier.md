# Protein Dossier — CXCL10 (C-X-C motif chemokine 10)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Alzheimer's disease | -0.345 | 0.117 | 0.00306 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: psoriasis | 0.335 | 0.124 | 0.0068 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: high cholesterol | -0.146 | 0.0568 | 0.01 | Wald ratio | 1 | cis | NA |
| Eczema | 0.29 | 0.127 | 0.023 | Wald ratio | 1 | cis | NA |
| Inflammatory bowel disease | -0.172 | 0.0784 | 0.0281 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: mania or bipolar disorder or manic depression | 0.496 | 0.23 | 0.0309 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertension | 0.0597 | 0.029 | 0.0399 | Wald ratio | 1 | cis | NA |
| Schizophrenia | -0.165 | 0.0812 | 0.0417 | Wald ratio | 1 | cis | NA |
| Ulcerative colitis | -0.188 | 0.0979 | 0.0552 | Wald ratio | 1 | cis | NA |
| Happiness | -0.0423 | 0.0224 | 0.0587 | Wald ratio | 1 | cis | NA |
| Autism | 0.403 | 0.214 | 0.0594 | Wald ratio | 1 | cis | NA |
| Sleep duration | 0.0262 | 0.0141 | 0.0634 | Wald ratio | 1 | cis | NA |
| _...and 91 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-4141_79_1` | IP-10 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_7 association rows across 5 traits (7 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| C-X-C motif chemokine 10 levels | 6e-271 | rs11548618 | 3 | GCST90274780 | no MR -> candidate analysis |
| C-X-C motif chemokine 10 levels (CXCL10.4141.79.1) | 2e-49 | rs11548618 | 1 | GCST90240520 | no MR -> candidate analysis |
| CXCL10 levels | 2e-37 | rs11548618 | 1 | GCST90274886 | no MR -> candidate analysis |
| CXCL10 protein levels | 2e-17 | rs11548618 | 1 | GCST90277748 | no MR -> candidate analysis |
| Neonatal cytokine/chemokine levels (fetal genetic effect) | 2e-14 | rs3921 | 1 | GCST006622 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 2 known modulators (C-X-C motif chemokine 10) |
| gnomAD constraint | pLI=0.063, LOEUF=1.09 — LoF-tolerant |
| GWAS Catalog | 105 unique SNPs / 228 rows |
| ClinVar | 53 records; 7 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 1 clinical annotations across 2 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1518 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'CXCL10' and resolved to 'C-X-C motif chemokine 10' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 53 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 5 of 5 traits by best p-value, aggregated from 7 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P02778 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000169245/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3712964/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CXCL10 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CXCL10 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CXCL10%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=CXCL10 — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CXCL10 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:13:30  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
