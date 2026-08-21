# Protein Dossier — RELT (Tumor necrosis factor receptor superfamily member 19L)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Forced expiratory volume in 1-second (FEV1) | 0.0316 | 0.00617 | 3.01e-07 | Wald ratio | 1 | cis | 0.667 |
| Diastolic blood pressure  automated reading | -0.0313 | 0.00731 | 1.87e-05 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N81 Female genital prolapse | 0.204 | 0.0487 | 2.73e-05 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: vaginal prolapse or uterine prolapse | 0.261 | 0.075 | 5.03e-04 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | 0.0197 | 0.00585 | 7.72e-04 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | -0.0221 | 0.00714 | 0.00198 | Wald ratio | 1 | cis | NA |
| Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | 0.0538 | 0.0184 | 0.00349 | Wald ratio | 1 | cis | NA |
| Potassium in urine | -0.0202 | 0.00725 | 0.00529 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R11 Nausea and vomiting | 0.249 | 0.0894 | 0.00531 | Wald ratio | 1 | cis | NA |
| Creatinine (enzymatic) in urine | -0.019 | 0.00683 | 0.00542 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertension | -0.0337 | 0.0126 | 0.00737 | Wald ratio | 1 | cis | NA |
| Weight | -0.0165 | 0.0063 | 0.00873 | Wald ratio | 1 | cis | NA |
| _...and 103 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-5115_31_3` | RELT | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_4 association rows across 4 traits (4 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating RELT levels | 5e-690 | rs56801796 | 1 | GCST90860670 | no MR -> candidate analysis |
| RELT protein levels | 1e-39 | rs151264098 | 1 | GCST90470453 | no MR -> candidate analysis |
| Blood protein levels | 2e-33 | rs7118982 | 1 | GCST006585 | no MR -> candidate analysis |
| Tumor necrosis factor receptor superfamily member 19L levels | 5e-31 | rs56801796 | 1 | GCST90137740 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 128 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| amelogenesis imperfecta | 0.818 | — | established (curated) | no MR -> candidate analysis |
| hypocalcified amelogenesis imperfecta | 0.608 | — | established (curated) | no MR -> candidate analysis |
| Pain | 0.467 | — | common-variant locus | MR: beta=0.0755, p=0.0183 (cis) |
| diverticular disease | 0.409 | — | common-variant locus | MR: beta=0.0523, p=0.274 (cis) |
| pernicious anemia | 0.395 | — | common-variant locus | no MR -> candidate analysis |
| Varicose veins | 0.325 | — | common-variant locus | no MR -> candidate analysis |
| vein disorder | 0.322 | — | common-variant locus | no MR -> candidate analysis |
| lymphatic system disorder | 0.322 | — | common-variant locus | no MR -> candidate analysis |
| Crohn disease | 0.321 | — | common-variant locus | no MR -> candidate analysis |
| hereditary disease | 0.317 | — | established (curated) | no MR -> candidate analysis |
| Abnormality of refraction | 0.155 | — | common-variant locus | no MR -> candidate analysis |

> Of the 11 rows above, **9 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1.1e-09, LOEUF=0.953 — LoF-tolerant |
| GWAS Catalog | 33 unique SNPs / 66 rows |
| ClinVar | 116 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 128 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'RELT'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 116 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 4 of 4 traits by best p-value, aggregated from 4 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q969Z4 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000054967/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/RELT — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/RELT — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=RELT%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/RELT — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:47:44  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
