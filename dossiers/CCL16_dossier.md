# Protein Dossier — CCL16 (C-C motif chemokine 16)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: hypopituitarism | 0.323 | 0.108 | 0.00286 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R35 Polyuria | -0.119 | 0.0492 | 0.016 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: osteoporosis | 0.0483 | 0.0208 | 0.0205 | Wald ratio | 1 | cis | NA |
| Alcohol intake frequency | -0.00898 | 0.00403 | 0.0257 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code self-reported: pulmonary embolism (with or without) dvt | -0.0723 | 0.0325 | 0.026 | Wald ratio | 1 | cis | NA |
| Thalamus volume | 16.7 | 7.83 | 0.0325 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: uterine fibroids | -0.0478 | 0.0231 | 0.0383 | Wald ratio | 1 | cis | NA |
| Hippocampus volume | 12 | 5.89 | 0.0424 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: G47 Sleep disorders | -0.0778 | 0.0384 | 0.043 | Wald ratio | 1 | cis | NA |
| Endometrioid ovarian cancer | -0.0703 | 0.0354 | 0.047 | Wald ratio | 1 | cis | NA |
| Lumbar spine bone mineral density | -0.0206 | 0.0104 | 0.0478 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: chronic obstructive airways disease or copd | -0.0992 | 0.0517 | 0.0548 | Wald ratio | 1 | cis | NA |
| _...and 67 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-4913_78_1` | HCC-4 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_63 association rows across 36 traits (55 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating CCL16 levels | 9e-5290 | rs112689088 | 3 | GCST90859998 | no MR -> candidate analysis |
| C-C motif chemokine 16 levels | 6e-1527 | rs10445391 | 8 | GCST90246904 | no MR -> candidate analysis |
| C-C motif chemokine 16 levels (CCL16.4913.78.1) | 3e-450 | rs112689088 | 2 | GCST90240485 | no MR -> candidate analysis |
| Cystatin-8 levels | 5e-398 | rs10445391 | 1 | GCST90247215 | no MR -> candidate analysis |
| NKG2-E type II integral membrane protein levels | 7e-380 | rs10445391 | 1 | GCST90248688 | no MR -> candidate analysis |
| Serum levels of protein KLRC3 | 9e-276 | rs112689088 | 1 | GCST90089837 | no MR -> candidate analysis |
| CCL16 protein levels | 2e-259 | rs1635272 | 7 | GCST90468568 | no MR -> candidate analysis |
| Blood protein levels | 9e-198 | rs10445391 | 7 | GCST006585 | no MR -> candidate analysis |
| Serum levels of protein CST8 | 4e-188 | rs112689088 | 1 | GCST90086348 | no MR -> candidate analysis |
| Cystatin-8 levels (CST8.10572.65.3) | 6e-186 | rs112689088 | 1 | GCST90240830 | no MR -> candidate analysis |
| Circulating CCL14 levels | 1e-180 | rs57450479 | 1 | GCST90860489 | no MR -> candidate analysis |
| CCL14 protein levels | 7e-167 | rs71366493 | 2 | GCST90468566 | no MR -> candidate analysis |
| _...and 24 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 138 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Raynaud disease | 0.042 | — | common-variant locus | no MR -> candidate analysis |

> Of the 1 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.011, LOEUF=1.57 — LoF-tolerant |
| GWAS Catalog | 156 unique SNPs / 376 rows |
| ClinVar | 33 records; 5 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 138 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'CCL16'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 33 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 36 traits by best p-value, aggregated from 63 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O15467 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000275152/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CCL16 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CCL16 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CCL16%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CCL16 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:31:35  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
