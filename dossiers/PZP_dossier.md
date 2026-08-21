# Protein Dossier — PZP (Pregnancy zone protein)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: R55 Syncope and collapse | 0.128 | 0.0497 | 0.00997 | Wald ratio | 1 | cis | NA |
| Iron | 0.0526 | 0.0216 | 0.0149 | Wald ratio | 1 | cis | NA |
| Transferrin Saturation | 0.0506 | 0.0216 | 0.0192 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N81 Female genital prolapse | 0.0943 | 0.0405 | 0.0198 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | 0.00899 | 0.00436 | 0.0392 | Wald ratio | 1 | cis | NA |
| Alcohol intake frequency | -0.016 | 0.00786 | 0.0413 | Wald ratio | 1 | cis | NA |
| Hippocampus volume | 19.2 | 10 | 0.0555 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | 0.0087 | 0.0046 | 0.0586 | Wald ratio | 1 | cis | NA |
| HDL cholesterol | 0.0196 | 0.0106 | 0.0644 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: vaginal prolapse or uterine prolapse | 0.117 | 0.0643 | 0.0679 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M23 Internal derangement of knee | 0.0603 | 0.0337 | 0.0734 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: prostate cancer | 0.0997 | 0.0565 | 0.0775 | Wald ratio | 1 | cis | NA |
| _...and 100 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_25 association rows across 18 traits (22 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Serum levels of protein PZP | 7e-239 | rs2277413 | 2 | GCST90089510 | no MR -> candidate analysis |
| Pregnancy zone protein levels | 3e-163 | rs3741849 | 2 | GCST90249199 | no MR -> candidate analysis |
| Blood protein levels | 3e-135 | rs7311982 | 2 | GCST006585 | no MR -> candidate analysis |
| Serum levels of protein NUDT16L1 | 4e-107 | rs2277413 | 1 | GCST90087025 | no MR -> candidate analysis |
| Refractive error | 1e-40 | rs10842971 | 1 | GCST010002 | no MR -> candidate analysis |
| Protein syndesmos levels (NUDT16L1.12497.29.3) | 3e-37 | rs2277413 | 1 | GCST90242520 | no MR -> candidate analysis |
| PZP protein levels | 4e-26 | rs16918159 | 5 | GCST90453199 | no MR -> candidate analysis |
| Primary angle-closure glaucoma (MTAG) | 6e-17 | rs10842970 | 1 | GCST90832185 | no MR -> candidate analysis |
| HYAL1 protein levels | 1e-15 | rs2277413 | 1 | GCST90469495 | no MR -> candidate analysis |
| Spherical equivalent or myopia (age of diagnosis) | 4e-12 | rs7968679 | 1 | GCST006291 | no MR -> candidate analysis |
| Myopia | 4e-12 | rs7968679 | 1 | GCST003997 | no MR -> candidate analysis |
| CCN5 protein levels | 7e-12 | rs2277413 | 1 | GCST90468591 | no MR -> candidate analysis |
| _...and 6 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 155 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| myopia | 0.416 | — | common-variant locus | no MR -> candidate analysis |
| refractive error | 0.387 | — | common-variant locus | no MR -> candidate analysis |
| primary angle-closure glaucoma | 0.369 | — | common-variant locus | no MR -> candidate analysis |
| Abnormality of refraction | 0.288 | — | common-variant locus | no MR -> candidate analysis |
| musculoskeletal system disorder | 0.266 | — | common-variant locus | no MR -> candidate analysis |
| upper respiratory tract disorder | 0.207 | — | common-variant locus | no MR -> candidate analysis |
| Aganglionic megacolon | 0.195 | — | established (curated) | no MR -> candidate analysis |
| hypertension, pregnancy-induced | 0.188 | — | common-variant locus | no MR -> candidate analysis |
| adolescent idiopathic scoliosis | 0.184 | — | common-variant locus | no MR -> candidate analysis |

> Of the 9 rows above, **9 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 1 known modulators (Alpha-2-macroglobulin) |
| gnomAD constraint | pLI=4.9e-42, LOEUF=0.956 — LoF-tolerant |
| GWAS Catalog | 78 unique SNPs / 153 rows |
| ClinVar | 267 records; 4 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 155 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'PZP' and resolved to 'Alpha-2-macroglobulin' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 267 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 18 of 18 traits by best p-value, aggregated from 25 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P20742 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000126838/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4295690/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PZP — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PZP — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PZP%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/PZP — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:43:23  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
