# Target Evidence Card — SCN2A × epilepsy

**Verdict:** GO — SCN2A has exceptionally strong genetic, clinical, and literature support for epilepsy, backed by robust target-disease evidence.

## Evidence

| Evidence | Tool | Result |
|---|---|---|
| Causal effect (MR) — retrieved, not computed | `get_mr_result` | **not available** — no pQTL MR estimate for this protein in the resource (absence of an estimate is not evidence of no effect) |
| Target–disease association | `get_target_disease_evidence` | overall score=0.906 (genetic_literature=0.913, clinical=0.999, literature=0.714, genetic_association=0.975) |
| Protein context | `get_uniprot_dossier` | Q99250 — Sodium channel protein type 2 subunit alpha; location: Cell membrane |
| Known modulators / druggability | `get_chembl_modulators` | target CHEMBL4523672 — **0 known modulators in ChEMBL** |
| Clinical variants | `get_clinvar_variants` | 3108 ClinVar records; 11 pathogenic in a sample of 30 |
| Population constraint / LoF tolerance | `get_gnomad_constraint` | pLI=1, LOEUF=0.154 → LoF-INTOLERANT (handle with care) |
| Extra genetic evidence | `get_gwas_catalog` | 75 unique SNPs from 144/144 association rows |
| Pharmacogenomics | `get_pharmgkb_drug_gene` | 7 clinical annotations across 8 drugs (level 3: 6, level 4: 1) |

## Caveats declared by the tools

- **`get_target_disease_evidence`** — Free-text inputs were resolved to ontology terms: 'SCN2A' -> ENSG00000136531 (SCN2A); 'epilepsy' -> MONDO_0005027 (epilepsy). Scores below describe THAT term, not the free-text phrase.
- **`get_chembl_modulators`** — ChEMBL target matched by text search on 'SCN2A' and resolved to 'SCN2A/SCN1B' — confirm this is the intended target.
- **`get_mr_result`** — No pQTL-based MR estimate for SCN2A in the EpiGraphDB pQTL resource. This resource only covers proteins with usable plasma pQTL instruments. ABSENCE OF AN ESTIMATE IS NOT EVIDENCE OF NO EFFECT.
- **`get_clinvar_variants`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 3108 ClinVar records for this gene; it is a sample, not a rate.

## Reasoning

Open Targets demonstrates a high overall evidence score linking SCN2A to epilepsy, driven by strong genetic associations, clinical data, and animal model support. ClinVar records confirm numerous pathogenic and uncertain variants in SCN2A associated with epileptic disorders. Although gnomAD constraint metrics indicate the gene is loss-of-function intolerant, and no MR pQTL estimate was available, the overwhelming genetic and pharmacogenomic signals — including multiple PharmGKB annotations for antiepileptic drugs — strongly support SCN2A as a valid therapeutic and pharmacogenomic target for epilepsy.

## Sources

- `get_uniprot_dossier`: https://www.uniprot.org/uniprotkb/Q99250 — _UniProt release 2026_02 (10-June-2026)_
- `get_target_disease_evidence`: https://platform.opentargets.org/evidence/ENSG00000136531/MONDO_0005027 — _Open Targets data release 26.06_
- `get_chembl_modulators`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4523672/ — _ChEMBL_37 (released 2026-05-01)_
- `get_mr_result`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `get_clinvar_variants`: https://www.ncbi.nlm.nih.gov/clinvar/?term=SCN2A%5Bgene%5D — _ClinVar build Build260804-2105.1_
- `get_gnomad_constraint`: https://gnomad.broadinstitute.org/gene/SCN2A — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `get_gwas_catalog`: https://www.ebi.ac.uk/gwas/genes/SCN2A — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `get_pharmgkb_drug_gene`: https://www.pharmgkb.org/search?query=SCN2A — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_

## Provenance

- Generated: 2026-08-07T06:23:28
- Model (reasoning text only): `gemini-flash-lite-latest`
- Tools invoked (8 calls): `get_uniprot_dossier`, `get_target_disease_evidence`, `get_chembl_modulators`, `get_mr_result`, `get_clinvar_variants`, `get_gnomad_constraint`, `get_gwas_catalog`, `get_pharmgkb_drug_gene`
- Evidence table, caveats, sources and this block are rendered mechanically from tool return values. The model wrote only the Verdict sentence and the Reasoning paragraph, both checked against tool output by `validate_card.py`.
- No Mendelian randomization or colocalization is computed by this agent; MR estimates, where present, are retrieved from published work.
