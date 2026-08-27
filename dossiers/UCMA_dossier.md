# Protein Dossier — UCMA (Unique cartilage matrix-associated protein)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: pneumothorax | 0.605 | 0.188 | 0.00125 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: migraine | -0.0992 | 0.043 | 0.0211 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N81 Female genital prolapse | -0.15 | 0.0656 | 0.0221 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: basal cell carcinoma | 0.139 | 0.0614 | 0.0235 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: S76 Injury of muscle and tendon at hip and thigh level | 0.466 | 0.212 | 0.0275 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: asthma | 0.0382 | 0.0181 | 0.0351 | Wald ratio | 1 | cis | NA |
| Alcohol intake frequency | 0.0194 | 0.00995 | 0.0514 | Wald ratio | 1 | cis | NA |
| Fasting proinsulin | -0.0597 | 0.0307 | 0.0518 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R07 Pain in throat and chest | 0.055 | 0.0284 | 0.0531 | Wald ratio | 1 | cis | NA |
| Autism | 0.161 | 0.0839 | 0.0544 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: vitiligo | 0.506 | 0.267 | 0.0581 | Wald ratio | 1 | cis | NA |
| Schizophrenia | -0.0568 | 0.031 | 0.0673 | Wald ratio | 1 | cis | NA |
| _...and 85 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_10 association rows across 6 traits (7 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Unique cartilage matrix-associated protein levels | 2e-147 | rs2399954 | 4 | GCST90421289 | no MR -> candidate analysis |
| Unique cartilage matrix-associated protein levels (UCMA.1097 | 3e-53 | rs2093847 | 2 | GCST90243285 | no MR -> candidate analysis |
| Total PHF-tau (SNP x SNP interaction) | 4e-8 | rs533555 x rs8083208 | 1 | GCST010340 | no MR -> candidate analysis |
| Gut microbiome abundance (class Clostridium sensu stricto sp | 2e-7 | rs113702951 | 1 | GCST90569029 | no MR -> candidate analysis |
| Cortical thickness | 4e-6 | rs605293 | 1 | GCST90104703 | no MR -> candidate analysis |
| Self-reported allergy | 7e-6 | rs10796051 | 1 | GCST002083 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 38 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| liver disorder | 0.463 | — | common-variant locus | no MR -> candidate analysis |
| pleural empyema | 0.461 | — | common-variant locus | no MR -> candidate analysis |
| foreign body | 0.461 | — | common-variant locus | no MR -> candidate analysis |
| pneumothorax | 0.461 | — | common-variant locus | MR: beta=0.605, p=0.00125 (cis) |
| thyroid cancer | 0.461 | — | common-variant locus | MR: beta=-0.223, p=0.25 (cis) |
| type 2 diabetes mellitus | 0.444 | — | common-variant locus | no MR -> candidate analysis |
| kidney transplant | 0.353 | — | common-variant locus | no MR -> candidate analysis |
| keratoconus | 0.182 | — | established (curated) | no MR -> candidate analysis |
| type 1 diabetes nephropathy | 0.038 | — | common-variant locus | no MR -> candidate analysis |
| neuroendocrine neoplasm | 0.036 | — | common-variant locus | no MR -> candidate analysis |

> Of the 10 rows above, **8 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1e-07, LOEUF=1.39 — LoF-tolerant |
| GWAS Catalog | 35 unique SNPs / 70 rows |
| ClinVar | 61 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 38 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'UCMA'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 61 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 6 of 6 traits by best p-value, aggregated from 10 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q8WVF2 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000165623/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/UCMA — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/UCMA — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=UCMA%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/UCMA — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:32:08  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
