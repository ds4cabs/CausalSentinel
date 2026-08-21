# Protein Dossier — B3GAT3 (Galactosylgalactosylxylosylprotein 3-beta-glucuronosyltransferase 3)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Forced expiratory volume in 1-second (FEV1) | -0.025 | 0.00509 | 9.36e-07 | Wald ratio | 1 | cis | NA |
| Thyroid cancer | -0.951 | 0.201 | 2.18e-06 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | -0.0214 | 0.00483 | 9.30e-06 | Wald ratio | 1 | cis | NA |
| Pulse rate | 0.0411 | 0.0104 | 7.58e-05 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: ankylosing spondylitis | 0.283 | 0.0845 | 8.04e-04 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | 0.0227 | 0.00762 | 0.00294 | Wald ratio | 1 | cis | NA |
| Height | -0.0206 | 0.00746 | 0.00582 | Wald ratio | 1 | cis | NA |
| ER-negative Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.0785 | 0.0301 | 0.00908 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: chronic obstructive airways disease or copd | 0.212 | 0.0822 | 0.00981 | Wald ratio | 1 | cis | NA |
| Diastolic blood pressure  automated reading | 0.0155 | 0.00603 | 0.0101 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: malignant melanoma | 0.137 | 0.0584 | 0.0189 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K44 Diaphragmatic hernia | 0.0944 | 0.043 | 0.028 | Wald ratio | 1 | cis | NA |
| _...and 81 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_9 association rows across 7 traits (9 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Apolipoprotein A-II levels | 6e-251 | rs12794886 | 2 | GCST90246542 | no MR -> candidate analysis |
| Galactosylgalactosylxylosylprotein 3-beta-glucuronosyltransf | 2e-149 | rs12794886 | 2 | GCST90247678 | no MR -> candidate analysis |
| Galactosylgalactosylxylosylprotein 3-beta-glucuronosyltransf | 8e-63 | rs12794886 | 1 | GCST90241217 | no MR -> candidate analysis |
| Impedance of arm right (UKB data field 23109) | 2e-17 | rs796771530 | 1 | GCST90468172 | no MR -> candidate analysis |
| Apolipoprotein A-II level in Chronic kidney disease with hyp | 5e-12 | rs7122950 | 1 | GCST90238491 | no MR -> candidate analysis |
| Appendicular lean mass | 8e-10 | rs7122950 | 1 | GCST90000025 | no MR -> candidate analysis |
| Triglyceride to phosphoglyceride ratio | 3e-8 | rs796771530 | 1 | GCST90454483 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 367 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Larsen-like syndrome, B3GAT3 type | 0.887 | — | established (curated) | no MR -> candidate analysis |
| Abnormality of the skeletal system | 0.48 | — | common-variant locus | no MR -> candidate analysis |
| hereditary disease | 0.316 | — | established (curated) | no MR -> candidate analysis |
| irritable bowel syndrome | 0.173 | — | common-variant locus | no MR -> candidate analysis |

> Of the 4 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Galactosylgalactosylxylosylprotein 3-beta-glucuronosyltransferase 3) |
| gnomAD constraint | pLI=0.00057, LOEUF=0.842 — LoF-tolerant |
| GWAS Catalog | 85 unique SNPs / 170 rows |
| ClinVar | 325 records; 4 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 367 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'B3GAT3' and resolved to 'Galactosylgalactosylxylosylprotein 3-beta-glucuronosyltransferase 3' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 325 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 7 of 7 traits by best p-value, aggregated from 9 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O94766 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000149541/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3958/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/B3GAT3 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/B3GAT3 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=B3GAT3%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/B3GAT3 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:14:11  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
