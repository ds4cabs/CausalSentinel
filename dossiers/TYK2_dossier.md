# Protein Dossier — TYK2 (Non-receptor tyrosine-protein kinase TYK2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Myocardial infarction | -0.154 | 0.044 | 4.76e-04 | Wald ratio | 1 | trans | NA |
| Coronary heart disease | -0.133 | 0.0399 | 8.64e-04 | Wald ratio | 1 | trans | NA |
| Amyotrophic lateral sclerosis | -0.235 | 0.0722 | 0.00113 | Wald ratio | 1 | trans | NA |
| Eczema | 0.212 | 0.0705 | 0.00266 | Wald ratio | 1 | trans | NA |
| Years of schooling | -0.0471 | 0.0157 | 0.0027 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: N92 Excessive  frequent and irregular menstruation | 0.166 | 0.056 | 0.00297 | Wald ratio | 1 | trans | NA |
| Chronic kidney disease | 0.173 | 0.0627 | 0.00596 | Wald ratio | 1 | trans | NA |
| Forced vital capacity (FVC) | -0.0211 | 0.00776 | 0.00649 | Wald ratio | 1 | trans | NA |
| LDL cholesterol | -0.0592 | 0.022 | 0.00701 | Wald ratio | 1 | trans | NA |
| Sodium in urine | 0.0235 | 0.00931 | 0.0115 | Wald ratio | 1 | trans | NA |
| Heel bone mineral density (BMD) T-score  automated | 0.03 | 0.0122 | 0.0143 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: deep venous thrombosis (dvt) | -0.2 | 0.0826 | 0.0153 | Wald ratio | 1 | trans | NA |
| _...and 99 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-5260_80_3` | TYK2 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_237 association rows across 118 traits (222 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| IFNAR1 protein levels | 2e-83 | rs12720356 | 3 | GCST90469512 | no MR -> candidate analysis |
| Height | 4e-59 | rs6511696 | 3 | GCST90245848 | MR: beta=-0.0129, p=0.302 (trans) |
| Circulating ICAM3 levels | 3e-56 | rs4611572 | 3 | GCST90860465 | no MR -> candidate analysis |
| Platelet count | 3e-47 | rs34536443 | 6 | GCST90662907 | no MR -> candidate analysis |
| Low density lipoprotein cholesterol levels | 3e-45 | rs12720359 | 2 | GCST90239655 | no MR -> candidate analysis |
| BST2 protein levels | 1e-40 | rs12720356 | 2 | GCST90468475 | no MR -> candidate analysis |
| Platelet crit (UKB data field 30090) | 7e-39 | rs34536443 | 1 | GCST90468096 | no MR -> candidate analysis |
| Total cholesterol levels | 2e-38 | rs12720359 | 2 | GCST90239673 | no MR -> candidate analysis |
| IL12RB1 protein levels | 4e-38 | rs34536443 | 2 | GCST90469550 | no MR -> candidate analysis |
| Non-HDL cholesterol levels | 4e-37 | rs12720359 | 2 | GCST90239667 | no MR -> candidate analysis |
| Circulating IL12RB1 levels (id: OID00835_OID20486) | 8e-37 | rs34536443 | 2 | GCST90860161 | no MR -> candidate analysis |
| Circulating IL12RB1 levels (id: OID01019_OID20486) | 1e-36 | rs34536443 | 2 | GCST90860245 | no MR -> candidate analysis |
| _...and 106 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 948 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| rheumatoid arthritis | 0.931 | — | common-variant locus | no MR -> candidate analysis |
| immunodeficiency 35 | 0.864 | — | established (curated) | no MR -> candidate analysis |
| psoriasis | 0.93 | — | common-variant locus | MR: beta=0.093, p=0.256 (trans) |
| psoriasis vulgaris | 0.874 | — | common-variant locus | no MR -> candidate analysis |
| Crohn disease | 0.801 | — | common-variant locus | no MR -> candidate analysis |
| psoriatic arthritis | 0.692 | — | common-variant locus | no MR -> candidate analysis |
| COVID-19 | 0.914 | — | common-variant locus | no MR -> candidate analysis |
| systemic lupus erythematosus | 0.878 | — | common-variant locus | no MR -> candidate analysis |
| ulcerative colitis | 0.052 | — | common-variant locus | no MR -> candidate analysis |
| Autosomal recessive hyper-IgE syndrome due to TYK2 deficiency | 0.608 | — | established (curated) | no MR -> candidate analysis |
| hypothyroidism | 0.913 | — | common-variant locus | MR: beta=-0.0401, p=0.361 (trans) |
| type 1 diabetes mellitus | 0.858 | — | common-variant locus | no MR -> candidate analysis |
| autoimmune disease | 0.864 | — | common-variant locus | no MR -> candidate analysis |
| sarcoidosis | 0.827 | — | common-variant locus | no MR -> candidate analysis |
| skin disorder | 0.846 | — | common-variant locus | no MR -> candidate analysis |

> Of the 15 rows above, **13 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 8 known modulators (Non-receptor tyrosine-protein kinase TYK2) |
| gnomAD constraint | pLI=2.8e-07, LOEUF=0.611 — LoF-tolerant |
| GWAS Catalog | 158 unique SNPs / 394 rows |
| ClinVar | 1152 records; 3 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 948 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'TYK2' and resolved to 'Non-receptor tyrosine-protein kinase TYK2' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 1152 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 118 traits by best p-value, aggregated from 237 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P29597 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000105397/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3553/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/TYK2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/TYK2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=TYK2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/TYK2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:31:00  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
