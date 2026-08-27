# Protein Dossier — C6orf89 (Bombesin receptor-activated protein C6orf89)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Alcohol intake frequency | -0.0359 | 0.0159 | 0.0238 | Wald ratio | 1 | trans | NA |
| Primary sclerosing cholangitis  | -0.341 | 0.155 | 0.0275 | Wald ratio | 1 | trans | NA |
| Sodium in urine | -0.0228 | 0.0106 | 0.0306 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: sleep apnoea | 0.312 | 0.145 | 0.032 | Wald ratio | 1 | trans | NA |
| Systolic blood pressure  automated reading | 0.0222 | 0.011 | 0.0436 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: G47 Sleep disorders | 0.227 | 0.113 | 0.0455 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: N92 Excessive  frequent and irregular menstruation | -0.167 | 0.0892 | 0.0611 | Wald ratio | 1 | trans | NA |
| Cancer code  self-reported: prostate cancer | -0.33 | 0.182 | 0.0696 | Wald ratio | 1 | trans | NA |
| Eye problems or disorders: Glaucoma | 0.142 | 0.0782 | 0.0696 | Wald ratio | 1 | trans | NA |
| Squamous cell lung cancer | -0.247 | 0.136 | 0.0701 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: C61 Malignant neoplasm of prostate | -0.354 | 0.197 | 0.0719 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: I84 Haemorrhoids | 0.106 | 0.0623 | 0.0879 | Wald ratio | 1 | trans | NA |
| _...and 65 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_15 association rows across 13 traits (8 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| PI16 protein levels | 3e-58 | rs113960910 | 2 | GCST90470229 | no MR -> candidate analysis |
| Serum levels of protein PPIL1 | 3e-46 | rs144656078 | 1 | GCST90090885 | no MR -> candidate analysis |
| Cerebrospinal fluid protein PI16 levels | 8e-24 | rs12203354 | 1 | GCST90945032 | no MR -> candidate analysis |
| MSMB protein levels | 2e-14 | rs67854134 | 1 | GCST90469949 | no MR -> candidate analysis |
| Circulating MSMB levels | 1e-13 | rs6920322 | 1 | GCST90860651 | no MR -> candidate analysis |
| Hypothyroidism | 3e-12 | rs79809702 | 1 | GCST90627749 | no MR -> candidate analysis |
| Type 2 diabetes | 7e-10 | rs72846863 | 2 | GCST90492734 | MR: beta=-0.11, p=0.486 (trans) |
| Heel bone mineral density | 1e-7 | rs9357229 | 1 | GCST007066 | no MR -> candidate analysis |
| Schizophrenia, bipolar disorder or recurrent major depressiv | 4e-6 | rs1543274 | 1 | GCST012293 | no MR -> candidate analysis |
| Schizophrenia, bipolar disorder or major depressive disorder | 4e-6 | rs1543274 | 1 | GCST012299 | no MR -> candidate analysis |
| Performance intelligence quotient (cesarean section interact | 7e-6 | rs4714020 | 1 | GCST007404 | no MR -> candidate analysis |
| Schizophrenia x sex interaction | 7e-6 | rs1543274 | 1 | GCST012310 | no MR -> candidate analysis |
| _...and 1 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 29 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| pontocerebellar hypoplasia, type 14 | 0.438 | — | established (curated) | no MR -> candidate analysis |
| hemorrhage | 0.287 | — | common-variant locus | no MR -> candidate analysis |
| complication | 0.287 | — | common-variant locus | no MR -> candidate analysis |
| hereditary disease | 0.243 | — | established (curated) | no MR -> candidate analysis |
| diverticular disease | 0.055 | — | common-variant locus | MR: beta=-0.147, p=0.0954 (trans) |
| hypothyroidism | 0.041 | — | common-variant locus | no MR -> candidate analysis |
| major depressive disorder | 0.033 | — | common-variant locus | no MR -> candidate analysis |

> Of the 7 rows above, **6 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1.2e-07, LOEUF=0.972 — LoF-tolerant |
| GWAS Catalog | 73 unique SNPs / 146 rows |
| ClinVar | 39 records; 4 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 29 of 29 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'C6orf89'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 39 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 13 of 13 traits by best p-value, aggregated from 15 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q6UWU4 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000198663/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/C6orf89 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/C6orf89 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=C6orf89%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/C6orf89 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:22:57  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
