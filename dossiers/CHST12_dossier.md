# Protein Dossier — CHST12 (Carbohydrate sulfotransferase 12)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: I30 Acute pericarditis | 1.19 | 0.309 | 1.23e-04 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I80 Phlebitis and thrombophlebitis | 0.521 | 0.142 | 2.35e-04 | Wald ratio | 1 | cis | NA |
| Schizophrenia | 0.2 | 0.0706 | 0.00472 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R14 Flatulence and related conditions | 0.852 | 0.317 | 0.00721 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertension | -0.0711 | 0.0292 | 0.0148 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M17 Gonarthrosis [arthrosis of knee] | -0.437 | 0.185 | 0.0182 | Wald ratio | 1 | cis | NA |
| Cough on most days | -0.206 | 0.101 | 0.0408 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: S76 Injury of muscle and tendon at hip and thigh level | 0.808 | 0.404 | 0.0455 | Wald ratio | 1 | cis | NA |
| Creatinine (enzymatic) in urine | -0.028 | 0.0152 | 0.0658 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Diabetes related eye disease | 0.286 | 0.158 | 0.0705 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R11 Nausea and vomiting | 0.33 | 0.19 | 0.0824 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | -0.0275 | 0.0159 | 0.084 | Wald ratio | 1 | cis | NA |
| _...and 60 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_35 association rows across 28 traits (27 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Diastolic blood pressure | 2e-26 | rs2969070 | 4 | GCST90310295 | no MR -> candidate analysis |
| Circulating PAPPA levels | 3e-21 | rs7808353 | 1 | GCST90859782 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 4e-20 | rs10259587 | 1 | GCST90838669 | no MR -> candidate analysis |
| Systolic blood pressure | 2e-19 | rs2969070 | 3 | GCST90310294 | no MR -> candidate analysis |
| Carbohydrate sulfotransferase 12 levels | 1e-16 | rs3735099 | 1 | GCST90426800 | no MR -> candidate analysis |
| Sorting nexin-8 levels | 2e-13 | rs151089696 | 1 | GCST90249602 | no MR -> candidate analysis |
| Serum levels of protein CHST12 | 1e-12 | rs10215904 | 1 | GCST90089536 | no MR -> candidate analysis |
| Hemoglobin levels | 3e-12 | rs886627 | 1 | GCST90662903 | no MR -> candidate analysis |
| Reticulocyte count | 1e-11 | rs35697782 | 1 | GCST90002405 | no MR -> candidate analysis |
| Pappalysin-1 levels | 2e-11 | rs7808353 | 1 | GCST90012036 | no MR -> candidate analysis |
| Alzheimer's disease or family history of Alzheimer's disease | 2e-11 | rs939252020 | 2 | GCST90624094 | no MR -> candidate analysis |
| Blood protein levels | 7e-11 | rs2969076 | 1 | GCST006585 | no MR -> candidate analysis |
| _...and 16 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 454 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| stroke disorder | 0.432 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.432 | — | common-variant locus | no MR -> candidate analysis |
| head and neck cancer | 0.223 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=2.7e-07, LOEUF=1.17 — LoF-tolerant |
| GWAS Catalog | 79 unique SNPs / 158 rows |
| ClinVar | 145 records; 3 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 454 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'CHST12'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 145 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 28 traits by best p-value, aggregated from 35 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9NRB3 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000136213/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CHST12 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CHST12 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CHST12%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CHST12 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:51:32  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
