# Protein Dossier — IL11RA (Interleukin-11 receptor subunit alpha)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: hypertension | -0.057 | 0.0172 | 9.42e-04 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: pneumothorax | 0.735 | 0.24 | 0.00221 | Wald ratio | 1 | cis | NA |
| Cigarettes smoked per day | -1.71 | 0.597 | 0.00424 | Wald ratio | 1 | cis | NA |
| Multiple sclerosis | -0.192 | 0.0703 | 0.00638 | Wald ratio | 1 | cis | NA |
| Ulcerative colitis | 0.142 | 0.0526 | 0.00705 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: enlarged prostate | -0.28 | 0.11 | 0.0105 | Wald ratio | 1 | cis | NA |
| PGC cross-disorder traits | 0.126 | 0.0494 | 0.0106 | Wald ratio | 1 | cis | NA |
| Cough on most days | -0.137 | 0.0559 | 0.0145 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | -0.0226 | 0.00954 | 0.0177 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: anxiety or panic attacks | 0.165 | 0.0701 | 0.0184 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Arm | 0.187 | 0.0803 | 0.0202 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | 0.0191 | 0.00826 | 0.0209 | Wald ratio | 1 | cis | NA |
| _...and 111 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3814_63_1` | IL-11 RA | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_9 association rows across 8 traits (8 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Interleukin-11 receptor subunit alpha levels | 6e-99 | rs11575578 | 1 | GCST90248029 | no MR -> candidate analysis |
| Interleukin-11 receptor subunit alpha levels (IL11RA.3814.63 | 4e-26 | rs11575578 | 1 | GCST90241586 | no MR -> candidate analysis |
| C-C motif chemokine 27 levels | 5e-22 | rs2812357 | 1 | GCST90059913 | no MR -> candidate analysis |
| Height | 9e-14 | rs11575580 | 2 | GCST007841 | MR: beta=-0.0188, p=0.241 (cis) |
| Circulating MEPE levels | 9e-13 | rs11575580 | 1 | GCST90859653 | no MR -> candidate analysis |
| MEPE protein levels | 1e-12 | rs11575580 | 1 | GCST90469889 | no MR -> candidate analysis |
| Body shape phenotype PC2 | 3e-11 | rs11575580 | 1 | GCST90832990 | no MR -> candidate analysis |
| Height (baseline) | 5e-9 | rs11575580 | 1 | GCST90565843 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 200 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| craniosynostosis and dental anomalies | 0.843 | — | established (curated) | no MR -> candidate analysis |
| craniosynostosis | 0.596 | — | established (curated) | no MR -> candidate analysis |
| protozoa infectious disease | 0.293 | — | common-variant locus | no MR -> candidate analysis |
| asthma | 0.112 | — | common-variant locus | MR: beta=-0.0435, p=0.12 (cis) |

> Of the 4 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 1 known modulators (Interleukin-11 receptor subunit alpha) |
| gnomAD constraint | pLI=4.5e-16, LOEUF=1.13 — LoF-tolerant |
| GWAS Catalog | 63 unique SNPs / 126 rows |
| ClinVar | 215 records; 6 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 200 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'IL11RA' and resolved to 'Interleukin-11 receptor subunit alpha' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 215 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 8 of 8 traits by best p-value, aggregated from 9 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q14626 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000137070/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2050/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/IL11RA — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/IL11RA — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=IL11RA%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/IL11RA — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:10:10  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
