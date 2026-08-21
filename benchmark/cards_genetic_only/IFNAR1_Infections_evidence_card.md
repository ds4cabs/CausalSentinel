# Target Evidence Card — IFNAR1 × Infections

**Verdict:** INSUFFICIENT EVIDENCE — while IFNAR1 has known roles in viral susceptibility and a ChEMBL modulator, there are no matching MR causal estimates or direct Open Targets genetic associations for infections.

> **You asked about "Infections". This card scored MONDO_0021679 — gram-positive bacterial infections.** If those are not the same thing, every number below answers a different question.
> **The druggability row is about ChEMBL target "Interferon alpha/beta receptor 1" (CHEMBL1887),** matched by text search. If that is not the molecular target you meant, that row is about something else.

## Evidence concordance — classified by rule, not written by the model

- Sources: EpiGraphDB — protein present, no estimate for THIS disease · Europe PMC — NOT checked in this run · Semantic Scholar — NOT checked in this run · MR-KG — NOT checked in this run

## Evidence

| Evidence | Tool | Result |
|---|---|---|
| Causal effect (MR) — retrieved, not computed | `get_mr_result` | **not available** — no pQTL MR estimate for this protein in the resource (absence of an estimate is not evidence of no effect) |
| Target–disease association | `get_target_disease_evidence` | **not available** — IFNAR1 is not among the top 500 associated targets for MONDO_0021679 (gram-positive bacterial infections). This is a TRUNCATED LOOKUP, not proof of no association. Free-text inputs were resolved to ontology terms: 'IFNAR1' -> ENSG00000142166 (IFNAR1); 'Infections' -> MONDO_0021679 (gram-positive bacterial infections). Scores below describe THAT term, not the free-text phrase. |
| Protein context | `get_uniprot_dossier` | P17181 — Interferon alpha/beta receptor 1; location: Cell membrane, Late endosome, Lysosome |
| Known modulators / druggability | `get_chembl_modulators` | 1 known modulators (ANTAGONIST) |
| Clinical variants | `get_clinvar_variants` | 439 ClinVar records; 4 pathogenic in a sample of 30 |
| Population constraint / LoF tolerance | `get_gnomad_constraint` | pLI=1.3e-12, LOEUF=0.966 → LoF-tolerant |
| Extra genetic evidence | `get_gwas_catalog` | 107 unique SNPs from 219/219 association rows |
| Pharmacogenomics | `get_pharmgkb_drug_gene` | **not available** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene). |
| Clinical development record | `get_clinical_evidence` | _tool not called by the agent in this run_ |

## Caveats declared by the tools

- **`get_target_disease_evidence`** — IFNAR1 is not among the top 500 associated targets for MONDO_0021679 (gram-positive bacterial infections). This is a TRUNCATED LOOKUP, not proof of no association. Free-text inputs were resolved to ontology terms: 'IFNAR1' -> ENSG00000142166 (IFNAR1); 'Infections' -> MONDO_0021679 (gram-positive bacterial infections). Scores below describe THAT term, not the free-text phrase.
- **`get_mr_result`** — IFNAR1 HAS pQTL MR estimates in this resource, but NONE matched the requested disease 'Infections'. The other outcomes are listed for context only — do not present them as evidence about 'Infections'.
- **`get_chembl_modulators`** — ChEMBL target matched by text search on 'IFNAR1' and resolved to 'Interferon alpha/beta receptor 1' — confirm this is the intended target.
- **`get_clinvar_variants`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 439 ClinVar records for this gene; it is a sample, not a rate.
- **`get_pharmgkb_drug_gene`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`classify_evidence_concordance`** — Nothing to compare: fewer than two matched estimates.

## Reasoning

The protein IFNAR1 functions as a receptor subunit for type I interferons, with UniProt documenting its role in immunodeficiency and viral infection susceptibility. However, no Mendelian randomization estimates were available for infections, and Open Targets disease evidence for the nearest mapped term did not highlight an association. The gene is loss-of-function tolerant according to gnomAD, and GWAS catalog queries returned 107 unique SNPs. One modulator was identified in ChEMBL, but clinical-stage or pharmacogenomic evidence was lacking.

## Sources

- `get_uniprot_dossier`: https://www.uniprot.org/uniprotkb/P17181 — _UniProt release 2026_02 (10-June-2026)_
- `get_mr_result`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `get_chembl_modulators`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL1887/ — _ChEMBL_37 (released 2026-05-01)_
- `get_clinvar_variants`: https://www.ncbi.nlm.nih.gov/clinvar/?term=IFNAR1%5Bgene%5D — _ClinVar build Build260818-0035.1_
- `get_gnomad_constraint`: https://gnomad.broadinstitute.org/gene/IFNAR1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `get_gwas_catalog`: https://www.ebi.ac.uk/gwas/genes/IFNAR1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_

## Provenance

- Generated: 2026-08-21T15:46:56
- Model (reasoning text only): `gemini-flash-lite-latest`
- Tools invoked (9 calls): `get_uniprot_dossier`, `get_target_disease_evidence`, `get_mr_result`, `get_chembl_modulators`, `get_clinvar_variants`, `get_gnomad_constraint`, `get_gwas_catalog`, `get_pharmgkb_drug_gene`, `classify_evidence_concordance`
- Evidence table, caveats, sources and this block are rendered mechanically from tool return values. The model wrote only the Verdict sentence and the Reasoning paragraph, both checked against tool output by `validate_card.py`.
- No Mendelian randomization or colocalization is computed by this agent; MR estimates, where present, are retrieved from published work.
