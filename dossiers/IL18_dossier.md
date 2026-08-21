# Protein Dossier — IL18 (Interleukin-18)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Type 2 diabetes | 0.223 | 0.0615 | 2.85e-04 | Inverse variance weighted | 2 | trans | NA |
| Type 2 diabetes | 0.223 | 0.0615 | 2.85e-04 | Inverse variance weighted | 2 | cis | NA |
| Potassium in urine | -0.0239 | 0.00753 | 0.00154 | Inverse variance weighted | 2 | trans | NA |
| Potassium in urine | -0.0239 | 0.00753 | 0.00154 | Inverse variance weighted | 2 | cis | NA |
| Non-cancer illness code  self-reported: bone disorder | 0.351 | 0.113 | 0.00189 | Inverse variance weighted | 2 | trans | NA |
| Non-cancer illness code  self-reported: bone disorder | 0.351 | 0.113 | 0.00189 | Inverse variance weighted | 2 | cis | NA |
| Systemic lupus erythematosus | -0.524 | 0.178 | 0.00327 | Wald ratio | 1 | cis | NA |
| Sodium in urine | -0.0199 | 0.00731 | 0.00653 | Inverse variance weighted | 2 | trans | NA |
| Sodium in urine | -0.0199 | 0.00731 | 0.00653 | Inverse variance weighted | 2 | cis | NA |
| Lung adenocarcinoma | -0.235 | 0.0908 | 0.00955 | Inverse variance weighted | 2 | trans | NA |
| Lung adenocarcinoma | -0.235 | 0.0908 | 0.00955 | Inverse variance weighted | 2 | cis | NA |
| 2hr glucose | -0.183 | 0.0724 | 0.0116 | Wald ratio | 1 | cis | NA |
| _...and 160 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_12 association rows across 8 traits (10 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Interleukin-18 levels | 1e-119 | rs5744249 | 5 | GCST90012024 | no MR -> candidate analysis |
| Circulating PTS levels | 1e-53 | rs111311302 | 1 | GCST90860729 | no MR -> candidate analysis |
| IL18 protein levels | 1e-12 | rs5744254 | 1 | GCST90469567 | no MR -> candidate analysis |
| Age of smoking initiation (MTAG) | 4e-10 | rs5744250 | 1 | GCST007462 | no MR -> candidate analysis |
| Smoking initiation (MTAG) | 1e-9 | rs117695734 | 1 | GCST90296430 | no MR -> candidate analysis |
| Bone mineral density variability | 2e-8 | rs143917761 | 1 | GCST90321119 | no MR -> candidate analysis |
| Trypanosoma cruzi infection | 8e-7 | rs4937075 | 1 | GCST90026452 | no MR -> candidate analysis |
| Vaginal microbiome MetaCyc pathway (KDO-NAGLIPASYN-PWY|super | 1e-6 | rs5744233 | 1 | GCST90026751 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1985 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| smoking initiation | 0.211 | — | common-variant locus | no MR -> candidate analysis |
| systemic lupus erythematosus | 0.059 | — | common-variant locus | MR: beta=-0.524, p=0.00327 (cis) |

> Of the 2 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 3 known modulators (Interleukin-18) |
| gnomAD constraint | pLI=0.031, LOEUF=1.01 — LoF-tolerant |
| GWAS Catalog | 39 unique SNPs / 78 rows |
| ClinVar | 37 records; 9 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 4 clinical annotations across 3 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1985 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'IL18' and resolved to 'Interleukin-18' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 37 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 8 of 8 traits by best p-value, aggregated from 12 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q14116 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000150782/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL1741305/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/IL18 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/IL18 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=IL18%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=IL18 — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/IL18 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:12:39  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
