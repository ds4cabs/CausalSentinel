# Target Evidence Card — HMGCR × high cholesterol

**Verdict:** GO — HMGCR is robustly linked genetically and clinically to hypercholesterolemia, with extensive validation as the established therapeutic target of statins.

## Evidence

| Evidence | Tool | Result |
|---|---|---|
| Causal effect (MR) — retrieved, not computed | `get_mr_result` | **not available** — no pQTL MR estimate for this protein in the resource (absence of an estimate is not evidence of no effect) |
| Target–disease association | `get_target_disease_evidence` | overall score=0.74 (literature=0.206, genetic_association=0.857, clinical=0.998) |
| Protein context | `get_uniprot_dossier` | P04035 — 3-hydroxy-3-methylglutaryl-coenzyme A reductase; location: Endoplasmic reticulum membrane, Peroxisome membrane |
| Known modulators / druggability | `get_chembl_modulators` | 10 known modulators (INHIBITOR) |
| Clinical variants | `get_clinvar_variants` | 112 ClinVar records; 1 pathogenic in a sample of 30 |
| Population constraint / LoF tolerance | `get_gnomad_constraint` | pLI=1, LOEUF=0.433 → LoF-INTOLERANT (handle with care) |
| Extra genetic evidence | `get_gwas_catalog` | 92 unique SNPs from 177/177 association rows |
| Pharmacogenomics | `get_pharmgkb_drug_gene` | 10 clinical annotations across 6 drugs (level 3: 10) |

## Caveats declared by the tools

- **`get_target_disease_evidence`** — Free-text inputs were resolved to ontology terms: 'HMGCR' -> ENSG00000113161 (HMGCR); 'high cholesterol' -> HP_0003124 (Hypercholesterolemia). Scores below describe THAT term, not the free-text phrase.
- **`get_mr_result`** — No pQTL-based MR estimate for HMGCR in the EpiGraphDB pQTL resource. This resource only covers proteins with usable plasma pQTL instruments. ABSENCE OF AN ESTIMATE IS NOT EVIDENCE OF NO EFFECT.
- **`get_chembl_modulators`** — ChEMBL target matched by text search on 'HMGCR' and resolved to '3-hydroxy-3-methylglutaryl-coenzyme A reductase' — confirm this is the intended target.
- **`get_clinvar_variants`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 112 ClinVar records for this gene; it is a sample, not a rate.

## Reasoning

Open Targets shows strong overall evidence linking HMGCR to hypercholesterolemia. ChEMBL lists multiple small-molecule inhibitors targeting HMGCR, matching its well-documented role as the primary target for cholesterol-lowering statin therapy. The GWAS catalog maps 92 unique SNPs to the gene, reflecting robust genetic association. Although gnomAD constraint metrics indicate the gene is loss-of-function intolerant, this aligns with its essential housekeeping role and therapeutic inhibition is clinically proven safe and effective.
```

## Sources

- `get_uniprot_dossier`: https://www.uniprot.org/uniprotkb/P04035 — _UniProt release 2026_02 (10-June-2026)_
- `get_target_disease_evidence`: https://platform.opentargets.org/evidence/ENSG00000113161/HP_0003124 — _Open Targets data release 26.06_
- `get_mr_result`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `get_chembl_modulators`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL402/ — _ChEMBL_37 (released 2026-05-01)_
- `get_clinvar_variants`: https://www.ncbi.nlm.nih.gov/clinvar/?term=HMGCR%5Bgene%5D — _ClinVar build Build260804-2105.1_
- `get_gnomad_constraint`: https://gnomad.broadinstitute.org/gene/HMGCR — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `get_gwas_catalog`: https://www.ebi.ac.uk/gwas/genes/HMGCR — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `get_pharmgkb_drug_gene`: https://www.pharmgkb.org/search?query=HMGCR — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_

## Provenance

- Generated: 2026-08-07T06:23:07
- Model (reasoning text only): `gemini-flash-lite-latest`
- Tools invoked (8 calls): `get_uniprot_dossier`, `get_target_disease_evidence`, `get_mr_result`, `get_chembl_modulators`, `get_clinvar_variants`, `get_gnomad_constraint`, `get_gwas_catalog`, `get_pharmgkb_drug_gene`
- Evidence table, caveats, sources and this block are rendered mechanically from tool return values. The model wrote only the Verdict sentence and the Reasoning paragraph, both checked against tool output by `validate_card.py`.
- No Mendelian randomization or colocalization is computed by this agent; MR estimates, where present, are retrieved from published work.
