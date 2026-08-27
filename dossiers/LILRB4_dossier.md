# Protein Dossier — LILRB4 (Leukocyte immunoglobulin-like receptor subfamily B member 4)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Fasting proinsulin | -0.136 | 0.0394 | 5.80e-04 | Wald ratio | 1 | trans | NA |
| Height | -0.0508 | 0.0165 | 0.00209 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: hypertension | 0.065 | 0.0212 | 0.00221 | Wald ratio | 1 | trans | NA |
| Forced vital capacity (FVC) | -0.0286 | 0.0109 | 0.00869 | Wald ratio | 1 | trans | NA |
| Fracture resulting from simple fall | 0.0807 | 0.0324 | 0.0129 | Wald ratio | 1 | trans | NA |
| Transferrin Saturation | 0.134 | 0.0551 | 0.0151 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: K35 Acute appendicitis | 0.334 | 0.14 | 0.0171 | Wald ratio | 1 | trans | NA |
| Iron | 0.13 | 0.0551 | 0.0178 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: hypopituitarism | 0.836 | 0.363 | 0.0212 | Wald ratio | 1 | trans | NA |
| Body mass index (BMI) | 0.0305 | 0.0133 | 0.0217 | Wald ratio | 1 | trans | NA |
| Femoral neck bone mineral density | -0.0895 | 0.0409 | 0.0287 | Wald ratio | 1 | trans | NA |
| Cancer code  self-reported: malignant melanoma | 0.247 | 0.12 | 0.0393 | Wald ratio | 1 | trans | NA |
| _...and 94 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_92 association rows across 48 traits (81 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating LILRB4 levels | 5e-411 | rs417477 | 6 | GCST90860196 | no MR -> candidate analysis |
| CD4/LILRB4 protein level ratio | 2e-371 | rs370156 | 1 | GCST90313843 | no MR -> candidate analysis |
| CD74/LILRB4 protein level ratio | 3e-341 | rs370156 | 1 | GCST90313894 | no MR -> candidate analysis |
| BTN2A1/LILRB4 protein level ratio | 7e-333 | rs370156 | 1 | GCST90313546 | no MR -> candidate analysis |
| Leukocyte immunoglobulin-like receptor subfamily B member 1  | 1e-136 | rs71195783 | 1 | GCST90241793 | no MR -> candidate analysis |
| LILRA2 protein levels | 3e-85 | rs1654668 | 2 | GCST90469771 | no MR -> candidate analysis |
| KIR2DS4 protein levels | 4e-66 | rs117040207 | 13 | GCST90469686 | no MR -> candidate analysis |
| Serum levels of protein LILRB1 | 3e-65 | rs145320563 | 1 | GCST90088913 | no MR -> candidate analysis |
| LILRB4 protein levels | 8e-57 | rs3745871 | 6 | GCST90469778 | no MR -> candidate analysis |
| KIR2DL3 protein levels | 2e-52 | rs11574578 | 3 | GCST90469685 | no MR -> candidate analysis |
| FCAR protein levels | 2e-42 | rs12460776 | 2 | GCST90469197 | no MR -> candidate analysis |
| LAIR2 protein levels | 8e-41 | rs912734 | 6 | GCST90469729 | no MR -> candidate analysis |
| _...and 36 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 228 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| preeclampsia | 0.259 | — | common-variant locus | no MR -> candidate analysis |
| sialolithiasis | 0.164 | — | common-variant locus | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=2.2e-15, LOEUF=1.13 — LoF-tolerant |
| GWAS Catalog | 160 unique SNPs / 413 rows |
| ClinVar | 65 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 228 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'LILRB4'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 65 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 48 traits by best p-value, aggregated from 92 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q8NHJ6 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000186818/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/LILRB4 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/LILRB4 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=LILRB4%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/LILRB4 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:35:02  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
