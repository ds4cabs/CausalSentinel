# Protein Dossier — SEMG2 (Semenogelin-2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Age at menarche | -0.0621 | 0.0116 | 9.00e-08 | Wald ratio | 1 | trans | 0.88 |
| Weight | -0.0217 | 0.00414 | 1.55e-07 | Wald ratio | 1 | trans | 0.0065 |
| Body mass index (BMI) | -0.0184 | 0.00468 | 8.63e-05 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: osteoarthritis | -0.0631 | 0.0167 | 1.57e-04 | Wald ratio | 1 | trans | NA |
| Ovarian cancer | 0.092 | 0.026 | 3.95e-04 | Wald ratio | 1 | trans | NA |
| Serum cystatin C (eGFRcys) | -0.0135 | 0.00383 | 4.25e-04 | Wald ratio | 1 | trans | NA |
| High grade serous ovarian cancer | 0.0891 | 0.0309 | 0.00394 | Wald ratio | 1 | trans | NA |
| Small vessel disease | 0.207 | 0.0727 | 0.00435 | Wald ratio | 1 | trans | NA |
| Total cholesterol | -0.0294 | 0.0104 | 0.00473 | Wald ratio | 1 | trans | NA |
| Pulse rate | -0.023 | 0.00827 | 0.00541 | Wald ratio | 1 | trans | NA |
| HDL cholesterol | -0.0256 | 0.00968 | 0.00825 | Wald ratio | 1 | trans | NA |
| Creatinine (enzymatic) in urine | -0.0114 | 0.00449 | 0.011 | Wald ratio | 1 | trans | NA |
| _...and 84 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_14 association rows across 7 traits (11 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| WFDC12 protein levels | 1e-33 | rs555590563 | 7 | GCST90471073 | no MR -> candidate analysis |
| Elafin levels | 3e-21 | rs34274189 | 2 | GCST90162216 | no MR -> candidate analysis |
| Height (baseline) | 2e-15 | rs11699099 | 1 | GCST90565843 | no MR -> candidate analysis |
| PI3 protein levels | 1e-11 | rs6017525 | 1 | GCST90470230 | no MR -> candidate analysis |
| Asthma | 3e-6 | rs16989837 | 1 | GCST005212 | MR: beta=-0.00917, p=0.489 (trans) |
| Bipolar disorder | 3e-6 | rs190905111 | 1 | GCST008103 | MR: beta=-0.0903, p=0.375 (trans) |
| Gut microbiota (bacterial taxa, hurdle binary method) | 3e-6 | rs6124695 | 1 | GCST010396 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 45 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| nephrotic syndrome | 0.041 | — | common-variant locus | no MR -> candidate analysis |
| sialolithiasis | 0.041 | — | common-variant locus | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.41, LOEUF=0.962 — LoF-tolerant |
| GWAS Catalog | 53 unique SNPs / 106 rows |
| ClinVar | 104 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 45 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'SEMG2'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 104 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 7 of 7 traits by best p-value, aggregated from 14 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q02383 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000124157/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/SEMG2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/SEMG2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=SEMG2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/SEMG2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:00:11  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
