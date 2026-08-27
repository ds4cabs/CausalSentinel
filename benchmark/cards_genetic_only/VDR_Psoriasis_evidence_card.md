# Target Evidence Card — VDR × Psoriasis

**Verdict:** GO — VDR demonstrates substantial genetic, clinical, and pharmacological support as a therapeutic target for psoriasis.

> **You asked about "Psoriasis". This card scored MONDO_0005083 — psoriasis.** If those are not the same thing, every number below answers a different question.
> **The druggability row is about ChEMBL target "Vitamin D3 receptor" (CHEMBL1977),** matched by text search. If that is not the molecular target you meant, that row is about something else.

## Evidence concordance — classified by rule, not written by the model

- Sources: EpiGraphDB — no pQTL instrument · Europe PMC — NOT checked in this run · Semantic Scholar — NOT checked in this run · MR-KG — NOT checked in this run

## Evidence

| Evidence | Tool | Result |
|---|---|---|
| Causal effect (MR) — retrieved, not computed | `get_mr_result` | **not available** — no pQTL MR estimate for this protein in the resource (absence of an estimate is not evidence of no effect) |
| Target–disease association | `get_target_disease_evidence` | overall score=0.637 (literature=0.869, animal_model=0.468, clinical=0.993) |
| Protein context | `get_uniprot_dossier` | P11473 — Vitamin D3 receptor; location: Nucleus, Cytoplasm |
| Known modulators / druggability | `get_chembl_modulators` | 18 known modulators (AGONIST) |
| Clinical variants | `get_clinvar_variants` | 583 ClinVar records; 4 pathogenic in a sample of 30 |
| Population constraint / LoF tolerance | `get_gnomad_constraint` | pLI=0.016, LOEUF=0.702 → LoF-tolerant |
| Extra genetic evidence | `get_gwas_catalog` | 132 unique SNPs from 285/285 association rows |
| Pharmacogenomics | `get_pharmgkb_drug_gene` | 18 clinical annotation(s) over 13 drug(s): alendronate, calcium, clodronate, conjugated estrogens +9 more — ClinPGx evidence level 3 (scale 1A strongest to 4 weakest) — e.g. rs1544410 (VDR); alendronate; Osteoporosis (level 3 Efficacy) |
| Clinical development record | `get_clinical_evidence` | _tool not called by the agent in this run_ |

## Caveats declared by the tools

- **`get_target_disease_evidence`** — Free-text inputs were resolved to ontology terms: 'VDR' -> ENSG00000111424 (VDR); 'Psoriasis' -> MONDO_0005083 (psoriasis). Scores below describe THAT term, not the free-text phrase.
- **`get_mr_result`** — No pQTL-based MR estimate for VDR in the EpiGraphDB pQTL resource. This resource only covers proteins with usable plasma pQTL instruments. ABSENCE OF AN ESTIMATE IS NOT EVIDENCE OF NO EFFECT.
- **`get_chembl_modulators`** — ChEMBL target matched by text search on 'VDR' and resolved to 'Vitamin D3 receptor' — confirm this is the intended target.
- **`get_clinvar_variants`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 583 ClinVar records for this gene; it is a sample, not a rate.
- **`classify_evidence_concordance`** — Nothing to compare: fewer than two matched estimates.

## Reasoning

The vitamin D receptor (VDR) is well-validated in clinical contexts for psoriasis, supported by a strong overall target-disease association score and numerous known receptor agonists in ChEMBL. Although no pQTL Mendelian randomization estimate is available in the EpiGraphDB resource, the locus is backed by extensive GWAS catalog associations and favorable gnomAD constraint metrics indicating tolerance to loss-of-function variation.

## Sources

- `get_uniprot_dossier`: https://www.uniprot.org/uniprotkb/P11473 — _UniProt release 2026_02 (10-June-2026)_
- `get_target_disease_evidence`: https://platform.opentargets.org/evidence/ENSG00000111424/MONDO_0005083 — _Open Targets data release 26.06_
- `get_mr_result`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `get_chembl_modulators`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL1977/ — _ChEMBL_37 (released 2026-05-01)_
- `get_clinvar_variants`: https://www.ncbi.nlm.nih.gov/clinvar/?term=VDR%5Bgene%5D — _ClinVar build Build260818-0035.1_
- `get_gnomad_constraint`: https://gnomad.broadinstitute.org/gene/VDR — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `get_gwas_catalog`: https://www.ebi.ac.uk/gwas/genes/VDR — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `get_pharmgkb_drug_gene`: https://www.pharmgkb.org/search?query=VDR — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_

## Provenance

- Generated: 2026-08-21T15:46:18
- Model (reasoning text only): `gemini-flash-lite-latest`
- Tools invoked (9 calls): `get_uniprot_dossier`, `get_target_disease_evidence`, `get_mr_result`, `get_chembl_modulators`, `get_clinvar_variants`, `get_gnomad_constraint`, `get_gwas_catalog`, `get_pharmgkb_drug_gene`, `classify_evidence_concordance`
- Evidence table, caveats, sources and this block are rendered mechanically from tool return values. The model wrote only the Verdict sentence and the Reasoning paragraph, both checked against tool output by `validate_card.py`.
- No Mendelian randomization or colocalization is computed by this agent; MR estimates, where present, are retrieved from published work.
