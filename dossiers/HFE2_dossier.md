# Protein Dossier — HFE2 (Hemojuvelin)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Triglycerides | -0.05 | 0.0143 | 4.84e-04 | Wald ratio | 1 | trans | NA |
| Urate | -0.0549 | 0.0165 | 8.58e-04 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: emphysema or chronic bronchitis | 0.155 | 0.0554 | 0.00514 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: gout | -0.21 | 0.0777 | 0.00679 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: N92 Excessive  frequent and irregular menstruation | 0.115 | 0.0464 | 0.0135 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: D12 Benign neoplasm of colon  rectum  anus and anal canal | 0.133 | 0.0553 | 0.0164 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: R55 Syncope and collapse | 0.161 | 0.0677 | 0.0177 | Wald ratio | 1 | trans | NA |
| 2hr glucose | 0.137 | 0.0579 | 0.0179 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: migraine | 0.0859 | 0.0396 | 0.0301 | Wald ratio | 1 | trans | NA |
| Chronic kidney disease | -0.0975 | 0.0457 | 0.0329 | Wald ratio | 1 | trans | NA |
| Nucleus accumbens volume | -6.98 | 3.28 | 0.033 | Wald ratio | 1 | trans | NA |
| Body mass index (BMI) | 0.0158 | 0.00745 | 0.0345 | Wald ratio | 1 | trans | NA |
| _...and 111 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3332_57_1` | RGM-C | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_No GWAS Catalog associations mapped to this gene._

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 224 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| hemochromatosis type 2A | 0.955 | — | established (curated) | no MR -> candidate analysis |
| hemochromatosis type 2 | 0.657 | — | established (curated) | no MR -> candidate analysis |
| hemochromatosis type 1 | 0.684 | — | established (curated) | no MR -> candidate analysis |
| type 2 diabetes mellitus | 0.14 | — | common-variant locus | no MR -> candidate analysis |

> Of the 4 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | not available |
| GWAS Catalog | no mapped SNPs |
| ClinVar | no records |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 224 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'HFE2'.
- **`gnomad`** — No gnomAD constraint data.
- **`gwas`** — No GWAS Catalog SNPs mapped to this gene.
- **`clinvar`** — No ClinVar records.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — No GWAS Catalog associations mapped to this gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q6ZVN8 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000168509/associations — _Open Targets data release 26.06_

## Provenance

- Generated: 2026-08-14T02:59:44  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
