# Protein Dossier — ICOSLG (ICOS ligand)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Rheumatoid arthritis | 0.145 | 0.0289 | 5.44e-07 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: polio  or  poliomyelitis | 0.423 | 0.12 | 4.29e-04 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R14 Flatulence and related conditions | 0.423 | 0.131 | 0.00123 | Wald ratio | 1 | cis | NA |
| Crohn's disease | 0.0705 | 0.0241 | 0.00336 | Wald ratio | 1 | cis | NA |
| Thyroid cancer | -0.393 | 0.153 | 0.0101 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: pernicious anaemia | 0.183 | 0.0728 | 0.012 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: vitiligo | 0.466 | 0.187 | 0.0125 | Wald ratio | 1 | cis | NA |
| Eczema | -0.0855 | 0.0343 | 0.0127 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: gout | 0.0901 | 0.0362 | 0.0127 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: emphysema or chronic bronchitis | 0.0886 | 0.0374 | 0.0178 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | 0.0109 | 0.00471 | 0.0205 | Wald ratio | 1 | cis | NA |
| Height | 0.0134 | 0.0059 | 0.0235 | Wald ratio | 1 | cis | NA |
| _...and 107 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-5061_27_3` | B7-H2 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_47 association rows across 26 traits (43 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating ICOSLG levels (id: OID00731_OID21351) | 4e-677 | rs4819388 | 3 | GCST90860072 | no MR -> candidate analysis |
| Circulating ICOSLG levels (id: OID00828_OID21351) | 7e-667 | rs4819388 | 3 | GCST90860156 | no MR -> candidate analysis |
| Blood protein levels | 6e-194 | rs11558819 | 2 | GCST006585 | no MR -> candidate analysis |
| ICOS ligand levels (ICOSLG.9303.9.3) | 4e-108 | rs11558819 | 1 | GCST90241463 | no MR -> candidate analysis |
| ICOSLG protein levels | 1e-58 | rs11558819 | 4 | GCST90453026 | no MR -> candidate analysis |
| Eosinophil count | 2e-36 | rs2847224 | 6 | GCST90002302 | no MR -> candidate analysis |
| Eosinophill percentage (UKB data field 30210) | 1e-31 | rs2847224 | 1 | GCST90468069 | no MR -> candidate analysis |
| eosinophil (fraction, mean, inv-norm transformed) | 2e-28 | rs2847224 | 2 | GCST90475300 | no MR -> candidate analysis |
| Eosinophil percentage of white cells | 9e-28 | rs2847224 | 2 | GCST90002382 | no MR -> candidate analysis |
| Eosinophill count (UKB data field 30150) | 6e-26 | rs2847224 | 1 | GCST90468068 | no MR -> candidate analysis |
| eosinophil (fraction, maximum, inv-norm transformed) | 1e-23 | rs2847224 | 2 | GCST90475297 | no MR -> candidate analysis |
| eosinophil (absolute count, mean, inv-norm transformed) | 4e-22 | rs2847224 | 2 | GCST90475291 | no MR -> candidate analysis |
| _...and 14 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 333 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| immunodeficiency 119 | 0.547 | — | established (curated) | no MR -> candidate analysis |
| combined immunodeficiency | 0.438 | — | established (curated) | no MR -> candidate analysis |
| rheumatoid arthritis | 0.428 | — | common-variant locus | MR: beta=0.145, p=5.44e-07 (cis) |
| Combined T and B cell immunodeficiency | 0.438 | — | established (curated) | no MR -> candidate analysis |
| hereditary disease | 0.438 | — | established (curated) | no MR -> candidate analysis |
| depressive disorder | 0.315 | — | common-variant locus | no MR -> candidate analysis |
| cardiomyopathy | 0.241 | — | common-variant locus | no MR -> candidate analysis |
| benign urinary system neoplasm | 0.241 | — | common-variant locus | no MR -> candidate analysis |
| type 1 diabetes mellitus | 0.176 | — | common-variant locus | no MR -> candidate analysis |

> Of the 9 rows above, **8 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 1 known modulators (ICOS ligand) |
| gnomAD constraint | pLI=NA, LOEUF=NA — Constraint metrics missing; LoF tolerance cannot be judged. |
| GWAS Catalog | 85 unique SNPs / 170 rows |
| ClinVar | 429 records; 3 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 333 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'ICOSLG' and resolved to 'ICOS ligand' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 429 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 26 traits by best p-value, aggregated from 47 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O75144 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000160223/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3712949/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/ICOSLG — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/ICOSLG — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=ICOSLG%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/ICOSLG — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:05:13  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
