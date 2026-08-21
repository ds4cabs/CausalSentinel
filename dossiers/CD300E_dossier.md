# Protein Dossier — CD300E (CMRF35-like molecule 2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Triglycerides | -0.0511 | 0.0178 | 0.00404 | Wald ratio | 1 | cis | NA |
| Underlying (primary) cause of death: ICD10: E85.4 Organ-limited amyloidosis | 1.54 | 0.627 | 0.0138 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R10 Abdominal and pelvic pain | 0.0943 | 0.0395 | 0.0171 | Wald ratio | 1 | cis | NA |
| Putamen volume | 50.5 | 21.9 | 0.0208 | Wald ratio | 1 | cis | NA |
| Body fat | -0.0463 | 0.0204 | 0.023 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: deep venous thrombosis (dvt) | 0.127 | 0.0563 | 0.0237 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I83 Varicose veins of lower extremities | 0.113 | 0.0562 | 0.0453 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | 0.0685 | 0.0373 | 0.0665 | Wald ratio | 1 | cis | NA |
| Systolic blood pressure  automated reading | -0.0168 | 0.00919 | 0.0681 | Wald ratio | 1 | cis | NA |
| Lumbar spine bone mineral density | 0.0588 | 0.0327 | 0.072 | Wald ratio | 1 | cis | NA |
| Diastolic blood pressure  automated reading | -0.0165 | 0.0092 | 0.0733 | Wald ratio | 1 | cis | NA |
| Bulimia nervosa | -0.0519 | 0.0296 | 0.0801 | Wald ratio | 1 | cis | NA |
| _...and 96 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_7 association rows across 5 traits (7 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| CD300E protein levels | 2e-230 | rs533419 | 3 | GCST90468621 | no MR -> candidate analysis |
| CMRF35-like molecule 2 (analyte X8287.17) levels | 2e-82 | rs581157 | 1 | GCST90427311 | no MR -> candidate analysis |
| Serum levels of protein CD300E | 7e-40 | rs8081669 | 1 | GCST90090104 | no MR -> candidate analysis |
| Blood protein levels | 4e-27 | rs8081669 | 1 | GCST006585 | no MR -> candidate analysis |
| CD300C protein levels | 8e-14 | rs113947931 | 1 | GCST90468620 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 76 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| chondrocalcinosis | 0.337 | — | common-variant locus | no MR -> candidate analysis |
| Hodgkins lymphoma | 0.331 | — | common-variant locus | no MR -> candidate analysis |
| Nasal polyposis | 0.194 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.00057, LOEUF=1.05 — LoF-tolerant |
| GWAS Catalog | 90 unique SNPs / 180 rows |
| ClinVar | 50 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 76 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'CD300E'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 50 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 5 of 5 traits by best p-value, aggregated from 7 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q496F6 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000186407/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CD300E — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CD300E — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CD300E%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CD300E — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:41:59  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
