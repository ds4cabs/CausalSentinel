# Protein Dossier — TNFSF14 (Tumor necrosis factor ligand superfamily member 14)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Cancer code  self-reported: prostate cancer | -0.3 | 0.113 | 0.008 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | -0.0879 | 0.0343 | 0.0103 | Wald ratio | 1 | cis | NA |
| ER-positive Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.0556 | 0.0227 | 0.0142 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: ankylosing spondylitis | 0.254 | 0.105 | 0.0152 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R10 Abdominal and pelvic pain | -0.0863 | 0.0372 | 0.0203 | Wald ratio | 1 | cis | NA |
| Cardioembolic stroke | -0.18 | 0.088 | 0.0411 | Wald ratio | 1 | cis | NA |
| Small vessel disease | -0.202 | 0.101 | 0.0466 | Wald ratio | 1 | cis | NA |
| Transferrin | 0.0697 | 0.0364 | 0.0554 | Wald ratio | 1 | cis | NA |
| Sodium in urine | 0.0133 | 0.00694 | 0.0557 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I83 Varicose veins of lower extremities | 0.085 | 0.0453 | 0.0609 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: L03 Cellulitis | 0.13 | 0.0693 | 0.0615 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K40 Inguinal hernia | 0.0743 | 0.0401 | 0.0638 | Wald ratio | 1 | cis | NA |
| _...and 83 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-5355_69_3` | LIGHT | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_102 association rows across 46 traits (97 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating TNFSF14 levels (id: OID00506_OID20953) | 8e-534 | rs344560 | 5 | GCST90859862 | no MR -> candidate analysis |
| HGF/TNFSF14 protein level ratio | 1e-413 | rs344560 | 1 | GCST90315060 | no MR -> candidate analysis |
| TNFRSF14/TNFSF14 protein level ratio | 3e-369 | rs344560 | 1 | GCST90315936 | no MR -> candidate analysis |
| CD40LG/TNFSF14 protein level ratio | 1e-360 | rs344560 | 1 | GCST90313827 | no MR -> candidate analysis |
| Circulating TNFSF14 levels (id: OID00787_OID20953) | 6e-333 | rs344560 | 5 | GCST90860119 | no MR -> candidate analysis |
| CD70 protein levels | 8e-214 | rs80196597 | 16 | GCST90468645 | no MR -> candidate analysis |
| TNFSF14 protein levels | 6e-208 | rs413141 | 5 | GCST90470922 | no MR -> candidate analysis |
| Tumor necrosis factor ligand superfamily member 14 levels | 8e-173 | rs344560 | 7 | GCST90012029 | no MR -> candidate analysis |
| FUT8/TNFSF14 protein level ratio | 5e-79 | rs1077667 | 1 | GCST90314895 | no MR -> candidate analysis |
| Monocyte count | 8e-58 | rs413141 | 8 | GCST90002344 | no MR -> candidate analysis |
| LTA protein levels | 1e-50 | rs344560 | 1 | GCST90469813 | no MR -> candidate analysis |
| Circulating LTA levels | 2e-48 | rs344560 | 1 | GCST90859910 | no MR -> candidate analysis |
| _...and 34 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 702 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| multiple sclerosis | 0.773 | — | common-variant locus | no MR -> candidate analysis |
| thyroid gland disorder | 0.56 | — | common-variant locus | no MR -> candidate analysis |
| hypothyroidism | 0.493 | — | common-variant locus | MR: beta=-0.0879, p=0.0103 (cis) |
| colorectal carcinoma | 0.285 | — | common-variant locus | no MR -> candidate analysis |
| malunion fracture | 0.293 | — | common-variant locus | no MR -> candidate analysis |
| gestational diabetes | 0.293 | — | common-variant locus | no MR -> candidate analysis |

> Of the 6 rows above, **5 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 2 known modulators (Tumor necrosis factor ligand superfamily member 14) |
| gnomAD constraint | pLI=0.00042, LOEUF=1.02 — LoF-tolerant |
| GWAS Catalog | 102 unique SNPs / 216 rows |
| ClinVar | 54 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 702 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'TNFSF14' and resolved to 'Tumor necrosis factor ligand superfamily member 14' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 54 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 46 traits by best p-value, aggregated from 102 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O43557 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000125735/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3712914/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/TNFSF14 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/TNFSF14 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=TNFSF14%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/TNFSF14 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:27:42  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
