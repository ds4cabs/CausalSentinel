# Protein Dossier — NPTXR (Neuronal pentraxin receptor)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: R11 Nausea and vomiting | 0.432 | 0.0911 | 2.11e-06 | Wald ratio | 1 | cis | NA |
| Schizophrenia | 0.12 | 0.0337 | 3.79e-04 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R14 Flatulence and related conditions | 0.608 | 0.208 | 0.00345 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: D12 Benign neoplasm of colon  rectum  anus and anal canal | 0.158 | 0.0632 | 0.0126 | Wald ratio | 1 | cis | NA |
| Cough on most days | -0.12 | 0.0508 | 0.0181 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: asthma | 0.0531 | 0.0232 | 0.0221 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: diverticular disease or diverticulitis | 0.158 | 0.0708 | 0.0256 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N81 Female genital prolapse | 0.134 | 0.0641 | 0.0369 | Wald ratio | 1 | cis | NA |
| Forearm bone mineral density | 0.109 | 0.0577 | 0.059 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: osteoporosis | 0.112 | 0.0629 | 0.0755 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Other bones | 0.0625 | 0.0357 | 0.0799 | Wald ratio | 1 | cis | NA |
| Birth weight | 0.021 | 0.0123 | 0.0884 | Wald ratio | 1 | cis | NA |
| _...and 62 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_30 association rows across 21 traits (25 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating NPTXR levels | 5e-1848 | rs185853862 | 4 | GCST90860330 | no MR -> candidate analysis |
| NPTXR protein levels | 2e-218 | rs5757299 | 3 | GCST90470080 | no MR -> candidate analysis |
| Neuronal pentraxin receptor levels | 2e-213 | rs117773903 | 3 | GCST90179374 | no MR -> candidate analysis |
| BCAN/NPTXR protein level ratio | 1e-204 | rs5757299 | 1 | GCST90313482 | no MR -> candidate analysis |
| Serum levels of protein NPTXR | 3e-32 | rs74703065 | 1 | GCST90090436 | no MR -> candidate analysis |
| Height | 5e-32 | rs13053505 | 1 | GCST90245848 | no MR -> candidate analysis |
| Blood protein levels | 5e-21 | rs12628473 | 1 | GCST006585 | no MR -> candidate analysis |
| Neuronal pentraxin receptor level in Chronic kidney disease  | 2e-20 | rs180925984 | 1 | GCST90234412 | no MR -> candidate analysis |
| Neuronal pentraxin receptor level in Chronic kidney disease  | 2e-15 | rs111444671 | 1 | GCST90239143 | no MR -> candidate analysis |
| NPTX2 protein levels | 1e-14 | rs192164176 | 1 | GCST90470079 | no MR -> candidate analysis |
| Sex hormone-binding globulin levels | 9e-12 | rs2075915 | 1 | GCST90012111 | no MR -> candidate analysis |
| Insomnia | 1e-11 | rs9607581 | 3 | GCST90131901 | no MR -> candidate analysis |
| _...and 9 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 175 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| insomnia | 0.59 | — | common-variant locus | no MR -> candidate analysis |
| cholelithiasis | 0.263 | — | common-variant locus | MR: beta=0.0531, p=0.359 (cis) |
| atrial fibrillation | 0.054 | — | common-variant locus | no MR -> candidate analysis |
| luminal A breast carcinoma | 0.034 | — | common-variant locus | no MR -> candidate analysis |

> Of the 4 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.66, LOEUF=0.604 — LoF-tolerant |
| GWAS Catalog | 66 unique SNPs / 132 rows |
| ClinVar | 119 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 175 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'NPTXR'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 119 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 21 traits by best p-value, aggregated from 30 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O95502 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000221890/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/NPTXR — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/NPTXR — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=NPTXR%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/NPTXR — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:03:02  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
