# Protein Dossier — SIRT2 (NAD-dependent protein deacetylase sirtuin-2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: R11 Nausea and vomiting | 0.184 | 0.056 | 0.00101 | Inverse variance weighted | 3 | trans | NA |
| Diagnoses - main ICD10: R11 Nausea and vomiting | 0.184 | 0.056 | 0.00101 | Inverse variance weighted | 3 | trans | NA |
| Diagnoses - main ICD10: R11 Nausea and vomiting | 0.184 | 0.056 | 0.00101 | Inverse variance weighted | 3 | trans | NA |
| Triglycerides | -0.0247 | 0.00817 | 0.0025 | Inverse variance weighted | 3 | trans | NA |
| Triglycerides | -0.0247 | 0.00817 | 0.0025 | Inverse variance weighted | 3 | trans | NA |
| Triglycerides | -0.0247 | 0.00817 | 0.0025 | Inverse variance weighted | 3 | trans | NA |
| Melanoma | 0.345 | 0.138 | 0.0127 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | -0.168 | 0.0743 | 0.0239 | Inverse variance weighted | 3 | trans | NA |
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | -0.168 | 0.0743 | 0.0239 | Inverse variance weighted | 3 | trans | NA |
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | -0.168 | 0.0743 | 0.0239 | Inverse variance weighted | 3 | trans | NA |
| Happiness | -0.0114 | 0.00523 | 0.0286 | Inverse variance weighted | 3 | trans | NA |
| Happiness | -0.0114 | 0.00523 | 0.0286 | Inverse variance weighted | 3 | trans | NA |
| _...and 273 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-5030_52_1` | SIRT2 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_3 association rows across 3 traits (3 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating SIRT2 levels | 1e-137 | rs144373891 | 1 | GCST90859891 | no MR -> candidate analysis |
| SIRT2 protein levels | 5e-93 | rs144373891 | 1 | GCST90470642 | no MR -> candidate analysis |
| SIR2-like protein 2 levels | 7e-34 | rs144373891 | 1 | GCST90012061 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 518 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| type 2 diabetes mellitus | 0.163 | — | common-variant locus | no MR -> candidate analysis |
| diabetes mellitus | 0.163 | — | common-variant locus | no MR -> candidate analysis |
| arthropathy | 0.165 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (NAD-dependent protein deacetylase sirtuin-2) |
| gnomAD constraint | pLI=6.7e-10, LOEUF=0.908 — LoF-tolerant |
| GWAS Catalog | 47 unique SNPs / 94 rows |
| ClinVar | 101 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 1 clinical annotations across 1 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 518 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'SIRT2' and resolved to 'NAD-dependent protein deacetylase sirtuin-2' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 101 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 3 of 3 traits by best p-value, aggregated from 3 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q8IXJ6 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000068903/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4462/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/SIRT2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/SIRT2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=SIRT2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=SIRT2 — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/SIRT2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:07:46  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
