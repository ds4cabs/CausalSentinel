# Protein Dossier — ASMTL (Probable bifunctional dTTP/UTP pyrophosphatase/methyltransferase protein)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Amyotrophic lateral sclerosis | -0.354 | 0.112 | 0.00156 | Wald ratio | 1 | trans | NA |
| Neuroticism | -0.0466 | 0.0233 | 0.0455 | Wald ratio | 1 | trans | NA |
| Invasive mucinous ovarian cancer | -0.431 | 0.238 | 0.0696 | Wald ratio | 1 | trans | NA |
| Depressive symptoms | -0.0326 | 0.0233 | 0.162 | Wald ratio | 1 | trans | NA |
| Clear cell ovarian cancer | 0.258 | 0.236 | 0.275 | Wald ratio | 1 | trans | NA |
| Low grade serous ovarian cancer | 0.283 | 0.282 | 0.316 | Wald ratio | 1 | trans | NA |
| Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.0373 | 0.0401 | 0.352 | Wald ratio | 1 | trans | NA |
| Eczema | 0.214 | 0.234 | 0.36 | Wald ratio | 1 | trans | NA |
| ER-positive Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.0424 | 0.0471 | 0.368 | Wald ratio | 1 | trans | NA |
| Birth weight | -0.0215 | 0.0243 | 0.376 | Wald ratio | 1 | trans | NA |
| Bulimia nervosa | 0.625 | 0.826 | 0.449 | Wald ratio | 1 | trans | NA |
| Endometrioid ovarian cancer | -0.118 | 0.171 | 0.492 | Wald ratio | 1 | trans | NA |
| _...and 1 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_3 association rows across 1 traits (3 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| N-acetylserotonin O-methyltransferase-like protein levels | 1e-136 | rs4503285 | 3 | GCST90248599 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 39 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Abnormality of prenatal development or birth | 0.051 | — | common-variant locus | no MR -> candidate analysis |
| Primary amenorrhea | 0.012 | — | established (curated) | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=7.9e-19, LOEUF=1.18 — LoF-tolerant |
| GWAS Catalog | 11 unique SNPs / 44 rows |
| ClinVar | 312 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 39 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'ASMTL'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 312 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 1 of 1 traits by best p-value, aggregated from 3 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O95671 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000169093/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/ASMTL — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/ASMTL — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=ASMTL%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/ASMTL — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:10:49  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
