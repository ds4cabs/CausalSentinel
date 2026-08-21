# Protein Dossier — RNASE1 (Ribonuclease pancreatic)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Underlying (primary) cause of death: ICD10: E85.4 Organ-limited amyloidosis | 1.79 | 0.597 | 0.00266 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: B37 Candidiasis | 0.755 | 0.281 | 0.00726 | Wald ratio | 1 | cis | NA |
| Caudate volume | 66.4 | 26.4 | 0.0119 | Wald ratio | 1 | cis | NA |
| Putamen volume | 79.7 | 32.2 | 0.0134 | Wald ratio | 1 | cis | NA |
| Neo-neuroticism | 1.23 | 0.539 | 0.0221 | Wald ratio | 1 | cis | NA |
| Rheumatoid arthritis | -0.177 | 0.0804 | 0.0275 | Wald ratio | 1 | cis | NA |
| Fasting glucose | 0.0391 | 0.0178 | 0.0282 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: J33 Nasal polyp | 0.272 | 0.129 | 0.0348 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: G47 Sleep disorders | 0.249 | 0.118 | 0.035 | Wald ratio | 1 | cis | NA |
| Height | -0.0317 | 0.0169 | 0.0612 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Arm | 0.178 | 0.0974 | 0.0679 | Wald ratio | 1 | cis | NA |
| Small vessel disease | 0.349 | 0.195 | 0.0737 | Wald ratio | 1 | cis | NA |
| _...and 82 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_35 association rows across 26 traits (29 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| AZU1/RNASE3 protein level ratio | 1e-422 | rs112539509 | 1 | GCST90313428 | no MR -> candidate analysis |
| Circulating RNASE3 levels | 2e-409 | rs1763559 | 1 | GCST90860416 | no MR -> candidate analysis |
| RNASE1 protein levels | 2e-208 | rs12885981 | 3 | GCST90470476 | no MR -> candidate analysis |
| Monocyte side fluorescence | 1e-59 | rs6571511 | 1 | GCST90281241 | no MR -> candidate analysis |
| Ribonuclease pancreatic levels | 8e-53 | rs17254387 | 2 | GCST90249353 | no MR -> candidate analysis |
| Serum levels of protein RNASE1 | 2e-35 | rs17254387 | 2 | GCST90089740 | no MR -> candidate analysis |
| Circulating CTRC levels | 8e-29 | rs35775091 | 1 | GCST90859776 | no MR -> candidate analysis |
| RNASE6 protein levels | 6e-27 | rs111513387 | 4 | GCST90470479 | no MR -> candidate analysis |
| Blood protein levels | 3e-25 | rs12885981 | 1 | GCST006585 | no MR -> candidate analysis |
| CTRC protein levels | 4e-22 | rs35775091 | 1 | GCST90468906 | no MR -> candidate analysis |
| Monocyte side fluorescence distribution width | 5e-19 | rs11845683 | 1 | GCST90281244 | no MR -> candidate analysis |
| Ebbinghaus illusion (overestimation) | 8e-19 | rs12878080 | 1 | GCST011568 | no MR -> candidate analysis |
| _...and 14 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 288 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| pregnancy disorder | 0.163 | — | common-variant locus | no MR -> candidate analysis |
| placental abruption | 0.124 | — | common-variant locus | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Ribonuclease pancreatic) |
| gnomAD constraint | pLI=NA, LOEUF=NA — Constraint metrics missing; LoF tolerance cannot be judged. |
| GWAS Catalog | 65 unique SNPs / 130 rows |
| ClinVar | 50 records; 9 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 288 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'RNASE1' and resolved to 'Ribonuclease pancreatic' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 50 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 26 traits by best p-value, aggregated from 35 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P07998 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000129538/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL5425/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/RNASE1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/RNASE1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=RNASE1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/RNASE1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:50:02  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
