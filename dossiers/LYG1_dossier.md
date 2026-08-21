# Protein Dossier — LYG1 (Lysozyme g-like protein 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Femoral neck bone mineral density | 0.142 | 0.0646 | 0.0279 | Wald ratio | 1 | trans | NA |
| Lumbar spine bone mineral density | 0.0983 | 0.073 | 0.178 | Wald ratio | 1 | trans | NA |
| Birth weight | -0.0341 | 0.0288 | 0.237 | Wald ratio | 1 | trans | NA |
| Low grade serous ovarian cancer | -0.351 | 0.298 | 0.239 | Wald ratio | 1 | trans | NA |
| Invasive mucinous ovarian cancer | 0.269 | 0.248 | 0.279 | Wald ratio | 1 | trans | NA |
| ER-negative Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | 0.0864 | 0.0816 | 0.29 | Wald ratio | 1 | trans | NA |
| Ovarian cancer | 0.0797 | 0.0837 | 0.341 | Wald ratio | 1 | trans | NA |
| High grade serous ovarian cancer | 0.0785 | 0.0993 | 0.429 | Wald ratio | 1 | trans | NA |
| Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.0341 | 0.0437 | 0.435 | Wald ratio | 1 | trans | NA |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_4 association rows across 4 traits (3 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Late effect (PheCode 1012) | 1e-12 | rs532494959 | 1 | GCST90479760 | no MR -> candidate analysis |
| Heel bone mineral density | 2e-11 | rs62153852 | 1 | GCST006433 | no MR -> candidate analysis |
| ICD10 D25: Leiomyoma of uterus | 4e-11 | rs12475639 | 1 | GCST90454204 | no MR -> candidate analysis |
| IgG glycosylation | 4e-7 | rs2200578 | 1 | GCST001848 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 35 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| inflammatory bowel disease | 0.337 | — | common-variant locus | no MR -> candidate analysis |
| uterine corpus leiomyoma | 0.163 | — | common-variant locus | no MR -> candidate analysis |
| placental abruption | 0.081 | — | common-variant locus | no MR -> candidate analysis |
| Uterine leiomyoma | 0.057 | — | common-variant locus | no MR -> candidate analysis |
| male reproductive organ cancer | 0.049 | — | common-variant locus | no MR -> candidate analysis |
| mathematical ability | 0.048 | — | common-variant locus | no MR -> candidate analysis |
| Cachexia | 0.041 | — | common-variant locus | no MR -> candidate analysis |
| intelligence | 0.037 | — | common-variant locus | no MR -> candidate analysis |
| Splenomegaly | 0.032 | — | common-variant locus | no MR -> candidate analysis |

> Of the 9 rows above, **9 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1.9e-05, LOEUF=1.18 — LoF-tolerant |
| GWAS Catalog | 24 unique SNPs / 48 rows |
| ClinVar | 51 records; 3 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 35 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'LYG1'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 51 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 4 of 4 traits by best p-value, aggregated from 4 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q8N1E2 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000144214/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/LYG1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/LYG1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=LYG1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/LYG1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:39:34  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
