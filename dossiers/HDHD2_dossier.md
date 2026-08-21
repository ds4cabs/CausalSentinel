# Protein Dossier — HDHD2 (Haloacid dehalogenase-like hydrolase domain-containing protein 2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Sodium in urine | 0.0176 | 0.00732 | 0.0164 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R11 Nausea and vomiting | 0.227 | 0.0954 | 0.0173 | Wald ratio | 1 | cis | NA |
| Weight | 0.0144 | 0.00657 | 0.028 | Wald ratio | 1 | cis | NA |
| Creatinine (enzymatic) in urine | 0.0154 | 0.00712 | 0.0311 | Wald ratio | 1 | cis | NA |
| Cough on most days | 0.0753 | 0.0353 | 0.0332 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R14 Flatulence and related conditions | 0.441 | 0.21 | 0.0357 | Wald ratio | 1 | cis | NA |
| Rheumatoid arthritis | 0.0964 | 0.0476 | 0.043 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code self-reported: pulmonary embolism (with or without) dvt | 0.144 | 0.0719 | 0.0456 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: diverticular disease or diverticulitis | 0.124 | 0.0624 | 0.0464 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: Z09 Follow-up examination after treatment for conditions other than malignant neoplasms | 0.108 | 0.0545 | 0.0468 | Wald ratio | 1 | cis | NA |
| Bulimia nervosa | 0.0442 | 0.0228 | 0.0527 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: deep venous thrombosis (dvt) | 0.092 | 0.0482 | 0.0564 | Wald ratio | 1 | cis | NA |
| _...and 61 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_14 association rows across 10 traits (7 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Serum levels of protein HDHD2 | 5e-133 | rs78720782 | 1 | GCST90087461 | no MR -> candidate analysis |
| Height | 1e-30 | rs3809966 | 2 | GCST90245848 | no MR -> candidate analysis |
| GLIPR1 protein levels | 1e-12 | rs188778473 | 1 | GCST90469357 | no MR -> candidate analysis |
| Bioavailable testosterone levels | 1e-11 | rs561968051 | 1 | GCST90012104 | no MR -> candidate analysis |
| Haloacid dehalogenase-like hydrolase domain-containing prote | 3e-11 | rs118090589 | 1 | GCST90422159 | no MR -> candidate analysis |
| P-selectin glycoprotein ligand 1 levels | 4e-11 | rs143459388 | 1 | GCST90012046 | no MR -> candidate analysis |
| Femur bone mineral density x serum urate levels interaction | 2e-9 | rs140964667 | 1 | GCST012490 | no MR -> candidate analysis |
| Vaginal microbiome relative abundance (c_Gammaproteobacteria | 2e-6 | rs115747623 | 3 | GCST90026665 | no MR -> candidate analysis |
| Sitting height ratio | 4e-6 | rs16958432 | 2 | GCST002843 | no MR -> candidate analysis |
| Response to paliperidone in schizophrenia (Multivariate) | 7e-6 | rs76297747 | 1 | GCST004043 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 35 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Abnormality of the skeletal system | 0.065 | — | common-variant locus | no MR -> candidate analysis |
| Abnormal urine sodium concentration | 0.062 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.053 | — | common-variant locus | no MR -> candidate analysis |
| ankylosing spondylitis | 0.039 | — | common-variant locus | no MR -> candidate analysis |
| urolithiasis | 0.033 | — | common-variant locus | no MR -> candidate analysis |
| stomach disorder | 0.031 | — | common-variant locus | no MR -> candidate analysis |

> Of the 6 rows above, **6 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=6.8e-10, LOEUF=1.45 — LoF-tolerant |
| GWAS Catalog | 48 unique SNPs / 96 rows |
| ClinVar | 95 records; 3 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 35 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'HDHD2'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 95 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 10 of 10 traits by best p-value, aggregated from 14 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9H0R4 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000167220/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/HDHD2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/HDHD2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=HDHD2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/HDHD2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:59:31  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
