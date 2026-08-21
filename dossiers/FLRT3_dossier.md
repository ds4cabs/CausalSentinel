# Protein Dossier — FLRT3 (Leucine-rich repeat transmembrane protein FLRT3)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Femoral neck bone mineral density | 0.078 | 0.0197 | 7.57e-05 | Wald ratio | 1 | cis | NA |
| ER-negative Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.11 | 0.0315 | 4.78e-04 | Wald ratio | 1 | cis | NA |
| Diastolic blood pressure  automated reading | -0.0213 | 0.00643 | 9.25e-04 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | 0.0247 | 0.00811 | 0.0023 | Wald ratio | 1 | cis | NA |
| Lumbar spine bone mineral density | 0.0678 | 0.0231 | 0.00329 | Wald ratio | 1 | cis | NA |
| Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.0475 | 0.0171 | 0.0055 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Wrist | -0.13 | 0.0511 | 0.011 | Wald ratio | 1 | cis | NA |
| Fractured or broken bones in last 5 years | -0.0509 | 0.0206 | 0.0135 | Wald ratio | 1 | cis | NA |
| Intracranial volume | -1.21e+04 | 4.92e+03 | 0.0136 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: enlarged prostate | -0.154 | 0.0628 | 0.0144 | Wald ratio | 1 | cis | NA |
| Cough on most days | -0.084 | 0.035 | 0.0163 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: gout | 0.112 | 0.0471 | 0.0171 | Wald ratio | 1 | cis | NA |
| _...and 73 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_1 association rows across 1 traits (0 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Mood disorder in prion disease | 7e-6 | rs761998 | 1 | GCST002864 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 140 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Kallmann syndrome | 0.814 | — | established (curated) | no MR -> candidate analysis |
| hypogonadotropic hypogonadism 21 with or without anosmia | 0.696 | — | established (curated) | no MR -> candidate analysis |
| bipolar disorder | 0.565 | — | common-variant locus | MR: beta=0.149, p=0.166 (cis) |
| alcohol drinking | 0.241 | — | common-variant locus | no MR -> candidate analysis |
| attention deficit-hyperactivity disorder | 0.21 | — | common-variant locus | no MR -> candidate analysis |
| intelligence | 0.211 | — | common-variant locus | no MR -> candidate analysis |
| smoking initiation | 0.21 | — | common-variant locus | no MR -> candidate analysis |
| adverse effect | 0.203 | — | common-variant locus | no MR -> candidate analysis |
| response to stimulus | 0.203 | — | common-variant locus | no MR -> candidate analysis |
| pathological myopia | 0.182 | — | established (curated) | no MR -> candidate analysis |
| Genetic 46,XY disorder of sex development | 0.182 | — | established (curated) | no MR -> candidate analysis |
| myopia | 0.182 | — | established (curated) | no MR -> candidate analysis |
| amenorrhea | 0.182 | — | established (curated) | no MR -> candidate analysis |
| disorder of sexual differentiation | 0.182 | — | established (curated) | no MR -> candidate analysis |
| chronic venous hypertension | 0.172 | — | common-variant locus | no MR -> candidate analysis |

> Of the 15 rows above, **14 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.44, LOEUF=0.599 — LoF-tolerant |
| GWAS Catalog | 8 unique SNPs / 16 rows |
| ClinVar | 150 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 140 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'FLRT3'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 150 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 1 of 1 traits by best p-value, aggregated from 1 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9NZU0 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000125848/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/FLRT3 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/FLRT3 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=FLRT3%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/FLRT3 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:41:37  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
