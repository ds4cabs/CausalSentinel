# Protein Dossier — LEPR (Leptin receptor)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Childhood intelligence | -0.0359 | 0.0122 | 0.00328 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | 0.00658 | 0.00232 | 0.00462 | Wald ratio | 1 | cis | NA |
| Chronic kidney disease | -0.0386 | 0.0138 | 0.00528 | Wald ratio | 1 | cis | NA |
| Autism | -0.0707 | 0.0271 | 0.00903 | Wald ratio | 1 | cis | NA |
| Eczema | 0.0422 | 0.0163 | 0.00966 | Wald ratio | 1 | cis | NA |
| Birth weight | -0.0088 | 0.00349 | 0.0117 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: G47 Sleep disorders | 0.0666 | 0.0283 | 0.0188 | Wald ratio | 1 | cis | NA |
| Diastolic blood pressure  automated reading | 0.00558 | 0.00238 | 0.019 | Wald ratio | 1 | cis | NA |
| Sleep duration | -0.00411 | 0.00181 | 0.0232 | Wald ratio | 1 | cis | NA |
| Weight | 0.0046 | 0.00205 | 0.025 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R10 Abdominal and pelvic pain | 0.0237 | 0.0109 | 0.0302 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K60 Fissure and fistula of anal and rectal regions | 0.0669 | 0.0322 | 0.0375 | Wald ratio | 1 | cis | NA |
| _...and 86 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-5400_52_3` | sLeptin R | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_481 association rows across 219 traits (464 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Leptin receptor levels | 1e-3146 | rs10399687 | 26 | GCST90248273 | no MR -> candidate analysis |
| Leptin receptor levels (LEPR.5400.52.3) | 3e-861 | rs3790438 | 3 | GCST90241749 | no MR -> candidate analysis |
| C-reactive protein levels | 2e-732 | rs2154384 | 35 | GCST009777 | no MR -> candidate analysis |
| Leptin receptor, soluble levels | 2e-698 | rs2376018 | 1 | GCST90426339 | no MR -> candidate analysis |
| Blood protein levels | 2e-654 | rs6658330 | 1 | GCST006585 | no MR -> candidate analysis |
| C-reactive protein | 2e-560 | rs12127241 | 5 | GCST90018950 | no MR -> candidate analysis |
| Circulating LEPR levels | 1e-311 | rs2376018 | 3 | GCST90860705 | no MR -> candidate analysis |
| C-reactive protein levels (MTAG) | 2e-310 | rs12030543 | 21 | GCST90179146 | no MR -> candidate analysis |
| IL6ST/LEPR protein level ratio | 2e-267 | rs1805094 | 1 | GCST90315165 | no MR -> candidate analysis |
| LEPR protein levels | 3e-251 | rs2376018 | 6 | GCST90469756 | no MR -> candidate analysis |
| C-reactive protein levels (UKB data field 30710) | 1e-187 | rs6698653 | 8 | GCST90468064 | no MR -> candidate analysis |
| Protein quantitative trait loci | 4e-138 | rs61781308 | 1 | GCST010900 | no MR -> candidate analysis |
| _...and 207 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 2475 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| obesity due to leptin receptor gene deficiency | 0.829 | — | established (curated) | no MR -> candidate analysis |
| type 2 diabetes mellitus | 0.795 | — | common-variant locus | no MR -> candidate analysis |
| obesity disorder | 0.552 | — | common-variant locus | no MR -> candidate analysis |
| diabetes mellitus | 0.475 | — | common-variant locus | no MR -> candidate analysis |
| Abnormality of the skeletal system | 0.672 | — | common-variant locus | no MR -> candidate analysis |
| Obesity | 0.442 | — | established (curated) | MR: beta=0.00658, p=0.00462 (cis) |
| metabolic dysfunction-associated steatohepatitis | 0.377 | — | common-variant locus | no MR -> candidate analysis |
| morbid obesity | 0.545 | — | common-variant locus | no MR -> candidate analysis |
| obesity due to congenital leptin deficiency | 0.438 | — | established (curated) | no MR -> candidate analysis |
| smoking cessation | 0.46 | — | common-variant locus | no MR -> candidate analysis |
| Barrett esophagus | 0.424 | — | common-variant locus | no MR -> candidate analysis |
| eye disorder | 0.424 | — | common-variant locus | no MR -> candidate analysis |
| ovarian dysfunction | 0.424 | — | common-variant locus | no MR -> candidate analysis |
| hereditary disease | 0.318 | — | established (curated) | no MR -> candidate analysis |
| monogenic diabetes | 0.302 | — | established (curated) | no MR -> candidate analysis |

> Of the 15 rows above, **14 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 2 known modulators (Leptin receptor) |
| gnomAD constraint | pLI=5.3e-06, LOEUF=0.61 — LoF-tolerant |
| GWAS Catalog | 184 unique SNPs / 498 rows |
| ClinVar | 579 records; 5 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 5 clinical annotations across 4 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 2475 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'LEPR' and resolved to 'Leptin receptor' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 579 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 20 of 219 traits by best p-value, aggregated from 481 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P48357 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000116678/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL5913/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/LEPR — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/LEPR — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=LEPR%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=LEPR — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/LEPR — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:29:53  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
