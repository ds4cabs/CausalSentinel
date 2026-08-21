# Target Evidence Card — NR3C1 × Rhinitis, Allergic, Seasonal

**Verdict:** INSUFFICIENT EVIDENCE — no disease-specific genetic association or causal MR estimate was retrieved for NR3C1 in allergic seasonal rhinitis.

> **The druggability row is about ChEMBL target "Glucocorticoid receptor" (CHEMBL2034),** matched by text search. If that is not the molecular target you meant, that row is about something else.

## Evidence concordance — classified by rule, not written by the model

- Sources: EpiGraphDB — no pQTL instrument · Europe PMC — NOT checked in this run · Semantic Scholar — NOT checked in this run · MR-KG — NOT checked in this run

## Evidence

| Evidence | Tool | Result |
|---|---|---|
| Causal effect (MR) — retrieved, not computed | `get_mr_result` | **not available** — no pQTL MR estimate for this protein in the resource (absence of an estimate is not evidence of no effect) |
| Target–disease association | `get_target_disease_evidence` | **not available** — Could not resolve target 'NR3C1' or disease 'Rhinitis, Allergic, Seasonal'. |
| Protein context | `get_uniprot_dossier` | P04150 — Glucocorticoid receptor; location: Cytoplasm, Nucleus, Mitochondrion, Cytoplasm, cytoskeleton,  |
| Known modulators / druggability | `get_chembl_modulators` | 20 known modulators (AGONIST) |
| Clinical variants | `get_clinvar_variants` | 354 ClinVar records; 0 pathogenic in a sample of 30 |
| Population constraint / LoF tolerance | `get_gnomad_constraint` | pLI=1, LOEUF=0.296 → LoF-INTOLERANT (handle with care) |
| Extra genetic evidence | `get_gwas_catalog` | 85 unique SNPs from 170/170 association rows |
| Pharmacogenomics | `get_pharmgkb_drug_gene` | **not available** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene). |
| Clinical development record | `get_clinical_evidence` | _tool not called by the agent in this run_ |

## Caveats declared by the tools

- **`get_target_disease_evidence`** — Could not resolve target 'NR3C1' or disease 'Rhinitis, Allergic, Seasonal'.
- **`get_mr_result`** — No pQTL-based MR estimate for NR3C1 in the EpiGraphDB pQTL resource. This resource only covers proteins with usable plasma pQTL instruments. ABSENCE OF AN ESTIMATE IS NOT EVIDENCE OF NO EFFECT.
- **`get_chembl_modulators`** — ChEMBL target matched by text search on 'NR3C1' and resolved to 'Glucocorticoid receptor' — confirm this is the intended target.
- **`get_clinvar_variants`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 354 ClinVar records for this gene; it is a sample, not a rate.
- **`get_pharmgkb_drug_gene`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`classify_evidence_concordance`** — Nothing to compare: fewer than two matched estimates.

## Reasoning

NR3C1 encodes the glucocorticoid receptor, a well-characterized target with multiple known small-molecule agonists in ChEMBL. However, no Mendelian randomization estimate or Open Targets disease association score was available for this target-disease pair. The gene exhibits strong loss-of-function intolerance in gnomAD, suggesting potential safety risks if inhibited, although current modulators are primarily agonists. GWAS catalog queries link numerous SNPs to the locus, but direct evidence connecting NR3C1 to seasonal allergic rhinitis remains unestablished in the provided datasets.

## Sources

- `get_uniprot_dossier`: https://www.uniprot.org/uniprotkb/P04150 — _UniProt release 2026_02 (10-June-2026)_
- `get_mr_result`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `get_chembl_modulators`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2034/ — _ChEMBL_37 (released 2026-05-01)_
- `get_clinvar_variants`: https://www.ncbi.nlm.nih.gov/clinvar/?term=NR3C1%5Bgene%5D — _ClinVar build Build260818-0035.1_
- `get_gnomad_constraint`: https://gnomad.broadinstitute.org/gene/NR3C1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `get_gwas_catalog`: https://www.ebi.ac.uk/gwas/genes/NR3C1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_

## Provenance

- Generated: 2026-08-21T15:48:29
- Model (reasoning text only): `gemini-flash-lite-latest`
- Tools invoked (9 calls): `get_uniprot_dossier`, `get_target_disease_evidence`, `get_mr_result`, `get_chembl_modulators`, `get_clinvar_variants`, `get_gnomad_constraint`, `get_gwas_catalog`, `get_pharmgkb_drug_gene`, `classify_evidence_concordance`
- Evidence table, caveats, sources and this block are rendered mechanically from tool return values. The model wrote only the Verdict sentence and the Reasoning paragraph, both checked against tool output by `validate_card.py`.
- No Mendelian randomization or colocalization is computed by this agent; MR estimates, where present, are retrieved from published work.

> **VALIDATION FAILED** — the model wrote claim tokens with no support in tool output:
> - [modality-not-in-chembl] `small-molecule`
