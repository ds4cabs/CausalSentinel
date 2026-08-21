# Protein Dossier — BCAN (Brevican core protein)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: S76 Injury of muscle and tendon at hip and thigh level | 1.01 | 0.27 | 1.86e-04 | Wald ratio | 1 | cis | NA |
| Potassium in urine | 0.0461 | 0.0145 | 0.00149 | Wald ratio | 1 | cis | NA |
| Creatinine (enzymatic) in urine | 0.0431 | 0.0137 | 0.00163 | Wald ratio | 1 | cis | NA |
| Pancreatic cancer | 0.862 | 0.275 | 0.00171 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertrophic cardiomyopathy (hcm  or  hocm) | 1.04 | 0.433 | 0.016 | Wald ratio | 1 | cis | NA |
| Sodium in urine | 0.0336 | 0.0141 | 0.0169 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: asthma | 0.0796 | 0.037 | 0.0316 | Wald ratio | 1 | cis | NA |
| Hippocampus volume | -60.3 | 28.1 | 0.0318 | Wald ratio | 1 | cis | NA |
| Thyroid cancer | 0.975 | 0.456 | 0.0323 | Wald ratio | 1 | cis | NA |
| Microalbuminuria | -0.254 | 0.119 | 0.0336 | Wald ratio | 1 | cis | NA |
| Neuroblastoma | -0.515 | 0.249 | 0.0387 | Wald ratio | 1 | cis | NA |
| Type 2 diabetes | -0.147 | 0.074 | 0.0468 | Wald ratio | 1 | cis | NA |
| _...and 99 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3461_58_1` | PGCB | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_38 association rows across 28 traits (36 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating BCAN levels | 4e-298 | rs2365715 | 3 | GCST90859689 | no MR -> candidate analysis |
| BCAN protein levels | 5e-292 | rs2365715 | 1 | GCST90468426 | no MR -> candidate analysis |
| BCAN/NPTXR protein level ratio | 3e-155 | rs3795736 | 1 | GCST90313482 | no MR -> candidate analysis |
| BCAN/DPP6 protein level ratio | 5e-148 | rs3795736 | 1 | GCST90313478 | no MR -> candidate analysis |
| BCAN/CD200 protein level ratio | 9e-144 | rs3795736 | 1 | GCST90313477 | no MR -> candidate analysis |
| BCAN/MOG protein level ratio | 2e-132 | rs3795736 | 1 | GCST90313480 | no MR -> candidate analysis |
| BCAN/KLK6 protein level ratio | 1e-129 | rs3795736 | 1 | GCST90313479 | no MR -> candidate analysis |
| HDGF protein levels | 7e-121 | rs150063652 | 3 | GCST90469442 | no MR -> candidate analysis |
| Brevican core protein levels | 4e-73 | rs2365715 | 5 | GCST90425778 | no MR -> candidate analysis |
| Serum levels of protein BCAN | 1e-31 | rs2365715 | 2 | GCST90088400 | no MR -> candidate analysis |
| Brevican core protein level in Chronic kidney disease with h | 1e-27 | rs113184515 | 1 | GCST90237392 | no MR -> candidate analysis |
| Brevican core protein levels (BCAN.3461.58.1) | 2e-26 | rs41267397 | 2 | GCST90240470 | no MR -> candidate analysis |
| _...and 16 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 160 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| chronic hepatitis | 0.271 | — | common-variant locus | no MR -> candidate analysis |
| myopia | 0.182 | — | established (curated) | no MR -> candidate analysis |
| pathological myopia | 0.182 | — | established (curated) | no MR -> candidate analysis |
| Decreased total leukocyte count | 0.083 | — | common-variant locus | no MR -> candidate analysis |

> Of the 4 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=3.7e-08, LOEUF=0.697 — LoF-tolerant |
| GWAS Catalog | 72 unique SNPs / 143 rows |
| ClinVar | 173 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 160 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'BCAN'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 173 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 28 traits by best p-value, aggregated from 38 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q96GW7 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000132692/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/BCAN — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/BCAN — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=BCAN%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/BCAN — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:16:07  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
