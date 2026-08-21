# Protein Dossier — GNPTG (N-acetylglucosamine-1-phosphotransferase subunit gamma)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Fractured bone site(s): Wrist | 0.255 | 0.0679 | 1.79e-04 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: muscle or soft tissue injuries | 0.309 | 0.107 | 0.00404 | Wald ratio | 1 | cis | NA |
| PGC cross-disorder traits | 0.205 | 0.0721 | 0.0045 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Injury or trauma resulting in loss of vision | 0.325 | 0.117 | 0.00555 | Wald ratio | 1 | cis | NA |
| Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | 0.0837 | 0.0343 | 0.0147 | Wald ratio | 1 | cis | NA |
| Bipolar disorder | 0.249 | 0.106 | 0.0189 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: depression | -0.13 | 0.0576 | 0.0236 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: bladder problem (not cancer) | 0.277 | 0.124 | 0.0251 | Wald ratio | 1 | cis | NA |
| Birth length | -0.114 | 0.0515 | 0.0264 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K57 Diverticular disease of intestine | -0.208 | 0.107 | 0.0528 | Wald ratio | 1 | cis | NA |
| Fasting insulin | 0.0291 | 0.0157 | 0.064 | Wald ratio | 1 | cis | NA |
| Cardioembolic stroke | -0.297 | 0.161 | 0.0646 | Wald ratio | 1 | cis | NA |
| _...and 91 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_7 association rows across 6 traits (5 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| N-acetylglucosamine-1-phosphotransferase subunit gamma level | 1e-259 | rs4984644 | 2 | GCST90248589 | no MR -> candidate analysis |
| Type 2 diabetes | 2e-21 | rs742460 | 1 | GCST90134620 | no MR -> candidate analysis |
| TPSAB1 protein levels | 5e-21 | rs199782632 | 1 | GCST90470951 | no MR -> candidate analysis |
| Blood protein levels | 8e-14 | rs4984820 | 1 | GCST006585 | no MR -> candidate analysis |
| T1 FreeSurfer DKT rh rostralanteriorcingulate thickness | 4e-9 | rs4984822 | 1 | GCST90384341 | no MR -> candidate analysis |
| Stuttering | 8e-7 | rs111790048 | 1 | GCST90707227 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 395 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| GNPTG-mucolipidosis | 0.899 | — | established (curated) | no MR -> candidate analysis |
| Retinal dystrophy | 0.74 | — | established (curated) | no MR -> candidate analysis |
| Rod-cone dystrophy | 0.699 | — | established (curated) | no MR -> candidate analysis |
| mucolipidosis | 0.547 | — | established (curated) | no MR -> candidate analysis |
| hereditary disease | 0.317 | — | established (curated) | no MR -> candidate analysis |
| type 2 diabetes mellitus | 0.238 | — | common-variant locus | no MR -> candidate analysis |
| diabetes mellitus | 0.201 | — | common-variant locus | no MR -> candidate analysis |

> Of the 7 rows above, **7 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=6.8e-17, LOEUF=1.34 — LoF-tolerant |
| GWAS Catalog | 85 unique SNPs / 170 rows |
| ClinVar | 1085 records; 19 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 395 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'GNPTG'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 1085 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 6 of 6 traits by best p-value, aggregated from 7 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9UJJ9 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000090581/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/GNPTG — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/GNPTG — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=GNPTG%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/GNPTG — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:51:16  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
