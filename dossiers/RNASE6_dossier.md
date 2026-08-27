# Protein Dossier — RNASE6 (Ribonuclease K6)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: joint disorder | 0.104 | 0.0375 | 0.00549 | Wald ratio | 1 | cis | NA |
| Autism | -0.0889 | 0.0328 | 0.00673 | Wald ratio | 1 | cis | NA |
| Sleep duration | 0.00555 | 0.00223 | 0.0126 | Wald ratio | 1 | cis | NA |
| Depressive symptoms | -0.00903 | 0.00401 | 0.0244 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code self-reported: pulmonary embolism (with or without) dvt | -0.0747 | 0.0341 | 0.0285 | Wald ratio | 1 | cis | NA |
| Knee osteoarthritis | 0.0679 | 0.031 | 0.0285 | Wald ratio | 1 | cis | NA |
| Triglycerides | 0.0134 | 0.00622 | 0.0307 | Wald ratio | 1 | cis | NA |
| Caudate volume | -12.1 | 5.65 | 0.0329 | Wald ratio | 1 | cis | NA |
| Height | -0.00822 | 0.00391 | 0.0355 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: psoriasis | -0.0591 | 0.0285 | 0.0381 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | 0.00509 | 0.00247 | 0.0392 | Wald ratio | 1 | cis | NA |
| Parkinson's disease | -0.0956 | 0.0472 | 0.0427 | Wald ratio | 1 | cis | NA |
| _...and 94 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_13 association rows across 12 traits (12 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Ribonuclease K6 levels | 4e-2405 | rs72669422 | 2 | GCST90249345 | no MR -> candidate analysis |
| Ribonuclease K6 levels (RNASE6.5646.20.3) | 6e-391 | rs11622942 | 1 | GCST90242668 | no MR -> candidate analysis |
| Serum levels of protein RNASE6 | 2e-306 | rs1045922 | 1 | GCST90089118 | no MR -> candidate analysis |
| EDDM3B protein levels | 2e-193 | rs12586813 | 1 | GCST90469069 | no MR -> candidate analysis |
| Blood protein levels | 4e-164 | rs2319516 | 1 | GCST006585 | no MR -> candidate analysis |
| RNAS6 protein level (protein group normalized intensity) | 4e-52 | rs11622942 | 1 | GCST90570754 | no MR -> candidate analysis |
| Monocyte side fluorescence | 1e-45 | rs1045922 | 1 | GCST90281241 | no MR -> candidate analysis |
| Ribonuclease K6 level in Chronic kidney disease with hyperte | 8e-40 | rs1045922 | 1 | GCST90238009 | no MR -> candidate analysis |
| Tumor necrosis factor receptor superfamily member 18 protein | 3e-26 | rs11623935 | 1 | GCST90437249 | no MR -> candidate analysis |
| RNASE6 protein levels | 1e-14 | rs112015241 | 1 | GCST90470479 | no MR -> candidate analysis |
| Gamma-crystallin C levels | 1e-14 | rs11622942 | 1 | GCST90423176 | no MR -> candidate analysis |
| Liver RNASE6 levels | 5e-7 | rs1045922 | 1 | GCST90802741 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 108 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| skin cancer | 0.259 | — | common-variant locus | no MR -> candidate analysis |

> Of the 1 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=NA, LOEUF=NA — Constraint metrics missing; LoF tolerance cannot be judged. |
| GWAS Catalog | 89 unique SNPs / 178 rows |
| ClinVar | 56 records; 4 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 108 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'RNASE6'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 56 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 12 of 12 traits by best p-value, aggregated from 13 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q93091 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000169413/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/RNASE6 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/RNASE6 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=RNASE6%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/RNASE6 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:51:36  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
