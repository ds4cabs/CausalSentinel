# Protein Dossier — GALP (Galanin-like peptide)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: osteoarthritis | -0.161 | 0.061 | 0.00839 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: depression | 0.119 | 0.0567 | 0.0358 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: diverticular disease or diverticulitis | 0.243 | 0.116 | 0.0367 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | 0.284 | 0.142 | 0.0457 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Injury or trauma resulting in loss of vision | 0.291 | 0.154 | 0.0589 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: high cholesterol | -0.0862 | 0.0456 | 0.0589 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: C50 Malignant neoplasm of breast | 0.18 | 0.102 | 0.0784 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: prostate cancer | 0.246 | 0.145 | 0.0901 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: G56 Mononeuropathies of upper limb | -0.25 | 0.155 | 0.108 | Wald ratio | 1 | cis | NA |
| Invasive mucinous ovarian cancer | 0.424 | 0.266 | 0.112 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Glaucoma | -0.279 | 0.176 | 0.113 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: emphysema or chronic bronchitis | -0.291 | 0.187 | 0.119 | Wald ratio | 1 | cis | NA |
| _...and 46 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_6 association rows across 6 traits (4 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| GLIPR1 protein levels | 9e-28 | rs538412728 | 1 | GCST90469357 | no MR -> candidate analysis |
| Bone mineral density mean | 5e-13 | rs117735362 | 1 | GCST90321120 | no MR -> candidate analysis |
| Galanin-like peptide levels (GALP.9398.30.3) | 1e-12 | rs111265125 | 1 | GCST90241219 | no MR -> candidate analysis |
| Total protein levels x insomnia interaction | 8e-9 | rs73617540 | 1 | GCST90026658 | no MR -> candidate analysis |
| COPD severity (based on Global Initiative for Chronic Obstru | 3e-6 | rs274165 | 1 | GCST90827700 | no MR -> candidate analysis |
| Microalbuminuria | 5e-6 | rs274173 | 1 | GCST003253 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 87 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| insomnia | 0.231 | — | common-variant locus | no MR -> candidate analysis |

> Of the 1 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (UDP-galactopyranose mutase) |
| gnomAD constraint | pLI=0.00034, LOEUF=1.28 — LoF-tolerant |
| GWAS Catalog | 49 unique SNPs / 98 rows |
| ClinVar | 57 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 87 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'GALP' and resolved to 'UDP-galactopyranose mutase' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 57 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 6 of 6 traits by best p-value, aggregated from 6 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9UBC7 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000197487/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4450/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/GALP — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/GALP — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=GALP%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/GALP — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:46:54  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
