# Target Evidence Card — TREM2 × Alzheimer disease

**Verdict:** GO — Strong genetic and biological evidence supports TREM2 as a target for Alzheimer disease, driven by robust genetic associations and its known microglial receptor role in amyloid-beta and lipoprotein clearance.

> **Question actually answered:** the free-text disease was resolved to **MONDO_0004975 (Alzheimer disease)**. If that is not what you meant, every score below answers a different question.

## Evidence

| Evidence | Tool | Result |
|---|---|---|
| Causal effect (MR) — retrieved, not computed | `get_mr_result` | **not available** — no pQTL MR estimate for this protein in the resource (absence of an estimate is not evidence of no effect) |
| Target–disease association | `get_target_disease_evidence` | overall score=0.558 (literature=0.994, animal_model=0.288, genetic_association=0.862) |
| Protein context | `get_uniprot_dossier` | Q9NZC2 — Triggering receptor expressed on myeloid cells 2; location: Cell membrane, Secreted, Secreted |
| Known modulators / druggability | `get_chembl_modulators` | **tool error** — ChEMBL HTTP 500 |
| Clinical variants | `get_clinvar_variants` | 202 ClinVar records; 5 pathogenic in a sample of 30 |
| Population constraint / LoF tolerance | `get_gnomad_constraint` | pLI=7.9e-07, LOEUF=1.27 → LoF-tolerant |
| Extra genetic evidence | `get_gwas_catalog` | 70 unique SNPs from 140/140 association rows |
| Pharmacogenomics | `get_pharmgkb_drug_gene` | **not available** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene). |

## Caveats declared by the tools

- **`get_target_disease_evidence`** — Free-text inputs were resolved to ontology terms: 'TREM2' -> ENSG00000095970 (TREM2); 'Alzheimer disease' -> MONDO_0004975 (Alzheimer disease). Scores below describe THAT term, not the free-text phrase.
- **`get_mr_result`** — TREM2 HAS pQTL MR estimates in this resource, but NONE matched the requested disease 'Alzheimer disease'. The other outcomes are listed for context only — do not present them as evidence about 'Alzheimer disease'.
- **`get_clinvar_variants`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 202 ClinVar records for this gene; it is a sample, not a rate.
- **`get_pharmgkb_drug_gene`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).

## Reasoning

Open Targets demonstrates a strong overall association score between TREM2 and Alzheimer disease, with particularly high genetic association evidence. UniProt confirms that TREM2 acts as a receptor for amyloid-beta peptide 42 and apolipoproteins, mediating microglial activation, phagocytosis, and lipid metabolism. ClinVar records pathogenic variants in the gene, and gnomAD constraint metrics indicate that TREM2 is tolerant to loss-of-function variants. While no specific Mendelian randomization estimate was available for Alzheimer disease, the combination of strong genetic associations and microglial biology supports its pursuit.

## Sources

- `get_uniprot_dossier`: https://www.uniprot.org/uniprotkb/Q9NZC2 — _UniProt release 2026_02 (10-June-2026)_
- `get_target_disease_evidence`: https://platform.opentargets.org/evidence/ENSG00000095970/MONDO_0004975 — _Open Targets data release 26.06_
- `get_mr_result`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `get_clinvar_variants`: https://www.ncbi.nlm.nih.gov/clinvar/?term=TREM2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `get_gnomad_constraint`: https://gnomad.broadinstitute.org/gene/TREM2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `get_gwas_catalog`: https://www.ebi.ac.uk/gwas/genes/TREM2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_

## Provenance

- Generated: 2026-08-17T22:29:37
- Model (reasoning text only): `gemini-flash-lite-latest`
- Tools invoked (8 calls): `get_uniprot_dossier`, `get_target_disease_evidence`, `get_mr_result`, `get_chembl_modulators`, `get_clinvar_variants`, `get_gnomad_constraint`, `get_gwas_catalog`, `get_pharmgkb_drug_gene`
- Evidence table, caveats, sources and this block are rendered mechanically from tool return values. The model wrote only the Verdict sentence and the Reasoning paragraph, both checked against tool output by `validate_card.py`.
- No Mendelian randomization or colocalization is computed by this agent; MR estimates, where present, are retrieved from published work.

> **VALIDATION FAILED** — the model wrote claim tokens with no support in tool output:
> - [modality-not-in-chembl] `peptide`
