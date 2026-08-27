# Protein Dossier — SPINT3 (Kunitz-type protease inhibitor 3)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: hypertension | -0.0232 | 0.00774 | 0.00269 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R35 Polyuria | 0.174 | 0.0599 | 0.00376 | Wald ratio | 1 | cis | NA |
| Parkinson's disease | 0.199 | 0.0756 | 0.00844 | Wald ratio | 1 | cis | NA |
| Endometrioid ovarian cancer | -0.122 | 0.0529 | 0.0209 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I48 Atrial fibrillation and flutter | -0.102 | 0.0466 | 0.029 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K35 Acute appendicitis | 0.12 | 0.0567 | 0.0341 | Wald ratio | 1 | cis | NA |
| 2hr glucose | 0.07 | 0.0331 | 0.0348 | Wald ratio | 1 | cis | NA |
| Ovarian cancer | -0.0504 | 0.0243 | 0.0386 | Wald ratio | 1 | cis | NA |
| Height | 0.0107 | 0.00534 | 0.0455 | Wald ratio | 1 | cis | NA |
| Cough on most days | 0.0433 | 0.0218 | 0.0469 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: bladder problem (not cancer) | -0.133 | 0.0667 | 0.047 | Wald ratio | 1 | cis | NA |
| Childhood intelligence | 0.046 | 0.0236 | 0.0508 | Wald ratio | 1 | cis | NA |
| _...and 90 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_26 association rows across 21 traits (25 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Kunitz-type protease inhibitor 3 levels | 1e-155 | rs6032259 | 2 | GCST90248217 | no MR -> candidate analysis |
| Kunitz-type protease inhibitor 3 levels (SPINT3.7926.13.3) | 6e-127 | rs6017591 | 1 | GCST90241719 | no MR -> candidate analysis |
| Serum levels of protein SPINT3 | 7e-118 | rs6032259 | 1 | GCST90089929 | no MR -> candidate analysis |
| Blood protein levels | 3e-76 | rs13042504 | 1 | GCST006585 | no MR -> candidate analysis |
| SPINT3 protein levels | 2e-73 | rs6073773 | 2 | GCST90470729 | no MR -> candidate analysis |
| WFDC12 protein levels | 8e-29 | rs17346952 | 1 | GCST90471073 | no MR -> candidate analysis |
| CD40 protein levels | 4e-18 | rs8115500 | 1 | GCST90468633 | no MR -> candidate analysis |
| Kunitz-type protease inhibitor 3 level in Chronic kidney dis | 8e-17 | rs6032259 | 1 | GCST90238714 | no MR -> candidate analysis |
| Stem cell factor levels | 2e-14 | rs6032254 | 1 | GCST90428432 | no MR -> candidate analysis |
| Concentration of small HDL particles | 7e-14 | rs117459421 | 1 | GCST90092951 | no MR -> candidate analysis |
| Cholesteryl ester levels in small HDL | 1e-13 | rs117459421 | 1 | GCST90092946 | no MR -> candidate analysis |
| Saturated fatty acids levels | 5e-13 | rs145184355 | 2 | GCST90502194 | no MR -> candidate analysis |
| _...and 9 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 9 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| placental retention | 0.301 | — | common-variant locus | no MR -> candidate analysis |
| bladder exstrophy | 0.195 | — | established (curated) | no MR -> candidate analysis |
| thyroiditis | 0.035 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.014, LOEUF=2.79 — LoF-tolerant |
| GWAS Catalog | 55 unique SNPs / 110 rows |
| ClinVar | 30 records; 10 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 9 of 9 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'SPINT3'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 30 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 21 traits by best p-value, aggregated from 26 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P49223 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000101446/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/SPINT3 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/SPINT3 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=SPINT3%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/SPINT3 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:13:09  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
