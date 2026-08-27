# Target Evidence Card — PDGFRB × Retinal Detachment

**Verdict:** INSUFFICIENT EVIDENCE — there is no available causal estimate or direct genetic association linking PDGFRB to retinal detachment.

> **You asked about "Retinal Detachment". This card scored MONDO_0008375 — retinal detachment.** If those are not the same thing, every number below answers a different question.
> **The druggability row is about ChEMBL target "Platelet-derived growth factor receptor beta" (CHEMBL1913),** matched by text search. If that is not the molecular target you meant, that row is about something else.

## Evidence concordance — classified by rule, not written by the model

- Sources: EpiGraphDB — no pQTL instrument · Europe PMC — NOT checked in this run · Semantic Scholar — NOT checked in this run · MR-KG — NOT checked in this run

## Evidence

| Evidence | Tool | Result |
|---|---|---|
| Causal effect (MR) — retrieved, not computed | `get_mr_result` | **not available** — no pQTL MR estimate for this protein in the resource (absence of an estimate is not evidence of no effect) |
| Target–disease association | `get_target_disease_evidence` | **not available** — PDGFRB is not among the top 500 associated targets for MONDO_0008375 (retinal detachment). This is a TRUNCATED LOOKUP, not proof of no association. Free-text inputs were resolved to ontology terms: 'PDGFRB' -> ENSG00000113721 (PDGFRB); 'Retinal Detachment' -> MONDO_0008375 (retinal detachment). Scores below describe THAT term, not the free-text phrase. |
| Protein context | `get_uniprot_dossier` | P09619 — Platelet-derived growth factor receptor beta; location: Cell membrane, Cytoplasmic vesicle, Lysosome lumen |
| Known modulators / druggability | `get_chembl_modulators` | 17 known modulators (INHIBITOR) |
| Clinical variants | `get_clinvar_variants` | 870 ClinVar records; 1 pathogenic in a sample of 30 |
| Population constraint / LoF tolerance | `get_gnomad_constraint` | pLI=1, LOEUF=0.452 → LoF-INTOLERANT (handle with care) |
| Extra genetic evidence | `get_gwas_catalog` | 114 unique SNPs from 287/287 association rows |
| Pharmacogenomics | `get_pharmgkb_drug_gene` | **not available** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene). |
| Clinical development record | `get_clinical_evidence` | _tool not called by the agent in this run_ |

## Caveats declared by the tools

- **`get_target_disease_evidence`** — PDGFRB is not among the top 500 associated targets for MONDO_0008375 (retinal detachment). This is a TRUNCATED LOOKUP, not proof of no association. Free-text inputs were resolved to ontology terms: 'PDGFRB' -> ENSG00000113721 (PDGFRB); 'Retinal Detachment' -> MONDO_0008375 (retinal detachment). Scores below describe THAT term, not the free-text phrase.
- **`get_chembl_modulators`** — ChEMBL target matched by text search on 'PDGFRB' and resolved to 'Platelet-derived growth factor receptor beta' — confirm this is the intended target.
- **`get_mr_result`** — No pQTL-based MR estimate for PDGFRB in the EpiGraphDB pQTL resource. This resource only covers proteins with usable plasma pQTL instruments. ABSENCE OF AN ESTIMATE IS NOT EVIDENCE OF NO EFFECT.
- **`get_clinvar_variants`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 870 ClinVar records for this gene; it is a sample, not a rate.
- **`get_pharmgkb_drug_gene`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`classify_evidence_concordance`** — Nothing to compare: fewer than two matched estimates.

## Reasoning

Open Targets did not retrieve an association between PDGFRB and retinal detachment, and no Mendelian randomization estimate was available to establish a causal link. Although ChEMBL confirms the target is druggable with known modulators and gnomAD indicates constraint, the lack of disease-specific genetic support leaves insufficient evidence to prioritize this target for retinal detachment.

## Sources

- `get_uniprot_dossier`: https://www.uniprot.org/uniprotkb/P09619 — _UniProt release 2026_02 (10-June-2026)_
- `get_chembl_modulators`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL1913/ — _ChEMBL_37 (released 2026-05-01)_
- `get_mr_result`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `get_clinvar_variants`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PDGFRB%5Bgene%5D — _ClinVar build Build260818-0035.1_
- `get_gnomad_constraint`: https://gnomad.broadinstitute.org/gene/PDGFRB — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `get_gwas_catalog`: https://www.ebi.ac.uk/gwas/genes/PDGFRB — _GWAS Catalog REST (live; release not exposed by this endpoint)_

## Provenance

- Generated: 2026-08-21T15:53:07
- Model (reasoning text only): `gemini-flash-lite-latest`
- Tools invoked (9 calls): `get_uniprot_dossier`, `get_target_disease_evidence`, `get_chembl_modulators`, `get_mr_result`, `get_clinvar_variants`, `get_gnomad_constraint`, `get_gwas_catalog`, `get_pharmgkb_drug_gene`, `classify_evidence_concordance`
- Evidence table, caveats, sources and this block are rendered mechanically from tool return values. The model wrote only the Verdict sentence and the Reasoning paragraph, both checked against tool output by `validate_card.py`.
- No Mendelian randomization or colocalization is computed by this agent; MR estimates, where present, are retrieved from published work.
