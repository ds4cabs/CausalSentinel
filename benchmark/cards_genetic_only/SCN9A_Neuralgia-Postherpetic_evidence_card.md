# Target Evidence Card — SCN9A × Neuralgia, Postherpetic

**Verdict:** INSUFFICIENT EVIDENCE — there is no direct genetic or causal estimate available linking SCN9A to postherpetic neuralgia, despite its known role in pain sensory perception and channelopathy variants.

> **The druggability row is about ChEMBL target "SCN9A/SCN1B" (CHEMBL4523670),** matched by text search. If that is not the molecular target you meant, that row is about something else.

## Evidence concordance — classified by rule, not written by the model

- Sources: EpiGraphDB — no pQTL instrument · Europe PMC — NOT checked in this run · Semantic Scholar — NOT checked in this run · MR-KG — NOT checked in this run

## Evidence

| Evidence | Tool | Result |
|---|---|---|
| Causal effect (MR) — retrieved, not computed | `get_mr_result` | **not available** — no pQTL MR estimate for this protein in the resource (absence of an estimate is not evidence of no effect) |
| Target–disease association | `get_target_disease_evidence` | **not available** — Could not resolve target 'SCN9A' or disease 'Neuralgia, Postherpetic'. |
| Protein context | `get_uniprot_dossier` | Q15858 — Sodium channel protein type 9 subunit alpha; location: Cell membrane, Cell projection, neuron projection, Cell proj |
| Known modulators / druggability | `get_chembl_modulators` | target CHEMBL4523670 — **0 known modulators in ChEMBL** |
| Clinical variants | `get_clinvar_variants` | 3117 ClinVar records; 5 pathogenic in a sample of 30 |
| Population constraint / LoF tolerance | `get_gnomad_constraint` | pLI=2.8e-30, LOEUF=0.81 → LoF-tolerant |
| Extra genetic evidence | `get_gwas_catalog` | 43 unique SNPs from 86/86 association rows |
| Pharmacogenomics | `get_pharmgkb_drug_gene` | **not available** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene). |
| Clinical development record | `get_clinical_evidence` | _tool not called by the agent in this run_ |

## Caveats declared by the tools

- **`get_target_disease_evidence`** — Could not resolve target 'SCN9A' or disease 'Neuralgia, Postherpetic'.
- **`get_mr_result`** — No pQTL-based MR estimate for SCN9A in the EpiGraphDB pQTL resource. This resource only covers proteins with usable plasma pQTL instruments. ABSENCE OF AN ESTIMATE IS NOT EVIDENCE OF NO EFFECT.
- **`get_chembl_modulators`** — ChEMBL target matched by text search on 'SCN9A' and resolved to 'SCN9A/SCN1B' — confirm this is the intended target.
- **`get_clinvar_variants`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 3117 ClinVar records for this gene; it is a sample, not a rate.
- **`get_pharmgkb_drug_gene`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`classify_evidence_concordance`** — Nothing to compare: fewer than two matched estimates.

## Reasoning

SCN9A encodes the voltage-gated sodium channel Nav1.7, which is a major contributor to the sensory perception of pain in nociceptor neurons, with multiple pathogenic variants recorded in ClinVar. However, query matching in Open Targets failed to link SCN9A directly to postherpetic neuralgia, and no Mendelian randomization estimates were available in EpiGraphDB to support a causal effect. Although the GWAS Catalog maps multiple trait-associated SNPs to the gene, and gnomAD indicates tolerance to loss-of-function variation, ChEMBL reports no modulators and PharmGKB lists no clinical annotations for this target. Therefore, current data are insufficient to establish SCN9A as a validated target for this specific neuralgia indication.

## Sources

- `get_uniprot_dossier`: https://www.uniprot.org/uniprotkb/Q15858 — _UniProt release 2026_02 (10-June-2026)_
- `get_mr_result`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `get_chembl_modulators`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4523670/ — _ChEMBL_37 (released 2026-05-01)_
- `get_clinvar_variants`: https://www.ncbi.nlm.nih.gov/clinvar/?term=SCN9A%5Bgene%5D — _ClinVar build Build260818-0035.1_
- `get_gnomad_constraint`: https://gnomad.broadinstitute.org/gene/SCN9A — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `get_gwas_catalog`: https://www.ebi.ac.uk/gwas/genes/SCN9A — _GWAS Catalog REST (live; release not exposed by this endpoint)_

## Provenance

- Generated: 2026-08-21T15:47:19
- Model (reasoning text only): `gemini-flash-lite-latest`
- Tools invoked (9 calls): `get_uniprot_dossier`, `get_target_disease_evidence`, `get_mr_result`, `get_chembl_modulators`, `get_clinvar_variants`, `get_gnomad_constraint`, `get_gwas_catalog`, `get_pharmgkb_drug_gene`, `classify_evidence_concordance`
- Evidence table, caveats, sources and this block are rendered mechanically from tool return values. The model wrote only the Verdict sentence and the Reasoning paragraph, both checked against tool output by `validate_card.py`.
- No Mendelian randomization or colocalization is computed by this agent; MR estimates, where present, are retrieved from published work.
