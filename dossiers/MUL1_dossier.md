# Protein Dossier — MUL1 (Mitochondrial ubiquitin ligase activator of NFKB 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Glioma | 0.581 | 0.167 | 5.03e-04 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: D25 Leiomyoma of uterus | -0.277 | 0.106 | 0.00911 | Wald ratio | 1 | trans | NA |
| Endometrioid ovarian cancer | -0.25 | 0.105 | 0.0176 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: uterine fibroids | -0.18 | 0.0879 | 0.0401 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: bladder problem (not cancer) | -0.338 | 0.172 | 0.0486 | Wald ratio | 1 | trans | NA |
| Serum cystatin C (eGFRcys) | 0.0143 | 0.00736 | 0.052 | Wald ratio | 1 | trans | NA |
| Iron | -0.0729 | 0.0378 | 0.0539 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: sleep apnoea | 0.242 | 0.13 | 0.0628 | Wald ratio | 1 | trans | NA |
| Microalbuminuria | -0.153 | 0.0862 | 0.075 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: depression | -0.0698 | 0.0398 | 0.0799 | Wald ratio | 1 | trans | NA |
| Neo-openness to experience | 0.481 | 0.282 | 0.0882 | Wald ratio | 1 | trans | NA |
| Cancer code  self-reported: prostate cancer | -0.23 | 0.136 | 0.0901 | Wald ratio | 1 | trans | NA |
| _...and 89 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_7 association rows across 6 traits (7 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| CDA protein levels | 6e-18 | rs114564927 | 2 | GCST90468660 | no MR -> candidate analysis |
| General cognitive ability | 8e-10 | rs10916805 | 1 | GCST006269 | no MR -> candidate analysis |
| Verbal-numerical reasoning | 4e-9 | rs12076947 | 1 | GCST90011298 | no MR -> candidate analysis |
| Forced vital capacity (FVC) | 4e-9 | rs609210 | 1 | GCST90705071 | no MR -> candidate analysis |
| Protein quantitative trait loci (liver) | 9e-9 | rs7544348 | 1 | GCST011427 | no MR -> candidate analysis |
| Height | 2e-8 | rs501108 | 1 | GCST007841 | MR: beta=-0.0181, p=0.118 (trans) |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 129 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| jaw disease | 0.337 | — | common-variant locus | no MR -> candidate analysis |
| intelligence | 0.105 | — | common-variant locus | MR: beta=0.0534, p=0.274 (trans) |
| mathematical ability | 0.052 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=9.5e-10, LOEUF=1.19 — LoF-tolerant |
| GWAS Catalog | 66 unique SNPs / 131 rows |
| ClinVar | 92 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 129 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'MUL1'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 92 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 6 of 6 traits by best p-value, aggregated from 7 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q969V5 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000090432/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/MUL1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/MUL1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=MUL1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/MUL1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:53:28  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
