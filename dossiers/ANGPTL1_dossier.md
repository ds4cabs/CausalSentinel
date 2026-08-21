# Protein Dossier — ANGPTL1 (Angiopoietin-related protein 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| HDL cholesterol | 0.0409 | 0.0116 | 4.32e-04 | Wald ratio | 1 | cis | NA |
| Myocardial infarction | -0.0847 | 0.0244 | 5.30e-04 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: asthma | 0.048 | 0.0157 | 0.00217 | Wald ratio | 1 | cis | NA |
| Height | -0.0209 | 0.00697 | 0.0027 | Wald ratio | 1 | cis | NA |
| Coronary heart disease | -0.0652 | 0.0221 | 0.00321 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | 0.0129 | 0.00481 | 0.00714 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: C50 Malignant neoplasm of breast | 0.109 | 0.0411 | 0.00781 | Wald ratio | 1 | cis | NA |
| Vascular or heart problems diagnosed by doctor: Angina | -0.0875 | 0.0359 | 0.0149 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: S76 Injury of muscle and tendon at hip and thigh level | 0.45 | 0.185 | 0.0151 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: high cholesterol | -0.0393 | 0.0165 | 0.0171 | Wald ratio | 1 | cis | NA |
| High grade serous ovarian cancer | 0.0877 | 0.0381 | 0.0215 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: migraine | 0.0722 | 0.0315 | 0.0221 | Wald ratio | 1 | cis | NA |
| _...and 105 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_3 association rows across 3 traits (3 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Angiopoietin-related protein 1 levels | 2e-100 | rs148080321 | 1 | GCST90246507 | no MR -> candidate analysis |
| Brain shape (segment 40) | 4e-16 | rs28372846 | 1 | GCST90012919 | no MR -> candidate analysis |
| FEV1 | 5e-11 | rs3753535 | 1 | GCST90270081 | MR: beta=0.00954, p=0.0601 (cis) |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 488 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| gastritis | 0.47 | — | common-variant locus | no MR -> candidate analysis |
| gestational diabetes | 0.427 | — | common-variant locus | no MR -> candidate analysis |
| Hallux valgus | 0.425 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=4.2e-10, LOEUF=1.02 — LoF-tolerant |
| GWAS Catalog | 37 unique SNPs / 74 rows |
| ClinVar | 120 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 488 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'ANGPTL1'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 120 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 3 of 3 traits by best p-value, aggregated from 3 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O95841 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000116194/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/ANGPTL1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/ANGPTL1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=ANGPTL1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/ANGPTL1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:03:45  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
