# Protein Dossier — WARS (Tryptophan--tRNA ligase, cytoplasmic)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Age at menarche | -0.114 | 0.0267 | 2.10e-05 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertension | -0.064 | 0.0194 | 9.79e-04 | Wald ratio | 1 | cis | NA |
| Total cholesterol | 0.0788 | 0.0239 | 9.84e-04 | Wald ratio | 1 | cis | NA |
| LDL cholesterol | 0.0776 | 0.0247 | 0.00167 | Wald ratio | 1 | cis | NA |
| Celiac disease | 0.276 | 0.0879 | 0.00171 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: G56 Mononeuropathies of upper limb | 0.201 | 0.0668 | 0.00261 | Wald ratio | 1 | cis | NA |
| Fasting glucose | 0.0431 | 0.0145 | 0.00295 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: C61 Malignant neoplasm of prostate | 0.287 | 0.0995 | 0.00387 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: osteoporosis | 0.197 | 0.0708 | 0.00544 | Wald ratio | 1 | cis | NA |
| Systolic blood pressure  automated reading | 0.028 | 0.0109 | 0.0105 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M16 Coxarthrosis [arthrosis of hip] | 0.187 | 0.0743 | 0.012 | Wald ratio | 1 | cis | NA |
| Transferrin | -0.115 | 0.0482 | 0.0176 | Wald ratio | 1 | cis | NA |
| _...and 114 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_No GWAS Catalog associations mapped to this gene._

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 608 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| neurodevelopmental disorder with microcephaly and speech delay, with or without brain abnormalities | 0.693 | — | established (curated) | no MR -> candidate analysis |
| complex neurodevelopmental disorder | 0.608 | — | established (curated) | no MR -> candidate analysis |
| autosomal recessive primary microcephaly | 0.608 | — | established (curated) | no MR -> candidate analysis |
| neuronopathy, distal hereditary motor, type 9 | 0.538 | — | established (curated) | no MR -> candidate analysis |
| diabetes mellitus | 0.469 | — | common-variant locus | no MR -> candidate analysis |
| adolescent idiopathic scoliosis | 0.403 | — | common-variant locus | no MR -> candidate analysis |
| Abnormality of the skeletal system | 0.337 | — | common-variant locus | no MR -> candidate analysis |
| hereditary disease | 0.317 | — | established (curated) | no MR -> candidate analysis |
| vertebral disorder | 0.279 | — | common-variant locus | no MR -> candidate analysis |
| schizophrenia | 0.182 | — | established (curated) | MR: beta=-0.0447, p=0.346 (cis) |
| asthma | 0.152 | 0.152 | exploratory rare-variant signal | MR: beta=0.0254, p=0.385 (cis) |

> Of the 11 rows above, **9 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 1 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Tryptophan--tRNA ligase, cytoplasmic) |
| gnomAD constraint | not available |
| GWAS Catalog | no mapped SNPs |
| ClinVar | no records |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 608 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'WARS' and resolved to 'Tryptophan--tRNA ligase, cytoplasmic' — confirm this is the intended target.
- **`gnomad`** — No gnomAD constraint data.
- **`gwas`** — No GWAS Catalog SNPs mapped to this gene.
- **`clinvar`** — No ClinVar records.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — No GWAS Catalog associations mapped to this gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P23381 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000140105/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL6066299/ — _ChEMBL_37 (released 2026-05-01)_

## Provenance

- Generated: 2026-08-14T05:37:02  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
