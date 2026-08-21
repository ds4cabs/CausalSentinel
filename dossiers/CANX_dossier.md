# Protein Dossier — CANX (Calnexin)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Ulcerative colitis | -0.158 | 0.0674 | 0.0187 | Wald ratio | 1 | trans | NA |
| Total cholesterol | 0.0482 | 0.0209 | 0.0211 | Wald ratio | 1 | trans | NA |
| Serum cystatin C (eGFRcys) | -0.0217 | 0.0098 | 0.0266 | Wald ratio | 1 | trans | NA |
| Alzheimer's disease | 0.196 | 0.0899 | 0.0296 | Wald ratio | 1 | trans | NA |
| Crohn's disease | 0.133 | 0.0654 | 0.0414 | Wald ratio | 1 | trans | NA |
| Red blood cell count | -0.0251 | 0.0124 | 0.0419 | Wald ratio | 1 | trans | NA |
| HDL cholesterol | 0.0405 | 0.02 | 0.0433 | Wald ratio | 1 | trans | NA |
| High grade serous ovarian cancer | 0.168 | 0.0884 | 0.0577 | Wald ratio | 1 | trans | NA |
| Neuroticism | -0.0384 | 0.0213 | 0.0719 | Wald ratio | 1 | trans | NA |
| Internalizing problems | -0.208 | 0.117 | 0.0743 | Wald ratio | 1 | trans | NA |
| Neo-openness to experience | 0.621 | 0.37 | 0.0935 | Wald ratio | 1 | trans | NA |
| Clear cell ovarian cancer | 0.378 | 0.229 | 0.0996 | Wald ratio | 1 | trans | NA |
| _...and 40 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_28 association rows across 16 traits (25 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| monocyte (fraction, mean, inv-norm transformed) | 2e-32 | rs59666900 | 2 | GCST90475511 | no MR -> candidate analysis |
| monocyte (fraction, maximum, inv-norm transformed) | 2e-26 | rs59666900 | 2 | GCST90475508 | no MR -> candidate analysis |
| White blood cell count | 1e-23 | rs13182141 | 8 | GCST90662906 | no MR -> candidate analysis |
| Neutrophil count | 4e-18 | rs13182141 | 3 | GCST90002398 | no MR -> candidate analysis |
| Serum levels of protein MGAT4B | 2e-14 | rs192173275 | 1 | GCST90089688 | no MR -> candidate analysis |
| white blood cell count (WBC, minimum, inv-norm transformed) | 3e-11 | rs1134924 | 1 | GCST90480725 | no MR -> candidate analysis |
| Circulating LGALS3 levels | 4e-11 | rs557104923 | 1 | GCST90859927 | no MR -> candidate analysis |
| Lymphocyte count | 9e-11 | rs369386134 | 2 | GCST90002388 | no MR -> candidate analysis |
| Myeloid white cell count | 6e-10 | rs13182141 | 1 | GCST004626 | no MR -> candidate analysis |
| Platelet count | 8e-10 | rs111374658 | 1 | GCST90662907 | no MR -> candidate analysis |
| Alzheimer's disease or family history of Alzheimer's disease | 1e-9 | rs1459112573 | 1 | GCST90624094 | no MR -> candidate analysis |
| Blood pressure (pleiotropy model 2 SBP adjusted for estimate | 4e-9 | rs13180726 | 1 | GCST90239829 | no MR -> candidate analysis |
| _...and 4 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 2080 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Alzheimer disease | 0.206 | — | common-variant locus | no MR -> candidate analysis |
| Abnormality of the skeletal system | 0.208 | — | common-variant locus | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Calnexin) |
| gnomAD constraint | pLI=1, LOEUF=0.289 — LoF-INTOLERANT |
| GWAS Catalog | 65 unique SNPs / 130 rows |
| ClinVar | 164 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 2080 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'CANX' and resolved to 'Calnexin' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 164 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 16 of 16 traits by best p-value, aggregated from 28 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P27824 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000127022/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2719/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CANX — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CANX — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CANX%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CANX — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:27:15  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
