# Protein Dossier — TREM1 (Triggering receptor expressed on myeloid cells 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Alzheimer's disease | 0.148 | 0.0479 | 0.00201 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | -0.0262 | 0.00923 | 0.00456 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertension | -0.0304 | 0.0125 | 0.0155 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: gastro-oesophageal reflux (gord)  or  gastric reflux | 0.0768 | 0.0319 | 0.016 | Wald ratio | 1 | cis | NA |
| Squamous cell lung cancer | -0.172 | 0.0767 | 0.0252 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | -0.0154 | 0.00714 | 0.031 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Ankle | 0.115 | 0.0545 | 0.0349 | Wald ratio | 1 | cis | NA |
| Transferrin | 0.062 | 0.0302 | 0.0401 | Wald ratio | 1 | cis | NA |
| Putamen volume | -33.9 | 17.4 | 0.0517 | Wald ratio | 1 | cis | NA |
| Fasting glucose | -0.0174 | 0.00936 | 0.0633 | Wald ratio | 1 | cis | NA |
| Happiness | 0.0162 | 0.00884 | 0.0671 | Wald ratio | 1 | cis | NA |
| Height | 0.016 | 0.00882 | 0.069 | Wald ratio | 1 | cis | NA |
| _...and 91 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_20 association rows across 13 traits (15 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Triggering receptor expressed on myeloid cells 1 levels | 2e-101 | rs2101270 | 3 | GCST90427734 | no MR -> candidate analysis |
| Triggering receptor expressed on myeloid cells 1 levels (TRE | 4e-88 | rs139121778 | 2 | GCST90243115 | no MR -> candidate analysis |
| Serum levels of protein TREM1 | 4e-85 | rs3789204 | 4 | GCST90090595 | no MR -> candidate analysis |
| Blood protein levels | 1e-54 | rs3789204 | 1 | GCST006585 | no MR -> candidate analysis |
| Circulating TREML2 levels | 8e-49 | rs113955667 | 1 | GCST90859936 | no MR -> candidate analysis |
| TREM2 protein levels | 4e-29 | rs11755124 | 1 | GCST90470960 | no MR -> candidate analysis |
| Triggering receptor expressed on myeloid cells 1 level in Ch | 4e-13 | rs148091594 | 1 | GCST90239280 | no MR -> candidate analysis |
| Femur bone mineral density x serum urate levels interaction | 2e-11 | rs34542207 | 2 | GCST012490 | no MR -> candidate analysis |
| Alzheimer’s disease polygenic risk score (upper quantile vs  | 2e-8 | rs1872245 | 1 | GCST90132260 | no MR -> candidate analysis |
| 3-hydroxypropylmercapturic acid levels in smokers | 2e-7 | rs74851542 | 1 | GCST002956 | no MR -> candidate analysis |
| Cognitive function (generalized correlation coefficient) | 9e-7 | rs1872245 | 1 | GCST012066 | no MR -> candidate analysis |
| Metabolite levels | 2e-6 | rs17701319 | 1 | GCST009391 | no MR -> candidate analysis |
| _...and 1 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 577 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| liver disorder | 0.166 | — | common-variant locus | no MR -> candidate analysis |
| Alzheimer disease | 0.09 | — | common-variant locus | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 1 known modulators (Triggering receptor expressed on myeloid cells 1) |
| gnomAD constraint | pLI=0.0001, LOEUF=1.08 — LoF-tolerant |
| GWAS Catalog | 65 unique SNPs / 130 rows |
| ClinVar | 56 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 577 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'TREM1' and resolved to 'Triggering receptor expressed on myeloid cells 1' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 56 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 13 of 13 traits by best p-value, aggregated from 20 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9NP99 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000124731/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL1697674/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/TREM1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/TREM1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=TREM1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/TREM1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:29:11  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
