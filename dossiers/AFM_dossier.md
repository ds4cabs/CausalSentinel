# Protein Dossier — AFM (Afamin)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Cancer code  self-reported: malignant melanoma | 0.235 | 0.0894 | 0.00865 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hayfever or allergic rhinitis | 0.0942 | 0.037 | 0.0109 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: basal cell carcinoma | -0.384 | 0.156 | 0.0138 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K35 Acute appendicitis | -0.662 | 0.307 | 0.0309 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertrophic cardiomyopathy (hcm  or  hocm) | 0.782 | 0.368 | 0.0337 | Wald ratio | 1 | cis | NA |
| Neo-extraversion | -0.735 | 0.35 | 0.0358 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: migraine | 0.105 | 0.0515 | 0.0422 | Wald ratio | 1 | cis | NA |
| HbA1C | -0.0277 | 0.0142 | 0.0501 | Wald ratio | 1 | cis | NA |
| Major depressive disorder | -0.16 | 0.0846 | 0.0588 | Wald ratio | 1 | cis | NA |
| Low grade serous ovarian cancer | -0.316 | 0.169 | 0.0609 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K20 Oesophagitis | -0.236 | 0.129 | 0.0665 | Wald ratio | 1 | cis | NA |
| Lung cancer | 0.107 | 0.0598 | 0.0739 | Wald ratio | 1 | cis | NA |
| _...and 86 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-4763_31_3` | Afamin | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_15 association rows across 9 traits (14 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Afamin levels | 3e-125 | rs72856641 | 5 | GCST90246450 | no MR -> candidate analysis |
| CXCL1 protein levels | 9e-52 | rs13131508 | 1 | GCST90468930 | no MR -> candidate analysis |
| AFM protein levels | 6e-23 | rs115264016 | 2 | GCST90468249 | no MR -> candidate analysis |
| Serum levels of protein AFM | 4e-20 | rs72853185 | 1 | GCST90088767 | no MR -> candidate analysis |
| CXCL6 protein levels | 1e-18 | rs139818614 | 1 | GCST90468933 | no MR -> candidate analysis |
| Insulin-like growth factor-binding protein 7 levels | 1e-15 | rs1289184022 | 1 | GCST90179322 | no MR -> candidate analysis |
| Prostate cancer | 5e-15 | rs1894292 | 2 | GCST006085 | no MR -> candidate analysis |
| Afamin level in Chronic kidney disease with hypertension and | 2e-13 | rs72856634 | 1 | GCST90237707 | no MR -> candidate analysis |
| Iris color (b* coordinate) | 4e-7 | rs12510870 | 1 | GCST005096 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 193 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Abnormality of the skeletal system | 0.531 | — | common-variant locus | no MR -> candidate analysis |
| prostate carcinoma | 0.482 | — | common-variant locus | no MR -> candidate analysis |
| adrenal gland disorder | 0.105 | — | common-variant locus | no MR -> candidate analysis |
| escherichia coli infection | 0.057 | — | common-variant locus | no MR -> candidate analysis |
| Disorder of lipid metabolism | 0.049 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.043 | — | common-variant locus | no MR -> candidate analysis |

> Of the 6 rows above, **6 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=7.2e-33, LOEUF=1.43 — LoF-tolerant |
| GWAS Catalog | 52 unique SNPs / 104 rows |
| ClinVar | 131 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 193 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'AFM'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 131 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 9 of 9 traits by best p-value, aggregated from 15 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P43652 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000079557/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/AFM — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/AFM — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=AFM%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/AFM — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T00:57:04  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
