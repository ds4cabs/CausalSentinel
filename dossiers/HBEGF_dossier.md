# Protein Dossier — HBEGF (Proheparin-binding EGF-like growth factor)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Mean platelet volume | -0.0759 | 0.00592 | 1.30e-37 | Wald ratio | 1 | trans | NA |
| Platelet count | 20.4 | 2.17 | 4.86e-21 | Wald ratio | 1 | trans | 0.991 |
| Triglycerides | -0.152 | 0.0253 | 1.73e-09 | Wald ratio | 1 | trans | 0.85 |
| HDL cholesterol | 0.125 | 0.0258 | 1.21e-06 | Wald ratio | 1 | trans | NA |
| Years of schooling | 0.0861 | 0.0215 | 6.33e-05 | Wald ratio | 1 | trans | NA |
| Height | 0.0522 | 0.0161 | 0.00122 | Wald ratio | 1 | trans | NA |
| Childhood intelligence | 0.217 | 0.07 | 0.00189 | Wald ratio | 1 | trans | NA |
| Total cholesterol | 0.0856 | 0.028 | 0.00223 | Wald ratio | 1 | trans | NA |
| LDL cholesterol | 0.085 | 0.0285 | 0.00287 | Wald ratio | 1 | trans | NA |
| Fasting proinsulin | -0.108 | 0.0371 | 0.00375 | Wald ratio | 1 | trans | NA |
| ER-positive Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.114 | 0.0409 | 0.00528 | Wald ratio | 1 | trans | NA |
| Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.0834 | 0.0339 | 0.0139 | Wald ratio | 1 | trans | NA |
| _...and 42 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-4134_4_2` | HB-EGF | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_139 association rows across 89 traits (128 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| IDP dMRI TBSS ICVF Genu of corpus callosum | 4e-39 | rs4150197 | 1 | GCST90004329 | no MR -> candidate analysis |
| IDP dMRI TBSS ICVF Body of corpus callosum | 3e-34 | rs3776089 | 1 | GCST90004330 | no MR -> candidate analysis |
| IDP dMRI TBSS ICVF Splenium of corpus callosum | 2e-32 | rs4150197 | 1 | GCST90004331 | no MR -> candidate analysis |
| HBEGF/PDGFA protein level ratio | 9e-32 | rs2237077 | 1 | GCST90315033 | no MR -> candidate analysis |
| White matter microstructure (fractional anisotropy) | 4e-31 | rs3776089 | 12 | GCST009539 | no MR -> candidate analysis |
| White matter microstructure (radial diusivities) | 2e-27 | rs3776089 | 12 | GCST009540 | no MR -> candidate analysis |
| Circulating DLK1 levels | 4e-27 | rs2282802 | 1 | GCST90859946 | no MR -> candidate analysis |
| Corpus callosum fractional anisotropy (MOSTest) | 1e-26 | rs4150197 | 1 | GCST90281340 | no MR -> candidate analysis |
| IDP dMRI TBSS FA Splenium of corpus callosum | 2e-24 | rs3776089 | 1 | GCST90003881 | no MR -> candidate analysis |
| Corpus callosum fractional anisotropy (splenium) | 2e-23 | rs4150197 | 1 | GCST90281343 | no MR -> candidate analysis |
| IDP dMRI TBSS L2 Splenium of corpus callosum | 9e-23 | rs3776089 | 1 | GCST90004127 | no MR -> candidate analysis |
| IDP dMRI ProbtrackX ICVF fmi | 2e-22 | rs3776089 | 1 | GCST90004386 | no MR -> candidate analysis |
| _...and 77 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1413 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| atrial fibrillation | 0.646 | — | common-variant locus | no MR -> candidate analysis |
| Abnormality of the skeletal system | 0.573 | — | common-variant locus | no MR -> candidate analysis |
| vein disorder | 0.421 | — | common-variant locus | no MR -> candidate analysis |
| Varicose veins | 0.421 | — | common-variant locus | no MR -> candidate analysis |
| lymphatic system disorder | 0.421 | — | common-variant locus | no MR -> candidate analysis |
| Alzheimer disease | 0.349 | — | common-variant locus | no MR -> candidate analysis |
| obesity disorder | 0.283 | — | common-variant locus | no MR -> candidate analysis |

> Of the 7 rows above, **7 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 1 known modulators (Proheparin-binding EGF-like growth factor) |
| gnomAD constraint | pLI=0.32, LOEUF=0.741 — LoF-tolerant |
| GWAS Catalog | 60 unique SNPs / 120 rows |
| ClinVar | 36 records; 6 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1413 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'HBEGF' and resolved to 'Proheparin-binding EGF-like growth factor' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 36 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 89 traits by best p-value, aggregated from 139 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q99075 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000113070/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3286070/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/HBEGF — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/HBEGF — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=HBEGF%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/HBEGF — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:58:40  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
