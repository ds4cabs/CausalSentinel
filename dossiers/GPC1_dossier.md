# Protein Dossier — GPC1 (Glypican-1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: pneumothorax | 0.872 | 0.193 | 6.43e-06 | Wald ratio | 1 | cis | NA |
| Gallbladder cancer | 2.94 | 0.892 | 9.89e-04 | Wald ratio | 1 | cis | NA |
| HOMA-IR | 0.0519 | 0.0189 | 0.00596 | Wald ratio | 1 | cis | NA |
| HOMA-B | 0.0401 | 0.0149 | 0.00697 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: sleep apnoea | 0.298 | 0.123 | 0.0156 | Wald ratio | 1 | cis | NA |
| Alzheimer's disease | 0.145 | 0.067 | 0.0306 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertension | -0.0339 | 0.0159 | 0.0332 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R35 Polyuria | 0.242 | 0.115 | 0.0359 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R14 Flatulence and related conditions | 0.505 | 0.243 | 0.0378 | Wald ratio | 1 | cis | NA |
| Systemic lupus erythematosus | 0.358 | 0.178 | 0.0439 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: deep venous thrombosis (dvt) | 0.111 | 0.0575 | 0.0536 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Other bones | 0.0704 | 0.0366 | 0.0547 | Wald ratio | 1 | cis | NA |
| _...and 89 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_59 association rows across 35 traits (43 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating GPC1 levels | 5e-654 | rs11892254 | 3 | GCST90860018 | no MR -> candidate analysis |
| Glypican-1 levels | 1e-181 | rs1126920 | 2 | GCST90247755 | no MR -> candidate analysis |
| GPC1 protein levels | 6e-139 | rs11892190 | 7 | GCST90469386 | no MR -> candidate analysis |
| Dual specificity phosphatase 28 levels | 2e-72 | rs148245427 | 1 | GCST90247371 | no MR -> candidate analysis |
| Height | 1e-40 | rs12467087 | 5 | GCST90245848 | no MR -> candidate analysis |
| Mean platelet thrombocyte volume (UKB data field 30100) | 2e-16 | rs113438952 | 4 | GCST90468087 | no MR -> candidate analysis |
| Male-pattern baldness | 2e-14 | rs76710549 | 1 | GCST007020 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 2e-14 | rs6742784 | 1 | GCST90838669 | no MR -> candidate analysis |
| Cholelithiasis with acute cholecystitis (PheCode 574.11) | 2e-12 | rs557276480 | 1 | GCST90480349 | no MR -> candidate analysis |
| Infection with drug-resistant microorganisms (PheCode 41.9) | 2e-11 | rs191571179 | 1 | GCST90479748 | no MR -> candidate analysis |
| Balding type 1 | 5e-11 | rs56003038 | 1 | GCST007038 | no MR -> candidate analysis |
| Keloid | 6e-10 | rs12989123 | 2 | GCST90652487 | no MR -> candidate analysis |
| _...and 23 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 307 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| keloid | 0.405 | — | common-variant locus | no MR -> candidate analysis |
| androgenetic alopecia | 0.393 | — | common-variant locus | no MR -> candidate analysis |
| infectious disease | 0.353 | — | common-variant locus | no MR -> candidate analysis |
| liver disorder | 0.306 | — | common-variant locus | no MR -> candidate analysis |
| cholelithiasis | 0.304 | — | common-variant locus | no MR -> candidate analysis |

> Of the 5 rows above, **5 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.0011, LOEUF=0.7 — LoF-tolerant |
| GWAS Catalog | 71 unique SNPs / 129 rows |
| ClinVar | 255 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 307 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'GPC1'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 255 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 35 traits by best p-value, aggregated from 59 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P35052 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000063660/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/GPC1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/GPC1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=GPC1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/GPC1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:52:44  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
