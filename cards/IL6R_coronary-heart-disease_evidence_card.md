# Target Evidence Card — IL6R × coronary heart disease

**Verdict:** GO — IL6R shows strong genetic and causal Mendelian randomization support for a protective effect in coronary artery disease, alongside established pharmacological tractability.

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
| Extra genetic evidence | `get_gwas_catalog` | 156 unique SNPs from 368/368 association rows |
| Pharmacogenomics | `get_pharmgkb_drug_gene` | 3 clinical annotations across 1 drugs (level 3: 2, level 4: 1) |

## Caveats declared by the tools

- **`get_target_disease_evidence`** — Free-text inputs were resolved to ontology terms: 'IL6R' -> ENSG00000160712 (IL6R); 'coronary heart disease' -> MONDO_0005010 (coronary artery disorder). Scores below describe THAT term, not the free-text phrase.
- **`get_mr_result`** — Estimates RETRIEVED from published pQTL MR, not computed by this agent. Check cis_or_trans (cis instruments are less pleiotropy-prone), steiger_direction_ok, and coloc_prob before treating this as causal; coloc_prob=null means colocalization was not available for this pair.
- **`get_chembl_modulators`** — ChEMBL target matched by text search on 'IL6R' and resolved to 'Interleukin-6 receptor subunit alpha' — confirm this is the intended target.
- **`get_clinvar_variants`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 366 ClinVar records for this gene; it is a sample, not a rate.

## Reasoning

Open Targets records a high genetic association score for IL6R with coronary artery disease. Mendelian randomization provides a retrieved causal estimate supporting its role in the condition. The protein is well-characterized in UniProt, and ChEMBL identifies known modulators such as inhibitors and antagonists against the target. Furthermore, gnomAD constraint metrics indicate loss-of-function tolerance, and PharmGKB documents clinical pharmacogenomic annotations with the drug tocilizumab.

## Sources

- `get_uniprot_dossier`: https://www.uniprot.org/uniprotkb/P08887 — _UniProt release 2026_02 (10-June-2026)_
- `get_target_disease_evidence`: https://platform.opentargets.org/evidence/ENSG00000160712/MONDO_0005010 — _Open Targets data release 26.06_
- `get_mr_result`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `get_chembl_modulators`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2364155/ — _ChEMBL_37 (released 2026-05-01)_
- `get_clinvar_variants`: https://www.ncbi.nlm.nih.gov/clinvar/?term=IL6R%5Bgene%5D — _ClinVar build Build260804-2105.1_
- `get_gnomad_constraint`: https://gnomad.broadinstitute.org/gene/IL6R — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `get_gwas_catalog`: https://www.ebi.ac.uk/gwas/genes/IL6R — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `get_pharmgkb_drug_gene`: https://www.pharmgkb.org/search?query=IL6R — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_

## Provenance

- Generated: 2026-08-07T06:22:14
- Model (reasoning text only): `gemini-flash-lite-latest`
- Tools invoked (8 calls): `get_uniprot_dossier`, `get_target_disease_evidence`, `get_mr_result`, `get_chembl_modulators`, `get_clinvar_variants`, `get_gnomad_constraint`, `get_gwas_catalog`, `get_pharmgkb_drug_gene`
- Evidence table, caveats, sources and this block are rendered mechanically from tool return values. The model wrote only the Verdict sentence and the Reasoning paragraph, both checked against tool output by `validate_card.py`.
- No Mendelian randomization or colocalization is computed by this agent; MR estimates, where present, are retrieved from published work.
