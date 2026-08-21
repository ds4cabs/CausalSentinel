# Protein Dossier — KLRC3 (NKG2-E type II integral membrane protein)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: hypopituitarism | 0.624 | 0.188 | 8.73e-04 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: osteoporosis | 0.106 | 0.0447 | 0.0173 | Wald ratio | 1 | trans | NA |
| Alcohol intake frequency | -0.0204 | 0.00915 | 0.0257 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: R35 Polyuria | -0.293 | 0.136 | 0.0309 | Wald ratio | 1 | trans | NA |
| Thalamus volume | 38 | 17.8 | 0.0325 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code self-reported: pulmonary embolism (with or without) dvt | -0.173 | 0.0822 | 0.0358 | Wald ratio | 1 | trans | NA |
| Hippocampus volume | 27.1 | 13.4 | 0.0424 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: uterine fibroids | -0.112 | 0.0561 | 0.0456 | Wald ratio | 1 | trans | NA |
| Endometrioid ovarian cancer | -0.16 | 0.0803 | 0.047 | Wald ratio | 1 | trans | NA |
| Lumbar spine bone mineral density | -0.0469 | 0.0237 | 0.0478 | Wald ratio | 1 | trans | NA |
| Weight | -0.0104 | 0.00546 | 0.0558 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: G47 Sleep disorders | -0.186 | 0.0984 | 0.0581 | Wald ratio | 1 | trans | NA |
| _...and 66 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_12 association rows across 12 traits (10 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| KLRK1 protein levels | 2e-27 | rs542584463 | 1 | GCST90469713 | no MR -> candidate analysis |
| monocyte (fraction, mean, inv-norm transformed) | 4e-21 | rs2682487 | 1 | GCST90479705 | no MR -> candidate analysis |
| Aspartate aminotransferase levels | 5e-18 | rs17513937 | 1 | GCST90011899 | no MR -> candidate analysis |
| platelet count (minimum, inv-norm transformed) | 2e-16 | rs2682487 | 1 | GCST90476302 | no MR -> candidate analysis |
| monocyte (fraction, maximum, inv-norm transformed) | 4e-15 | rs2682487 | 1 | GCST90479704 | no MR -> candidate analysis |
| monocyte (absolute count, maximum, inv-norm transformed) | 1e-14 | rs2859659 | 1 | GCST90479701 | no MR -> candidate analysis |
| Platelet count | 2e-14 | rs2859659 | 1 | GCST90002361 | no MR -> candidate analysis |
| Complex ventricular septal defect | 3e-11 | rs10734829 | 1 | GCST90246230 | no MR -> candidate analysis |
| Gamma glutamyl transferase levels | 3e-11 | rs17513937 | 1 | GCST90662899 | no MR -> candidate analysis |
| Mean corpuscular volume | 5e-9 | rs77926410 | 1 | GCST004602 | no MR -> candidate analysis |
| Neutrophil-to-lymphocyte ratio | 5e-8 | rs182561471 | 1 | GCST90866310 | no MR -> candidate analysis |
| Composite immunoglobulin trait (IgA/IgG) | 3e-6 | rs2682491 | 1 | GCST008572 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 92 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| ventricular septal defect | 0.44 | — | common-variant locus | no MR -> candidate analysis |
| psoriasis | 0.337 | — | common-variant locus | MR: beta=0.0629, p=0.252 (trans) |
| Behcet disease | 0.138 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.00018, LOEUF=1.03 — LoF-tolerant |
| GWAS Catalog | 85 unique SNPs / 170 rows |
| ClinVar | 86 records; 5 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 92 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'KLRC3'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 86 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 12 of 12 traits by best p-value, aggregated from 12 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q07444 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000205810/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/KLRC3 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/KLRC3 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=KLRC3%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/KLRC3 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:26:14  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
