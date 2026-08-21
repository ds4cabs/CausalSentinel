# Protein Dossier — PRSS22 (Brain-specific serine protease 4)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Lung cancer | -0.183 | 0.0594 | 0.00211 | Wald ratio | 1 | cis | NA |
| Squamous cell lung cancer | -0.246 | 0.0899 | 0.00622 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K43 Ventral hernia | 0.263 | 0.0969 | 0.0066 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I83 Varicose veins of lower extremities | 0.13 | 0.0511 | 0.0109 | Wald ratio | 1 | cis | NA |
| Depressive symptoms | 0.0326 | 0.013 | 0.0124 | Wald ratio | 1 | cis | NA |
| Primary sclerosing cholangitis  | -0.296 | 0.121 | 0.0142 | Wald ratio | 1 | cis | NA |
| Ferritin | 0.0809 | 0.0333 | 0.015 | Wald ratio | 1 | cis | NA |
| Packed cell volume | 0.139 | 0.062 | 0.0246 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: C61 Malignant neoplasm of prostate | 0.189 | 0.0852 | 0.0269 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | -0.0875 | 0.0404 | 0.0304 | Wald ratio | 1 | cis | NA |
| Putamen volume | 46.2 | 21.5 | 0.0318 | Wald ratio | 1 | cis | NA |
| Happiness | 0.0212 | 0.0103 | 0.0405 | Wald ratio | 1 | cis | NA |
| _...and 97 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-4534_10_2` | BSSP4 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_11 association rows across 8 traits (10 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| PRSS22 protein levels | 6e-262 | rs8046218 | 2 | GCST90470341 | no MR -> candidate analysis |
| Brain-specific serine protease 4 levels | 1e-80 | rs7204669 | 3 | GCST90246746 | no MR -> candidate analysis |
| Blood protein levels | 4e-24 | rs7204669 | 1 | GCST006585 | no MR -> candidate analysis |
| Seborrheic dermatitis (PheCode 690.1) | 2e-23 | rs8046218 | 1 | GCST90480445 | no MR -> candidate analysis |
| Erythematosquamous dermatosis (PheCode 690) | 5e-23 | rs8046218 | 1 | GCST90480446 | no MR -> candidate analysis |
| red cell diameter width (RDW, maximum, inv-norm transformed) | 2e-11 | rs73495044 | 1 | GCST90480671 | no MR -> candidate analysis |
| Gut microbial network clusters (Salmon (at 1 year) x Househo | 2e-8 | rs4786345 | 1 | GCST90569455 | no MR -> candidate analysis |
| 3-hydroxypropylmercapturic acid levels in smokers | 4e-7 | rs9925432 | 1 | GCST002956 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 70 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| erythematosquamous dermatosis | 0.629 | — | common-variant locus | no MR -> candidate analysis |
| seborrheic dermatitis | 0.623 | — | common-variant locus | no MR -> candidate analysis |
| pulmonary vascular congestion | 0.066 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=5.2e-09, LOEUF=1.29 — LoF-tolerant |
| GWAS Catalog | 46 unique SNPs / 92 rows |
| ClinVar | 101 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 70 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'PRSS22'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 101 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 8 of 8 traits by best p-value, aggregated from 11 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9GZN4 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000005001/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PRSS22 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PRSS22 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PRSS22%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/PRSS22 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:38:04  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
