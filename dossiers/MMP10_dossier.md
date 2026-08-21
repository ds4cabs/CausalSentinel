# Protein Dossier — MMP10 (Stromelysin-2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Eczema | 0.233 | 0.0931 | 0.0122 | Wald ratio | 1 | cis | NA |
| Clear cell ovarian cancer | -0.369 | 0.157 | 0.0189 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R04 Haemorrhage from respiratory passages | 0.247 | 0.106 | 0.0197 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R14 Flatulence and related conditions | 0.558 | 0.247 | 0.0237 | Wald ratio | 1 | cis | NA |
| Nucleus accumbens volume | -13.8 | 6.24 | 0.0266 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: iron deficiency anaemia | 0.233 | 0.106 | 0.0279 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R10 Abdominal and pelvic pain | 0.0893 | 0.0426 | 0.0363 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: gastro-oesophageal reflux (gord)  or  gastric reflux | -0.0993 | 0.0514 | 0.0535 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: deep venous thrombosis (dvt) | 0.118 | 0.061 | 0.0535 | Wald ratio | 1 | cis | NA |
| Putamen volume | -60.8 | 32.2 | 0.0589 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K80 Cholelithiasis | 0.113 | 0.0602 | 0.0606 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Arm | 0.155 | 0.0838 | 0.0641 | Wald ratio | 1 | cis | NA |
| _...and 60 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3743_1_2` | MMP-10 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_33 association rows across 17 traits (31 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating MMP10 levels | 2e-597 | rs17860955 | 3 | GCST90859882 | no MR -> candidate analysis |
| Matrix metalloproteinase-10 levels | 5e-155 | rs17860955 | 4 | GCST90012050 | no MR -> candidate analysis |
| Stromelysin-2 levels | 5e-118 | rs17860955 | 4 | GCST90249716 | no MR -> candidate analysis |
| Stromelysin-2 (analyte X10479.18) levels | 4e-80 | rs12804929 | 1 | GCST90421127 | no MR -> candidate analysis |
| Serum levels of protein MMP10 | 3e-67 | rs486055 | 4 | GCST90090215 | no MR -> candidate analysis |
| Matrix metalloproteinase-1 levels | 1e-48 | rs12290253 | 1 | GCST90012033 | no MR -> candidate analysis |
| MMP10 protein levels | 2e-48 | rs17359230 | 3 | GCST90469915 | no MR -> candidate analysis |
| Stromelysin-2 (analyte X8479.4) levels | 6e-47 | rs486055 | 1 | GCST90427410 | no MR -> candidate analysis |
| Cerebrospinal fluid protein MMP10 levels | 5e-42 | rs486055 | 1 | GCST90944431 | no MR -> candidate analysis |
| Stromelysin-2 levels (MMP10.8479.4.3) | 1e-23 | rs17860955 | 2 | GCST90242905 | no MR -> candidate analysis |
| Blood protein levels | 4e-21 | rs12807063 | 2 | GCST006585 | no MR -> candidate analysis |
| MMP3 protein levels | 8e-14 | rs17860984 | 1 | GCST90469920 | no MR -> candidate analysis |
| _...and 5 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 629 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| respiratory tract infectious disorder | 0.19 | — | common-variant locus | no MR -> candidate analysis |
| benign neoplasm | 0.19 | — | common-variant locus | MR: beta=-0.0813, p=0.362 (cis) |
| essential tremor | 0.182 | — | established (curated) | no MR -> candidate analysis |

> Of the 3 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Stromelysin-2) |
| gnomAD constraint | pLI=8.1e-18, LOEUF=1.29 — LoF-tolerant |
| GWAS Catalog | 168 unique SNPs / 382 rows |
| ClinVar | 119 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 629 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'MMP10' and resolved to 'Stromelysin-2' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 119 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 17 of 17 traits by best p-value, aggregated from 33 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P09238 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000166670/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4270/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/MMP10 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/MMP10 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=MMP10%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/MMP10 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:49:48  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
