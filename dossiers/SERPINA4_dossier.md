# Protein Dossier — SERPINA4 (Kallistatin)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: bladder problem (not cancer) | 0.154 | 0.0472 | 0.00108 | Inverse variance weighted | 2 | cis | NA |
| Non-cancer illness code  self-reported: bladder problem (not cancer) | 0.154 | 0.0472 | 0.00108 | Inverse variance weighted | 2 | cis | NA |
| Creatinine (enzymatic) in urine | 0.0113 | 0.00401 | 0.00472 | Inverse variance weighted | 2 | cis | NA |
| Creatinine (enzymatic) in urine | 0.0113 | 0.00401 | 0.00472 | Inverse variance weighted | 2 | cis | NA |
| Neo-neuroticism | -0.412 | 0.162 | 0.011 | Inverse variance weighted | 2 | cis | NA |
| Neo-neuroticism | -0.412 | 0.162 | 0.011 | Inverse variance weighted | 2 | cis | NA |
| Non-cancer illness code  self-reported: hiatus hernia | 0.061 | 0.0259 | 0.0184 | Inverse variance weighted | 2 | cis | NA |
| Non-cancer illness code  self-reported: hiatus hernia | 0.061 | 0.0259 | 0.0184 | Inverse variance weighted | 2 | cis | NA |
| Fracture resulting from simple fall | -0.0248 | 0.0113 | 0.0281 | Inverse variance weighted | 2 | cis | NA |
| Fracture resulting from simple fall | -0.0248 | 0.0113 | 0.0281 | Inverse variance weighted | 2 | cis | NA |
| Neo-agreeableness | 0.26 | 0.126 | 0.0391 | Inverse variance weighted | 2 | cis | NA |
| Neo-agreeableness | 0.26 | 0.126 | 0.0391 | Inverse variance weighted | 2 | cis | NA |
| _...and 145 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3449_58_2` | Kallistatin | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_90 association rows across 40 traits (86 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating SERPINA12 levels | 5e-3381 | rs17091005 | 3 | GCST90859783 | no MR -> candidate analysis |
| Serpin A12 levels | 1e-382 | rs4900235 | 2 | GCST90249609 | no MR -> candidate analysis |
| Serum levels of protein SERPINA4 | 2e-135 | rs5511 | 3 | GCST90088394 | no MR -> candidate analysis |
| Kallistatin levels (SERPINA4.3449.58.2) | 5e-110 | rs10139745 | 6 | GCST90241682 | no MR -> candidate analysis |
| KLK13 protein levels | 2e-101 | rs5511 | 2 | GCST90469699 | no MR -> candidate analysis |
| SERPINA12 protein levels | 2e-96 | rs17752932 | 10 | GCST90470581 | no MR -> candidate analysis |
| Kallistatin levels | 1e-95 | rs5511 | 9 | GCST90161793 | no MR -> candidate analysis |
| Circulating KLK13 levels | 8e-95 | rs5511 | 3 | GCST90860002 | no MR -> candidate analysis |
| Serum levels of protein SERPINA12 | 3e-69 | rs4900235 | 1 | GCST90089492 | no MR -> candidate analysis |
| Circulating GDF2 levels | 2e-66 | rs4905214 | 1 | GCST90859810 | no MR -> candidate analysis |
| SERPINA4 protein levels | 1e-62 | rs10139745 | 13 | GCST90453221 | no MR -> candidate analysis |
| Protein S100-A10 levels | 3e-52 | rs5511 | 1 | GCST90249400 | no MR -> candidate analysis |
| _...and 28 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 230 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| optic atrophy | 0.392 | — | common-variant locus | no MR -> candidate analysis |

> Of the 1 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1.6e-08, LOEUF=1.33 — LoF-tolerant |
| GWAS Catalog | 170 unique SNPs / 441 rows |
| ClinVar | 119 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 230 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'SERPINA4'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 119 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 40 traits by best p-value, aggregated from 90 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P29622 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000100665/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/SERPINA4 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/SERPINA4 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=SERPINA4%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/SERPINA4 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:01:58  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
