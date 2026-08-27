# Protein Dossier — SIGLEC12 (Sialic acid-binding Ig-like lectin 12)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: pneumothorax | 0.313 | 0.105 | 0.00294 | Wald ratio | 1 | cis | NA |
| Multiple sclerosis | -0.0862 | 0.0295 | 0.00353 | Wald ratio | 1 | cis | NA |
| Fasting proinsulin | -0.024 | 0.00878 | 0.00639 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I83 Varicose veins of lower extremities | -0.0553 | 0.0214 | 0.00968 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M54 Dorsalgia | 0.05 | 0.0214 | 0.0196 | Wald ratio | 1 | cis | NA |
| Paget's disease | 0.149 | 0.0683 | 0.0297 | Wald ratio | 1 | cis | NA |
| Serum cystatin C (eGFRcys) | -0.00488 | 0.00231 | 0.0344 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Diabetes related eye disease | -0.0821 | 0.0404 | 0.0421 | Wald ratio | 1 | cis | NA |
| Myocardial infarction | 0.0249 | 0.0125 | 0.0465 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: bone disorder | 0.11 | 0.0556 | 0.0484 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: enlarged prostate | 0.0459 | 0.0237 | 0.0523 | Wald ratio | 1 | cis | NA |
| Knee osteoarthritis | -0.0644 | 0.0341 | 0.0593 | Wald ratio | 1 | cis | NA |
| _...and 88 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_17 association rows across 11 traits (16 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Blood protein levels | 1e-371 | rs1973095 | 5 | GCST006585 | no MR -> candidate analysis |
| Sialic acid-binding Ig-like lectin 12 levels (SIGLEC12.8352. | 3e-366 | rs3826667 | 1 | GCST90242807 | no MR -> candidate analysis |
| Sialic acid-binding Ig-like lectin 12:Ig-like V-type 2 domai | 5e-323 | rs3810114 | 1 | GCST90421049 | no MR -> candidate analysis |
| Circulating SIGLEC6 levels | 7e-280 | rs79814518 | 1 | GCST90860512 | no MR -> candidate analysis |
| SIGLEC5 protein levels | 3e-201 | rs2034889 | 1 | GCST90470633 | no MR -> candidate analysis |
| SIGLEC8 protein levels | 5e-117 | rs3810110 | 1 | GCST90470636 | no MR -> candidate analysis |
| Sialic acid-binding Ig-like lectin 12 level in Chronic kidne | 7e-39 | rs4801871 | 1 | GCST90232810 | no MR -> candidate analysis |
| Septin-6 protein levels (SomaScan ID:10037-98) | 4e-33 | rs968491 | 1 | GCST90442431 | no MR -> candidate analysis |
| Sialic acid-binding Ig-like lectin 6 levels | 3e-21 | rs75950899 | 2 | GCST90161451 | no MR -> candidate analysis |
| CD33 protein levels | 5e-18 | rs73051357 | 2 | GCST90468625 | no MR -> candidate analysis |
| Plasma calcium levels | 6e-6 | rs73049701 | 1 | GCST90100541 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 58 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| placental abruption | 0.33 | — | common-variant locus | no MR -> candidate analysis |

> Of the 1 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=3e-12, LOEUF=1.03 — LoF-tolerant |
| GWAS Catalog | 99 unique SNPs / 198 rows |
| ClinVar | 151 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 58 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'SIGLEC12'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 151 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 11 of 11 traits by best p-value, aggregated from 17 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q96PQ1 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000254521/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/SIGLEC12 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/SIGLEC12 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=SIGLEC12%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/SIGLEC12 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:05:23  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
