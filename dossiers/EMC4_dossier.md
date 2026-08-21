# Protein Dossier — EMC4 (ER membrane protein complex subunit 4)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Squamous cell lung cancer | -0.143 | 0.0467 | 0.0022 | Wald ratio | 1 | trans | NA |
| 2hr glucose | -0.121 | 0.0455 | 0.00766 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: K40 Inguinal hernia | 0.0589 | 0.0244 | 0.0157 | Wald ratio | 1 | trans | NA |
| Fractured bone site(s): Ankle | -0.0929 | 0.0397 | 0.0192 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: retinal detachment | 0.146 | 0.0639 | 0.0226 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: S76 Injury of muscle and tendon at hip and thigh level | 0.329 | 0.148 | 0.0264 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: I80 Phlebitis and thrombophlebitis | -0.155 | 0.0727 | 0.0331 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: bone disorder | 0.16 | 0.0774 | 0.0391 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: C61 Malignant neoplasm of prostate | 0.0954 | 0.0473 | 0.0435 | Wald ratio | 1 | trans | NA |
| Fractured or broken bones in last 5 years | -0.0268 | 0.0135 | 0.0477 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: G56 Mononeuropathies of upper limb | 0.0574 | 0.0304 | 0.0587 | Wald ratio | 1 | trans | NA |
| HDL cholesterol | 0.0185 | 0.00986 | 0.0605 | Wald ratio | 1 | trans | NA |
| _...and 91 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_1 association rows across 1 traits (1 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Hematological traits (multi-trait analysis) | 5e-9 | rs57626952 | 1 | GCST90838669 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 35 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| agenesis of the corpus callosum with peripheral neuropathy | 0.265 | — | established (curated) | no MR -> candidate analysis |

> Of the 1 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.59, LOEUF=0.65 — LoF-tolerant |
| GWAS Catalog | 10 unique SNPs / 20 rows |
| ClinVar | 54 records; 6 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 35 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'EMC4'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 54 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 1 of 1 traits by best p-value, aggregated from 1 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q5J8M3 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000128463/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/EMC4 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/EMC4 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=EMC4%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/EMC4 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:25:00  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
