# Protein Dossier — MAPK13 (Mitogen-activated protein kinase 13)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Red blood cell count | 0.0382 | 0.00946 | 5.31e-05 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K57 Diverticular disease of intestine | 0.183 | 0.061 | 0.00265 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: D25 Leiomyoma of uterus | 0.206 | 0.0749 | 0.00591 | Wald ratio | 1 | cis | NA |
| Birth length | -0.112 | 0.0422 | 0.00795 | Wald ratio | 1 | cis | NA |
| Schizophrenia | -0.116 | 0.0473 | 0.0143 | Wald ratio | 1 | cis | NA |
| Height | -0.0307 | 0.013 | 0.0181 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: diverticular disease or diverticulitis | 0.191 | 0.0816 | 0.0191 | Wald ratio | 1 | cis | NA |
| Subjective well being | -0.0276 | 0.0118 | 0.0196 | Wald ratio | 1 | cis | NA |
| Mean cell haemoglobin | -0.0981 | 0.0437 | 0.0249 | Wald ratio | 1 | cis | NA |
| Knee and hip osteoarthritis | 0.192 | 0.0866 | 0.0265 | Wald ratio | 1 | cis | NA |
| Mean cell volume | -0.247 | 0.112 | 0.0265 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: enlarged prostate | 0.165 | 0.0757 | 0.0297 | Wald ratio | 1 | cis | NA |
| _...and 97 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-5006_71_1` | MK13 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_6 association rows across 6 traits (5 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| SEMA3G protein levels | 6e-57 | rs147247331 | 1 | GCST90470571 | no MR -> candidate analysis |
| Height | 1e-49 | rs9689522 | 1 | GCST90245848 | MR: beta=-0.0307, p=0.0181 (cis) |
| Mitogen-activated protein kinase 13 levels | 2e-37 | rs12210904 | 1 | GCST90248406 | no MR -> candidate analysis |
| Mitogen-activated protein kinase 13 levels (MAPK13.5006.71.1 | 2e-21 | rs12210904 | 1 | GCST90241949 | no MR -> candidate analysis |
| MAPK13 protein levels | 5e-17 | rs12210904 | 1 | GCST90469856 | no MR -> candidate analysis |
| Alcohol use frequency in adolescence | 5e-6 | rs115149227 | 1 | GCST90454589 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 225 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| attention deficit-hyperactivity disorder | 0.438 | — | common-variant locus | no MR -> candidate analysis |
| substance abuse | 0.438 | — | common-variant locus | no MR -> candidate analysis |
| diabetes mellitus | 0.049 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Mitogen-activated protein kinase 13) |
| gnomAD constraint | pLI=3.3e-10, LOEUF=0.952 — LoF-tolerant |
| GWAS Catalog | 50 unique SNPs / 100 rows |
| ClinVar | 79 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 225 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'MAPK13' and resolved to 'Mitogen-activated protein kinase 13' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 79 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 6 of 6 traits by best p-value, aggregated from 6 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O15264 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000156711/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2939/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/MAPK13 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/MAPK13 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=MAPK13%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/MAPK13 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:43:56  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
