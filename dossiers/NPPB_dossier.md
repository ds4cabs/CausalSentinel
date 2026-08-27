# Protein Dossier — NPPB (Natriuretic peptides B)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Neuroblastoma | 0.216 | 0.162 | 0.185 | Wald ratio | 1 | cis | NA |
| Thyroid cancer | -0.355 | 0.317 | 0.263 | Wald ratio | 1 | cis | NA |
| Childhood intelligence | 0.05 | 0.0591 | 0.398 | Wald ratio | 1 | trans | NA |
| Knee osteoarthritis | 0.0878 | 0.124 | 0.479 | Wald ratio | 1 | trans | NA |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3723_1_2` | BNP-32 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_83 association rows across 49 traits (78 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating NTproBNP levels (id: OID01214_OID20125) | 7e-506 | rs198389 | 2 | GCST90860419 | no MR -> candidate analysis |
| Circulating NTproBNP levels (id: OID00455_OID20125) | 2e-468 | rs198389 | 2 | GCST90859816 | no MR -> candidate analysis |
| Circulating NTproBNP levels (id: OID00131_OID20125) | 4e-409 | rs198389 | 2 | GCST90859652 | no MR -> candidate analysis |
| Circulating NPPB levels (id: OID01214_OID20049) | 3e-292 | rs198389 | 1 | GCST90860418 | no MR -> candidate analysis |
| Circulating NPPB levels (id: OID00455_OID20049) | 7e-260 | rs198389 | 1 | GCST90859815 | no MR -> candidate analysis |
| Circulating NPPB levels (id: OID00131_OID20049) | 3e-200 | rs198389 | 1 | GCST90859651 | no MR -> candidate analysis |
| NPPB protein levels | 5e-174 | rs198389 | 1 | GCST90470074 | no MR -> candidate analysis |
| B-type natriuretic peptide to N-terminal pro B-type natriure | 5e-103 | rs61761991 | 1 | GCST005208 | no MR -> candidate analysis |
| NTPROBNP protein levels | 1e-84 | rs5229 | 2 | GCST90470096 | no MR -> candidate analysis |
| N-terminal pro-BNP levels | 9e-80 | rs198379 | 4 | GCST90248745 | no MR -> candidate analysis |
| N-terminal prohormone brain natriuretic peptide levels | 3e-77 | rs198389 | 2 | GCST90012082 | no MR -> candidate analysis |
| N-terminal pro B-type natriuretic peptide levels | 9e-68 | rs61761991 | 2 | GCST005205 | no MR -> candidate analysis |
| _...and 37 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1371 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| hypertensive disorder | 0.76 | — | common-variant locus | no MR -> candidate analysis |
| Increased blood pressure | 0.634 | — | common-variant locus | no MR -> candidate analysis |
| major depressive disorder | 0.294 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.307 | — | common-variant locus | no MR -> candidate analysis |
| viral eye infection | 0.302 | — | common-variant locus | no MR -> candidate analysis |
| spinal cord injury | 0.3 | — | common-variant locus | no MR -> candidate analysis |
| ankylosing spondylitis | 0.289 | — | common-variant locus | no MR -> candidate analysis |

> Of the 7 rows above, **7 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=2.1e-05, LOEUF=1.63 — LoF-tolerant |
| GWAS Catalog | 241 unique SNPs / 580 rows |
| ClinVar | 84 records; 5 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1371 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'NPPB'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 84 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 49 traits by best p-value, aggregated from 83 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P16860 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000120937/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/NPPB — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/NPPB — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=NPPB%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/NPPB — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:02:23  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
