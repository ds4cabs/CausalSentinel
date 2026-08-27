# Protein Dossier — AHSG (Alpha-2-HS-glycoprotein)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: diverticular disease or diverticulitis | 0.102 | 0.0367 | 0.00566 | Wald ratio | 1 | cis | NA |
| Endometrioid ovarian cancer | 0.121 | 0.0524 | 0.0207 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | -0.135 | 0.0588 | 0.0213 | Wald ratio | 1 | cis | NA |
| Paget's disease | 0.259 | 0.117 | 0.0269 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: ankylosing spondylitis | -0.228 | 0.103 | 0.0274 | Wald ratio | 1 | cis | NA |
| Lumbar spine bone mineral density | 0.0345 | 0.0158 | 0.0294 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: bladder problem (not cancer) | 0.11 | 0.0506 | 0.0296 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Ankle | 0.0735 | 0.0341 | 0.0313 | Wald ratio | 1 | cis | NA |
| Fractured or broken bones in last 5 years | 0.0277 | 0.013 | 0.0336 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypopituitarism | 0.35 | 0.17 | 0.04 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code self-reported: pulmonary embolism (with or without) dvt | 0.0896 | 0.0436 | 0.0401 | Wald ratio | 1 | cis | NA |
| Type 2 diabetes | 0.0627 | 0.0314 | 0.0457 | Wald ratio | 1 | cis | NA |
| _...and 94 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3581_53_3` | a2-HS-Glycoprotein | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_117 association rows across 95 traits (114 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Alpha-2-HS-glycoprotein (analyte X10966.1) levels | 5e-1417 | rs4917 | 1 | GCST90421283 | no MR -> candidate analysis |
| AHSG protein levels | 2e-211 | rs140827890 | 7 | GCST90468263 | no MR -> candidate analysis |
| Alpha-2-HS-glycoprotein level in Chronic kidney disease with | 3e-197 | rs4917 | 1 | GCST90233040 | no MR -> candidate analysis |
| Circulating ENTPD5 levels | 3e-144 | rs35457250 | 1 | GCST90860373 | no MR -> candidate analysis |
| ENTPD5 protein levels | 6e-118 | rs35457250 | 1 | GCST90469121 | no MR -> candidate analysis |
| Serum calciprotein particle maturation time (T50) | 2e-101 | rs4917 | 1 | GCST90102513 | no MR -> candidate analysis |
| PINLYP protein levels | 3e-90 | rs35457250 | 1 | GCST90470238 | no MR -> candidate analysis |
| PDZK1 protein levels | 3e-78 | rs1900618 | 2 | GCST90470203 | no MR -> candidate analysis |
| Glycoprotein acetyls levels | 4e-77 | rs4918 | 4 | GCST90501111 | no MR -> candidate analysis |
| Protein FAM210A protein levels (SomaScan ID:10966-1) | 3e-75 | rs4917 | 1 | GCST90442358 | no MR -> candidate analysis |
| PXK protein levels | 2e-71 | rs4918 | 1 | GCST90453317 | no MR -> candidate analysis |
| VWA1 protein levels | 2e-58 | rs35457250 | 1 | GCST90471061 | no MR -> candidate analysis |
| _...and 83 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1892 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Alopecia-intellectual disability syndrome | 0.561 | — | established (curated) | no MR -> candidate analysis |
| otosclerosis | 0.718 | — | common-variant locus | no MR -> candidate analysis |
| alopecia - intellectual disability syndrome | 0.608 | — | established (curated) | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Alpha-2-HS-glycoprotein) |
| gnomAD constraint | pLI=8.5e-07, LOEUF=1.08 — LoF-tolerant |
| GWAS Catalog | 179 unique SNPs / 458 rows |
| ClinVar | 123 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1892 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'AHSG' and resolved to 'Alpha-2-HS-glycoprotein' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 123 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 95 traits by best p-value, aggregated from 117 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P02765 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000145192/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4295694/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/AHSG — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/AHSG — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=AHSG%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/AHSG — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T00:59:00  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
