# Protein Dossier — FCN3 (Ficolin-3)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: hypertension | 0.0475 | 0.00984 | 1.37e-06 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | -0.0238 | 0.00783 | 0.00242 | Wald ratio | 1 | cis | NA |
| Alcohol intake frequency | 0.0252 | 0.00895 | 0.00485 | Wald ratio | 1 | cis | NA |
| Systolic blood pressure  automated reading | 0.0173 | 0.00618 | 0.00504 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R55 Syncope and collapse | 0.143 | 0.0558 | 0.0104 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: osteoporosis | 0.111 | 0.0436 | 0.011 | Wald ratio | 1 | cis | NA |
| Serum creatinine (eGFRcrea) | 0.00517 | 0.00209 | 0.0136 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I48 Atrial fibrillation and flutter | 0.12 | 0.051 | 0.019 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: depression | -0.0622 | 0.0266 | 0.0192 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M72 Fibroblastic disorders | -0.245 | 0.107 | 0.0216 | Wald ratio | 1 | cis | NA |
| Fasting insulin | 0.0154 | 0.0067 | 0.0219 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertrophic cardiomyopathy (hcm  or  hocm) | 0.573 | 0.258 | 0.0265 | Wald ratio | 1 | cis | NA |
| _...and 108 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3811_1_2` | Ficolin-3 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_13 association rows across 9 traits (13 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Ficolin-3 levels | 7e-186 | rs532781899 | 4 | GCST90247616 | no MR -> candidate analysis |
| Circulating MASP1 levels | 1e-129 | rs58337722 | 2 | GCST90860240 | no MR -> candidate analysis |
| MASP1 protein levels | 1e-51 | rs141300199 | 1 | GCST90469863 | no MR -> candidate analysis |
| Ficolin-3 level in Chronic kidney disease with hypertension  | 8e-27 | rs72882750 | 1 | GCST90237943 | no MR -> candidate analysis |
| Ficolin-3 level in Chronic kidney disease with hypertension  | 1e-20 | rs72882750 | 1 | GCST90234172 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 3e-20 | rs28385651 | 1 | GCST90838669 | no MR -> candidate analysis |
| Mannan-binding lectin serine protease 1 levels | 8e-14 | rs28357092 | 1 | GCST90161850 | no MR -> candidate analysis |
| NPTX1 protein levels | 5e-12 | rs141300199 | 1 | GCST90470078 | no MR -> candidate analysis |
| FCN3 protein levels | 4e-9 | rs10794501 | 1 | GCST90453028 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 232 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| immunodeficiency due to ficolin3 deficiency | 0.607 | — | established (curated) | no MR -> candidate analysis |
| rheumatic heart disease | 0.35 | — | established (curated) | no MR -> candidate analysis |
| microcephaly | 0.182 | — | established (curated) | no MR -> candidate analysis |
| gout | 0.127 | — | common-variant locus | no MR -> candidate analysis |
| hypertensive disorder | 0.091 | — | common-variant locus | no MR -> candidate analysis |

> Of the 5 rows above, **5 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=2.9e-09, LOEUF=1.22 — LoF-tolerant |
| GWAS Catalog | 37 unique SNPs / 74 rows |
| ClinVar | 93 records; 4 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 232 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'FCN3'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 93 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 9 of 9 traits by best p-value, aggregated from 13 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O75636 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000142748/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/FCN3 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/FCN3 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=FCN3%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/FCN3 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:38:34  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
