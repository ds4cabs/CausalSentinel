# Protein Dossier — BOC (Brother of CDO)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Height | -0.0705 | 0.0158 | 7.69e-06 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | 0.066 | 0.0172 | 1.20e-04 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | 0.0423 | 0.0133 | 0.00144 | Wald ratio | 1 | cis | NA |
| Vascular or heart problems diagnosed by doctor: Angina | 0.19 | 0.0618 | 0.00205 | Wald ratio | 1 | cis | NA |
| Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.0938 | 0.0336 | 0.00527 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | 0.138 | 0.0515 | 0.00733 | Wald ratio | 1 | cis | NA |
| Autism | -0.345 | 0.151 | 0.022 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I48 Atrial fibrillation and flutter | 0.228 | 0.101 | 0.0242 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: bladder problem (not cancer) | 0.295 | 0.132 | 0.0257 | Wald ratio | 1 | cis | NA |
| Birth weight | -0.0386 | 0.0195 | 0.0478 | Wald ratio | 1 | cis | NA |
| Low grade serous ovarian cancer | -0.532 | 0.27 | 0.049 | Wald ratio | 1 | cis | NA |
| Fractured or broken bones in last 5 years | -0.0866 | 0.0452 | 0.0556 | Wald ratio | 1 | cis | NA |
| _...and 81 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-4328_2_2` | BOC | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_76 association rows across 37 traits (67 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating BOC levels (id: OID00386_OID20116) | 1e-218 | rs4682478 | 7 | GCST90859748 | no MR -> candidate analysis |
| Circulating BOC levels (id: OID01380_OID20116) | 3e-140 | rs4682478 | 7 | GCST90860567 | no MR -> candidate analysis |
| BOC protein levels | 8e-140 | rs3856718 | 4 | GCST90468458 | no MR -> candidate analysis |
| CD200R1 protein levels | 2e-115 | rs1846594 | 5 | GCST90468605 | no MR -> candidate analysis |
| Height | 4e-105 | rs3846046 | 10 | GCST90245848 | MR: beta=-0.0705, p=7.69e-06 (cis) |
| Brother of CDO levels | 7e-34 | rs34284771 | 3 | GCST90246727 | no MR -> candidate analysis |
| Serum levels of protein BOC | 2e-20 | rs3856720 | 1 | GCST90088664 | no MR -> candidate analysis |
| Cerebrospinal fluid protein BOC levels | 8e-20 | rs79231157 | 1 | GCST90943087 | no MR -> candidate analysis |
| Benign neoplasm of colon (PheCode 208) | 1e-18 | rs1499899 | 2 | GCST90475617 | no MR -> candidate analysis |
| Colorectal cancer | 2e-16 | rs13086367 | 6 | GCST90129505 | no MR -> candidate analysis |
| Type 2 diabetes | 2e-14 | rs775230 | 1 | GCST90492734 | no MR -> candidate analysis |
| Height (baseline) | 4e-14 | rs41271357 | 1 | GCST90565843 | no MR -> candidate analysis |
| _...and 25 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 178 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| benign colon neoplasm | 0.641 | — | common-variant locus | MR: beta=0.16, p=0.098 (cis) |
| polyp of colon | 0.626 | — | common-variant locus | no MR -> candidate analysis |
| adolescent idiopathic scoliosis | 0.55 | — | common-variant locus | no MR -> candidate analysis |
| colonic neoplasm | 0.535 | — | common-variant locus | no MR -> candidate analysis |
| rectal neoplasm | 0.535 | — | common-variant locus | no MR -> candidate analysis |
| anus neoplasm | 0.535 | — | common-variant locus | MR: beta=0.16, p=0.098 (cis) |
| colorectal cancer | 0.511 | — | common-variant locus | no MR -> candidate analysis |
| intestinal disorder | 0.497 | — | common-variant locus | no MR -> candidate analysis |
| frozen shoulder | 0.47 | — | common-variant locus | no MR -> candidate analysis |
| type 2 diabetes mellitus | 0.461 | — | common-variant locus | no MR -> candidate analysis |
| diabetes mellitus | 0.433 | — | common-variant locus | no MR -> candidate analysis |
| benign neoplasm | 0.39 | — | common-variant locus | MR: beta=0.16, p=0.098 (cis) |
| device complication | 0.378 | — | common-variant locus | no MR -> candidate analysis |
| placenta praevia | 0.366 | — | common-variant locus | no MR -> candidate analysis |
| idiopathic dilated cardiomyopathy | 0.362 | — | common-variant locus | no MR -> candidate analysis |

> Of the 15 rows above, **12 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=3.1e-17, LOEUF=0.821 — LoF-tolerant |
| GWAS Catalog | 70 unique SNPs / 140 rows |
| ClinVar | 266 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 178 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'BOC'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 266 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 37 traits by best p-value, aggregated from 76 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9BWV1 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000144857/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/BOC — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/BOC — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=BOC%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/BOC — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:17:51  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
