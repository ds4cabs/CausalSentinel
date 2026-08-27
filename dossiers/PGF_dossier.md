# Protein Dossier — PGF (Placenta growth factor)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: M23 Internal derangement of knee | 0.153 | 0.0515 | 0.00302 | Wald ratio | 1 | trans | NA |
| Body mass index (BMI) | 0.0253 | 0.00889 | 0.00444 | Wald ratio | 1 | trans | NA |
| Lung cancer | -0.265 | 0.106 | 0.0126 | Wald ratio | 1 | trans | NA |
| Cough on most days | 0.0982 | 0.041 | 0.0166 | Wald ratio | 1 | trans | NA |
| High grade serous ovarian cancer | -0.161 | 0.0683 | 0.0182 | Wald ratio | 1 | trans | NA |
| Weight | 0.0185 | 0.00785 | 0.0187 | Wald ratio | 1 | trans | NA |
| Forced expiratory volume in 1-second (FEV1) | 0.0167 | 0.00769 | 0.0301 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: enlarged prostate | -0.188 | 0.0927 | 0.0424 | Wald ratio | 1 | trans | NA |
| Eye problems or disorders: Injury or trauma resulting in loss of vision | 0.191 | 0.0959 | 0.0467 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: R07 Pain in throat and chest | 0.0734 | 0.0369 | 0.0468 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: K80 Cholelithiasis | 0.109 | 0.0557 | 0.0494 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: K57 Diverticular disease of intestine | -0.14 | 0.0724 | 0.0528 | Wald ratio | 1 | trans | NA |
| _...and 67 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3078_1_2` | PlGF | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_38 association rows across 34 traits (36 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating PGF levels (id: OID00384_OID20673) | 2e-202 | rs6574205 | 1 | GCST90859746 | no MR -> candidate analysis |
| Circulating PGF levels (id: OID00762_OID20673) | 5e-158 | rs6574205 | 1 | GCST90860097 | no MR -> candidate analysis |
| Circulating PGF levels (id: OID01493_OID20673) | 1e-156 | rs6574205 | 1 | GCST90860674 | no MR -> candidate analysis |
| Cerebrospinal fluid protein ACYP1 levels | 4e-56 | rs144552657 | 1 | GCST90944089 | no MR -> candidate analysis |
| ENTPD5 protein levels | 5e-30 | rs573241313 | 1 | GCST90469121 | no MR -> candidate analysis |
| Alkaline phosphatase (UKB data field 30610) | 2e-21 | rs4903273 | 1 | GCST90468060 | no MR -> candidate analysis |
| Circulating COL1A1 levels | 1e-20 | rs2012627 | 1 | GCST90859986 | no MR -> candidate analysis |
| Septin-5 levels | 1e-19 | rs562158551 | 1 | GCST90423614 | no MR -> candidate analysis |
| Serum alkaline phosphatase levels | 2e-19 | rs10162358 | 3 | GCST90018942 | no MR -> candidate analysis |
| Unsupervised deep imaging phenotypes (UDIP-FA) | 1e-18 | rs10162358 | 1 | GCST90860937 | no MR -> candidate analysis |
| COL1A1 protein levels | 9e-15 | rs8005138 | 1 | GCST90468813 | no MR -> candidate analysis |
| Circulating WIF1 levels | 2e-14 | rs175035 | 1 | GCST90860083 | no MR -> candidate analysis |
| _...and 22 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 954 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| hypothyroidism | 0.546 | — | common-variant locus | no MR -> candidate analysis |
| acute pancreatitis | 0.459 | — | common-variant locus | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 3 known modulators (Placenta growth factor) |
| gnomAD constraint | pLI=0.18, LOEUF=0.72 — LoF-tolerant |
| GWAS Catalog | 88 unique SNPs / 176 rows |
| ClinVar | 56 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 954 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'PGF' and resolved to 'Placenta growth factor' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 56 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 34 traits by best p-value, aggregated from 38 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P49763 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000119630/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL1697671/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PGF — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PGF — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PGF%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/PGF — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:18:32  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
