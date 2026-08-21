# Protein Dossier — TMEM2 (Cell surface hyaluronidase CEMIP2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Eye problems or disorders: Glaucoma | 0.246 | 0.075 | 0.00104 | Wald ratio | 1 | trans | NA |
| Systolic blood pressure  automated reading | 0.0364 | 0.0117 | 0.00188 | Wald ratio | 1 | trans | NA |
| Fractured bone site(s): Wrist | 0.199 | 0.0673 | 0.00312 | Wald ratio | 1 | trans | NA |
| Mean cell haemoglobin concentration | 0.0482 | 0.0172 | 0.00494 | Wald ratio | 1 | trans | NA |
| Cough on most days | 0.142 | 0.0511 | 0.00562 | Wald ratio | 1 | trans | NA |
| ER-negative Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.135 | 0.0589 | 0.0219 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: G47 Sleep disorders | 0.263 | 0.117 | 0.0239 | Wald ratio | 1 | trans | NA |
| Small vessel disease | -0.379 | 0.17 | 0.026 | Wald ratio | 1 | trans | NA |
| Percent emphysema | -0.194 | 0.0909 | 0.033 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: M54 Dorsalgia | 0.16 | 0.0762 | 0.0356 | Wald ratio | 1 | trans | NA |
| Forearm bone mineral density | 0.15 | 0.0743 | 0.043 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: D25 Leiomyoma of uterus | 0.17 | 0.086 | 0.0479 | Wald ratio | 1 | trans | NA |
| _...and 92 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_No GWAS Catalog associations mapped to this gene._

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 124 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Inguinal hernia | 0.699 | — | established (curated) | no MR -> candidate analysis |
| Hypertelorism | 0.699 | — | established (curated) | no MR -> candidate analysis |
| myopia | 0.699 | — | established (curated) | no MR -> candidate analysis |
| Retinal dystrophy | 0.699 | — | established (curated) | no MR -> candidate analysis |
| Abnormal sternum morphology | 0.699 | — | established (curated) | no MR -> candidate analysis |
| Joint hypermobility | 0.699 | — | established (curated) | no MR -> candidate analysis |
| smoking initiation | 0.644 | — | common-variant locus | no MR -> candidate analysis |
| ventricular septal defect | 0.517 | — | common-variant locus | no MR -> candidate analysis |
| atherosclerosis | 0.509 | — | common-variant locus | no MR -> candidate analysis |
| substance abuse | 0.501 | — | common-variant locus | no MR -> candidate analysis |
| attention deficit-hyperactivity disorder | 0.501 | — | common-variant locus | no MR -> candidate analysis |
| rheumatoid arthritis | 0.482 | — | common-variant locus | no MR -> candidate analysis |
| eye disorder | 0.456 | — | common-variant locus | no MR -> candidate analysis |
| benign prostatic hyperplasia | 0.396 | — | common-variant locus | no MR -> candidate analysis |
| congenital heart disease | 0.285 | — | established (curated) | no MR -> candidate analysis |

> Of the 15 rows above, **15 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | not available |
| GWAS Catalog | no mapped SNPs |
| ClinVar | no records |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 124 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'TMEM2'.
- **`gnomad`** — No gnomAD constraint data.
- **`gwas`** — No GWAS Catalog SNPs mapped to this gene.
- **`clinvar`** — No ClinVar records.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — No GWAS Catalog associations mapped to this gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9UHN6 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000135048/associations — _Open Targets data release 26.06_

## Provenance

- Generated: 2026-08-14T05:24:40  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
