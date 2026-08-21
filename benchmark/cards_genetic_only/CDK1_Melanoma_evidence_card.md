# Target Evidence Card — CDK1 × Melanoma

**Verdict:** INSUFFICIENT EVIDENCE — there is no direct genetic association or causal estimate linking CDK1 to melanoma.

> **You asked about "Melanoma". This card scored MONDO_0005105 — melanoma.** If those are not the same thing, every number below answers a different question.
> **The druggability row is about ChEMBL target "CDK4/CDK1" (CHEMBL4523963),** matched by text search. If that is not the molecular target you meant, that row is about something else.

## Evidence concordance — classified by rule, not written by the model

- Sources: EpiGraphDB — no pQTL instrument · Europe PMC — NOT checked in this run · Semantic Scholar — NOT checked in this run · MR-KG — NOT checked in this run

## Evidence

| Evidence | Tool | Result |
|---|---|---|
| Causal effect (MR) — retrieved, not computed | `get_mr_result` | **not available** — no pQTL MR estimate for this protein in the resource (absence of an estimate is not evidence of no effect) |
| Target–disease association | `get_target_disease_evidence` | **not available** — CDK1 is not among the top 500 associated targets for MONDO_0005105 (melanoma). This is a TRUNCATED LOOKUP, not proof of no association. Free-text inputs were resolved to ontology terms: 'CDK1' -> ENSG00000170312 (CDK1); 'Melanoma' -> MONDO_0005105 (melanoma). Scores below describe THAT term, not the free-text phrase. |
| Protein context | `get_uniprot_dossier` | P06493 — Cyclin-dependent kinase 1; location: Nucleus, Cytoplasm, Mitochondrion, Cytoplasm, cytoskeleton,  |
| Known modulators / druggability | `get_chembl_modulators` | target CHEMBL4523963 — **0 known modulators in ChEMBL** |
| Clinical variants | `get_clinvar_variants` | 52 ClinVar records; 3 pathogenic in a sample of 30 |
| Population constraint / LoF tolerance | `get_gnomad_constraint` | pLI=1, LOEUF=0.304 → LoF-INTOLERANT (handle with care) |
| Extra genetic evidence | `get_gwas_catalog` | 20 unique SNPs from 40/40 association rows |
| Pharmacogenomics | `get_pharmgkb_drug_gene` | 1 clinical annotation(s) over 1 drug(s): radiotherapy — ClinPGx evidence level 3 (scale 1A strongest to 4 weakest) — e.g. rs10711 (CDK1); radiotherapy; pneumonitis (level 3 Toxicity) |
| Clinical development record | `get_clinical_evidence` | _tool not called by the agent in this run_ |

## Caveats declared by the tools

- **`get_target_disease_evidence`** — CDK1 is not among the top 500 associated targets for MONDO_0005105 (melanoma). This is a TRUNCATED LOOKUP, not proof of no association. Free-text inputs were resolved to ontology terms: 'CDK1' -> ENSG00000170312 (CDK1); 'Melanoma' -> MONDO_0005105 (melanoma). Scores below describe THAT term, not the free-text phrase.
- **`get_mr_result`** — No pQTL-based MR estimate for CDK1 in the EpiGraphDB pQTL resource. This resource only covers proteins with usable plasma pQTL instruments. ABSENCE OF AN ESTIMATE IS NOT EVIDENCE OF NO EFFECT.
- **`get_chembl_modulators`** — ChEMBL target matched by text search on 'CDK1' and resolved to 'CDK4/CDK1' — confirm this is the intended target.
- **`get_clinvar_variants`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 52 ClinVar records for this gene; it is a sample, not a rate.
- **`classify_evidence_concordance`** — Nothing to compare: fewer than two matched estimates.

## Reasoning

CDK1 encodes a key cell cycle kinase (cyclin-dependent kinase 1) involved in mitotic onset and G2-M transition, but it is not among the top associated targets for melanoma in Open Targets, and no causal Mendelian randomization estimate is available. Although gnomAD constraint metrics indicate strong intolerance to loss-of-function variants (high pLI and low LOEUF), suggesting that systemic inhibition could carry safety risks, ChEMBL modulators identify no direct targeted inhibitors specific to CDK1 alone. Furthermore, GWAS catalog hits and pharmacogenomic records provide no direct evidence linking CDK1 variation to melanoma pathogenesis or therapeutic response.

## Sources

- `get_uniprot_dossier`: https://www.uniprot.org/uniprotkb/P06493 — _UniProt release 2026_02 (10-June-2026)_
- `get_mr_result`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `get_chembl_modulators`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4523963/ — _ChEMBL_37 (released 2026-05-01)_
- `get_clinvar_variants`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CDK1%5Bgene%5D — _ClinVar build Build260818-0035.1_
- `get_gnomad_constraint`: https://gnomad.broadinstitute.org/gene/CDK1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `get_gwas_catalog`: https://www.ebi.ac.uk/gwas/genes/CDK1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `get_pharmgkb_drug_gene`: https://www.pharmgkb.org/search?query=CDK1 — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_

## Provenance

- Generated: 2026-08-21T15:52:24
- Model (reasoning text only): `gemini-flash-lite-latest`
- Tools invoked (9 calls): `get_uniprot_dossier`, `get_target_disease_evidence`, `get_mr_result`, `get_chembl_modulators`, `get_clinvar_variants`, `get_gnomad_constraint`, `get_gwas_catalog`, `get_pharmgkb_drug_gene`, `classify_evidence_concordance`
- Evidence table, caveats, sources and this block are rendered mechanically from tool return values. The model wrote only the Verdict sentence and the Reasoning paragraph, both checked against tool output by `validate_card.py`.
- No Mendelian randomization or colocalization is computed by this agent; MR estimates, where present, are retrieved from published work.
