# Protein Dossier — TREML2 (Trem-like transcript 2 protein)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Weight | -0.0149 | 0.00449 | 9.08e-04 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | -0.0145 | 0.00508 | 0.00437 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: malignant melanoma | -0.189 | 0.0701 | 0.00694 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I83 Varicose veins of lower extremities | 0.0866 | 0.0326 | 0.00793 | Wald ratio | 1 | cis | NA |
| ER-negative Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.07 | 0.0264 | 0.00804 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M72 Fibroblastic disorders | 0.156 | 0.0594 | 0.00867 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: bladder problem (not cancer) | 0.145 | 0.0579 | 0.0126 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code self-reported: pulmonary embolism (with or without) dvt | -0.164 | 0.0668 | 0.0141 | Wald ratio | 1 | cis | NA |
| Creatinine (enzymatic) in urine | 0.0118 | 0.00487 | 0.0156 | Wald ratio | 1 | cis | NA |
| Potassium in urine | 0.0123 | 0.00516 | 0.0168 | Wald ratio | 1 | cis | NA |
| Clear cell ovarian cancer | -0.204 | 0.0894 | 0.0223 | Wald ratio | 1 | cis | NA |
| Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.0326 | 0.0144 | 0.0238 | Wald ratio | 1 | cis | NA |
| _...and 62 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_59 association rows across 37 traits (46 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Trem-like transcript 2 protein levels | 4e-897 | rs62396356 | 3 | GCST90249975 | no MR -> candidate analysis |
| Circulating TREML2 levels | 6e-566 | rs11759347 | 4 | GCST90859936 | no MR -> candidate analysis |
| PEAR1/TREML2 protein level ratio | 9e-403 | rs62396356 | 1 | GCST90315645 | no MR -> candidate analysis |
| CD244/TREML2 protein level ratio | 6e-402 | rs41273772 | 1 | GCST90313767 | no MR -> candidate analysis |
| SEMA4D/TREML2 protein level ratio | 5e-391 | rs62396356 | 1 | GCST90315823 | no MR -> candidate analysis |
| CD84/TREML2 protein level ratio | 3e-352 | rs62396356 | 1 | GCST90313919 | no MR -> candidate analysis |
| Blood protein levels | 2e-233 | rs13207171 | 1 | GCST006585 | no MR -> candidate analysis |
| Trem-like transcript 2 protein levels (TREML2.5736.1.3) | 5e-86 | rs61998254 | 1 | GCST90243113 | no MR -> candidate analysis |
| TREML2 protein levels | 7e-46 | rs62621763 | 4 | GCST90470962 | no MR -> candidate analysis |
| TREM2 protein levels | 3e-39 | rs9462674 | 1 | GCST90470960 | no MR -> candidate analysis |
| HBEGF/PDGFA protein level ratio | 3e-37 | rs62396356 | 1 | GCST90315033 | no MR -> candidate analysis |
| CCN2/HBEGF protein level ratio | 7e-31 | rs62396356 | 1 | GCST90313713 | no MR -> candidate analysis |
| _...and 25 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 78 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Alzheimer disease | 0.47 | — | common-variant locus | no MR -> candidate analysis |
| Lewy body dementia | 0.49 | — | common-variant locus | no MR -> candidate analysis |
| type 2 diabetes mellitus | 0.436 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=2.2e-08, LOEUF=1.3 — LoF-tolerant |
| GWAS Catalog | 77 unique SNPs / 154 rows |
| ClinVar | 66 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 78 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'TREML2'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 66 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 37 traits by best p-value, aggregated from 59 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q5T2D2 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000112195/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/TREML2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/TREML2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=TREML2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/TREML2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:29:36  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
