# Protein Dossier — RPRD1A (Regulation of nuclear pre-mRNA domain-containing protein 1A)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Alcohol intake frequency | -0.0509 | 0.0182 | 0.00527 | Wald ratio | 1 | trans | NA |
| Depressive symptoms | -0.048 | 0.0192 | 0.0124 | Wald ratio | 1 | trans | NA |
| Glioma | 0.556 | 0.224 | 0.013 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: D12 Benign neoplasm of colon  rectum  anus and anal canal | 0.208 | 0.0853 | 0.0147 | Wald ratio | 1 | trans | NA |
| Cardioembolic stroke | 0.384 | 0.162 | 0.0176 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: arthritis (nos) | 0.256 | 0.112 | 0.0215 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: Z09 Follow-up examination after treatment for conditions other than malignant neoplasms | 0.175 | 0.085 | 0.0393 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: hypertension | -0.0452 | 0.022 | 0.0402 | Wald ratio | 1 | trans | NA |
| Heel bone mineral density (BMD) T-score  automated | -0.031 | 0.016 | 0.0521 | Wald ratio | 1 | trans | NA |
| Height | -0.0283 | 0.0149 | 0.057 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: asthma | -0.0678 | 0.037 | 0.067 | Wald ratio | 1 | trans | NA |
| Mean cell volume | -0.238 | 0.13 | 0.0672 | Wald ratio | 1 | trans | NA |
| _...and 91 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_9 association rows across 5 traits (7 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Mean corpuscular hemoglobin | 8e-14 | rs28791905 | 5 | GCST90002326 | no MR -> candidate analysis |
| Mean corpuscular volume | 1e-11 | rs74277390 | 1 | GCST90002392 | no MR -> candidate analysis |
| Free Cholesterol to Cholesteryl Esters in Large HDL ratio | 2e-9 | rs145925439 | 1 | GCST90827800 | no MR -> candidate analysis |
| Tuberculosis | 2e-6 | rs75764086 | 1 | GCST90275070 | no MR -> candidate analysis |
| Tenofovir clearance in HIV infection | 6e-6 | rs17562912 | 1 | GCST006073 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 36 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Nasal polyposis | 0.401 | — | common-variant locus | no MR -> candidate analysis |
| bipolar disorder | 0.054 | — | common-variant locus | MR: beta=0.167, p=0.162 (trans) |
| Loss of consciousness | 0.043 | — | common-variant locus | no MR -> candidate analysis |
| deficiency anemia | 0.043 | — | common-variant locus | no MR -> candidate analysis |
| Phenotypic abnormality | 0.038 | — | common-variant locus | no MR -> candidate analysis |
| hyperaldosteronism | 0.035 | — | common-variant locus | no MR -> candidate analysis |

> Of the 6 rows above, **5 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1, LOEUF=0.415 — LoF-INTOLERANT |
| GWAS Catalog | 19 unique SNPs / 38 rows |
| ClinVar | 86 records; 6 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 36 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'RPRD1A'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 86 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 5 of 5 traits by best p-value, aggregated from 9 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q96P16 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000141425/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/RPRD1A — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/RPRD1A — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=RPRD1A%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/RPRD1A — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:53:08  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
