# Protein Dossier — LHB (Lutropin subunit beta)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Creatinine (enzymatic) in urine | 0.0322 | 0.00991 | 0.00117 | Wald ratio | 1 | cis | NA |
| Fractured or broken bones in last 5 years | 0.0921 | 0.0295 | 0.00179 | Wald ratio | 1 | cis | NA |
| Age at menarche | 0.0783 | 0.0258 | 0.0024 | Wald ratio | 1 | cis | NA |
| Alcohol intake frequency | -0.0463 | 0.0153 | 0.0025 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: kidney stone or ureter stone or bladder stone | 0.271 | 0.0901 | 0.00266 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: prostate cancer | 0.263 | 0.0941 | 0.00519 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Other bones | 0.105 | 0.0406 | 0.00957 | Wald ratio | 1 | cis | NA |
| Potassium in urine | 0.027 | 0.0105 | 0.0103 | Wald ratio | 1 | cis | NA |
| Weight | 0.0229 | 0.00914 | 0.0121 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: C61 Malignant neoplasm of prostate | 0.25 | 0.1 | 0.0123 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: Z09 Follow-up examination after treatment for conditions other than malignant neoplasms | -0.26 | 0.111 | 0.019 | Wald ratio | 1 | cis | NA |
| Low grade serous ovarian cancer | 0.516 | 0.224 | 0.021 | Wald ratio | 1 | cis | NA |
| _...and 93 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_10 association rows across 9 traits (10 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Luteinizing hormone levels | 2e-187 | rs3795052 | 1 | GCST90248348 | no MR -> candidate analysis |
| Human Chorionic Gonadotropin levels | 2e-167 | rs113572723 | 1 | GCST90162185 | no MR -> candidate analysis |
| Human Chorionic Gonadotropin levels (CGA.CGB.4914.10.1) | 7e-100 | rs3795047 | 2 | GCST90241456 | no MR -> candidate analysis |
| Lutropin subunit beta levels | 2e-67 | rs144948359 | 1 | GCST90248342 | no MR -> candidate analysis |
| Luteinizing hormone levels (CGA.LHB.2953.31.2) | 7e-43 | rs3795047 | 1 | GCST90241825 | no MR -> candidate analysis |
| LHB protein levels | 9e-17 | rs3795050 | 1 | GCST90469767 | no MR -> candidate analysis |
| Circulating LHB levels | 7e-15 | rs3795051 | 1 | GCST90860326 | no MR -> candidate analysis |
| Bioavailable testosterone levels | 1e-10 | rs6521 | 1 | GCST90012103 | no MR -> candidate analysis |
| Free testosterone levels | 2e-8 | rs3795047 | 1 | GCST90239826 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 467 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| hypogonadotropic hypogonadism 23 with or without anosmia | 0.779 | — | established (curated) | no MR -> candidate analysis |
| Leydig cell hypoplasia due to LHB deficiency | 0.779 | — | established (curated) | no MR -> candidate analysis |
| hypogonadotropic hypogonadism | 0.195 | — | established (curated) | no MR -> candidate analysis |
| uterine disorder | 0.14 | — | common-variant locus | no MR -> candidate analysis |

> Of the 4 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 3 known modulators (Large envelope protein) |
| gnomAD constraint | pLI=9e-05, LOEUF=1.72 — LoF-tolerant |
| GWAS Catalog | 79 unique SNPs / 156 rows |
| ClinVar | 109 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 467 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'LHB' and resolved to 'Large envelope protein' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 109 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 9 of 9 traits by best p-value, aggregated from 10 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P01229 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000104826/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL1928/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/LHB — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/LHB — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=LHB%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/LHB — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:32:27  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
