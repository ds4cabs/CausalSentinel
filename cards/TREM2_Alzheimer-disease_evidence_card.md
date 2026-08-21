# Target Evidence Card — TREM2 × Alzheimer disease

**Verdict:** GO — TREM2 shows strong genetic and literature associations with Alzheimer disease, supported by loss-of-function tolerance indicating safety for therapeutic modulation.

> **You asked about "Alzheimer disease". This card scored MONDO_0004975 — Alzheimer disease.** If those are not the same thing, every number below answers a different question.
> **The druggability row is about ChEMBL target "Triggering receptor expressed on myeloid cells 2" (CHEMBL6196124),** matched by text search. If that is not the molecular target you meant, that row is about something else.

## Evidence concordance — classified by rule, not written by the model

- Sources: EpiGraphDB — protein present, no estimate for THIS disease · Europe PMC — NOT checked in this run · Semantic Scholar — NOT checked in this run · MR-KG — NOT checked in this run

## Evidence

| Evidence | Tool | Result |
|---|---|---|
| Causal effect (MR) — retrieved, not computed | `get_mr_result` | **not available** — no pQTL MR estimate for this protein in the resource (absence of an estimate is not evidence of no effect) |
| Target–disease association | `get_target_disease_evidence` | overall score=0.558 (literature=0.994, animal_model=0.288, genetic_association=0.862) |
| Protein context | `get_uniprot_dossier` | Q9NZC2 — Triggering receptor expressed on myeloid cells 2; location: Cell membrane, Secreted, Secreted |
| Known modulators / druggability | `get_chembl_modulators` | target CHEMBL6196124 — **0 known modulators in ChEMBL** |
| Clinical variants | `get_clinvar_variants` | 202 ClinVar records; 5 pathogenic in a sample of 30 |
| Population constraint / LoF tolerance | `get_gnomad_constraint` | pLI=7.9e-07, LOEUF=1.27 → LoF-tolerant |
| Extra genetic evidence | `get_gwas_catalog` | 70 unique SNPs from 140/140 association rows |
| Pharmacogenomics | `get_pharmgkb_drug_gene` | **not available** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene). |
| Clinical development record | `get_clinical_evidence` | **not available** — No drug or clinical candidate against TREM2 in Open Targets. An empty clinical record means the clinic has not filed results against this target — NOT that the target is bad, and not that nothing was ever tried outside registries. |

## Caveats declared by the tools

- **`get_target_disease_evidence`** — Free-text inputs were resolved to ontology terms: 'TREM2' -> ENSG00000095970 (TREM2); 'Alzheimer disease' -> MONDO_0004975 (Alzheimer disease). Scores below describe THAT term, not the free-text phrase.
- **`get_chembl_modulators`** — ChEMBL target matched by text search on 'TREM2' and resolved to 'Triggering receptor expressed on myeloid cells 2' — confirm this is the intended target.
- **`get_mr_result`** — TREM2 HAS pQTL MR estimates in this resource, but NONE matched the requested disease 'Alzheimer disease'. The other outcomes are listed for context only — do not present them as evidence about 'Alzheimer disease'.
- **`get_clinvar_variants`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 202 ClinVar records for this gene; it is a sample, not a rate.
- **`get_pharmgkb_drug_gene`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`get_clinical_evidence`** — No drug or clinical candidate against TREM2 in Open Targets. An empty clinical record means the clinic has not filed results against this target — NOT that the target is bad, and not that nothing was ever tried outside registries.
- **`classify_evidence_concordance`** — Nothing to compare: fewer than two matched estimates.

## Reasoning

Open Targets data reveals a strong overall association score and high genetic and literature evidence for TREM2 in Alzheimer disease. The protein functions as a microglial receptor mediating amyloid-beta uptake and degradation, aligning directly with disease pathology. Although no pre-computed Mendelian randomization estimate matching Alzheimer disease was available from the EpiGraphDB resource and no clinical modulators are currently cataloged in ChEMBL or Open Targets clinical evidence, ClinVar records and gnomAD constraint metrics indicate the gene is loss-of-function tolerant. Furthermore, GWAS Catalog mapping identifies multiple associated SNPs, reinforcing the genetic link.

## Sources

- `get_uniprot_dossier`: https://www.uniprot.org/uniprotkb/Q9NZC2 — _UniProt release 2026_02 (10-June-2026)_
- `get_target_disease_evidence`: https://platform.opentargets.org/evidence/ENSG00000095970/MONDO_0004975 — _Open Targets data release 26.06_
- `get_chembl_modulators`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL6196124/ — _ChEMBL_37 (released 2026-05-01)_
- `get_mr_result`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `get_clinvar_variants`: https://www.ncbi.nlm.nih.gov/clinvar/?term=TREM2%5Bgene%5D — _ClinVar build Build260818-0035.1_
- `get_gnomad_constraint`: https://gnomad.broadinstitute.org/gene/TREM2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `get_gwas_catalog`: https://www.ebi.ac.uk/gwas/genes/TREM2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `get_clinical_evidence`: https://platform.opentargets.org/target/ENSG00000095970 — _Open Targets data release 26.06_

## Provenance

- Generated: 2026-08-21T15:34:04
- Model (reasoning text only): `gemini-flash-lite-latest`
- Tools invoked (10 calls): `get_uniprot_dossier`, `get_target_disease_evidence`, `get_chembl_modulators`, `get_mr_result`, `get_clinvar_variants`, `get_gnomad_constraint`, `get_gwas_catalog`, `get_pharmgkb_drug_gene`, `get_clinical_evidence`, `classify_evidence_concordance`
- Evidence table, caveats, sources and this block are rendered mechanically from tool return values. The model wrote only the Verdict sentence and the Reasoning paragraph, both checked against tool output by `validate_card.py`.
- No Mendelian randomization or colocalization is computed by this agent; MR estimates, where present, are retrieved from published work.
