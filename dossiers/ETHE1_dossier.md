# Protein Dossier — ETHE1 (Persulfide dioxygenase ETHE1, mitochondrial)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Intracranial volume | -1.42e+04 | 5.52e+03 | 0.0103 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: hypopituitarism | 0.589 | 0.23 | 0.0103 | Wald ratio | 1 | trans | NA |
| Systolic blood pressure  automated reading | -0.0172 | 0.00732 | 0.0186 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: pernicious anaemia | 0.245 | 0.104 | 0.019 | Wald ratio | 1 | trans | NA |
| LDL cholesterol | -0.0363 | 0.0157 | 0.0206 | Wald ratio | 1 | trans | NA |
| Total cholesterol | -0.0335 | 0.0154 | 0.0294 | Wald ratio | 1 | trans | NA |
| Eye problems or disorders: Glaucoma | -0.149 | 0.0698 | 0.0322 | Wald ratio | 1 | trans | NA |
| IgA nephropathy | 0.473 | 0.228 | 0.0381 | Wald ratio | 1 | trans | NA |
| Neo-openness to experience | 0.43 | 0.211 | 0.041 | Wald ratio | 1 | trans | NA |
| Vascular or heart problems diagnosed by doctor: Angina | -0.0883 | 0.0439 | 0.0443 | Wald ratio | 1 | trans | NA |
| Age at menopause | -0.11 | 0.0549 | 0.0455 | Wald ratio | 1 | trans | NA |
| Mean cell haemoglobin | 0.0629 | 0.0319 | 0.0484 | Wald ratio | 1 | trans | NA |
| _...and 93 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3847_56_2` | ETHE1 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_10 association rows across 5 traits (9 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating TNFRSF10C levels | 2e-280 | rs78110932 | 1 | GCST90859942 | no MR -> candidate analysis |
| LYPD3 protein levels | 1e-140 | rs112093284 | 4 | GCST90469828 | no MR -> candidate analysis |
| PINLYP protein levels | 1e-33 | rs139053385 | 3 | GCST90470238 | no MR -> candidate analysis |
| Cerebrospinal fluid protein LYPD3 levels | 5e-17 | rs73043650 | 1 | GCST90944409 | no MR -> candidate analysis |
| Neutrophil-to-lymphocyte ratio | 2e-9 | rs201252431 | 1 | GCST90866310 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 120 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| ethylmalonic encephalopathy | 0.927 | — | established (curated) | no MR -> candidate analysis |
| Abnormality of the nervous system | 0.438 | — | established (curated) | no MR -> candidate analysis |
| hereditary disease | 0.312 | — | established (curated) | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.00055, LOEUF=0.946 — LoF-tolerant |
| GWAS Catalog | 109 unique SNPs / 240 rows |
| ClinVar | 504 records; 14 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 120 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'ETHE1'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 504 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 5 of 5 traits by best p-value, aggregated from 10 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O95571 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000105755/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/ETHE1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/ETHE1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=ETHE1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/ETHE1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:29:43  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
