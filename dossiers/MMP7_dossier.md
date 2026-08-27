# Protein Dossier — MMP7 (Matrilysin)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: R55 Syncope and collapse | 0.179 | 0.0662 | 0.00688 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: osteoarthritis | 0.0604 | 0.0234 | 0.00987 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N40 Hyperplasia of prostate | 0.163 | 0.066 | 0.0137 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: chronic obstructive airways disease or copd | 0.233 | 0.102 | 0.0223 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: C50 Malignant neoplasm of breast | 0.114 | 0.0519 | 0.0287 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: mania or bipolar disorder or manic depression | 0.242 | 0.116 | 0.0369 | Wald ratio | 1 | cis | NA |
| Vascular or heart problems diagnosed by doctor: Angina | 0.0793 | 0.0385 | 0.0395 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: bone disorder | 0.245 | 0.126 | 0.0521 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: polio  or  poliomyelitis | 0.39 | 0.202 | 0.0527 | Wald ratio | 1 | cis | NA |
| Neo-openness to experience | -0.482 | 0.257 | 0.0609 | Wald ratio | 1 | cis | NA |
| Birth weight | 0.0216 | 0.0117 | 0.0649 | Wald ratio | 1 | cis | NA |
| Clear cell ovarian cancer | 0.222 | 0.123 | 0.072 | Wald ratio | 1 | cis | NA |
| _...and 94 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2789_26_2` | MMP-7 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_78 association rows across 31 traits (68 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating MMP7 levels (id: OID00441_OID20087) | 4e-661 | rs11568819 | 5 | GCST90859801 | no MR -> candidate analysis |
| Circulating MMP7 levels (id: OID00814_OID20087) | 3e-387 | rs11568819 | 6 | GCST90860144 | no MR -> candidate analysis |
| Matrilysin (analyte X2789.26) levels | 2e-278 | rs11568819 | 1 | GCST90425473 | no MR -> candidate analysis |
| Cerebrospinal fluid protein MMP7 levels | 1e-232 | rs11568819 | 1 | GCST90944433 | no MR -> candidate analysis |
| Matrix metalloproteinase-7 levels | 2e-222 | rs11568819 | 6 | GCST90012056 | no MR -> candidate analysis |
| Matrilysin levels | 2e-139 | rs11568819 | 7 | GCST90248425 | no MR -> candidate analysis |
| MMP7 protein levels | 6e-112 | rs7946641 | 3 | GCST90469921 | no MR -> candidate analysis |
| MMP10 protein levels | 4e-111 | rs184354018 | 3 | GCST90469915 | no MR -> candidate analysis |
| Prostate-specific antigen levels | 3e-82 | rs11568818 | 5 | GCST90461907 | no MR -> candidate analysis |
| prostate-specific antigen (PSA, minimum, inv-norm transforme | 2e-49 | rs11568818 | 2 | GCST90476322 | no MR -> candidate analysis |
| Serum levels of protein MMP7 | 6e-42 | rs11568819 | 1 | GCST90088072 | no MR -> candidate analysis |
| prostate-specific antigen (PSA, mean, inv-norm transformed) | 1e-39 | rs11568818 | 2 | GCST90476319 | no MR -> candidate analysis |
| _...and 19 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1135 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| prostate carcinoma | 0.745 | — | common-variant locus | no MR -> candidate analysis |
| prostate cancer | 0.663 | — | common-variant locus | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 4 known modulators (Matrilysin) |
| gnomAD constraint | pLI=3.9e-08, LOEUF=1.15 — LoF-tolerant |
| GWAS Catalog | 65 unique SNPs / 129 rows |
| ClinVar | 75 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1135 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'MMP7' and resolved to 'Matrilysin' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 75 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 31 traits by best p-value, aggregated from 78 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P09237 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000137673/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4073/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/MMP7 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/MMP7 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=MMP7%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/MMP7 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:50:23  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
