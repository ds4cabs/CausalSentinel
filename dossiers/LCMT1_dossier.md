# Protein Dossier — LCMT1 (Leucine carboxyl methyltransferase 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Serum creatinine (eGFRcrea) | -0.0142 | 0.00307 | 3.44e-06 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: K60 Fissure and fistula of anal and rectal regions | 0.344 | 0.0886 | 1.03e-04 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: Z09 Follow-up examination after treatment for conditions other than malignant neoplasms | 0.15 | 0.0588 | 0.0106 | Wald ratio | 1 | trans | NA |
| Type 2 diabetes | -0.107 | 0.0426 | 0.0121 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code self-reported: pulmonary embolism (with or without) dvt | -0.314 | 0.13 | 0.0154 | Wald ratio | 1 | trans | NA |
| Fracture resulting from simple fall | -0.0547 | 0.0235 | 0.0199 | Wald ratio | 1 | trans | NA |
| Fractured or broken bones in last 5 years | -0.058 | 0.0277 | 0.036 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | 0.171 | 0.0846 | 0.0431 | Wald ratio | 1 | trans | NA |
| Eye problems or disorders: Glaucoma | 0.123 | 0.0622 | 0.0485 | Wald ratio | 1 | trans | NA |
| Caudate volume | 32.5 | 16.7 | 0.0515 | Wald ratio | 1 | trans | NA |
| Neo-openness to experience | -0.437 | 0.229 | 0.0559 | Wald ratio | 1 | trans | NA |
| Haemoglobin concentration | -0.0408 | 0.0217 | 0.0603 | Wald ratio | 1 | trans | NA |
| _...and 100 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-4237_70_3` | LCMT1 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_4 association rows across 4 traits (3 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Height | 2e-12 | rs17774085 | 1 | GCST90245848 | MR: beta=0.00986, p=0.349 (trans) |
| Protein quantitative trait loci (liver) | 2e-8 | rs111254682 | 1 | GCST011427 | no MR -> candidate analysis |
| Alzheimer's disease or family history of Alzheimer's disease | 4e-8 | rs1248734336 | 1 | GCST90624094 | no MR -> candidate analysis |
| Color vision defects (Tritan) | 5e-8 | rs60713925 | 1 | GCST90301671 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 103 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| arthropathy | 0.528 | — | common-variant locus | no MR -> candidate analysis |
| kidney disorder | 0.401 | — | common-variant locus | no MR -> candidate analysis |
| gestational diabetes | 0.401 | — | common-variant locus | no MR -> candidate analysis |
| bile duct disorder | 0.372 | — | common-variant locus | no MR -> candidate analysis |
| Abnormality of the gastrointestinal tract | 0.355 | — | common-variant locus | no MR -> candidate analysis |

> Of the 5 rows above, **5 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1e-07, LOEUF=0.9 — LoF-tolerant |
| GWAS Catalog | 19 unique SNPs / 38 rows |
| ClinVar | 102 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 103 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'LCMT1'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 102 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 4 of 4 traits by best p-value, aggregated from 4 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9UIC8 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000205629/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/LCMT1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/LCMT1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=LCMT1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/LCMT1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:28:18  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
