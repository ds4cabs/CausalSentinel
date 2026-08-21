# Protein Dossier — TF (Serotransferrin)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Transferrin | 1.83 | 0.0471 | 0.00e+00 | Wald ratio | 1 | cis | NA |
| Transferrin Saturation | -0.414 | 0.0463 | 3.48e-19 | Wald ratio | 1 | cis | NA |
| Iron | 0.323 | 0.0458 | 1.81e-12 | Wald ratio | 1 | cis | NA |
| Mean cell haemoglobin | -0.222 | 0.0463 | 1.66e-06 | Wald ratio | 1 | cis | NA |
| Mean cell volume | -0.474 | 0.118 | 5.67e-05 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: J33 Nasal polyp | 0.39 | 0.112 | 4.88e-04 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | -0.0317 | 0.00919 | 5.62e-04 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | -0.033 | 0.00969 | 6.71e-04 | Wald ratio | 1 | cis | NA |
| Red blood cell count | 0.0273 | 0.0101 | 0.00703 | Wald ratio | 1 | cis | NA |
| Ferritin | -0.116 | 0.0432 | 0.00706 | Wald ratio | 1 | cis | NA |
| Intracranial volume | -2.22e+04 | 8.8e+03 | 0.0117 | Wald ratio | 1 | cis | NA |
| Neo-extraversion | 0.878 | 0.356 | 0.0136 | Wald ratio | 1 | cis | NA |
| _...and 101 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-4162_54_2` | Transferrin | Suhre K | 2019 |
| `prot-c-4931_59_1` | TF | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_219 association rows across 106 traits (211 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Iron status biomarkers (transferrin levels) | 8e-610 | rs8177240 | 2 | GCST002678 | no MR -> candidate analysis |
| Iron status biomarkers (transferrin saturation) | 1e-323 | rs6762719 | 5 | GCST004572 | no MR -> candidate analysis |
| Iron status biomarkers (total iron binding capacity) | 1e-323 | rs6762719 | 3 | GCST004571 | no MR -> candidate analysis |
| total iron (mean, inv-norm transformed) | 4e-215 | rs6762719 | 3 | GCST90480712 | no MR -> candidate analysis |
| total iron (minimum, inv-norm transformed) | 7e-205 | rs6762719 | 3 | GCST90480713 | no MR -> candidate analysis |
| Total iron (maximum, inv-norm transformed) | 3e-197 | rs6762719 | 4 | GCST90480711 | no MR -> candidate analysis |
| N-acetylated-alpha-linked acidic dipeptidase 2 levels | 5e-170 | rs1049296 | 3 | GCST90248595 | no MR -> candidate analysis |
| Putamen iron levels (R2* MRI) | 2e-97 | rs4428180 | 1 | GCST90551870 | no MR -> candidate analysis |
| Serum levels of protein NAALAD2 | 1e-80 | rs1049296 | 2 | GCST90089966 | no MR -> candidate analysis |
| transferrin saturation (TSAT, mean, inv-norm transformed) | 2e-76 | rs6762719 | 2 | GCST90480721 | no MR -> candidate analysis |
| Putamen iron levels (quantitative susceptibility mapping) | 7e-71 | rs4428180 | 1 | GCST90551869 | no MR -> candidate analysis |
| THAP5 protein levels | 9e-69 | rs1049296 | 2 | GCST90453316 | no MR -> candidate analysis |
| _...and 94 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1995 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| atransferrinemia | 0.839 | — | established (curated) | no MR -> candidate analysis |
| Congenital atransferrinemia | 0.608 | — | established (curated) | no MR -> candidate analysis |
| hemochromatosis type 1 | 0.743 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.743 | — | common-variant locus | no MR -> candidate analysis |
| urolithiasis | 0.472 | — | common-variant locus | no MR -> candidate analysis |
| preeclampsia | 0.384 | — | common-variant locus | no MR -> candidate analysis |
| Iron deficiency anemia | 0.182 | — | established (curated) | no MR -> candidate analysis |

> Of the 7 rows above, **7 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1.8e-12, LOEUF=0.836 — LoF-tolerant |
| GWAS Catalog | 104 unique SNPs / 201 rows |
| ClinVar | 522 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 1 clinical annotations across 1 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1995 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 522 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 20 of 106 traits by best p-value, aggregated from 219 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P02787 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000091513/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/TF — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/TF — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=TF%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=TF — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/TF — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:19:14  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: chembl
