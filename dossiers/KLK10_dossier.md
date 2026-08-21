# Protein Dossier — KLK10 (Kallikrein-10)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Body fat | -0.213 | 0.0691 | 0.00203 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: pneumothorax | 0.471 | 0.195 | 0.0157 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: asthma | -0.0401 | 0.0178 | 0.024 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | 0.139 | 0.0634 | 0.0286 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: emphysema or chronic bronchitis | -0.125 | 0.06 | 0.0378 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N40 Hyperplasia of prostate | -0.149 | 0.0741 | 0.0438 | Wald ratio | 1 | cis | NA |
| Creatinine (enzymatic) in urine | 0.0118 | 0.00583 | 0.0439 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: basal cell carcinoma | -0.145 | 0.074 | 0.0502 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: Z09 Follow-up examination after treatment for conditions other than malignant neoplasms | -0.106 | 0.0553 | 0.0561 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R11 Nausea and vomiting | 0.156 | 0.0836 | 0.0614 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Diabetes related eye disease | -0.175 | 0.0937 | 0.0622 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R14 Flatulence and related conditions | 0.335 | 0.189 | 0.0767 | Wald ratio | 1 | cis | NA |
| _...and 79 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_38 association rows across 29 traits (35 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating KLK10 levels | 3e-2250 | rs3760738 | 2 | GCST90860356 | no MR -> candidate analysis |
| KLK10/KLK11 protein level ratio | 4e-1456 | rs201982139 | 1 | GCST90315253 | no MR -> candidate analysis |
| Kallikrein-10 levels | 4e-329 | rs2569454 | 5 | GCST90248155 | no MR -> candidate analysis |
| Cerebrospinal fluid protein KLK10 levels | 3e-199 | rs77303625 | 1 | GCST90944378 | no MR -> candidate analysis |
| KLK10 protein levels | 4e-154 | rs145472676 | 2 | GCST90469696 | no MR -> candidate analysis |
| KLK12 protein levels | 5e-122 | rs117025461 | 1 | GCST90469698 | no MR -> candidate analysis |
| Serum levels of protein KLK10 | 2e-117 | rs3760738 | 1 | GCST90089306 | no MR -> candidate analysis |
| Cerebrospinal fluid protein KLK11 levels | 1e-87 | rs2569451 | 1 | GCST90944379 | no MR -> candidate analysis |
| Blood protein levels in cardiovascular risk | 7e-76 | rs62115757 | 1 | GCST009731 | no MR -> candidate analysis |
| KLK14 protein levels | 3e-62 | rs7259451 | 1 | GCST90469700 | no MR -> candidate analysis |
| Blood protein levels | 4e-54 | rs2569454 | 1 | GCST006585 | no MR -> candidate analysis |
| CDSN/KLK8 protein level ratio | 8e-52 | rs3745535 | 1 | GCST90313996 | no MR -> candidate analysis |
| _...and 17 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 203 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| obesity disorder | 0.128 | — | common-variant locus | no MR -> candidate analysis |
| fracture of pelvis | 0.106 | — | common-variant locus | no MR -> candidate analysis |
| arthropathy | 0.078 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=3e-10, LOEUF=1.45 — LoF-tolerant |
| GWAS Catalog | 188 unique SNPs / 444 rows |
| ClinVar | 84 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 203 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'KLK10'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 84 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 29 traits by best p-value, aggregated from 38 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O43240 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000129451/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/KLK10 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/KLK10 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=KLK10%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/KLK10 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:22:43  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
