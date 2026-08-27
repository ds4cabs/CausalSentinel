# Protein Dossier — THBS4 (Thrombospondin-4)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: sleep apnoea | 0.48 | 0.158 | 0.00234 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K40 Inguinal hernia | 0.173 | 0.071 | 0.015 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: gastro-oesophageal reflux (gord)  or  gastric reflux | 0.137 | 0.0578 | 0.018 | Wald ratio | 1 | cis | NA |
| Caudate volume | -67 | 28.8 | 0.0199 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: diverticular disease or diverticulitis | 0.229 | 0.105 | 0.0286 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Injury or trauma resulting in loss of vision | 0.289 | 0.138 | 0.0361 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: bladder problem (not cancer) | 0.281 | 0.139 | 0.0432 | Wald ratio | 1 | cis | NA |
| Squamous cell lung cancer | -0.299 | 0.149 | 0.0448 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: enlarged prostate | -0.329 | 0.169 | 0.0512 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: L03 Cellulitis | 0.238 | 0.123 | 0.0525 | Wald ratio | 1 | cis | NA |
| Femoral neck bone mineral density | -0.0821 | 0.0425 | 0.0532 | Wald ratio | 1 | cis | NA |
| Thalamus volume | -70.5 | 36.8 | 0.0554 | Wald ratio | 1 | cis | NA |
| _...and 66 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3340_53_1` | TSP4 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_49 association rows across 31 traits (45 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| COMP/THBS4 protein level ratio | 2e-435 | rs2438637 | 1 | GCST90314193 | no MR -> candidate analysis |
| FAP/THBS4 protein level ratio | 2e-320 | rs2438637 | 1 | GCST90314785 | no MR -> candidate analysis |
| Circulating THBS4 levels | 3e-267 | rs35351529 | 4 | GCST90860466 | no MR -> candidate analysis |
| Thrombospondin-4 levels | 8e-110 | rs13167730 | 3 | GCST90249997 | no MR -> candidate analysis |
| Cerebrospinal fluid protein THBS4 levels | 3e-55 | rs256438 | 1 | GCST90945058 | no MR -> candidate analysis |
| THBS4 protein levels | 3e-27 | rs568927878 | 6 | GCST90470855 | no MR -> candidate analysis |
| Height | 4e-27 | rs2451933 | 1 | GCST90245848 | no MR -> candidate analysis |
| Smoking initiation | 1e-22 | rs7707036 | 2 | GCST90243985 | no MR -> candidate analysis |
| Corneal curvature | 2e-22 | rs13180294 | 3 | GCST90012795 | no MR -> candidate analysis |
| Corneal resistance factor (MTAG) | 2e-19 | rs13167730 | 2 | GCST90102517 | no MR -> candidate analysis |
| Impedance of arm right (UKB data field 23109) | 3e-19 | rs41272276 | 1 | GCST90468172 | no MR -> candidate analysis |
| Refractive error | 1e-18 | rs256438 | 3 | GCST90841196 | no MR -> candidate analysis |
| _...and 19 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 535 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Abnormality of the skeletal system | 0.894 | 0.799 | multi-layer: burden+GWAS (allelic-series candidate) | no MR -> candidate analysis |
| Abnormality of refraction | 0.473 | — | common-variant locus | no MR -> candidate analysis |
| attention deficit-hyperactivity disorder | 0.339 | — | common-variant locus | no MR -> candidate analysis |
| substance abuse | 0.339 | — | common-variant locus | no MR -> candidate analysis |
| smoking initiation | 0.284 | — | common-variant locus | no MR -> candidate analysis |
| Varicose veins | 0.166 | — | common-variant locus | MR: beta=0.136, p=0.108 (cis) |
| post term pregnancy | 0.15 | — | common-variant locus | no MR -> candidate analysis |
| benign thyroid gland neoplasm | 0.146 | — | common-variant locus | no MR -> candidate analysis |
| vein disorder | 0.129 | — | common-variant locus | no MR -> candidate analysis |
| lymphatic system disorder | 0.129 | — | common-variant locus | no MR -> candidate analysis |
| glaucoma | 0.122 | — | common-variant locus | no MR -> candidate analysis |

> Of the 11 rows above, **10 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 1 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=6.7e-24, LOEUF=0.927 — LoF-tolerant |
| GWAS Catalog | 62 unique SNPs / 115 rows |
| ClinVar | 158 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 535 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'THBS4'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 158 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 31 traits by best p-value, aggregated from 49 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P35443 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000113296/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/THBS4 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/THBS4 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=THBS4%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/THBS4 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:20:46  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
