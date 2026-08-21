# Target Evidence Card — TNF × Dermatitis, Seborrheic

**Verdict:** INSUFFICIENT EVIDENCE — although extensive genetic associations and pharmacogenomic data link TNF to various inflammatory conditions, no causal Mendelian randomization estimate is available for seborrheic dermatitis.

> **You asked about "Dermatitis, Seborrheic". This card scored MONDO_0002406 — dermatitis.** If those are not the same thing, every number below answers a different question.
> **The druggability row is about ChEMBL target "TNF receptor-associated factor 6" (CHEMBL3588728),** matched by text search. If that is not the molecular target you meant, that row is about something else.

## Evidence concordance — classified by rule, not written by the model

- Sources: EpiGraphDB — no pQTL instrument · Europe PMC — NOT checked in this run · Semantic Scholar — NOT checked in this run · MR-KG — NOT checked in this run

## Evidence

| Evidence | Tool | Result |
|---|---|---|
| Causal effect (MR) — retrieved, not computed | `get_mr_result` | **not available** — no pQTL MR estimate for this protein in the resource (absence of an estimate is not evidence of no effect) |
| Target–disease association | `get_target_disease_evidence` | overall score=0.644 (literature=0.989, animal_model=0.644, clinical=0.995) |
| Protein context | `get_uniprot_dossier` | P01375 — Tumor necrosis factor; location: Cell membrane, Membrane, Secreted, Secreted, Secreted |
| Known modulators / druggability | `get_chembl_modulators` | target CHEMBL3588728 — **0 known modulators in ChEMBL** |
| Clinical variants | `get_clinvar_variants` | 36 ClinVar records; 7 pathogenic in a sample of 30 |
| Population constraint / LoF tolerance | `get_gnomad_constraint` | pLI=0.84, LOEUF=0.603 → LoF-tolerant |
| Extra genetic evidence | `get_gwas_catalog` | 507 unique SNPs from 1372/1372 association rows |
| Pharmacogenomics | `get_pharmgkb_drug_gene` | 18 clinical annotation(s) over 20 drug(s): Tumor necrosis factor alpha (TNF-alpha) inhibitors, aspirin, atorvastatin, carbamazepine +16 more — ClinPGx evidence level 2B/3/4 (scale 1A strongest to 4 weakest) — e.g. rs1800629 (TNF); Tumor necrosis factor alpha (TNF-alpha) inhibitors (level 3 Efficacy) |
| Clinical development record | `get_clinical_evidence` | _tool not called by the agent in this run_ |

## Caveats declared by the tools

- **`get_target_disease_evidence`** — Free-text inputs were resolved to ontology terms: 'TNF' -> ENSG00000232810 (TNF); 'Dermatitis, Seborrheic' -> MONDO_0002406 (dermatitis). Scores below describe THAT term, not the free-text phrase.
- **`get_chembl_modulators`** — ChEMBL target matched by text search on 'TNF' and resolved to 'TNF receptor-associated factor 6' — confirm this is the intended target.
- **`get_mr_result`** — No pQTL-based MR estimate for TNF in the EpiGraphDB pQTL resource. This resource only covers proteins with usable plasma pQTL instruments. ABSENCE OF AN ESTIMATE IS NOT EVIDENCE OF NO EFFECT.
- **`get_clinvar_variants`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 36 ClinVar records for this gene; it is a sample, not a rate.
- **`classify_evidence_concordance`** — Nothing to compare: fewer than two matched estimates.

## Reasoning

Open Targets evidence for TNF associates it with the resolved ontology term dermatitis. However, no Mendelian randomization estimate is available for this target and disease pairing in EpiGraphDB. Although the GWAS catalog lists numerous associated SNPs for TNF, and PharmGKB documents multiple pharmacogenomic annotations with TNF-alpha inhibitors, the absence of disease-specific causal evidence prevents a definitive assessment. Furthermore, constraint metrics and ClinVar variant records indicate potential safety and genetic considerations, but do not establish a direct causal mechanism for seborrheic dermatitis.

## Sources

- `get_uniprot_dossier`: https://www.uniprot.org/uniprotkb/P01375 — _UniProt release 2026_02 (10-June-2026)_
- `get_target_disease_evidence`: https://platform.opentargets.org/evidence/ENSG00000232810/MONDO_0002406 — _Open Targets data release 26.06_
- `get_chembl_modulators`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3588728/ — _ChEMBL_37 (released 2026-05-01)_
- `get_mr_result`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `get_clinvar_variants`: https://www.ncbi.nlm.nih.gov/clinvar/?term=TNF%5Bgene%5D — _ClinVar build Build260818-0035.1_
- `get_gnomad_constraint`: https://gnomad.broadinstitute.org/gene/TNF — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `get_gwas_catalog`: https://www.ebi.ac.uk/gwas/genes/TNF — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `get_pharmgkb_drug_gene`: https://www.pharmgkb.org/search?query=TNF — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_

## Provenance

- Generated: 2026-08-21T15:45:32
- Model (reasoning text only): `gemini-flash-lite-latest`
- Tools invoked (9 calls): `get_uniprot_dossier`, `get_target_disease_evidence`, `get_chembl_modulators`, `get_mr_result`, `get_clinvar_variants`, `get_gnomad_constraint`, `get_gwas_catalog`, `get_pharmgkb_drug_gene`, `classify_evidence_concordance`
- Evidence table, caveats, sources and this block are rendered mechanically from tool return values. The model wrote only the Verdict sentence and the Reasoning paragraph, both checked against tool output by `validate_card.py`.
- No Mendelian randomization or colocalization is computed by this agent; MR estimates, where present, are retrieved from published work.
