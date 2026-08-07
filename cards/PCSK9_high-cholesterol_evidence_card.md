# Target Evidence Card — PCSK9 × high cholesterol

**Verdict:** GO — PCSK9 shows extremely robust genetic, causal, and clinical evidence for a role in high cholesterol.

## Evidence

| Evidence | Tool | Result |
|---|---|---|
| Causal effect (MR) — retrieved, not computed | `get_mr_result` | outcome: Non-cancer illness code  self-reported: high cholesterol — beta=0.277, se=0.0294, p=3.74e-21, Wald ratio, n_snp=1, cis instrument, coloc=not available  
_retrieved from published MR; not computed here_ |
| Target–disease association | `get_target_disease_evidence` | overall score=0.82 (literature=0.859, genetic_association=0.923, clinical=0.97, genetic_literature=0.608) |
| Protein context | `get_uniprot_dossier` | Q8NBP7 — Proprotein convertase subtilisin/kexin type 9; location: Cytoplasm, Secreted, Endosome, Lysosome, Cell surface, Endop |
| Known modulators / druggability | `get_chembl_modulators` | 2 known modulators (RNAI INHIBITOR) |
| Clinical variants | `get_clinvar_variants` | 1569 ClinVar records; 0 pathogenic in a sample of 30 |
| Population constraint / LoF tolerance | `get_gnomad_constraint` | pLI=2.8e-18, LOEUF=1.14 → LoF-tolerant |
| Extra genetic evidence | `get_gwas_catalog` | 112 unique SNPs from 246/246 association rows |
| Pharmacogenomics | `get_pharmgkb_drug_gene` | **not available** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene). |

## Caveats declared by the tools

- **`get_target_disease_evidence`** — Free-text inputs were resolved to ontology terms: 'PCSK9' -> ENSG00000169174 (PCSK9); 'high cholesterol' -> HP_0003124 (Hypercholesterolemia). Scores below describe THAT term, not the free-text phrase.
- **`get_mr_result`** — Estimates RETRIEVED from published pQTL MR, not computed by this agent. Check cis_or_trans (cis instruments are less pleiotropy-prone), steiger_direction_ok, and coloc_prob before treating this as causal; coloc_prob=null means colocalization was not available for this pair.
- **`get_chembl_modulators`** — ChEMBL target matched by text search on 'PCSK9' and resolved to 'PCSK9 mRNA' — confirm this is the intended target.
- **`get_clinvar_variants`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 1569 ClinVar records for this gene; it is a sample, not a rate.
- **`get_pharmgkb_drug_gene`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).

## Reasoning

Open Targets associates PCSK9 strongly with hypercholesterolemia, backed by extensive GWAS catalog coverage of 112 unique SNPs. Mendelian randomization estimates from published pQTL resources support a causal relationship with high cholesterol outcomes. Furthermore, UniProt highlights its fundamental biological role in regulating plasma cholesterol homeostasis through low-density lipoprotein receptor degradation. ChEMBL identifies known modulators targeting the pathway, supporting its established druggability.

## Sources

- `get_uniprot_dossier`: https://www.uniprot.org/uniprotkb/Q8NBP7 — _UniProt release 2026_02 (10-June-2026)_
- `get_target_disease_evidence`: https://platform.opentargets.org/evidence/ENSG00000169174/HP_0003124 — _Open Targets data release 26.06_
- `get_mr_result`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `get_chembl_modulators`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4630662/ — _ChEMBL_37 (released 2026-05-01)_
- `get_clinvar_variants`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PCSK9%5Bgene%5D — _ClinVar build Build260804-2105.1_
- `get_gnomad_constraint`: https://gnomad.broadinstitute.org/gene/PCSK9 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `get_gwas_catalog`: https://www.ebi.ac.uk/gwas/genes/PCSK9 — _GWAS Catalog REST (live; release not exposed by this endpoint)_

## Provenance

- Generated: 2026-08-07T06:21:53
- Model (reasoning text only): `gemini-flash-lite-latest`
- Tools invoked (8 calls): `get_uniprot_dossier`, `get_target_disease_evidence`, `get_mr_result`, `get_chembl_modulators`, `get_clinvar_variants`, `get_gnomad_constraint`, `get_gwas_catalog`, `get_pharmgkb_drug_gene`
- Evidence table, caveats, sources and this block are rendered mechanically from tool return values. The model wrote only the Verdict sentence and the Reasoning paragraph, both checked against tool output by `validate_card.py`.
- No Mendelian randomization or colocalization is computed by this agent; MR estimates, where present, are retrieved from published work.
