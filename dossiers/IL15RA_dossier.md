# Protein Dossier — IL15RA (Interleukin-15 receptor subunit alpha)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | 0.0697 | 0.0208 | 8.16e-04 | Wald ratio | 1 | cis | NA |
| Height | 0.0181 | 0.00609 | 0.003 | Wald ratio | 1 | cis | NA |
| Sleep duration | 0.00968 | 0.00392 | 0.0135 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K80 Cholelithiasis | 0.0774 | 0.0324 | 0.0168 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | 0.0116 | 0.00502 | 0.0205 | Wald ratio | 1 | cis | NA |
| Weight | 0.00991 | 0.00443 | 0.0254 | Wald ratio | 1 | cis | NA |
| Thalamus volume | 28.7 | 13 | 0.027 | Wald ratio | 1 | cis | NA |
| Alzheimer's disease | 0.0717 | 0.0334 | 0.0318 | Wald ratio | 1 | cis | NA |
| Alcohol intake frequency | -0.0159 | 0.00742 | 0.0326 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I80 Phlebitis and thrombophlebitis | 0.137 | 0.0644 | 0.0333 | Wald ratio | 1 | cis | NA |
| Rheumatoid arthritis | -0.0581 | 0.0292 | 0.0468 | Wald ratio | 1 | cis | NA |
| Mean cell volume | -0.108 | 0.0546 | 0.0479 | Wald ratio | 1 | cis | NA |
| _...and 91 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3445_53_2` | IL-15 Ra | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_115 association rows across 60 traits (104 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| IL2RA/NCR1 protein level ratio | 7e-902 | rs7911500 | 1 | GCST90315161 | no MR -> candidate analysis |
| Circulating IL15RA levels | 2e-543 | rs2228059 | 9 | GCST90859870 | no MR -> candidate analysis |
| IL15RA protein levels | 8e-276 | rs3136630 | 9 | GCST90469555 | no MR -> candidate analysis |
| Interleukin-15 receptor subunit alpha levels | 2e-184 | rs2228059 | 8 | GCST90274800 | no MR -> candidate analysis |
| Soluble interleukin-2 receptor subunit alpha | 1e-100 | rs7911500 | 2 | GCST003088 | no MR -> candidate analysis |
| Interleukin-15 receptor subunit alpha levels (IL15RA.14054.1 | 2e-91 | rs8177641 | 4 | GCST90241594 | no MR -> candidate analysis |
| IL2RA protein levels | 7e-73 | rs146712466 | 7 | GCST90469585 | no MR -> candidate analysis |
| Circulating IL2RA levels | 4e-66 | rs183050850 | 2 | GCST90859919 | no MR -> candidate analysis |
| Serum levels of protein IL15RA | 1e-63 | rs7086174 | 5 | GCST90087746 | no MR -> candidate analysis |
| Interleukin-15 receptor subunit alpha (analyte X14054.17) le | 3e-61 | rs7086174 | 1 | GCST90422434 | no MR -> candidate analysis |
| Circulating NCR1 levels (id: OID01007_OID20566) | 1e-44 | rs8177653 | 3 | GCST90860233 | no MR -> candidate analysis |
| Circulating NCR1 levels (id: OID00816_OID20566) | 1e-43 | rs8177653 | 3 | GCST90860146 | no MR -> candidate analysis |
| _...and 48 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 312 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| neuroblastoma | 0.55 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.463 | — | common-variant locus | no MR -> candidate analysis |
| arthropathy | 0.457 | — | common-variant locus | no MR -> candidate analysis |
| atopic eczema | 0.123 | — | common-variant locus | no MR -> candidate analysis |
| rheumatoid arthritis | 0.031 | — | common-variant locus | MR: beta=-0.0581, p=0.0468 (cis) |
| Iron deficiency anemia | 0.111 | — | common-variant locus | no MR -> candidate analysis |

> Of the 6 rows above, **5 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (IL15-IL15 receptor) |
| gnomAD constraint | pLI=4.5e-10, LOEUF=1.49 — LoF-tolerant |
| GWAS Catalog | 160 unique SNPs / 403 rows |
| ClinVar | 99 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 312 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'IL15RA' and resolved to 'IL15-IL15 receptor' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 99 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 60 traits by best p-value, aggregated from 115 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q13261 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000134470/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4106128/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/IL15RA — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/IL15RA — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=IL15RA%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/IL15RA — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:11:28  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
