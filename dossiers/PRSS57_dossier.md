# Protein Dossier — PRSS57 (Serine protease 57)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Eye problems or disorders: Diabetes related eye disease | 0.15 | 0.0488 | 0.00212 | Wald ratio | 1 | cis | NA |
| Serum creatinine (eGFRcrea) | 0.00451 | 0.00184 | 0.0141 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Cataract | 0.0551 | 0.0229 | 0.0159 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: osteoporosis | 0.0786 | 0.0328 | 0.0166 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K44 Diaphragmatic hernia | -0.0902 | 0.0388 | 0.02 | Wald ratio | 1 | cis | NA |
| Chronic kidney disease | -0.0684 | 0.0301 | 0.0227 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M16 Coxarthrosis [arthrosis of hip] | -0.0864 | 0.0402 | 0.0314 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K35 Acute appendicitis | 0.121 | 0.0564 | 0.0314 | Wald ratio | 1 | cis | NA |
| Pulse rate | -0.0163 | 0.00781 | 0.0373 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: pneumothorax | 0.331 | 0.16 | 0.0392 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M72 Fibroblastic disorders | -0.141 | 0.0696 | 0.0423 | Wald ratio | 1 | cis | NA |
| Alcohol intake frequency | -0.0128 | 0.00653 | 0.0491 | Wald ratio | 1 | cis | NA |
| _...and 81 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_13 association rows across 12 traits (12 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Serine protease 57 levels | 2e-338 | rs9304936 | 2 | GCST90249623 | no MR -> candidate analysis |
| Bone mineral density mean | 1e-300 | rs36098180 | 1 | GCST90321120 | no MR -> candidate analysis |
| Serum levels of protein PRSS57 | 2e-226 | rs9304936 | 1 | GCST90090145 | no MR -> candidate analysis |
| Blood protein levels | 7e-107 | rs9304936 | 1 | GCST006585 | no MR -> candidate analysis |
| Circulating FSTL3 levels | 3e-35 | rs112418024 | 1 | GCST90860653 | no MR -> candidate analysis |
| FSTL3 protein levels | 6e-21 | rs564375277 | 1 | GCST90469272 | no MR -> candidate analysis |
| Cerebrospinal fluid protein FSTL3 levels | 4e-13 | rs8105856 | 1 | GCST90944313 | no MR -> candidate analysis |
| Follistatin-related protein 3 levels | 1e-12 | rs112418024 | 1 | GCST90247639 | no MR -> candidate analysis |
| Parathyroid hormone protein levels (SomaScan ID:8351-17) | 4e-12 | rs62131274 | 1 | GCST90438314 | no MR -> candidate analysis |
| Free Cholesterol to Cholesteryl Esters in Large HDL ratio | 7e-9 | rs111492798 | 1 | GCST90827800 | no MR -> candidate analysis |
| Forced vital capacity (FVC) | 7e-9 | rs138248777 | 1 | GCST90705071 | MR: beta=-0.00256, p=0.48 (cis) |
| Height | 6e-8 | rs2057714 | 1 | GCST90245848 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 55 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Graves disease | 0.136 | — | common-variant locus | no MR -> candidate analysis |
| nicotine dependence | 0.134 | — | common-variant locus | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=8e-07, LOEUF=1.35 — LoF-tolerant |
| GWAS Catalog | 77 unique SNPs / 153 rows |
| ClinVar | 121 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 55 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'PRSS57'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 121 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 12 of 12 traits by best p-value, aggregated from 13 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q6UWY2 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000185198/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PRSS57 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PRSS57 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PRSS57%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/PRSS57 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:38:19  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
