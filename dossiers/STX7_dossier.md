# Protein Dossier — STX7 (Syntaxin-7)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Serum creatinine (eGFRcrea) | -0.0126 | 0.00271 | 3.44e-06 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: K60 Fissure and fistula of anal and rectal regions | 0.31 | 0.0809 | 1.30e-04 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: Z09 Follow-up examination after treatment for conditions other than malignant neoplasms | 0.134 | 0.0528 | 0.0112 | Wald ratio | 1 | trans | NA |
| Type 2 diabetes | -0.0945 | 0.0377 | 0.0121 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code self-reported: pulmonary embolism (with or without) dvt | -0.272 | 0.109 | 0.0127 | Wald ratio | 1 | trans | NA |
| Fracture resulting from simple fall | -0.0482 | 0.0206 | 0.0195 | Wald ratio | 1 | trans | NA |
| Fractured or broken bones in last 5 years | -0.0511 | 0.0243 | 0.0354 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | 0.153 | 0.0761 | 0.0446 | Wald ratio | 1 | trans | NA |
| Eye problems or disorders: Glaucoma | 0.109 | 0.0557 | 0.0497 | Wald ratio | 1 | trans | NA |
| Caudate volume | 28.8 | 14.8 | 0.0515 | Wald ratio | 1 | trans | NA |
| Neo-openness to experience | -0.386 | 0.202 | 0.0559 | Wald ratio | 1 | trans | NA |
| Haemoglobin concentration | -0.036 | 0.0192 | 0.0603 | Wald ratio | 1 | trans | NA |
| _...and 100 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_71 association rows across 39 traits (67 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| STX7 protein levels | 5e-208 | rs62424931 | 11 | GCST90470775 | no MR -> candidate analysis |
| VNN1 protein levels | 2e-79 | rs6908213 | 4 | GCST90471043 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 2e-40 | rs3813356 | 2 | GCST90838669 | no MR -> candidate analysis |
| Syntaxin-7 levels | 8e-36 | rs12190479 | 1 | GCST90249723 | no MR -> candidate analysis |
| High light scatter reticulocyte count | 5e-30 | rs3813356 | 2 | GCST90002385 | no MR -> candidate analysis |
| mean corpuscular hemoglobin concentration (MCHC, mean, inv-n | 6e-30 | rs3813356 | 2 | GCST90475458 | no MR -> candidate analysis |
| High light scatter reticulocyte percentage of red cells | 5e-29 | rs3813356 | 2 | GCST90002386 | no MR -> candidate analysis |
| Reticulocyte count | 1e-28 | rs3813356 | 2 | GCST90002405 | no MR -> candidate analysis |
| Reticulocyte fraction of red cells | 5e-27 | rs3813356 | 2 | GCST90002406 | no MR -> candidate analysis |
| Red cell distribution width | 6e-26 | rs3813356 | 6 | GCST90002369 | no MR -> candidate analysis |
| High light scatter reticulocyte percentage (UKB data field 3 | 1e-24 | rs3813356 | 1 | GCST90468077 | no MR -> candidate analysis |
| Reticulocyte count (UKB data field 30250) | 1e-24 | rs3813356 | 1 | GCST90468100 | no MR -> candidate analysis |
| _...and 27 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 68 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Abnormality of neuronal migration | 0.426 | — | established (curated) | no MR -> candidate analysis |
| Raynaud disease | 0.416 | — | common-variant locus | no MR -> candidate analysis |
| placental abruption | 0.337 | — | common-variant locus | no MR -> candidate analysis |
| atrial fibrillation | 0.046 | — | common-variant locus | no MR -> candidate analysis |
| cardiac arrhythmia | 0.046 | — | common-variant locus | no MR -> candidate analysis |
| aortic stenosis | 0.043 | — | common-variant locus | no MR -> candidate analysis |

> Of the 6 rows above, **6 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1.1e-10, LOEUF=1.14 — LoF-tolerant |
| GWAS Catalog | 75 unique SNPs / 150 rows |
| ClinVar | 61 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 68 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'STX7'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 61 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 39 traits by best p-value, aggregated from 71 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O15400 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000079950/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/STX7 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/STX7 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=STX7%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/STX7 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:15:54  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
