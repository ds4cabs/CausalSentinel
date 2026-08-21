# Protein Dossier — MFAP2 (Microfibrillar-associated protein 2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Forced vital capacity (FVC) | 0.11 | 0.0096 | 3.48e-30 | Wald ratio | 1 | cis | 0.931 |
| Forced expiratory volume in 1-second (FEV1) | 0.058 | 0.0101 | 1.02e-08 | Wald ratio | 1 | cis | 0.993 |
| Rheumatoid arthritis | 0.371 | 0.0802 | 3.63e-06 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | -0.0451 | 0.0117 | 1.15e-04 | Wald ratio | 1 | cis | NA |
| Ovarian cancer | 0.242 | 0.0648 | 1.82e-04 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | -0.0551 | 0.0151 | 2.68e-04 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I80 Phlebitis and thrombophlebitis | 0.402 | 0.116 | 5.57e-04 | Wald ratio | 1 | cis | NA |
| Weight | 0.034 | 0.0103 | 9.90e-04 | Wald ratio | 1 | cis | NA |
| High grade serous ovarian cancer | 0.219 | 0.077 | 0.00445 | Wald ratio | 1 | cis | NA |
| Potassium in urine | 0.0303 | 0.0119 | 0.0107 | Wald ratio | 1 | cis | NA |
| Schizophrenia | -0.131 | 0.0516 | 0.0113 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K57 Diverticular disease of intestine | 0.173 | 0.0696 | 0.0131 | Wald ratio | 1 | cis | NA |
| _...and 63 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_136 association rows across 65 traits (131 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Height | 1e-300 | rs9435734 | 21 | GCST90245843 | no MR -> candidate analysis |
| Height (maximum, inv-normal transformed) | 6e-296 | rs55750792 | 2 | GCST90475359 | no MR -> candidate analysis |
| Standing height (UKB data field 50) | 2e-129 | rs9435731 | 1 | GCST90468178 | no MR -> candidate analysis |
| Height (baseline) | 3e-97 | rs9435731 | 1 | GCST90565843 | no MR -> candidate analysis |
| height (mean, inv-normal transformed) | 7e-84 | rs55750792 | 1 | GCST90479635 | no MR -> candidate analysis |
| height (minimum, inv-normal transformed) | 2e-80 | rs55750792 | 1 | GCST90479636 | no MR -> candidate analysis |
| Body shape phenotype PC2 | 3e-77 | rs9435731 | 1 | GCST90832990 | no MR -> candidate analysis |
| Lung function (FEV1/FVC) | 7e-76 | rs3754512 | 4 | GCST007080 | no MR -> candidate analysis |
| FEV1/FVC ratio | 2e-75 | rs2284746 | 1 | GCST90705072 | no MR -> candidate analysis |
| DKK3/LTBP2 protein level ratio | 9e-59 | rs9435731 | 1 | GCST90314487 | no MR -> candidate analysis |
| FEV1 FVC ratio Z score (UKB data field 20258) | 9e-59 | rs2284746 | 1 | GCST90468165 | no MR -> candidate analysis |
| FVC | 4e-51 | rs9435731 | 2 | GCST90270083 | MR: beta=0.11, p=3.48e-30 (cis) |
| _...and 53 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 258 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Abnormality of the skeletal system | 0.887 | — | common-variant locus | no MR -> candidate analysis |
| smoking behavior | 0.607 | — | common-variant locus | no MR -> candidate analysis |
| Varicose veins | 0.594 | — | common-variant locus | MR: beta=0.154, p=0.0293 (cis) |
| ovarian cancer | 0.445 | — | established (curated) | MR: beta=0.242, p=1.82e-04 (cis) |
| pulmonary tuberculosis | 0.511 | — | common-variant locus | no MR -> candidate analysis |
| gastroesophageal reflux disease | 0.443 | — | common-variant locus | no MR -> candidate analysis |
| lymphatic system disorder | 0.318 | — | common-variant locus | no MR -> candidate analysis |
| vein disorder | 0.318 | — | common-variant locus | no MR -> candidate analysis |
| chronic obstructive pulmonary disease | 0.294 | — | common-variant locus | no MR -> candidate analysis |
| obesity disorder | 0.035 | — | common-variant locus | no MR -> candidate analysis |

> Of the 10 rows above, **8 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1.1e-06, LOEUF=1.07 — LoF-tolerant |
| GWAS Catalog | 86 unique SNPs / 172 rows |
| ClinVar | 66 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 258 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'MFAP2'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 66 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 65 traits by best p-value, aggregated from 136 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P55001 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000117122/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/MFAP2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/MFAP2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=MFAP2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/MFAP2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:46:41  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
