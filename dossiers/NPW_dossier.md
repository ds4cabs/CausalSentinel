# Protein Dossier — NPW (Neuropeptide W)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Weight | 0.0251 | 0.00589 | 1.99e-05 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | 0.0237 | 0.00667 | 3.80e-04 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertension | -0.0374 | 0.0118 | 0.00156 | Wald ratio | 1 | cis | NA |
| Birth length | -0.0872 | 0.0323 | 0.00703 | Wald ratio | 1 | cis | NA |
| Small vessel disease | -0.29 | 0.109 | 0.00794 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: uterine fibroids | 0.121 | 0.0479 | 0.0116 | Wald ratio | 1 | cis | NA |
| Subjective well being | 0.0234 | 0.00938 | 0.0124 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hyperthyroidism or thyrotoxicosis | -0.223 | 0.098 | 0.0231 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: chronic obstructive airways disease or copd | 0.2 | 0.0946 | 0.0346 | Wald ratio | 1 | cis | NA |
| Forearm bone mineral density | -0.089 | 0.0427 | 0.0372 | Wald ratio | 1 | cis | NA |
| Sodium in urine | 0.0136 | 0.00657 | 0.0379 | Wald ratio | 1 | cis | NA |
| Chronic kidney disease | -0.0985 | 0.0516 | 0.0563 | Wald ratio | 1 | cis | NA |
| _...and 87 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_6 association rows across 5 traits (6 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Neuropeptide W levels | 3e-238 | rs12921264 | 2 | GCST90248663 | no MR -> candidate analysis |
| Serum levels of protein NPW | 7e-115 | rs112724384 | 1 | GCST90090948 | no MR -> candidate analysis |
| Blood protein levels | 1e-74 | rs112050738 | 1 | GCST006585 | no MR -> candidate analysis |
| PKD1 protein levels | 7e-17 | rs8051877 | 1 | GCST90470240 | no MR -> candidate analysis |
| Gut microbial network clusters (Red (at 1 year) x Vaginal Bi | 4e-9 | rs7186383 | 1 | GCST90569440 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 23 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| hypertensive disorder | 0.16 | — | common-variant locus | no MR -> candidate analysis |

> Of the 1 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.0032, LOEUF=1.46 — LoF-tolerant |
| GWAS Catalog | 106 unique SNPs / 216 rows |
| ClinVar | 93 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 23 of 23 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'NPW'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 93 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 5 of 5 traits by best p-value, aggregated from 6 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q8N729 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000183971/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/NPW — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/NPW — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=NPW%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/NPW — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:03:18  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
