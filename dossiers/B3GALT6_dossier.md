# Protein Dossier — B3GALT6 (Beta-1,3-galactosyltransferase 6)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: K35 Acute appendicitis | 0.453 | 0.141 | 0.00136 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: polio  or  poliomyelitis | 0.836 | 0.273 | 0.00223 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R07 Pain in throat and chest | 0.17 | 0.0571 | 0.00298 | Wald ratio | 1 | cis | NA |
| Hirschsprung's disease | -1.68 | 0.664 | 0.0116 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K44 Diaphragmatic hernia | 0.233 | 0.0969 | 0.0163 | Wald ratio | 1 | cis | NA |
| High grade serous ovarian cancer | 0.23 | 0.103 | 0.0255 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: vaginal prolapse or uterine prolapse | 0.333 | 0.151 | 0.0276 | Wald ratio | 1 | cis | NA |
| Serum creatinine (eGFRcrea) | 0.0122 | 0.00554 | 0.0278 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: malignant melanoma | 0.285 | 0.132 | 0.0305 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N92 Excessive  frequent and irregular menstruation | -0.32 | 0.149 | 0.0315 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypopituitarism | 0.865 | 0.419 | 0.0391 | Wald ratio | 1 | cis | NA |
| Percent emphysema | -0.118 | 0.0579 | 0.0415 | Wald ratio | 1 | cis | NA |
| _...and 93 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_No GWAS Catalog associations mapped to this gene._

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 67 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| spondyloepimetaphyseal dysplasia with joint laxity, type 1, with or without fractures | 0.904 | — | established (curated) | no MR -> candidate analysis |
| Ehlers-Danlos syndrome, spondylodysplastic type, 2 | 0.892 | — | established (curated) | no MR -> candidate analysis |
| spondyloepimetaphyseal dysplasia with joint laxity | 0.9 | — | established (curated) | no MR -> candidate analysis |
| Ehlers-Danlos syndrome, progeroid type | 0.93 | — | established (curated) | no MR -> candidate analysis |
| Al-Gazali syndrome | 0.831 | — | established (curated) | no MR -> candidate analysis |
| spondyloepiphyseal dysplasia | 0.438 | — | established (curated) | no MR -> candidate analysis |
| hereditary disease | 0.317 | — | established (curated) | no MR -> candidate analysis |
| hypothyroidism | 0.094 | — | common-variant locus | MR: beta=0.115, p=0.0553 (cis) |
| hair color | 0.064 | — | common-variant locus | no MR -> candidate analysis |
| asthma | 0.04 | — | common-variant locus | MR: beta=-0.0728, p=0.111 (cis) |
| ankylosing spondylitis | 0.037 | — | common-variant locus | no MR -> candidate analysis |
| sclerosing cholangitis | 0.037 | — | common-variant locus | no MR -> candidate analysis |
| psoriasis | 0.037 | — | common-variant locus | MR: beta=-0.139, p=0.413 (cis) |
| Crohn disease | 0.037 | — | common-variant locus | no MR -> candidate analysis |
| ulcerative colitis | 0.037 | — | common-variant locus | no MR -> candidate analysis |

> Of the 15 rows above, **12 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=5.3e-11, LOEUF=1.6 — LoF-tolerant |
| GWAS Catalog | 51 unique SNPs / 102 rows |
| ClinVar | 573 records; 9 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 67 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'B3GALT6'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 573 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — No GWAS Catalog associations mapped to this gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q96L58 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000176022/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/B3GALT6 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/B3GALT6 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=B3GALT6%5Bgene%5D — _ClinVar build Build260809-1055.1_

## Provenance

- Generated: 2026-08-14T01:13:40  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
