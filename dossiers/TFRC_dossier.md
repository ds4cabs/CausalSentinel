# Protein Dossier — TFRC (Transferrin receptor protein 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Transferrin Saturation | -0.951 | 0.05 | 1.17e-80 | Wald ratio | 1 | trans | NA |
| Iron | -0.925 | 0.05 | 2.26e-76 | Wald ratio | 1 | trans | NA |
| Mean cell haemoglobin | -0.955 | 0.0555 | 2.07e-66 | Wald ratio | 1 | trans | NA |
| Mean cell volume | -2.11 | 0.142 | 4.15e-50 | Wald ratio | 1 | trans | NA |
| Haemoglobin concentration | -0.392 | 0.0312 | 3.71e-36 | Wald ratio | 1 | trans | NA |
| Packed cell volume | -0.767 | 0.0921 | 8.22e-17 | Wald ratio | 1 | trans | NA |
| HbA1C | 0.134 | 0.0178 | 5.16e-14 | Wald ratio | 1 | trans | 1 |
| Ferritin | -0.254 | 0.0471 | 6.66e-08 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: R07 Pain in throat and chest | 0.187 | 0.0446 | 2.66e-05 | Wald ratio | 1 | trans | NA |
| Transferrin | 0.196 | 0.051 | 1.26e-04 | Wald ratio | 1 | trans | NA |
| Mean cell haemoglobin concentration | -0.0614 | 0.0183 | 8.04e-04 | Wald ratio | 1 | trans | NA |
| LDL cholesterol | 0.0515 | 0.0188 | 0.0062 | Wald ratio | 1 | trans | NA |
| _...and 110 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_221 association rows across 98 traits (199 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating TFRC levels | 3e-1757 | rs3817672 | 3 | GCST90859941 | no MR -> candidate analysis |
| Mean corpuscular hemoglobin | 1e-319 | rs3804139 | 19 | GCST90002326 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 1e-300 | rs11718657 | 3 | GCST90838671 | no MR -> candidate analysis |
| Mean corpuscular haemoglobin (UKB data field 30050) | 8e-263 | rs9877493 | 5 | GCST90468084 | no MR -> candidate analysis |
| Mean corpuscular volume | 2e-257 | rs3804139 | 14 | GCST90002338 | no MR -> candidate analysis |
| Red cell distribution width | 4e-220 | rs41300435 | 12 | GCST90002369 | no MR -> candidate analysis |
| Mean corpuscular volume (UKB data field 30040) | 4e-217 | rs9877493 | 4 | GCST90468086 | no MR -> candidate analysis |
| Red blood cell erythrocyte distribution width (UKB data fiel | 2e-175 | rs41300435 | 3 | GCST90468099 | no MR -> candidate analysis |
| mean corpuscular hemoglobin (MCH, mean, inv-norm transformed | 1e-104 | rs493661 | 2 | GCST90479673 | no MR -> candidate analysis |
| mean corpuscular hemoglobin (MCH, maximum, inv-norm transfor | 3e-104 | rs454516 | 2 | GCST90479672 | no MR -> candidate analysis |
| Red blood cell count | 2e-94 | rs9877493 | 8 | GCST90002363 | MR: beta=0.0213, p=0.0732 (trans) |
| mean corpuscular hemoglobin (MCH, minimum, inv-norm transfor | 8e-90 | rs493661 | 2 | GCST90479674 | no MR -> candidate analysis |
| _...and 86 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1129 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| TFRC-related combined immunodeficiency | 0.694 | — | established (curated) | no MR -> candidate analysis |
| type 2 diabetes mellitus | 0.79 | — | common-variant locus | no MR -> candidate analysis |
| diabetes mellitus | 0.729 | — | common-variant locus | no MR -> candidate analysis |
| combined immunodeficiency | 0.547 | — | established (curated) | no MR -> candidate analysis |
| Combined T and B cell immunodeficiency | 0.547 | — | established (curated) | no MR -> candidate analysis |
| diabetic retinopathy | 0.542 | — | common-variant locus | no MR -> candidate analysis |
| hereditary disease | 0.317 | — | established (curated) | no MR -> candidate analysis |

> Of the 7 rows above, **7 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 1 known modulators (Transferrin receptor protein 1) |
| gnomAD constraint | pLI=0.31, LOEUF=0.541 — LoF-tolerant |
| GWAS Catalog | 124 unique SNPs / 270 rows |
| ClinVar | 840 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1129 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'TFRC' and resolved to 'Transferrin receptor protein 1' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 840 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 98 traits by best p-value, aggregated from 221 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P02786 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000072274/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3712860/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/TFRC — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/TFRC — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=TFRC%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/TFRC — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:19:43  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
