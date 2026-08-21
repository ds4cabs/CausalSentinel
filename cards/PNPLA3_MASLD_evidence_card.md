# Target Evidence Card — PNPLA3 × MASLD

**Verdict:** GO — PNPLA3 is robustly associated with metabolic dysfunction-associated steatotic liver disease via genetic evidence, acting on lipid droplets in the liver, though no causal Mendelian randomization estimate or clinical drug trials are currently recorded in the retrieved sources.

> **You asked about "MASLD". This card scored MONDO_0013209 — metabolic dysfunction-associated steatotic liver disease.** If those are not the same thing, every number below answers a different question.

## Evidence concordance — classified by rule, not written by the model

- Sources: EpiGraphDB — no pQTL instrument · Europe PMC — NOT checked in this run · Semantic Scholar — NOT checked in this run · MR-KG — NOT checked in this run

## Evidence

| Evidence | Tool | Result |
|---|---|---|
| Causal effect (MR) — retrieved, not computed | `get_mr_result` | **not available** — no pQTL MR estimate for this protein in the resource (absence of an estimate is not evidence of no effect) |
| Target–disease association | `get_target_disease_evidence` | overall score=0.714 (literature=0.988, animal_model=0.646, genetic_association=0.871, genetic_literature=0.608) |
| Protein context | `get_uniprot_dossier` | Q9NST1 — 1-acylglycerol-3-phosphate O-acyltransferase PNPLA3; location: Membrane, Lipid droplet |
| Known modulators / druggability | `get_chembl_modulators` | **not available** — No ChEMBL target for 'PNPLA3'. |
| Clinical variants | `get_clinvar_variants` | 216 ClinVar records; 0 pathogenic in a sample of 30 |
| Population constraint / LoF tolerance | `get_gnomad_constraint` | pLI=1.6e-14, LOEUF=1.26 → LoF-tolerant |
| Extra genetic evidence | `get_gwas_catalog` | 107 unique SNPs from 256/256 association rows |
| Pharmacogenomics | `get_pharmgkb_drug_gene` | 2 clinical annotation(s) over 6 drug(s): asparaginase, cyclophosphamide, daunorubicin, ethanol +2 more — ClinPGx evidence level 3 (scale 1A strongest to 4 weakest) — e.g. rs738409 (PNPLA3); ethanol; Alcoholism (level 3 Toxicity) |
| Clinical development record | `get_clinical_evidence` | **not available** — No drug or clinical candidate against PNPLA3 in Open Targets. An empty clinical record means the clinic has not filed results against this target — NOT that the target is bad, and not that nothing was ever tried outside registries. |

## Caveats declared by the tools

- **`get_target_disease_evidence`** — Free-text inputs were resolved to ontology terms: 'PNPLA3' -> ENSG00000100344 (PNPLA3); 'MASLD' -> MONDO_0013209 (metabolic dysfunction-associated steatotic liver disease). Scores below describe THAT term, not the free-text phrase.
- **`get_chembl_modulators`** — No ChEMBL target for 'PNPLA3'.
- **`get_clinvar_variants`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 216 ClinVar records for this gene; it is a sample, not a rate.
- **`get_clinical_evidence`** — No drug or clinical candidate against PNPLA3 in Open Targets. An empty clinical record means the clinic has not filed results against this target — NOT that the target is bad, and not that nothing was ever tried outside registries.
- **`get_mr_result`** — No pQTL-based MR estimate for PNPLA3 in the EpiGraphDB pQTL resource. This resource only covers proteins with usable plasma pQTL instruments. ABSENCE OF AN ESTIMATE IS NOT EVIDENCE OF NO EFFECT.
- **`classify_evidence_concordance`** — Nothing to compare: fewer than two matched estimates.

## Reasoning

Open Targets reports a strong overall disease association score for PNPLA3 with metabolic dysfunction-associated steatotic liver disease, supported by extensive GWAS catalog associations (including 107 unique SNPs). UniProt confirms the protein localizes to lipid droplets and functions in lipid metabolism. Furthermore, gnomAD constraint metrics indicate the gene is tolerant to loss of function, and PharmGKB documents pharmacogenomic annotations involving ethanol and other drugs. Although no Mendelian randomization estimates or clinical trial records were retrieved, the powerful genetic association and biological rationale support pursuing PNPLA3 as a target.

## Sources

- `get_target_disease_evidence`: https://platform.opentargets.org/evidence/ENSG00000100344/MONDO_0013209 — _Open Targets data release 26.06_
- `get_uniprot_dossier`: https://www.uniprot.org/uniprotkb/Q9NST1 — _UniProt release 2026_02 (10-June-2026)_
- `get_gnomad_constraint`: https://gnomad.broadinstitute.org/gene/PNPLA3 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `get_clinvar_variants`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PNPLA3%5Bgene%5D — _ClinVar build Build260818-0035.1_
- `get_gwas_catalog`: https://www.ebi.ac.uk/gwas/genes/PNPLA3 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `get_pharmgkb_drug_gene`: https://www.pharmgkb.org/search?query=PNPLA3 — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `get_clinical_evidence`: https://platform.opentargets.org/target/ENSG00000100344 — _Open Targets data release 26.06_
- `get_mr_result`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_

## Provenance

- Generated: 2026-08-21T15:32:54
- Model (reasoning text only): `gemini-flash-lite-latest`
- Tools invoked (10 calls): `get_target_disease_evidence`, `get_uniprot_dossier`, `get_gnomad_constraint`, `get_chembl_modulators`, `get_clinvar_variants`, `get_gwas_catalog`, `get_pharmgkb_drug_gene`, `get_clinical_evidence`, `get_mr_result`, `classify_evidence_concordance`
- Evidence table, caveats, sources and this block are rendered mechanically from tool return values. The model wrote only the Verdict sentence and the Reasoning paragraph, both checked against tool output by `validate_card.py`.
- No Mendelian randomization or colocalization is computed by this agent; MR estimates, where present, are retrieved from published work.
