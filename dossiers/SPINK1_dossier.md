# Protein Dossier — SPINK1 (Serine protease inhibitor Kazal-type 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: diverticular disease or diverticulitis | -0.563 | 0.2 | 0.00489 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I84 Haemorrhoids | 0.174 | 0.0623 | 0.00533 | Wald ratio | 1 | cis | NA |
| Forearm bone mineral density | -0.182 | 0.0735 | 0.0133 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: vitiligo | 0.834 | 0.346 | 0.0159 | Wald ratio | 1 | cis | NA |
| Cigarettes smoked per day | 0.923 | 0.392 | 0.0185 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hayfever or allergic rhinitis | 0.0934 | 0.0431 | 0.0302 | Wald ratio | 1 | cis | NA |
| Ovarian cancer | 0.136 | 0.0637 | 0.0333 | Wald ratio | 1 | cis | NA |
| Triglycerides | 0.0462 | 0.0222 | 0.0371 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Other bones | -0.116 | 0.0563 | 0.0397 | Wald ratio | 1 | cis | NA |
| Bulimia nervosa | 0.066 | 0.033 | 0.0455 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M17 Gonarthrosis [arthrosis of knee] | -0.201 | 0.102 | 0.0495 | Wald ratio | 1 | cis | NA |
| Birth length | -0.0882 | 0.0453 | 0.0514 | Wald ratio | 1 | cis | NA |
| _...and 84 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_51 association rows across 30 traits (40 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating SPINK1 levels | 7e-854 | rs6580502 | 5 | GCST90860600 | no MR -> candidate analysis |
| Circulating SCGB3A2 levels | 9e-327 | rs17717320 | 3 | GCST90859981 | no MR -> candidate analysis |
| SPINK1/TFF3 protein level ratio | 1e-301 | rs4705209 | 1 | GCST90315876 | no MR -> candidate analysis |
| SCGB3A2 protein levels | 1e-236 | rs17717320 | 2 | GCST90470543 | no MR -> candidate analysis |
| SPINK1 protein levels | 8e-150 | rs550228048 | 7 | GCST90470721 | no MR -> candidate analysis |
| Non-alcoholic chronic pancreatitis | 7e-47 | rs17107296 | 1 | GCST90104595 | no MR -> candidate analysis |
| Serum levels of protein SPINK1 | 3e-31 | rs3777126 | 1 | GCST90090073 | no MR -> candidate analysis |
| Acute pancreatitis | 2e-29 | rs150261364 | 3 | GCST90255375 | no MR -> candidate analysis |
| Serine protease inhibitor Kazal-type 1 levels | 9e-20 | rs3777125 | 1 | GCST90249630 | no MR -> candidate analysis |
| Blood protein levels | 2e-17 | rs4705205 | 2 | GCST006585 | no MR -> candidate analysis |
| Chronic pancreatitis (PheCode 577.2) | 2e-17 | rs148911734 | 1 | GCST90480358 | no MR -> candidate analysis |
| Alcoholic chronic pancreatitis | 3e-15 | rs146437551 | 1 | GCST004860 | no MR -> candidate analysis |
| _...and 18 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 559 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| hereditary chronic pancreatitis | 0.902 | — | established (curated) | no MR -> candidate analysis |
| chronic pancreatitis | 0.82 | — | established (curated) | no MR -> candidate analysis |
| acute pancreatitis | 0.807 | — | common-variant locus | no MR -> candidate analysis |
| pancreas disorder | 0.758 | — | common-variant locus | no MR -> candidate analysis |
| pancreatitis | 0.595 | — | established (curated) | no MR -> candidate analysis |
| alcoholic pancreatitis | 0.695 | — | common-variant locus | no MR -> candidate analysis |
| diabetes mellitus | 0.547 | — | established (curated) | no MR -> candidate analysis |
| non-alcoholic pancreatitis | 0.447 | — | common-variant locus | no MR -> candidate analysis |

> Of the 8 rows above, **8 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.11, LOEUF=1.1 — LoF-tolerant |
| GWAS Catalog | 67 unique SNPs / 123 rows |
| ClinVar | 273 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 559 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'SPINK1'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 273 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 30 traits by best p-value, aggregated from 51 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P00995 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000164266/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/SPINK1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/SPINK1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=SPINK1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/SPINK1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:11:22  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
