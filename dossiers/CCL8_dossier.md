# Protein Dossier — CCL8 (C-C motif chemokine 8)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Crohn's disease | 0.109 | 0.0358 | 0.00239 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: kidney stone or ureter stone or bladder stone | 0.195 | 0.066 | 0.00311 | Wald ratio | 1 | cis | NA |
| Inflammatory bowel disease | 0.0795 | 0.0294 | 0.00689 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: mania or bipolar disorder or manic depression | 0.265 | 0.108 | 0.014 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | 0.165 | 0.0717 | 0.0215 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M17 Gonarthrosis [arthrosis of knee] | -0.127 | 0.058 | 0.0286 | Wald ratio | 1 | cis | NA |
| Percent emphysema | 0.0623 | 0.0287 | 0.03 | Wald ratio | 1 | cis | NA |
| Microalbuminuria | -0.121 | 0.0574 | 0.0348 | Wald ratio | 1 | cis | NA |
| Subjective well being | 0.017 | 0.0085 | 0.0455 | Wald ratio | 1 | cis | NA |
| Fracture resulting from simple fall | -0.0379 | 0.0194 | 0.0508 | Wald ratio | 1 | cis | NA |
| Mean platelet volume | -0.00574 | 0.00298 | 0.0538 | Wald ratio | 1 | cis | NA |
| Systemic lupus erythematosus | -0.259 | 0.136 | 0.0575 | Wald ratio | 1 | cis | NA |
| _...and 97 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2785_15_2` | MCP-2 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_88 association rows across 40 traits (76 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating CCL8 levels (id: OID00549_OID21466) | 1e-5501 | rs1133763 | 4 | GCST90859899 | no MR -> candidate analysis |
| Circulating CCL8 levels (id: OID00795_OID21466) | 4e-3481 | rs1133763 | 4 | GCST90860127 | no MR -> candidate analysis |
| C-C motif chemokine 8 levels | 8e-1704 | rs1133763 | 8 | GCST90246922 | no MR -> candidate analysis |
| C-C motif chemokine 7 levels | 2e-718 | rs1133763 | 10 | GCST90246921 | no MR -> candidate analysis |
| CCL13/CCL8 protein level ratio | 9e-495 | rs11652256 | 1 | GCST90313676 | no MR -> candidate analysis |
| Blood protein levels | 2e-460 | rs4795912 | 6 | GCST006585 | no MR -> candidate analysis |
| CCL13 protein levels | 4e-263 | rs3136674 | 2 | GCST90468565 | no MR -> candidate analysis |
| C-C motif chemokine 8 (analyte X13748.4) levels | 1e-187 | rs12450497 | 1 | GCST90422346 | no MR -> candidate analysis |
| Corneodesmosin levels | 1e-120 | rs3136674 | 1 | GCST90247131 | no MR -> candidate analysis |
| CCL8 protein levels | 2e-116 | rs34202026 | 16 | GCST90468586 | no MR -> candidate analysis |
| Serum levels of protein CCL8 | 5e-109 | rs3138036 | 1 | GCST90088070 | no MR -> candidate analysis |
| C-C motif chemokine 7 levels (CCL7.4886.3.1) | 7e-72 | rs11342894 | 2 | GCST90240501 | no MR -> candidate analysis |
| _...and 28 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 456 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| alcohol drinking | 0.198 | — | common-variant locus | no MR -> candidate analysis |
| systemic lupus erythematosus | 0.04 | — | common-variant locus | MR: beta=-0.259, p=0.0575 (cis) |
| inflammatory bowel disease | 0.135 | — | common-variant locus | MR: beta=0.0795, p=0.00689 (cis) |
| cartilage disease | 0.095 | — | common-variant locus | no MR -> candidate analysis |

> Of the 4 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.24, LOEUF=1.17 — LoF-tolerant |
| GWAS Catalog | 87 unique SNPs / 174 rows |
| ClinVar | 38 records; 3 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 456 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'CCL8'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 38 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 40 traits by best p-value, aggregated from 88 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P80075 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000108700/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CCL8 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CCL8 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CCL8%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CCL8 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:39:35  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
