# Protein Dossier — PPBP (Platelet basic protein)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Height | -0.0901 | 0.0197 | 4.84e-06 | Wald ratio | 1 | trans | NA |
| Forced vital capacity (FVC) | -0.039 | 0.0116 | 7.66e-04 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: pernicious anaemia | 0.44 | 0.174 | 0.0113 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: hiatus hernia | -0.312 | 0.129 | 0.0158 | Wald ratio | 1 | trans | NA |
| ER-positive Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | 0.109 | 0.0451 | 0.0158 | Wald ratio | 1 | trans | NA |
| Mean cell haemoglobin concentration | -0.0501 | 0.0208 | 0.0162 | Wald ratio | 1 | trans | NA |
| Subjective well being | 0.0394 | 0.0169 | 0.0196 | Wald ratio | 1 | trans | NA |
| Heel bone mineral density (BMD) T-score  automated | 0.0422 | 0.0183 | 0.0208 | Wald ratio | 1 | trans | NA |
| Hearing difficulty or problems: Yes | 0.0499 | 0.0232 | 0.0314 | Wald ratio | 1 | trans | NA |
| ER-negative Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.146 | 0.0693 | 0.0352 | Wald ratio | 1 | trans | NA |
| Forced expiratory volume in 1-second (FEV1) | -0.0256 | 0.0122 | 0.0362 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: arthritis (nos) | 0.265 | 0.127 | 0.0376 | Wald ratio | 1 | trans | NA |
| _...and 92 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2790_54_2` | NAP-2 | Suhre K | 2019 |
| `prot-c-4544_4_3` | CTAP-III | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_78 association rows across 66 traits (73 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| C-X-C motif chemokine 5 levels | 8e-172 | rs450373 | 2 | GCST90274782 | no MR -> candidate analysis |
| Blood protein levels | 5e-119 | rs450373 | 12 | GCST006585 | no MR -> candidate analysis |
| PPBP protein levels | 5e-45 | rs202224981 | 1 | GCST90470289 | no MR -> candidate analysis |
| Albumin levels | 1e-36 | rs184650103 | 1 | GCST90132699 | no MR -> candidate analysis |
| CXCL6 protein levels | 3e-26 | rs73824600 | 1 | GCST90468933 | no MR -> candidate analysis |
| Serum levels of protein HMP19 | 8e-26 | rs3756074 | 1 | GCST90087426 | no MR -> candidate analysis |
| Annexin A6 levels | 1e-24 | rs3756074 | 1 | GCST90246525 | no MR -> candidate analysis |
| Serum levels of protein BMP4 | 9e-23 | rs3756074 | 1 | GCST90089352 | no MR -> candidate analysis |
| BGN protein levels | 2e-22 | rs3756074 | 1 | GCST90468441 | no MR -> candidate analysis |
| Serum levels of protein SETD2 | 1e-21 | rs3756074 | 1 | GCST90087122 | no MR -> candidate analysis |
| Serum levels of protein FAM174B | 1e-21 | rs3756074 | 1 | GCST90090475 | no MR -> candidate analysis |
| Chymotrypsin-C levels | 6e-20 | rs3756074 | 1 | GCST90247186 | no MR -> candidate analysis |
| _...and 54 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 578 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| injury | 0.075 | — | common-variant locus | no MR -> candidate analysis |
| phosphorus metabolism disease | 0.075 | — | common-variant locus | no MR -> candidate analysis |
| acute cystitis | 0.075 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.0013, LOEUF=1.75 — LoF-tolerant |
| GWAS Catalog | 87 unique SNPs / 174 rows |
| ClinVar | 40 records; 14 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 578 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'PPBP'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 40 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 66 traits by best p-value, aggregated from 78 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P02775 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000163736/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PPBP — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PPBP — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PPBP%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/PPBP — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:33:41  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
