# Protein Dossier — CDNF (Cerebral dopamine neurotrophic factor)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Eczema | -0.303 | 0.111 | 0.00641 | Wald ratio | 1 | cis | NA |
| Clear cell ovarian cancer | -0.492 | 0.204 | 0.016 | Wald ratio | 1 | cis | NA |
| Neuroticism | -0.0381 | 0.0159 | 0.0164 | Wald ratio | 1 | cis | NA |
| Invasive mucinous ovarian cancer | -0.488 | 0.205 | 0.0173 | Wald ratio | 1 | cis | NA |
| Depressive symptoms | -0.0413 | 0.0191 | 0.0303 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: G56 Mononeuropathies of upper limb | -0.193 | 0.103 | 0.0604 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M72 Fibroblastic disorders | 0.226 | 0.122 | 0.0638 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: C61 Malignant neoplasm of prostate | 0.2 | 0.112 | 0.0749 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: vitiligo | 0.7 | 0.394 | 0.0755 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: enlarged prostate | 0.145 | 0.0822 | 0.0785 | Wald ratio | 1 | cis | NA |
| Endometrioid ovarian cancer | -0.269 | 0.153 | 0.0786 | Wald ratio | 1 | cis | NA |
| Myocardial infarction | -0.122 | 0.0709 | 0.0847 | Wald ratio | 1 | cis | NA |
| _...and 56 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-4962_52_1` | ARMEL | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_17 association rows across 11 traits (15 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Cerebral dopamine neurotrophic factor levels | 3e-219 | rs61738953 | 5 | GCST90246967 | no MR -> candidate analysis |
| Circulating CDNF levels | 1e-210 | rs55884544 | 3 | GCST90860549 | no MR -> candidate analysis |
| Cyclic AMP-dependent transcription factor ATF-6 alpha levels | 2e-97 | rs61738953 | 1 | GCST90246610 | no MR -> candidate analysis |
| Serum levels of protein CDNF | 9e-38 | rs61738953 | 1 | GCST90088828 | no MR -> candidate analysis |
| Cyclic AMP-dependent transcription factor ATF-6 alpha levels | 5e-29 | rs61738953 | 1 | GCST90240816 | no MR -> candidate analysis |
| Serum levels of protein ATF6 | 4e-24 | rs61738953 | 1 | GCST90086655 | no MR -> candidate analysis |
| Cerebral dopamine neurotrophic factor levels (CDNF.4962.52.1 | 3e-20 | rs61738953 | 1 | GCST90240675 | no MR -> candidate analysis |
| Total PHF-tau (SNP x SNP interaction) | 1e-13 | rs2163935 x rs7091494 | 1 | GCST010340 | no MR -> candidate analysis |
| Peyronie's disease (PheCode 604.3) | 2e-11 | rs1051993455 | 1 | GCST90480417 | no MR -> candidate analysis |
| Ovarian dysfunction in childhood cancer survivors | 8e-7 | rs116926206 | 1 | GCST90838701 | no MR -> candidate analysis |
| Parental extreme longevity (95 years and older) | 6e-6 | rs149930776 | 1 | GCST003395 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 491 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Peyronie disease | 0.416 | — | common-variant locus | no MR -> candidate analysis |

> Of the 1 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.012, LOEUF=1.06 — LoF-tolerant |
| GWAS Catalog | 24 unique SNPs / 48 rows |
| ClinVar | 29 records; 17 pathogenic in sample of 29 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 491 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'CDNF'.
- **`clinvar`** — Pathogenic count is over the 29 record(s) retrieved, NOT over all 29 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 11 of 11 traits by best p-value, aggregated from 17 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q49AH0 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000185267/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CDNF — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CDNF — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CDNF%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CDNF — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:45:40  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
