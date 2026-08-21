# Protein Dossier — ART3 (Ecto-ADP-ribosyltransferase 3)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: I30 Acute pericarditis | 0.724 | 0.253 | 0.00418 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: deep venous thrombosis (dvt) | 0.148 | 0.052 | 0.0045 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: B37 Candidiasis | 0.585 | 0.241 | 0.0154 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertension | 0.0329 | 0.014 | 0.0187 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | -0.0251 | 0.011 | 0.0225 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Cataract | 0.0941 | 0.0423 | 0.0261 | Wald ratio | 1 | cis | NA |
| Hippocampus volume | 33.7 | 16.7 | 0.0431 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Injury or trauma resulting in loss of vision | -0.308 | 0.155 | 0.0473 | Wald ratio | 1 | cis | NA |
| Happiness | -0.0204 | 0.0105 | 0.0524 | Wald ratio | 1 | cis | NA |
| Myocardial infarction | 0.0699 | 0.0373 | 0.0611 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: joint disorder | 0.191 | 0.104 | 0.0655 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: D25 Leiomyoma of uterus | -0.164 | 0.089 | 0.066 | Wald ratio | 1 | cis | NA |
| _...and 76 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_92 association rows across 51 traits (83 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| C-X-C motif chemokine 11 levels | 8e-389 | rs35170645 | 8 | GCST90247202 | no MR -> candidate analysis |
| CXCL11/DKK1 protein level ratio | 1e-359 | rs6826163 | 1 | GCST90314334 | no MR -> candidate analysis |
| ART3/RGMB protein level ratio | 2e-346 | rs4859418 | 1 | GCST90313363 | no MR -> candidate analysis |
| Circulating CXCL11 levels (id: OID00486_OID21042) | 8e-314 | rs35170645 | 5 | GCST90859845 | no MR -> candidate analysis |
| CXCL11 protein levels | 9e-301 | rs35170645 | 4 | GCST90468924 | no MR -> candidate analysis |
| ART3/RGMA protein level ratio | 9e-300 | rs4859418 | 1 | GCST90313362 | no MR -> candidate analysis |
| Circulating CXCL11 levels (id: OID00767_OID21042) | 9e-295 | rs35170645 | 5 | GCST90860102 | no MR -> candidate analysis |
| C-X-C motif chemokine 10 levels | 6e-271 | rs11548618 | 3 | GCST90274780 | no MR -> candidate analysis |
| Circulating CXCL10 levels (id: OID00535_OID20697) | 7e-267 | rs564487523 | 2 | GCST90859889 | no MR -> candidate analysis |
| CXCL11/VTA1 protein level ratio | 3e-215 | rs6532086 | 1 | GCST90314337 | no MR -> candidate analysis |
| Circulating CXCL10 levels (id: OID00807_OID20697) | 1e-158 | rs564487523 | 2 | GCST90860137 | no MR -> candidate analysis |
| ART3 protein levels | 5e-128 | rs7682766 | 1 | GCST90468370 | no MR -> candidate analysis |
| _...and 39 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 97 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| type 2 diabetes mellitus | 0.489 | — | common-variant locus | no MR -> candidate analysis |
| bone Paget disease | 0.416 | — | common-variant locus | no MR -> candidate analysis |
| Parkinson disease | 0.25 | — | common-variant locus | no MR -> candidate analysis |
| atrial fibrillation | 0.178 | — | common-variant locus | MR: beta=-0.0643, p=0.457 (cis) |
| atrial flutter | 0.065 | — | common-variant locus | MR: beta=-0.0643, p=0.457 (cis) |

> Of the 5 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=2.5e-17, LOEUF=1.28 — LoF-tolerant |
| GWAS Catalog | 125 unique SNPs / 296 rows |
| ClinVar | 160 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 97 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'ART3'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 160 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 51 traits by best p-value, aggregated from 92 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q13508 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000156219/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/ART3 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/ART3 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=ART3%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/ART3 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:09:53  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
