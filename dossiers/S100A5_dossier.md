# Protein Dossier — S100A5 (Protein S100-A5)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Low grade serous ovarian cancer | -0.394 | 0.134 | 0.00325 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: hiatus hernia | 0.106 | 0.0372 | 0.00432 | Wald ratio | 1 | trans | NA |
| Rheumatoid arthritis | 0.107 | 0.0377 | 0.0044 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: K29 Gastritis and duodenitis | -0.124 | 0.0462 | 0.00709 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: hypertrophic cardiomyopathy (hcm  or  hocm) | 0.64 | 0.25 | 0.0104 | Wald ratio | 1 | trans | NA |
| Forearm bone mineral density | -0.0995 | 0.0397 | 0.0123 | Wald ratio | 1 | trans | NA |
| Eye problems or disorders: Glaucoma | -0.15 | 0.0612 | 0.0141 | Wald ratio | 1 | trans | NA |
| Platelet count | 2.42 | 1.07 | 0.0241 | Wald ratio | 1 | trans | NA |
| Anorexia nervosa | 0.175 | 0.0809 | 0.0303 | Wald ratio | 1 | trans | NA |
| Fasting glucose | 0.0173 | 0.00815 | 0.0334 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | -0.194 | 0.0917 | 0.0348 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: muscle or soft tissue injuries | 0.137 | 0.065 | 0.0357 | Wald ratio | 1 | trans | NA |
| _...and 98 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_3 association rows across 3 traits (2 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Hematological traits (multi-trait analysis) | 8e-29 | rs1810765 | 1 | GCST90838667 | no MR -> candidate analysis |
| Atopic dermatitis | 3e-8 | rs141484567 | 1 | GCST90244002 | no MR -> candidate analysis |
| White blood cell count (monocyte) | 5e-8 | rs1810765 | 1 | GCST90026507 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 59 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| liver disorder | 0.066 | — | common-variant locus | no MR -> candidate analysis |
| osteomyelitis | 0.055 | — | common-variant locus | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Protein S100-A5) |
| gnomAD constraint | pLI=0.026, LOEUF=1.57 — LoF-tolerant |
| GWAS Catalog | 54 unique SNPs / 106 rows |
| ClinVar | 32 records; 8 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 59 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'S100A5' and resolved to 'Protein S100-A5' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 32 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 3 of 3 traits by best p-value, aggregated from 3 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P33763 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000196420/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4296264/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/S100A5 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/S100A5 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=S100A5%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/S100A5 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:55:06  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
