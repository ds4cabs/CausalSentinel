# Protein Dossier — CDSN (Corneodesmosin)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Body mass index (BMI) | -0.0215 | 0.00657 | 0.00107 | Inverse variance weighted | 2 | trans | NA |
| Body mass index (BMI) | -0.0215 | 0.00657 | 0.00107 | Inverse variance weighted | 2 | trans | NA |
| Weight | -0.0177 | 0.00581 | 0.00235 | Inverse variance weighted | 2 | trans | NA |
| Weight | -0.0177 | 0.00581 | 0.00235 | Inverse variance weighted | 2 | trans | NA |
| Major depressive disorder | -0.179 | 0.0612 | 0.0035 | Inverse variance weighted | 2 | trans | NA |
| Major depressive disorder | -0.179 | 0.0612 | 0.0035 | Inverse variance weighted | 2 | trans | NA |
| Childhood intelligence | -0.151 | 0.0558 | 0.00665 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: R04 Haemorrhage from respiratory passages | 0.177 | 0.0771 | 0.0215 | Inverse variance weighted | 2 | trans | NA |
| Diagnoses - main ICD10: R04 Haemorrhage from respiratory passages | 0.177 | 0.0771 | 0.0215 | Inverse variance weighted | 2 | trans | NA |
| Urinary albumin-to-creatinine ratio | -0.0397 | 0.0184 | 0.0312 | Inverse variance weighted | 2 | trans | NA |
| Urinary albumin-to-creatinine ratio | -0.0397 | 0.0184 | 0.0312 | Inverse variance weighted | 2 | trans | NA |
| Years of schooling | -0.0423 | 0.0199 | 0.0339 | Inverse variance weighted | 2 | trans | NA |
| _...and 186 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_27 association rows across 25 traits (23 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Primary sclerosing cholangitis (MTAG) | 1e-61 | rs3094210 | 1 | GCST90271580 | no MR -> candidate analysis |
| Hemoglobin levels | 5e-44 | rs34182778 | 1 | GCST010083 | no MR -> candidate analysis |
| KIR2DL2 protein levels | 7e-33 | rs115510688 | 1 | GCST90469684 | no MR -> candidate analysis |
| PLB1 protein levels | 1e-27 | rs9501053 | 1 | GCST90470253 | no MR -> candidate analysis |
| Polyunsaturated fatty acid levels | 1e-24 | rs3130988 | 1 | GCST90502134 | no MR -> candidate analysis |
| FCRL1/TNFRSF13C protein level ratio | 1e-21 | rs1265045 | 1 | GCST90314796 | no MR -> candidate analysis |
| Omega-6 fatty acid levels | 2e-21 | rs3130988 | 1 | GCST90502095 | no MR -> candidate analysis |
| Mouth ulcers | 3e-20 | rs78479381 | 1 | GCST007839 | no MR -> candidate analysis |
| FEV1 x serum 25-hydroxyvitamin D interaction in never smoker | 1e-19 | rs3130985 | 1 | GCST90590340 | no MR -> candidate analysis |
| Psoriasis | 6e-16 | rs3130982 x rs9366778 | 1 | GCST007023 | MR: beta=-0.0548, p=0.404 (trans) |
| MHC class I polypeptide-related sequence B levels | 4e-15 | rs3130991 | 1 | GCST90101317 | no MR -> candidate analysis |
| Height | 1e-14 | rs1042127 | 1 | GCST90245848 | no MR -> candidate analysis |
| _...and 13 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1125 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| peeling skin syndrome 1 | 0.778 | — | established (curated) | no MR -> candidate analysis |
| hypotrichosis 2 | 0.707 | — | established (curated) | no MR -> candidate analysis |
| hypotrichosis simplex of the scalp | 0.608 | — | established (curated) | no MR -> candidate analysis |
| hereditary disease | 0.316 | — | established (curated) | no MR -> candidate analysis |

> Of the 4 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.2, LOEUF=0.712 — LoF-tolerant |
| GWAS Catalog | 843 unique SNPs / 2456 rows |
| ClinVar | 179 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 1 clinical annotations across 2 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1125 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'CDSN'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 179 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 20 of 25 traits by best p-value, aggregated from 27 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q15517 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000204539/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CDSN — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CDSN — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CDSN%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=CDSN — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CDSN — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:46:42  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
