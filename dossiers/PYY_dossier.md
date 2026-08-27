# Protein Dossier — PYY (Peptide YY)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: G47 Sleep disorders | 0.593 | 0.121 | 9.10e-07 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Arm | 0.441 | 0.108 | 4.61e-05 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N81 Female genital prolapse | 0.385 | 0.0946 | 4.74e-05 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypopituitarism | 1.19 | 0.303 | 8.85e-05 | Wald ratio | 1 | cis | NA |
| Triglycerides | 0.117 | 0.0318 | 2.33e-04 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: emphysema or chronic bronchitis | 0.362 | 0.1 | 3.14e-04 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: gastro-oesophageal reflux (gord)  or  gastric reflux | 0.216 | 0.0642 | 7.72e-04 | Wald ratio | 1 | cis | NA |
| Putamen volume | -117 | 40.8 | 0.00412 | Wald ratio | 1 | cis | NA |
| HDL cholesterol | -0.0904 | 0.0325 | 0.00536 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: osteoarthritis | 0.132 | 0.0484 | 0.00624 | Wald ratio | 1 | cis | NA |
| Fasting glucose | 0.0522 | 0.0204 | 0.0104 | Wald ratio | 1 | cis | NA |
| Age at menopause | 0.318 | 0.127 | 0.0124 | Wald ratio | 1 | cis | NA |
| _...and 97 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3727_35_1` | PYY | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_19 association rows across 17 traits (13 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| PYY protein levels | 1e-249 | rs8074783 | 2 | GCST90470398 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 9e-38 | rs573345854 | 2 | GCST90838669 | no MR -> candidate analysis |
| CD300LG protein levels | 3e-21 | rs1642598 | 1 | GCST90468623 | no MR -> candidate analysis |
| HDL levels x fish oil supplementation interaction (2df) | 3e-16 | rs147438979 | 1 | GCST011927 | no MR -> candidate analysis |
| Triglyceride levels | 1e-15 | rs116878033 | 1 | GCST010244 | no MR -> candidate analysis |
| Serum levels of protein PYY | 2e-14 | rs2341378 | 1 | GCST90088497 | no MR -> candidate analysis |
| Metabolic syndrome cluster 4 (lipodystrophy-like endotype) | 4e-10 | rs147438979 | 1 | GCST90859211 | no MR -> candidate analysis |
| Blood protein levels | 1e-9 | rs8074783 | 1 | GCST006585 | no MR -> candidate analysis |
| Total body bone mineral density | 2e-9 | rs116953263 | 1 | GCST005348 | no MR -> candidate analysis |
| DNA methylation variation (age effect) | 3e-8 | rs4793062 | 1 | GCST006660 | no MR -> candidate analysis |
| Pulse pressure | 4e-8 | rs62080325 | 1 | GCST004278 | no MR -> candidate analysis |
| Omega-6 fatty acid percentage of total fatty acids | 5e-8 | rs116878033 | 1 | GCST90454484 | no MR -> candidate analysis |
| _...and 5 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 551 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| hyperammonemia due to N-acetylglutamate synthase deficiency | 0.532 | — | established (curated) | no MR -> candidate analysis |
| Hyperammonemia due to N-acetylglutamate synthetase deficiency | 0.532 | — | established (curated) | no MR -> candidate analysis |
| Obesity | 0.182 | — | established (curated) | MR: beta=0.729, p=0.0501 (cis) |

> Of the 3 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1.9e-05, LOEUF=1.89 — LoF-tolerant |
| GWAS Catalog | 62 unique SNPs / 124 rows |
| ClinVar | 58 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 551 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'PYY'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 58 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 17 of 17 traits by best p-value, aggregated from 19 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P10082 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000131096/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PYY — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PYY — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PYY%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/PYY — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:43:07  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
