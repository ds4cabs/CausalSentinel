# Protein Dossier — IGFLR1 (IGF-like family receptor 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Body fat | 0.036 | 0.0116 | 0.00186 | Wald ratio | 1 | cis | NA |
| Major depressive disorder | 0.122 | 0.0421 | 0.00385 | Wald ratio | 1 | cis | NA |
| Knee and hip osteoarthritis | -0.123 | 0.0437 | 0.00486 | Wald ratio | 1 | cis | NA |
| Years of schooling | -0.0186 | 0.00714 | 0.00932 | Wald ratio | 1 | cis | NA |
| Systolic blood pressure  automated reading | 0.0124 | 0.00499 | 0.0127 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: C50 Malignant neoplasm of breast | -0.105 | 0.0425 | 0.0136 | Wald ratio | 1 | cis | NA |
| Diastolic blood pressure  automated reading | 0.012 | 0.00499 | 0.0163 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: G47 Sleep disorders | -0.174 | 0.0763 | 0.0223 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | 0.0106 | 0.00488 | 0.0299 | Wald ratio | 1 | cis | NA |
| Childhood intelligence | -0.0541 | 0.0263 | 0.0394 | Wald ratio | 1 | cis | NA |
| Haemoglobin concentration | 0.0277 | 0.0136 | 0.0411 | Wald ratio | 1 | cis | NA |
| Hearing difficulty or problems: Yes | -0.0173 | 0.00858 | 0.0434 | Wald ratio | 1 | cis | NA |
| _...and 101 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_5 association rows across 4 traits (5 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| IGF-like family receptor 1 levels | 1e-278 | rs2871921 | 2 | GCST90248013 | no MR -> candidate analysis |
| IGF-like family receptor 1 levels (IGFLR1.7244.16.3) | 6e-100 | rs12459634 | 1 | GCST90241467 | no MR -> candidate analysis |
| Red cell distribution width | 1e-15 | rs12459634 | 1 | GCST90002404 | no MR -> candidate analysis |
| Lichen sclerosus | 1e-10 | rs140952221 | 1 | GCST90824102 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 57 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| lichen sclerosus et atrophicus | 0.614 | — | common-variant locus | no MR -> candidate analysis |
| dermatitis | 0.127 | — | common-variant locus | no MR -> candidate analysis |
| Eczematoid dermatitis | 0.127 | — | common-variant locus | no MR -> candidate analysis |
| spinal cord injury | 0.068 | — | common-variant locus | no MR -> candidate analysis |
| mathematical ability | 0.041 | — | common-variant locus | no MR -> candidate analysis |

> Of the 5 rows above, **5 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (IGF-like family receptor 1) |
| gnomAD constraint | pLI=4.8e-05, LOEUF=1.09 — LoF-tolerant |
| GWAS Catalog | 72 unique SNPs / 144 rows |
| ClinVar | 95 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 57 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'IGFLR1' and resolved to 'IGF-like family receptor 1' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 95 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 4 of 4 traits by best p-value, aggregated from 5 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9H665 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000126246/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2029192/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/IGFLR1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/IGFLR1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=IGFLR1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/IGFLR1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:09:23  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
