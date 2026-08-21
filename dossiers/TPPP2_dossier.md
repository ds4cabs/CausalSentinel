# Protein Dossier — TPPP2 (Tubulin polymerization-promoting protein family member 2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Height | 0.0809 | 0.0146 | 2.77e-08 | Wald ratio | 1 | trans | 0.866 |
| HDL cholesterol | -0.11 | 0.024 | 4.81e-06 | Wald ratio | 1 | trans | NA |
| Birth weight | 0.0698 | 0.017 | 3.94e-05 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | -0.267 | 0.0723 | 2.24e-04 | Wald ratio | 1 | trans | NA |
| Forced vital capacity (FVC) | 0.0328 | 0.0102 | 0.00124 | Wald ratio | 1 | trans | NA |
| Depressive symptoms | -0.0512 | 0.0162 | 0.00154 | Wald ratio | 1 | trans | NA |
| Mean platelet volume | -0.0167 | 0.00539 | 0.00194 | Wald ratio | 1 | trans | NA |
| Ovarian cancer | -0.187 | 0.068 | 0.00587 | Wald ratio | 1 | trans | NA |
| Subjective well being | -0.0431 | 0.0162 | 0.00766 | Wald ratio | 1 | trans | NA |
| Weight | 0.028 | 0.0109 | 0.0104 | Wald ratio | 1 | trans | NA |
| Lung cancer | -0.244 | 0.0967 | 0.0116 | Wald ratio | 1 | trans | NA |
| Urate | 0.0674 | 0.027 | 0.0124 | Wald ratio | 1 | trans | NA |
| _...and 115 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_5 association rows across 5 traits (3 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Histidine levels | 3e-23 | rs147773754 | 1 | GCST90092830 | no MR -> candidate analysis |
| Glutamine levels | 1e-15 | rs147773754 | 1 | GCST90092818 | no MR -> candidate analysis |
| Exostosis of jaw (PheCode 526.8) | 5e-12 | rs539018113 | 1 | GCST90480282 | no MR -> candidate analysis |
| Alzheimer's disease, proxy Alzheimer's disease or related de | 5e-6 | rs1243453 | 1 | GCST90654666 | no MR -> candidate analysis |
| Hip circumference adjusted for BMI | 9e-6 | rs190897369 | 1 | GCST008156 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 98 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| alcohol drinking | 0.312 | — | common-variant locus | no MR -> candidate analysis |
| exostosis | 0.132 | — | common-variant locus | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.017, LOEUF=1.11 — LoF-tolerant |
| GWAS Catalog | 81 unique SNPs / 162 rows |
| ClinVar | 95 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 98 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'TPPP2'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 95 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 5 of 5 traits by best p-value, aggregated from 5 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P59282 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000179636/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/TPPP2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/TPPP2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=TPPP2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/TPPP2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:28:10  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
