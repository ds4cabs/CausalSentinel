# Protein Dossier — PMEL (Melanocyte protein PMEL)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: asthma | 0.163 | 0.0333 | 1.01e-06 | Wald ratio | 1 | trans | NA |
| Weight | 0.0498 | 0.0124 | 5.52e-05 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: vitiligo | 1.12 | 0.31 | 3.24e-04 | Wald ratio | 1 | trans | NA |
| Forced vital capacity (FVC) | 0.041 | 0.0115 | 3.58e-04 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: N92 Excessive  frequent and irregular menstruation | 0.22 | 0.0788 | 0.00526 | Wald ratio | 1 | trans | NA |
| Forced expiratory volume in 1-second (FEV1) | 0.0323 | 0.0121 | 0.00767 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: D25 Leiomyoma of uterus | 0.254 | 0.0969 | 0.00869 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: emphysema or chronic bronchitis | 0.245 | 0.0958 | 0.0106 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | 0.133 | 0.0546 | 0.0146 | Wald ratio | 1 | trans | NA |
| Myocardial infarction | 0.205 | 0.0897 | 0.0225 | Wald ratio | 1 | trans | NA |
| Heel bone mineral density (BMD) T-score  automated | 0.0384 | 0.018 | 0.0331 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: M17 Gonarthrosis [arthrosis of knee] | -0.293 | 0.138 | 0.0344 | Wald ratio | 1 | trans | NA |
| _...and 64 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_9 association rows across 9 traits (9 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Melanocyte protein PMEL levels | 5e-27 | rs2069398 | 1 | GCST90249044 | no MR -> candidate analysis |
| Serum levels of protein PMEL | 4e-22 | rs12309895 | 1 | GCST90089451 | no MR -> candidate analysis |
| Whole body water mass (UKB data field 23102) | 4e-17 | rs2069408 | 1 | GCST90468184 | no MR -> candidate analysis |
| Basal metabolic rate (UKB data field 23105) | 2e-16 | rs2069408 | 1 | GCST90468159 | no MR -> candidate analysis |
| Blood protein levels | 2e-13 | rs3213122 | 1 | GCST006585 | no MR -> candidate analysis |
| Whole body fat free mass (UKB data field 23101) | 2e-11 | rs2069408 | 1 | GCST90428120 | no MR -> candidate analysis |
| Circulating DNER levels | 4e-11 | rs2069408 | 1 | GCST90860417 | no MR -> candidate analysis |
| Asthma | 1e-10 | rs2069408 | 1 | GCST001183 | MR: beta=0.163, p=1.01e-06 (trans) |
| Refractive error | 8e-10 | rs2069408 | 1 | GCST90841196 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 851 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| autoimmune disease | 0.142 | — | common-variant locus | no MR -> candidate analysis |

> Of the 1 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 2 known modulators (Melanocyte protein PMEL) |
| gnomAD constraint | pLI=3e-15, LOEUF=1.03 — LoF-tolerant |
| GWAS Catalog | 61 unique SNPs / 120 rows |
| ClinVar | 104 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 851 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'PMEL' and resolved to 'Melanocyte protein PMEL' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 104 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 9 of 9 traits by best p-value, aggregated from 9 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P40967 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000185664/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3712988/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PMEL — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PMEL — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PMEL%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/PMEL — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:28:16  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
