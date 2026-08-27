# Protein Dossier — RCAN1 (Calcipressin-1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: R10 Abdominal and pelvic pain | -0.154 | 0.0714 | 0.0312 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: I48 Atrial fibrillation and flutter | -0.343 | 0.175 | 0.0494 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: hypertrophic cardiomyopathy (hcm  or  hocm) | 0.876 | 0.462 | 0.0581 | Wald ratio | 1 | trans | NA |
| Cancer code  self-reported: prostate cancer | -0.496 | 0.263 | 0.0595 | Wald ratio | 1 | trans | NA |
| Invasive mucinous ovarian cancer | 0.454 | 0.246 | 0.065 | Wald ratio | 1 | trans | NA |
| Sleep duration | 0.0169 | 0.00984 | 0.0859 | Wald ratio | 1 | trans | NA |
| ER-positive Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | 0.0811 | 0.0491 | 0.0988 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: C61 Malignant neoplasm of prostate | -0.415 | 0.253 | 0.101 | Wald ratio | 1 | trans | NA |
| Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | 0.068 | 0.0417 | 0.103 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: ankylosing spondylitis | 0.299 | 0.184 | 0.105 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: pernicious anaemia | 0.287 | 0.181 | 0.114 | Wald ratio | 1 | trans | NA |
| Diastolic blood pressure  automated reading | 0.02 | 0.0129 | 0.12 | Wald ratio | 1 | trans | NA |
| _...and 58 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_18 association rows across 13 traits (6 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Calcium levels | 1e-14 | rs928760 | 2 | GCST90018951 | no MR -> candidate analysis |
| Calcium levels (UKB data field 30680) | 1e-11 | rs13051296 | 1 | GCST90468065 | no MR -> candidate analysis |
| Rheumatoid arthritis | 1e-8 | rs79818725 | 4 | GCST90132222 | no MR -> candidate analysis |
| Hypothyroidism | 2e-8 | rs79125270 | 1 | GCST90627750 | no MR -> candidate analysis |
| Rheumatoid arthritis (ACPA-positive) | 3e-8 | rs2834512 | 2 | GCST005568 | no MR -> candidate analysis |
| Hippocampal volume | 2e-7 | rs2284609 | 1 | GCST007009 | no MR -> candidate analysis |
| Cancer | 5e-7 | rs2834439; rs4817642; rs2834440; rs2834450; rs2834461; rs723548; rs13048252; rs10854373; rs2834475; rs2834478; rs8129326; rs2834485; rs3453; rs2070359; rs2247810; rs4817656; rs11911509; rs2211698; rs7279771; rs727957; rs2834502; rs8131131; rs2834506; rs2834512; rs2284576 | 1 | GCST005275 | MR: beta=0.876, p=0.0581 (trans) |
| Psoriasis | 1e-6 | rs9305556 | 1 | GCST002874 | MR: beta=0.0858, p=0.438 (trans) |
| Maximum habitual alcohol consumption | 1e-6 | rs114086924 | 1 | GCST008675 | no MR -> candidate analysis |
| Opioid analgesic dose requirement in cancer pain treatment | 5e-6 | rs2834573 | 1 | GCST90226002 | no MR -> candidate analysis |
| C reactive protein levels x vegetarianism interaction | 5e-6 | rs2006998 | 1 | GCST90161180 | no MR -> candidate analysis |
| Epigenetic age acceleration in alcohol use disorder | 8e-6 | rs1571695 | 1 | GCST008748 | no MR -> candidate analysis |
| _...and 1 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 313 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| hypothyroidism | 0.414 | — | common-variant locus | no MR -> candidate analysis |
| rheumatoid arthritis | 0.372 | — | common-variant locus | no MR -> candidate analysis |
| type 2 diabetes mellitus | 0.053 | — | common-variant locus | no MR -> candidate analysis |
| breast cancer | 0.07 | — | common-variant locus | MR: beta=0.0811, p=0.0988 (trans) |
| lung cancer | 0.025 | — | established (curated) | no MR -> candidate analysis |
| breast carcinoma | 0.092 | — | common-variant locus | no MR -> candidate analysis |
| atrial fibrillation | 0.104 | — | common-variant locus | MR: beta=-0.343, p=0.0494 (trans) |

> Of the 7 rows above, **5 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.061, LOEUF=0.795 — LoF-tolerant |
| GWAS Catalog | 50 unique SNPs / 100 rows |
| ClinVar | 103 records; 13 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 313 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'RCAN1'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 103 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 13 of 13 traits by best p-value, aggregated from 18 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P53805 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000159200/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/RCAN1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/RCAN1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=RCAN1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/RCAN1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:46:12  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
