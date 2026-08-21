# Protein Dossier — IL27 (Interleukin-27 subunit alpha)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Crohn's disease | -0.666 | 0.0717 | 1.44e-20 | Wald ratio | 1 | cis | NA |
| Inflammatory bowel disease | -0.515 | 0.0597 | 6.42e-18 | Wald ratio | 1 | cis | NA |
| Ulcerative colitis | -0.296 | 0.075 | 8.05e-05 | Wald ratio | 1 | cis | NA |
| Juvenile idiopathic arthritis | -0.715 | 0.307 | 0.0198 | Wald ratio | 1 | cis | NA |
| Multiple sclerosis | 0.0986 | 0.097 | 0.309 | Wald ratio | 1 | cis | NA |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2829_19_2` | IL-27 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_96 association rows across 60 traits (81 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| APOBR protein levels | 3e-234 | rs12448270 | 2 | GCST90468334 | no MR -> candidate analysis |
| Circulating EBI3_IL27 levels | 1e-84 | rs181209 | 1 | GCST90859764 | no MR -> candidate analysis |
| Height | 1e-39 | rs28698667 | 2 | GCST90245848 | no MR -> candidate analysis |
| Circulating SULT1A1 levels | 1e-37 | rs12448270 | 1 | GCST90859907 | no MR -> candidate analysis |
| Drinks per week | 4e-32 | rs4788084 | 4 | GCST90243989 | no MR -> candidate analysis |
| Mean spheric corpuscular volume | 7e-30 | rs181205 | 1 | GCST90002397 | no MR -> candidate analysis |
| Chronic inflammatory diseases (ankylosing spondylitis, Crohn | 3e-29 | rs26528 | 1 | GCST005537 | no MR -> candidate analysis |
| Educational attainment (years of education) | 2e-28 | rs62034319 | 1 | GCST006442 | no MR -> candidate analysis |
| Glycated haemoglobin HbA1c levels (UKB data field 30750) | 4e-28 | rs181205 | 1 | GCST90468072 | no MR -> candidate analysis |
| monocyte (fraction, mean, inv-norm transformed) | 1e-26 | rs181207 | 2 | GCST90475511 | no MR -> candidate analysis |
| mean corpuscular hemoglobin concentration (MCHC, mean, inv-n | 3e-26 | rs181207 | 2 | GCST90475458 | no MR -> candidate analysis |
| Mean corpuscular volume (UKB data field 30040) | 8e-25 | rs4787458 | 1 | GCST90468086 | no MR -> candidate analysis |
| _...and 48 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 711 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Crohn disease | 0.72 | — | common-variant locus | no MR -> candidate analysis |
| obesity disorder | 0.569 | — | common-variant locus | no MR -> candidate analysis |
| leprosy | 0.533 | — | common-variant locus | no MR -> candidate analysis |
| cystic kidney disease | 0.481 | — | common-variant locus | no MR -> candidate analysis |
| overnutrition | 0.449 | — | common-variant locus | no MR -> candidate analysis |
| psoriasis | 0.406 | — | common-variant locus | no MR -> candidate analysis |
| ulcerative colitis | 0.406 | — | common-variant locus | MR: beta=-0.296, p=8.05e-05 (cis) |
| ankylosing spondylitis | 0.406 | — | common-variant locus | no MR -> candidate analysis |
| sclerosing cholangitis | 0.393 | — | common-variant locus | no MR -> candidate analysis |
| inflammatory bowel disease | 0.201 | — | common-variant locus | MR: beta=-0.515, p=6.42e-18 (cis) |
| type 1 diabetes mellitus | 0.138 | — | common-variant locus | no MR -> candidate analysis |
| ovarian dysfunction | 0.185 | — | common-variant locus | no MR -> candidate analysis |
| chronic obstructive pulmonary disease | 0.114 | — | common-variant locus | no MR -> candidate analysis |

> Of the 13 rows above, **11 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.34, LOEUF=0.673 — LoF-tolerant |
| GWAS Catalog | 109 unique SNPs / 253 rows |
| ClinVar | 131 records; 3 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 711 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'IL27'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 131 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 60 traits by best p-value, aggregated from 96 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q8NEV9 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000197272/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/IL27 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/IL27 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=IL27%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/IL27 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:15:35  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
