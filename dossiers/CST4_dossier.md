# Protein Dossier — CST4 (Cystatin-S)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Serum cystatin C (eGFRcys) | 0.071 | 0.00645 | 3.82e-28 | Wald ratio | 1 | cis | NA |
| Myocardial infarction | -0.106 | 0.0376 | 0.00462 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: psoriasis | 0.169 | 0.0648 | 0.00927 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Glaucoma | 0.15 | 0.0587 | 0.0105 | Wald ratio | 1 | cis | NA |
| Coronary heart disease | -0.087 | 0.034 | 0.0105 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: vitiligo | 0.686 | 0.269 | 0.0108 | Wald ratio | 1 | cis | NA |
| Age at menopause | 0.215 | 0.086 | 0.0124 | Wald ratio | 1 | cis | NA |
| Urate | -0.0452 | 0.0187 | 0.0158 | Wald ratio | 1 | cis | NA |
| Birth weight | -0.0292 | 0.0125 | 0.019 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: depression | 0.0612 | 0.0315 | 0.0519 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I30 Acute pericarditis | 0.558 | 0.293 | 0.0563 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: gastro-oesophageal reflux (gord)  or  gastric reflux | 0.0693 | 0.0365 | 0.0576 | Wald ratio | 1 | cis | NA |
| _...and 81 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3802_50_1` | Cystatin-S | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_42 association rows across 22 traits (36 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Cystatin C levels | 8e-3580 | rs13039144 | 4 | GCST90019504 | no MR -> candidate analysis |
| Circulating CST3 levels | 9e-462 | rs35488434 | 3 | GCST90860429 | no MR -> candidate analysis |
| Cystatin C plasma levels | 1e-308 | rs66590796 | 1 | GCST90100559 | no MR -> candidate analysis |
| Cystatin-S levels | 4e-130 | rs7263473 | 3 | GCST90247221 | no MR -> candidate analysis |
| Cystatin-SA levels | 6e-113 | rs6036489 | 4 | GCST90247222 | no MR -> candidate analysis |
| Cystatin-SN levels | 7e-76 | rs6049008 | 4 | GCST90247223 | no MR -> candidate analysis |
| Serum levels of protein CST4 | 9e-62 | rs7263473 | 1 | GCST90087762 | no MR -> candidate analysis |
| CST3 protein levels | 7e-54 | rs28463225 | 2 | GCST90468894 | no MR -> candidate analysis |
| Serum levels of protein CST3 | 1e-51 | rs2254635 | 1 | GCST90087977 | no MR -> candidate analysis |
| CST1 protein levels | 5e-44 | rs3004155 | 4 | GCST90468893 | no MR -> candidate analysis |
| Cystatin-C levels | 3e-42 | rs16985615 | 4 | GCST90247216 | no MR -> candidate analysis |
| Blood protein levels | 2e-31 | rs7270028 | 1 | GCST006585 | no MR -> candidate analysis |
| _...and 10 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 371 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| alcohol drinking | 0.423 | — | common-variant locus | no MR -> candidate analysis |
| chronic laryngitis | 0.244 | — | common-variant locus | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=2.6e-08, LOEUF=2.27 — LoF-tolerant |
| GWAS Catalog | 101 unique SNPs / 222 rows |
| ClinVar | 62 records; 3 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 371 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'CST4'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 62 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 22 traits by best p-value, aggregated from 42 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P01036 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000101441/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CST4 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CST4 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CST4%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CST4 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:07:41  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
