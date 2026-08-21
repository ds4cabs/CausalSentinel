# Protein Dossier — PEBP1 (Phosphatidylethanolamine-binding protein 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Cancer code  self-reported: basal cell carcinoma | -0.204 | 0.0801 | 0.0111 | Wald ratio | 1 | cis | NA |
| Hearing difficulty or problems: Yes | 0.0259 | 0.0105 | 0.0133 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: migraine | -0.0941 | 0.0395 | 0.0173 | Wald ratio | 1 | cis | NA |
| Sodium in urine | 0.0139 | 0.00612 | 0.0228 | Wald ratio | 1 | cis | NA |
| Nucleus accumbens volume | -6.64 | 2.97 | 0.0253 | Wald ratio | 1 | cis | NA |
| Intracranial volume | 9.92e+03 | 4.48e+03 | 0.027 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: high cholesterol | -0.038 | 0.0175 | 0.0296 | Wald ratio | 1 | cis | NA |
| Pallidum volume | -10.5 | 5.05 | 0.0386 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: malignant melanoma | 0.127 | 0.0624 | 0.0412 | Wald ratio | 1 | cis | NA |
| Schizophrenia | 0.0409 | 0.0201 | 0.0423 | Wald ratio | 1 | cis | NA |
| Potassium in urine | 0.0127 | 0.00632 | 0.0442 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: depression | -0.05 | 0.027 | 0.0636 | Wald ratio | 1 | cis | NA |
| _...and 62 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-4276_10_2` | prostatic binding protein | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_8 association rows across 5 traits (8 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Phosphatidylethanolamine-binding protein 1 levels | 2e-117 | rs76597567 | 2 | GCST90248864 | no MR -> candidate analysis |
| Blood protein levels | 4e-111 | rs76597567 | 1 | GCST006585 | no MR -> candidate analysis |
| PEBP1 protein levels | 6e-49 | rs76597567 | 2 | GCST90470205 | no MR -> candidate analysis |
| Circulating PEBP1 levels | 1e-45 | rs76597567 | 2 | GCST90860664 | no MR -> candidate analysis |
| Positive affect | 2e-8 | rs7974375 | 1 | GCST007338 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 425 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| prostate carcinoma | 0.031 | — | common-variant locus | no MR -> candidate analysis |

> Of the 1 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Phosphatidylethanolamine-binding protein 1) |
| gnomAD constraint | pLI=3.4e-05, LOEUF=1.12 — LoF-tolerant |
| GWAS Catalog | 58 unique SNPs / 116 rows |
| ClinVar | 34 records; 11 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 425 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'PEBP1' and resolved to 'Phosphatidylethanolamine-binding protein 1' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 34 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 5 of 5 traits by best p-value, aggregated from 8 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P30086 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000089220/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4105856/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PEBP1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PEBP1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PEBP1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/PEBP1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:17:27  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
