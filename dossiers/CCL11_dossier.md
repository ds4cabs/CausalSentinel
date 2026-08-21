# Protein Dossier — CCL11 (Eotaxin)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Percent emphysema | -0.158 | 0.093 | 0.0892 | Wald ratio | 1 | trans | NA |
| Primary sclerosing cholangitis  | 0.238 | 0.153 | 0.12 | Wald ratio | 1 | trans | NA |
| Hirschsprung's disease | -1.66 | 1.14 | 0.147 | Wald ratio | 1 | trans | NA |
| Gallbladder cancer | 1.37 | 1.61 | 0.392 | Wald ratio | 1 | trans | NA |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-5301_7_3` | Eotaxin | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_29 association rows across 18 traits (26 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| CCL13/CCL8 protein level ratio | 9e-495 | rs11652256 | 1 | GCST90313676 | no MR -> candidate analysis |
| CCL13 protein levels | 7e-95 | rs1233650 | 1 | GCST90468565 | no MR -> candidate analysis |
| CCL8 protein levels | 1e-66 | rs184953165 | 7 | GCST90468586 | no MR -> candidate analysis |
| Circulating CCL11 levels (id: OID00505_OID20668) | 3e-61 | rs79722574 | 2 | GCST90859861 | no MR -> candidate analysis |
| Circulating CCL11 levels (id: OID00970_OID20668) | 5e-47 | rs79722574 | 2 | GCST90860201 | no MR -> candidate analysis |
| Circulating CCL7 levels (id: OID00474_OID20523) | 2e-42 | rs3091323 | 1 | GCST90859834 | no MR -> candidate analysis |
| Circulating CCL7 levels (id: OID00755_OID20523) | 4e-32 | rs3091323 | 1 | GCST90860091 | no MR -> candidate analysis |
| Blood protein levels | 2e-30 | rs2215184 | 1 | GCST010104 | no MR -> candidate analysis |
| C-C motif chemokine 7 levels | 3e-24 | rs16969454 | 1 | GCST90162169 | no MR -> candidate analysis |
| CCL7 protein levels | 2e-22 | rs1233653 | 2 | GCST90428425 | no MR -> candidate analysis |
| Circulating CCL13 levels (id: OID00504_OID20655) | 2e-21 | rs202247332 | 1 | GCST90859860 | no MR -> candidate analysis |
| Circulating CCL13 levels (id: OID00768_OID20655) | 2e-17 | rs202247332 | 1 | GCST90860103 | no MR -> candidate analysis |
| _...and 6 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 821 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| inflammatory bowel disease | 0.471 | — | common-variant locus | no MR -> candidate analysis |
| vertebral column disorder | 0.375 | — | common-variant locus | no MR -> candidate analysis |
| psoriasis | 0.26 | — | common-variant locus | no MR -> candidate analysis |
| hyperpituitarism | 0.244 | — | common-variant locus | no MR -> candidate analysis |
| ulcerative colitis | 0.089 | — | common-variant locus | no MR -> candidate analysis |
| Apnea | 0.137 | — | common-variant locus | no MR -> candidate analysis |
| Crohn disease | 0.111 | — | common-variant locus | no MR -> candidate analysis |
| colitis | 0.053 | — | common-variant locus | no MR -> candidate analysis |
| drug allergy | 0.117 | — | common-variant locus | no MR -> candidate analysis |

> Of the 9 rows above, **9 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 1 known modulators (Eotaxin) |
| gnomAD constraint | pLI=0.0027, LOEUF=1.81 — LoF-tolerant |
| GWAS Catalog | 104 unique SNPs / 212 rows |
| ClinVar | 41 records; 3 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 1 clinical annotations across 1 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 821 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'CCL11' and resolved to 'Eotaxin' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 41 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 18 of 18 traits by best p-value, aggregated from 29 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P51671 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000172156/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3286077/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CCL11 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CCL11 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CCL11%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=CCL11 — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CCL11 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:30:42  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
