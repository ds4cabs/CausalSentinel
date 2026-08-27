# Protein Dossier — BMP6 (Bone morphogenetic protein 6)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: D12 Benign neoplasm of colon  rectum  anus and anal canal | 0.374 | 0.0811 | 3.90e-06 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: diverticular disease or diverticulitis | 0.329 | 0.0952 | 5.42e-04 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: Z09 Follow-up examination after treatment for conditions other than malignant neoplasms | 0.269 | 0.0869 | 0.00193 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: C50 Malignant neoplasm of breast | 0.216 | 0.088 | 0.014 | Wald ratio | 1 | trans | NA |
| Red blood cell count | 0.0358 | 0.0152 | 0.0188 | Wald ratio | 1 | trans | NA |
| Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | 0.0925 | 0.0404 | 0.0219 | Wald ratio | 1 | trans | NA |
| Mean cell haemoglobin concentration | -0.0503 | 0.0222 | 0.0232 | Wald ratio | 1 | trans | NA |
| Mean cell volume | -0.396 | 0.178 | 0.0257 | Wald ratio | 1 | trans | NA |
| Small vessel disease | 0.578 | 0.282 | 0.0406 | Wald ratio | 1 | trans | NA |
| Age at menopause | 0.277 | 0.138 | 0.0455 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: enlarged prostate | -0.332 | 0.171 | 0.0523 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: K80 Cholelithiasis | 0.157 | 0.0831 | 0.0583 | Wald ratio | 1 | trans | NA |
| _...and 81 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3736_60_3` | BMP-6 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_233 association rows across 107 traits (201 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Height | 1e-300 | rs3812163 | 43 | GCST90245843 | no MR -> candidate analysis |
| height (mean, inv-normal transformed) | 8e-300 | rs9392172 | 2 | GCST90475362 | no MR -> candidate analysis |
| height (minimum, inv-normal transformed) | 4e-274 | rs9392172 | 2 | GCST90475365 | no MR -> candidate analysis |
| Height (maximum, inv-normal transformed) | 3e-266 | rs9392172 | 2 | GCST90475359 | no MR -> candidate analysis |
| Standing height (UKB data field 50) | 1e-176 | rs3812163 | 5 | GCST90468178 | no MR -> candidate analysis |
| What is your height? (cm, inv-normal transformed) | 2e-143 | rs9392172 | 2 | GCST90475368 | no MR -> candidate analysis |
| Circulating BMP6 levels | 1e-123 | rs12198986 | 2 | GCST90859741 | no MR -> candidate analysis |
| Height (baseline) | 6e-122 | rs11243202 | 22 | GCST90565843 | no MR -> candidate analysis |
| Body shape phenotype PC2 | 2e-109 | rs11243202 | 2 | GCST90832990 | no MR -> candidate analysis |
| BMP6 protein levels | 2e-106 | rs12198986 | 2 | GCST90468454 | no MR -> candidate analysis |
| Appendicular lean mass | 3e-57 | rs11243202 | 2 | GCST90000025 | no MR -> candidate analysis |
| Height (standard GWA) | 2e-46 | rs7741360 | 1 | GCST90267284 | no MR -> candidate analysis |
| _...and 95 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 506 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Tangier disease | 0.919 | — | established (curated) | no MR -> candidate analysis |
| osteoarthritis, knee | 0.735 | — | common-variant locus | MR: beta=0.243, p=0.133 (trans) |
| Hernia | 0.663 | — | common-variant locus | MR: beta=0.142, p=0.144 (trans) |
| osteoarthritis, hip | 0.665 | — | common-variant locus | MR: beta=-0.199, p=0.205 (trans) |
| Abnormality of the skeletal system | 0.614 | — | common-variant locus | no MR -> candidate analysis |
| Hallux rigidus | 0.585 | — | common-variant locus | no MR -> candidate analysis |
| Abnormal meniscus morphology | 0.582 | — | common-variant locus | no MR -> candidate analysis |
| osteoarthritis | 0.565 | — | common-variant locus | MR: beta=0.243, p=0.133 (trans) |
| sleep apnea syndrome | 0.538 | — | common-variant locus | no MR -> candidate analysis |
| injury | 0.537 | — | common-variant locus | MR: beta=0.394, p=0.118 (trans) |
| Inguinal hernia | 0.535 | — | common-variant locus | no MR -> candidate analysis |
| medical procedure | 0.513 | — | common-variant locus | no MR -> candidate analysis |
| Umbilical hernia | 0.506 | — | common-variant locus | no MR -> candidate analysis |
| spinal stenosis | 0.49 | — | common-variant locus | no MR -> candidate analysis |
| total knee arthroplasty | 0.477 | — | common-variant locus | no MR -> candidate analysis |

> Of the 15 rows above, **10 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Bone morphogenetic protein 6) |
| gnomAD constraint | pLI=1, LOEUF=0.471 — LoF-INTOLERANT |
| GWAS Catalog | 123 unique SNPs / 294 rows |
| ClinVar | 169 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 506 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'BMP6' and resolved to 'Bone morphogenetic protein 6' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 169 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 107 traits by best p-value, aggregated from 233 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P22004 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000153162/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3286078/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/BMP6 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/BMP6 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=BMP6%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/BMP6 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:17:37  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
