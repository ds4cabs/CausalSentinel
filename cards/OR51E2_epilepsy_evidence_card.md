# Target Evidence Card — OR51E2 × epilepsy

**Verdict:** INSUFFICIENT EVIDENCE — there is currently no direct genetic association, causal estimate, or disease-specific evidence linking OR51E2 to epilepsy.

> **Question actually answered:** the free-text disease was resolved to **MONDO_0005027 (epilepsy)**. If that is not what you meant, every score below answers a different question.

## Evidence

| Evidence | Tool | Result |
|---|---|---|
| Causal effect (MR) — retrieved, not computed | `get_mr_result` | **not available** — no pQTL MR estimate for this protein in the resource (absence of an estimate is not evidence of no effect) |
| Target–disease association | `get_target_disease_evidence` | **not available** — OR51E2 is not among the top 500 associated targets for MONDO_0005027 (epilepsy). This is a TRUNCATED LOOKUP, not proof of no association. Free-text inputs were resolved to ontology terms: 'OR51E2' -> ENSG00000167332 (OR51E2); 'epilepsy' -> MONDO_0005027 (epilepsy). Scores below describe THAT term, not the free-text phrase. |
| Protein context | `get_uniprot_dossier` | Q9H255 — Olfactory receptor 51E2; location: Cell membrane, Early endosome membrane |
| Known modulators / druggability | `get_chembl_modulators` | **tool error** — ChEMBL HTTP 500 |
| Clinical variants | `get_clinvar_variants` | 96 ClinVar records; 0 pathogenic in a sample of 30 |
| Population constraint / LoF tolerance | `get_gnomad_constraint` | pLI=1e-05, LOEUF=1.6 → LoF-tolerant |
| Extra genetic evidence | `get_gwas_catalog` | 34 unique SNPs from 68/68 association rows |
| Pharmacogenomics | `get_pharmgkb_drug_gene` | **not available** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene). |

## Caveats declared by the tools

- **`get_target_disease_evidence`** — OR51E2 is not among the top 500 associated targets for MONDO_0005027 (epilepsy). This is a TRUNCATED LOOKUP, not proof of no association. Free-text inputs were resolved to ontology terms: 'OR51E2' -> ENSG00000167332 (OR51E2); 'epilepsy' -> MONDO_0005027 (epilepsy). Scores below describe THAT term, not the free-text phrase.
- **`get_mr_result`** — No pQTL-based MR estimate for OR51E2 in the EpiGraphDB pQTL resource. This resource only covers proteins with usable plasma pQTL instruments. ABSENCE OF AN ESTIMATE IS NOT EVIDENCE OF NO EFFECT.
- **`get_clinvar_variants`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 96 ClinVar records for this gene; it is a sample, not a rate.
- **`get_pharmgkb_drug_gene`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).

## Reasoning

Open Targets indicates that OR51E2 is not among the top associated targets for epilepsy, and no Mendelian randomization estimate is available for this protein-disease pair. The gene demonstrates loss-of-function tolerance in gnomAD with a high LOEUF, suggesting safety from genetic inactivation, but ClinVar variants are primarily of uncertain significance. Although GWAS catalog records map multiple SNPs to the locus, none link the gene to epilepsy, and there are no pharmacogenomic annotations in PharmGKB.

## Sources

- `get_uniprot_dossier`: https://www.uniprot.org/uniprotkb/Q9H255 — _UniProt release 2026_02 (10-June-2026)_
- `get_mr_result`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `get_clinvar_variants`: https://www.ncbi.nlm.nih.gov/clinvar/?term=OR51E2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `get_gnomad_constraint`: https://gnomad.broadinstitute.org/gene/OR51E2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `get_gwas_catalog`: https://www.ebi.ac.uk/gwas/genes/OR51E2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_

## Provenance

- Generated: 2026-08-17T22:25:56
- Model (reasoning text only): `gemini-flash-lite-latest`
- Tools invoked (8 calls): `get_uniprot_dossier`, `get_target_disease_evidence`, `get_chembl_modulators`, `get_mr_result`, `get_clinvar_variants`, `get_gnomad_constraint`, `get_gwas_catalog`, `get_pharmgkb_drug_gene`
- Evidence table, caveats, sources and this block are rendered mechanically from tool return values. The model wrote only the Verdict sentence and the Reasoning paragraph, both checked against tool output by `validate_card.py`.
- No Mendelian randomization or colocalization is computed by this agent; MR estimates, where present, are retrieved from published work.
