# Protein Dossier — RNASE4 (Ribonuclease 4)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Hirschsprung's disease | 1.56 | 0.324 | 1.40e-06 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertension | 0.0342 | 0.0108 | 0.00152 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K40 Inguinal hernia | -0.14 | 0.0461 | 0.00243 | Wald ratio | 1 | cis | NA |
| Haemoglobin concentration | -0.0516 | 0.0178 | 0.00373 | Wald ratio | 1 | cis | NA |
| Juvenile idiopathic arthritis | -0.389 | 0.139 | 0.00522 | Wald ratio | 1 | cis | NA |
| Height | -0.0218 | 0.00846 | 0.00991 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertrophic cardiomyopathy (hcm  or  hocm) | 0.658 | 0.256 | 0.0102 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: depression | -0.0682 | 0.0289 | 0.0182 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M54 Dorsalgia | 0.107 | 0.0457 | 0.0194 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hayfever or allergic rhinitis | 0.0591 | 0.0254 | 0.02 | Wald ratio | 1 | cis | NA |
| Nucleus accumbens volume | 6.65 | 2.9 | 0.0217 | Wald ratio | 1 | cis | NA |
| Percent emphysema | -0.0592 | 0.026 | 0.023 | Wald ratio | 1 | cis | NA |
| _...and 104 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_47 association rows across 18 traits (41 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating ANG levels | 1e-1158 | rs10220701 | 5 | GCST90860430 | no MR -> candidate analysis |
| ANG/F9 protein level ratio | 6e-1118 | rs17114671 | 1 | GCST90313259 | no MR -> candidate analysis |
| Angiogenin levels | 3e-452 | rs11851044 | 12 | GCST90246501 | no MR -> candidate analysis |
| RNASE4 protein levels | 2e-247 | rs143247343 | 5 | GCST90470478 | no MR -> candidate analysis |
| Serum levels of protein ANG | 2e-86 | rs36071889 | 3 | GCST90088789 | no MR -> candidate analysis |
| ANG protein levels | 1e-69 | rs552960263 | 5 | GCST90468307 | no MR -> candidate analysis |
| Ribonuclease 4 levels | 8e-45 | rs4470055 | 3 | GCST90426424 | no MR -> candidate analysis |
| Ribonuclease 4 levels (RNASE4.5644.60.3) | 1e-36 | rs184297073 | 2 | GCST90242666 | no MR -> candidate analysis |
| RNASE6 protein levels | 4e-28 | rs3748338 | 1 | GCST90470479 | no MR -> candidate analysis |
| Blood protein levels | 1e-18 | rs1888560 | 1 | GCST006585 | no MR -> candidate analysis |
| Protein quantitative trait loci | 1e-17 | rs34121942 | 1 | GCST010900 | no MR -> candidate analysis |
| Ribonuclease 4 level in Chronic kidney disease with hyperten | 4e-15 | rs944438 | 1 | GCST90238008 | no MR -> candidate analysis |
| _...and 6 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 107 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| amyotrophic lateral sclerosis | 0.847 | — | established (curated) | no MR -> candidate analysis |
| schizophrenia | 0.537 | — | common-variant locus | MR: beta=-0.0516, p=0.0677 (cis) |
| frontotemporal dementia | 0.426 | — | established (curated) | no MR -> candidate analysis |
| hereditary disease | 0.306 | — | established (curated) | no MR -> candidate analysis |
| frontotemporal dementia with motor neuron disease | 0.195 | — | established (curated) | no MR -> candidate analysis |

> Of the 5 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | not available |
| GWAS Catalog | 105 unique SNPs / 226 rows |
| ClinVar | 172 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 107 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'RNASE4'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 172 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 18 of 18 traits by best p-value, aggregated from 47 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P34096 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000258818/associations — _Open Targets data release 26.06_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/RNASE4 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=RNASE4%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/RNASE4 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:51:21  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: gnomad
