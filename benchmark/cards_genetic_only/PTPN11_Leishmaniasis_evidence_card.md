# Target Evidence Card — PTPN11 × Leishmaniasis

**Verdict:** INSUFFICIENT EVIDENCE — there is currently no direct evidence linking PTPN11 to leishmaniasis and no available causal estimate.

> **You asked about "Leishmaniasis". This card scored MONDO_0011989 — leishmaniasis.** If those are not the same thing, every number below answers a different question.
> **The druggability row is about ChEMBL target "Tyrosine-protein phosphatase non-receptor type 11" (CHEMBL3864),** matched by text search. If that is not the molecular target you meant, that row is about something else.

## Evidence concordance — classified by rule, not written by the model

- Sources: EpiGraphDB — no pQTL instrument · Europe PMC — NOT checked in this run · Semantic Scholar — NOT checked in this run · MR-KG — NOT checked in this run

## Evidence

| Evidence | Tool | Result |
|---|---|---|
| Causal effect (MR) — retrieved, not computed | `get_mr_result` | **not available** — no pQTL MR estimate for this protein in the resource (absence of an estimate is not evidence of no effect) |
| Target–disease association | `get_target_disease_evidence` | **not available** — PTPN11 is not among the top 500 associated targets for MONDO_0011989 (leishmaniasis). This is a TRUNCATED LOOKUP, not proof of no association. Free-text inputs were resolved to ontology terms: 'PTPN11' -> ENSG00000179295 (PTPN11); 'Leishmaniasis' -> MONDO_0011989 (leishmaniasis). Scores below describe THAT term, not the free-text phrase. |
| Protein context | `get_uniprot_dossier` | Q06124 — Tyrosine-protein phosphatase non-receptor type 11; location: Cytoplasm, Nucleus |
| Known modulators / druggability | `get_chembl_modulators` | 1 known modulators (INHIBITOR) |
| Clinical variants | `get_clinvar_variants` | 1379 ClinVar records; 1 pathogenic in a sample of 30 |
| Population constraint / LoF tolerance | `get_gnomad_constraint` | pLI=1, LOEUF=0.15 → LoF-INTOLERANT (handle with care) |
| Extra genetic evidence | `get_gwas_catalog` | 110 unique SNPs from 223/223 association rows |
| Pharmacogenomics | `get_pharmgkb_drug_gene` | **not available** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene). |
| Clinical development record | `get_clinical_evidence` | _tool not called by the agent in this run_ |

## Caveats declared by the tools

- **`get_target_disease_evidence`** — PTPN11 is not among the top 500 associated targets for MONDO_0011989 (leishmaniasis). This is a TRUNCATED LOOKUP, not proof of no association. Free-text inputs were resolved to ontology terms: 'PTPN11' -> ENSG00000179295 (PTPN11); 'Leishmaniasis' -> MONDO_0011989 (leishmaniasis). Scores below describe THAT term, not the free-text phrase.
- **`get_mr_result`** — No pQTL-based MR estimate for PTPN11 in the EpiGraphDB pQTL resource. This resource only covers proteins with usable plasma pQTL instruments. ABSENCE OF AN ESTIMATE IS NOT EVIDENCE OF NO EFFECT.
- **`get_chembl_modulators`** — ChEMBL target matched by text search on 'PTPN11' and resolved to 'Tyrosine-protein phosphatase non-receptor type 11' — confirm this is the intended target.
- **`get_clinvar_variants`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 1379 ClinVar records for this gene; it is a sample, not a rate.
- **`get_pharmgkb_drug_gene`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`classify_evidence_concordance`** — Nothing to compare: fewer than two matched estimates.

## Reasoning

Open Targets shows PTPN11 is not among the top associated targets for leishmaniasis, and no Mendelian randomization estimate is available for this disease-protein pair. While PTPN11 is a well-studied tyrosine-protein phosphatase with known modulators in ChEMBL and multiple GWAS catalog associations, gnomAD constraint metrics indicate high loss-of-function intolerance, presenting potential safety risks if inhibited. Furthermore, there are no pharmacogenomic annotations in PharmGKB for PTPN11.
```

## Sources

- `get_uniprot_dossier`: https://www.uniprot.org/uniprotkb/Q06124 — _UniProt release 2026_02 (10-June-2026)_
- `get_mr_result`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `get_chembl_modulators`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3864/ — _ChEMBL_37 (released 2026-05-01)_
- `get_clinvar_variants`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PTPN11%5Bgene%5D — _ClinVar build Build260818-0035.1_
- `get_gnomad_constraint`: https://gnomad.broadinstitute.org/gene/PTPN11 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `get_gwas_catalog`: https://www.ebi.ac.uk/gwas/genes/PTPN11 — _GWAS Catalog REST (live; release not exposed by this endpoint)_

## Provenance

- Generated: 2026-08-21T15:45:51
- Model (reasoning text only): `gemini-flash-lite-latest`
- Tools invoked (9 calls): `get_uniprot_dossier`, `get_target_disease_evidence`, `get_mr_result`, `get_chembl_modulators`, `get_clinvar_variants`, `get_gnomad_constraint`, `get_gwas_catalog`, `get_pharmgkb_drug_gene`, `classify_evidence_concordance`
- Evidence table, caveats, sources and this block are rendered mechanically from tool return values. The model wrote only the Verdict sentence and the Reasoning paragraph, both checked against tool output by `validate_card.py`.
- No Mendelian randomization or colocalization is computed by this agent; MR estimates, where present, are retrieved from published work.
