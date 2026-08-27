# Protein Dossier — EMC1 (ER membrane protein complex subunit 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Forced expiratory volume in 1-second (FEV1) | 0.0191 | 0.00641 | 0.00295 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: enlarged prostate | 0.159 | 0.0542 | 0.0034 | Wald ratio | 1 | trans | NA |
| Fasting glucose | 0.0309 | 0.0115 | 0.0073 | Wald ratio | 1 | trans | NA |
| Hearing difficulty or problems: Yes | -0.0338 | 0.0132 | 0.0106 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: bladder problem (not cancer) | 0.186 | 0.0813 | 0.0221 | Wald ratio | 1 | trans | NA |
| Birth length | 0.0713 | 0.0317 | 0.0246 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: Z09 Follow-up examination after treatment for conditions other than malignant neoplasms | -0.157 | 0.071 | 0.0268 | Wald ratio | 1 | trans | NA |
| Forced vital capacity (FVC) | 0.0132 | 0.00608 | 0.0302 | Wald ratio | 1 | trans | NA |
| Ferritin | -0.0629 | 0.0292 | 0.0313 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: C50 Malignant neoplasm of breast | 0.102 | 0.0525 | 0.0525 | Wald ratio | 1 | trans | NA |
| Transferrin | 0.0572 | 0.032 | 0.0735 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: migraine | 0.0711 | 0.0399 | 0.075 | Wald ratio | 1 | trans | NA |
| _...and 79 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_4 association rows across 4 traits (3 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Aflatoxin B1 aldehyde reductase member 3 levels | 5e-97 | rs12095284 | 1 | GCST90246404 | no MR -> candidate analysis |
| Serum alkaline phosphatase levels | 3e-13 | rs144713581 | 1 | GCST90018942 | no MR -> candidate analysis |
| Resistance to COVID-19 infection (Exposed negative vs positi | 3e-8 | rs61764877 | 1 | GCST90255358 | no MR -> candidate analysis |
| Brain structure | 1e-7 | rs710865 | 1 | GCST000597 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 87 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| cerebellar atrophy, visual impairment, and psychomotor retardation; | 0.892 | — | established (curated) | no MR -> candidate analysis |
| hereditary disease | 0.817 | — | established (curated) | no MR -> candidate analysis |
| Retinal dystrophy | 0.798 | — | established (curated) | no MR -> candidate analysis |
| Global developmental delay | 0.669 | — | established (curated) | no MR -> candidate analysis |
| Cerebellar atrophy | 0.669 | — | established (curated) | no MR -> candidate analysis |
| global developmental delay-visual anomalies-progressive cerebellar atrophy-truncal hypotonia syndrome | 0.608 | — | established (curated) | no MR -> candidate analysis |
| autosomal recessive retinitis pigmentosa | 0.547 | — | established (curated) | no MR -> candidate analysis |
| congenital anomaly of kidney and urinary tract | 0.438 | — | established (curated) | no MR -> candidate analysis |
| Obesity | 0.426 | — | established (curated) | no MR -> candidate analysis |
| retinitis pigmentosa | 0.195 | — | established (curated) | no MR -> candidate analysis |
| microcephaly | 0.182 | — | established (curated) | no MR -> candidate analysis |

> Of the 11 rows above, **11 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (ER membrane protein complex subunit 1) |
| gnomAD constraint | pLI=5.2e-28, LOEUF=0.942 — LoF-tolerant |
| GWAS Catalog | 34 unique SNPs / 68 rows |
| ClinVar | 1457 records; 4 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 87 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'EMC1' and resolved to 'ER membrane protein complex subunit 1' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 1457 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 4 of 4 traits by best p-value, aggregated from 4 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q8N766 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000127463/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL6067163/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/EMC1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/EMC1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=EMC1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/EMC1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:24:48  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
