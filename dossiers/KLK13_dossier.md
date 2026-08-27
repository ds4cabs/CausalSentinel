# Protein Dossier — KLK13 (Kallikrein-13)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Years of schooling | 0.0309 | 0.0103 | 0.0027 | Wald ratio | 1 | cis | NA |
| Serum cystatin C (eGFRcys) | 0.0149 | 0.00567 | 0.00838 | Wald ratio | 1 | cis | NA |
| Alzheimer's disease | -0.112 | 0.0438 | 0.0107 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R07 Pain in throat and chest | -0.0743 | 0.0312 | 0.0171 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I83 Varicose veins of lower extremities | 0.0959 | 0.0412 | 0.0199 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: H25 Senile cataract | 0.137 | 0.0647 | 0.0346 | Wald ratio | 1 | cis | NA |
| Neo-agreeableness | -0.356 | 0.176 | 0.0424 | Wald ratio | 1 | cis | NA |
| Lung adenocarcinoma | -0.149 | 0.0774 | 0.0542 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N81 Female genital prolapse | 0.0944 | 0.0494 | 0.056 | Wald ratio | 1 | cis | NA |
| Coronary heart disease | 0.0481 | 0.0263 | 0.0667 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: bladder problem (not cancer) | -0.184 | 0.103 | 0.0753 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: pernicious anaemia | 0.178 | 0.101 | 0.0786 | Wald ratio | 1 | cis | NA |
| _...and 74 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3200_49_2` | kallikrein 13 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_60 association rows across 23 traits (60 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating KLK12 levels | 6e-2130 | rs62117666 | 5 | GCST90860580 | no MR -> candidate analysis |
| Circulating KLK13 levels | 3e-1112 | rs3760739 | 4 | GCST90860002 | no MR -> candidate analysis |
| Kallikrein-13 levels | 3e-189 | rs2569459 | 5 | GCST90248158 | no MR -> candidate analysis |
| KLK12 protein levels | 2e-182 | rs77342236 | 11 | GCST90469698 | no MR -> candidate analysis |
| KLK13 protein levels | 2e-110 | rs7253072 | 5 | GCST90469699 | no MR -> candidate analysis |
| Circulating KLK10 levels | 8e-101 | rs3760744 | 1 | GCST90860356 | no MR -> candidate analysis |
| KLK14 protein levels | 2e-96 | rs2569459 | 4 | GCST90469700 | no MR -> candidate analysis |
| Serum levels of protein KLK13 | 1e-79 | rs2569459 | 3 | GCST90086572 | no MR -> candidate analysis |
| Blood protein levels | 4e-54 | rs3760739 | 2 | GCST006585 | no MR -> candidate analysis |
| Kallikrein-12 levels | 5e-50 | rs8103941 | 3 | GCST90101221 | no MR -> candidate analysis |
| Kallikrein-13 (analyte X11152.46) levels | 2e-48 | rs34089525 | 1 | GCST90421334 | no MR -> candidate analysis |
| Circulating KLK14 levels | 1e-44 | rs8103083 | 1 | GCST90860034 | no MR -> candidate analysis |
| _...and 11 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 309 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| actinic keratosis | 0.275 | — | common-variant locus | no MR -> candidate analysis |

> Of the 1 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Kallikrein-13) |
| gnomAD constraint | pLI=2.2e-06, LOEUF=1.24 — LoF-tolerant |
| GWAS Catalog | 199 unique SNPs / 474 rows |
| ClinVar | 76 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 309 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'KLK13' and resolved to 'Kallikrein-13' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 76 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 23 traits by best p-value, aggregated from 60 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9UKR3 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000167759/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4863/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/KLK13 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/KLK13 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=KLK13%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/KLK13 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:23:47  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
