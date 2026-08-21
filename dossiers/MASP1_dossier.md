# Protein Dossier — MASP1 (Mannan-binding lectin serine protease 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Systolic blood pressure  automated reading | -0.0209 | 0.00727 | 0.00409 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: pernicious anaemia | 0.263 | 0.102 | 0.00965 | Wald ratio | 1 | trans | NA |
| Sleep duration | -0.0137 | 0.00554 | 0.0134 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: I30 Acute pericarditis | 0.573 | 0.245 | 0.0195 | Wald ratio | 1 | trans | NA |
| Happiness | 0.0205 | 0.0088 | 0.0199 | Wald ratio | 1 | trans | NA |
| Triglycerides | -0.0339 | 0.0148 | 0.0221 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: migraine | -0.103 | 0.0456 | 0.0238 | Wald ratio | 1 | trans | NA |
| Pulse rate | 0.0268 | 0.0125 | 0.0324 | Wald ratio | 1 | trans | NA |
| Microalbuminuria | -0.131 | 0.0627 | 0.0365 | Wald ratio | 1 | trans | NA |
| Eye problems or disorders: Diabetes related eye disease | -0.247 | 0.118 | 0.0368 | Wald ratio | 1 | trans | NA |
| Subjective well being | -0.0171 | 0.00856 | 0.0455 | Wald ratio | 1 | trans | NA |
| Percent emphysema | 0.077 | 0.0391 | 0.0487 | Wald ratio | 1 | trans | NA |
| _...and 94 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3605_77_4` | MASP3 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_69 association rows across 43 traits (60 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Bone mineral density mean | 1e-300 | rs190858137 | 1 | GCST90321120 | no MR -> candidate analysis |
| MASP1 protein levels | 1e-222 | rs34053057 | 8 | GCST90469863 | no MR -> candidate analysis |
| Circulating MASP1 levels | 2e-210 | rs62292760 | 8 | GCST90860240 | no MR -> candidate analysis |
| Serum levels of protein MASP1 | 4e-127 | rs28945068 | 1 | GCST90090044 | no MR -> candidate analysis |
| Blood protein levels | 6e-43 | rs28945068 | 1 | GCST006585 | no MR -> candidate analysis |
| FCN1 protein levels | 4e-23 | rs850313 | 1 | GCST90469203 | no MR -> candidate analysis |
| Kidney-associated antigen 1 levels | 2e-21 | rs1533593 | 1 | GCST90248152 | no MR -> candidate analysis |
| Descending aorta maximum area (MTAG) | 5e-21 | rs698099 | 1 | GCST90137451 | no MR -> candidate analysis |
| Mannan-binding lectin serine protease 1 levels | 7e-21 | rs34053057 | 2 | GCST90248429 | no MR -> candidate analysis |
| Connective tissue growth factor levels | 2e-19 | rs3214401 | 1 | GCST90137906 | no MR -> candidate analysis |
| Descending aorta maximum area | 2e-19 | rs698099 | 1 | GCST90137442 | no MR -> candidate analysis |
| Descending thoracic aortic diameter | 2e-16 | rs698099 | 2 | GCST90094401 | no MR -> candidate analysis |
| _...and 31 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 438 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| 3MC syndrome 1 | 0.913 | — | established (curated) | no MR -> candidate analysis |
| 3MC syndrome | 0.608 | — | established (curated) | no MR -> candidate analysis |
| hereditary disease | 0.684 | — | established (curated) | no MR -> candidate analysis |
| coronary atherosclerosis | 0.537 | — | common-variant locus | no MR -> candidate analysis |
| coronary artery disorder | 0.53 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.533 | — | common-variant locus | no MR -> candidate analysis |
| Furuncle | 0.419 | — | common-variant locus | no MR -> candidate analysis |
| carbuncle | 0.419 | — | common-variant locus | no MR -> candidate analysis |
| stroke disorder | 0.404 | — | common-variant locus | no MR -> candidate analysis |
| corneal neovascularization | 0.388 | — | common-variant locus | no MR -> candidate analysis |
| osteoarthritis, hip | 0.286 | — | common-variant locus | MR: beta=0.146, p=0.0812 (trans) |
| hypertrophic cardiomyopathy | 0.182 | — | established (curated) | no MR -> candidate analysis |
| microcephaly | 0.182 | — | established (curated) | no MR -> candidate analysis |

> Of the 13 rows above, **12 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Mannan-binding lectin serine protease 1) |
| gnomAD constraint | pLI=9.5e-16, LOEUF=0.95 — LoF-tolerant |
| GWAS Catalog | 61 unique SNPs / 122 rows |
| ClinVar | 452 records; 5 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 438 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'MASP1' and resolved to 'Mannan-binding lectin serine protease 1' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 452 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 43 traits by best p-value, aggregated from 69 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P48740 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000127241/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4295768/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/MASP1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/MASP1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=MASP1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/MASP1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:44:43  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
