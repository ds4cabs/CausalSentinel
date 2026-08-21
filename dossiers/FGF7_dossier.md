# Protein Dossier — FGF7 (Fibroblast growth factor 7)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Fracture resulting from simple fall | -0.0868 | 0.0385 | 0.0242 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: R55 Syncope and collapse | 0.246 | 0.112 | 0.0283 | Wald ratio | 1 | trans | NA |
| Body mass index (BMI) | 0.028 | 0.0133 | 0.036 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: retinal detachment | 0.345 | 0.17 | 0.0427 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | 0.247 | 0.127 | 0.0511 | Wald ratio | 1 | trans | NA |
| Alzheimer's disease | -0.164 | 0.0873 | 0.0606 | Wald ratio | 1 | trans | NA |
| Sleep duration | -0.0195 | 0.0104 | 0.0609 | Wald ratio | 1 | trans | NA |
| Cancer code  self-reported: basal cell carcinoma | 0.213 | 0.114 | 0.0621 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: R35 Polyuria | 0.29 | 0.165 | 0.0796 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: pernicious anaemia | 0.319 | 0.186 | 0.0867 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: osteoporosis | -0.236 | 0.139 | 0.0888 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: M16 Coxarthrosis [arthrosis of hip] | -0.245 | 0.146 | 0.0926 | Wald ratio | 1 | trans | NA |
| _...and 68 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-4487_1_1` | FGF7 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_22 association rows across 14 traits (21 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Nontoxic multinodular goiter (PheCode 241.2) | 2e-104 | rs4338740 | 3 | GCST90479861 | no MR -> candidate analysis |
| TG protein levels | 1e-36 | rs4338740 | 1 | GCST90470851 | no MR -> candidate analysis |
| Circulating TSHB levels | 5e-34 | rs10519226 | 1 | GCST90860403 | no MR -> candidate analysis |
| Nontoxic nodular goiter (PheCode 241) | 4e-29 | rs4338740 | 1 | GCST90475637 | no MR -> candidate analysis |
| Simple and unspecified goiter (PheCode 240) | 3e-26 | rs12592277 | 2 | GCST90479859 | no MR -> candidate analysis |
| Lung adenocarcinoma | 3e-14 | rs71467682 | 2 | GCST90297562 | MR: beta=0.116, p=0.44 (trans) |
| Creatinine levels (UKB data field 30700) | 6e-14 | rs28375625 | 1 | GCST90468067 | no MR -> candidate analysis |
| Thyroid volume | 3e-13 | rs4338740 | 2 | GCST001069 | no MR -> candidate analysis |
| Circulating GAL levels | 1e-12 | rs11639111 | 1 | GCST90860395 | no MR -> candidate analysis |
| Hyperthyroidism | 3e-12 | rs4338740 | 2 | GCST90018860 | MR: beta=0.174, p=0.191 (trans) |
| Thyroid hormone levels | 1e-11 | rs10519227 | 2 | GCST001856 | no MR -> candidate analysis |
| Hypothyroidism | 3e-10 | rs200066768 | 2 | GCST90627749 | no MR -> candidate analysis |
| _...and 2 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1982 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| hypothyroidism | 0.719 | — | common-variant locus | no MR -> candidate analysis |
| goiter | 0.681 | — | common-variant locus | no MR -> candidate analysis |
| multinodular goiter | 0.649 | — | common-variant locus | no MR -> candidate analysis |
| thyrotoxicosis | 0.631 | — | common-variant locus | MR: beta=0.174, p=0.191 (trans) |
| nontoxic goiter | 0.564 | — | common-variant locus | no MR -> candidate analysis |
| toxic multinodular goitre | 0.543 | — | common-variant locus | no MR -> candidate analysis |
| basal cell carcinoma | 0.469 | — | common-variant locus | MR: beta=0.213, p=0.0621 (trans) |
| asthma | 0.443 | — | common-variant locus | MR: beta=0.0308, p=0.396 (trans) |
| oral cavity cancer | 0.423 | — | common-variant locus | no MR -> candidate analysis |
| human papilloma virus infection | 0.423 | — | common-variant locus | no MR -> candidate analysis |
| irritable bowel syndrome | 0.365 | — | common-variant locus | no MR -> candidate analysis |
| hyperthyroidism | 0.333 | — | common-variant locus | MR: beta=0.174, p=0.191 (trans) |
| thyroid gland disorder | 0.305 | — | common-variant locus | no MR -> candidate analysis |
| Graves disease | 0.224 | — | common-variant locus | no MR -> candidate analysis |
| nodular goiter | 0.211 | — | common-variant locus | no MR -> candidate analysis |

> Of the 15 rows above, **11 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Fibroblast growth factor 7) |
| gnomAD constraint | pLI=0.9, LOEUF=0.577 — LoF-INTOLERANT |
| GWAS Catalog | 52 unique SNPs / 101 rows |
| ClinVar | 47 records; 6 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1982 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'FGF7' and resolved to 'Fibroblast growth factor 7' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 47 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 14 of 14 traits by best p-value, aggregated from 22 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P21781 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000140285/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3286071/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/FGF7 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/FGF7 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=FGF7%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/FGF7 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:40:09  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
