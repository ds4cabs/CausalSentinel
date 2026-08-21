# Protein Dossier — SCARF2 (Scavenger receptor class F member 2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Forced expiratory volume in 1-second (FEV1) | 0.0404 | 0.00878 | 4.14e-06 | Wald ratio | 1 | cis | NA |
| Fasting insulin | -0.04 | 0.0133 | 0.0027 | Wald ratio | 1 | cis | NA |
| Weight | 0.0258 | 0.00897 | 0.00397 | Wald ratio | 1 | cis | NA |
| Thyroid cancer | 1.13 | 0.41 | 0.00573 | Wald ratio | 1 | cis | NA |
| Vascular or heart problems diagnosed by doctor: Angina | 0.134 | 0.05 | 0.00749 | Wald ratio | 1 | cis | NA |
| Age at menarche | 0.0634 | 0.0246 | 0.01 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N40 Hyperplasia of prostate | 0.22 | 0.0856 | 0.0103 | Wald ratio | 1 | cis | NA |
| Height | 0.029 | 0.0127 | 0.0221 | Wald ratio | 1 | cis | NA |
| Schizophrenia | -0.103 | 0.0457 | 0.0241 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | 0.0293 | 0.0132 | 0.0259 | Wald ratio | 1 | cis | NA |
| Depressive symptoms | 0.0367 | 0.0167 | 0.0278 | Wald ratio | 1 | cis | NA |
| Melanoma | 0.477 | 0.229 | 0.037 | Wald ratio | 1 | cis | NA |
| _...and 107 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-5130_67_3` | SREC-II | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_47 association rows across 31 traits (46 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating SCARF2 levels | 1e-738 | rs9610955 | 4 | GCST90859705 | no MR -> candidate analysis |
| Height | 2e-144 | rs1477178 | 7 | GCST90245848 | MR: beta=0.029, p=0.0221 (cis) |
| Scavenger receptor class F member 2 levels | 4e-58 | rs738084 | 3 | GCST90249445 | no MR -> candidate analysis |
| SCARF2 protein levels | 2e-39 | rs12483784 | 2 | GCST90470537 | no MR -> candidate analysis |
| Cerebrospinal fluid protein SCARF2 levels | 1e-35 | rs738084 | 1 | GCST90944551 | no MR -> candidate analysis |
| FEV1/FVC ratio | 2e-32 | rs5763025 | 1 | GCST90705072 | no MR -> candidate analysis |
| Lung function (FEV1/FVC) | 2e-27 | rs5763025 | 3 | GCST90244094 | no MR -> candidate analysis |
| FEV1 FVC ratio Z score (UKB data field 20258) | 3e-24 | rs738084 | 1 | GCST90468165 | no MR -> candidate analysis |
| Height (baseline) | 2e-23 | rs12628193 | 3 | GCST90565843 | no MR -> candidate analysis |
| Standing height (UKB data field 50) | 2e-23 | rs874100 | 1 | GCST90468178 | no MR -> candidate analysis |
| Scavenger receptor class F member 2 levels (SCARF2.8956.96.3 | 5e-21 | rs738086 | 1 | GCST90242719 | no MR -> candidate analysis |
| Body shape phenotype PC2 | 7e-21 | rs12628193 | 1 | GCST90832990 | no MR -> candidate analysis |
| _...and 19 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 285 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| van den Ende-Gupta syndrome | 0.803 | — | established (curated) | no MR -> candidate analysis |
| Abnormality of the skeletal system | 0.895 | — | common-variant locus | no MR -> candidate analysis |
| open-angle glaucoma | 0.56 | — | common-variant locus | no MR -> candidate analysis |
| COVID-19 | 0.521 | — | common-variant locus | no MR -> candidate analysis |
| severe acute respiratory syndrome | 0.521 | — | common-variant locus | no MR -> candidate analysis |
| poisoning | 0.475 | — | common-variant locus | no MR -> candidate analysis |
| response to xenobiotic stimulus | 0.475 | — | common-variant locus | no MR -> candidate analysis |
| hereditary disease | 0.319 | — | established (curated) | no MR -> candidate analysis |
| microcephaly | 0.182 | — | established (curated) | no MR -> candidate analysis |

> Of the 9 rows above, **9 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=6.9e-06, LOEUF=0.694 — LoF-tolerant |
| GWAS Catalog | 45 unique SNPs / 90 rows |
| ClinVar | 684 records; 20 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 285 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'SCARF2'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 684 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 31 traits by best p-value, aggregated from 47 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q96GP6 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000244486/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/SCARF2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/SCARF2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=SCARF2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/SCARF2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:56:06  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
