# Protein Dossier — RAD51D (DNA repair protein RAD51 homolog 4)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Body mass index (BMI) | 0.0294 | 0.00537 | 4.15e-08 | Wald ratio | 1 | trans | 0.00381 |
| Heel bone mineral density (BMD) T-score  automated | 0.0375 | 0.00694 | 6.72e-08 | Wald ratio | 1 | trans | 0.999 |
| Forced expiratory volume in 1-second (FEV1) | -0.0208 | 0.00464 | 7.37e-06 | Wald ratio | 1 | trans | NA |
| Forced vital capacity (FVC) | -0.0195 | 0.0044 | 9.08e-06 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: hypertension | 0.0329 | 0.00886 | 2.04e-04 | Wald ratio | 1 | trans | NA |
| Birth weight | -0.0215 | 0.00819 | 0.00865 | Inverse variance weighted | 2 | trans | NA |
| Birth weight | -0.0215 | 0.00819 | 0.00865 | Inverse variance weighted | 2 | trans | NA |
| Eye problems or disorders: Diabetes related eye disease | 0.148 | 0.0597 | 0.0133 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: R04 Haemorrhage from respiratory passages | 0.154 | 0.0643 | 0.0166 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: K80 Cholelithiasis | 0.0806 | 0.0345 | 0.0196 | Wald ratio | 1 | trans | NA |
| Sodium in urine | 0.0118 | 0.00528 | 0.0256 | Wald ratio | 1 | trans | NA |
| Hearing difficulty or problems: Yes | 0.0197 | 0.00909 | 0.0299 | Wald ratio | 1 | trans | NA |
| _...and 86 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_2 association rows across 2 traits (2 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| CCL15 protein levels | 2e-16 | rs185961963 | 1 | GCST90468567 | no MR -> candidate analysis |
| CCL16 protein levels | 2e-14 | rs188753384 | 1 | GCST90468568 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 205 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Hereditary breast and ovarian cancer syndrome | 0.867 | — | established (curated) | no MR -> candidate analysis |
| ovarian cancer | 0.825 | — | established (curated) | MR: beta=-0.145, p=0.142 (trans) |
| hereditary breast ovarian cancer syndrome | 0.866 | — | established (curated) | no MR -> candidate analysis |
| ovarian carcinoma | 0.731 | — | established (curated) | no MR -> candidate analysis |
| RAD51D-related cancer predisposition | 0.817 | — | established (curated) | no MR -> candidate analysis |
| hereditary neoplastic syndrome | 0.946 | — | established (curated) | no MR -> candidate analysis |
| Inherited cancer-predisposing syndrome | 0.946 | — | established (curated) | no MR -> candidate analysis |
| gastric cancer | 0.859 | — | established (curated) | no MR -> candidate analysis |
| familial ovarian cancer | 0.867 | — | established (curated) | no MR -> candidate analysis |
| breast cancer | 0.824 | — | established (curated) | MR: beta=0.029, p=0.0306 (trans) |
| breast-ovarian cancer, familial, susceptibility to, 1 | 0.718 | — | established (curated) | no MR -> candidate analysis |
| Hereditary breast cancer | 0.696 | — | established (curated) | no MR -> candidate analysis |
| hereditary breast carcinoma | 0.696 | — | established (curated) | no MR -> candidate analysis |
| breast carcinoma | 0.547 | — | established (curated) | no MR -> candidate analysis |
| colorectal cancer | 0.559 | — | established (curated) | no MR -> candidate analysis |

> Of the 15 rows above, **13 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=7.7e-12, LOEUF=1.13 — LoF-tolerant |
| GWAS Catalog | 20 unique SNPs / 40 rows |
| ClinVar | 2130 records; 6 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 205 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'RAD51D'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 2130 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 2 of 2 traits by best p-value, aggregated from 2 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O75771 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000185379/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/RAD51D — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/RAD51D — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=RAD51D%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/RAD51D — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:45:07  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
