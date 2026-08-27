# Protein Dossier — ACP5 (Tartrate-resistant acid phosphatase type 5)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Paget's disease | -0.584 | 0.175 | 8.52e-04 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: osteoporosis | 0.166 | 0.0516 | 0.00132 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I84 Haemorrhoids | 0.118 | 0.0433 | 0.00623 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | -0.101 | 0.0373 | 0.00694 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | -0.0262 | 0.00979 | 0.00744 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypopituitarism | 0.554 | 0.255 | 0.0299 | Wald ratio | 1 | cis | NA |
| Sodium in urine | 0.016 | 0.00745 | 0.032 | Wald ratio | 1 | cis | NA |
| Creatinine (enzymatic) in urine | 0.015 | 0.00724 | 0.038 | Wald ratio | 1 | cis | NA |
| Ischemic stroke | -0.103 | 0.0499 | 0.0388 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: emphysema or chronic bronchitis | -0.157 | 0.0771 | 0.0421 | Wald ratio | 1 | cis | NA |
| Bulimia nervosa | -0.0454 | 0.0227 | 0.0455 | Wald ratio | 1 | cis | NA |
| HOMA-B | -0.0206 | 0.0105 | 0.0499 | Wald ratio | 1 | cis | NA |
| _...and 76 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3232_28_2` | TrATPase | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_10 association rows across 4 traits (9 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating ACP5 levels | 6e-971 | rs2305799 | 4 | GCST90859953 | no MR -> candidate analysis |
| ACP5 protein levels | 2e-208 | rs147025508 | 2 | GCST90468203 | no MR -> candidate analysis |
| Tartrate-resistant acid phosphatase type 5 levels | 2e-77 | rs7256770 | 3 | GCST90425665 | no MR -> candidate analysis |
| Cerebrospinal fluid protein ACP5 levels | 2e-42 | rs2071484 | 1 | GCST90944664 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1599 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Spondyloenchondrodysplasia with immune dysregulation | 0.909 | — | established (curated) | no MR -> candidate analysis |
| hereditary disease | 0.771 | — | established (curated) | no MR -> candidate analysis |
| Alzheimer disease | 0.302 | — | common-variant locus | no MR -> candidate analysis |
| thrombophilia | 0.336 | — | common-variant locus | no MR -> candidate analysis |
| Abnormality of the skeletal system | 0.206 | — | common-variant locus | no MR -> candidate analysis |

> Of the 5 rows above, **5 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Tartrate-resistant acid phosphatase type 5) |
| gnomAD constraint | pLI=1.1e-07, LOEUF=1.18 — LoF-tolerant |
| GWAS Catalog | 49 unique SNPs / 98 rows |
| ClinVar | 368 records; 3 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1599 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'ACP5' and resolved to 'Tartrate-resistant acid phosphatase type 5' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 368 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 4 of 4 traits by best p-value, aggregated from 10 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P13686 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000102575/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3120042/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/ACP5 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/ACP5 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=ACP5%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/ACP5 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T00:52:06  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
