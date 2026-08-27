# Protein Dossier — CASP3 (Caspase-3)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Systemic lupus erythematosus | -0.519 | 0.177 | 0.00339 | Wald ratio | 1 | cis | NA |
| Body fat | -0.0523 | 0.0215 | 0.0149 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | -0.0294 | 0.0121 | 0.0149 | Wald ratio | 1 | cis | NA |
| Birth length | -0.091 | 0.0387 | 0.0186 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hyperthyroidism or thyrotoxicosis | 0.209 | 0.089 | 0.0189 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: depression | 0.0827 | 0.0355 | 0.0199 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: gastro-oesophageal reflux (gord)  or  gastric reflux | 0.0913 | 0.0412 | 0.0265 | Wald ratio | 1 | cis | NA |
| Pulse rate | 0.0359 | 0.0166 | 0.0302 | Wald ratio | 1 | cis | NA |
| HbA1C | 0.0281 | 0.0131 | 0.0328 | Wald ratio | 1 | cis | NA |
| High grade serous ovarian cancer | -0.117 | 0.0588 | 0.0465 | Wald ratio | 1 | cis | NA |
| Lumbar spine bone mineral density | -0.0656 | 0.0331 | 0.0477 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: L03 Cellulitis | -0.277 | 0.141 | 0.0491 | Wald ratio | 1 | cis | NA |
| _...and 88 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3593_72_3` | Caspase-3 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_6 association rows across 5 traits (5 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| CASP3/SERPINB9 protein level ratio | 7e-113 | rs113420705 | 1 | GCST90313642 | no MR -> candidate analysis |
| CASP3 protein levels | 5e-73 | rs62339863 | 1 | GCST90468545 | no MR -> candidate analysis |
| Caspase-3 levels | 3e-40 | rs4647601 | 1 | GCST90246840 | no MR -> candidate analysis |
| Kawasaki disease | 1e-10 | rs2720378 | 2 | GCST90013537 | no MR -> candidate analysis |
| IL18R1 levels | 5e-6 | rs3087455 | 1 | GCST90503374 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 3936 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Kawasaki disease | 0.542 | — | established (curated) | no MR -> candidate analysis |
| response to vaccine | 0.616 | — | common-variant locus | no MR -> candidate analysis |
| response to water | 0.492 | — | common-variant locus | no MR -> candidate analysis |
| response to stimulus | 0.351 | — | common-variant locus | no MR -> candidate analysis |

> Of the 4 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Caspase-3) |
| gnomAD constraint | pLI=0.008, LOEUF=0.809 — LoF-tolerant |
| GWAS Catalog | 25 unique SNPs / 50 rows |
| ClinVar | 146 records; 12 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 3936 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'CASP3' and resolved to 'Caspase-3' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 146 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 5 of 5 traits by best p-value, aggregated from 6 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P42574 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000164305/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2334/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CASP3 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CASP3 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CASP3%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CASP3 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:28:12  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
