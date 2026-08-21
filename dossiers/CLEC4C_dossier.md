# Protein Dossier — CLEC4C (C-type lectin domain family 4 member C)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Thalamus volume | 20.3 | 6.73 | 0.00254 | Wald ratio | 1 | cis | NA |
| Squamous cell lung cancer | -0.0772 | 0.0279 | 0.00567 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: Z09 Follow-up examination after treatment for conditions other than malignant neoplasms | -0.0538 | 0.0221 | 0.0149 | Wald ratio | 1 | cis | NA |
| Creatinine (enzymatic) in urine | -0.00593 | 0.00246 | 0.0161 | Wald ratio | 1 | cis | NA |
| Pallidum volume | 4.47 | 2.06 | 0.03 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | 0.0593 | 0.0289 | 0.0403 | Wald ratio | 1 | cis | NA |
| Potassium in urine | -0.00526 | 0.00261 | 0.044 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Wrist | 0.0352 | 0.0177 | 0.0469 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K43 Ventral hernia | -0.0753 | 0.0417 | 0.0711 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M54 Dorsalgia | 0.0341 | 0.0193 | 0.0775 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: uterine fibroids | -0.0376 | 0.0216 | 0.0819 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: basal cell carcinoma | -0.0482 | 0.0282 | 0.0875 | Wald ratio | 1 | cis | NA |
| _...and 57 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_29 association rows across 8 traits (28 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating CLEC4C levels | 7e-3909 | rs7302014 | 5 | GCST90860180 | no MR -> candidate analysis |
| C-type lectin domain family 4 member C levels | 5e-517 | rs7302014 | 3 | GCST90247053 | no MR -> candidate analysis |
| Blood protein levels | 1e-418 | rs11055602 | 1 | GCST006585 | no MR -> candidate analysis |
| CLEC4C protein levels | 4e-221 | rs78224908 | 15 | GCST90468772 | no MR -> candidate analysis |
| C-type lectin domain family 4 member C level in Chronic kidn | 1e-47 | rs12310416 | 1 | GCST90239199 | no MR -> candidate analysis |
| Interleukin-3 protein levels (SomaScan ID:9094-5) | 2e-14 | rs12310416 | 1 | GCST90439034 | no MR -> candidate analysis |
| RBP5 protein levels | 2e-14 | rs1966414 | 1 | GCST90470439 | no MR -> candidate analysis |
| Core binding factor acute myeloid leukemia | 7e-12 | rs10772679; rs17199006; rs6488610; rs1894823; rs9300243; rs10845821 | 2 | GCST008413 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 176 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| congenital anomaly of cardiovascular system | 0.241 | — | common-variant locus | no MR -> candidate analysis |

> Of the 1 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 1 known modulators (C-type lectin domain family 4 member C) |
| gnomAD constraint | pLI=0.00045, LOEUF=0.92 — LoF-tolerant |
| GWAS Catalog | 71 unique SNPs / 140 rows |
| ClinVar | 89 records; 7 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 176 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'CLEC4C' and resolved to 'C-type lectin domain family 4 member C' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 89 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 8 of 8 traits by best p-value, aggregated from 29 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q8WTT0 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000198178/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2176855/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CLEC4C — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CLEC4C — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CLEC4C%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CLEC4C — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:53:17  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
