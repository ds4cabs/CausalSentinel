# Protein Dossier — SIGLEC6 (Sialic acid-binding Ig-like lectin 6)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Rheumatoid arthritis | 0.0747 | 0.0187 | 6.43e-05 | Wald ratio | 1 | cis | NA |
| HbA1C | 0.0161 | 0.00521 | 0.00201 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: bone disorder | 0.188 | 0.0666 | 0.00484 | Wald ratio | 1 | cis | NA |
| ER-negative Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | 0.0473 | 0.0176 | 0.00721 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: depression | -0.0354 | 0.016 | 0.0271 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M54 Dorsalgia | 0.059 | 0.0274 | 0.0316 | Wald ratio | 1 | cis | NA |
| Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | 0.0205 | 0.00965 | 0.0334 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: pneumothorax | 0.276 | 0.143 | 0.0526 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: S66 Injury of muscle and tendon at wrist and hand level | 0.155 | 0.081 | 0.0563 | Wald ratio | 1 | cis | NA |
| Fasting proinsulin | -0.0199 | 0.0109 | 0.0671 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: uterine fibroids | -0.0574 | 0.0321 | 0.0735 | Wald ratio | 1 | cis | NA |
| Red blood cell count | 0.00597 | 0.00337 | 0.0763 | Wald ratio | 1 | cis | NA |
| _...and 98 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2741_22_2` | Siglec-6 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_55 association rows across 20 traits (50 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating SIGLEC6 levels | 3e-880 | rs62617068 | 9 | GCST90860512 | no MR -> candidate analysis |
| Sialic acid-binding Ig-like lectin 6 levels | 8e-533 | rs4146202 | 11 | GCST90249550 | no MR -> candidate analysis |
| SIGLEC6 protein levels | 8e-252 | rs180865472 | 7 | GCST90470634 | no MR -> candidate analysis |
| Serum levels of protein SIGLEC6 | 1e-210 | rs12460678 | 2 | GCST90088041 | no MR -> candidate analysis |
| Sialic acid-binding Ig-like lectin 5 levels | 6e-150 | rs140056884 | 2 | GCST90249549 | no MR -> candidate analysis |
| Cerebrospinal fluid protein SIGLEC6 levels | 6e-119 | rs79864857 | 1 | GCST90943899 | no MR -> candidate analysis |
| Blood protein levels | 1e-114 | rs2305771 | 2 | GCST006585 | no MR -> candidate analysis |
| SIGLEC5 protein levels | 6e-77 | rs736574 | 5 | GCST90470633 | no MR -> candidate analysis |
| Serum levels of protein SIGLEC14 | 2e-46 | rs140056884 | 1 | GCST90088943 | no MR -> candidate analysis |
| SIGLEC8 protein levels | 7e-28 | rs10401247 | 4 | GCST90470636 | no MR -> candidate analysis |
| Protein quantitative trait loci | 4e-22 | rs10221508 | 1 | GCST010900 | no MR -> candidate analysis |
| Sialic acid-binding Ig-like lectin 14 levels | 2e-15 | rs56109198 | 1 | GCST90162313 | no MR -> candidate analysis |
| _...and 8 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 209 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Splenomegaly | 0.213 | — | common-variant locus | no MR -> candidate analysis |

> Of the 1 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1.4e-08, LOEUF=1.01 — LoF-tolerant |
| GWAS Catalog | 107 unique SNPs / 252 rows |
| ClinVar | 93 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 209 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'SIGLEC6'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 93 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 20 traits by best p-value, aggregated from 55 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O43699 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000105492/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/SIGLEC6 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/SIGLEC6 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=SIGLEC6%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/SIGLEC6 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:05:56  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
