# Target Evidence Card — TREM2 × Alzheimer disease

**Verdict:** GO — TREM2 has robust genetic and functional evidence supporting its role in Alzheimer disease pathogenesis, despite the current lack of dedicated Mendelian randomization or chemical modulator records.

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

## Caveats declared by the tools

- **`get_target_disease_evidence`** — Free-text inputs were resolved to ontology terms: 'TREM2' -> ENSG00000095970 (TREM2); 'Alzheimer disease' -> MONDO_0004975 (Alzheimer disease). Scores below describe THAT term, not the free-text phrase.
- **`get_chembl_modulators`** — ChEMBL target matched by text search on 'TREM2' and resolved to 'Triggering receptor expressed on myeloid cells 2' — confirm this is the intended target.
- **`get_mr_result`** — TREM2 HAS pQTL MR estimates in this resource, but NONE matched the requested disease 'Alzheimer disease'. The other outcomes are listed for context only — do not present them as evidence about 'Alzheimer disease'.
- **`get_clinvar_variants`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 202 ClinVar records for this gene; it is a sample, not a rate.
- **`get_pharmgkb_drug_gene`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).

## Reasoning

Open Targets shows a strong genetic and literature association between TREM2 and Alzheimer disease. UniProt confirms its role as a microglial receptor that binds amyloid-beta and lipoprotein particles to mediate phagocytosis and immune response. ClinVar records pathogenic variants in the gene, and GWAS Catalog mapping demonstrates multiple associated SNPs. Although no ChEMBL modulators or disease-specific Mendelian randomization estimates are available, the extensive genetic and functional validation supports its pursuit as a target.

## Sources

- `get_uniprot_dossier`: https://www.uniprot.org/uniprotkb/Q9NZC2 — _UniProt release 2026_02 (10-June-2026)_
- `get_target_disease_evidence`: https://platform.opentargets.org/evidence/ENSG00000095970/MONDO_0004975 — _Open Targets data release 26.06_
- `get_chembl_modulators`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL6196124/ — _ChEMBL_37 (released 2026-05-01)_
- `get_mr_result`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `get_clinvar_variants`: https://www.ncbi.nlm.nih.gov/clinvar/?term=TREM2%5Bgene%5D — _ClinVar build Build260804-2105.1_
- `get_gnomad_constraint`: https://gnomad.broadinstitute.org/gene/TREM2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `get_gwas_catalog`: https://www.ebi.ac.uk/gwas/genes/TREM2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_

## Provenance

- Generated: 2026-08-07T06:23:44
- Model (reasoning text only): `gemini-flash-lite-latest`
- Tools invoked (8 calls): `get_uniprot_dossier`, `get_target_disease_evidence`, `get_chembl_modulators`, `get_mr_result`, `get_clinvar_variants`, `get_gnomad_constraint`, `get_gwas_catalog`, `get_pharmgkb_drug_gene`
- Evidence table, caveats, sources and this block are rendered mechanically from tool return values. The model wrote only the Verdict sentence and the Reasoning paragraph, both checked against tool output by `validate_card.py`.
- No Mendelian randomization or colocalization is computed by this agent; MR estimates, where present, are retrieved from published work.
