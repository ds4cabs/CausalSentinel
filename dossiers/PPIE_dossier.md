# Protein Dossier — PPIE (Peptidyl-prolyl cis-trans isomerase E)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Body mass index (BMI) | -0.0185 | 0.00648 | 0.00424 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: vaginal prolapse or uterine prolapse | 0.182 | 0.0737 | 0.0138 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertrophic cardiomyopathy (hcm  or  hocm) | 0.621 | 0.265 | 0.019 | Wald ratio | 1 | cis | NA |
| Subjective well being | 0.0183 | 0.00783 | 0.0196 | Wald ratio | 1 | cis | NA |
| Glioma | 0.267 | 0.119 | 0.0253 | Wald ratio | 1 | cis | NA |
| Urinary albumin-to-creatinine ratio | 0.0444 | 0.0201 | 0.0273 | Wald ratio | 1 | cis | NA |
| Diastolic blood pressure  automated reading | -0.0147 | 0.00664 | 0.0273 | Wald ratio | 1 | cis | NA |
| Endometrioid ovarian cancer | 0.174 | 0.0799 | 0.0295 | Wald ratio | 1 | cis | NA |
| Amygdala volume | 13.6 | 6.27 | 0.0305 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N81 Female genital prolapse | 0.105 | 0.0489 | 0.0312 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: diverticular disease or diverticulitis | 0.115 | 0.0548 | 0.0366 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | 0.0173 | 0.00838 | 0.0394 | Wald ratio | 1 | cis | NA |
| _...and 92 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-5238_26_3` | PPIE | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_14 association rows across 9 traits (11 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Peptidyl-prolyl cis-trans isomerase E levels | 5e-240 | rs514868 | 6 | GCST90249094 | no MR -> candidate analysis |
| Peptidyl-prolyl cis-trans isomerase E levels (PPIE.5238.26.3 | 5e-53 | rs12086750 | 1 | GCST90242217 | no MR -> candidate analysis |
| Serum levels of protein PPIE | 8e-44 | rs3738673 | 1 | GCST90088971 | no MR -> candidate analysis |
| Blood protein levels | 4e-25 | rs1046988 | 1 | GCST006585 | no MR -> candidate analysis |
| High-density lipoprotein levels (MTAG) | 1e-12 | rs72665235 | 1 | GCST90179147 | no MR -> candidate analysis |
| Heel bone mineral density | 9e-10 | rs76571594 | 1 | GCST007066 | MR: beta=0.0173, p=0.0394 (cis) |
| Gut microbiome abundance (class Bacteroides thetaiotaomicron | 6e-8 | rs16826510 | 1 | GCST90568673 | no MR -> candidate analysis |
| Bone mineral density (Ward's triangle area) | 4e-6 | rs11577371 | 1 | GCST003654 | no MR -> candidate analysis |
| Cold sores | 7e-6 | rs506424 | 1 | GCST005000 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 75 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| diabetes mellitus | 0.15 | — | common-variant locus | no MR -> candidate analysis |
| sleep apnea syndrome | 0.069 | — | common-variant locus | no MR -> candidate analysis |
| Abnormality of the gastrointestinal tract | 0.05 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Peptidyl-prolyl cis-trans isomerase E) |
| gnomAD constraint | pLI=0.0024, LOEUF=0.757 — LoF-tolerant |
| GWAS Catalog | 64 unique SNPs / 105 rows |
| ClinVar | 91 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 75 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'PPIE' and resolved to 'Peptidyl-prolyl cis-trans isomerase E' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 91 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 9 of 9 traits by best p-value, aggregated from 14 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9UNP9 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000084072/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL6066227/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PPIE — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PPIE — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PPIE%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/PPIE — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:34:15  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
