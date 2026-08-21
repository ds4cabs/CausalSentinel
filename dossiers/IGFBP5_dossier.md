# Protein Dossier — IGFBP5 (Insulin-like growth factor-binding protein 5)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: kidney stone or ureter stone or bladder stone | 0.522 | 0.145 | 3.16e-04 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: joint disorder | 0.481 | 0.2 | 0.0161 | Wald ratio | 1 | cis | NA |
| Sleep duration | -0.0384 | 0.0165 | 0.0198 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K20 Oesophagitis | 0.357 | 0.153 | 0.02 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Other bones | -0.244 | 0.119 | 0.0405 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: C61 Malignant neoplasm of prostate | 0.367 | 0.187 | 0.0496 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: osteoporosis | 0.249 | 0.135 | 0.0647 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: G56 Mononeuropathies of upper limb | -0.815 | 0.453 | 0.0716 | Wald ratio | 1 | cis | NA |
| Eczema | 0.277 | 0.162 | 0.0863 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Ankle | 0.242 | 0.145 | 0.0959 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Wrist | 0.192 | 0.127 | 0.131 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: H25 Senile cataract | 0.282 | 0.189 | 0.137 | Wald ratio | 1 | cis | NA |
| _...and 42 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2685_21_2` | IGFBP-5 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_9 association rows across 9 traits (5 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Serum levels of protein IGFBP5 | 2e-48 | rs11575194 | 1 | GCST90088017 | no MR -> candidate analysis |
| Height | 2e-24 | rs11575134 | 1 | GCST90245848 | no MR -> candidate analysis |
| Oxysterol-binding protein-related protein 11 levels (OSBPL11 | 9e-12 | rs11575194 | 1 | GCST90242184 | no MR -> candidate analysis |
| Pulse pressure | 4e-10 | rs11575194 | 1 | GCST90310296 | no MR -> candidate analysis |
| Glycated hemoglobin levels | 2e-9 | rs10932672 | 1 | GCST90134495 | no MR -> candidate analysis |
| Visceral fat | 1e-7 | rs2241193 | 1 | GCST001525 | no MR -> candidate analysis |
| Metabolite levels | 5e-6 | rs9341226 | 1 | GCST009391 | no MR -> candidate analysis |
| Systolic blood pressure | 7e-6 | rs11575194 | 1 | GCST90310294 | MR: beta=0.0179, p=0.407 (cis) |
| Behenoyl dihydrosphingomyelin (d18:0/22:0) levels | 9e-6 | rs2067039 | 1 | GCST90503964 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 426 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| hypothyroidism | 0.534 | — | common-variant locus | MR: beta=0.096, p=0.264 (cis) |
| nodular goiter | 0.479 | — | common-variant locus | no MR -> candidate analysis |
| Incisional hernia | 0.465 | — | common-variant locus | no MR -> candidate analysis |
| hyperthyroidism | 0.447 | — | common-variant locus | MR: beta=-0.432, p=0.372 (cis) |
| thyrotoxicosis | 0.432 | — | common-variant locus | MR: beta=-0.432, p=0.372 (cis) |
| thyroid gland disorder | 0.398 | — | common-variant locus | no MR -> candidate analysis |
| cervical carcinoma | 0.372 | — | common-variant locus | no MR -> candidate analysis |
| nontoxic goiter | 0.365 | — | common-variant locus | no MR -> candidate analysis |
| coronary atherosclerosis | 0.308 | — | common-variant locus | no MR -> candidate analysis |
| Hashimoto thyroiditis | 0.307 | — | common-variant locus | no MR -> candidate analysis |
| autoimmune disease | 0.296 | — | common-variant locus | no MR -> candidate analysis |
| multinodular goiter | 0.28 | — | common-variant locus | no MR -> candidate analysis |
| Age-related cataract | 0.262 | — | common-variant locus | no MR -> candidate analysis |
| Abnormality of the skeletal system | 0.164 | — | common-variant locus | no MR -> candidate analysis |

> Of the 14 rows above, **11 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Insulin-like growth factor-binding protein 5) |
| gnomAD constraint | pLI=0.2, LOEUF=0.694 — LoF-tolerant |
| GWAS Catalog | 61 unique SNPs / 122 rows |
| ClinVar | 83 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 426 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'IGFBP5' and resolved to 'Insulin-like growth factor-binding protein 5' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 83 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 9 of 9 traits by best p-value, aggregated from 9 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P24593 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000115461/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2665/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/IGFBP5 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/IGFBP5 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=IGFBP5%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/IGFBP5 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:08:53  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
