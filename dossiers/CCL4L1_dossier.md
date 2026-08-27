# Protein Dossier — CCL4L1 (C-C motif chemokine 4-like)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Fractured bone site(s): Ankle | 0.267 | 0.0773 | 5.41e-04 | Wald ratio | 1 | cis | NA |
| Crohn's disease | -0.161 | 0.0589 | 0.00635 | Wald ratio | 1 | cis | NA |
| Chronic kidney disease | -0.201 | 0.0753 | 0.00766 | Wald ratio | 1 | cis | NA |
| Femoral neck bone mineral density | 0.0894 | 0.0366 | 0.0146 | Wald ratio | 1 | cis | NA |
| Platelet count | 4.99 | 2.08 | 0.0163 | Wald ratio | 1 | cis | NA |
| Low grade serous ovarian cancer | 0.543 | 0.232 | 0.0194 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K57 Diverticular disease of intestine | 0.164 | 0.0706 | 0.0203 | Wald ratio | 1 | cis | NA |
| Hip osteoarthritis | -0.304 | 0.138 | 0.0277 | Wald ratio | 1 | cis | NA |
| Fasting proinsulin | -0.0753 | 0.0356 | 0.0342 | Wald ratio | 1 | cis | NA |
| Neo-extraversion | 0.73 | 0.368 | 0.0475 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: pneumothorax | 0.661 | 0.339 | 0.051 | Wald ratio | 1 | cis | NA |
| Lumbar spine bone mineral density | 0.0814 | 0.0426 | 0.0564 | Wald ratio | 1 | cis | NA |
| _...and 87 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2781_63_2` | LAG-1 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_No GWAS Catalog associations mapped to this gene._

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 292 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| multiple sclerosis | 0.033 | — | common-variant locus | MR: beta=-0.116, p=0.148 (cis) |

> Of the 1 rows above, **0 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | not available |
| GWAS Catalog | no mapped SNPs |
| ClinVar | 30 records; 25 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 292 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'CCL4L1'.
- **`gnomad`** — No gnomAD constraint data.
- **`gwas`** — No GWAS Catalog SNPs mapped to this gene.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 30 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — No GWAS Catalog associations mapped to this gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q8NHW4 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000276070/associations — _Open Targets data release 26.06_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CCL4L1%5Bgene%5D — _ClinVar build Build260809-1055.1_

## Provenance

- Generated: 2026-08-14T01:38:16  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
