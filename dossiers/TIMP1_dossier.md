# Protein Dossier — TIMP1 (Metalloproteinase inhibitor 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: D12 Benign neoplasm of colon  rectum  anus and anal canal | 0.316 | 0.116 | 0.00656 | Wald ratio | 1 | trans | NA |
| Age at menopause | 0.367 | 0.138 | 0.00766 | Wald ratio | 1 | trans | NA |
| HbA1C | -0.0679 | 0.0257 | 0.00822 | Wald ratio | 1 | trans | NA |
| Cigarettes smoked per day | -1.58 | 0.613 | 0.00981 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: K29 Gastritis and duodenitis | 0.239 | 0.0957 | 0.0126 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: vaginal prolapse or uterine prolapse | 0.425 | 0.171 | 0.0128 | Wald ratio | 1 | trans | NA |
| Iron | 0.178 | 0.0752 | 0.0177 | Wald ratio | 1 | trans | NA |
| Knee osteoarthritis | -0.483 | 0.209 | 0.0205 | Wald ratio | 1 | trans | NA |
| Nucleus accumbens volume | 18.6 | 8.46 | 0.0282 | Wald ratio | 1 | trans | NA |
| Potassium in urine | -0.039 | 0.0188 | 0.0386 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: R11 Nausea and vomiting | 0.418 | 0.205 | 0.0409 | Wald ratio | 1 | trans | NA |
| Eye problems or disorders: Injury or trauma resulting in loss of vision | 0.354 | 0.177 | 0.0459 | Wald ratio | 1 | trans | NA |
| _...and 85 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2211_9_6` | TIMP-1 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_No GWAS Catalog associations mapped to this gene._

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.51, LOEUF=0.765 — LoF-tolerant |
| GWAS Catalog | 2 unique SNPs / 4 rows |
| ClinVar | 208 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 2170 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'TIMP1'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 208 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — No GWAS Catalog associations mapped to this gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P01033 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000102265/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/TIMP1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/TIMP1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=TIMP1%5Bgene%5D — _ClinVar build Build260809-1055.1_

## Provenance

- Generated: 2026-08-14T05:21:24  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
