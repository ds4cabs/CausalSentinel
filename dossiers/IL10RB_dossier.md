# Protein Dossier — IL10RB (Interleukin-10 receptor subunit beta)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: retinal detachment | 0.613 | 0.17 | 3.04e-04 | Wald ratio | 1 | cis | NA |
| Urate | 0.119 | 0.0419 | 0.00457 | Wald ratio | 1 | cis | NA |
| Mean cell volume | 0.575 | 0.228 | 0.0115 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K60 Fissure and fistula of anal and rectal regions | 0.431 | 0.173 | 0.0128 | Wald ratio | 1 | cis | NA |
| Pulse rate | -0.0754 | 0.0307 | 0.0139 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: asthma | 0.102 | 0.044 | 0.0201 | Wald ratio | 1 | cis | NA |
| Thalamus volume | 94.3 | 44.1 | 0.0326 | Wald ratio | 1 | cis | NA |
| Endometrioid ovarian cancer | -0.51 | 0.241 | 0.0342 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R07 Pain in throat and chest | 0.142 | 0.0675 | 0.0354 | Wald ratio | 1 | cis | NA |
| Ovarian cancer | -0.229 | 0.112 | 0.0416 | Wald ratio | 1 | cis | NA |
| High grade serous ovarian cancer | -0.265 | 0.133 | 0.0474 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | -0.0292 | 0.015 | 0.0515 | Wald ratio | 1 | cis | NA |
| _...and 80 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2631_50_2` | IL-10 Rb | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_88 association rows across 45 traits (80 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| BTN2A1/IL10RB protein level ratio | 3e-2884 | rs765429 | 1 | GCST90313544 | no MR -> candidate analysis |
| IFNGR1/IL10RB protein level ratio | 8e-2593 | rs765429 | 1 | GCST90315127 | no MR -> candidate analysis |
| Circulating IL10RB levels | 3e-2001 | rs2266590 | 2 | GCST90859871 | no MR -> candidate analysis |
| HYOU1/IL10RB protein level ratio | 6e-1956 | rs765429 | 1 | GCST90315101 | no MR -> candidate analysis |
| CSF1/IL10RB protein level ratio | 4e-1932 | rs765429 | 1 | GCST90314284 | no MR -> candidate analysis |
| B4GALT1/IL10RB protein level ratio | 2e-1735 | rs765429 | 1 | GCST90313431 | no MR -> candidate analysis |
| CD58/IL10RB protein level ratio | 2e-1672 | rs765429 | 1 | GCST90313850 | no MR -> candidate analysis |
| Interleukin-10 receptor subunit beta levels | 4e-316 | rs2266590 | 5 | GCST90274797 | no MR -> candidate analysis |
| Cerebrospinal fluid protein IL10RB levels | 7e-138 | rs2843717 | 1 | GCST90944362 | no MR -> candidate analysis |
| IFNAR1 protein levels | 9e-85 | rs62654645 | 5 | GCST90469512 | no MR -> candidate analysis |
| IL10RB protein levels | 1e-77 | rs370410755 | 10 | GCST90469545 | no MR -> candidate analysis |
| IFNGR2 protein levels | 1e-57 | rs193235943 | 4 | GCST90469514 | no MR -> candidate analysis |
| _...and 33 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 483 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| inflammatory bowel disease 25 | 0.915 | — | established (curated) | no MR -> candidate analysis |
| Autosomal recessive early-onset inflammatory bowel disease | 0.608 | — | established (curated) | no MR -> candidate analysis |
| IL10-related early-onset inflammatory bowel disease | 0.608 | — | established (curated) | no MR -> candidate analysis |
| COVID-19 | 0.755 | — | common-variant locus | no MR -> candidate analysis |
| obesity disorder | 0.389 | — | common-variant locus | no MR -> candidate analysis |
| major depressive disorder | 0.34 | — | common-variant locus | MR: beta=0.13, p=0.41 (cis) |
| hereditary disease | 0.314 | — | established (curated) | no MR -> candidate analysis |
| osteoarthritis | 0.277 | — | common-variant locus | MR: beta=0.0627, p=0.252 (cis) |
| respiratory failure | 0.261 | — | common-variant locus | no MR -> candidate analysis |
| systemic lupus erythematosus | 0.241 | — | common-variant locus | MR: beta=-0.35, p=0.291 (cis) |
| age-related macular degeneration | 0.166 | — | common-variant locus | no MR -> candidate analysis |

> Of the 11 rows above, **8 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 1 known modulators (IL22 Receptor) |
| gnomAD constraint | pLI=1.2e-08, LOEUF=1.05 — LoF-tolerant |
| GWAS Catalog | 101 unique SNPs / 212 rows |
| ClinVar | 361 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 483 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'IL10RB' and resolved to 'IL22 Receptor' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 361 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 45 traits by best p-value, aggregated from 88 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q08334 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000243646/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4804251/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/IL10RB — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/IL10RB — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=IL10RB%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/IL10RB — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:09:54  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
