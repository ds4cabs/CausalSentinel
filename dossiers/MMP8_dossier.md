# Protein Dossier — MMP8 (Neutrophil collagenase)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Height | -0.0985 | 0.0217 | 5.48e-06 | Wald ratio | 1 | trans | NA |
| Lumbar spine bone mineral density | 0.218 | 0.0635 | 6.05e-04 | Wald ratio | 1 | trans | NA |
| Cancer code  self-reported: prostate cancer | -0.00295 | 0.000896 | 9.99e-04 | Inverse variance weighted | 2 | cis | NA |
| Cancer code  self-reported: prostate cancer | -0.00295 | 0.000896 | 9.99e-04 | Inverse variance weighted | 2 | trans | NA |
| HbA1C | -0.0773 | 0.0266 | 0.00364 | Wald ratio | 1 | trans | NA |
| Femoral neck bone mineral density | 0.145 | 0.0544 | 0.00754 | Wald ratio | 1 | trans | NA |
| Birth length | 0.185 | 0.0739 | 0.0122 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: M16 Coxarthrosis [arthrosis of hip] | -0.0031 | 0.00126 | 0.0138 | Inverse variance weighted | 2 | cis | NA |
| Diagnoses - main ICD10: M16 Coxarthrosis [arthrosis of hip] | -0.0031 | 0.00126 | 0.0138 | Inverse variance weighted | 2 | trans | NA |
| Non-cancer illness code  self-reported: hypertension | 0.0142 | 0.00579 | 0.014 | Inverse variance weighted | 2 | cis | NA |
| Non-cancer illness code  self-reported: hypertension | 0.0142 | 0.00579 | 0.014 | Inverse variance weighted | 2 | trans | NA |
| Weight | 0.0214 | 0.00914 | 0.0193 | Inverse variance weighted | 2 | cis | NA |
| _...and 156 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2954_56_2` | MMP-8 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_26 association rows across 19 traits (26 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| MMP8/OLR1 protein level ratio | 2e-1504 | rs35231465 | 1 | GCST90315464 | no MR -> candidate analysis |
| MMP8/MMP9 protein level ratio | 5e-1381 | rs35231465 | 1 | GCST90315463 | no MR -> candidate analysis |
| HGF/MMP8 protein level ratio | 9e-990 | rs35231465 | 1 | GCST90315055 | no MR -> candidate analysis |
| MMP8/TGFA protein level ratio | 2e-920 | rs35231465 | 1 | GCST90315466 | no MR -> candidate analysis |
| MMP8/PGLYRP1 protein level ratio | 3e-857 | rs35231465 | 1 | GCST90315465 | no MR -> candidate analysis |
| LCN2/MMP8 protein level ratio | 6e-852 | rs35231465 | 1 | GCST90315305 | no MR -> candidate analysis |
| Neutrophil collagenase (analyte X9172.69) levels | 5e-238 | rs1320632 | 1 | GCST90427676 | no MR -> candidate analysis |
| MMP1 protein levels | 2e-126 | rs146135014 | 3 | GCST90469919 | no MR -> candidate analysis |
| Neutrophil collagenase levels | 4e-104 | rs35231465 | 1 | GCST90248651 | no MR -> candidate analysis |
| Cerebrospinal fluid protein MMP8 levels | 1e-64 | rs1320632 | 1 | GCST90944434 | no MR -> candidate analysis |
| MMP8 protein levels | 5e-55 | rs141116762 | 3 | GCST90469922 | no MR -> candidate analysis |
| Serum levels of protein MMP8 | 6e-48 | rs35231465 | 1 | GCST90090532 | no MR -> candidate analysis |
| _...and 7 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 754 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| response to stimulus | 0.457 | — | common-variant locus | no MR -> candidate analysis |

> Of the 1 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 5 known modulators (Neutrophil collagenase) |
| gnomAD constraint | pLI=1.2e-28, LOEUF=1.6 — LoF-tolerant |
| GWAS Catalog | 120 unique SNPs / 263 rows |
| ClinVar | 118 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 754 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'MMP8' and resolved to 'Neutrophil collagenase' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 118 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 19 of 19 traits by best p-value, aggregated from 26 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P22894 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000118113/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4588/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/MMP8 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/MMP8 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=MMP8%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/MMP8 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:50:44  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
