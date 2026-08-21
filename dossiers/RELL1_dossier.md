# Protein Dossier — RELL1 (RELT-like protein 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Lung cancer | -0.507 | 0.102 | 7.28e-07 | Wald ratio | 1 | trans | NA |
| Squamous cell lung cancer | -0.572 | 0.15 | 1.38e-04 | Wald ratio | 1 | trans | NA |
| Body mass index (BMI) | -0.0456 | 0.0141 | 0.00123 | Wald ratio | 1 | trans | NA |
| Weight | -0.038 | 0.0125 | 0.00229 | Wald ratio | 1 | trans | NA |
| Cough on most days | -0.223 | 0.0903 | 0.0135 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: anxiety or panic attacks | 0.229 | 0.0978 | 0.0192 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: K43 Ventral hernia | 0.344 | 0.154 | 0.0257 | Wald ratio | 1 | trans | NA |
| Eye problems or disorders: Cataract | 0.133 | 0.067 | 0.0469 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: R10 Abdominal and pelvic pain | -0.159 | 0.0805 | 0.0482 | Wald ratio | 1 | trans | NA |
| Fractured bone site(s): Other bones | -0.137 | 0.0708 | 0.0524 | Wald ratio | 1 | trans | NA |
| HbA1C | 0.0523 | 0.0274 | 0.0563 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: C50 Malignant neoplasm of breast | 0.177 | 0.0934 | 0.0583 | Wald ratio | 1 | trans | NA |
| _...and 75 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_14 association rows across 10 traits (1 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Height | 2e-9 | rs6531568 | 1 | GCST90245848 | no MR -> candidate analysis |
| Adolescent idiopathic scoliosis | 3e-7 | rs17495047 | 1 | GCST006287 | no MR -> candidate analysis |
| 3-hydroxy-1-methylpropylmercapturic acid levels in smokers | 6e-7 | rs6531565 | 1 | GCST002957 | no MR -> candidate analysis |
| IgG glycosylation | 6e-7 | rs13144232 | 3 | GCST001848 | no MR -> candidate analysis |
| Lumbar disc herniation | 8e-7 | rs13128262 | 1 | GCST90837384 | no MR -> candidate analysis |
| Breast cancer | 1e-6 | rs180714962 | 1 | GCST90551892 | no MR -> candidate analysis |
| General cognitive ability | 2e-6 | rs111283315 | 1 | GCST006269 | no MR -> candidate analysis |
| Tuberculosis | 2e-6 | rs2940989 | 3 | GCST004922 | no MR -> candidate analysis |
| Total cholesterol levels | 6e-6 | rs78410324 | 1 | GCST007203 | no MR -> candidate analysis |
| COVID-19 | 6e-6 | rs3029357 | 1 | GCST90104722 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 65 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| placental abruption | 0.466 | — | common-variant locus | no MR -> candidate analysis |
| placental retention | 0.424 | — | common-variant locus | no MR -> candidate analysis |
| contracture | 0.163 | — | common-variant locus | no MR -> candidate analysis |
| esophageal cancer | 0.079 | — | established (curated) | no MR -> candidate analysis |
| urolithiasis | 0.08 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.08 | — | common-variant locus | no MR -> candidate analysis |
| Abnormal nasolacrimal system morphology | 0.046 | — | common-variant locus | no MR -> candidate analysis |
| osteonecrosis | 0.041 | — | common-variant locus | no MR -> candidate analysis |
| male reproductive organ cancer | 0.041 | — | common-variant locus | no MR -> candidate analysis |
| Subdural hemorrhage | 0.036 | — | common-variant locus | no MR -> candidate analysis |
| schizophrenia | 0.036 | — | common-variant locus | no MR -> candidate analysis |

> Of the 11 rows above, **11 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.19, LOEUF=0.736 — LoF-tolerant |
| GWAS Catalog | 31 unique SNPs / 62 rows |
| ClinVar | 73 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 65 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'RELL1'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 73 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 10 of 10 traits by best p-value, aggregated from 14 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q8IUW5 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000181826/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/RELL1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/RELL1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=RELL1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/RELL1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:47:31  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
