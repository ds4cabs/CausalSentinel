# Protein Dossier — SERPINA11 (Serpin A11)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Fasting insulin | -0.0451 | 0.0153 | 0.00313 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: joint disorder | 0.318 | 0.119 | 0.00758 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: deep venous thrombosis (dvt) | 0.174 | 0.0659 | 0.0083 | Wald ratio | 1 | cis | NA |
| HOMA-IR | -0.0486 | 0.0201 | 0.0158 | Wald ratio | 1 | cis | NA |
| Low grade serous ovarian cancer | 0.547 | 0.233 | 0.0191 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertension | 0.0412 | 0.018 | 0.0222 | Wald ratio | 1 | cis | NA |
| Hirschsprung's disease | -1.23 | 0.542 | 0.0228 | Wald ratio | 1 | cis | NA |
| Age at menarche | 0.059 | 0.027 | 0.029 | Wald ratio | 1 | cis | NA |
| Myocardial infarction | -0.101 | 0.0473 | 0.0325 | Wald ratio | 1 | cis | NA |
| Nucleus accumbens volume | -10.5 | 5.27 | 0.0461 | Wald ratio | 1 | cis | NA |
| Lumbar spine bone mineral density | -0.0824 | 0.0418 | 0.0484 | Wald ratio | 1 | cis | NA |
| Subjective well being | 0.0243 | 0.0139 | 0.0801 | Wald ratio | 1 | cis | NA |
| _...and 93 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_64 association rows across 29 traits (58 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating SERPINA9 levels | 4e-957 | rs2402447 | 4 | GCST90860312 | no MR -> candidate analysis |
| SERPINA9 protein levels | 4e-302 | rs55664577 | 6 | GCST90470588 | no MR -> candidate analysis |
| Height | 3e-140 | rs7151526 | 1 | GCST90245848 | MR: beta=-0.0135, p=0.353 (cis) |
| SERPINA11 protein levels | 1e-101 | rs1957042 | 15 | GCST90453321 | no MR -> candidate analysis |
| Circulating GDF2 levels | 4e-94 | rs1956721 | 3 | GCST90859810 | no MR -> candidate analysis |
| Serpin A11 levels | 4e-89 | rs56026704 | 1 | GCST90249608 | no MR -> candidate analysis |
| GDF2 protein levels | 2e-50 | rs61738925 | 1 | GCST90469322 | no MR -> candidate analysis |
| SERPINA12 protein levels | 3e-40 | rs17751962 | 4 | GCST90470581 | no MR -> candidate analysis |
| BMP10 protein levels | 8e-40 | rs7152610 | 2 | GCST90468452 | no MR -> candidate analysis |
| SERPINA4 protein levels | 3e-37 | rs1951020 | 4 | GCST90470584 | no MR -> candidate analysis |
| Serum levels of protein NCF2 | 1e-35 | rs112963922 | 1 | GCST90086205 | no MR -> candidate analysis |
| Serum levels of protein MRPL33 | 6e-34 | rs112963922 | 1 | GCST90087451 | no MR -> candidate analysis |
| _...and 17 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 34 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| alcohol drinking | 0.52 | — | common-variant locus | no MR -> candidate analysis |
| Pleural effusion | 0.438 | — | established (curated) | no MR -> candidate analysis |
| pericardial effusion | 0.438 | — | established (curated) | no MR -> candidate analysis |
| stroke disorder | 0.366 | — | common-variant locus | no MR -> candidate analysis |
| Non-immune hydrops fetalis | 0.182 | — | established (curated) | no MR -> candidate analysis |
| respiratory system disorder | 0.177 | — | common-variant locus | no MR -> candidate analysis |
| acute tonsillitis | 0.095 | — | common-variant locus | no MR -> candidate analysis |
| placenta praevia | 0.065 | — | common-variant locus | no MR -> candidate analysis |

> Of the 8 rows above, **8 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=8.3e-10, LOEUF=1.3 — LoF-tolerant |
| GWAS Catalog | 160 unique SNPs / 424 rows |
| ClinVar | 108 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 34 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'SERPINA11'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 108 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 29 traits by best p-value, aggregated from 64 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q86U17 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000186910/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/SERPINA11 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/SERPINA11 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=SERPINA11%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/SERPINA11 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:01:17  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
