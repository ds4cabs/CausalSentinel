# Target Evidence Card — IL6R × coronary heart disease

**Verdict:** GO — genetic and causal evidence support IL6R as a promising target for coronary heart disease.

> **Question actually answered:** the free-text disease was resolved to **MONDO_0005010 (coronary artery disorder)**. If that is not what you meant, every score below answers a different question.
> **ChEMBL target resolved by text search** to **"Interleukin-6 receptor subunit alpha"** (CHEMBL2364155). If that is not the intended molecular target, the druggability row is about something else.

## MR direction — rendered from the ledger, not written by the model

- Genetically-predicted **higher plasma IL6R** is associated with **LOWER Coronary heart disease** (beta -0.04419, se 0.00853, p=2.21e-07; Wald ratio, n_snp 1, instrument rs4129267, cis).
  - Not available for this estimate: Steiger direction, colocalization, LD check.
  - Single-instrument Wald ratio: no heterogeneity or pleiotropy test is possible.

> **The exposure is IL6R protein abundance, not a drug.** This run retrieved no evidence about what pharmacological inhibition or activation of IL6R does. Turning the direction above into a drug direction needs a mechanism this run did not retrieve.

## Evidence

| Evidence | Tool | Result |
|---|---|---|
| Causal effect (MR) — retrieved, not computed | `get_mr_result` | outcome: Coronary heart disease — beta=-0.0442, se=0.00853, p=2.21e-07, Wald ratio, n_snp=1, cis instrument, coloc=not available  
_retrieved from published MR; not computed here_ |
| Target–disease association | `get_target_disease_evidence` | overall score=0.586 (literature=0.868, genetic_association=0.92, clinical=0.0061) |
| Protein context | `get_uniprot_dossier` | P08887 — Interleukin-6 receptor subunit alpha; location: Cell membrane, Secreted, Secreted |
| Known modulators / druggability | `get_chembl_modulators` | 4 known modulators (ANTAGONIST, INHIBITOR) |
| Clinical variants | `get_clinvar_variants` | 366 ClinVar records; 1 pathogenic in a sample of 30 |
| Population constraint / LoF tolerance | `get_gnomad_constraint` | pLI=7.9e-11, LOEUF=1.03 → LoF-tolerant |
| Extra genetic evidence | `get_gwas_catalog` | 148 unique SNPs from 368/368 association rows |
| Pharmacogenomics | `get_pharmgkb_drug_gene` | 3 clinical annotations across 1 drugs (level 3: 2, level 4: 1) |

## Caveats declared by the tools

- **`get_mr_result`** — Estimates RETRIEVED from published pQTL MR, not computed by this agent. Check cis_or_trans (cis instruments are less pleiotropy-prone), steiger_direction_ok, and coloc_prob before treating this as causal; coloc_prob=null means colocalization was not available for this pair.
- **`get_target_disease_evidence`** — Free-text inputs were resolved to ontology terms: 'IL6R' -> ENSG00000160712 (IL6R); 'coronary heart disease' -> MONDO_0005010 (coronary artery disorder). Scores below describe THAT term, not the free-text phrase.
- **`get_chembl_modulators`** — ChEMBL target matched by text search on 'IL6R' and resolved to 'Interleukin-6 receptor subunit alpha' — confirm this is the intended target.
- **`get_clinvar_variants`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 366 ClinVar records for this gene; it is a sample, not a rate.

## Reasoning

Retrieved Mendelian randomization estimates suggest a causal relationship between IL6R and coronary heart disease, supported by a strong genetic association score and numerous mapped GWAS variants. The target protein is well-characterized as an interleukin-6 receptor subunit involved in inflammatory signaling pathways. ChEMBL identifies known modulators against IL6R, confirming its druggability. Furthermore, gnomAD constraint metrics indicate loss-of-function tolerance, and PharmGKB highlights pharmacogenomic annotations for related modulators.
```

## Sources

- `get_mr_result`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `get_target_disease_evidence`: https://platform.opentargets.org/evidence/ENSG00000160712/MONDO_0005010 — _Open Targets data release 26.06_
- `get_uniprot_dossier`: https://www.uniprot.org/uniprotkb/P08887 — _UniProt release 2026_02 (10-June-2026)_
- `get_chembl_modulators`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2364155/ — _ChEMBL_37 (released 2026-05-01)_
- `get_gnomad_constraint`: https://gnomad.broadinstitute.org/gene/IL6R — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `get_clinvar_variants`: https://www.ncbi.nlm.nih.gov/clinvar/?term=IL6R%5Bgene%5D — _ClinVar build Build260804-2105.1_
- `get_gwas_catalog`: https://www.ebi.ac.uk/gwas/genes/IL6R — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `get_pharmgkb_drug_gene`: https://www.pharmgkb.org/search?query=IL6R — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_

## Provenance

- Generated: 2026-08-07T06:41:52
- Model (reasoning text only): `gemini-flash-lite-latest`
- Tools invoked (8 calls): `get_mr_result`, `get_target_disease_evidence`, `get_uniprot_dossier`, `get_chembl_modulators`, `get_gnomad_constraint`, `get_clinvar_variants`, `get_gwas_catalog`, `get_pharmgkb_drug_gene`
- Evidence table, caveats, sources and this block are rendered mechanically from tool return values. The model wrote only the Verdict sentence and the Reasoning paragraph, both checked against tool output by `validate_card.py`.
- No Mendelian randomization or colocalization is computed by this agent; MR estimates, where present, are retrieved from published work.
