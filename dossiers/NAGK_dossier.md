# Protein Dossier — NAGK (N-acetyl-D-glucosamine kinase)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Forearm bone mineral density | 0.135 | 0.0495 | 0.00657 | Wald ratio | 1 | cis | NA |
| Urinary albumin-to-creatinine ratio | 0.0463 | 0.0187 | 0.0135 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: osteoarthritis | -0.0664 | 0.0277 | 0.0166 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N40 Hyperplasia of prostate | 0.159 | 0.0691 | 0.0211 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: D12 Benign neoplasm of colon  rectum  anus and anal canal | 0.131 | 0.0575 | 0.0227 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Glaucoma | -0.172 | 0.0771 | 0.0261 | Wald ratio | 1 | cis | NA |
| Eczema | -0.125 | 0.0575 | 0.0291 | Wald ratio | 1 | cis | NA |
| Red blood cell count | 0.0141 | 0.00648 | 0.0294 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: G56 Mononeuropathies of upper limb | 0.114 | 0.0527 | 0.0306 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K57 Diverticular disease of intestine | 0.105 | 0.0492 | 0.0334 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: H25 Senile cataract | -0.243 | 0.114 | 0.0336 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: J33 Nasal polyp | 0.191 | 0.0938 | 0.0416 | Wald ratio | 1 | cis | NA |
| _...and 102 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3894_15_2` | NAGK | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_23 association rows across 14 traits (20 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| NAGK protein levels | 6e-206 | rs11680831 | 1 | GCST90469995 | no MR -> candidate analysis |
| Serum levels of protein NAGK | 1e-102 | rs2287327 | 1 | GCST90088573 | no MR -> candidate analysis |
| Blood protein levels | 2e-57 | rs2287327 | 1 | GCST006585 | no MR -> candidate analysis |
| N-acetyl-D-glucosamine kinase levels (NAGK.3894.15.2) | 9e-36 | rs11680831 | 1 | GCST90242001 | no MR -> candidate analysis |
| N-acetyl-D-glucosamine kinase levels | 1e-34 | rs1861853 | 6 | GCST90248577 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 9e-24 | rs56693109 | 1 | GCST90838669 | no MR -> candidate analysis |
| Eosinophil count | 2e-14 | rs2160783 | 5 | GCST90002298 | no MR -> candidate analysis |
| Height (baseline) | 5e-13 | rs10198989 | 1 | GCST90565843 | no MR -> candidate analysis |
| Eosinophil percentage of white cells | 3e-12 | rs2160783 | 1 | GCST90002382 | no MR -> candidate analysis |
| Body size or adipose distribution (multivariate analysis) | 2e-11 | rs10198989 | 1 | GCST90624105 | no MR -> candidate analysis |
| B-cell differentiation antigen CD72 protein levels (SomaScan | 3e-10 | rs2287331 | 1 | GCST90441219 | no MR -> candidate analysis |
| Reaction time | 7e-7 | rs560576410 | 1 | GCST006268 | no MR -> candidate analysis |
| _...and 2 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 92 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| response to xenobiotic stimulus | 0.195 | — | common-variant locus | no MR -> candidate analysis |
| male reproductive organ cancer | 0.062 | — | common-variant locus | no MR -> candidate analysis |
| secondary malignant neoplasm | 0.041 | — | common-variant locus | no MR -> candidate analysis |
| type 1 diabetes nephropathy | 0.036 | — | common-variant locus | no MR -> candidate analysis |

> Of the 4 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (N-acetyl-D-glucosamine kinase) |
| gnomAD constraint | pLI=2e-10, LOEUF=1.08 — LoF-tolerant |
| GWAS Catalog | 48 unique SNPs / 94 rows |
| ClinVar | 102 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 92 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'NAGK' and resolved to 'N-acetyl-D-glucosamine kinase' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 102 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 14 of 14 traits by best p-value, aggregated from 23 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9UJ70 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000124357/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4295978/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/NAGK — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/NAGK — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=NAGK%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/NAGK — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:54:45  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
