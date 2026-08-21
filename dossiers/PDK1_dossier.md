# Protein Dossier — PDK1 ([Pyruvate dehydrogenase (acetyl-transferring)] kinase isozyme 1, mitochondrial)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Ferritin | 0.0607 | 0.0196 | 0.00195 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: prostate cancer | 0.154 | 0.0501 | 0.00218 | Wald ratio | 1 | cis | NA |
| Mean cell haemoglobin | 0.0567 | 0.0201 | 0.00484 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Other bones | 0.0472 | 0.0207 | 0.0223 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: enlarged prostate | -0.0993 | 0.0471 | 0.0351 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: D25 Leiomyoma of uterus | -0.0993 | 0.0486 | 0.0413 | Wald ratio | 1 | cis | NA |
| Red blood cell count | -0.00892 | 0.00437 | 0.0414 | Wald ratio | 1 | cis | NA |
| Forearm bone mineral density | 0.0616 | 0.0327 | 0.0596 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Glaucoma | 0.0726 | 0.0388 | 0.0612 | Wald ratio | 1 | cis | NA |
| Knee osteoarthritis | -0.102 | 0.0545 | 0.0616 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code self-reported: pulmonary embolism (with or without) dvt | 0.0934 | 0.0504 | 0.0638 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: high cholesterol | 0.0242 | 0.0131 | 0.0656 | Wald ratio | 1 | cis | NA |
| _...and 81 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-5227_60_3` | PDK1 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_7 association rows across 6 traits (3 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Height | 8e-12 | rs836624 | 2 | GCST90245848 | no MR -> candidate analysis |
| Insomnia | 4e-8 | rs836603 | 1 | GCST90131901 | no MR -> candidate analysis |
| Crohn's disease | 1e-6 | rs151175749 | 1 | GCST90446792 | no MR -> candidate analysis |
| Gastric cancer | 2e-6 | rs12693006 | 1 | GCST90455528 | no MR -> candidate analysis |
| Erectile dysfunction in type 1 diabetes | 2e-6 | rs836589 | 1 | GCST001572 | no MR -> candidate analysis |
| Behenoyl sphingomyelin (d18:1/22:0) levels in elite athletes | 6e-6 | rs12693006 | 1 | GCST90133880 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 488 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| prostate carcinoma | 0.657 | — | common-variant locus | no MR -> candidate analysis |
| brain cancer | 0.515 | — | common-variant locus | no MR -> candidate analysis |
| Crohn disease | 0.498 | — | common-variant locus | no MR -> candidate analysis |
| liver disorder | 0.484 | — | common-variant locus | no MR -> candidate analysis |
| prostate cancer | 0.197 | — | common-variant locus | MR: beta=0.154, p=0.00218 (cis) |
| mental disorder | 0.171 | — | common-variant locus | no MR -> candidate analysis |

> Of the 6 rows above, **5 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 2 known modulators (3-phosphoinositide-dependent protein kinase 1) |
| gnomAD constraint | pLI=4.7e-10, LOEUF=0.94 — LoF-tolerant |
| GWAS Catalog | 46 unique SNPs / 82 rows |
| ClinVar | 100 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 488 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'PDK1' and resolved to '3-phosphoinositide-dependent protein kinase 1' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 100 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 6 of 6 traits by best p-value, aggregated from 7 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q15118 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000152256/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2534/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PDK1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PDK1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PDK1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/PDK1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:16:30  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
