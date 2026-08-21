# Protein Dossier — HTATIP2 (Protein HTATIP2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Height | -0.0194 | 0.00537 | 3.05e-04 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: sleep apnoea | 0.197 | 0.066 | 0.00291 | Wald ratio | 1 | trans | NA |
| Birth weight | -0.0179 | 0.00657 | 0.00639 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: N81 Female genital prolapse | -0.111 | 0.0415 | 0.00744 | Wald ratio | 1 | trans | NA |
| Body mass index (BMI) | 0.0116 | 0.00443 | 0.00908 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: osteoporosis | -0.0805 | 0.0386 | 0.0372 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: bladder problem (not cancer) | 0.109 | 0.0523 | 0.0373 | Wald ratio | 1 | trans | NA |
| Cancer code  self-reported: malignant melanoma | -0.116 | 0.0567 | 0.0403 | Wald ratio | 1 | trans | NA |
| ER-negative Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | 0.0419 | 0.0206 | 0.0417 | Wald ratio | 1 | trans | NA |
| Years of schooling | -0.0149 | 0.00746 | 0.0455 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: retinal detachment | 0.134 | 0.0679 | 0.0483 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: polio  or  poliomyelitis | 0.255 | 0.134 | 0.0569 | Wald ratio | 1 | trans | NA |
| _...and 79 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_37 association rows across 26 traits (21 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Oxidoreductase HTATIP2 levels | 1e-1325 | rs10437608 | 2 | GCST90248807 | no MR -> candidate analysis |
| Bone mineral density mean | 1e-300 | rs79753040 | 2 | GCST90321120 | no MR -> candidate analysis |
| Height | 1e-27 | rs11025443 | 6 | GCST90245848 | MR: beta=-0.0194, p=3.05e-04 (trans) |
| Severe COVID-19 infection | 6e-17 | rs11025535 | 3 | GCST90255357 | no MR -> candidate analysis |
| Height (baseline) | 5e-13 | rs35081743 | 1 | GCST90565843 | no MR -> candidate analysis |
| Response to inhaled glucocorticoid treatment in asthma (chan | 6e-11 | rs1353649 | 1 | GCST002754 | no MR -> candidate analysis |
| Free Cholesterol to Cholesteryl Esters in Large HDL ratio | 4e-10 | rs117384644 | 1 | GCST90827800 | no MR -> candidate analysis |
| Gut microbial network clusters (Salmon (at 1 year) x Househo | 2e-9 | rs11826915 | 1 | GCST90569475 | no MR -> candidate analysis |
| Physical function (baseline) | 2e-8 | rs35081743 | 1 | GCST90565837 | no MR -> candidate analysis |
| Cerebrospinal fluid t-tau:AB1-42 ratio | 3e-8 | rs7129826 | 1 | GCST004490 | no MR -> candidate analysis |
| Gut microbiome abundance (class Collinsella sp. 3 (at 1 year | 3e-8 | rs34236148 | 1 | GCST90568927 | no MR -> candidate analysis |
| Fractional shortening | 4e-8 | rs11025521 | 1 | GCST006029 | no MR -> candidate analysis |
| _...and 14 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 145 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| COVID-19 | 0.557 | — | common-variant locus | no MR -> candidate analysis |
| severe acute respiratory syndrome | 0.557 | — | common-variant locus | no MR -> candidate analysis |
| liver disorder | 0.425 | — | common-variant locus | no MR -> candidate analysis |
| placental abruption | 0.425 | — | common-variant locus | no MR -> candidate analysis |
| injury | 0.053 | — | common-variant locus | MR: beta=-0.174, p=0.198 (trans) |
| atrial fibrillation | 0.05 | — | common-variant locus | MR: beta=-0.0479, p=0.278 (trans) |
| response to glucocorticoid | 0.049 | — | common-variant locus | no MR -> candidate analysis |

> Of the 7 rows above, **5 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=6.2e-10, LOEUF=1.46 — LoF-tolerant |
| GWAS Catalog | 40 unique SNPs / 74 rows |
| ClinVar | 69 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 145 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'HTATIP2'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 69 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 26 traits by best p-value, aggregated from 37 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9BUP3 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000109854/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/HTATIP2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/HTATIP2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=HTATIP2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/HTATIP2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:03:47  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
