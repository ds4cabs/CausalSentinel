# Protein Dossier — LANCL1 (Glutathione S-transferase LANCL1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Cancer code  self-reported: prostate cancer | 0.471 | 0.149 | 0.00156 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: G47 Sleep disorders | 0.469 | 0.167 | 0.005 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Injury or trauma resulting in loss of vision | 0.435 | 0.175 | 0.0131 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K29 Gastritis and duodenitis | 0.226 | 0.104 | 0.0295 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Cataract | 0.188 | 0.0917 | 0.0408 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: asthma | 0.1 | 0.0504 | 0.0473 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: kidney stone or ureter stone or bladder stone | 0.327 | 0.167 | 0.0498 | Wald ratio | 1 | cis | NA |
| Potassium in urine | 0.0386 | 0.0201 | 0.0554 | Wald ratio | 1 | cis | NA |
| ER-negative Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.204 | 0.107 | 0.056 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: H25 Senile cataract | 0.323 | 0.169 | 0.0566 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I83 Varicose veins of lower extremities | -0.412 | 0.222 | 0.063 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | -0.0297 | 0.0162 | 0.0672 | Wald ratio | 1 | cis | NA |
| _...and 43 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_23 association rows across 19 traits (20 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Glycine levels | 4e-35 | rs62202072 | 4 | GCST90503747 | no MR -> candidate analysis |
| Creatinine levels | 1e-12 | rs79675564 | 1 | GCST90019502 | no MR -> candidate analysis |
| Estimated glomerular filtration rate | 2e-12 | rs79675564 | 1 | GCST90019506 | no MR -> candidate analysis |
| Contracture of joint (PheCode 739) | 8e-12 | rs572240213 | 1 | GCST90480542 | no MR -> candidate analysis |
| CRYGD protein levels | 1e-11 | rs185471906 | 1 | GCST90468876 | no MR -> candidate analysis |
| Citrulline levels | 1e-10 | rs3732055 | 1 | GCST90200403 | no MR -> candidate analysis |
| Gamma-glutamylcitrulline levels | 1e-10 | rs3732055 | 1 | GCST90200185 | no MR -> candidate analysis |
| Age when finished full-time education (standard GWA) | 7e-10 | rs1585241 | 1 | GCST90267280 | no MR -> candidate analysis |
| Adult body size | 3e-9 | rs79675564 | 1 | GCST010988 | no MR -> candidate analysis |
| Educational attainment | 4e-9 | rs3900166 | 2 | GCST90105038 | no MR -> candidate analysis |
| Phospholipid levels in HDL | 8e-9 | rs754778318 | 1 | GCST90092827 | no MR -> candidate analysis |
| Total lipid levels in HDL | 9e-9 | rs754778318 | 1 | GCST90092825 | no MR -> candidate analysis |
| _...and 7 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 168 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Abnormality of the skeletal system | 0.513 | — | common-variant locus | no MR -> candidate analysis |
| Pain | 0.436 | — | common-variant locus | MR: beta=0.0769, p=0.352 (cis) |
| contracture | 0.425 | — | common-variant locus | no MR -> candidate analysis |
| placental abruption | 0.425 | — | common-variant locus | no MR -> candidate analysis |
| squamous cell carcinoma | 0.11 | — | common-variant locus | no MR -> candidate analysis |
| adverse effect | 0.11 | — | common-variant locus | no MR -> candidate analysis |
| response to stimulus | 0.11 | — | common-variant locus | no MR -> candidate analysis |

> Of the 7 rows above, **6 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Glutathione S-transferase LANCL1) |
| gnomAD constraint | pLI=2.5e-17, LOEUF=1.25 — LoF-tolerant |
| GWAS Catalog | 57 unique SNPs / 114 rows |
| ClinVar | 109 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 168 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'LANCL1' and resolved to 'Glutathione S-transferase LANCL1' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 109 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 19 of 19 traits by best p-value, aggregated from 23 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O43813 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000115365/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL6066415/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/LANCL1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/LANCL1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=LANCL1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/LANCL1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:27:47  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
