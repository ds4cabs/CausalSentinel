# Protein Dossier — CD300C (CMRF35-like molecule 6)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Coronary heart disease | -0.0838 | 0.0199 | 2.44e-05 | Inverse variance weighted | 2 | cis | NA |
| Coronary heart disease | -0.0838 | 0.0199 | 2.44e-05 | Inverse variance weighted | 2 | trans | NA |
| Non-cancer illness code  self-reported: hypertension | 0.0321 | 0.00785 | 4.43e-05 | Inverse variance weighted | 2 | cis | NA |
| Non-cancer illness code  self-reported: hypertension | 0.0321 | 0.00785 | 4.43e-05 | Inverse variance weighted | 2 | trans | NA |
| Myocardial infarction | -0.0861 | 0.0227 | 1.53e-04 | Inverse variance weighted | 2 | cis | NA |
| Myocardial infarction | -0.0861 | 0.0227 | 1.53e-04 | Inverse variance weighted | 2 | trans | NA |
| Age at menopause | 0.16 | 0.0599 | 0.00766 | Wald ratio | 1 | trans | NA |
| Body fat | -0.0315 | 0.0126 | 0.0121 | Wald ratio | 1 | trans | NA |
| HOMA-B | 0.0184 | 0.00778 | 0.0183 | Wald ratio | 1 | trans | NA |
| HOMA-IR | 0.022 | 0.00938 | 0.0193 | Wald ratio | 1 | trans | NA |
| Diastolic blood pressure  automated reading | 0.0113 | 0.00487 | 0.0201 | Inverse variance weighted | 2 | cis | NA |
| Diastolic blood pressure  automated reading | 0.0113 | 0.00487 | 0.0201 | Inverse variance weighted | 2 | trans | NA |
| _...and 156 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-5066_134_3` | CLM6 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_8 association rows across 8 traits (5 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Cerebrospinal fluid protein CD300C levels | 3e-253 | rs2293188 | 1 | GCST90944162 | no MR -> candidate analysis |
| Circulating CD300C levels | 9e-102 | rs924828 | 1 | GCST90859659 | no MR -> candidate analysis |
| CD300E protein levels | 6e-20 | rs56095552 | 1 | GCST90468621 | no MR -> candidate analysis |
| CMRF35-like molecule 6 levels | 2e-17 | rs73359962 | 1 | GCST90059929 | no MR -> candidate analysis |
| CD300C protein levels | 1e-14 | rs144088488 | 1 | GCST90468620 | no MR -> candidate analysis |
| Velopharyngeal dysfunction | 2e-6 | rs931791 | 1 | GCST006280 | no MR -> candidate analysis |
| Baseline memory in impaired cognition x sex interaction | 5e-6 | rs113310167 | 1 | GCST90448440 | no MR -> candidate analysis |
| Parkinson's disease motor subtype (tremor to postural instab | 9e-6 | rs118076379 | 1 | GCST90000015 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 82 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| diabetes mellitus | 0.207 | — | common-variant locus | no MR -> candidate analysis |

> Of the 1 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.0066, LOEUF=0.989 — LoF-tolerant |
| GWAS Catalog | 81 unique SNPs / 162 rows |
| ClinVar | 77 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 82 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'CD300C'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 77 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 8 of 8 traits by best p-value, aggregated from 8 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q08708 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000167850/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CD300C — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CD300C — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CD300C%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CD300C — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:41:47  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
