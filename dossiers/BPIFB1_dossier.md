# Protein Dossier — BPIFB1 (BPI fold-containing family B member 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| ER-positive Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.0458 | 0.0179 | 0.0103 | Wald ratio | 1 | cis | NA |
| Femoral neck bone mineral density | 0.0426 | 0.0177 | 0.0159 | Wald ratio | 1 | cis | NA |
| Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.0353 | 0.0149 | 0.0178 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: gastro-oesophageal reflux (gord)  or  gastric reflux | -0.0664 | 0.0289 | 0.0216 | Wald ratio | 1 | cis | NA |
| Hirschsprung's disease | -0.871 | 0.387 | 0.0245 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I48 Atrial fibrillation and flutter | 0.107 | 0.0478 | 0.0246 | Wald ratio | 1 | cis | NA |
| Lumbar spine bone mineral density | 0.0457 | 0.0206 | 0.0269 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | -0.056 | 0.0264 | 0.0338 | Wald ratio | 1 | cis | NA |
| Mean cell haemoglobin concentration | 0.0405 | 0.0195 | 0.0373 | Wald ratio | 1 | cis | NA |
| Systolic blood pressure  automated reading | 0.0114 | 0.00574 | 0.0465 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: migraine | 0.0598 | 0.0306 | 0.0504 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I83 Varicose veins of lower extremities | 0.0694 | 0.0366 | 0.0577 | Wald ratio | 1 | cis | NA |
| _...and 68 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_15 association rows across 9 traits (13 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| BPIFB1 protein levels | 5e-281 | rs1884886 | 5 | GCST90468462 | no MR -> candidate analysis |
| Serum levels of protein BPIFB1 | 2e-31 | rs117258330 | 2 | GCST90086636 | no MR -> candidate analysis |
| LPO protein levels | 7e-27 | rs61739245 | 1 | GCST90469789 | no MR -> candidate analysis |
| Height (baseline) | 2e-16 | rs117461583 | 2 | GCST90565843 | no MR -> candidate analysis |
| PROC protein levels | 2e-15 | rs200193317 | 1 | GCST90470335 | no MR -> candidate analysis |
| BPI fold-containing family B member 1 levels (BPIFB1.11246.3 | 7e-15 | rs117258330 | 1 | GCST90240464 | no MR -> candidate analysis |
| Height (standard GWA) | 2e-12 | rs75744141 | 1 | GCST90267284 | no MR -> candidate analysis |
| Breast cancer | 8e-7 | rs4911315 | 1 | GCST90011804 | MR: beta=-0.0458, p=0.0103 (cis) |
| Height (weighted GWA) | 9e-7 | rs75744141 | 1 | GCST90267285 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 482 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| poisoning | 0.459 | — | common-variant locus | no MR -> candidate analysis |
| squamous cell carcinoma | 0.421 | — | common-variant locus | no MR -> candidate analysis |
| liver disorder | 0.389 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=3.5e-07, LOEUF=0.821 — LoF-tolerant |
| GWAS Catalog | 51 unique SNPs / 98 rows |
| ClinVar | 90 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 482 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'BPIFB1'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 90 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 9 of 9 traits by best p-value, aggregated from 15 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q8TDL5 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000125999/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/BPIFB1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/BPIFB1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=BPIFB1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/BPIFB1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:18:35  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
