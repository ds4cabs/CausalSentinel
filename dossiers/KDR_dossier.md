# Protein Dossier — KDR (Vascular endothelial growth factor receptor 2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: R07 Pain in throat and chest | 0.0564 | 0.0245 | 0.0213 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R14 Flatulence and related conditions | 0.368 | 0.173 | 0.0332 | Wald ratio | 1 | cis | NA |
| Potassium in urine | 0.0117 | 0.00589 | 0.0469 | Wald ratio | 1 | cis | NA |
| Cough on most days | -0.0605 | 0.0313 | 0.0534 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K35 Acute appendicitis | 0.137 | 0.0731 | 0.0611 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I48 Atrial fibrillation and flutter | -0.108 | 0.0615 | 0.0778 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: psoriasis | 0.0879 | 0.0502 | 0.0795 | Wald ratio | 1 | cis | NA |
| Weight | 0.00884 | 0.00512 | 0.0846 | Wald ratio | 1 | cis | NA |
| Hearing difficulty or problems: Yes | 0.0167 | 0.00984 | 0.0902 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Cataract | 0.0511 | 0.0302 | 0.091 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: G47 Sleep disorders | -0.149 | 0.0886 | 0.0927 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K57 Diverticular disease of intestine | -0.0734 | 0.044 | 0.0954 | Wald ratio | 1 | cis | NA |
| _...and 55 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3651_50_5` | VEGF sR2 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_79 association rows across 37 traits (66 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating KDR levels (id: OID00677_OID21497) | 1e-1414 | rs34231037 | 7 | GCST90860021 | no MR -> candidate analysis |
| Circulating KDR levels (id: OID00780_OID21497) | 7e-1370 | rs34231037 | 7 | GCST90860113 | no MR -> candidate analysis |
| KDR protein levels | 2e-231 | rs35389572 | 7 | GCST90469672 | no MR -> candidate analysis |
| Vascular endothelial growth factor receptor 2 levels (KDR.36 | 1e-70 | rs34231037 | 2 | GCST90243323 | no MR -> candidate analysis |
| Serum levels of protein KDR | 5e-53 | rs34231037 | 3 | GCST90088480 | no MR -> candidate analysis |
| Vascular endothelial growth factor receptor 2 levels | 2e-48 | rs2305948 | 8 | GCST90250164 | no MR -> candidate analysis |
| Endometriosis | 2e-45 | rs10517343 | 6 | GCST90841381 | no MR -> candidate analysis |
| Clinical endometriosis | 8e-31 | rs10517343 | 2 | GCST90841386 | no MR -> candidate analysis |
| Endometriosis (MTAG) | 7e-27 | rs1903068 | 2 | GCST90570207 | no MR -> candidate analysis |
| Dupuytren's disease | 7e-23 | rs73818546 | 2 | GCST90301252 | no MR -> candidate analysis |
| Self-reported endometriosis | 9e-22 | rs10517343 | 1 | GCST90841387 | no MR -> candidate analysis |
| Blood protein levels | 6e-21 | rs2305948 | 1 | GCST006585 | no MR -> candidate analysis |
| _...and 25 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1602 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| neoplasm | 0.285 | — | established (curated) | MR: beta=0.0663, p=0.149 (cis) |
| endometriosis | 0.88 | — | common-variant locus | no MR -> candidate analysis |
| capillary infantile hemangioma | 0.547 | — | established (curated) | no MR -> candidate analysis |

> Of the 3 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (TEL/KDR) |
| gnomAD constraint | pLI=1, LOEUF=0.345 — LoF-INTOLERANT |
| GWAS Catalog | 53 unique SNPs / 106 rows |
| ClinVar | 277 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 7 clinical annotations across 3 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1602 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'KDR' and resolved to 'TEL/KDR' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 277 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 20 of 37 traits by best p-value, aggregated from 79 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P35968 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000128052/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4630759/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/KDR — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/KDR — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=KDR%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=KDR — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/KDR — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:21:00  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
