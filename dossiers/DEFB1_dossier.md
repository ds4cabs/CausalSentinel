# Protein Dossier — DEFB1 (Beta-defensin 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Squamous cell lung cancer | 0.447 | 0.138 | 0.00123 | Wald ratio | 1 | trans | NA |
| Happiness | -0.0175 | 0.00718 | 0.0146 | Inverse variance weighted | 2 | cis | NA |
| Happiness | -0.0175 | 0.00718 | 0.0146 | Inverse variance weighted | 2 | trans | NA |
| Eye problems or disorders: Injury or trauma resulting in loss of vision | -0.211 | 0.0944 | 0.0252 | Inverse variance weighted | 2 | cis | NA |
| Eye problems or disorders: Injury or trauma resulting in loss of vision | -0.211 | 0.0944 | 0.0252 | Inverse variance weighted | 2 | trans | NA |
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | 0.0484 | 0.0245 | 0.0487 | Inverse variance weighted | 2 | cis | NA |
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | 0.0484 | 0.0245 | 0.0487 | Inverse variance weighted | 2 | trans | NA |
| Diagnoses - main ICD10: L03 Cellulitis | 0.114 | 0.0578 | 0.0489 | Inverse variance weighted | 2 | cis | NA |
| Diagnoses - main ICD10: L03 Cellulitis | 0.114 | 0.0578 | 0.0489 | Inverse variance weighted | 2 | trans | NA |
| Diagnoses - main ICD10: J33 Nasal polyp | -0.196 | 0.104 | 0.0592 | Inverse variance weighted | 2 | cis | NA |
| Diagnoses - main ICD10: J33 Nasal polyp | -0.196 | 0.104 | 0.0592 | Inverse variance weighted | 2 | trans | NA |
| Femoral neck bone mineral density | 0.0344 | 0.0198 | 0.0829 | Wald ratio | 1 | cis | NA |
| _...and 101 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_11 association rows across 9 traits (9 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Serum levels of protein DEFB1 | 2e-103 | rs2741130 | 2 | GCST90089538 | no MR -> candidate analysis |
| Cerebrospinal fluid protein DEFB1 levels | 4e-80 | rs2977772 | 1 | GCST90944743 | no MR -> candidate analysis |
| Beta-defensin 1 levels (DEFB1.6629.3.3) | 3e-39 | rs2702945 | 1 | GCST90240410 | no MR -> candidate analysis |
| Circulating CDSN levels | 3e-26 | rs2293959 | 1 | GCST90860191 | no MR -> candidate analysis |
| Blood cell traits latent factor 22 (white cell) | 2e-20 | rs5743467 | 2 | GCST90559264 | no MR -> candidate analysis |
| WFDC12 protein levels | 7e-13 | rs2702945 | 1 | GCST90471073 | no MR -> candidate analysis |
| Tanner 2 to Tanner 4 pubertal stage transition (joint longit | 4e-8 | rs2741127 | 1 | GCST90444215 | no MR -> candidate analysis |
| Plasma kynurenine to tryptophan ratio in major depressive di | 2e-7 | rs5743467 | 1 | GCST005343 | no MR -> candidate analysis |
| Plasma kynurenine levels in major depressive disorder | 8e-7 | rs5743467 | 1 | GCST005342 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 455 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| cervical carcinoma | 0.39 | — | common-variant locus | no MR -> candidate analysis |
| diabetes mellitus | 0.367 | — | common-variant locus | no MR -> candidate analysis |
| cardioembolic stroke | 0.355 | — | common-variant locus | no MR -> candidate analysis |
| response to xenobiotic stimulus | 0.191 | — | common-variant locus | no MR -> candidate analysis |
| gastrointestinal disease | 0.162 | — | common-variant locus | no MR -> candidate analysis |

> Of the 5 rows above, **5 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.0093, LOEUF=3.51 — LoF-tolerant |
| GWAS Catalog | 147 unique SNPs / 353 rows |
| ClinVar | 148 records; 8 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 455 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'DEFB1'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 148 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 9 of 9 traits by best p-value, aggregated from 11 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P60022 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000164825/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/DEFB1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/DEFB1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=DEFB1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/DEFB1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:15:23  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
