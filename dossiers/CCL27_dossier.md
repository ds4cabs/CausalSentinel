# Protein Dossier — CCL27 (C-C motif chemokine 27)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Serum creatinine (eGFRcrea) | -0.0131 | 0.00467 | 0.00511 | Wald ratio | 1 | cis | NA |
| Cough on most days | 0.155 | 0.0561 | 0.00567 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R10 Abdominal and pelvic pain | 0.146 | 0.0534 | 0.00638 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: sleep apnoea | 0.415 | 0.157 | 0.00809 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertension | 0.0508 | 0.0207 | 0.014 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: enlarged prostate | 0.216 | 0.0887 | 0.0148 | Wald ratio | 1 | cis | NA |
| Body fat | -0.0692 | 0.0287 | 0.0158 | Wald ratio | 1 | cis | NA |
| Alcohol intake frequency | -0.0453 | 0.0189 | 0.0164 | Wald ratio | 1 | cis | NA |
| Birth weight | 0.0467 | 0.0199 | 0.0191 | Wald ratio | 1 | cis | NA |
| Depressive symptoms | -0.0436 | 0.0187 | 0.0196 | Wald ratio | 1 | cis | NA |
| Systemic lupus erythematosus | -0.599 | 0.26 | 0.021 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | 0.115 | 0.0507 | 0.0233 | Wald ratio | 1 | cis | NA |
| _...and 97 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2192_63_10` | CTACK | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_11 association rows across 9 traits (9 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating CCL27 levels | 2e-98 | rs2812349 | 1 | GCST90860726 | no MR -> candidate analysis |
| C-C motif chemokine 27 levels | 6e-20 | rs867811 | 2 | GCST90137615 | no MR -> candidate analysis |
| Serum levels of protein PAPLN | 7e-13 | rs72737145 | 1 | GCST90086640 | no MR -> candidate analysis |
| Interleukin-11 receptor subunit alpha (analyte X3814.63) lev | 3e-11 | rs78600552 | 1 | GCST90425887 | no MR -> candidate analysis |
| Noncognitive aspects of educational attainment | 2e-9 | rs6476459 | 1 | GCST90011874 | no MR -> candidate analysis |
| Core binding factor acute myeloid leukemia | 7e-9 | rs3176820; rs2772559; rs3176818; rs3176817; rs3176813 | 2 | GCST008413 | no MR -> candidate analysis |
| Height at take-off | 1e-8 | rs2026118 | 1 | GCST90567945 | no MR -> candidate analysis |
| Baseline memory in normal cognition | 6e-6 | rs913835 | 1 | GCST90448423 | no MR -> candidate analysis |
| Height | 7e-6 | rs2026118 | 1 | GCST90567944 | MR: beta=0.0202, p=0.194 (cis) |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.00091, LOEUF=1.88 — LoF-tolerant |
| GWAS Catalog | 59 unique SNPs / 118 rows |
| ClinVar | 98 records; 10 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 498 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'CCL27'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 98 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 9 of 9 traits by best p-value, aggregated from 11 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9Y4X3 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000213927/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CCL27 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CCL27 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CCL27%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CCL27 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:37:02  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
