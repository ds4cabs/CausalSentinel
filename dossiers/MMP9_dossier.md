# Protein Dossier — MMP9 (Matrix metalloproteinase-9)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | 0.0817 | 0.0336 | 0.015 | Inverse variance weighted | 2 | trans | NA |
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | 0.0817 | 0.0336 | 0.015 | Inverse variance weighted | 2 | cis | NA |
| Non-cancer illness code  self-reported: gastro-oesophageal reflux (gord)  or  gastric reflux | 0.097 | 0.04 | 0.0154 | Inverse variance weighted | 2 | trans | NA |
| Non-cancer illness code  self-reported: gastro-oesophageal reflux (gord)  or  gastric reflux | 0.097 | 0.04 | 0.0154 | Inverse variance weighted | 2 | cis | NA |
| Diagnoses - main ICD10: K80 Cholelithiasis | 0.122 | 0.0506 | 0.0156 | Inverse variance weighted | 2 | trans | NA |
| Diagnoses - main ICD10: K80 Cholelithiasis | 0.122 | 0.0506 | 0.0156 | Inverse variance weighted | 2 | cis | NA |
| Large vessel disease | -0.361 | 0.16 | 0.0243 | Wald ratio | 1 | cis | NA |
| Autism | 0.519 | 0.235 | 0.0269 | Wald ratio | 1 | trans | NA |
| Fasting insulin | -0.0242 | 0.0119 | 0.0416 | Inverse variance weighted | 2 | trans | NA |
| Fasting insulin | -0.0242 | 0.0119 | 0.0416 | Inverse variance weighted | 2 | cis | NA |
| Systolic blood pressure  automated reading | 0.0164 | 0.00838 | 0.0505 | Inverse variance weighted | 2 | trans | NA |
| Systolic blood pressure  automated reading | 0.0164 | 0.00838 | 0.0505 | Inverse variance weighted | 2 | cis | NA |
| _...and 127 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2579_17_5` | MMP-9 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_75 association rows across 60 traits (70 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| MMP9/OSM protein level ratio | 3e-346 | rs17576 | 1 | GCST90315468 | no MR -> candidate analysis |
| MMP9/OLR1 protein level ratio | 5e-213 | rs17576 | 1 | GCST90315467 | no MR -> candidate analysis |
| MMP9/PLTP protein level ratio | 7e-205 | rs17576 | 1 | GCST90315471 | no MR -> candidate analysis |
| MMP8/MMP9 protein level ratio | 1e-162 | rs17576 | 1 | GCST90315463 | no MR -> candidate analysis |
| HGF/MMP9 protein level ratio | 4e-160 | rs17576 | 1 | GCST90315056 | no MR -> candidate analysis |
| CEACAM8/MMP9 protein level ratio | 4e-136 | rs17576 | 1 | GCST90314002 | no MR -> candidate analysis |
| Circulating PLTP levels | 8e-135 | rs572063876 | 4 | GCST90860472 | no MR -> candidate analysis |
| Circulating MMP9 levels | 5e-134 | rs17576 | 2 | GCST90859917 | no MR -> candidate analysis |
| MMP9/PGLYRP1 protein level ratio | 3e-130 | rs17576 | 1 | GCST90315469 | no MR -> candidate analysis |
| MMP9/PLAUR protein level ratio | 5e-125 | rs17576 | 1 | GCST90315470 | no MR -> candidate analysis |
| CLEC4D/MMP9 protein level ratio | 4e-121 | rs17576 | 1 | GCST90314113 | no MR -> candidate analysis |
| MMP9 protein levels | 6e-116 | rs17576 | 2 | GCST90469923 | no MR -> candidate analysis |
| _...and 48 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 3214 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| metaphyseal anadysplasia | 0.796 | — | established (curated) | no MR -> candidate analysis |
| Crohn disease | 0.626 | — | common-variant locus | no MR -> candidate analysis |
| COVID-19 | 0.441 | — | common-variant locus | no MR -> candidate analysis |
| age-related macular degeneration | 0.443 | — | common-variant locus | no MR -> candidate analysis |
| macular degeneration | 0.425 | — | common-variant locus | no MR -> candidate analysis |
| coronary artery disorder | 0.09 | — | common-variant locus | no MR -> candidate analysis |

> Of the 6 rows above, **6 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 5 known modulators (Matrix metalloproteinase-9) |
| gnomAD constraint | pLI=3.8e-24, LOEUF=1.16 — LoF-tolerant |
| GWAS Catalog | 142 unique SNPs / 350 rows |
| ClinVar | 519 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 3214 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'MMP9' and resolved to 'Matrix metalloproteinase-9' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 519 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 60 traits by best p-value, aggregated from 75 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P14780 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000100985/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL321/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/MMP9 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/MMP9 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=MMP9%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/MMP9 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:51:06  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
