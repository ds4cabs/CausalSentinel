# Target Evidence Card — PNPLA3 × MASLD

**Verdict:** GO — Strong genetic and literature evidence supports PNPLA3 as a key target for metabolic dysfunction-associated steatotic liver disease (MASLD).

## Evidence

| Evidence | Tool | Result |
|---|---|---|
| Causal effect (MR) — retrieved, not computed | `get_mr_result` | **not available** — no pQTL MR estimate for this protein in the resource (absence of an estimate is not evidence of no effect) |
| Target–disease association | `get_target_disease_evidence` | overall score=0.714 (literature=0.988, animal_model=0.646, genetic_association=0.871, genetic_literature=0.608) |
| Protein context | `get_uniprot_dossier` | Q9NST1 — 1-acylglycerol-3-phosphate O-acyltransferase PNPLA3; location: Membrane, Lipid droplet |
| Known modulators / druggability | `get_chembl_modulators` | **not available** — No ChEMBL target for 'PNPLA3'. |
| Clinical variants | `get_clinvar_variants` | 216 ClinVar records; 0 pathogenic in a sample of 30 |
| Population constraint / LoF tolerance | `get_gnomad_constraint` | pLI=1.6e-14, LOEUF=1.26 → LoF-tolerant |
| Extra genetic evidence | `get_gwas_catalog` | 111 unique SNPs from 256/256 association rows |
| Pharmacogenomics | `get_pharmgkb_drug_gene` | 2 clinical annotations across 6 drugs (level 3: 2) |

## Caveats declared by the tools

- **`get_target_disease_evidence`** — Free-text inputs were resolved to ontology terms: 'PNPLA3' -> ENSG00000100344 (PNPLA3); 'MASLD' -> MONDO_0013209 (metabolic dysfunction-associated steatotic liver disease). Scores below describe THAT term, not the free-text phrase.
- **`get_chembl_modulators`** — No ChEMBL target for 'PNPLA3'.
- **`get_mr_result`** — No pQTL-based MR estimate for PNPLA3 in the EpiGraphDB pQTL resource. This resource only covers proteins with usable plasma pQTL instruments. ABSENCE OF AN ESTIMATE IS NOT EVIDENCE OF NO EFFECT.
- **`get_clinvar_variants`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 216 ClinVar records for this gene; it is a sample, not a rate.

## Reasoning

Open Targets shows a high overall association score between PNPLA3 and metabolic dysfunction-associated steatotic liver disease, backed by strong genetic association and literature evidence. Numerous GWAS associations map to the locus, and UniProt notes the protein's localization to lipid droplets and its role in lipid metabolism linked to non-alcoholic fatty liver disease. Constraint metrics indicate that PNPLA3 is tolerant to loss-of-function variation. Although ChEMBL currently lists no modulators for this target, the robust genetic validation makes it a compelling candidate for therapeutic intervention.

## Sources

- `get_uniprot_dossier`: https://www.uniprot.org/uniprotkb/Q9NST1 — _UniProt release 2026_02 (10-June-2026)_
- `get_target_disease_evidence`: https://platform.opentargets.org/evidence/ENSG00000100344/MONDO_0013209 — _Open Targets data release 26.06_
- `get_mr_result`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `get_clinvar_variants`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PNPLA3%5Bgene%5D — _ClinVar build Build260804-2105.1_
- `get_gnomad_constraint`: https://gnomad.broadinstitute.org/gene/PNPLA3 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `get_gwas_catalog`: https://www.ebi.ac.uk/gwas/genes/PNPLA3 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `get_pharmgkb_drug_gene`: https://www.pharmgkb.org/search?query=PNPLA3 — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_

## Provenance

- Generated: 2026-08-07T06:22:50
- Model (reasoning text only): `gemini-flash-lite-latest`
- Tools invoked (8 calls): `get_uniprot_dossier`, `get_target_disease_evidence`, `get_chembl_modulators`, `get_mr_result`, `get_clinvar_variants`, `get_gnomad_constraint`, `get_gwas_catalog`, `get_pharmgkb_drug_gene`
- Evidence table, caveats, sources and this block are rendered mechanically from tool return values. The model wrote only the Verdict sentence and the Reasoning paragraph, both checked against tool output by `validate_card.py`.
- No Mendelian randomization or colocalization is computed by this agent; MR estimates, where present, are retrieved from published work.
