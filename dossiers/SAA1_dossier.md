# Protein Dossier — SAA1 (Serum amyloid A-1 protein)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Mean cell volume | -0.529 | 0.159 | 8.44e-04 | Inverse variance weighted | 2 | trans | NA |
| Mean cell volume | -0.529 | 0.159 | 8.44e-04 | Inverse variance weighted | 2 | trans | NA |
| Haemoglobin concentration | -0.111 | 0.0351 | 0.00162 | Inverse variance weighted | 2 | trans | NA |
| Haemoglobin concentration | -0.111 | 0.0351 | 0.00162 | Inverse variance weighted | 2 | trans | NA |
| Platelet count | 14.1 | 4.61 | 0.00228 | Inverse variance weighted | 2 | trans | NA |
| Platelet count | 14.1 | 4.61 | 0.00228 | Inverse variance weighted | 2 | trans | NA |
| Knee and hip osteoarthritis | -0.401 | 0.137 | 0.00331 | Inverse variance weighted | 2 | trans | NA |
| Knee and hip osteoarthritis | -0.401 | 0.137 | 0.00331 | Inverse variance weighted | 2 | trans | NA |
| Non-cancer illness code  self-reported: sleep apnoea | 0.216 | 0.0817 | 0.00828 | Inverse variance weighted | 3 | trans | NA |
| Non-cancer illness code  self-reported: sleep apnoea | 0.216 | 0.0817 | 0.00828 | Inverse variance weighted | 3 | cis | NA |
| Non-cancer illness code  self-reported: sleep apnoea | 0.216 | 0.0817 | 0.00828 | Inverse variance weighted | 3 | trans | NA |
| Knee osteoarthritis | -0.443 | 0.173 | 0.0103 | Inverse variance weighted | 2 | trans | NA |
| _...and 278 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-4336_2_1` | SAA | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_18 association rows across 8 traits (15 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Serum amyloid A-1 protein levels (SAA1.4336.2.1) | 1e-771 | rs35179000 | 3 | GCST90242795 | no MR -> candidate analysis |
| Serum amyloid A-1 protein levels | 2e-247 | rs10690148 | 5 | GCST90162052 | no MR -> candidate analysis |
| Amyloid A serum levels | 4e-145 | rs11024600 | 2 | GCST90244128 | no MR -> candidate analysis |
| SAA4 protein levels | 1e-30 | rs139240396 | 2 | GCST90470521 | no MR -> candidate analysis |
| ER membrane protein complex subunit 2 protein levels (SomaSc | 2e-29 | rs1829575 | 1 | GCST90441815 | no MR -> candidate analysis |
| Bone mineral density mean | 3e-20 | rs566507596 | 1 | GCST90321120 | no MR -> candidate analysis |
| SAA1 protein levels | 1e-19 | rs10832916 | 1 | GCST90453161 | no MR -> candidate analysis |
| Lewy body disease | 3e-6 | rs2124379 | 3 | GCST002591 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 719 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Abnormality of the gastrointestinal tract | 0.384 | — | common-variant locus | no MR -> candidate analysis |

> Of the 1 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.33, LOEUF=0.93 — LoF-tolerant |
| GWAS Catalog | 114 unique SNPs / 274 rows |
| ClinVar | 49 records; 5 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 719 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'SAA1'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 49 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 8 of 8 traits by best p-value, aggregated from 18 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P0DJI8 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000173432/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/SAA1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/SAA1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=SAA1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/SAA1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:55:37  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
