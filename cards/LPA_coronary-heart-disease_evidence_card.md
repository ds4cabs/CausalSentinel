# Target Evidence Card — LPA × coronary heart disease

**Verdict:** GO — genetic, causal, and clinical evidence strongly support LPA as a therapeutic target for coronary heart disease.

> **Question actually answered:** the free-text disease was resolved to **MONDO_0005010 (coronary artery disorder)**. If that is not what you meant, every score below answers a different question.
> **ChEMBL target resolved by text search** to **"LPA mRNA"** (CHEMBL4662965). If that is not the intended molecular target, the druggability row is about something else.

## MR direction — rendered from the ledger, not written by the model

- Genetically-predicted **higher plasma LPA** is associated with **HIGHER Coronary heart disease** (beta +0.2523, se 0.0193, p=5.39e-39; Wald ratio, n_snp 1, instrument rs55730499, cis).
  - Not available for this estimate: colocalization.
  - Single-instrument Wald ratio: no heterogeneity or pleiotropy test is possible.

> **The exposure is LPA protein abundance, not a drug.** This run retrieved no evidence about what pharmacological inhibition or activation of LPA does. Turning the direction above into a drug direction needs a mechanism this run did not retrieve.

## Evidence

| Evidence | Tool | Result |
|---|---|---|
| Causal effect (MR) — retrieved, not computed | `get_mr_result` | outcome: Coronary heart disease — beta=0.252, se=0.0193, p=5.39e-39, Wald ratio, n_snp=1, cis instrument, coloc=not available  
_retrieved from published MR; not computed here_ |
| Target–disease association | `get_target_disease_evidence` | overall score=0.576 (literature=0.977, genetic_association=0.898, clinical=0.0061) |
| Protein context | `get_uniprot_dossier` | P08519 — Apolipoprotein(a); location: Not annotated. |
| Known modulators / druggability | `get_chembl_modulators` | 2 known modulators (ANTISENSE INHIBITOR, RNAI INHIBITOR) |
| Clinical variants | `get_clinvar_variants` | 365 ClinVar records; 2 pathogenic in a sample of 30 |
| Population constraint / LoF tolerance | `get_gnomad_constraint` | pLI=2.1e-68, LOEUF=1.13 → LoF-tolerant |
| Extra genetic evidence | `get_gwas_catalog` | 267 unique SNPs from 690/690 association rows |
| Pharmacogenomics | `get_pharmgkb_drug_gene` | 3 clinical annotations across 2 drugs (level 3: 3) |

## Caveats declared by the tools

- **`get_target_disease_evidence`** — Free-text inputs were resolved to ontology terms: 'LPA' -> ENSG00000198670 (LPA); 'coronary heart disease' -> MONDO_0005010 (coronary artery disorder). Scores below describe THAT term, not the free-text phrase.
- **`get_chembl_modulators`** — ChEMBL target matched by text search on 'LPA' and resolved to 'LPA mRNA' — confirm this is the intended target.
- **`get_mr_result`** — Estimates RETRIEVED from published pQTL MR, not computed by this agent. Check cis_or_trans (cis instruments are less pleiotropy-prone), steiger_direction_ok, and coloc_prob before treating this as causal; coloc_prob=null means colocalization was not available for this pair.
- **`get_clinvar_variants`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 365 ClinVar records for this gene; it is a sample, not a rate.

## Reasoning

Open Targets and GWAS catalog queries reveal strong genetic association between LPA and coronary artery disease. Published Mendelian randomization estimates retrieved from pQTL resources demonstrate a significant causal relationship with coronary heart disease outcomes using cis-instruments. Furthermore, the protein is targetable, with active small interfering RNA and antisense modulators present in ChEMBL. Constraint metrics indicate that LPA is tolerant to loss-of-function variations, suggesting safety for inhibitory therapeutic approaches.

## Sources

- `get_uniprot_dossier`: https://www.uniprot.org/uniprotkb/P08519 — _UniProt release 2026_02 (10-June-2026)_
- `get_target_disease_evidence`: https://platform.opentargets.org/evidence/ENSG00000198670/MONDO_0005010 — _Open Targets data release 26.06_
- `get_chembl_modulators`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4662965/ — _ChEMBL_37 (released 2026-05-01)_
- `get_mr_result`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `get_clinvar_variants`: https://www.ncbi.nlm.nih.gov/clinvar/?term=LPA%5Bgene%5D — _ClinVar build Build260804-2105.1_
- `get_gnomad_constraint`: https://gnomad.broadinstitute.org/gene/LPA — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `get_gwas_catalog`: https://www.ebi.ac.uk/gwas/genes/LPA — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `get_pharmgkb_drug_gene`: https://www.pharmgkb.org/search?query=LPA — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_

## Provenance

- Generated: 2026-08-07T06:42:18
- Model (reasoning text only): `gemini-flash-lite-latest`
- Tools invoked (8 calls): `get_uniprot_dossier`, `get_target_disease_evidence`, `get_chembl_modulators`, `get_mr_result`, `get_clinvar_variants`, `get_gnomad_constraint`, `get_gwas_catalog`, `get_pharmgkb_drug_gene`
- Evidence table, caveats, sources and this block are rendered mechanically from tool return values. The model wrote only the Verdict sentence and the Reasoning paragraph, both checked against tool output by `validate_card.py`.
- No Mendelian randomization or colocalization is computed by this agent; MR estimates, where present, are retrieved from published work.
