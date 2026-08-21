# Protein Dossier — MPO (Myeloperoxidase)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Sleep duration | 0.016 | 0.00469 | 6.58e-04 | Inverse variance weighted | 5 | trans | NA |
| Sleep duration | 0.016 | 0.00469 | 6.58e-04 | Inverse variance weighted | 5 | trans | NA |
| Sleep duration | 0.016 | 0.00469 | 6.58e-04 | Inverse variance weighted | 5 | trans | NA |
| Sleep duration | 0.016 | 0.00469 | 6.58e-04 | Inverse variance weighted | 5 | cis | NA |
| Sleep duration | 0.016 | 0.00469 | 6.58e-04 | Inverse variance weighted | 5 | trans | NA |
| Diagnoses - main ICD10: I80 Phlebitis and thrombophlebitis | 0.188 | 0.0733 | 0.0102 | Inverse variance weighted | 5 | trans | NA |
| Diagnoses - main ICD10: I80 Phlebitis and thrombophlebitis | 0.188 | 0.0733 | 0.0102 | Inverse variance weighted | 5 | trans | NA |
| Diagnoses - main ICD10: I80 Phlebitis and thrombophlebitis | 0.188 | 0.0733 | 0.0102 | Inverse variance weighted | 5 | trans | NA |
| Diagnoses - main ICD10: I80 Phlebitis and thrombophlebitis | 0.188 | 0.0733 | 0.0102 | Inverse variance weighted | 5 | cis | NA |
| Diagnoses - main ICD10: I80 Phlebitis and thrombophlebitis | 0.188 | 0.0733 | 0.0102 | Inverse variance weighted | 5 | trans | NA |
| Age at menopause | 0.219 | 0.0933 | 0.0189 | Inverse variance weighted | 3 | trans | NA |
| Age at menopause | 0.219 | 0.0933 | 0.0189 | Inverse variance weighted | 3 | trans | NA |
| _...and 392 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2580_83_2` | Myeloperoxidase | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_139 association rows across 64 traits (136 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating MPO levels | 3e-475 | rs34097845 | 7 | GCST90859948 | no MR -> candidate analysis |
| MPO protein levels | 2e-307 | rs34097845 | 6 | GCST90469937 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 4e-178 | rs34097845 | 1 | GCST90838669 | no MR -> candidate analysis |
| Monocyte percentage (UKB data field 30190) | 2e-158 | rs34097845 | 2 | GCST90468091 | no MR -> candidate analysis |
| Myeloperoxidase levels | 4e-134 | rs34097845 | 5 | GCST90012031 | no MR -> candidate analysis |
| Monocyte count | 3e-124 | rs34097845 | 8 | GCST90002340 | no MR -> candidate analysis |
| Monocyte count (UKB data field 30130) | 1e-102 | rs34097845 | 3 | GCST90468090 | no MR -> candidate analysis |
| AZU1/MPO protein level ratio | 9e-81 | rs56378716 | 1 | GCST90313425 | no MR -> candidate analysis |
| CEACAM6 protein levels | 5e-76 | rs56378716 | 2 | GCST90468697 | no MR -> candidate analysis |
| Monocyte percentage of white cells | 7e-71 | rs34097845 | 5 | GCST90002394 | no MR -> candidate analysis |
| Neutrophil side scatter | 3e-64 | rs119468010 | 2 | GCST90281222 | no MR -> candidate analysis |
| Granulocyte percentage of myeloid white cells | 9e-57 | rs34097845 | 1 | GCST004608 | no MR -> candidate analysis |
| _...and 52 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1665 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| myeloperoxidase deficiency | 0.874 | — | established (curated) | no MR -> candidate analysis |
| Alzheimer disease type 1 | 0.798 | — | established (curated) | no MR -> candidate analysis |
| Alzheimer disease | 0.195 | — | established (curated) | no MR -> candidate analysis |
| Abnormality of the skeletal system | 0.22 | — | common-variant locus | no MR -> candidate analysis |

> Of the 4 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 1 known modulators (Myeloperoxidase) |
| gnomAD constraint | pLI=2.1e-16, LOEUF=1.02 — LoF-tolerant |
| GWAS Catalog | 105 unique SNPs / 212 rows |
| ClinVar | 177 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1665 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'MPO' and resolved to 'Myeloperoxidase' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 177 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 64 traits by best p-value, aggregated from 139 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P05164 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000005381/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2439/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/MPO — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/MPO — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=MPO%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/MPO — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:51:25  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
