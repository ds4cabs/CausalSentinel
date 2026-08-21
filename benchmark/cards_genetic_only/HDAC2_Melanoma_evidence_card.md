# Target Evidence Card — HDAC2 × Melanoma

**Verdict:** INSUFFICIENT EVIDENCE — HDAC2 is not among the top associated targets for melanoma in Open Targets and lacks causal Mendelian randomization evidence.

> **You asked about "Melanoma". This card scored MONDO_0005105 — melanoma.** If those are not the same thing, every number below answers a different question.
> **The druggability row is about ChEMBL target "Histone deacetylase 2" (CHEMBL1937),** matched by text search. If that is not the molecular target you meant, that row is about something else.

## Evidence concordance — classified by rule, not written by the model

- Sources: EpiGraphDB — no pQTL instrument · Europe PMC — NOT checked in this run · Semantic Scholar — NOT checked in this run · MR-KG — NOT checked in this run

## Evidence

| Evidence | Tool | Result |
|---|---|---|
| Causal effect (MR) — retrieved, not computed | `get_mr_result` | **not available** — no pQTL MR estimate for this protein in the resource (absence of an estimate is not evidence of no effect) |
| Target–disease association | `get_target_disease_evidence` | **not available** — HDAC2 is not among the top 500 associated targets for MONDO_0005105 (melanoma). This is a TRUNCATED LOOKUP, not proof of no association. Free-text inputs were resolved to ontology terms: 'HDAC2' -> ENSG00000196591 (HDAC2); 'Melanoma' -> MONDO_0005105 (melanoma). Scores below describe THAT term, not the free-text phrase. |
| Protein context | `get_uniprot_dossier` | Q92769 — Histone deacetylase 2; location: Nucleus, Cytoplasm |
| Known modulators / druggability | `get_chembl_modulators` | 2 known modulators (INHIBITOR) |
| Clinical variants | `get_clinvar_variants` | 86 ClinVar records; 0 pathogenic in a sample of 30 |
| Population constraint / LoF tolerance | `get_gnomad_constraint` | pLI=1, LOEUF=0.153 → LoF-INTOLERANT (handle with care) |
| Extra genetic evidence | `get_gwas_catalog` | 17 unique SNPs from 34/34 association rows |
| Pharmacogenomics | `get_pharmgkb_drug_gene` | **not available** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene). |
| Clinical development record | `get_clinical_evidence` | _tool not called by the agent in this run_ |

## Caveats declared by the tools

- **`get_target_disease_evidence`** — HDAC2 is not among the top 500 associated targets for MONDO_0005105 (melanoma). This is a TRUNCATED LOOKUP, not proof of no association. Free-text inputs were resolved to ontology terms: 'HDAC2' -> ENSG00000196591 (HDAC2); 'Melanoma' -> MONDO_0005105 (melanoma). Scores below describe THAT term, not the free-text phrase.
- **`get_chembl_modulators`** — ChEMBL target matched by text search on 'HDAC2' and resolved to 'Histone deacetylase 2' — confirm this is the intended target.
- **`get_mr_result`** — No pQTL-based MR estimate for HDAC2 in the EpiGraphDB pQTL resource. This resource only covers proteins with usable plasma pQTL instruments. ABSENCE OF AN ESTIMATE IS NOT EVIDENCE OF NO EFFECT.
- **`get_clinvar_variants`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 86 ClinVar records for this gene; it is a sample, not a rate.
- **`get_pharmgkb_drug_gene`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`classify_evidence_concordance`** — Nothing to compare: fewer than two matched estimates.

## Reasoning

HDAC2 encodes a nuclear histone deacetylase involved in epigenetic repression and transcriptional regulation. Although small-molecule inhibitors are documented in ChEMBL, the target has no available causal estimate for melanoma from the EpiGraphDB pQTL resource, and Open Targets does not rank it among the top associated targets for melanoma. Furthermore, gnomAD constraint metrics indicate that HDAC2 is extremely loss-of-function intolerant (pLI = 1.0, low LOEUF), raising notable safety considerations for its inhibition.

## Sources

- `get_uniprot_dossier`: https://www.uniprot.org/uniprotkb/Q92769 — _UniProt release 2026_02 (10-June-2026)_
- `get_chembl_modulators`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL1937/ — _ChEMBL_37 (released 2026-05-01)_
- `get_mr_result`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `get_clinvar_variants`: https://www.ncbi.nlm.nih.gov/clinvar/?term=HDAC2%5Bgene%5D — _ClinVar build Build260818-0035.1_
- `get_gnomad_constraint`: https://gnomad.broadinstitute.org/gene/HDAC2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `get_gwas_catalog`: https://www.ebi.ac.uk/gwas/genes/HDAC2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_

## Provenance

- Generated: 2026-08-21T15:50:40
- Model (reasoning text only): `gemini-flash-lite-latest`
- Tools invoked (9 calls): `get_uniprot_dossier`, `get_target_disease_evidence`, `get_chembl_modulators`, `get_mr_result`, `get_clinvar_variants`, `get_gnomad_constraint`, `get_gwas_catalog`, `get_pharmgkb_drug_gene`, `classify_evidence_concordance`
- Evidence table, caveats, sources and this block are rendered mechanically from tool return values. The model wrote only the Verdict sentence and the Reasoning paragraph, both checked against tool output by `validate_card.py`.
- No Mendelian randomization or colocalization is computed by this agent; MR estimates, where present, are retrieved from published work.
