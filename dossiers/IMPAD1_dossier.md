# Protein Dossier — IMPAD1 (Golgi-resident adenosine 3',5'-bisphosphate 3'-phosphatase)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: psoriasis | 0.168 | 0.0487 | 5.48e-04 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I83 Varicose veins of lower extremities | 0.101 | 0.0387 | 0.00919 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: gastro-oesophageal reflux (gord)  or  gastric reflux | 0.0688 | 0.0275 | 0.0123 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Other bones | -0.0714 | 0.0286 | 0.0125 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N40 Hyperplasia of prostate | 0.131 | 0.056 | 0.0194 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: vaginal prolapse or uterine prolapse | -0.219 | 0.105 | 0.0363 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: migraine | 0.0674 | 0.0331 | 0.0414 | Wald ratio | 1 | cis | NA |
| Creatinine (enzymatic) in urine | -0.0115 | 0.00585 | 0.0502 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: C61 Malignant neoplasm of prostate | 0.129 | 0.0663 | 0.0525 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M23 Internal derangement of knee | 0.0727 | 0.0383 | 0.0574 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: S76 Injury of muscle and tendon at hip and thigh level | 0.384 | 0.208 | 0.0656 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K20 Oesophagitis | -0.128 | 0.0706 | 0.0695 | Wald ratio | 1 | cis | NA |
| _...and 57 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_No GWAS Catalog associations mapped to this gene._

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1718 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| chondrodysplasia with joint dislocations, gPAPP type | 0.838 | — | established (curated) | no MR -> candidate analysis |
| chronic kidney disease | 0.515 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.433 | — | common-variant locus | no MR -> candidate analysis |
| rheumatoid arthritis | 0.383 | — | common-variant locus | no MR -> candidate analysis |
| placental abruption | 0.378 | — | common-variant locus | no MR -> candidate analysis |
| benign thyroid gland neoplasm | 0.378 | — | common-variant locus | no MR -> candidate analysis |
| bone remodeling disease | 0.37 | — | common-variant locus | no MR -> candidate analysis |
| breast disorder | 0.357 | — | common-variant locus | no MR -> candidate analysis |
| liver disorder | 0.353 | — | common-variant locus | no MR -> candidate analysis |
| adolescent idiopathic scoliosis | 0.351 | — | common-variant locus | no MR -> candidate analysis |
| stroke disorder | 0.35 | — | common-variant locus | no MR -> candidate analysis |
| ovarian neoplasm | 0.347 | — | common-variant locus | no MR -> candidate analysis |
| temporomandibular joint disorder | 0.346 | — | common-variant locus | no MR -> candidate analysis |
| placental retention | 0.269 | — | common-variant locus | no MR -> candidate analysis |
| connective tissue disorder | 0.268 | — | common-variant locus | no MR -> candidate analysis |

> Of the 15 rows above, **15 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | not available |
| GWAS Catalog | no mapped SNPs |
| ClinVar | no records |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1718 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'IMPAD1'.
- **`gnomad`** — No gnomAD constraint data.
- **`gwas`** — No GWAS Catalog SNPs mapped to this gene.
- **`clinvar`** — No ClinVar records.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — No GWAS Catalog associations mapped to this gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9NX62 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000104331/associations — _Open Targets data release 26.06_

## Provenance

- Generated: 2026-08-14T03:17:05  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
