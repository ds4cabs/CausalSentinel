# Protein Dossier — FCRL4 (Fc receptor-like protein 4)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Cardioembolic stroke | 0.119 | 0.0395 | 0.00266 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertension | 0.0135 | 0.00496 | 0.00663 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: mania or bipolar disorder or manic depression | 0.118 | 0.0514 | 0.0212 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: osteoarthritis | 0.02 | 0.00966 | 0.038 | Wald ratio | 1 | cis | NA |
| Vascular or heart problems diagnosed by doctor: Angina | 0.0329 | 0.016 | 0.0396 | Wald ratio | 1 | cis | NA |
| LDL cholesterol | 0.0132 | 0.00644 | 0.0412 | Wald ratio | 1 | cis | NA |
| Height | 0.0068 | 0.00353 | 0.0542 | Wald ratio | 1 | cis | NA |
| Clear cell ovarian cancer | 0.107 | 0.0584 | 0.0661 | Wald ratio | 1 | cis | NA |
| Eczema | 0.0369 | 0.0204 | 0.0706 | Wald ratio | 1 | cis | NA |
| Years of schooling | -0.00794 | 0.00441 | 0.0719 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: C61 Malignant neoplasm of prostate | -0.0695 | 0.0388 | 0.0734 | Wald ratio | 1 | cis | NA |
| Endometrioid ovarian cancer | -0.0716 | 0.0401 | 0.0739 | Wald ratio | 1 | cis | NA |
| _...and 96 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_58 association rows across 23 traits (53 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Fc receptor-like protein 4 levels | 5e-1076 | rs11582663 | 3 | GCST90247567 | no MR -> candidate analysis |
| Circulating FCRL3 levels | 9e-647 | rs6677006 | 1 | GCST90860213 | no MR -> candidate analysis |
| Circulating FCRL2 levels | 2e-621 | rs141931363 | 2 | GCST90859715 | no MR -> candidate analysis |
| Fc receptor-like protein 4 levels (FCRL4.8973.23.3) | 3e-322 | rs11582663 | 3 | GCST90241153 | no MR -> candidate analysis |
| Blood protein levels | 2e-283 | rs11591129 | 2 | GCST006585 | no MR -> candidate analysis |
| Circulating FCRL5 levels | 8e-262 | rs17723386 | 3 | GCST90860603 | no MR -> candidate analysis |
| FCRL5 protein levels | 4e-258 | rs17723386 | 5 | GCST90469208 | no MR -> candidate analysis |
| FCRL3 protein levels | 1e-101 | rs111344687 | 16 | GCST90469207 | no MR -> candidate analysis |
| Serum levels of protein FCRL4 | 5e-87 | rs12125713 | 1 | GCST90090419 | no MR -> candidate analysis |
| White blood cell count | 2e-70 | rs11264765 | 2 | GCST90026503 | no MR -> candidate analysis |
| Core binding factor acute myeloid leukemia | 3e-33 | rs12145148; rs10489676; rs2785662; rs2785663; rs2785664; rs2778010; rs2785665; rs12743309; rs12123141; rs12070820 | 2 | GCST008413 | no MR -> candidate analysis |
| FCRL1 protein levels | 6e-25 | rs139449126 | 2 | GCST90469205 | no MR -> candidate analysis |
| _...and 11 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 191 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| IgA glomerulonephritis | 0.508 | — | common-variant locus | no MR -> candidate analysis |
| functional neutrophil defect | 0.465 | — | common-variant locus | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=4.9e-10, LOEUF=0.865 — LoF-tolerant |
| GWAS Catalog | 100 unique SNPs / 200 rows |
| ClinVar | 98 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 191 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'FCRL4'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 98 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 23 traits by best p-value, aggregated from 58 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q96PJ5 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000163518/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/FCRL4 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/FCRL4 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=FCRL4%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/FCRL4 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:39:03  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
