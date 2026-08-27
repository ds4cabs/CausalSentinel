# Protein Dossier — CCL1 (C-C motif chemokine 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Childhood intelligence | -0.148 | 0.049 | 0.00257 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: hypopituitarism | 0.719 | 0.264 | 0.00649 | Wald ratio | 1 | trans | NA |
| Body mass index (BMI) | 0.0242 | 0.00919 | 0.00862 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: R11 Nausea and vomiting | 0.283 | 0.112 | 0.0113 | Wald ratio | 1 | trans | NA |
| Knee osteoarthritis | 0.277 | 0.11 | 0.0119 | Wald ratio | 1 | trans | NA |
| Age at menarche | -0.054 | 0.0222 | 0.015 | Wald ratio | 1 | trans | NA |
| Ischemic stroke | 0.147 | 0.0608 | 0.0158 | Wald ratio | 1 | trans | NA |
| Microalbuminuria | 0.191 | 0.0792 | 0.016 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: I48 Atrial fibrillation and flutter | -0.279 | 0.117 | 0.0173 | Wald ratio | 1 | trans | NA |
| Sodium in urine | 0.0202 | 0.00905 | 0.0253 | Wald ratio | 1 | trans | NA |
| Creatinine (enzymatic) in urine | 0.0195 | 0.00881 | 0.0271 | Wald ratio | 1 | trans | NA |
| Small vessel disease | 0.294 | 0.134 | 0.0279 | Wald ratio | 1 | trans | NA |
| _...and 107 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2770_51_2` | I-309 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_21 association rows across 15 traits (16 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating CCL13 levels (id: OID00504_OID20655) | 2e-334 | rs159314 | 1 | GCST90859860 | no MR -> candidate analysis |
| CCL13/CCL2 protein level ratio | 2e-277 | rs16969619 | 1 | GCST90313675 | no MR -> candidate analysis |
| Circulating CCL13 levels (id: OID00768_OID20655) | 7e-248 | rs159314 | 1 | GCST90860103 | no MR -> candidate analysis |
| CCL11/CCL13 protein level ratio | 9e-236 | rs16969619 | 1 | GCST90313671 | no MR -> candidate analysis |
| Serum levels of protein CCL7 | 2e-26 | rs182223589 | 1 | GCST90088794 | no MR -> candidate analysis |
| CCL8 protein levels | 2e-25 | rs118139462 | 7 | GCST90468586 | no MR -> candidate analysis |
| RANTES levels | 2e-9 | rs295070 | 1 | GCST90428431 | no MR -> candidate analysis |
| Protein quantitative trait loci (liver) | 2e-8 | rs159250 | 1 | GCST011427 | no MR -> candidate analysis |
| Gut microbiome abundance (class Clostridium sensu stricto sp | 2e-8 | rs80018508 | 1 | GCST90569115 | no MR -> candidate analysis |
| Chronic obstructive pulmonary disease or colon polyp (MTAG) | 2e-8 | rs78975483 | 1 | GCST90570621 | no MR -> candidate analysis |
| Anti-hepatitis C virus antibody seropositivity | 8e-8 | rs75125828 | 1 | GCST90104165 | no MR -> candidate analysis |
| Color vision defects (Tritan) | 5e-7 | rs78565129 | 1 | GCST90301671 | no MR -> candidate analysis |
| _...and 3 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 516 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| alcohol drinking | 0.093 | — | common-variant locus | no MR -> candidate analysis |

> Of the 1 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.00021, LOEUF=2.09 — LoF-tolerant |
| GWAS Catalog | 95 unique SNPs / 172 rows |
| ClinVar | 21 records; 5 pathogenic in sample of 21 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 516 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'CCL1'.
- **`clinvar`** — Pathogenic count is over the 21 record(s) retrieved, NOT over all 21 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 15 of 15 traits by best p-value, aggregated from 21 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P22362 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000108702/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CCL1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CCL1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CCL1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CCL1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:30:24  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
