# Protein Dossier — NLGN2 (Neuroligin-2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: R14 Flatulence and related conditions | 1.08 | 0.285 | 1.44e-04 | Wald ratio | 1 | cis | NA |
| Alcohol intake frequency | 0.0882 | 0.0271 | 0.00115 | Wald ratio | 1 | cis | NA |
| Glioma | -0.934 | 0.302 | 0.00202 | Wald ratio | 1 | cis | NA |
| Years of schooling | -0.0714 | 0.0238 | 0.0027 | Wald ratio | 1 | cis | NA |
| Anorexia nervosa | -0.659 | 0.223 | 0.00308 | Wald ratio | 1 | cis | NA |
| Height | -0.0516 | 0.021 | 0.0142 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: enlarged prostate | 0.284 | 0.12 | 0.0181 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R10 Abdominal and pelvic pain | 0.176 | 0.0749 | 0.0187 | Wald ratio | 1 | cis | NA |
| Lung cancer | -0.284 | 0.134 | 0.034 | Wald ratio | 1 | cis | NA |
| HbA1C | -0.0528 | 0.025 | 0.0348 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K57 Diverticular disease of intestine | 0.218 | 0.105 | 0.0383 | Wald ratio | 1 | cis | NA |
| Sleep duration | 0.0291 | 0.0143 | 0.0422 | Wald ratio | 1 | cis | NA |
| _...and 95 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_22 association rows across 13 traits (22 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Sex hormone-binding globulin levels | 1e-307 | rs35386490 | 5 | GCST90019518 | no MR -> candidate analysis |
| Testosterone levels | 7e-52 | rs35386490 | 2 | GCST90019520 | no MR -> candidate analysis |
| Neuroligin-2 levels | 2e-26 | rs114576150 | 1 | GCST90248690 | no MR -> candidate analysis |
| SHBG protein levels | 3e-26 | rs3174744 | 1 | GCST90470622 | no MR -> candidate analysis |
| Uterine fibroids | 2e-20 | rs72842813 | 3 | GCST90461958 | no MR -> candidate analysis |
| Serum alkaline phosphatase levels | 6e-20 | rs35386490 | 1 | GCST90019494 | no MR -> candidate analysis |
| Mean platelet thrombocyte volume (UKB data field 30100) | 2e-15 | rs2241233 | 1 | GCST90468087 | no MR -> candidate analysis |
| Serum levels of protein NLGN2 | 3e-14 | rs114576150 | 1 | GCST90090815 | no MR -> candidate analysis |
| Body fat percentage (adjusted for testosterone and SHBG) | 1e-13 | rs11078674 | 3 | GCST90432180 | no MR -> candidate analysis |
| Height (standard GWA) | 4e-12 | rs78355381 | 1 | GCST90267284 | no MR -> candidate analysis |
| Smoking cessation | 3e-10 | rs9900691 | 1 | GCST90243988 | no MR -> candidate analysis |
| Height (baseline) | 2e-9 | rs72842813 | 1 | GCST90565843 | no MR -> candidate analysis |
| _...and 1 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 119 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| seasonal allergic rhinitis | 0.215 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.215 | — | common-variant locus | no MR -> candidate analysis |
| autism | 0.195 | — | established (curated) | MR: beta=0.178, p=0.364 (cis) |
| nervous system benign neoplasm | 0.183 | — | common-variant locus | no MR -> candidate analysis |
| duodenal ulcer | 0.148 | — | common-variant locus | no MR -> candidate analysis |
| smoking cessation | 0.106 | — | common-variant locus | no MR -> candidate analysis |

> Of the 6 rows above, **5 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1, LOEUF=0.374 — LoF-INTOLERANT |
| GWAS Catalog | 148 unique SNPs / 348 rows |
| ClinVar | 303 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 119 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'NLGN2'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 303 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 13 of 13 traits by best p-value, aggregated from 22 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q8NFZ4 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000169992/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/NLGN2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/NLGN2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=NLGN2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/NLGN2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:59:21  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
