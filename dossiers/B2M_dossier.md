# Protein Dossier — B2M (Beta-2-microglobulin)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | 0.983 | 0.0333 | 4.19e-191 | Wald ratio | 1 | trans | NA |
| Diastolic blood pressure  automated reading | 0.317 | 0.0205 | 5.54e-54 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: hypertension | 0.31 | 0.0251 | 5.15e-35 | Wald ratio | 1 | trans | NA |
| Platelet count | 34.2 | 3.46 | 4.64e-23 | Wald ratio | 1 | trans | NA |
| Systolic blood pressure  automated reading | 0.178 | 0.0205 | 3.52e-18 | Wald ratio | 1 | trans | NA |
| Haemoglobin concentration | 0.409 | 0.0475 | 7.05e-18 | Wald ratio | 1 | trans | NA |
| Total cholesterol | -0.248 | 0.03 | 1.25e-16 | Wald ratio | 1 | trans | NA |
| Packed cell volume | 1.1 | 0.15 | 1.75e-13 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: psoriasis | 0.674 | 0.0972 | 4.08e-12 | Wald ratio | 1 | trans | NA |
| Red blood cell count | 0.126 | 0.0183 | 6.71e-12 | Wald ratio | 1 | trans | NA |
| HDL cholesterol | -0.196 | 0.0292 | 1.89e-11 | Wald ratio | 1 | trans | NA |
| LDL cholesterol | -0.203 | 0.0308 | 4.26e-11 | Wald ratio | 1 | trans | NA |
| _...and 124 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3485_28_2` | b2-Microglobulin | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_No GWAS Catalog associations mapped to this gene._

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1076 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Immunodeficiency by defective expression of HLA class 1 | 0.778 | — | established (curated) | no MR -> candidate analysis |
| amyloidosis, hereditary systemic 6 | 0.715 | — | established (curated) | no MR -> candidate analysis |
| non-Hodgkin lymphoma | 0.559 | — | established (curated) | no MR -> candidate analysis |
| Familial renal amyloidosis | 0.734 | — | established (curated) | no MR -> candidate analysis |
| familial visceral amyloidosis | 0.734 | — | established (curated) | no MR -> candidate analysis |
| variant ABeta2M amyloidosis | 0.608 | — | established (curated) | no MR -> candidate analysis |
| Autosomal dominant beta2-microglobulinic amyloidosis | 0.608 | — | established (curated) | no MR -> candidate analysis |

> Of the 7 rows above, **7 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Beta-2-microglobulin) |
| gnomAD constraint | pLI=0.95, LOEUF=0.534 — LoF-INTOLERANT |
| GWAS Catalog | 19 unique SNPs / 42 rows |
| ClinVar | 118 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1076 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'B2M' and resolved to 'Beta-2-microglobulin' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 118 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — No GWAS Catalog associations mapped to this gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P61769 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000166710/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL1741302/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/B2M — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/B2M — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=B2M%5Bgene%5D — _ClinVar build Build260809-1055.1_

## Provenance

- Generated: 2026-08-14T01:13:22  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
