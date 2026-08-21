# Protein Dossier — FABP1 (Fatty acid-binding protein, liver)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: K44 Diaphragmatic hernia | 0.229 | 0.0877 | 0.00894 | Wald ratio | 1 | cis | NA |
| Major depressive disorder | -0.283 | 0.118 | 0.0165 | Wald ratio | 1 | cis | NA |
| Birth weight | -0.0483 | 0.021 | 0.0214 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hayfever or allergic rhinitis | 0.11 | 0.0504 | 0.0299 | Wald ratio | 1 | cis | NA |
| Paget's disease | -0.719 | 0.333 | 0.0306 | Wald ratio | 1 | cis | NA |
| Nucleus accumbens volume | 12.4 | 6.02 | 0.0398 | Wald ratio | 1 | cis | NA |
| Bipolar disorder | 0.254 | 0.131 | 0.0526 | Wald ratio | 1 | cis | NA |
| Mean platelet volume | 0.011 | 0.00577 | 0.0563 | Wald ratio | 1 | cis | NA |
| Height | -0.0304 | 0.0163 | 0.0613 | Wald ratio | 1 | cis | NA |
| Cough on most days | 0.113 | 0.0625 | 0.0697 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: psoriasis | 0.194 | 0.107 | 0.0712 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: depression | -0.113 | 0.0632 | 0.075 | Wald ratio | 1 | cis | NA |
| _...and 82 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_59 association rows across 37 traits (54 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| FABP1/RBP2 protein level ratio | 1e-591 | rs2241883 | 1 | GCST90314753 | no MR -> candidate analysis |
| FABP1/FABP2 protein level ratio | 6e-551 | rs2241883 | 1 | GCST90314750 | no MR -> candidate analysis |
| FABP1/LGALS4 protein level ratio | 3e-374 | rs2241883 | 1 | GCST90314752 | no MR -> candidate analysis |
| FABP1/SULT2A1 protein level ratio | 8e-332 | rs2241883 | 1 | GCST90314755 | no MR -> candidate analysis |
| FABP1/RBP5 protein level ratio | 1e-328 | rs2241883 | 1 | GCST90314754 | no MR -> candidate analysis |
| FABP1/HNMT protein level ratio | 3e-273 | rs2241883 | 1 | GCST90314751 | no MR -> candidate analysis |
| FABP1 protein levels | 9e-265 | rs2241883 | 1 | GCST90469173 | no MR -> candidate analysis |
| Fatty acid-binding protein, liver levels | 6e-43 | rs2241883 | 4 | GCST90247553 | no MR -> candidate analysis |
| Serum levels of protein FABP1 | 9e-40 | rs1545223 | 1 | GCST90086776 | no MR -> candidate analysis |
| Total bilirubin levels | 5e-35 | rs2241883 | 3 | GCST90662900 | no MR -> candidate analysis |
| Alkaline phosphatase (UKB data field 30610) | 6e-28 | rs2919872 | 1 | GCST90468060 | no MR -> candidate analysis |
| Liver enzyme levels (alkaline phosphatase) | 1e-26 | rs2919872 | 1 | GCST90013406 | no MR -> candidate analysis |
| _...and 25 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 469 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| non-melanoma skin carcinoma | 0.109 | — | common-variant locus | no MR -> candidate analysis |
| basal cell carcinoma | 0.1 | — | common-variant locus | MR: beta=-0.208, p=0.255 (cis) |
| skin cancer | 0.099 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Fatty acid-binding protein, liver) |
| gnomAD constraint | pLI=4e-05, LOEUF=1.51 — LoF-tolerant |
| GWAS Catalog | 28 unique SNPs / 56 rows |
| ClinVar | 41 records; 4 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 1 clinical annotations across 1 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 469 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'FABP1' and resolved to 'Fatty acid-binding protein, liver' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 41 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 20 of 37 traits by best p-value, aggregated from 59 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P07148 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000163586/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL5421/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/FABP1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/FABP1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=FABP1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=FABP1 — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/FABP1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:32:21  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
