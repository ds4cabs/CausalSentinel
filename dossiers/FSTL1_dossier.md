# Protein Dossier — FSTL1 (Follistatin-related protein 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: vitiligo | 1.15 | 0.242 | 1.95e-06 | Wald ratio | 1 | cis | NA |
| Hearing difficulty or problems: Yes | 0.0533 | 0.0192 | 0.00561 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: depression | 0.119 | 0.0431 | 0.00585 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: J33 Nasal polyp | 0.299 | 0.129 | 0.0204 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N40 Hyperplasia of prostate | 0.228 | 0.0985 | 0.0207 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: vaginal prolapse or uterine prolapse | 0.271 | 0.124 | 0.0287 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K40 Inguinal hernia | 0.133 | 0.0632 | 0.0347 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: anxiety or panic attacks | 0.18 | 0.0854 | 0.0353 | Wald ratio | 1 | cis | NA |
| Creatinine (enzymatic) in urine | 0.0232 | 0.0113 | 0.0388 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: osteoarthritis | -0.0848 | 0.0429 | 0.0481 | Wald ratio | 1 | cis | NA |
| Sleep duration | -0.0179 | 0.00918 | 0.051 | Wald ratio | 1 | cis | NA |
| Fracture resulting from simple fall | -0.0616 | 0.0329 | 0.0613 | Wald ratio | 1 | cis | NA |
| _...and 61 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_16 association rows across 12 traits (13 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Bone mineral density mean | 1e-300 | rs76311806 | 2 | GCST90321120 | no MR -> candidate analysis |
| Follistatin-related protein 1 levels | 4e-114 | rs1147707 | 2 | GCST90247638 | no MR -> candidate analysis |
| FSTL1 protein levels | 4e-102 | rs1147707 | 2 | GCST90469271 | no MR -> candidate analysis |
| Serum levels of protein FSTL1 | 1e-61 | rs1147707 | 1 | GCST90087381 | no MR -> candidate analysis |
| Blood protein levels | 1e-26 | rs1147707 | 1 | GCST006585 | no MR -> candidate analysis |
| Height | 1e-17 | rs1262395 | 2 | GCST90245848 | no MR -> candidate analysis |
| Follistatin-related protein 1 levels (FSTL1.13112.179.3) | 1e-16 | rs1147707 | 1 | GCST90241195 | no MR -> candidate analysis |
| Cerebrospinal fluid protein FSTL1 levels | 1e-14 | rs1147712 | 1 | GCST90943394 | no MR -> candidate analysis |
| Height (baseline) | 1e-8 | rs13088020 | 1 | GCST90565843 | no MR -> candidate analysis |
| Symptomatic menopause (PheCode 627.2) | 5e-8 | rs75745060 | 1 | GCST90651694 | no MR -> candidate analysis |
| FSTL1 protein level (protein group normalized intensity) | 5e-7 | rs1147707 | 1 | GCST90570985 | no MR -> candidate analysis |
| Drusen | 2e-6 | rs56100867 | 1 | GCST90104237 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 3088 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| immune system disorder | 0.468 | — | common-variant locus | no MR -> candidate analysis |

> Of the 1 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.00075, LOEUF=0.735 — LoF-tolerant |
| GWAS Catalog | 21 unique SNPs / 42 rows |
| ClinVar | 90 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 3088 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'FSTL1'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 90 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 12 of 12 traits by best p-value, aggregated from 16 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q12841 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000163430/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/FSTL1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/FSTL1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=FSTL1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/FSTL1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:43:33  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
