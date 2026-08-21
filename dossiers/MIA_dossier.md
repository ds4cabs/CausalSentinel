# Protein Dossier — MIA (Melanoma-derived growth regulatory protein)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Creatinine (enzymatic) in urine | 0.00949 | 0.00308 | 0.00204 | Wald ratio | 1 | cis | NA |
| Birth weight | 0.0139 | 0.00458 | 0.00244 | Wald ratio | 1 | cis | NA |
| Neo-agreeableness | 0.214 | 0.0791 | 0.00684 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R11 Nausea and vomiting | 0.122 | 0.0454 | 0.0073 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypopituitarism | 0.327 | 0.128 | 0.0107 | Wald ratio | 1 | cis | NA |
| Sodium in urine | 0.00745 | 0.00316 | 0.0185 | Wald ratio | 1 | cis | NA |
| Nucleus accumbens volume | 3.34 | 1.47 | 0.0234 | Wald ratio | 1 | cis | NA |
| Neo-neuroticism | -0.271 | 0.122 | 0.0265 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hyperthyroidism or thyrotoxicosis | 0.0766 | 0.0346 | 0.027 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R04 Haemorrhage from respiratory passages | -0.107 | 0.0498 | 0.0325 | Wald ratio | 1 | cis | NA |
| Birth length | 0.0277 | 0.013 | 0.0329 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K57 Diverticular disease of intestine | 0.0451 | 0.0216 | 0.037 | Wald ratio | 1 | cis | NA |
| _...and 98 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2687_2_1` | MIA | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_52 association rows across 35 traits (43 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating MIA levels | 5e-2954 | rs2607423 | 1 | GCST90860044 | no MR -> candidate analysis |
| MIA/NBL1 protein level ratio | 2e-1524 | rs112889062 | 1 | GCST90315445 | no MR -> candidate analysis |
| melanoma-derived growth regulatory protein levels | 7e-864 | rs2233159 | 10 | GCST90248443 | no MR -> candidate analysis |
| Melanoma-derived growth regulatory protein levels (MIA.2687. | 3e-253 | rs2604877 | 2 | GCST90241910 | no MR -> candidate analysis |
| Blood protein levels | 1e-164 | rs2233154 | 1 | GCST006585 | no MR -> candidate analysis |
| Melanoma-derived growth regulatory protein level in Chronic  | 3e-64 | rs2607421 | 1 | GCST90237048 | no MR -> candidate analysis |
| Protein levels in obesity | 4e-34 | rs2607426 | 1 | GCST010196 | no MR -> candidate analysis |
| Cigarettes smoked per day | 8e-33 | rs117248593 | 1 | GCST90243987 | MR: beta=-0.0914, p=0.409 (cis) |
| MIA levels | 2e-26 | rs2279699 | 1 | GCST90274901 | no MR -> candidate analysis |
| Serum levels of protein MIA | 9e-26 | rs2604894 | 1 | GCST90088019 | no MR -> candidate analysis |
| Liver enzyme levels (alkaline phosphatase) | 1e-22 | rs11672227 | 1 | GCST90013406 | no MR -> candidate analysis |
| Cerebrospinal fluid protein MIA levels | 3e-19 | rs2607421 | 1 | GCST90944429 | no MR -> candidate analysis |
| _...and 23 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 102 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Kawasaki disease | 0.5 | — | common-variant locus | no MR -> candidate analysis |
| chronic obstructive pulmonary disease | 0.482 | — | common-variant locus | no MR -> candidate analysis |
| preeclampsia | 0.153 | — | common-variant locus | no MR -> candidate analysis |
| medical procedure | 0.097 | — | common-variant locus | no MR -> candidate analysis |
| osteoarthritis, knee | 0.097 | — | common-variant locus | MR: beta=0.0338, p=0.236 (cis) |
| venous thromboembolism | 0.053 | — | common-variant locus | no MR -> candidate analysis |
| Hammer Toe Syndrome | 0.045 | — | common-variant locus | no MR -> candidate analysis |
| chronic bronchitis | 0.038 | — | common-variant locus | no MR -> candidate analysis |

> Of the 8 rows above, **7 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (MIA PaCa-2) |
| gnomAD constraint | pLI=8.5e-07, LOEUF=1.44 — LoF-tolerant |
| GWAS Catalog | 148 unique SNPs / 362 rows |
| ClinVar | 30 records; 9 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 102 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'MIA' and resolved to 'MIA PaCa-2' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 30 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 35 traits by best p-value, aggregated from 52 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q16674 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000261857/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL614725/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/MIA — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/MIA — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=MIA%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/MIA — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:48:05  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
