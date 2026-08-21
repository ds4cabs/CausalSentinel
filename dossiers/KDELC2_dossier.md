# Protein Dossier — KDELC2 (Protein O-glucosyltransferase 3)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: uterine fibroids | -0.398 | 0.0686 | 6.85e-09 | Wald ratio | 1 | cis | 0.99 |
| Diagnoses - main ICD10: D25 Leiomyoma of uterus | -0.37 | 0.073 | 3.90e-07 | Wald ratio | 1 | cis | NA |
| ER-negative Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | 0.152 | 0.0322 | 2.29e-06 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: prostate cancer | -0.303 | 0.0908 | 8.50e-04 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: chronic obstructive airways disease or copd | 0.25 | 0.0762 | 0.00104 | Wald ratio | 1 | cis | NA |
| Primary sclerosing cholangitis  | -0.235 | 0.0792 | 0.00297 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hiatus hernia | 0.0956 | 0.0339 | 0.0048 | Wald ratio | 1 | cis | NA |
| Diastolic blood pressure  automated reading | -0.0163 | 0.00579 | 0.00493 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: D12 Benign neoplasm of colon  rectum  anus and anal canal | -0.153 | 0.0561 | 0.00633 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: C61 Malignant neoplasm of prostate | -0.237 | 0.0891 | 0.00782 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: malignant melanoma | -0.199 | 0.0792 | 0.0119 | Wald ratio | 1 | cis | NA |
| High grade serous ovarian cancer | 0.0976 | 0.0407 | 0.0166 | Wald ratio | 1 | cis | NA |
| _...and 75 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_No GWAS Catalog associations mapped to this gene._

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 93 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Abnormality of the skeletal system | 0.867 | — | common-variant locus | no MR -> candidate analysis |
| prostate carcinoma | 0.818 | — | common-variant locus | no MR -> candidate analysis |
| uterine corpus leiomyoma | 0.81 | — | common-variant locus | no MR -> candidate analysis |
| Uterine leiomyoma | 0.723 | — | common-variant locus | no MR -> candidate analysis |
| clonal hematopoiesis | 0.662 | — | common-variant locus | no MR -> candidate analysis |
| renal carcinoma | 0.644 | — | common-variant locus | no MR -> candidate analysis |
| benign colon neoplasm | 0.58 | — | common-variant locus | MR: beta=-0.153, p=0.00633 (cis) |
| cancer | 0.563 | — | common-variant locus | MR: beta=-0.398, p=6.85e-09 (cis) |
| renal cell carcinoma | 0.565 | — | common-variant locus | no MR -> candidate analysis |
| clear cell renal carcinoma | 0.568 | — | common-variant locus | no MR -> candidate analysis |
| prostate cancer | 0.538 | — | common-variant locus | MR: beta=-0.303, p=8.50e-04 (cis) |
| estrogen-receptor negative breast cancer | 0.487 | — | common-variant locus | no MR -> candidate analysis |
| hematopoietic and lymphoid cell neoplasm | 0.482 | — | common-variant locus | no MR -> candidate analysis |
| uterine benign neoplasm | 0.411 | — | common-variant locus | no MR -> candidate analysis |
| breast carcinoma | 0.373 | — | common-variant locus | no MR -> candidate analysis |

> Of the 15 rows above, **12 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | not available |
| GWAS Catalog | no mapped SNPs |
| ClinVar | no records |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 93 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'KDELC2'.
- **`gnomad`** — No gnomAD constraint data.
- **`gwas`** — No GWAS Catalog SNPs mapped to this gene.
- **`clinvar`** — No ClinVar records.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — No GWAS Catalog associations mapped to this gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q7Z4H8 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000178202/associations — _Open Targets data release 26.06_

## Provenance

- Generated: 2026-08-14T03:20:44  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
