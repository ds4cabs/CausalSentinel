# Protein Dossier — FST (Follistatin)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Triglycerides | 0.82 | 0.0243 | 6.50e-250 | Wald ratio | 1 | trans | 0.999 |
| Non-cancer illness code  self-reported: gout | 0.962 | 0.0564 | 2.86e-65 | Wald ratio | 1 | trans | 0.998 |
| Non-cancer illness code  self-reported: high cholesterol | 0.468 | 0.0298 | 1.09e-55 | Wald ratio | 1 | trans | 0.999 |
| Total cholesterol | 0.366 | 0.0257 | 6.67e-46 | Wald ratio | 1 | trans | 0.997 |
| Urate | 0.55 | 0.0393 | 1.56e-44 | Wald ratio | 1 | trans | NA |
| Alcohol intake frequency | 0.343 | 0.0259 | 7.43e-40 | Wald ratio | 1 | trans | 0.998 |
| Fasting glucose | -0.229 | 0.0221 | 5.57e-25 | Wald ratio | 1 | trans | 0.998 |
| Crohn's disease | 0.819 | 0.086 | 1.74e-21 | Wald ratio | 1 | trans | 0.998 |
| Weight | -0.127 | 0.0155 | 2.52e-16 | Wald ratio | 1 | trans | 0.999 |
| Sodium in urine | 0.14 | 0.0173 | 6.66e-16 | Wald ratio | 1 | trans | 0.999 |
| Inflammatory bowel disease | 0.551 | 0.0712 | 1.03e-14 | Wald ratio | 1 | trans | 0.999 |
| Serum creatinine (eGFRcrea) | 0.0486 | 0.00657 | 1.45e-13 | Wald ratio | 1 | trans | 0.999 |
| _...and 127 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-4132_27_2` | FST | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_141 association rows across 87 traits (120 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Bone mineral density mean | 1e-300 | rs75580782 | 2 | GCST90321120 | no MR -> candidate analysis |
| MOCS2 protein levels | 3e-102 | rs38059 | 8 | GCST90469928 | no MR -> candidate analysis |
| Corneal resistance factor (MTAG) | 5e-78 | rs4865543 | 3 | GCST90102517 | no MR -> candidate analysis |
| Height | 1e-60 | rs11954686 | 9 | GCST90245848 | MR: beta=-0.143, p=2.62e-11 (trans) |
| Corneal hysteresis | 5e-60 | rs27323 | 1 | GCST011391 | no MR -> candidate analysis |
| Circulating FST levels | 1e-56 | rs62370480 | 2 | GCST90859779 | no MR -> candidate analysis |
| Corneal resistance factor | 5e-53 | rs27323 | 3 | GCST90100568 | no MR -> candidate analysis |
| Central corneal thickness (MTAG) | 7e-53 | rs7737693 | 1 | GCST90102518 | no MR -> candidate analysis |
| FST protein levels | 4e-41 | rs1469101 | 1 | GCST90469273 | no MR -> candidate analysis |
| Kidney sinus volume | 5e-35 | rs6875756 | 3 | GCST90668000 | no MR -> candidate analysis |
| acne vulgaris | 4e-28 | rs629725 | 3 | GCST90092000 | no MR -> candidate analysis |
| Appendicular lean mass | 1e-27 | rs62370472 | 3 | GCST90000025 | no MR -> candidate analysis |
| _...and 75 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 2614 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Abnormality of the skeletal system | 0.809 | — | common-variant locus | no MR -> candidate analysis |
| gout | 0.689 | — | common-variant locus | MR: beta=0.962, p=2.86e-65 (trans) |
| acne | 0.656 | — | common-variant locus | no MR -> candidate analysis |
| type 2 diabetes mellitus | 0.583 | — | common-variant locus | no MR -> candidate analysis |
| hair anomaly | 0.507 | — | common-variant locus | no MR -> candidate analysis |
| prostate carcinoma | 0.466 | — | common-variant locus | no MR -> candidate analysis |
| orofacial cleft | 0.426 | — | established (curated) | no MR -> candidate analysis |
| abdominal aortic aneurysm | 0.392 | — | common-variant locus | no MR -> candidate analysis |
| coronary artery disorder | 0.345 | — | common-variant locus | no MR -> candidate analysis |
| hypertensive disorder | 0.345 | — | common-variant locus | no MR -> candidate analysis |
| Abnormality of refraction | 0.348 | — | common-variant locus | no MR -> candidate analysis |
| dyshidrosis | 0.346 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.339 | — | common-variant locus | no MR -> candidate analysis |
| peritonitis | 0.339 | — | common-variant locus | no MR -> candidate analysis |
| tibia fracture | 0.339 | — | common-variant locus | no MR -> candidate analysis |

> Of the 15 rows above, **14 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1, LOEUF=0.308 — LoF-INTOLERANT |
| GWAS Catalog | 113 unique SNPs / 175 rows |
| ClinVar | 54 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 2614 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'FST'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 54 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 87 traits by best p-value, aggregated from 141 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P19883 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000134363/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/FST — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/FST — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=FST%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/FST — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:43:20  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
