# Protein Dossier — MRC2 (C-type mannose receptor 2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: I80 Phlebitis and thrombophlebitis | 0.536 | 0.125 | 1.88e-05 | Wald ratio | 1 | cis | NA |
| Weight | 0.0442 | 0.0127 | 4.87e-04 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | 0.0399 | 0.0118 | 7.03e-04 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: deep venous thrombosis (dvt) | 0.258 | 0.0793 | 0.00114 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | 0.0569 | 0.0186 | 0.00224 | Wald ratio | 1 | cis | NA |
| Diastolic blood pressure  automated reading | 0.0418 | 0.0147 | 0.00447 | Wald ratio | 1 | cis | NA |
| Birth weight | 0.0667 | 0.0247 | 0.00686 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M54 Dorsalgia | 0.232 | 0.0893 | 0.00955 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: gout | -0.559 | 0.224 | 0.0125 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | 0.0353 | 0.0144 | 0.0139 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code self-reported: pulmonary embolism (with or without) dvt | 0.295 | 0.121 | 0.0146 | Wald ratio | 1 | cis | NA |
| Ovarian cancer | -0.194 | 0.0885 | 0.0286 | Wald ratio | 1 | cis | NA |
| _...and 62 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3041_55_2` | MRC2 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_68 association rows across 41 traits (62 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| MATN3 protein levels | 1e-85 | rs12452590 | 1 | GCST90469865 | no MR -> candidate analysis |
| Pulse pressure | 7e-42 | rs56288724 | 7 | GCST90310296 | no MR -> candidate analysis |
| C-type mannose receptor 2 levels | 5e-37 | rs2465428 | 4 | GCST90137810 | no MR -> candidate analysis |
| Height | 4e-29 | rs2014055 | 5 | GCST90245848 | no MR -> candidate analysis |
| diastolic blood pressure (DBP, mean, inv-normal transformed) | 1e-22 | rs56288724 | 2 | GCST90475255 | no MR -> candidate analysis |
| Sex hormone-binding globulin levels and heel estimated bone  | 2e-21 | rs12452590 | 1 | GCST90399396 | no MR -> candidate analysis |
| FEV1 FVC ratio Z score (UKB data field 20258) | 3e-21 | rs12452590 | 1 | GCST90468165 | no MR -> candidate analysis |
| Body shape phenotype PC2 | 1e-20 | rs12452590 | 1 | GCST90832990 | no MR -> candidate analysis |
| Sex hormone-binding globulin levels adjusted for BMI and hee | 2e-20 | rs12452590 | 1 | GCST90399398 | no MR -> candidate analysis |
| Lung function (FEV1/FVC) | 4e-19 | rs12452590 | 2 | GCST90244094 | no MR -> candidate analysis |
| Heel bone mineral density | 6e-19 | rs12452590 | 2 | GCST006979 | MR: beta=0.0569, p=0.00224 (cis) |
| THBS2 protein levels | 4e-18 | rs146172137 | 1 | GCST90470854 | no MR -> candidate analysis |
| _...and 29 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 199 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| abdominal aortic aneurysm | 0.735 | — | common-variant locus | no MR -> candidate analysis |
| aneurysm | 0.636 | — | common-variant locus | no MR -> candidate analysis |
| aortic aneurysm | 0.635 | — | common-variant locus | no MR -> candidate analysis |
| hypertensive disorder | 0.512 | — | common-variant locus | no MR -> candidate analysis |
| type 2 diabetes mellitus | 0.488 | — | common-variant locus | no MR -> candidate analysis |
| coronary artery disorder | 0.461 | — | common-variant locus | no MR -> candidate analysis |
| migraine disorder | 0.461 | — | common-variant locus | no MR -> candidate analysis |
| musculoskeletal system disorder | 0.373 | — | common-variant locus | no MR -> candidate analysis |
| mathematical ability | 0.094 | — | common-variant locus | no MR -> candidate analysis |

> Of the 9 rows above, **9 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.31, LOEUF=0.488 — LoF-tolerant |
| GWAS Catalog | 70 unique SNPs / 125 rows |
| ClinVar | 239 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 199 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'MRC2'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 239 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 41 traits by best p-value, aggregated from 68 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9UBG0 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000011028/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/MRC2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/MRC2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=MRC2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/MRC2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:51:58  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
