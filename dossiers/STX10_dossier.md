# Protein Dossier — STX10 (Syntaxin-10)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Body mass index (BMI) | 0.0128 | 0.00497 | 0.00996 | Wald ratio | 1 | trans | NA |
| Lung cancer | -0.0869 | 0.0354 | 0.0139 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: R04 Haemorrhage from respiratory passages | 0.14 | 0.0603 | 0.0206 | Wald ratio | 1 | trans | NA |
| Underlying (primary) cause of death: ICD10: E85.4 Organ-limited amyloidosis | 1.08 | 0.481 | 0.0247 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: joint disorder | -0.186 | 0.0882 | 0.0349 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: K20 Oesophagitis | 0.0953 | 0.0457 | 0.0371 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: bone disorder | 0.185 | 0.0889 | 0.0377 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: J33 Nasal polyp | 0.131 | 0.0636 | 0.0387 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: kidney stone or ureter stone or bladder stone | 0.103 | 0.0508 | 0.043 | Wald ratio | 1 | trans | NA |
| Age at menopause | -0.0751 | 0.0375 | 0.0455 | Wald ratio | 1 | trans | NA |
| Weight | 0.00855 | 0.00439 | 0.0514 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: M17 Gonarthrosis [arthrosis of knee] | 0.0653 | 0.0336 | 0.0517 | Wald ratio | 1 | trans | NA |
| _...and 103 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_3 association rows across 3 traits (2 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Venous thromboembolism | 2e-9 | rs7508633 | 1 | GCST009030 | no MR -> candidate analysis |
| Household income (MTAG) | 3e-8 | rs116712274 | 1 | GCST009524 | no MR -> candidate analysis |
| Triamcinolone acetonide-induced ocular hypertension | 6e-7 | rs546725617 | 1 | GCST90244659 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 27 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| osteoarthritis, knee | 0.441 | — | common-variant locus | MR: beta=-0.0372, p=0.377 (trans) |
| venous thromboembolism | 0.409 | — | common-variant locus | no MR -> candidate analysis |
| brain aneurysm | 0.197 | — | common-variant locus | no MR -> candidate analysis |
| skin neoplasm | 0.197 | — | common-variant locus | no MR -> candidate analysis |
| exfoliation syndrome | 0.079 | — | common-variant locus | no MR -> candidate analysis |
| Abnormality of the cardiovascular system | 0.048 | — | common-variant locus | no MR -> candidate analysis |
| placental retention | 0.043 | — | common-variant locus | no MR -> candidate analysis |

> Of the 7 rows above, **6 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=8.4e-13, LOEUF=1.36 — LoF-tolerant |
| GWAS Catalog | 66 unique SNPs / 132 rows |
| ClinVar | 86 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 27 of 27 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'STX10'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 86 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 3 of 3 traits by best p-value, aggregated from 3 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O60499 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000104915/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/STX10 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/STX10 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=STX10%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/STX10 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:15:42  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
