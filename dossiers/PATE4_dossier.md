# Protein Dossier — PATE4 (Prostate and testis expressed protein 4)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| HOMA-IR | -0.0353 | 0.00892 | 7.70e-05 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | -0.0171 | 0.00454 | 1.69e-04 | Wald ratio | 1 | cis | NA |
| HOMA-B | -0.0228 | 0.00726 | 0.00167 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: ankylosing spondylitis | 0.251 | 0.0821 | 0.00224 | Wald ratio | 1 | cis | NA |
| Age at menarche | -0.0394 | 0.0129 | 0.0023 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Other bones | -0.0781 | 0.026 | 0.0027 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: D25 Leiomyoma of uterus | -0.173 | 0.0583 | 0.00302 | Wald ratio | 1 | cis | NA |
| Fractured or broken bones in last 5 years | -0.0486 | 0.0181 | 0.00733 | Wald ratio | 1 | cis | NA |
| Vascular or heart problems diagnosed by doctor: Angina | 0.0762 | 0.0288 | 0.00804 | Wald ratio | 1 | cis | NA |
| Primary sclerosing cholangitis  | -0.179 | 0.0706 | 0.0113 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: C50 Malignant neoplasm of breast | 0.0954 | 0.0394 | 0.0154 | Wald ratio | 1 | cis | NA |
| 2hr glucose | 0.0996 | 0.0415 | 0.0164 | Wald ratio | 1 | cis | NA |
| _...and 80 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_6 association rows across 6 traits (4 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Prostate and testis expressed protein 4 levels | 6e-77 | rs875500 | 1 | GCST90248859 | no MR -> candidate analysis |
| Prostate and testis expressed protein 4 levels (PATE4.8065.2 | 1e-75 | rs875500 | 1 | GCST90242405 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 3e-13 | rs10893443 | 1 | GCST90838669 | no MR -> candidate analysis |
| Physical function (baseline) | 4e-9 | rs11220256 | 1 | GCST90565837 | no MR -> candidate analysis |
| Astrocytoma (high-grade) | 6e-6 | rs118098308 | 1 | GCST90296478 | no MR -> candidate analysis |
| Itch intensity from mosquito bite adjusted by bite size | 9e-6 | rs11220237 | 1 | GCST004862 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 26 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| stroke disorder | 0.342 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.342 | — | common-variant locus | no MR -> candidate analysis |
| ovarian neoplasm | 0.335 | — | common-variant locus | no MR -> candidate analysis |
| tongue cancer | 0.062 | — | common-variant locus | no MR -> candidate analysis |

> Of the 4 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1.4e-06, LOEUF=2.43 — LoF-tolerant |
| GWAS Catalog | 15 unique SNPs / 30 rows |
| ClinVar | 83 records; 13 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 26 of 26 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'PATE4'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 83 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 6 of 6 traits by best p-value, aggregated from 6 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P0C8F1 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000237353/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PATE4 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PATE4 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PATE4%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/PATE4 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:11:32  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
