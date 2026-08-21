# Protein Dossier — OXT (Oxytocin-neurophysin 1 proprotein)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Creatinine (enzymatic) in urine | -0.0133 | 0.00397 | 8.02e-04 | Wald ratio | 1 | cis | NA |
| Amyotrophic lateral sclerosis | -0.0861 | 0.0293 | 0.0033 | Wald ratio | 1 | cis | NA |
| Potassium in urine | -0.0119 | 0.00421 | 0.00458 | Wald ratio | 1 | cis | NA |
| Caudate volume | -26.2 | 9.58 | 0.00615 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: bladder problem (not cancer) | -0.144 | 0.0632 | 0.0229 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: muscle or soft tissue injuries | 0.0946 | 0.0447 | 0.0344 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I83 Varicose veins of lower extremities | 0.057 | 0.0274 | 0.0375 | Wald ratio | 1 | cis | NA |
| Pallidum volume | -7.39 | 3.58 | 0.0388 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: malignant melanoma | 0.0883 | 0.0432 | 0.041 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: G47 Sleep disorders | -0.121 | 0.0614 | 0.0487 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: kidney stone or ureter stone or bladder stone | -0.1 | 0.052 | 0.0541 | Wald ratio | 1 | cis | NA |
| Lumbar spine bone mineral density | 0.0273 | 0.0152 | 0.0715 | Wald ratio | 1 | cis | NA |
| _...and 74 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_18 association rows across 16 traits (15 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| CDHR2/OXT protein level ratio | 1e-688 | rs2740210 | 1 | GCST90313964 | no MR -> candidate analysis |
| EPHA1/OXT protein level ratio | 6e-648 | rs2740210 | 1 | GCST90314677 | no MR -> candidate analysis |
| MEGF9/OXT protein level ratio | 1e-634 | rs2740210 | 1 | GCST90315419 | no MR -> candidate analysis |
| Serum levels of protein OXT | 3e-241 | rs877172 | 1 | GCST90090149 | no MR -> candidate analysis |
| Blood protein levels | 6e-156 | rs877172 | 1 | GCST006585 | no MR -> candidate analysis |
| Oxytocin-neurophysin 1 levels | 2e-154 | rs877172 | 2 | GCST90248810 | no MR -> candidate analysis |
| OXT protein levels | 2e-121 | rs557663677 | 2 | GCST90470139 | no MR -> candidate analysis |
| ITPA protein levels | 4e-21 | rs2740210 | 1 | GCST90469654 | no MR -> candidate analysis |
| Oxytocin-neurophysin 1 level in Chronic kidney disease with  | 1e-20 | rs877172 | 1 | GCST90238907 | no MR -> candidate analysis |
| CPXM1 protein levels | 3e-12 | rs913554 | 1 | GCST90468849 | no MR -> candidate analysis |
| Estimated glomerular filtration rate (creatinine, cystatin c | 2e-10 | rs2740192 | 1 | GCST90428446 | no MR -> candidate analysis |
| Serum oxytocin levels | 3e-8 | rs12625893 | 1 | GCST009027 | no MR -> candidate analysis |
| _...and 4 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 857 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| neurodevelopmental disorder | 0.195 | — | established (curated) | no MR -> candidate analysis |

> Of the 1 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Oxytocin-neurophysin 1) |
| gnomAD constraint | pLI=0.0018, LOEUF=1.4 — LoF-tolerant |
| GWAS Catalog | 68 unique SNPs / 136 rows |
| ClinVar | 56 records; 7 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 857 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'OXT' and resolved to 'Oxytocin-neurophysin 1' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 56 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 16 of 16 traits by best p-value, aggregated from 18 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P01178 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000101405/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL5169107/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/OXT — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/OXT — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=OXT%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/OXT — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:10:43  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
