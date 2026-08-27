# Protein Dossier — ART4 (Ecto-ADP-ribosyltransferase 4)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Heel bone mineral density (BMD) T-score  automated | -0.0213 | 0.00433 | 8.90e-07 | Wald ratio | 1 | cis | NA |
| Fractured or broken bones in last 5 years | 0.0454 | 0.00998 | 5.32e-06 | Wald ratio | 1 | cis | NA |
| Height | -0.0124 | 0.00405 | 0.00216 | Wald ratio | 1 | cis | NA |
| Lumbar spine bone mineral density | -0.0362 | 0.0121 | 0.00274 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Ankle | 0.0784 | 0.0264 | 0.003 | Wald ratio | 1 | cis | NA |
| Femoral neck bone mineral density | -0.0272 | 0.0104 | 0.00858 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: psoriasis | -0.0826 | 0.0343 | 0.0158 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Wrist | 0.0545 | 0.0226 | 0.016 | Wald ratio | 1 | cis | NA |
| Weight | -0.00698 | 0.00296 | 0.0182 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: osteoporosis | 0.0591 | 0.0253 | 0.0197 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: H25 Senile cataract | -0.0943 | 0.042 | 0.0248 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N81 Female genital prolapse | 0.0579 | 0.0264 | 0.0282 | Wald ratio | 1 | cis | NA |
| _...and 99 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_5 association rows across 5 traits (5 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Ecto-ADP-ribosyltransferase 4 levels | 9e-1651 | rs10772808 | 1 | GCST90246589 | no MR -> candidate analysis |
| Ecto-ADP-ribosyltransferase 4 levels (ART4.6576.1.3) | 1e-254 | rs1001096 | 1 | GCST90241017 | no MR -> candidate analysis |
| Ecto-ADP-ribosyltransferase 4 level in Chronic kidney diseas | 7e-63 | rs11056202 | 1 | GCST90238347 | no MR -> candidate analysis |
| Protrudin:Cytoplasmic domain, region 1, isoform 6 protein le | 4e-39 | rs12822851 | 1 | GCST90437421 | no MR -> candidate analysis |
| Hand grip strength | 1e-12 | rs2287226 | 1 | GCST005830 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 855 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| osteoarthritis, knee | 0.63 | — | common-variant locus | MR: beta=-0.0273, p=0.332 (cis) |
| preeclampsia | 0.548 | — | common-variant locus | no MR -> candidate analysis |
| total knee arthroplasty | 0.53 | — | common-variant locus | no MR -> candidate analysis |
| osteoarthritis, hand | 0.421 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.368 | — | common-variant locus | no MR -> candidate analysis |
| urolithiasis | 0.368 | — | common-variant locus | no MR -> candidate analysis |
| osteoarthritis, hip | 0.285 | — | common-variant locus | MR: beta=-0.0273, p=0.332 (cis) |
| polyarticular arthritis | 0.217 | — | common-variant locus | no MR -> candidate analysis |
| bone fracture | 0.144 | — | common-variant locus | no MR -> candidate analysis |
| musculoskeletal system disorder | 0.05 | — | common-variant locus | no MR -> candidate analysis |
| stomach disorder | 0.05 | — | common-variant locus | no MR -> candidate analysis |
| endometriosis | 0.04 | — | common-variant locus | no MR -> candidate analysis |

> Of the 12 rows above, **10 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.0031, LOEUF=0.904 — LoF-tolerant |
| GWAS Catalog | 48 unique SNPs / 96 rows |
| ClinVar | 89 records; 5 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 855 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'ART4'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 89 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 5 of 5 traits by best p-value, aggregated from 5 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q93070 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000111339/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/ART4 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/ART4 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=ART4%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/ART4 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:10:06  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
