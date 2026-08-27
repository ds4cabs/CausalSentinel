# Protein Dossier — EPYC (Epiphycan)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: high cholesterol | 0.262 | 0.0242 | 2.47e-27 | Wald ratio | 1 | trans | 1 |
| Non-cancer illness code  self-reported: deep venous thrombosis (dvt) | 0.344 | 0.0586 | 4.46e-09 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code self-reported: pulmonary embolism (with or without) dvt | 0.386 | 0.0884 | 1.24e-05 | Wald ratio | 1 | trans | NA |
| Forced expiratory volume in 1-second (FEV1) | 0.0375 | 0.0101 | 1.96e-04 | Wald ratio | 1 | trans | NA |
| Forced vital capacity (FVC) | 0.0343 | 0.00954 | 3.20e-04 | Wald ratio | 1 | trans | NA |
| Eye problems or disorders: Glaucoma | 0.27 | 0.0756 | 3.61e-04 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: M16 Coxarthrosis [arthrosis of hip] | 0.261 | 0.075 | 4.97e-04 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | 0.143 | 0.0449 | 0.00143 | Wald ratio | 1 | trans | NA |
| Schizophrenia | -0.178 | 0.0577 | 0.00209 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: gout | -0.511 | 0.168 | 0.00237 | Wald ratio | 1 | trans | NA |
| Systolic blood pressure  automated reading | -0.0341 | 0.0119 | 0.00425 | Wald ratio | 1 | trans | NA |
| Alcohol intake frequency | -0.0481 | 0.0172 | 0.00512 | Wald ratio | 1 | trans | NA |
| _...and 62 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_5 association rows across 4 traits (2 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Protein quantitative trait loci (liver) | 4e-10 | rs11105949 | 1 | GCST011427 | no MR -> candidate analysis |
| Corneal resistance factor (MTAG) | 7e-10 | rs10859098 | 1 | GCST90102517 | no MR -> candidate analysis |
| Long sleep duration (>=10 hours) | 2e-6 | rs79779552 | 1 | GCST90428610 | no MR -> candidate analysis |
| Glioblastoma | 6e-6 | rs186984001 | 2 | GCST90296471 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 441 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| ovarian dysfunction | 0.415 | — | common-variant locus | no MR -> candidate analysis |
| Abnormality of the skeletal system | 0.172 | — | common-variant locus | no MR -> candidate analysis |
| hair color | 0.171 | — | common-variant locus | no MR -> candidate analysis |
| pernicious anemia | 0.125 | — | common-variant locus | no MR -> candidate analysis |
| Hodgkins lymphoma | 0.108 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.107 | — | common-variant locus | no MR -> candidate analysis |
| cholelithiasis | 0.102 | — | common-variant locus | MR: beta=-0.241, p=0.0207 (trans) |

> Of the 7 rows above, **6 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1.2e-09, LOEUF=1.28 — LoF-tolerant |
| GWAS Catalog | 33 unique SNPs / 66 rows |
| ClinVar | 80 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 441 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'EPYC'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 80 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 4 of 4 traits by best p-value, aggregated from 5 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q99645 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000083782/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/EPYC — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/EPYC — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=EPYC%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/EPYC — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:27:41  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
