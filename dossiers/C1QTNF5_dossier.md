# Protein Dossier — C1QTNF5 (Complement C1q tumor necrosis factor-related protein 5)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Crohn's disease | -0.612 | 0.0489 | 7.15e-36 | Wald ratio | 1 | trans | 1.52e-05 |
| Inflammatory bowel disease | -0.445 | 0.0404 | 3.06e-28 | Wald ratio | 1 | trans | 1.54e-12 |
| Ulcerative colitis | -0.267 | 0.0509 | 1.50e-07 | Wald ratio | 1 | trans | 4.17e-14 |
| Microalbuminuria | 0.191 | 0.0562 | 6.70e-04 | Inverse variance weighted | 3 | trans | NA |
| Microalbuminuria | 0.191 | 0.0562 | 6.70e-04 | Inverse variance weighted | 3 | cis | NA |
| Microalbuminuria | 0.191 | 0.0562 | 6.70e-04 | Inverse variance weighted | 3 | trans | NA |
| Urinary albumin-to-creatinine ratio | 0.051 | 0.0163 | 0.00174 | Inverse variance weighted | 3 | trans | NA |
| Urinary albumin-to-creatinine ratio | 0.051 | 0.0163 | 0.00174 | Inverse variance weighted | 3 | cis | NA |
| Urinary albumin-to-creatinine ratio | 0.051 | 0.0163 | 0.00174 | Inverse variance weighted | 3 | trans | NA |
| Triglycerides | 0.0383 | 0.0133 | 0.00384 | Inverse variance weighted | 3 | trans | NA |
| Triglycerides | 0.0383 | 0.0133 | 0.00384 | Inverse variance weighted | 3 | cis | NA |
| Triglycerides | 0.0383 | 0.0133 | 0.00384 | Inverse variance weighted | 3 | trans | NA |
| _...and 308 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_2 association rows across 2 traits (2 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| C1QTNF5 protein levels | 4e-68 | rs2509656 | 1 | GCST90468489 | no MR -> candidate analysis |
| Complement C1q tumor necrosis factor-related protein 5 level | 4e-44 | rs2509656 | 1 | GCST90246768 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 967 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| late-onset retinal degeneration | 0.789 | — | established (curated) | no MR -> candidate analysis |
| Retinal dystrophy | 0.833 | — | established (curated) | no MR -> candidate analysis |
| retinitis pigmentosa | 0.195 | — | established (curated) | no MR -> candidate analysis |
| isolated microphthalmia 5 | 0.313 | — | established (curated) | no MR -> candidate analysis |
| hereditary disease | 0.307 | — | established (curated) | no MR -> candidate analysis |
| gout | 0.268 | — | common-variant locus | no MR -> candidate analysis |
| nanophthalmos 2 | 0.195 | — | established (curated) | no MR -> candidate analysis |

> Of the 7 rows above, **7 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.19, LOEUF=0.966 — LoF-tolerant |
| GWAS Catalog | 71 unique SNPs / 142 rows |
| ClinVar | 963 records; 5 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 967 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'C1QTNF5'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 963 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 2 of 2 traits by best p-value, aggregated from 2 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9BXJ0 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000223953/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/C1QTNF5 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/C1QTNF5 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=C1QTNF5%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/C1QTNF5 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:21:11  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
