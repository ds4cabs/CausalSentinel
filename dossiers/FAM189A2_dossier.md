# Protein Dossier — FAM189A2 (Endosomal transmembrane epsin interactor 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: R14 Flatulence and related conditions | 0.529 | 0.152 | 5.28e-04 | Inverse variance weighted | 2 | trans | NA |
| Diagnoses - main ICD10: R14 Flatulence and related conditions | 0.529 | 0.152 | 5.28e-04 | Inverse variance weighted | 2 | trans | NA |
| Diagnoses - main ICD10: D12 Benign neoplasm of colon  rectum  anus and anal canal | 0.132 | 0.0449 | 0.00335 | Inverse variance weighted | 2 | trans | NA |
| Diagnoses - main ICD10: D12 Benign neoplasm of colon  rectum  anus and anal canal | 0.132 | 0.0449 | 0.00335 | Inverse variance weighted | 2 | trans | NA |
| Potassium in urine | -0.0175 | 0.00614 | 0.00433 | Inverse variance weighted | 2 | trans | NA |
| Potassium in urine | -0.0175 | 0.00614 | 0.00433 | Inverse variance weighted | 2 | trans | NA |
| Alcohol intake frequency | 0.0243 | 0.00895 | 0.00655 | Inverse variance weighted | 2 | trans | NA |
| Alcohol intake frequency | 0.0243 | 0.00895 | 0.00655 | Inverse variance weighted | 2 | trans | NA |
| Diagnoses - main ICD10: C50 Malignant neoplasm of breast | -0.139 | 0.0545 | 0.0107 | Inverse variance weighted | 2 | trans | NA |
| Diagnoses - main ICD10: C50 Malignant neoplasm of breast | -0.139 | 0.0545 | 0.0107 | Inverse variance weighted | 2 | trans | NA |
| Schizophrenia | -0.0568 | 0.0257 | 0.027 | Inverse variance weighted | 2 | trans | NA |
| Schizophrenia | -0.0568 | 0.0257 | 0.027 | Inverse variance weighted | 2 | trans | NA |
| _...and 167 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_No GWAS Catalog associations mapped to this gene._

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 66 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| atrial fibrillation | 0.576 | — | common-variant locus | no MR -> candidate analysis |
| benign prostatic hyperplasia | 0.484 | — | common-variant locus | no MR -> candidate analysis |
| dislocation | 0.44 | — | common-variant locus | no MR -> candidate analysis |
| inflammatory bowel disease | 0.44 | — | common-variant locus | no MR -> candidate analysis |
| systemic lupus erythematosus | 0.164 | — | common-variant locus | no MR -> candidate analysis |
| intelligence | 0.123 | — | common-variant locus | MR: beta=0.0524, p=0.108 (trans) |
| connective tissue disorder | 0.094 | — | common-variant locus | no MR -> candidate analysis |
| schizophrenia | 0.078 | — | common-variant locus | MR: beta=-0.0568, p=0.027 (trans) |
| mathematical ability | 0.073 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.039 | — | common-variant locus | no MR -> candidate analysis |
| urolithiasis | 0.039 | — | common-variant locus | no MR -> candidate analysis |
| drug allergy | 0.038 | — | common-variant locus | no MR -> candidate analysis |

> Of the 12 rows above, **10 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | not available |
| GWAS Catalog | 1 unique SNPs / 2 rows |
| ClinVar | 1 records; 0 pathogenic in sample of 1 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 66 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'FAM189A2'.
- **`gnomad`** — No gnomAD constraint data.
- **`clinvar`** — Pathogenic count is over the 1 record(s) retrieved, NOT over all 1 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — No GWAS Catalog associations mapped to this gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q15884 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000135063/associations — _Open Targets data release 26.06_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/FAM189A2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=FAM189A2%5Bgene%5D — _ClinVar build Build260809-1055.1_

## Provenance

- Generated: 2026-08-14T02:34:07  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
