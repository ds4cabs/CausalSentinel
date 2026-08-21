# Protein Dossier — VCAM1 (Vascular cell adhesion protein 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | 0.74 | 0.0273 | 1.92e-161 | Wald ratio | 1 | trans | 0.997 |
| Diastolic blood pressure  automated reading | 0.205 | 0.0132 | 1.66e-54 | Wald ratio | 1 | trans | 0.994 |
| Non-cancer illness code  self-reported: hypertension | 0.214 | 0.0177 | 1.53e-33 | Wald ratio | 1 | trans | 0.994 |
| Platelet count | 21.9 | 2.21 | 3.64e-23 | Wald ratio | 1 | trans | 0.997 |
| Haemoglobin concentration | 0.273 | 0.0306 | 3.64e-19 | Wald ratio | 1 | trans | NA |
| Systolic blood pressure  automated reading | 0.115 | 0.0132 | 2.52e-18 | Wald ratio | 1 | trans | 0.993 |
| Total cholesterol | -0.171 | 0.0198 | 8.36e-18 | Wald ratio | 1 | trans | 0.998 |
| Packed cell volume | 0.779 | 0.0949 | 2.34e-16 | Wald ratio | 1 | trans | NA |
| Red blood cell count | 0.0858 | 0.0118 | 3.52e-13 | Wald ratio | 1 | trans | NA |
| HDL cholesterol | -0.138 | 0.0193 | 7.68e-13 | Wald ratio | 1 | trans | 0.997 |
| LDL cholesterol | -0.144 | 0.0204 | 1.76e-12 | Wald ratio | 1 | trans | 0.997 |
| Non-cancer illness code  self-reported: psoriasis | 0.501 | 0.074 | 1.36e-11 | Wald ratio | 1 | trans | 0.992 |
| _...and 130 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2967_8_1` | VCAM-1 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_63 association rows across 39 traits (57 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Hematological traits (multi-trait analysis) | 2e-78 | rs6684679 | 2 | GCST90838669 | no MR -> candidate analysis |
| Lymphocyte count (UKB data field 30120) | 5e-49 | rs2148404 | 2 | GCST90468082 | no MR -> candidate analysis |
| Circulating VCAM1 levels | 1e-42 | rs139561173 | 2 | GCST90860455 | no MR -> candidate analysis |
| VCAM1 protein levels | 7e-39 | rs12240047 | 2 | GCST90471031 | no MR -> candidate analysis |
| Lymphocyte count | 1e-38 | rs12088882 | 4 | GCST90085815 | no MR -> candidate analysis |
| Platelet-to-lymphocyte ratio | 1e-35 | rs12047102 | 1 | GCST90056184 | no MR -> candidate analysis |
| monocyte (absolute count, mean, inv-norm transformed) | 1e-31 | rs78453488 | 1 | GCST90475502 | no MR -> candidate analysis |
| Monocyte count | 3e-30 | rs71660930 | 3 | GCST90002393 | no MR -> candidate analysis |
| lymphocyte (absolute count, maximum, inv-norm transformed) | 1e-29 | rs1409425 | 1 | GCST90479663 | no MR -> candidate analysis |
| lymphocyte (absolute count, mean, inv-norm transformed) | 2e-28 | rs11166512 | 1 | GCST90479664 | no MR -> candidate analysis |
| Monocyte count (UKB data field 30130) | 7e-26 | rs71660930 | 1 | GCST90468090 | no MR -> candidate analysis |
| Lymphocyte percentage (UKB data field 30180) | 6e-24 | rs10875333 | 1 | GCST90468083 | no MR -> candidate analysis |
| _...and 27 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1289 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| open-angle glaucoma | 0.55 | — | common-variant locus | no MR -> candidate analysis |
| glaucoma | 0.459 | — | common-variant locus | MR: beta=-0.231, p=0.0954 (trans) |
| Crohn disease | 0.346 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Vascular cell adhesion protein 1) |
| gnomAD constraint | pLI=5e-09, LOEUF=0.833 — LoF-tolerant |
| GWAS Catalog | 55 unique SNPs / 110 rows |
| ClinVar | 114 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1289 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'VCAM1' and resolved to 'Vascular cell adhesion protein 1' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 114 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 39 traits by best p-value, aggregated from 63 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P19320 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000162692/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3735/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/VCAM1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/VCAM1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=VCAM1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/VCAM1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:34:40  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
