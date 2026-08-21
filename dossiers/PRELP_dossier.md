# Protein Dossier — PRELP (Prolargin)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Body mass index (BMI) | 0.00819 | 0.00265 | 0.00196 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: K80 Cholelithiasis | 0.0538 | 0.0175 | 0.00206 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: I80 Phlebitis and thrombophlebitis | 0.0884 | 0.0355 | 0.0128 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | 0.0699 | 0.0294 | 0.0174 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: osteoarthritis | -0.0185 | 0.00902 | 0.0402 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: R04 Haemorrhage from respiratory passages | 0.0703 | 0.0343 | 0.0406 | Wald ratio | 1 | trans | NA |
| Pulse rate | 0.00933 | 0.00467 | 0.0459 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: L03 Cellulitis | 0.0553 | 0.0279 | 0.0475 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: iron deficiency anaemia | -0.0765 | 0.0392 | 0.0511 | Wald ratio | 1 | trans | NA |
| Fracture resulting from simple fall | 0.0132 | 0.00688 | 0.0552 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: M72 Fibroblastic disorders | 0.0642 | 0.0338 | 0.0575 | Wald ratio | 1 | trans | NA |
| Eye problems or disorders: Diabetes related eye disease | 0.0605 | 0.0319 | 0.0578 | Wald ratio | 1 | trans | NA |
| _...and 54 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_40 association rows across 26 traits (35 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating PRELP levels | 3e-1687 | rs41313926 | 4 | GCST90859791 | no MR -> candidate analysis |
| Ankyrin-2 levels | 5e-265 | rs41313926 | 6 | GCST90246511 | no MR -> candidate analysis |
| OPTC protein levels | 4e-104 | rs10217817 | 2 | GCST90470128 | no MR -> candidate analysis |
| Ankyrin-2 levels (ANK2.7624.19.3) | 1e-91 | rs41313926 | 1 | GCST90240295 | no MR -> candidate analysis |
| Circulating OPTC levels | 5e-79 | rs3766907 | 1 | GCST90860578 | no MR -> candidate analysis |
| Keratocan levels | 5e-62 | rs879446 | 2 | GCST90248183 | no MR -> candidate analysis |
| CHIT1 protein levels | 2e-42 | rs544579097 | 4 | GCST90468744 | no MR -> candidate analysis |
| Potassium voltage-gated channel subfamily E regulatory beta  | 2e-39 | rs41313926 | 1 | GCST90249191 | no MR -> candidate analysis |
| PRELP protein levels | 5e-35 | rs74599912 | 1 | GCST90470321 | no MR -> candidate analysis |
| Prolow-density lipoprotein receptor-related protein 1 levels | 6e-31 | rs41313926 | 2 | GCST90421198 | no MR -> candidate analysis |
| Serum levels of protein KERA | 7e-30 | rs10920636 | 1 | GCST90086440 | no MR -> candidate analysis |
| Cerebrospinal fluid protein PRELP levels | 9e-27 | rs41313926 | 1 | GCST90944512 | no MR -> candidate analysis |
| _...and 14 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 210 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| osteoarthritis, hip | 0.509 | — | common-variant locus | no MR -> candidate analysis |
| cervical carcinoma | 0.393 | — | common-variant locus | no MR -> candidate analysis |
| ovarian neoplasm | 0.273 | — | common-variant locus | no MR -> candidate analysis |
| arthropathy | 0.192 | — | common-variant locus | no MR -> candidate analysis |
| liver disorder | 0.191 | — | common-variant locus | no MR -> candidate analysis |
| Abnormality of the skeletal system | 0.113 | — | common-variant locus | no MR -> candidate analysis |

> Of the 6 rows above, **6 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.00013, LOEUF=1.06 — LoF-tolerant |
| GWAS Catalog | 68 unique SNPs / 136 rows |
| ClinVar | 79 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 210 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'PRELP'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 79 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 26 traits by best p-value, aggregated from 40 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P51888 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000188783/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PRELP — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PRELP — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PRELP%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/PRELP — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:36:25  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
