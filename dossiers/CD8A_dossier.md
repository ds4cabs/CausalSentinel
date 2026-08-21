# Protein Dossier — CD8A (T-cell surface glycoprotein CD8 alpha chain)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Invasive mucinous ovarian cancer | 0.271 | 0.0964 | 0.00497 | Wald ratio | 1 | cis | NA |
| Schizophrenia | -0.0723 | 0.0265 | 0.00627 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K35 Acute appendicitis | 0.188 | 0.0692 | 0.00645 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: Z09 Follow-up examination after treatment for conditions other than malignant neoplasms | 0.111 | 0.0422 | 0.00827 | Wald ratio | 1 | cis | NA |
| Alcohol intake frequency | -0.0207 | 0.00855 | 0.0157 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: C50 Malignant neoplasm of breast | 0.0938 | 0.0412 | 0.023 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | -0.0126 | 0.00578 | 0.0295 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Injury or trauma resulting in loss of vision | -0.178 | 0.0906 | 0.0492 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | 0.115 | 0.0617 | 0.0632 | Wald ratio | 1 | cis | NA |
| Alzheimer's disease | -0.0758 | 0.0413 | 0.0661 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Arm | -0.118 | 0.0659 | 0.0723 | Wald ratio | 1 | cis | NA |
| Low grade serous ovarian cancer | -0.217 | 0.123 | 0.0771 | Wald ratio | 1 | cis | NA |
| _...and 58 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_34 association rows across 30 traits (34 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating CD8A levels (id: OID05124_OID21018) | 9e-554 | rs3020726 | 2 | GCST90860677 | no MR -> candidate analysis |
| Circulating CD8A levels (id: OID00772_OID21018) | 2e-435 | rs3020726 | 2 | GCST90860107 | no MR -> candidate analysis |
| Serum levels of protein CD8A | 2e-122 | rs3020726 | 1 | GCST90089255 | no MR -> candidate analysis |
| T-cell surface glycoprotein CD8 alpha chain levels | 2e-100 | rs3020726 | 2 | GCST90249784 | no MR -> candidate analysis |
| CD8A protein levels | 4e-90 | rs62146078 | 1 | GCST90468655 | no MR -> candidate analysis |
| Blood protein levels | 7e-73 | rs111976570 | 1 | GCST006585 | no MR -> candidate analysis |
| CD8 on CD28+ CD45RA+ CD8+ T cell | 3e-65 | rs938487 | 1 | GCST90002119 | no MR -> candidate analysis |
| T-cell surface glycoprotein CD8 alpha chain (analyte X5992.5 | 3e-49 | rs3020726 | 1 | GCST90426555 | no MR -> candidate analysis |
| CD8 on naive CD8+ T cell | 3e-46 | rs35626322 | 1 | GCST90002055 | no MR -> candidate analysis |
| CD8 on CD8+ T cell | 6e-43 | rs3020726 | 1 | GCST90002058 | no MR -> candidate analysis |
| Cerebrospinal fluid protein CD8A levels | 4e-42 | rs3020726 | 1 | GCST90944172 | no MR -> candidate analysis |
| CD4+ CD8dim T cell %lymphocyte | 1e-36 | rs35706509 | 2 | GCST90001610 | no MR -> candidate analysis |
| _...and 18 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 2798 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| tinea unguium | 0.484 | — | common-variant locus | no MR -> candidate analysis |
| progressive supranuclear palsy | 0.31 | — | common-variant locus | no MR -> candidate analysis |
| stroke disorder | 0.128 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1.9e-09, LOEUF=1.44 — LoF-tolerant |
| GWAS Catalog | 47 unique SNPs / 94 rows |
| ClinVar | 239 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 2798 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'CD8A'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 239 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 30 traits by best p-value, aggregated from 34 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P01732 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000153563/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CD8A — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CD8A — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CD8A%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CD8A — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:44:27  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
