# Protein Dossier — VSIR (V-type immunoglobulin domain-containing suppressor of T-cell activation)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Body fat | 0.0795 | 0.0274 | 0.00367 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: asthma | 0.0865 | 0.0324 | 0.00768 | Wald ratio | 1 | cis | NA |
| HOMA-B | 0.0444 | 0.017 | 0.00909 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: B37 Candidiasis | 0.784 | 0.306 | 0.0104 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | 0.035 | 0.0163 | 0.0322 | Wald ratio | 1 | cis | NA |
| Vascular or heart problems diagnosed by doctor: Angina | 0.133 | 0.0622 | 0.0328 | Wald ratio | 1 | cis | NA |
| HOMA-IR | 0.0444 | 0.0211 | 0.0353 | Wald ratio | 1 | cis | NA |
| Lumbar spine bone mineral density | -0.0936 | 0.0452 | 0.0386 | Wald ratio | 1 | cis | NA |
| Schizophrenia | -0.108 | 0.054 | 0.0448 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K35 Acute appendicitis | 0.277 | 0.141 | 0.0488 | Wald ratio | 1 | cis | NA |
| HDL cholesterol | 0.0481 | 0.0248 | 0.0523 | Wald ratio | 1 | cis | NA |
| Coronary heart disease | 0.0869 | 0.0467 | 0.0625 | Wald ratio | 1 | cis | NA |
| _...and 81 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_100 association rows across 52 traits (97 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| V-type immunoglobulin domain-containing suppressor of T-cell | 2e-559 | rs10762476 | 4 | GCST90250167 | no MR -> candidate analysis |
| DIABLO/VSIR protein level ratio | 1e-164 | rs9415041 | 1 | GCST90314470 | no MR -> candidate analysis |
| Circulating CXCL16 levels | 5e-88 | rs748113 | 1 | GCST90859949 | no MR -> candidate analysis |
| Lymphocyte count | 2e-65 | rs748113 | 6 | GCST90002316 | no MR -> candidate analysis |
| CXCL16 protein levels | 8e-65 | rs748113 | 1 | GCST90468928 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 7e-61 | rs748113 | 2 | GCST90838669 | no MR -> candidate analysis |
| Lymphocyte count (UKB data field 30120) | 8e-48 | rs748113 | 1 | GCST90468082 | no MR -> candidate analysis |
| White blood cell count | 2e-46 | rs3747869 | 13 | GCST90662906 | no MR -> candidate analysis |
| Platelet receptor Gi24 levels | 2e-36 | rs12415873 | 3 | GCST90161317 | no MR -> candidate analysis |
| white blood cell count (WBC, mean, inv-norm transformed) | 2e-27 | rs3747869 | 2 | GCST90476454 | no MR -> candidate analysis |
| Monocyte count | 6e-27 | rs7919533 | 8 | GCST90002344 | no MR -> candidate analysis |
| C-X-C motif chemokine 16 levels | 7e-26 | rs748113 | 2 | GCST90247204 | no MR -> candidate analysis |
| _...and 40 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 368 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| hypothyroidism | 0.494 | — | common-variant locus | MR: beta=-0.0631, p=0.293 (cis) |
| alcohol drinking | 0.47 | — | common-variant locus | no MR -> candidate analysis |
| ulcerative colitis | 0.195 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (V-type immunoglobulin domain-containing suppressor of T-cell activation) |
| gnomAD constraint | pLI=0.93, LOEUF=0.547 — LoF-INTOLERANT |
| GWAS Catalog | 88 unique SNPs / 176 rows |
| ClinVar | 48 records; 3 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 368 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'VSIR' and resolved to 'V-type immunoglobulin domain-containing suppressor of T-cell activation' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 48 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 52 traits by best p-value, aggregated from 100 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9H7M9 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000107738/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4523457/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/VSIR — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/VSIR — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=VSIR%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/VSIR — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:36:02  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
