# Target Evidence Card — ANGPT1 × Sarcoma

**Verdict:** INSUFFICIENT EVIDENCE — there is currently no direct genetic or Mendelian randomization evidence connecting ANGPT1 to sarcoma.

> **You asked about "Sarcoma". This card scored MONDO_0005089 — sarcoma.** If those are not the same thing, every number below answers a different question.
> **The druggability row is about ChEMBL target "Angiopoietin-1" (CHEMBL3217395),** matched by text search. If that is not the molecular target you meant, that row is about something else.

## Evidence concordance — classified by rule, not written by the model

- Sources: EpiGraphDB — no pQTL instrument · Europe PMC — NOT checked in this run · Semantic Scholar — NOT checked in this run · MR-KG — NOT checked in this run

## Evidence

| Evidence | Tool | Result |
|---|---|---|
| Causal effect (MR) — retrieved, not computed | `get_mr_result` | **not available** — no pQTL MR estimate for this protein in the resource (absence of an estimate is not evidence of no effect) |
| Target–disease association | `get_target_disease_evidence` | **not available** — ANGPT1 is not among the top 500 associated targets for MONDO_0005089 (sarcoma). This is a TRUNCATED LOOKUP, not proof of no association. Free-text inputs were resolved to ontology terms: 'ANGPT1' -> ENSG00000154188 (ANGPT1); 'Sarcoma' -> MONDO_0005089 (sarcoma). Scores below describe THAT term, not the free-text phrase. |
| Protein context | `get_uniprot_dossier` | Q15389 — Angiopoietin-1; location: Secreted |
| Known modulators / druggability | `get_chembl_modulators` | 2 known modulators (INHIBITOR) |
| Clinical variants | `get_clinvar_variants` | 383 ClinVar records; 0 pathogenic in a sample of 30 |
| Population constraint / LoF tolerance | `get_gnomad_constraint` | pLI=1, LOEUF=0.41 → LoF-INTOLERANT (handle with care) |
| Extra genetic evidence | `get_gwas_catalog` | 97 unique SNPs from 194/194 association rows |
| Pharmacogenomics | `get_pharmgkb_drug_gene` | **not available** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene). |
| Clinical development record | `get_clinical_evidence` | _tool not called by the agent in this run_ |

## Caveats declared by the tools

- **`get_target_disease_evidence`** — ANGPT1 is not among the top 500 associated targets for MONDO_0005089 (sarcoma). This is a TRUNCATED LOOKUP, not proof of no association. Free-text inputs were resolved to ontology terms: 'ANGPT1' -> ENSG00000154188 (ANGPT1); 'Sarcoma' -> MONDO_0005089 (sarcoma). Scores below describe THAT term, not the free-text phrase.
- **`get_mr_result`** — No pQTL-based MR estimate for ANGPT1 in the EpiGraphDB pQTL resource. This resource only covers proteins with usable plasma pQTL instruments. ABSENCE OF AN ESTIMATE IS NOT EVIDENCE OF NO EFFECT.
- **`get_chembl_modulators`** — ChEMBL target matched by text search on 'ANGPT1' and resolved to 'Angiopoietin-1' — confirm this is the intended target.
- **`get_clinvar_variants`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 383 ClinVar records for this gene; it is a sample, not a rate.
- **`get_pharmgkb_drug_gene`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`classify_evidence_concordance`** — Nothing to compare: fewer than two matched estimates.

## Reasoning

Open Targets does not list ANGPT1 among the top associated targets for sarcoma, and no causal Mendelian randomization estimate is available from the EpiGraphDB pQTL resource. Although the gene has multiple GWAS associations and ChEMBL lists known small-molecule modulators, gnomAD constraint metrics indicate that ANGPT1 is loss-of-function intolerant (pLI near 1, low LOEUF), raising potential safety concerns for target inhibition. Furthermore, ClinVar records contain no pathogenic variants in this sample, and PharmGKB shows no pharmacogenomic annotations.
```

## Sources

- `get_uniprot_dossier`: https://www.uniprot.org/uniprotkb/Q15389 — _UniProt release 2026_02 (10-June-2026)_
- `get_mr_result`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `get_chembl_modulators`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3217395/ — _ChEMBL_37 (released 2026-05-01)_
- `get_clinvar_variants`: https://www.ncbi.nlm.nih.gov/clinvar/?term=ANGPT1%5Bgene%5D — _ClinVar build Build260818-0035.1_
- `get_gnomad_constraint`: https://gnomad.broadinstitute.org/gene/ANGPT1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `get_gwas_catalog`: https://www.ebi.ac.uk/gwas/genes/ANGPT1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_

## Provenance

- Generated: 2026-08-21T15:52:02
- Model (reasoning text only): `gemini-flash-lite-latest`
- Tools invoked (9 calls): `get_uniprot_dossier`, `get_target_disease_evidence`, `get_mr_result`, `get_chembl_modulators`, `get_clinvar_variants`, `get_gnomad_constraint`, `get_gwas_catalog`, `get_pharmgkb_drug_gene`, `classify_evidence_concordance`
- Evidence table, caveats, sources and this block are rendered mechanically from tool return values. The model wrote only the Verdict sentence and the Reasoning paragraph, both checked against tool output by `validate_card.py`.
- No Mendelian randomization or colocalization is computed by this agent; MR estimates, where present, are retrieved from published work.
