# Protein Dossier — PLAT (Tissue-type plasminogen activator)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: N81 Female genital prolapse | 0.265 | 0.0923 | 0.00412 | Wald ratio | 1 | cis | NA |
| Caudate volume | -83.5 | 33.2 | 0.0117 | Wald ratio | 1 | cis | NA |
| Low grade serous ovarian cancer | 0.808 | 0.329 | 0.014 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M54 Dorsalgia | 0.212 | 0.0904 | 0.0188 | Wald ratio | 1 | cis | NA |
| Rheumatoid arthritis | -0.286 | 0.123 | 0.0204 | Wald ratio | 1 | cis | NA |
| Weight | -0.0286 | 0.0126 | 0.023 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Ankle | 0.224 | 0.0985 | 0.0232 | Wald ratio | 1 | cis | NA |
| Putamen volume | -88.2 | 40.9 | 0.0309 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: D12 Benign neoplasm of colon  rectum  anus and anal canal | 0.202 | 0.0996 | 0.0423 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: G47 Sleep disorders | 0.285 | 0.143 | 0.0464 | Wald ratio | 1 | cis | NA |
| Thalamus volume | -82.5 | 42.2 | 0.0508 | Wald ratio | 1 | cis | NA |
| Melanoma | -0.674 | 0.348 | 0.0526 | Wald ratio | 1 | cis | NA |
| _...and 86 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2212_69_1` | tPA | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_9 association rows across 8 traits (7 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating PLAT levels | 1e-52 | rs8178885 | 1 | GCST90859980 | no MR -> candidate analysis |
| PLAT protein levels | 2e-51 | rs2020921 | 1 | GCST90470250 | no MR -> candidate analysis |
| Tissue-type plasminogen activator levels | 3e-43 | rs8178885 | 2 | GCST90249945 | no MR -> candidate analysis |
| Height | 1e-26 | rs2020922 | 1 | GCST90245848 | MR: beta=-0.0291, p=0.0568 (cis) |
| Plasma plasminogen activator levels | 2e-8 | rs2020921 | 1 | GCST002374 | no MR -> candidate analysis |
| Systemic lupus erythematosus | 3e-8 | rs1804182 | 1 | GCST005752 | no MR -> candidate analysis |
| Hair color | 9e-8 | rs2070711 | 1 | GCST007082 | no MR -> candidate analysis |
| Carboxyethyl-GABA levels in elite athletes | 7e-6 | rs3020640 | 1 | GCST90133545 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1921 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| pulmonary embolism | 0.195 | — | established (curated) | MR: beta=-0.446, p=0.0977 (cis) |
| placental abruption | 0.564 | — | common-variant locus | no MR -> candidate analysis |
| preeclampsia | 0.468 | — | common-variant locus | no MR -> candidate analysis |
| memory impairment | 0.466 | — | common-variant locus | no MR -> candidate analysis |

> Of the 4 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 8 known modulators (Tissue-type plasminogen activator) |
| gnomAD constraint | pLI=2.3e-10, LOEUF=0.816 — LoF-tolerant |
| GWAS Catalog | 19 unique SNPs / 38 rows |
| ClinVar | 178 records; 3 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1921 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'PLAT' and resolved to 'Tissue-type plasminogen activator' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 178 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 8 of 8 traits by best p-value, aggregated from 9 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P00750 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000104368/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL1873/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PLAT — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PLAT — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PLAT%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/PLAT — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:25:01  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
