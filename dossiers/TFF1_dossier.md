# Protein Dossier — TFF1 (Trefoil factor 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: vitiligo | 1.17 | 0.265 | 1.04e-05 | Wald ratio | 1 | cis | NA |
| Birth weight | -0.0576 | 0.02 | 0.0039 | Wald ratio | 1 | cis | NA |
| Hippocampus volume | -71.5 | 25.4 | 0.00484 | Wald ratio | 1 | cis | NA |
| Pulse rate | 0.056 | 0.0228 | 0.0142 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Injury or trauma resulting in loss of vision | 0.307 | 0.126 | 0.015 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hayfever or allergic rhinitis | 0.114 | 0.0476 | 0.0172 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R10 Abdominal and pelvic pain | -0.166 | 0.0743 | 0.0255 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: iron deficiency anaemia | 0.265 | 0.139 | 0.0578 | Wald ratio | 1 | cis | NA |
| ER-negative Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.119 | 0.0653 | 0.0678 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: L03 Cellulitis | 0.213 | 0.118 | 0.0722 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I48 Atrial fibrillation and flutter | -0.285 | 0.169 | 0.091 | Wald ratio | 1 | cis | NA |
| Rheumatoid arthritis | 0.138 | 0.084 | 0.0999 | Wald ratio | 1 | cis | NA |
| _...and 57 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_19 association rows across 13 traits (18 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| TFF1/TFF2 protein level ratio | 3e-514 | rs184432 | 1 | GCST90315914 | no MR -> candidate analysis |
| Trefoil factor 1 levels | 5e-111 | rs3761376 | 4 | GCST90249813 | no MR -> candidate analysis |
| Circulating TFF2 levels | 1e-90 | rs225344 | 3 | GCST90860338 | no MR -> candidate analysis |
| Serum levels of protein TFF1 | 1e-75 | rs3761376 | 1 | GCST90090541 | no MR -> candidate analysis |
| TFF1 protein levels | 2e-55 | rs117389225 | 2 | GCST90470835 | no MR -> candidate analysis |
| Blood protein levels | 6e-42 | rs3761376 | 1 | GCST006585 | no MR -> candidate analysis |
| TFF3 protein levels | 5e-35 | rs4920094 | 1 | GCST90470837 | no MR -> candidate analysis |
| Trefoil factor 1 levels (TFF1.9185.15.3) | 4e-14 | rs3761376 | 1 | GCST90243108 | no MR -> candidate analysis |
| TFF2 protein levels | 1e-13 | rs12626926 | 1 | GCST90470836 | no MR -> candidate analysis |
| Pancreatic cancer | 4e-13 | rs1547374 | 1 | GCST001350 | no MR -> candidate analysis |
| Cerebrospinal fluid protein TFF1 levels | 3e-12 | rs3761376 | 1 | GCST90944910 | no MR -> candidate analysis |
| Thyroid stimulating hormone levels | 4e-8 | rs178740 | 1 | GCST90572789 | no MR -> candidate analysis |
| _...and 1 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 315 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| exocrine pancreatic carcinoma | 0.236 | — | common-variant locus | no MR -> candidate analysis |

> Of the 1 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.00091, LOEUF=1.87 — LoF-tolerant |
| GWAS Catalog | 69 unique SNPs / 138 rows |
| ClinVar | 113 records; 14 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 315 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'TFF1'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 113 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 13 of 13 traits by best p-value, aggregated from 19 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P04155 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000160182/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/TFF1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/TFF1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=TFF1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/TFF1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:19:26  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
