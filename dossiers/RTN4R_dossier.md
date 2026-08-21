# Protein Dossier — RTN4R (Reticulon-4 receptor)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: kidney stone or ureter stone or bladder stone | 0.231 | 0.0718 | 0.00128 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: sleep apnoea | 0.305 | 0.107 | 0.00451 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I83 Varicose veins of lower extremities | -0.189 | 0.0674 | 0.00518 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: D25 Leiomyoma of uterus | 0.156 | 0.0603 | 0.00971 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | 0.0264 | 0.0103 | 0.0102 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K20 Oesophagitis | 0.172 | 0.068 | 0.0113 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: basal cell carcinoma | 0.164 | 0.0709 | 0.0208 | Wald ratio | 1 | cis | NA |
| Happiness | 0.0227 | 0.00986 | 0.0211 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertrophic cardiomyopathy (hcm  or  hocm) | 0.693 | 0.312 | 0.0261 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: chronic obstructive airways disease or copd | 0.236 | 0.109 | 0.0311 | Wald ratio | 1 | cis | NA |
| Knee and hip osteoarthritis | 0.147 | 0.0695 | 0.0349 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: asthma | 0.0442 | 0.0213 | 0.0384 | Wald ratio | 1 | cis | NA |
| _...and 67 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-5105_2_3` | Nogo Receptor | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_22 association rows across 13 traits (18 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating RTN4R levels | 1e-398 | rs696881 | 5 | GCST90860400 | no MR -> candidate analysis |
| Reticulon-4 receptor levels | 1e-86 | rs696881 | 3 | GCST90249206 | no MR -> candidate analysis |
| RTN4R protein levels | 7e-86 | rs112262759 | 4 | GCST90470508 | no MR -> candidate analysis |
| Serum levels of protein RTN4R | 2e-36 | rs696880 | 1 | GCST90088927 | no MR -> candidate analysis |
| Reticulon-4 receptor levels (RTN4R.5105.2.3) | 1e-23 | rs701428 | 1 | GCST90242633 | no MR -> candidate analysis |
| COMT protein levels | 3e-22 | rs145542169 | 1 | GCST90468828 | no MR -> candidate analysis |
| Gut microbial network clusters (Cyan (at 3 months) x Vaginal | 9e-9 | rs9617869 | 1 | GCST90569293 | no MR -> candidate analysis |
| Relative abundance of the human milk microbiota (HMM) Entero | 9e-9 | rs17757179 | 1 | GCST90428938 | no MR -> candidate analysis |
| S-adenosylhomocysteine (SAH) levels | 4e-8 | rs145542169 | 1 | GCST90503881 | no MR -> candidate analysis |
| RS-6-hydroxywarfarin levels | 1e-6 | rs8139225 | 1 | GCST90129567 | no MR -> candidate analysis |
| Obesity-related traits | 2e-6 | rs701428 | 1 | GCST001762 | no MR -> candidate analysis |
| Tiglylcarnitine (C5:1-DC) levels in elite athletes | 3e-6 | rs854941 | 1 | GCST90133612 | no MR -> candidate analysis |
| _...and 1 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 570 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| schizophrenia | 0.784 | — | established (curated) | MR: beta=0.0635, p=0.0688 (cis) |
| placenta praevia | 0.193 | — | common-variant locus | no MR -> candidate analysis |
| response to stimulus | 0.193 | — | common-variant locus | no MR -> candidate analysis |
| head and neck cancer | 0.182 | — | established (curated) | no MR -> candidate analysis |

> Of the 4 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1, LOEUF=0.33 — LoF-INTOLERANT |
| GWAS Catalog | 60 unique SNPs / 119 rows |
| ClinVar | 501 records; 23 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 570 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'RTN4R'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 501 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 13 of 13 traits by best p-value, aggregated from 22 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9BZR6 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000040608/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/RTN4R — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/RTN4R — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=RTN4R%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/RTN4R — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:54:31  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
