# Protein Dossier — FCN2 (Ficolin-2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| ER-positive Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | 0.0525 | 0.0158 | 9.06e-04 | Inverse variance weighted | 2 | cis | NA |
| ER-positive Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | 0.0525 | 0.0158 | 9.06e-04 | Inverse variance weighted | 2 | trans | NA |
| Diagnoses - main ICD10: M17 Gonarthrosis [arthrosis of knee] | 0.0973 | 0.0307 | 0.00154 | Inverse variance weighted | 2 | cis | NA |
| Diagnoses - main ICD10: M17 Gonarthrosis [arthrosis of knee] | 0.0973 | 0.0307 | 0.00154 | Inverse variance weighted | 2 | trans | NA |
| Red blood cell count | 0.0248 | 0.00851 | 0.00359 | Wald ratio | 1 | trans | NA |
| Small vessel disease | -0.334 | 0.126 | 0.0082 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: G56 Mononeuropathies of upper limb | -0.0973 | 0.0395 | 0.0136 | Inverse variance weighted | 2 | cis | NA |
| Diagnoses - main ICD10: G56 Mononeuropathies of upper limb | -0.0973 | 0.0395 | 0.0136 | Inverse variance weighted | 2 | trans | NA |
| Forced vital capacity (FVC) | -0.00937 | 0.00386 | 0.0152 | Inverse variance weighted | 2 | cis | NA |
| Forced vital capacity (FVC) | -0.00937 | 0.00386 | 0.0152 | Inverse variance weighted | 2 | trans | NA |
| Non-cancer illness code  self-reported: hypertension | 0.0187 | 0.00787 | 0.0174 | Inverse variance weighted | 2 | cis | NA |
| Non-cancer illness code  self-reported: hypertension | 0.0187 | 0.00787 | 0.0174 | Inverse variance weighted | 2 | trans | NA |
| _...and 155 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3313_21_2` | FCN2 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_69 association rows across 31 traits (63 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating FCN2 levels | 7e-2318 | rs7041446 | 5 | GCST90860487 | no MR -> candidate analysis |
| Ficolin-2 levels | 1e-645 | rs7851696 | 10 | GCST90247615 | no MR -> candidate analysis |
| Serum levels of protein FCN2 | 2e-305 | rs12685659 | 5 | GCST90087631 | no MR -> candidate analysis |
| Ficolin-1 levels | 3e-255 | rs7037264 | 1 | GCST90247614 | no MR -> candidate analysis |
| Ficolin-2 (analyte X13717.15) levels | 5e-215 | rs7037264 | 1 | GCST90422320 | no MR -> candidate analysis |
| Blood protein levels | 1e-164 | rs12685659 | 2 | GCST006585 | no MR -> candidate analysis |
| FCN2 protein levels | 2e-125 | rs7041446 | 14 | GCST90453290 | no MR -> candidate analysis |
| FCN1 protein levels | 3e-102 | rs17514136 | 3 | GCST90469203 | no MR -> candidate analysis |
| SUN domain-containing protein 3 levels | 2e-100 | rs7041446 | 2 | GCST90249734 | no MR -> candidate analysis |
| Ficolin-2 (analyte X3313.21) levels | 7e-97 | rs4521835 | 1 | GCST90425688 | no MR -> candidate analysis |
| Ficolin-2 levels (FCN2.3313.21.2) | 4e-72 | rs57136797 | 3 | GCST90241185 | no MR -> candidate analysis |
| Mannan-binding lectin serine protease 1 levels | 6e-68 | rs7041446 | 2 | GCST90248429 | no MR -> candidate analysis |
| _...and 19 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 249 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| hypopituitarism | 0.389 | — | common-variant locus | MR: beta=-0.376, p=0.425 (cis) |
| male infertility | 0.104 | — | common-variant locus | no MR -> candidate analysis |
| major depressive disorder | 0.062 | — | common-variant locus | MR: beta=-0.0618, p=0.427 (trans) |
| musculoskeletal system disorder | 0.058 | — | common-variant locus | no MR -> candidate analysis |
| insomnia | 0.053 | — | common-variant locus | no MR -> candidate analysis |
| pernicious anemia | 0.045 | — | common-variant locus | no MR -> candidate analysis |

> Of the 6 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=8.8e-11, LOEUF=1.29 — LoF-tolerant |
| GWAS Catalog | 109 unique SNPs / 236 rows |
| ClinVar | 121 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 2 clinical annotations across 1 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 249 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'FCN2'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 121 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 20 of 31 traits by best p-value, aggregated from 69 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q15485 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000160339/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/FCN2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/FCN2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=FCN2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=FCN2 — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/FCN2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:38:22  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
