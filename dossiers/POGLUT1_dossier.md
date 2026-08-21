# Protein Dossier — POGLUT1 (Protein O-glucosyltransferase 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Happiness | -0.0562 | 0.0154 | 2.60e-04 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: S76 Injury of muscle and tendon at hip and thigh level | 0.911 | 0.256 | 3.70e-04 | Wald ratio | 1 | cis | NA |
| HbA1C | 0.0564 | 0.0173 | 0.0011 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: S66 Injury of muscle and tendon at wrist and hand level | 0.546 | 0.188 | 0.00361 | Wald ratio | 1 | cis | NA |
| Diastolic blood pressure  automated reading | -0.0365 | 0.0127 | 0.00411 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: C50 Malignant neoplasm of breast | 0.214 | 0.0788 | 0.00656 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | -0.176 | 0.0661 | 0.00761 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: pneumothorax | 0.785 | 0.31 | 0.0113 | Wald ratio | 1 | cis | NA |
| Fasting glucose | 0.0381 | 0.0155 | 0.0139 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | -0.0295 | 0.0124 | 0.0172 | Wald ratio | 1 | cis | NA |
| Large vessel disease | -0.436 | 0.188 | 0.0207 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Wrist | -0.25 | 0.115 | 0.0305 | Wald ratio | 1 | cis | NA |
| _...and 104 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_6 association rows across 5 traits (5 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Serum levels of protein POGLUT1 | 5e-109 | rs6794833 | 1 | GCST90089446 | no MR -> candidate analysis |
| Protein O-glucosyltransferase 1 levels | 8e-104 | rs6794833 | 2 | GCST90426717 | no MR -> candidate analysis |
| Height | 5e-11 | rs3088258 | 1 | GCST007841 | MR: beta=-0.016, p=0.294 (cis) |
| Primary biliary cholangitis | 8e-10 | rs12695386 | 1 | GCST90061441 | no MR -> candidate analysis |
| Total PHF-tau (SNP x SNP interaction) | 6e-8 | rs4688005 x rs11176397 | 1 | GCST010340 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 292 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Dowling-Degos disease | 0.782 | — | established (curated) | no MR -> candidate analysis |
| Autosomal recessive limb-girdle muscular dystrophy due to ISPD deficiency | 0.791 | — | established (curated) | no MR -> candidate analysis |
| hereditary disease | 0.316 | — | established (curated) | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=9e-05, LOEUF=0.701 — LoF-tolerant |
| GWAS Catalog | 62 unique SNPs / 124 rows |
| ClinVar | 362 records; 3 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 292 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'POGLUT1'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 362 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 5 of 5 traits by best p-value, aggregated from 6 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q8NBL1 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000163389/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/POGLUT1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/POGLUT1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=POGLUT1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/POGLUT1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:29:49  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: pharmgkb
