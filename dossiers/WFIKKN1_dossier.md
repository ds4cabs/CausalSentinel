# Protein Dossier — WFIKKN1 (WAP, Kazal, immunoglobulin, Kunitz and NTR domain-containing protein 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: R07 Pain in throat and chest | 0.142 | 0.0566 | 0.012 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K20 Oesophagitis | 0.274 | 0.114 | 0.0158 | Wald ratio | 1 | cis | NA |
| Alzheimer's disease | 0.22 | 0.0985 | 0.0254 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: muscle or soft tissue injuries | 0.292 | 0.131 | 0.026 | Wald ratio | 1 | cis | NA |
| Height | 0.0399 | 0.0182 | 0.0286 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K29 Gastritis and duodenitis | 0.169 | 0.0802 | 0.0355 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: deep venous thrombosis (dvt) | -0.298 | 0.143 | 0.0368 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: asthma | -0.0916 | 0.0448 | 0.0409 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | 0.0257 | 0.0126 | 0.0413 | Wald ratio | 1 | cis | NA |
| Urinary albumin-to-creatinine ratio | 0.0739 | 0.0365 | 0.0427 | Wald ratio | 1 | cis | NA |
| Subjective well being | 0.0394 | 0.0197 | 0.0455 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: diverticular disease or diverticulitis | 0.217 | 0.113 | 0.0543 | Wald ratio | 1 | cis | NA |
| _...and 91 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3191_50_2` | WFKN1 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_12 association rows across 9 traits (10 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating WFIKKN1 levels | 1e-271 | rs17139376 | 3 | GCST90859694 | no MR -> candidate analysis |
| Height | 1e-253 | rs4984903 | 2 | GCST90245848 | MR: beta=0.0399, p=0.0286 (cis) |
| MSLN protein levels | 2e-40 | rs374542712 | 1 | GCST90469948 | no MR -> candidate analysis |
| Body size or adipose distribution (multivariate analysis) | 7e-25 | rs4984903 | 1 | GCST90624105 | no MR -> candidate analysis |
| Mean corpuscular haemoglobin concentration (UKB data field 3 | 1e-24 | rs35800913 | 1 | GCST90468085 | no MR -> candidate analysis |
| HBQ1 protein levels | 6e-13 | rs9929621 | 1 | GCST90469434 | no MR -> candidate analysis |
| Height (standard GWA) | 2e-10 | rs10153076 | 1 | GCST90267284 | no MR -> candidate analysis |
| Cystatin C levels in bottom 99% of individuals by creatinine | 3e-8 | rs34080030 | 1 | GCST90566734 | no MR -> candidate analysis |
| Height (weighted GWA) | 2e-7 | rs10153076 | 1 | GCST90267285 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.0021, LOEUF=2.59 — LoF-tolerant |
| GWAS Catalog | 122 unique SNPs / 302 rows |
| ClinVar | 219 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 664 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'WFIKKN1'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 219 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 9 of 9 traits by best p-value, aggregated from 12 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q96NZ8 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000127578/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/WFIKKN1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/WFIKKN1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=WFIKKN1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/WFIKKN1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:37:50  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
