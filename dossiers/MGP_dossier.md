# Protein Dossier — MGP (Matrix Gla protein)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Heel bone mineral density (BMD) T-score  automated | 0.0545 | 0.0121 | 6.42e-06 | Wald ratio | 1 | cis | NA |
| Fractured or broken bones in last 5 years | -0.147 | 0.0338 | 1.29e-05 | Wald ratio | 1 | cis | NA |
| Height | 0.0351 | 0.0113 | 0.00194 | Wald ratio | 1 | cis | NA |
| Mean cell haemoglobin | 0.105 | 0.0374 | 0.00498 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: psoriasis | 0.2 | 0.0724 | 0.00565 | Wald ratio | 1 | cis | NA |
| Weight | 0.022 | 0.00825 | 0.00752 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Ankle | -0.278 | 0.107 | 0.00913 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: H25 Senile cataract | 0.214 | 0.0867 | 0.0138 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Wrist | -0.199 | 0.082 | 0.0153 | Wald ratio | 1 | cis | NA |
| Lumbar spine bone mineral density | 0.0822 | 0.034 | 0.0157 | Wald ratio | 1 | cis | NA |
| Mean cell volume | 0.223 | 0.0955 | 0.0193 | Wald ratio | 1 | cis | NA |
| Sleep duration | 0.017 | 0.00729 | 0.0195 | Wald ratio | 1 | cis | NA |
| _...and 90 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_3 association rows across 3 traits (3 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Hand grip strength left (UKB data field 46) | 3e-30 | rs1800801 | 1 | GCST90468168 | no MR -> candidate analysis |
| Erosive hand osteoarthritis | 4e-13 | rs1800801 | 1 | GCST90271957 | no MR -> candidate analysis |
| Estimated glomerular filtration rate (creatinine) | 2e-9 | rs11393307 | 1 | GCST90100220 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1118 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Keutel syndrome | 0.794 | — | established (curated) | no MR -> candidate analysis |
| spondyloepiphyseal dysplasia | 0.195 | — | established (curated) | no MR -> candidate analysis |
| osteoarthritis, hand | 0.581 | — | common-variant locus | no MR -> candidate analysis |
| osteoarthritis, knee | 0.568 | — | common-variant locus | no MR -> candidate analysis |
| osteoarthritis, hip | 0.542 | — | common-variant locus | no MR -> candidate analysis |
| total joint arthroplasty | 0.487 | — | common-variant locus | no MR -> candidate analysis |
| hereditary disease | 0.265 | — | established (curated) | no MR -> candidate analysis |
| polyarticular arthritis | 0.262 | — | common-variant locus | no MR -> candidate analysis |
| Short distal phalanx of finger | 0.195 | — | established (curated) | no MR -> candidate analysis |
| Short palm | 0.195 | — | established (curated) | no MR -> candidate analysis |
| Platyspondyly | 0.195 | — | established (curated) | no MR -> candidate analysis |
| Short stature | 0.195 | — | established (curated) | no MR -> candidate analysis |

> Of the 12 rows above, **12 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=6.5e-05, LOEUF=1.42 — LoF-tolerant |
| GWAS Catalog | 39 unique SNPs / 78 rows |
| ClinVar | 179 records; 4 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1118 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'MGP'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 179 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 3 of 3 traits by best p-value, aggregated from 3 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P08493 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000111341/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/MGP — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/MGP — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=MGP%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/MGP — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:47:46  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
