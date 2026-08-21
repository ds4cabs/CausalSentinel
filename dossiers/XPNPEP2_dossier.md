# Protein Dossier — XPNPEP2 (Xaa-Pro aminopeptidase 2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Urate | 0.16 | 0.0285 | 1.98e-08 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: L03 Cellulitis | 0.38 | 0.0987 | 1.18e-04 | Wald ratio | 1 | trans | NA |
| Thyroid cancer | -1.66 | 0.455 | 2.54e-04 | Wald ratio | 1 | trans | NA |
| Serum creatinine (eGFRcrea) | 0.0165 | 0.0046 | 3.35e-04 | Wald ratio | 1 | trans | NA |
| Transferrin | -0.187 | 0.054 | 5.34e-04 | Wald ratio | 1 | trans | NA |
| Chronic kidney disease | -0.265 | 0.08 | 9.25e-04 | Wald ratio | 1 | trans | NA |
| Fractured bone site(s): Wrist | 0.236 | 0.0727 | 0.00115 | Wald ratio | 1 | trans | NA |
| Birth weight | 0.063 | 0.0195 | 0.00123 | Wald ratio | 1 | trans | NA |
| Primary sclerosing cholangitis  | 0.504 | 0.165 | 0.00227 | Wald ratio | 1 | trans | NA |
| HOMA-IR | -0.065 | 0.0215 | 0.0025 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: R07 Pain in throat and chest | -0.194 | 0.0698 | 0.00537 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: high cholesterol | -0.103 | 0.0385 | 0.00741 | Wald ratio | 1 | trans | NA |
| _...and 109 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_8 association rows across 8 traits (8 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating XPNPEP2 levels | 9e-3826 | rs4829707 | 1 | GCST90860047 | no MR -> candidate analysis |
| Superoxide dismutase [Mn], mitochondrial levels | 4e-122 | rs11096255 | 1 | GCST90249469 | no MR -> candidate analysis |
| Serum levels of protein SOD2 | 4e-80 | rs11096255 | 1 | GCST90088866 | no MR -> candidate analysis |
| Prolylproline levels | 2e-78 | rs4830164 | 1 | GCST90140334 | no MR -> candidate analysis |
| Blood protein levels in cardiovascular risk | 2e-68 | rs2050011 | 1 | GCST009731 | no MR -> candidate analysis |
| Pro-hydroxy-pro levels | 2e-25 | rs4830159 | 1 | GCST90139421 | no MR -> candidate analysis |
| Monocyte count | 3e-10 | rs3747343 | 1 | GCST90002393 | no MR -> candidate analysis |
| Serum uric acid levels | 4e-8 | rs3788853 | 1 | GCST90018977 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 100 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| acquired angioedema | 0.353 | — | established (curated) | no MR -> candidate analysis |
| primary ovarian failure | 0.195 | — | established (curated) | no MR -> candidate analysis |
| response to darapladib | 0.039 | — | common-variant locus | no MR -> candidate analysis |
| Diarrhea | 0.039 | — | common-variant locus | no MR -> candidate analysis |

> Of the 4 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Xaa-Pro aminopeptidase 2) |
| gnomAD constraint | pLI=1.2e-23, LOEUF=1.32 — LoF-tolerant |
| GWAS Catalog | 8 unique SNPs / 16 rows |
| ClinVar | 341 records; 6 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 1 clinical annotations across 1 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 100 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'XPNPEP2' and resolved to 'Xaa-Pro aminopeptidase 2' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 341 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 8 of 8 traits by best p-value, aggregated from 8 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O43895 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000122121/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4610/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/XPNPEP2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/XPNPEP2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=XPNPEP2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=XPNPEP2 — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/XPNPEP2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:38:54  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
