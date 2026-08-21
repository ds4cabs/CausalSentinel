# Protein Dossier — ECE1 (Endothelin-converting enzyme 1)

**MR feasibility tier: B** — No published MR estimate in this resource, BUT a pQTL GWAS exists - instruments are derivable, so a two-sample MR could be run. The upstream is waiting.

## 1. Published MR estimates (retrieved, not computed)

_None in the EpiGraphDB pQTL resource. Absence of an estimate is not evidence of no effect._

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3611_70_4` | Endothelin-converting enzyme 1 | Suhre K | 2019 |

> Instruments exist but no MR estimate is in this resource — **a two-sample MR here is un-run work.**

## 3. GWAS Catalog results — traits with signal at this locus

_98 association rows across 61 traits (81 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Height | 3e-157 | rs212526 | 7 | GCST90245848 | no MR -> candidate analysis |
| ECE1 protein levels | 7e-130 | rs148461660 | 2 | GCST90469061 | no MR -> candidate analysis |
| Alkaline phosphatase (UKB data field 30610) | 3e-112 | rs1067237 | 5 | GCST90468060 | no MR -> candidate analysis |
| Circulating ECE1 levels | 1e-110 | rs148461660 | 2 | GCST90860682 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 1e-48 | rs6702331 | 2 | GCST90838669 | no MR -> candidate analysis |
| Serum alkaline phosphatase levels | 1e-45 | rs6695985 | 12 | GCST90019494 | no MR -> candidate analysis |
| Standing height (UKB data field 50) | 1e-36 | rs797014597 | 1 | GCST90468178 | no MR -> candidate analysis |
| Height (baseline) | 6e-33 | rs212515 | 3 | GCST90565843 | no MR -> candidate analysis |
| Appendicular lean mass | 4e-29 | rs212526 | 1 | GCST90000025 | no MR -> candidate analysis |
| Body shape phenotype PC2 | 9e-28 | rs12743070 | 1 | GCST90832990 | no MR -> candidate analysis |
| Basophil count | 2e-23 | rs4060971 | 3 | GCST90002292 | no MR -> candidate analysis |
| Calcium levels (UKB data field 30680) | 3e-19 | rs34693054 | 1 | GCST90468065 | no MR -> candidate analysis |
| _...and 49 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 2621 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Hirschsprung disease | 0.72 | — | established (curated) | no MR -> candidate analysis |
| neurodegenerative disease | 0.187 | — | common-variant locus | no MR -> candidate analysis |
| liver disorder | 0.535 | — | common-variant locus | no MR -> candidate analysis |
| Aganglionic megacolon | 0.532 | — | established (curated) | no MR -> candidate analysis |
| stomach disorder | 0.484 | — | common-variant locus | no MR -> candidate analysis |
| dementia | 0.432 | — | common-variant locus | no MR -> candidate analysis |
| mathematical ability | 0.408 | — | common-variant locus | no MR -> candidate analysis |
| Anxiety | 0.402 | — | common-variant locus | no MR -> candidate analysis |
| placental abruption | 0.315 | — | common-variant locus | no MR -> candidate analysis |
| atrial fibrillation | 0.288 | — | common-variant locus | no MR -> candidate analysis |
| hypertensive disorder | 0.233 | — | common-variant locus | no MR -> candidate analysis |
| essential hypertension, genetic | 0.195 | — | established (curated) | no MR -> candidate analysis |

> Of the 12 rows above, **12 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 1 known modulators (Endothelin-converting enzyme 1) |
| gnomAD constraint | pLI=1, LOEUF=0.471 — LoF-INTOLERANT |
| GWAS Catalog | 91 unique SNPs / 182 rows |
| ClinVar | 197 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 2621 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'ECE1' and resolved to 'Endothelin-converting enzyme 1' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 197 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 61 traits by best p-value, aggregated from 98 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P42892 — _UniProt release 2026_02 (10-June-2026)_
- `phenome`: https://platform.opentargets.org/target/ENSG00000117298/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4791/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/ECE1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/ECE1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=ECE1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/ECE1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:22:40  ·  Tier: B
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: mr_outcomes
