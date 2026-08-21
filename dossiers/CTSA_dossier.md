# Protein Dossier — CTSA (Lysosomal protective protein)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Mean platelet volume | -0.0762 | 0.00644 | 3.14e-32 | Wald ratio | 1 | trans | NA |
| Triglycerides | -0.161 | 0.0193 | 1.01e-16 | Wald ratio | 1 | trans | 0.989 |
| Platelet count | 19.3 | 2.43 | 1.79e-15 | Wald ratio | 1 | trans | 0.65 |
| Diastolic blood pressure  automated reading | -0.0939 | 0.0144 | 7.83e-11 | Wald ratio | 1 | trans | 0.157 |
| HDL cholesterol | 0.114 | 0.0199 | 1.16e-08 | Wald ratio | 1 | trans | 0.967 |
| Sodium in urine | -0.0748 | 0.0139 | 7.01e-08 | Wald ratio | 1 | trans | 0.899 |
| Body mass index (BMI) | -0.0747 | 0.0141 | 1.18e-07 | Wald ratio | 1 | trans | 0.111 |
| Non-cancer illness code  self-reported: hypertension | -0.124 | 0.0273 | 5.28e-06 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: deep venous thrombosis (dvt) | 0.33 | 0.0724 | 5.28e-06 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: K80 Cholelithiasis | 0.32 | 0.0718 | 8.32e-06 | Wald ratio | 1 | trans | NA |
| Height | 0.0703 | 0.0176 | 6.33e-05 | Wald ratio | 1 | trans | NA |
| Creatinine (enzymatic) in urine | -0.0524 | 0.0135 | 1.03e-04 | Wald ratio | 1 | trans | NA |
| _...and 118 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3179_51_2` | Cathepsin A | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_2 association rows across 2 traits (2 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Lysosomal protective protein levels | 1e-8 | rs2075962 | 1 | GCST90425637 | no MR -> candidate analysis |
| Body shape phenotype PC2 | 3e-8 | rs6104390 | 1 | GCST90832990 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1827 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| galactosialidosis | 0.922 | — | established (curated) | no MR -> candidate analysis |
| cathepsin a-related arteriopathy-strokes-leukoencephalopathy | 0.486 | — | established (curated) | no MR -> candidate analysis |
| hereditary disease | 0.742 | — | established (curated) | no MR -> candidate analysis |
| Lynch syndrome | 0.559 | — | established (curated) | no MR -> candidate analysis |
| Non-immune hydrops fetalis | 0.438 | — | established (curated) | no MR -> candidate analysis |
| Abnormality of prenatal development or birth | 0.438 | — | established (curated) | no MR -> candidate analysis |
| coronary artery disorder | 0.276 | — | common-variant locus | no MR -> candidate analysis |
| prostate carcinoma | 0.201 | — | common-variant locus | no MR -> candidate analysis |
| breast carcinoma | 0.201 | — | common-variant locus | no MR -> candidate analysis |
| ovarian dysfunction | 0.18 | — | common-variant locus | no MR -> candidate analysis |
| macular degeneration | 0.148 | — | common-variant locus | no MR -> candidate analysis |
| abdominal aortic aneurysm | 0.102 | — | common-variant locus | no MR -> candidate analysis |
| familial hyperlipidemia | 0.103 | — | common-variant locus | no MR -> candidate analysis |

> Of the 13 rows above, **13 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Lysosomal protective protein) |
| gnomAD constraint | pLI=6.1e-09, LOEUF=0.815 — LoF-tolerant |
| GWAS Catalog | 122 unique SNPs / 294 rows |
| ClinVar | 635 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1827 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'CTSA' and resolved to 'Lysosomal protective protein' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 635 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 2 of 2 traits by best p-value, aggregated from 2 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P10619 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000064601/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL6115/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CTSA — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CTSA — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CTSA%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CTSA — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:10:03  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
