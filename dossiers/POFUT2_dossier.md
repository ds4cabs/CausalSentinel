# Protein Dossier — POFUT2 (GDP-fucose protein O-fucosyltransferase 2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: K80 Cholelithiasis | 0.0825 | 0.0264 | 0.00179 | Wald ratio | 1 | trans | NA |
| Body mass index (BMI) | 0.0128 | 0.00412 | 0.00196 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: I80 Phlebitis and thrombophlebitis | 0.134 | 0.0529 | 0.011 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | 0.107 | 0.0442 | 0.0155 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: R04 Haemorrhage from respiratory passages | 0.107 | 0.0516 | 0.0374 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: osteoarthritis | -0.029 | 0.0142 | 0.0413 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: L03 Cellulitis | 0.0847 | 0.0422 | 0.0446 | Wald ratio | 1 | trans | NA |
| Pulse rate | 0.0145 | 0.00727 | 0.0459 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: M72 Fibroblastic disorders | 0.0982 | 0.0509 | 0.0539 | Wald ratio | 1 | trans | NA |
| Eye problems or disorders: Diabetes related eye disease | 0.0927 | 0.0482 | 0.0543 | Wald ratio | 1 | trans | NA |
| Fracture resulting from simple fall | 0.0205 | 0.0106 | 0.0544 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: iron deficiency anaemia | -0.122 | 0.0641 | 0.0574 | Wald ratio | 1 | trans | NA |
| _...and 53 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_2 association rows across 2 traits (0 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Suicide attempt severity in mood disorders | 2e-6 | rs74961332 | 1 | GCST012279 | no MR -> candidate analysis |
| Coronary artery calcified atherosclerotic plaque (90 or 130  | 8e-6 | rs4819052 | 1 | GCST005175 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 163 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| cataract | 0.501 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.308 | — | common-variant locus | no MR -> candidate analysis |
| metabolic syndrome | 0.134 | — | common-variant locus | no MR -> candidate analysis |
| major depressive disorder | 0.125 | — | common-variant locus | no MR -> candidate analysis |
| type 2 diabetes mellitus | 0.117 | — | common-variant locus | no MR -> candidate analysis |
| attention deficit-hyperactivity disorder | 0.117 | — | common-variant locus | no MR -> candidate analysis |

> Of the 6 rows above, **6 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=4.5e-05, LOEUF=0.74 — LoF-tolerant |
| GWAS Catalog | 36 unique SNPs / 72 rows |
| ClinVar | 190 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 163 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'POFUT2'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 190 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 2 of 2 traits by best p-value, aggregated from 2 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9Y2G5 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000186866/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/POFUT2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/POFUT2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=POFUT2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/POFUT2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:29:26  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
