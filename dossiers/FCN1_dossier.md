# Protein Dossier — FCN1 (Ficolin-1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Mean cell haemoglobin concentration | -0.0261 | 0.00772 | 7.31e-04 | Wald ratio | 1 | cis | NA |
| Femoral neck bone mineral density | 0.0434 | 0.015 | 0.00376 | Wald ratio | 1 | cis | NA |
| Schizophrenia | 0.0558 | 0.0203 | 0.00589 | Wald ratio | 1 | cis | NA |
| HOMA-IR | 0.024 | 0.00875 | 0.00605 | Wald ratio | 1 | cis | NA |
| Fasting insulin | 0.0161 | 0.00686 | 0.0188 | Wald ratio | 1 | cis | NA |
| Transferrin | 0.0477 | 0.0213 | 0.025 | Wald ratio | 1 | cis | NA |
| HOMA-B | 0.016 | 0.00721 | 0.0268 | Wald ratio | 1 | cis | NA |
| Transferrin Saturation | -0.0441 | 0.0209 | 0.0352 | Wald ratio | 1 | cis | NA |
| Melanoma | -0.213 | 0.103 | 0.0383 | Wald ratio | 1 | cis | NA |
| Primary sclerosing cholangitis  | -0.126 | 0.0618 | 0.0419 | Wald ratio | 1 | cis | NA |
| Amyotrophic lateral sclerosis | -0.0686 | 0.0347 | 0.0477 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertension | 0.0152 | 0.00786 | 0.0527 | Wald ratio | 1 | cis | NA |
| _...and 93 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3613_62_5` | FCN1 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_114 association rows across 48 traits (103 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| FCN1 protein levels | 3e-293 | rs150625869 | 19 | GCST90469203 | no MR -> candidate analysis |
| FCN2 protein levels | 9e-173 | rs3012792 | 28 | GCST90469204 | no MR -> candidate analysis |
| Semaphorin-4A levels | 3e-161 | rs11103604 | 2 | GCST90249488 | no MR -> candidate analysis |
| Ficolin-1 levels (FCN1.3613.62.5) | 2e-106 | rs11103602 | 2 | GCST90241184 | no MR -> candidate analysis |
| Ficolin-2 levels | 3e-106 | rs75430132 | 2 | GCST90247615 | no MR -> candidate analysis |
| Serum levels of protein FCN1 | 3e-98 | rs7873100 | 2 | GCST90088459 | no MR -> candidate analysis |
| Blood protein levels | 4e-66 | rs11103604 | 1 | GCST006585 | no MR -> candidate analysis |
| Ficolin-1 levels | 1e-64 | rs11103604 | 7 | GCST90161856 | no MR -> candidate analysis |
| Kidney-associated antigen 1 levels | 3e-43 | rs1038193 | 2 | GCST90248152 | no MR -> candidate analysis |
| Circulating TNFRSF10C levels | 1e-26 | rs10858304 | 1 | GCST90859942 | no MR -> candidate analysis |
| Neutrophil count | 1e-24 | rs1038193 | 3 | GCST90002351 | no MR -> candidate analysis |
| White blood cell count | 5e-22 | rs1038193 | 5 | GCST90002374 | no MR -> candidate analysis |
| _...and 36 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 256 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| ovarian neoplasm | 0.521 | — | common-variant locus | no MR -> candidate analysis |
| insomnia | 0.502 | — | common-variant locus | no MR -> candidate analysis |
| musculoskeletal system disorder | 0.5 | — | common-variant locus | no MR -> candidate analysis |
| major depressive disorder | 0.476 | — | common-variant locus | MR: beta=0.0752, p=0.0632 (cis) |
| gestational diabetes | 0.469 | — | common-variant locus | no MR -> candidate analysis |
| contact dermatitis | 0.438 | — | common-variant locus | no MR -> candidate analysis |
| temporomandibular joint disorder | 0.057 | — | common-variant locus | no MR -> candidate analysis |

> Of the 7 rows above, **6 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=6e-17, LOEUF=1.53 — LoF-tolerant |
| GWAS Catalog | 132 unique SNPs / 292 rows |
| ClinVar | 129 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 256 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'FCN1'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 129 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 48 traits by best p-value, aggregated from 114 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O00602 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000085265/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/FCN1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/FCN1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=FCN1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/FCN1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:37:59  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
