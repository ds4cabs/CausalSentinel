# Protein Dossier — IMPDH1 (Inosine-5'-monophosphate dehydrogenase 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Forced expiratory volume in 1-second (FEV1) | -0.0128 | 0.00328 | 8.97e-05 | Inverse variance weighted | 2 | trans | NA |
| Forced expiratory volume in 1-second (FEV1) | -0.0128 | 0.00328 | 8.97e-05 | Inverse variance weighted | 2 | trans | NA |
| Forced vital capacity (FVC) | -0.0138 | 0.00422 | 0.00107 | Inverse variance weighted | 2 | trans | NA |
| Forced vital capacity (FVC) | -0.0138 | 0.00422 | 0.00107 | Inverse variance weighted | 2 | trans | NA |
| PGC cross-disorder traits | -0.0608 | 0.0191 | 0.0014 | Inverse variance weighted | 2 | trans | NA |
| PGC cross-disorder traits | -0.0608 | 0.0191 | 0.0014 | Inverse variance weighted | 2 | trans | NA |
| Non-cancer illness code  self-reported: hayfever or allergic rhinitis | 0.00345 | 0.00111 | 0.00192 | Inverse variance weighted | 2 | trans | NA |
| Non-cancer illness code  self-reported: hayfever or allergic rhinitis | 0.00345 | 0.00111 | 0.00192 | Inverse variance weighted | 2 | trans | NA |
| Mean cell haemoglobin | 0.0498 | 0.0165 | 0.00251 | Inverse variance weighted | 2 | trans | NA |
| Mean cell haemoglobin | 0.0498 | 0.0165 | 0.00251 | Inverse variance weighted | 2 | trans | NA |
| Mean cell volume | 0.121 | 0.0421 | 0.00417 | Inverse variance weighted | 2 | trans | NA |
| Mean cell volume | 0.121 | 0.0421 | 0.00417 | Inverse variance weighted | 2 | trans | NA |
| _...and 191 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-5229_90_3` | IMDH1 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_7 association rows across 6 traits (5 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Free Cholesterol to Cholesteryl Esters in Large HDL ratio | 4e-16 | rs56777177 | 1 | GCST90827800 | no MR -> candidate analysis |
| Pelvic organ prolapse | 4e-12 | rs72624976 | 2 | GCST010174 | no MR -> candidate analysis |
| Thyroiditis (PheCode 245) | 8e-12 | rs541866506 | 1 | GCST90479871 | no MR -> candidate analysis |
| Protein quantitative trait loci (liver) | 3e-8 | rs115597874 | 1 | GCST011427 | no MR -> candidate analysis |
| Height | 2e-7 | rs13245629 | 1 | GCST90245848 | MR: beta=-0.0266, p=0.0569 (trans) |
| Glycochenodeoxycholate levels in elite athletes | 8e-6 | rs4731448 | 1 | GCST90133913 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 628 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| retinitis pigmentosa | 0.803 | — | established (curated) | no MR -> candidate analysis |
| retinitis pigmentosa 10 | 0.894 | — | established (curated) | no MR -> candidate analysis |
| Leber congenital amaurosis | 0.573 | — | established (curated) | no MR -> candidate analysis |
| Leber congenital amaurosis 11 | 0.758 | — | established (curated) | no MR -> candidate analysis |
| Retinal dystrophy | 0.695 | — | established (curated) | no MR -> candidate analysis |

> Of the 5 rows above, **5 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 2 known modulators (Inosine-5'-monophosphate dehydrogenase 1) |
| gnomAD constraint | pLI=6.3e-07, LOEUF=0.724 — LoF-tolerant |
| GWAS Catalog | 23 unique SNPs / 46 rows |
| ClinVar | 740 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 4 clinical annotations across 1 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 628 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'IMPDH1' and resolved to 'Inosine-5'-monophosphate dehydrogenase 1' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 740 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 6 of 6 traits by best p-value, aggregated from 7 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P20839 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000106348/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL1822/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/IMPDH1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/IMPDH1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=IMPDH1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=IMPDH1 — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/IMPDH1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:17:20  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
