# Protein Dossier — ANXA2 (Annexin A2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Age at menarche | -0.0351 | 0.00894 | 8.90e-05 | Wald ratio | 1 | cis | NA |
| Weight | -0.0105 | 0.00317 | 8.68e-04 | Wald ratio | 1 | cis | NA |
| Amygdala volume | -9.2 | 3.48 | 0.00813 | Wald ratio | 1 | cis | NA |
| Birth weight | -0.0133 | 0.00557 | 0.0169 | Wald ratio | 1 | cis | NA |
| HOMA-IR | 0.0144 | 0.00608 | 0.0176 | Wald ratio | 1 | cis | NA |
| Fasting proinsulin | 0.0237 | 0.0102 | 0.0202 | Wald ratio | 1 | cis | NA |
| Putamen volume | -20.5 | 8.89 | 0.021 | Wald ratio | 1 | cis | NA |
| Platelet count | -1.39 | 0.603 | 0.0212 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | -0.00792 | 0.00359 | 0.0271 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: C50 Malignant neoplasm of breast | 0.0582 | 0.0265 | 0.0279 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: anxiety or panic attacks | 0.0626 | 0.029 | 0.0312 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: high cholesterol | -0.0208 | 0.0099 | 0.0359 | Wald ratio | 1 | cis | NA |
| _...and 107 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-4961_17_1` | annexin II | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_50 association rows across 31 traits (36 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Annexin A2 levels | 6e-987 | rs8033800 | 8 | GCST90246522 | no MR -> candidate analysis |
| ANXA2 protein levels | 7e-99 | rs6494191 | 11 | GCST90468317 | no MR -> candidate analysis |
| KLRB1 protein levels | 3e-23 | rs11071528 | 1 | GCST90469709 | no MR -> candidate analysis |
| Height | 3e-17 | rs8040209 | 2 | GCST90245848 | MR: beta=-0.00567, p=0.211 (cis) |
| Circulating FLT4 levels | 2e-15 | rs17845226 | 1 | GCST90860081 | no MR -> candidate analysis |
| FLT4 protein levels | 8e-15 | rs17845226 | 1 | GCST90469252 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 9e-14 | rs11071528 | 1 | GCST90838669 | no MR -> candidate analysis |
| Serum levels of protein ANXA2 | 6e-13 | rs61381915 | 1 | GCST90088827 | no MR -> candidate analysis |
| Blood protein levels | 2e-10 | rs61381915 | 1 | GCST006585 | no MR -> candidate analysis |
| Total PHF-tau (SNP x SNP interaction) | 2e-10 | rs10196561 x rs2414660 | 1 | GCST010340 | no MR -> candidate analysis |
| Bioavailable testosterone levels | 2e-9 | rs12437778 | 1 | GCST90027085 | no MR -> candidate analysis |
| Bcl-2-like protein 11 protein levels (SomaScan ID:13700-10) | 3e-9 | rs12440452 | 1 | GCST90438342 | no MR -> candidate analysis |
| _...and 19 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 697 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| benign urinary system neoplasm | 0.486 | — | common-variant locus | no MR -> candidate analysis |
| multiple sclerosis | 0.035 | — | common-variant locus | no MR -> candidate analysis |
| ovarian neoplasm | 0.447 | — | common-variant locus | no MR -> candidate analysis |
| Hallux valgus | 0.388 | — | common-variant locus | no MR -> candidate analysis |
| myasthenia gravis | 0.384 | — | common-variant locus | no MR -> candidate analysis |
| biliary tract disorder | 0.377 | — | common-variant locus | no MR -> candidate analysis |
| diabetes mellitus | 0.352 | — | common-variant locus | no MR -> candidate analysis |
| mastodynia | 0.355 | — | common-variant locus | no MR -> candidate analysis |

> Of the 8 rows above, **8 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Annexin A2) |
| gnomAD constraint | pLI=1.1e-05, LOEUF=0.812 — LoF-tolerant |
| GWAS Catalog | 66 unique SNPs / 113 rows |
| ClinVar | 69 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 697 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'ANXA2' and resolved to 'Annexin A2' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 69 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 31 traits by best p-value, aggregated from 50 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P07355 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000182718/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL1764938/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/ANXA2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/ANXA2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=ANXA2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/ANXA2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:04:43  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
