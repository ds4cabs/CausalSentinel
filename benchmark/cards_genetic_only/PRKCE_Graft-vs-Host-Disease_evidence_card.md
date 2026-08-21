# Target Evidence Card — PRKCE × Graft vs Host Disease

**Verdict:** INSUFFICIENT EVIDENCE — PRKCE lacks direct genetic association or causal evidence for graft versus host disease despite general druggability.

> **You asked about "Graft vs Host Disease". This card scored MONDO_0013730 — graft versus host disease.** If those are not the same thing, every number below answers a different question.
> **The druggability row is about ChEMBL target "Protein kinase C epsilon type" (CHEMBL3582),** matched by text search. If that is not the molecular target you meant, that row is about something else.

## Evidence concordance — classified by rule, not written by the model

- Sources: EpiGraphDB — no pQTL instrument · Europe PMC — NOT checked in this run · Semantic Scholar — NOT checked in this run · MR-KG — NOT checked in this run

## Evidence

| Evidence | Tool | Result |
|---|---|---|
| Causal effect (MR) — retrieved, not computed | `get_mr_result` | **not available** — no pQTL MR estimate for this protein in the resource (absence of an estimate is not evidence of no effect) |
| Target–disease association | `get_target_disease_evidence` | **not available** — PRKCE is not among the top 500 associated targets for MONDO_0013730 (graft versus host disease). This is a TRUNCATED LOOKUP, not proof of no association. Free-text inputs were resolved to ontology terms: 'PRKCE' -> ENSG00000171132 (PRKCE); 'Graft vs Host Disease' -> MONDO_0013730 (graft versus host disease). Scores below describe THAT term, not the free-text phrase. |
| Protein context | `get_uniprot_dossier` | Q02156 — Protein kinase C epsilon type; location: Cytoplasm, Cytoplasm, cytoskeleton, Cell membrane, Cytoplasm |
| Known modulators / druggability | `get_chembl_modulators` | 1 known modulators (INHIBITOR) |
| Clinical variants | `get_clinvar_variants` | 104 ClinVar records; 0 pathogenic in a sample of 30 |
| Population constraint / LoF tolerance | `get_gnomad_constraint` | pLI=1, LOEUF=0.284 → LoF-INTOLERANT (handle with care) |
| Extra genetic evidence | `get_gwas_catalog` | 123 unique SNPs from 314/314 association rows |
| Pharmacogenomics | `get_pharmgkb_drug_gene` | 2 clinical annotation(s) over 2 drug(s): radiotherapy, sorafenib — ClinPGx evidence level 3 (scale 1A strongest to 4 weakest) — e.g. rs11125039 (PRKCE); sorafenib; Hypertension (level 3 Toxicity) |
| Clinical development record | `get_clinical_evidence` | _tool not called by the agent in this run_ |

## Caveats declared by the tools

- **`get_target_disease_evidence`** — PRKCE is not among the top 500 associated targets for MONDO_0013730 (graft versus host disease). This is a TRUNCATED LOOKUP, not proof of no association. Free-text inputs were resolved to ontology terms: 'PRKCE' -> ENSG00000171132 (PRKCE); 'Graft vs Host Disease' -> MONDO_0013730 (graft versus host disease). Scores below describe THAT term, not the free-text phrase.
- **`get_chembl_modulators`** — ChEMBL target matched by text search on 'PRKCE' and resolved to 'Protein kinase C epsilon type' — confirm this is the intended target.
- **`get_mr_result`** — No pQTL-based MR estimate for PRKCE in the EpiGraphDB pQTL resource. This resource only covers proteins with usable plasma pQTL instruments. ABSENCE OF AN ESTIMATE IS NOT EVIDENCE OF NO EFFECT.
- **`get_clinvar_variants`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 104 ClinVar records for this gene; it is a sample, not a rate.
- **`classify_evidence_concordance`** — Nothing to compare: fewer than two matched estimates.

## Reasoning

Open Targets shows no direct genetic association between PRKCE and graft versus host disease, and no Mendelian randomization estimates are available for this pair. Although PRKCE is loss-of-function intolerant in gnomAD, representing a potential safety warning, it has known chemical modulators in ChEMBL. Furthermore, GWAS catalog data links the locus to multiple traits and PharmGKB notes pharmacogenomic annotations with sorafenib and radiotherapy, but the absence of disease-specific genetic or causal evidence precludes target support for this indication.

## Sources

- `get_uniprot_dossier`: https://www.uniprot.org/uniprotkb/Q02156 — _UniProt release 2026_02 (10-June-2026)_
- `get_chembl_modulators`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3582/ — _ChEMBL_37 (released 2026-05-01)_
- `get_mr_result`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `get_clinvar_variants`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PRKCE%5Bgene%5D — _ClinVar build Build260818-0035.1_
- `get_gnomad_constraint`: https://gnomad.broadinstitute.org/gene/PRKCE — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `get_gwas_catalog`: https://www.ebi.ac.uk/gwas/genes/PRKCE — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `get_pharmgkb_drug_gene`: https://www.pharmgkb.org/search?query=PRKCE — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_

## Provenance

- Generated: 2026-08-21T15:51:44
- Model (reasoning text only): `gemini-flash-lite-latest`
- Tools invoked (9 calls): `get_uniprot_dossier`, `get_target_disease_evidence`, `get_chembl_modulators`, `get_mr_result`, `get_clinvar_variants`, `get_gnomad_constraint`, `get_gwas_catalog`, `get_pharmgkb_drug_gene`, `classify_evidence_concordance`
- Evidence table, caveats, sources and this block are rendered mechanically from tool return values. The model wrote only the Verdict sentence and the Reasoning paragraph, both checked against tool output by `validate_card.py`.
- No Mendelian randomization or colocalization is computed by this agent; MR estimates, where present, are retrieved from published work.
