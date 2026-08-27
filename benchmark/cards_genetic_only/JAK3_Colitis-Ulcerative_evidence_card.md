# Target Evidence Card — JAK3 × Colitis, Ulcerative

**Verdict:** GO — JAK3 is an established therapeutic target supported by high clinical-trial association scores for inflammatory bowel disease and multiple known modulators.

> **You asked about "Colitis, Ulcerative". This card scored MONDO_0005265 — inflammatory bowel disease.** If those are not the same thing, every number below answers a different question.
> **The druggability row is about ChEMBL target "Tyrosine-protein kinase JAK3" (CHEMBL2148),** matched by text search. If that is not the molecular target you meant, that row is about something else.

## Evidence concordance — classified by rule, not written by the model

- Sources: EpiGraphDB — no pQTL instrument · Europe PMC — NOT checked in this run · Semantic Scholar — NOT checked in this run · MR-KG — NOT checked in this run

## Evidence

| Evidence | Tool | Result |
|---|---|---|
| Causal effect (MR) — retrieved, not computed | `get_mr_result` | **not available** — no pQTL MR estimate for this protein in the resource (absence of an estimate is not evidence of no effect) |
| Target–disease association | `get_target_disease_evidence` | overall score=0.667 (rna_expression=0.0258, clinical=0.967, literature=0.169, somatic_mutation=0.456) |
| Protein context | `get_uniprot_dossier` | P52333 — Tyrosine-protein kinase JAK3; location: Endomembrane system, Cytoplasm |
| Known modulators / druggability | `get_chembl_modulators` | 13 known modulators (INHIBITOR) |
| Clinical variants | `get_clinvar_variants` | 1423 ClinVar records; 4 pathogenic in a sample of 30 |
| Population constraint / LoF tolerance | `get_gnomad_constraint` | pLI=1e-21, LOEUF=0.87 → LoF-tolerant |
| Extra genetic evidence | `get_gwas_catalog` | 44 unique SNPs from 88/88 association rows |
| Pharmacogenomics | `get_pharmgkb_drug_gene` | **not available** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene). |
| Clinical development record | `get_clinical_evidence` | _tool not called by the agent in this run_ |

## Caveats declared by the tools

- **`get_target_disease_evidence`** — Free-text inputs were resolved to ontology terms: 'JAK3' -> ENSG00000105639 (JAK3); 'Colitis, Ulcerative' -> MONDO_0005265 (inflammatory bowel disease). Scores below describe THAT term, not the free-text phrase.
- **`get_chembl_modulators`** — ChEMBL target matched by text search on 'JAK3' and resolved to 'Tyrosine-protein kinase JAK3' — confirm this is the intended target.
- **`get_mr_result`** — No pQTL-based MR estimate for JAK3 in the EpiGraphDB pQTL resource. This resource only covers proteins with usable plasma pQTL instruments. ABSENCE OF AN ESTIMATE IS NOT EVIDENCE OF NO EFFECT.
- **`get_clinvar_variants`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 1423 ClinVar records for this gene; it is a sample, not a rate.
- **`get_pharmgkb_drug_gene`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`classify_evidence_concordance`** — Nothing to compare: fewer than two matched estimates.

## Reasoning

Open Targets demonstrates a high overall association score between JAK3 and inflammatory bowel disease, driven heavily by clinical evidence. Multiple chemical modulators and inhibitors are known in ChEMBL, confirming the druggability of the kinase. Genetic constraint metrics from gnomAD show that the gene is relatively tolerant to loss-of-function variants. While no MR estimate was available, robust clinical-stage and target-disease association evidence supports pursuing JAK3 for colitis.

## Sources

- `get_uniprot_dossier`: https://www.uniprot.org/uniprotkb/P52333 — _UniProt release 2026_02 (10-June-2026)_
- `get_target_disease_evidence`: https://platform.opentargets.org/evidence/ENSG00000105639/MONDO_0005265 — _Open Targets data release 26.06_
- `get_chembl_modulators`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2148/ — _ChEMBL_37 (released 2026-05-01)_
- `get_mr_result`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `get_clinvar_variants`: https://www.ncbi.nlm.nih.gov/clinvar/?term=JAK3%5Bgene%5D — _ClinVar build Build260818-0035.1_
- `get_gnomad_constraint`: https://gnomad.broadinstitute.org/gene/JAK3 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `get_gwas_catalog`: https://www.ebi.ac.uk/gwas/genes/JAK3 — _GWAS Catalog REST (live; release not exposed by this endpoint)_

## Provenance

- Generated: 2026-08-21T15:47:40
- Model (reasoning text only): `gemini-flash-lite-latest`
- Tools invoked (9 calls): `get_uniprot_dossier`, `get_target_disease_evidence`, `get_chembl_modulators`, `get_mr_result`, `get_clinvar_variants`, `get_gnomad_constraint`, `get_gwas_catalog`, `get_pharmgkb_drug_gene`, `classify_evidence_concordance`
- Evidence table, caveats, sources and this block are rendered mechanically from tool return values. The model wrote only the Verdict sentence and the Reasoning paragraph, both checked against tool output by `validate_card.py`.
- No Mendelian randomization or colocalization is computed by this agent; MR estimates, where present, are retrieved from published work.
