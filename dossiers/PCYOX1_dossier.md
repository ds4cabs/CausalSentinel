# Protein Dossier — PCYOX1 (Prenylcysteine oxidase 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Body mass index (BMI) | 0.0154 | 0.00426 | 2.89e-04 | Wald ratio | 1 | cis | NA |
| Diastolic blood pressure  automated reading | 0.0144 | 0.00436 | 9.78e-04 | Wald ratio | 1 | cis | NA |
| Systolic blood pressure  automated reading | 0.0143 | 0.00436 | 0.001 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | -0.0111 | 0.00349 | 0.00146 | Wald ratio | 1 | cis | NA |
| Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.0368 | 0.0127 | 0.00361 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertension | 0.0204 | 0.00711 | 0.00406 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | 0.0158 | 0.00552 | 0.00415 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | -0.00912 | 0.00368 | 0.0134 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: Z09 Follow-up examination after treatment for conditions other than malignant neoplasms | 0.0791 | 0.032 | 0.0135 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R04 Haemorrhage from respiratory passages | 0.129 | 0.0522 | 0.0137 | Wald ratio | 1 | cis | NA |
| Amyotrophic lateral sclerosis | 0.0766 | 0.0314 | 0.0147 | Wald ratio | 1 | cis | NA |
| Depressive symptoms | 0.0152 | 0.00633 | 0.0164 | Wald ratio | 1 | cis | NA |
| _...and 110 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_29 association rows across 23 traits (28 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Prenylcysteine oxidase 1 levels | 4e-704 | rs2706762 | 3 | GCST90248900 | no MR -> candidate analysis |
| Serum levels of protein PCYOX1 | 2e-206 | rs2706762 | 1 | GCST90089422 | no MR -> candidate analysis |
| Serum levels of protein IAPP | 2e-127 | rs2706762 | 1 | GCST90089119 | no MR -> candidate analysis |
| Blood protein levels | 1e-121 | rs2706762 | 2 | GCST006585 | no MR -> candidate analysis |
| Flavin adenine dinucleotide (FAD) levels | 2e-91 | rs2706762 | 2 | GCST90200376 | no MR -> candidate analysis |
| PCYOX1 protein levels | 3e-77 | rs2706762 | 1 | GCST90453398 | no MR -> candidate analysis |
| Rho-related GTP-binding protein RhoB levels | 4e-33 | rs2706762 | 1 | GCST90249317 | no MR -> candidate analysis |
| LMNB2 protein levels | 1e-24 | rs2706762 | 1 | GCST90469782 | no MR -> candidate analysis |
| Thimet oligopeptidase protein levels (SomaScan ID:6431-68) | 7e-17 | rs2706762 | 1 | GCST90440544 | no MR -> candidate analysis |
| Liver enzyme levels (alkaline phosphatase) | 9e-16 | rs2706762 | 1 | GCST90013406 | no MR -> candidate analysis |
| Morning person | 4e-14 | rs2706762 | 1 | GCST007565 | no MR -> candidate analysis |
| Chronotype | 4e-14 | rs2706762 | 1 | GCST007576 | no MR -> candidate analysis |
| _...and 11 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 57 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| mathematical ability | 0.384 | — | common-variant locus | no MR -> candidate analysis |
| Hypercholesterolemia | 0.131 | — | common-variant locus | MR: beta=0.0205, p=0.033 (cis) |
| thyroid cancer | 0.047 | — | common-variant locus | MR: beta=0.173, p=0.229 (cis) |

> Of the 3 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=4.6e-16, LOEUF=1.27 — LoF-tolerant |
| GWAS Catalog | 43 unique SNPs / 86 rows |
| ClinVar | 99 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 57 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'PCYOX1'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 99 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 23 traits by best p-value, aggregated from 29 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9UHG3 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000116005/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PCYOX1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PCYOX1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PCYOX1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/PCYOX1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:13:52  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
