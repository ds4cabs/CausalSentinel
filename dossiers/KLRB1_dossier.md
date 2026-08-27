# Protein Dossier — KLRB1 (Killer cell lectin-like receptor subfamily B member 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Depressive symptoms | 0.0423 | 0.0188 | 0.0244 | Wald ratio | 1 | cis | NA |
| Neuroticism | 0.0235 | 0.0141 | 0.0956 | Wald ratio | 1 | cis | NA |
| Putamen volume | -47.2 | 28.9 | 0.102 | Wald ratio | 1 | cis | NA |
| Lumbar spine bone mineral density | 0.0861 | 0.0595 | 0.148 | Wald ratio | 1 | cis | NA |
| Nucleus accumbens volume | -7.24 | 5.21 | 0.164 | Wald ratio | 1 | cis | NA |
| Pallidum volume | -8.06 | 9.25 | 0.384 | Wald ratio | 1 | cis | NA |
| Schizophrenia | -0.0395 | 0.0516 | 0.445 | Wald ratio | 1 | cis | NA |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_28 association rows across 17 traits (23 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| KLRB1 protein levels | 4e-189 | rs150796627 | 5 | GCST90469709 | no MR -> candidate analysis |
| Killer cell lectin-like receptor subfamily B member 1 levels | 3e-125 | rs4763630 | 1 | GCST90248209 | no MR -> candidate analysis |
| Killer cell lectin-like receptor subfamily B member 1 (analy | 1e-106 | rs1135816 | 1 | GCST90421233 | no MR -> candidate analysis |
| Cerebrospinal fluid protein KLRB1 levels | 2e-43 | rs7963831 | 1 | GCST90943562 | no MR -> candidate analysis |
| PZP protein levels | 8e-31 | rs186389452 | 5 | GCST90470399 | no MR -> candidate analysis |
| Serum levels of protein KLRB1 | 8e-27 | rs10771925 | 1 | GCST90086455 | no MR -> candidate analysis |
| KLRF1 protein levels | 4e-25 | rs563890415 | 1 | GCST90469712 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 2e-20 | rs28545519 | 1 | GCST90838669 | no MR -> candidate analysis |
| Circulating MFAP5 levels | 1e-17 | rs144729793 | 1 | GCST90860482 | no MR -> candidate analysis |
| Blood protein levels | 2e-16 | rs3933456 | 1 | GCST006585 | no MR -> candidate analysis |
| Hodgkin's lymphoma | 1e-10 | rs2109903 | 1 | GCST012335 | no MR -> candidate analysis |
| Mosaic loss of chromosome X | 5e-9 | rs5796352 | 2 | GCST90328148 | no MR -> candidate analysis |
| _...and 5 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 509 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| sensory perception of smell | 0.447 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.233 | — | common-variant locus | no MR -> candidate analysis |
| urolithiasis | 0.233 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=3.3e-08, LOEUF=1.11 — LoF-tolerant |
| GWAS Catalog | 46 unique SNPs / 85 rows |
| ClinVar | 91 records; 5 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 509 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'KLRB1'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 91 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 17 of 17 traits by best p-value, aggregated from 28 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q12918 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000111796/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/KLRB1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/KLRB1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=KLRB1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/KLRB1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:25:59  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
