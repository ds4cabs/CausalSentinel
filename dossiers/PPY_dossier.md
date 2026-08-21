# Protein Dossier — PPY (Pancreatic polypeptide prohormone)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Cancer code  self-reported: small intestine or small bowel cancer | 0.815 | 0.278 | 0.00338 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: hypertension | -0.0589 | 0.022 | 0.00733 | Wald ratio | 1 | trans | NA |
| Birth weight | 0.05 | 0.0211 | 0.018 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: vitiligo | 0.841 | 0.37 | 0.0231 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: K20 Oesophagitis | 0.221 | 0.0995 | 0.0263 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: N81 Female genital prolapse | -0.313 | 0.142 | 0.0275 | Wald ratio | 1 | trans | NA |
| Eye problems or disorders: Injury or trauma resulting in loss of vision | 0.264 | 0.124 | 0.0326 | Wald ratio | 1 | trans | NA |
| Systolic blood pressure  automated reading | -0.0262 | 0.0124 | 0.0353 | Wald ratio | 1 | trans | NA |
| ER-negative Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.138 | 0.066 | 0.0364 | Wald ratio | 1 | trans | NA |
| Diastolic blood pressure  automated reading | -0.0258 | 0.0125 | 0.0385 | Wald ratio | 1 | trans | NA |
| Cancer code  self-reported: prostate cancer | 0.233 | 0.114 | 0.0411 | Wald ratio | 1 | trans | NA |
| Vascular or heart problems diagnosed by doctor: Angina | 0.122 | 0.0605 | 0.0446 | Wald ratio | 1 | trans | NA |
| _...and 51 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-4588_1_2` | PH | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_No GWAS Catalog associations mapped to this gene._

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 307 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| pathological myopia | 0.122 | — | common-variant locus | no MR -> candidate analysis |

> Of the 1 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.029, LOEUF=1.27 — LoF-tolerant |
| GWAS Catalog | 57 unique SNPs / 114 rows |
| ClinVar | 24 records; 9 pathogenic in sample of 24 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 307 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'PPY'.
- **`clinvar`** — Pathogenic count is over the 24 record(s) retrieved, NOT over all 24 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — No GWAS Catalog associations mapped to this gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P01298 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000108849/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PPY — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PPY — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PPY%5Bgene%5D — _ClinVar build Build260809-1055.1_

## Provenance

- Generated: 2026-08-14T04:35:24  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
