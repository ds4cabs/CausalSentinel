# Protein Dossier — GHR (Growth hormone receptor)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Birth weight | -0.0498 | 0.033 | 0.131 | Wald ratio | 1 | cis | NA |
| Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | 0.0543 | 0.0386 | 0.16 | Wald ratio | 1 | cis | NA |
| ER-negative Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | 0.0744 | 0.0699 | 0.287 | Wald ratio | 1 | cis | NA |
| Low grade serous ovarian cancer | 0.238 | 0.294 | 0.418 | Wald ratio | 1 | cis | NA |
| ER-positive Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | 0.0313 | 0.0459 | 0.495 | Wald ratio | 1 | cis | NA |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2948_58_2` | Growth hormone receptor | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_140 association rows across 60 traits (122 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Height | 1e-300 | rs2910875 | 29 | GCST90245848 | no MR -> candidate analysis |
| GHR protein levels | 1e-298 | rs55730643 | 16 | GCST90469342 | no MR -> candidate analysis |
| Height (maximum, inv-normal transformed) | 2e-120 | rs55681913 | 2 | GCST90475359 | no MR -> candidate analysis |
| IGF 1 (UKB data field 30770) | 3e-71 | rs55681913 | 2 | GCST90468078 | no MR -> candidate analysis |
| What is your height? (cm, inv-normal transformed) | 4e-66 | rs55681913 | 2 | GCST90475368 | no MR -> candidate analysis |
| Growth hormone receptor levels | 1e-65 | rs10440652 | 4 | GCST90247729 | no MR -> candidate analysis |
| Standing height (UKB data field 50) | 2e-51 | rs55681913 | 2 | GCST90468178 | no MR -> candidate analysis |
| SELENOP protein levels | 1e-45 | rs4315928 | 1 | GCST90470565 | no MR -> candidate analysis |
| Height (baseline) | 9e-44 | rs55681913 | 8 | GCST90565843 | no MR -> candidate analysis |
| Appendicular lean mass | 8e-40 | rs62372052 | 2 | GCST90000025 | no MR -> candidate analysis |
| Whole body water mass (UKB data field 23102) | 5e-38 | rs62372052 | 2 | GCST90468184 | no MR -> candidate analysis |
| Body shape phenotype PC2 | 2e-35 | rs62372052 | 2 | GCST90832990 | no MR -> candidate analysis |
| _...and 48 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1358 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Laron syndrome | 0.919 | — | established (curated) | no MR -> candidate analysis |
| short stature due to partial GHR deficiency | 0.828 | — | established (curated) | no MR -> candidate analysis |
| growth hormone insensitivity syndrome | 0.835 | — | established (curated) | no MR -> candidate analysis |
| Short stature | 0.559 | — | established (curated) | no MR -> candidate analysis |
| hypercholesterolemia, familial, 1 | 0.81 | — | established (curated) | no MR -> candidate analysis |
| Abnormality of the skeletal system | 0.81 | — | common-variant locus | no MR -> candidate analysis |
| atrial fibrillation | 0.79 | — | common-variant locus | no MR -> candidate analysis |
| obesity disorder | 0.546 | — | common-variant locus | no MR -> candidate analysis |
| short stature due to GHSR deficiency | 0.525 | — | established (curated) | no MR -> candidate analysis |

> Of the 9 rows above, **9 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 6 known modulators (Growth hormone receptor) |
| gnomAD constraint | pLI=4e-05, LOEUF=0.692 — LoF-tolerant |
| GWAS Catalog | 102 unique SNPs / 208 rows |
| ClinVar | 681 records; 11 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1358 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'GHR' and resolved to 'Growth hormone receptor' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 681 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 60 traits by best p-value, aggregated from 140 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P10912 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000112964/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL1976/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/GHR — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/GHR — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=GHR%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/GHR — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:49:02  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
