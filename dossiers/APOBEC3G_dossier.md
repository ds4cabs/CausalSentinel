# Protein Dossier — APOBEC3G (DNA dC->dU-editing enzyme APOBEC-3G)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: hiatus hernia | 0.273 | 0.0837 | 0.00112 | Wald ratio | 1 | cis | NA |
| Lumbar spine bone mineral density | 0.214 | 0.0682 | 0.00172 | Wald ratio | 1 | cis | NA |
| Red blood cell count | 0.0371 | 0.0155 | 0.0166 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K44 Diaphragmatic hernia | 0.247 | 0.105 | 0.0193 | Wald ratio | 1 | cis | NA |
| Mean platelet volume | 0.0167 | 0.00735 | 0.0227 | Wald ratio | 1 | cis | NA |
| Triglycerides | -0.0739 | 0.0331 | 0.0254 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N40 Hyperplasia of prostate | 0.288 | 0.132 | 0.0296 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hayfever or allergic rhinitis | -0.177 | 0.0823 | 0.0311 | Wald ratio | 1 | cis | NA |
| Neuroticism | -0.0612 | 0.0286 | 0.0321 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: emphysema or chronic bronchitis | 0.231 | 0.116 | 0.0469 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: C50 Malignant neoplasm of breast | -0.399 | 0.203 | 0.0501 | Wald ratio | 1 | cis | NA |
| Invasive mucinous ovarian cancer | -0.552 | 0.293 | 0.0593 | Wald ratio | 1 | cis | NA |
| _...and 94 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_2 association rows across 2 traits (2 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| DNA dC->dU-editing enzyme APOBEC-3G levels | 5e-43 | rs6519166 | 1 | GCST90246553 | no MR -> candidate analysis |
| Monocyte count | 7e-9 | rs113023 | 1 | GCST90056177 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 146 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| inborn disorder of amino acid metabolism | 0.386 | — | common-variant locus | no MR -> candidate analysis |
| acquired thrombocytopenia | 0.209 | — | common-variant locus | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (DNA dC->dU-editing enzyme APOBEC-3G) |
| gnomAD constraint | pLI=8.4e-14, LOEUF=1.13 — LoF-tolerant |
| GWAS Catalog | 55 unique SNPs / 110 rows |
| ClinVar | 58 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 146 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'APOBEC3G' and resolved to 'DNA dC->dU-editing enzyme APOBEC-3G' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 58 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 2 of 2 traits by best p-value, aggregated from 2 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9HC16 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000239713/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL1741217/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/APOBEC3G — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/APOBEC3G — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=APOBEC3G%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/APOBEC3G — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:08:06  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
