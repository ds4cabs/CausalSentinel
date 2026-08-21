# Protein Dossier — IMPDH2 (Inosine-5'-monophosphate dehydrogenase 2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Height | -0.0502 | 0.00803 | 4.10e-10 | Wald ratio | 1 | trans | NA |
| Platelet count | -3.65 | 1.08 | 7.25e-04 | Wald ratio | 1 | trans | NA |
| PGC cross-disorder traits | -0.102 | 0.0329 | 0.00193 | Wald ratio | 1 | trans | NA |
| Mean platelet volume | 0.00803 | 0.00276 | 0.00362 | Wald ratio | 1 | trans | NA |
| Weight | -0.0164 | 0.00581 | 0.00487 | Wald ratio | 1 | trans | NA |
| Bipolar disorder | -0.17 | 0.0637 | 0.00775 | Wald ratio | 1 | trans | NA |
| Major depressive disorder | -0.152 | 0.0594 | 0.0104 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: hayfever or allergic rhinitis | 0.0639 | 0.0254 | 0.0118 | Wald ratio | 1 | trans | NA |
| Fractured bone site(s): Other bones | -0.0694 | 0.0307 | 0.0238 | Wald ratio | 1 | trans | NA |
| Eye problems or disorders: Diabetes related eye disease | -0.235 | 0.108 | 0.0293 | Wald ratio | 1 | trans | NA |
| Knee osteoarthritis | -0.155 | 0.0746 | 0.0374 | Wald ratio | 1 | trans | NA |
| Clear cell ovarian cancer | -0.23 | 0.112 | 0.0395 | Wald ratio | 1 | trans | NA |
| _...and 101 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-5250_53_3` | IMDH2 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_5 association rows across 5 traits (5 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Glycated hemoglobin levels | 3e-17 | rs11706052 | 1 | GCST90019509 | no MR -> candidate analysis |
| Educational attainment (years of education) | 6e-17 | rs72624911 | 1 | GCST006442 | no MR -> candidate analysis |
| Creatinine levels | 2e-13 | rs11706052 | 1 | GCST90019502 | no MR -> candidate analysis |
| Estimated glomerular filtration rate | 4e-13 | rs11706052 | 1 | GCST90019506 | no MR -> candidate analysis |
| Duration to complete alphanumeric path task (baseline) | 8e-12 | rs11706052 | 1 | GCST90565839 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 335 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| autosomal dominant dopa-responsive dystonia | 0.608 | — | established (curated) | no MR -> candidate analysis |
| Dystonia | 0.544 | — | established (curated) | no MR -> candidate analysis |
| dystonic disorder | 0.544 | — | established (curated) | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Inosine-5'-monophosphate dehydrogenase 2) |
| gnomAD constraint | pLI=4.6e-06, LOEUF=0.763 — LoF-tolerant |
| GWAS Catalog | 70 unique SNPs / 140 rows |
| ClinVar | 113 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 2 clinical annotations across 3 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 335 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'IMPDH2' and resolved to 'Inosine-5'-monophosphate dehydrogenase 2' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 113 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 5 of 5 traits by best p-value, aggregated from 5 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P12268 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000178035/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2002/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/IMPDH2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/IMPDH2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=IMPDH2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=IMPDH2 — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/IMPDH2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:17:35  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
