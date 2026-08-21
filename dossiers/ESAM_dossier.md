# Protein Dossier — ESAM (Endothelial cell-selective adhesion molecule)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Schizophrenia | 0.291 | 0.0515 | 1.50e-08 | Wald ratio | 1 | cis | NA |
| Diastolic blood pressure  automated reading | -0.0429 | 0.0121 | 4.07e-04 | Wald ratio | 1 | cis | NA |
| Systolic blood pressure  automated reading | -0.0401 | 0.0121 | 9.57e-04 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | 0.14 | 0.046 | 0.00241 | Wald ratio | 1 | cis | NA |
| PGC cross-disorder traits | 0.178 | 0.0587 | 0.00248 | Wald ratio | 1 | cis | NA |
| Sleep duration | -0.0256 | 0.00926 | 0.00571 | Wald ratio | 1 | cis | NA |
| Cough on most days | 0.145 | 0.0525 | 0.00574 | Wald ratio | 1 | cis | NA |
| Bipolar disorder | 0.313 | 0.115 | 0.0064 | Wald ratio | 1 | cis | NA |
| Years of schooling | 0.0425 | 0.017 | 0.0124 | Wald ratio | 1 | cis | NA |
| Sodium in urine | -0.0275 | 0.0117 | 0.0186 | Wald ratio | 1 | cis | NA |
| Large vessel disease | -0.384 | 0.167 | 0.0217 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: bone disorder | 0.402 | 0.176 | 0.0223 | Wald ratio | 1 | cis | NA |
| _...and 109 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2981_9_3` | ESAM | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_8 association rows across 8 traits (7 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Endothelial cell-selective adhesion molecule levels | 2e-120 | rs12792040 | 1 | GCST90247390 | no MR -> candidate analysis |
| Endothelial cell-selective adhesion molecule levels (ESAM.78 | 1e-28 | rs61753651 | 1 | GCST90241050 | no MR -> candidate analysis |
| Endothelial cell-selective adhesion molecule (analyte X20536 | 1e-22 | rs61753651 | 1 | GCST90423781 | no MR -> candidate analysis |
| Cerebrospinal fluid protein ESAM levels | 2e-22 | rs61753651 | 1 | GCST90944756 | no MR -> candidate analysis |
| Schizophrenia | 4e-13 | rs12541 | 1 | GCST90128471 | MR: beta=0.291, p=1.50e-08 (cis) |
| VSIG2 protein levels | 2e-12 | rs138993711 | 1 | GCST90471051 | no MR -> candidate analysis |
| Obesity class II and Anorexia nervosa or Schizophrenia | 1e-10 | rs1940171 | 1 | GCST90624556 | no MR -> candidate analysis |
| Reaction time | 4e-6 | rs12541 | 1 | GCST006268 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 236 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| neurodevelopmental disorder with intracranial hemorrhage, seizures, and spasticity | 0.789 | — | established (curated) | no MR -> candidate analysis |
| schizophrenia | 0.829 | — | common-variant locus | MR: beta=0.291, p=1.50e-08 (cis) |
| autism spectrum disorder | 0.607 | — | common-variant locus | no MR -> candidate analysis |
| anorexia nervosa | 0.566 | — | common-variant locus | no MR -> candidate analysis |
| irritable bowel syndrome | 0.534 | — | common-variant locus | no MR -> candidate analysis |
| attention deficit-hyperactivity disorder | 0.486 | — | common-variant locus | no MR -> candidate analysis |
| bipolar disorder | 0.486 | — | common-variant locus | MR: beta=0.313, p=0.0064 (cis) |
| major depressive disorder | 0.486 | — | common-variant locus | MR: beta=0.117, p=0.264 (cis) |
| Tourette syndrome | 0.486 | — | common-variant locus | no MR -> candidate analysis |
| intelligence | 0.486 | — | common-variant locus | no MR -> candidate analysis |
| obsessive-compulsive disorder | 0.486 | — | common-variant locus | no MR -> candidate analysis |
| preeclampsia | 0.451 | — | common-variant locus | no MR -> candidate analysis |
| obesity disorder | 0.32 | — | common-variant locus | no MR -> candidate analysis |
| post term pregnancy | 0.153 | — | common-variant locus | no MR -> candidate analysis |

> Of the 14 rows above, **11 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=2e-06, LOEUF=1.03 — LoF-tolerant |
| GWAS Catalog | 37 unique SNPs / 74 rows |
| ClinVar | 154 records; 6 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 236 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'ESAM'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 154 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 8 of 8 traits by best p-value, aggregated from 8 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q96AP7 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000149564/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/ESAM — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/ESAM — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=ESAM%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/ESAM — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:29:14  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
