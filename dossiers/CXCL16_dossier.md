# Protein Dossier — CXCL16 (C-X-C motif chemokine 16)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Crohn's disease | -0.475 | 0.0977 | 1.14e-06 | Wald ratio | 1 | trans | NA |
| Inflammatory bowel disease | -0.387 | 0.0809 | 1.71e-06 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: depression | 0.00687 | 0.00217 | 0.00158 | Inverse variance weighted | 3 | trans | NA |
| Non-cancer illness code  self-reported: depression | 0.00687 | 0.00217 | 0.00158 | Inverse variance weighted | 3 | trans | NA |
| Non-cancer illness code  self-reported: depression | 0.00687 | 0.00217 | 0.00158 | Inverse variance weighted | 3 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | -0.0412 | 0.0136 | 0.00236 | Inverse variance weighted | 3 | trans | NA |
| Heel bone mineral density (BMD) T-score  automated | -0.0412 | 0.0136 | 0.00236 | Inverse variance weighted | 3 | trans | NA |
| Heel bone mineral density (BMD) T-score  automated | -0.0412 | 0.0136 | 0.00236 | Inverse variance weighted | 3 | cis | NA |
| Ulcerative colitis | -0.303 | 0.102 | 0.00303 | Wald ratio | 1 | trans | NA |
| Age at menopause | 0.19 | 0.0684 | 0.00553 | Inverse variance weighted | 3 | trans | NA |
| Age at menopause | 0.19 | 0.0684 | 0.00553 | Inverse variance weighted | 3 | trans | NA |
| Age at menopause | 0.19 | 0.0684 | 0.00553 | Inverse variance weighted | 3 | cis | NA |
| _...and 271 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2436_49_4` | CXCL16, soluble | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_10 association rows across 4 traits (10 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating CXCL16 levels | 2e-216 | rs2304970 | 2 | GCST90859949 | no MR -> candidate analysis |
| CXCL16 protein levels | 4e-199 | rs60894000 | 2 | GCST90468928 | no MR -> candidate analysis |
| VMO1 protein levels | 2e-59 | rs186708492 | 2 | GCST90471042 | no MR -> candidate analysis |
| C-X-C motif chemokine 16 levels | 3e-42 | rs1876444 | 4 | GCST90247204 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 543 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| arthropathy | 0.211 | — | common-variant locus | no MR -> candidate analysis |
| nasal cavity polyp | 0.157 | — | common-variant locus | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1.7e-05, LOEUF=1.12 — LoF-tolerant |
| GWAS Catalog | 104 unique SNPs / 218 rows |
| ClinVar | 78 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 543 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'CXCL16'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 78 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 4 of 4 traits by best p-value, aggregated from 10 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9H2A7 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000161921/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CXCL16 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CXCL16 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CXCL16%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CXCL16 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:13:59  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
