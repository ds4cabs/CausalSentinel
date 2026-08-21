# Protein Dossier — SERPINE2 (Glia-derived nexin)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: deep venous thrombosis (dvt) | -0.23 | 0.0603 | 1.35e-04 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I80 Phlebitis and thrombophlebitis | -0.415 | 0.154 | 0.00685 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: B37 Candidiasis | 0.527 | 0.199 | 0.00802 | Wald ratio | 1 | cis | NA |
| Sodium in urine | 0.0145 | 0.00663 | 0.0283 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: ankylosing spondylitis | 0.219 | 0.104 | 0.0344 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: D12 Benign neoplasm of colon  rectum  anus and anal canal | 0.0997 | 0.0516 | 0.0532 | Wald ratio | 1 | cis | NA |
| Nucleus accumbens volume | 7.26 | 3.76 | 0.0537 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: H25 Senile cataract | 0.121 | 0.0683 | 0.0769 | Wald ratio | 1 | cis | NA |
| Thalamus volume | 37.5 | 21.3 | 0.0784 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Ankle | 0.092 | 0.0526 | 0.0799 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: C61 Malignant neoplasm of prostate | 0.128 | 0.0731 | 0.0811 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: malignant melanoma | 0.119 | 0.0682 | 0.0821 | Wald ratio | 1 | cis | NA |
| _...and 68 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3217_74_2` | Protease nexin I | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_288 association rows across 247 traits (276 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| ANGPT1/PDGFB protein level ratio | 2e-1484 | rs13412535 | 1 | GCST90313267 | no MR -> candidate analysis |
| PDGFA/PDGFB protein level ratio | 5e-1164 | rs13412535 | 1 | GCST90315614 | no MR -> candidate analysis |
| APP/PDGFB protein level ratio | 8e-1008 | rs13412535 | 1 | GCST90313329 | no MR -> candidate analysis |
| Glia-derived nexin levels | 4e-960 | rs13412535 | 3 | GCST90247735 | no MR -> candidate analysis |
| PDGFB/SPARC protein level ratio | 5e-894 | rs13412535 | 1 | GCST90315628 | no MR -> candidate analysis |
| DKK1/PDGFB protein level ratio | 2e-873 | rs13412535 | 1 | GCST90314476 | no MR -> candidate analysis |
| PDGFB/VEGFC protein level ratio | 9e-799 | rs13412535 | 1 | GCST90315635 | no MR -> candidate analysis |
| HBEGF/PDGFB protein level ratio | 8e-683 | rs13412535 | 1 | GCST90315034 | no MR -> candidate analysis |
| PRKAR1A/SNAP23 protein level ratio | 3e-489 | rs13412535 | 1 | GCST90315728 | no MR -> candidate analysis |
| PDGFB/SPINT2 protein level ratio | 2e-423 | rs13412535 | 1 | GCST90315629 | no MR -> candidate analysis |
| CCL28/PDGFB protein level ratio | 5e-423 | rs13412535 | 1 | GCST90313695 | no MR -> candidate analysis |
| DIABLO/PRKAR1A protein level ratio | 4e-382 | rs13412535 | 1 | GCST90314469 | no MR -> candidate analysis |
| _...and 235 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 318 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| venous thromboembolism | 0.814 | — | common-variant locus | no MR -> candidate analysis |
| Thromboembolism | 0.715 | — | common-variant locus | no MR -> candidate analysis |
| deep vein thrombosis | 0.572 | — | common-variant locus | no MR -> candidate analysis |
| phototoxic dermatitis | 0.32 | — | common-variant locus | no MR -> candidate analysis |
| bone Paget disease | 0.299 | — | common-variant locus | no MR -> candidate analysis |

> Of the 5 rows above, **5 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.57, LOEUF=0.603 — LoF-tolerant |
| GWAS Catalog | 52 unique SNPs / 101 rows |
| ClinVar | 92 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 318 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'SERPINE2'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 92 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 247 traits by best p-value, aggregated from 288 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P07093 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000135919/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/SERPINE2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/SERPINE2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=SERPINE2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/SERPINE2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:02:45  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
