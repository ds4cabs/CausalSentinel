# Protein Dossier — COLGALT1 (Procollagen galactosyltransferase 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Systolic blood pressure  automated reading | -0.0187 | 0.00661 | 0.00462 | Inverse variance weighted | 2 | trans | NA |
| Systolic blood pressure  automated reading | -0.0187 | 0.00661 | 0.00462 | Inverse variance weighted | 2 | trans | NA |
| Creatinine (enzymatic) in urine | -0.0166 | 0.00618 | 0.00723 | Inverse variance weighted | 2 | trans | NA |
| Creatinine (enzymatic) in urine | -0.0166 | 0.00618 | 0.00723 | Inverse variance weighted | 2 | trans | NA |
| Diagnoses - main ICD10: G56 Mononeuropathies of upper limb | 0.112 | 0.044 | 0.0107 | Inverse variance weighted | 2 | trans | NA |
| Diagnoses - main ICD10: G56 Mononeuropathies of upper limb | 0.112 | 0.044 | 0.0107 | Inverse variance weighted | 2 | trans | NA |
| Cancer code  self-reported: small intestine or small bowel cancer | 0.489 | 0.196 | 0.0125 | Inverse variance weighted | 2 | trans | NA |
| Cancer code  self-reported: small intestine or small bowel cancer | 0.489 | 0.196 | 0.0125 | Inverse variance weighted | 2 | trans | NA |
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | -0.24 | 0.0988 | 0.0153 | Inverse variance weighted | 2 | trans | NA |
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | -0.24 | 0.0988 | 0.0153 | Inverse variance weighted | 2 | trans | NA |
| Inflammatory bowel disease | 0.139 | 0.0595 | 0.0197 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: ankylosing spondylitis | 0.297 | 0.129 | 0.0213 | Inverse variance weighted | 2 | trans | NA |
| _...and 138 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_8 association rows across 5 traits (6 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Procollagen galactosyltransferase 1 levels | 8e-47 | rs4808666 | 1 | GCST90248987 | no MR -> candidate analysis |
| Height | 8e-13 | rs7249148 | 3 | GCST90245848 | no MR -> candidate analysis |
| White blood cell count | 1e-10 | rs62119898 | 2 | GCST90002407 | no MR -> candidate analysis |
| Total antibody levels in response to SARS-CoV-2 vaccination | 3e-9 | rs149813122 | 1 | GCST90244757 | no MR -> candidate analysis |
| Blood protein levels | 4e-6 | rs73525772 | 1 | GCST006585 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1370 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| cerebral small vessel disease | 0.824 | — | established (curated) | no MR -> candidate analysis |
| hereditary disease | 0.683 | — | established (curated) | no MR -> candidate analysis |
| familial porencephaly | 0.608 | — | established (curated) | no MR -> candidate analysis |
| response to COVID-19 vaccine | 0.3 | — | common-variant locus | no MR -> candidate analysis |
| vascular dementia | 0.182 | — | established (curated) | no MR -> candidate analysis |
| Genetic visceral malformation of the liver, biliary tract, pancreas or spleen | 0.153 | — | common-variant locus | no MR -> candidate analysis |
| digestive system disorder | 0.113 | — | common-variant locus | no MR -> candidate analysis |

> Of the 7 rows above, **7 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Procollagen galactosyltransferase 1) |
| gnomAD constraint | pLI=9.7e-11, LOEUF=0.911 — LoF-tolerant |
| GWAS Catalog | 43 unique SNPs / 86 rows |
| ClinVar | 353 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1370 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'COLGALT1' and resolved to 'Procollagen galactosyltransferase 1' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 353 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 5 of 5 traits by best p-value, aggregated from 8 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q8NBJ5 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000130309/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL6067420/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/COLGALT1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/COLGALT1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=COLGALT1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/COLGALT1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:58:28  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
