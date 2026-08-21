# Protein Dossier — CRLF1 (Cytokine receptor-like factor 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Potassium in urine | 0.0382 | 0.0105 | 2.87e-04 | Wald ratio | 1 | cis | NA |
| Age at menarche | 0.0699 | 0.0248 | 0.0048 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertension | -0.0521 | 0.0186 | 0.00517 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R10 Abdominal and pelvic pain | -0.157 | 0.0588 | 0.0077 | Wald ratio | 1 | cis | NA |
| Hirschsprung's disease | -1.22 | 0.473 | 0.00981 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: small intestine or small bowel cancer | 0.651 | 0.28 | 0.0199 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hayfever or allergic rhinitis | -0.106 | 0.0475 | 0.0253 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | 0.222 | 0.1 | 0.0263 | Wald ratio | 1 | cis | NA |
| HDL cholesterol | 0.0469 | 0.0213 | 0.028 | Wald ratio | 1 | cis | NA |
| Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.0629 | 0.029 | 0.0301 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: J33 Nasal polyp | 0.253 | 0.119 | 0.0332 | Wald ratio | 1 | cis | NA |
| ER-positive Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.0734 | 0.035 | 0.0357 | Wald ratio | 1 | cis | NA |
| _...and 104 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2607_54_2` | CLF-1/CLC Complex | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_14 association rows across 12 traits (13 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Serum levels of protein CRLF1 | 1e-34 | rs2238647 | 1 | GCST90087917 | no MR -> candidate analysis |
| COMP protein levels | 1e-23 | rs72995446 | 1 | GCST90468827 | no MR -> candidate analysis |
| Blood protein levels | 1e-22 | rs2238647 | 1 | GCST006585 | no MR -> candidate analysis |
| Mouth ulcers | 1e-20 | rs144474740 | 1 | GCST007839 | no MR -> candidate analysis |
| Smoking initiation | 8e-11 | rs4808821 | 1 | GCST90243968 | no MR -> candidate analysis |
| Spine osteoarthritis | 1e-9 | rs117943325 | 1 | GCST90566801 | no MR -> candidate analysis |
| Neutrophil-to-lymphocyte ratio | 2e-9 | rs4808822 | 2 | GCST90866310 | no MR -> candidate analysis |
| Post-traumatic stress disorder symptom severity (total) | 3e-9 | rs2314662 | 2 | GCST90271779 | no MR -> candidate analysis |
| Post-traumatic stress disorder symptom severity (avoidance) | 3e-9 | rs2314662 | 1 | GCST90271780 | no MR -> candidate analysis |
| ICD10 K22.1: Ulcer of esophagus | 2e-8 | rs79286782 | 1 | GCST90432131 | no MR -> candidate analysis |
| Total fatty acid levels | 3e-8 | rs117943325 | 1 | GCST90502711 | no MR -> candidate analysis |
| Height | 3e-7 | rs4808822 | 1 | GCST90245848 | MR: beta=0.0154, p=0.234 (cis) |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 141 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Cold-induced sweating syndrome 1 | 0.948 | — | established (curated) | no MR -> candidate analysis |
| cold-induced sweating syndrome | 0.717 | — | established (curated) | no MR -> candidate analysis |
| Crisponi syndrome | 0.608 | — | established (curated) | no MR -> candidate analysis |
| spinal stenosis | 0.693 | — | common-variant locus | no MR -> candidate analysis |
| hereditary disease | 0.682 | — | established (curated) | no MR -> candidate analysis |
| dentures | 0.478 | — | common-variant locus | no MR -> candidate analysis |
| cone-rod dystrophy 12 | 0.438 | — | established (curated) | no MR -> candidate analysis |
| esophageal disorder | 0.425 | — | common-variant locus | no MR -> candidate analysis |
| diaphragmatic hernia | 0.363 | — | common-variant locus | MR: beta=-0.135, p=0.161 (cis) |
| cholelithiasis | 0.242 | — | common-variant locus | MR: beta=0.073, p=0.279 (cis) |
| Barrett esophagus | 0.1 | — | common-variant locus | no MR -> candidate analysis |
| gastroesophageal reflux disease | 0.082 | — | common-variant locus | no MR -> candidate analysis |
| Hiatus hernia | 0.07 | — | common-variant locus | MR: beta=-0.155, p=0.0524 (cis) |
| Hernia | 0.07 | — | common-variant locus | MR: beta=-0.155, p=0.0524 (cis) |
| osteoarthritis, spine | 0.052 | — | common-variant locus | no MR -> candidate analysis |

> Of the 15 rows above, **11 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1.3e-09, LOEUF=0.972 — LoF-tolerant |
| GWAS Catalog | 108 unique SNPs / 210 rows |
| ClinVar | 256 records; 3 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 141 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'CRLF1'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 256 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 12 of 12 traits by best p-value, aggregated from 14 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O75462 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000006016/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CRLF1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CRLF1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CRLF1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CRLF1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:03:58  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
