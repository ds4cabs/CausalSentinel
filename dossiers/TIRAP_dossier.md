# Protein Dossier — TIRAP (Toll/interleukin-1 receptor domain-containing adapter protein)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: N92 Excessive  frequent and irregular menstruation | 0.317 | 0.0726 | 1.28e-05 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: osteoporosis | 0.267 | 0.0882 | 0.0025 | Wald ratio | 1 | cis | NA |
| Femoral neck bone mineral density | 0.12 | 0.0461 | 0.00904 | Wald ratio | 1 | cis | NA |
| Coronary heart disease | -0.156 | 0.0617 | 0.0117 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: high cholesterol | -0.0971 | 0.0425 | 0.0222 | Wald ratio | 1 | cis | NA |
| Cough on most days | 0.139 | 0.0645 | 0.0317 | Wald ratio | 1 | cis | NA |
| Birth weight | -0.0457 | 0.0219 | 0.0368 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I80 Phlebitis and thrombophlebitis | 0.322 | 0.155 | 0.0385 | Wald ratio | 1 | cis | NA |
| Platelet count | -5.06 | 2.51 | 0.0436 | Wald ratio | 1 | cis | NA |
| Hippocampus volume | 55.8 | 28 | 0.0465 | Wald ratio | 1 | cis | NA |
| Mean platelet volume | 0.0128 | 0.00648 | 0.0485 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: muscle or soft tissue injuries | 0.257 | 0.133 | 0.0532 | Wald ratio | 1 | cis | NA |
| _...and 76 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_32 association rows across 26 traits (32 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Height | 1e-99 | rs8177388 | 2 | GCST90245848 | MR: beta=-0.021, p=0.275 (cis) |
| CD300C/MANSC1 protein level ratio | 2e-83 | rs8177376 | 1 | GCST90313791 | no MR -> candidate analysis |
| MANSC1/PODXL protein level ratio | 1e-68 | rs8177376 | 1 | GCST90315372 | no MR -> candidate analysis |
| Toll/interleukin-1 receptor domain-containing adapter protei | 5e-60 | rs8177399 | 1 | GCST90249882 | no MR -> candidate analysis |
| Serum alkaline phosphatase levels | 7e-35 | rs8177376 | 2 | GCST90019494 | no MR -> candidate analysis |
| CEACAM8/VNN2 protein level ratio | 4e-28 | rs8177376 | 1 | GCST90314005 | no MR -> candidate analysis |
| neutrophil (fraction, mean, inv-norm transformed) | 8e-26 | rs8177391 | 1 | GCST90475538 | no MR -> candidate analysis |
| NPTX1 protein levels | 2e-25 | rs8177352 | 1 | GCST90470078 | no MR -> candidate analysis |
| Serum levels of protein TIRAP | 2e-23 | rs8177399 | 1 | GCST90090851 | no MR -> candidate analysis |
| Apolipoprotein B levels | 5e-22 | rs8177399 | 2 | GCST90019496 | no MR -> candidate analysis |
| Low density lipoprotein cholesterol levels | 7e-22 | rs8177399 | 1 | GCST90019512 | no MR -> candidate analysis |
| eosinophil (fraction, mean, inv-norm transformed) | 7e-22 | rs4935964 | 2 | GCST90475300 | no MR -> candidate analysis |
| _...and 14 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 203 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| response to statin | 0.093 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.055 | — | common-variant locus | no MR -> candidate analysis |
| urolithiasis | 0.047 | — | common-variant locus | no MR -> candidate analysis |
| lymphatic system disorder | 0.041 | — | common-variant locus | no MR -> candidate analysis |
| androgenetic alopecia | 0.038 | — | common-variant locus | no MR -> candidate analysis |
| risk-taking behaviour | 0.038 | — | common-variant locus | no MR -> candidate analysis |
| stroke disorder | 0.031 | — | common-variant locus | no MR -> candidate analysis |

> Of the 7 rows above, **7 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1.2e-07, LOEUF=1.47 — LoF-tolerant |
| GWAS Catalog | 131 unique SNPs / 327 rows |
| ClinVar | 110 records; 8 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 1 clinical annotations across 1 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 203 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'TIRAP'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 110 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 20 of 26 traits by best p-value, aggregated from 32 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P58753 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000150455/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/TIRAP — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/TIRAP — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=TIRAP%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=TIRAP — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/TIRAP — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:22:24  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
