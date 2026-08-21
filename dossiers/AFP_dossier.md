# Protein Dossier — AFP (Alpha-fetoprotein)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: B37 Candidiasis | 1.07 | 0.272 | 8.11e-05 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K44 Diaphragmatic hernia | 0.28 | 0.0933 | 0.00272 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | 0.0583 | 0.0197 | 0.00316 | Wald ratio | 1 | cis | NA |
| Systemic lupus erythematosus | 0.896 | 0.304 | 0.00322 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: vaginal prolapse or uterine prolapse | 0.401 | 0.142 | 0.00468 | Wald ratio | 1 | cis | NA |
| Transferrin | -0.181 | 0.0658 | 0.00585 | Wald ratio | 1 | cis | NA |
| LDL cholesterol | 0.0834 | 0.0337 | 0.0133 | Wald ratio | 1 | cis | NA |
| Bulimia nervosa | -0.118 | 0.0535 | 0.0278 | Wald ratio | 1 | cis | NA |
| Endometrioid ovarian cancer | 0.393 | 0.182 | 0.0306 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N92 Excessive  frequent and irregular menstruation | 0.181 | 0.0894 | 0.0426 | Wald ratio | 1 | cis | NA |
| Hearing difficulty or problems: Yes | 0.0501 | 0.025 | 0.0454 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: pneumothorax | 0.778 | 0.415 | 0.0607 | Wald ratio | 1 | cis | NA |
| _...and 102 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_23 association rows across 14 traits (22 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| AFP levels | 1e-237 | rs10031441 | 1 | GCST90239635 | no MR -> candidate analysis |
| AFP protein levels | 6e-233 | rs16849384 | 2 | GCST90468250 | no MR -> candidate analysis |
| alpha-Fetoprotein levels | 7e-198 | rs16849384 | 3 | GCST90278615 | no MR -> candidate analysis |
| CXCL1 protein levels | 9e-52 | rs13131508 | 2 | GCST90468930 | no MR -> candidate analysis |
| Afamin levels | 8e-48 | rs66841185 | 2 | GCST90137699 | no MR -> candidate analysis |
| Albumin levels | 7e-35 | rs72647032 | 4 | GCST90501097 | no MR -> candidate analysis |
| N(4)-(beta-N-acetylglucosaminyl)-L-asparaginase levels | 3e-29 | rs72647033 | 1 | GCST90248566 | no MR -> candidate analysis |
| Height | 1e-23 | rs10020432 | 2 | GCST90245848 | MR: beta=0.0187, p=0.331 (cis) |
| Serum levels of protein AFM | 4e-20 | rs72853185 | 1 | GCST90088767 | no MR -> candidate analysis |
| Tumor biomarkers | 3e-18 | rs12506899 | 1 | GCST001808 | no MR -> candidate analysis |
| Insulin-like growth factor-binding protein 7 levels | 1e-15 | rs1289184022 | 1 | GCST90179322 | no MR -> candidate analysis |
| CXCL6 protein levels | 4e-12 | rs188410248 | 1 | GCST90468933 | no MR -> candidate analysis |
| _...and 2 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1575 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Congenital deficiency in alpha-fetoprotein | 0.67 | — | established (curated) | no MR -> candidate analysis |
| Hereditary persistence of alpha-fetoprotein | 0.572 | — | established (curated) | no MR -> candidate analysis |
| primary ovarian failure | 0.438 | — | established (curated) | no MR -> candidate analysis |
| escherichia coli infection | 0.401 | — | common-variant locus | no MR -> candidate analysis |

> Of the 4 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 1 known modulators (Alpha-fetoprotein) |
| gnomAD constraint | pLI=4.8e-18, LOEUF=0.998 — LoF-tolerant |
| GWAS Catalog | 53 unique SNPs / 105 rows |
| ClinVar | 132 records; 3 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1575 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'AFP' and resolved to 'Alpha-fetoprotein' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 132 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 14 of 14 traits by best p-value, aggregated from 23 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P02771 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000081051/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3712864/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/AFP — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/AFP — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=AFP%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/AFP — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T00:57:28  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
