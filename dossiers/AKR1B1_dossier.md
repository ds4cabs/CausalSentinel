# Protein Dossier — AKR1B1 (Aldo-keto reductase family 1 member B1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Birth weight | -0.055 | 0.0216 | 0.011 | Wald ratio | 1 | cis | NA |
| Cough on most days | 0.144 | 0.0576 | 0.0125 | Wald ratio | 1 | cis | NA |
| Sodium in urine | 0.0297 | 0.0126 | 0.0188 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Other bones | 0.105 | 0.0504 | 0.0379 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: muscle or soft tissue injuries | -0.604 | 0.31 | 0.0514 | Wald ratio | 1 | cis | NA |
| Hearing difficulty or problems: Yes | 0.0411 | 0.0212 | 0.0525 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: depression | 0.0926 | 0.0483 | 0.0553 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: psoriasis | 0.191 | 0.101 | 0.0584 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: small intestine or small bowel cancer | 0.671 | 0.358 | 0.0609 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K43 Ventral hernia | 0.273 | 0.15 | 0.0691 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: uterine fibroids | 0.161 | 0.089 | 0.0699 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: migraine | 0.12 | 0.0661 | 0.0703 | Wald ratio | 1 | cis | NA |
| _...and 48 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_25 association rows across 17 traits (23 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| AKR1B1 protein levels | 2e-105 | rs2229542 | 2 | GCST90468273 | no MR -> candidate analysis |
| Serum levels of protein AKR1B1 | 5e-72 | rs2229542 | 1 | GCST90090865 | no MR -> candidate analysis |
| Aldose reductase (analyte X9854.36) levels | 1e-48 | rs2229542 | 1 | GCST90427957 | no MR -> candidate analysis |
| Aldose reductase levels | 6e-29 | rs796703 | 1 | GCST90246483 | no MR -> candidate analysis |
| Height | 6e-21 | rs10263438 | 1 | GCST90245848 | no MR -> candidate analysis |
| Aldose reductase levels (AKR1B1.9854.36.3) | 5e-15 | rs2229542 | 1 | GCST90240227 | no MR -> candidate analysis |
| Systolic blood pressure | 1e-13 | rs782520 | 4 | GCST90662908 | MR: beta=0.0177, p=0.177 (cis) |
| Diastolic blood pressure | 1e-13 | rs782513 | 3 | GCST90292474 | no MR -> candidate analysis |
| Medication use (calcium channel blockers) | 7e-13 | rs782507 | 1 | GCST90018987 | no MR -> candidate analysis |
| Protein quantitative trait loci (liver) | 7e-12 | rs2229542 | 2 | GCST011427 | no MR -> candidate analysis |
| Hypertension | 1e-11 | rs782513 | 2 | GCST90292475 | MR: beta=0.031, p=0.144 (cis) |
| Systolic blood pressure (MTAG) | 4e-11 | rs1790998 | 1 | GCST90449056 | no MR -> candidate analysis |
| _...and 5 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 737 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| hypertensive disorder | 0.248 | — | common-variant locus | no MR -> candidate analysis |
| essential hypertension | 0.229 | — | common-variant locus | no MR -> candidate analysis |
| alopecia areata | 0.134 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 4 known modulators (Aldo-keto reductase family 1 member B1) |
| gnomAD constraint | pLI=0.00056, LOEUF=0.778 — LoF-tolerant |
| GWAS Catalog | 30 unique SNPs / 60 rows |
| ClinVar | 73 records; 3 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 737 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'AKR1B1' and resolved to 'Aldo-keto reductase family 1 member B1' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 73 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 17 of 17 traits by best p-value, aggregated from 25 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P15121 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000085662/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL1900/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/AKR1B1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/AKR1B1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=AKR1B1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/AKR1B1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T00:59:58  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
