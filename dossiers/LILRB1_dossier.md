# Protein Dossier — LILRB1 (Leukocyte immunoglobulin-like receptor subfamily B member 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Juvenile idiopathic arthritis | 0.126 | 0.0748 | 0.0934 | Wald ratio | 1 | cis | NA |
| Lung cancer | 0.019 | 0.0218 | 0.383 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: prostate cancer | 0.0264 | 0.035 | 0.45 | Wald ratio | 1 | cis | NA |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-5090_49_2` | ILT-2 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_51 association rows across 26 traits (45 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Leukocyte immunoglobulin-like receptor subfamily B member 1  | 4e-1083 | rs10426886 | 8 | GCST90248301 | no MR -> candidate analysis |
| Circulating LILRB1 levels | 1e-460 | rs112988186 | 2 | GCST90860494 | no MR -> candidate analysis |
| Leukocyte immunoglobulin-like receptor subfamily B member 1  | 1e-336 | rs2114511 | 5 | GCST90241793 | no MR -> candidate analysis |
| LILRB1 protein levels | 9e-189 | rs8101262 | 3 | GCST90469776 | no MR -> candidate analysis |
| Leukocyte immunoglobulin-like receptor subfamily B member 1  | 3e-103 | rs10427127 | 1 | GCST90237833 | no MR -> candidate analysis |
| LAIR2 protein levels | 1e-99 | rs16985478 | 2 | GCST90469729 | no MR -> candidate analysis |
| LILRA2 protein levels | 9e-80 | rs184207698 | 3 | GCST90469771 | no MR -> candidate analysis |
| Serum levels of protein LILRB1 | 3e-65 | rs145320563 | 1 | GCST90088913 | no MR -> candidate analysis |
| KIR2DS4 protein levels | 9e-38 | rs575822772 | 4 | GCST90469686 | no MR -> candidate analysis |
| Circulating LILRB4 levels | 1e-35 | rs10426886 | 2 | GCST90860196 | no MR -> candidate analysis |
| LILRB4 protein levels | 3e-34 | rs190610084 | 3 | GCST90469778 | no MR -> candidate analysis |
| KIR3DL1 protein levels | 5e-25 | rs575822772 | 1 | GCST90469687 | no MR -> candidate analysis |
| _...and 14 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 292 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Epstein-Barr virus infection | 0.341 | — | common-variant locus | no MR -> candidate analysis |
| response to stimulus | 0.172 | — | common-variant locus | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=2.6e-16, LOEUF=0.983 — LoF-tolerant |
| GWAS Catalog | 150 unique SNPs / 392 rows |
| ClinVar | 221 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 292 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'LILRB1'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 221 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 26 traits by best p-value, aggregated from 51 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q8NHL6 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000104972/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/LILRB1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/LILRB1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=LILRB1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/LILRB1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:34:13  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
