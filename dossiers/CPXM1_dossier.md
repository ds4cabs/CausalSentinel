# Protein Dossier — CPXM1 (Probable carboxypeptidase X1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| ER-positive Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | 0.0415 | 0.0196 | 0.0341 | Wald ratio | 1 | cis | NA |
| Endometrioid ovarian cancer | -0.146 | 0.073 | 0.0455 | Wald ratio | 1 | cis | NA |
| Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | 0.0281 | 0.0165 | 0.0877 | Wald ratio | 1 | cis | NA |
| Low grade serous ovarian cancer | -0.136 | 0.121 | 0.261 | Wald ratio | 1 | cis | NA |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_58 association rows across 36 traits (52 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| CPXM1/VEGFC protein level ratio | 2e-1224 | rs34211052 | 1 | GCST90314223 | no MR -> candidate analysis |
| CPXM1/DKK1 protein level ratio | 4e-1156 | rs34211052 | 1 | GCST90314218 | no MR -> candidate analysis |
| CPXM1/SPARC protein level ratio | 1e-1030 | rs34211052 | 1 | GCST90314222 | no MR -> candidate analysis |
| ANGPT1/CPXM1 protein level ratio | 3e-839 | rs34211052 | 1 | GCST90313262 | no MR -> candidate analysis |
| CPXM1/MDK protein level ratio | 1e-802 | rs34211052 | 1 | GCST90314221 | no MR -> candidate analysis |
| CPXM1/HBEGF protein level ratio | 2e-598 | rs34211052 | 1 | GCST90314219 | no MR -> candidate analysis |
| CPXM1/LGMN protein level ratio | 1e-582 | rs34211052 | 1 | GCST90314220 | no MR -> candidate analysis |
| Circulating CPXM1 levels | 2e-556 | rs215545 | 2 | GCST90860566 | no MR -> candidate analysis |
| Probable carboxypeptidase X1 levels | 1e-284 | rs6132968 | 5 | GCST90426612 | no MR -> candidate analysis |
| Cerebrospinal fluid protein CPXM1 levels | 3e-201 | rs6132968 | 1 | GCST90944214 | no MR -> candidate analysis |
| CPXM1 protein levels | 1e-195 | rs41310169 | 9 | GCST90468849 | no MR -> candidate analysis |
| Serum levels of protein CPXM1 | 5e-116 | rs13043754 | 2 | GCST90089322 | no MR -> candidate analysis |
| _...and 24 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 117 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| portal hypertension | 0.453 | — | common-variant locus | no MR -> candidate analysis |
| nodular goiter | 0.13 | — | common-variant locus | no MR -> candidate analysis |
| major depressive disorder | 0.082 | — | common-variant locus | no MR -> candidate analysis |
| information processing speed | 0.072 | — | common-variant locus | no MR -> candidate analysis |
| campylobacteriosis | 0.061 | — | common-variant locus | no MR -> candidate analysis |

> Of the 5 rows above, **5 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=2.7e-22, LOEUF=1.09 — LoF-tolerant |
| GWAS Catalog | 59 unique SNPs / 118 rows |
| ClinVar | 155 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 117 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'CPXM1'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 155 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 36 traits by best p-value, aggregated from 58 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q96SM3 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000088882/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CPXM1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CPXM1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CPXM1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CPXM1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:01:44  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
