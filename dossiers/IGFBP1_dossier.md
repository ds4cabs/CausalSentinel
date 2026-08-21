# Protein Dossier — IGFBP1 (Insulin-like growth factor-binding protein 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Triglycerides | 0.731 | 0.0217 | 6.50e-250 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: gout | 0.884 | 0.0548 | 1.38e-58 | Wald ratio | 1 | trans | NA |
| Total cholesterol | 0.326 | 0.0229 | 6.67e-46 | Wald ratio | 1 | trans | NA |
| Urate | 0.49 | 0.035 | 1.56e-44 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: high cholesterol | 0.398 | 0.0286 | 7.29e-44 | Wald ratio | 1 | trans | NA |
| Alcohol intake frequency | 0.294 | 0.0233 | 1.26e-36 | Wald ratio | 1 | trans | NA |
| Fasting glucose | -0.204 | 0.0197 | 5.57e-25 | Wald ratio | 1 | trans | NA |
| Crohn's disease | 0.73 | 0.0767 | 1.74e-21 | Wald ratio | 1 | trans | NA |
| Inflammatory bowel disease | 0.491 | 0.0635 | 1.03e-14 | Wald ratio | 1 | trans | NA |
| Sodium in urine | 0.119 | 0.0155 | 2.00e-14 | Wald ratio | 1 | trans | NA |
| Weight | -0.103 | 0.0139 | 1.05e-13 | Wald ratio | 1 | trans | NA |
| Serum creatinine (eGFRcrea) | 0.0433 | 0.00586 | 1.45e-13 | Wald ratio | 1 | trans | NA |
| _...and 135 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2771_35_2` | IGFBP-1 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_11 association rows across 8 traits (10 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Height | 2e-30 | rs1496496 | 1 | GCST90245848 | MR: beta=-0.127, p=2.62e-11 (trans) |
| IGFBP3 protein levels | 5e-29 | rs9658222 | 4 | GCST90469529 | no MR -> candidate analysis |
| Circulating IGFBP1 levels | 6e-26 | rs2331390 | 1 | GCST90859951 | no MR -> candidate analysis |
| IGFBP1 protein levels | 7e-14 | rs28705240 | 1 | GCST90469527 | no MR -> candidate analysis |
| Insulin-like growth factor-binding protein 1 levels | 1e-12 | rs10577484 | 1 | GCST90248010 | no MR -> candidate analysis |
| Myocardial infarction | 3e-8 | rs117054298 | 1 | GCST90018877 | no MR -> candidate analysis |
| Blood pressure (pleiotropy model 1 DBP adjusted for estimate | 4e-8 | rs10282088 | 1 | GCST90239828 | no MR -> candidate analysis |
| Blood pressure (pleiotropy model 2 SBP adjusted for estimate | 1e-7 | rs10282088 | 1 | GCST90239829 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 708 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Abnormality of the skeletal system | 0.147 | — | common-variant locus | no MR -> candidate analysis |
| cataract | 0.139 | — | common-variant locus | MR: beta=0.165, p=0.0247 (trans) |
| Epidermal Inclusion Cyst | 0.117 | — | common-variant locus | no MR -> candidate analysis |
| tenosynovitis | 0.117 | — | common-variant locus | no MR -> candidate analysis |
| senile cataract | 0.11 | — | common-variant locus | no MR -> candidate analysis |

> Of the 5 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Insulin-like growth factor-binding protein 1) |
| gnomAD constraint | pLI=1e-13, LOEUF=1.81 — LoF-tolerant |
| GWAS Catalog | 83 unique SNPs / 166 rows |
| ClinVar | 63 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 708 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'IGFBP1' and resolved to 'Insulin-like growth factor-binding protein 1' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 63 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 8 of 8 traits by best p-value, aggregated from 11 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P08833 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000146678/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4178/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/IGFBP1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/IGFBP1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=IGFBP1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/IGFBP1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:08:19  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
