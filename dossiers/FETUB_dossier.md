# Protein Dossier — FETUB (Fetuin-B)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: hypopituitarism | 0.74 | 0.277 | 0.0076 | Wald ratio | 1 | cis | NA |
| Intracranial volume | -1.94e+04 | 7.55e+03 | 0.0103 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: pernicious anaemia | 0.322 | 0.133 | 0.0159 | Wald ratio | 1 | cis | NA |
| Systolic blood pressure  automated reading | -0.0236 | 0.01 | 0.0186 | Wald ratio | 1 | cis | NA |
| LDL cholesterol | -0.0496 | 0.0214 | 0.0206 | Wald ratio | 1 | cis | NA |
| Total cholesterol | -0.0458 | 0.021 | 0.0294 | Wald ratio | 1 | cis | NA |
| IgA nephropathy | 0.647 | 0.312 | 0.0381 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Glaucoma | -0.211 | 0.102 | 0.0393 | Wald ratio | 1 | cis | NA |
| Neo-openness to experience | 0.589 | 0.288 | 0.041 | Wald ratio | 1 | cis | NA |
| Age at menopause | -0.15 | 0.0751 | 0.0455 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: L03 Cellulitis | 0.183 | 0.0916 | 0.0457 | Wald ratio | 1 | cis | NA |
| Mean cell haemoglobin | 0.086 | 0.0436 | 0.0484 | Wald ratio | 1 | cis | NA |
| _...and 92 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3367_8_3` | FETUB | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_43 association rows across 21 traits (43 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating FETUB levels | 3e-990 | rs114780909 | 5 | GCST90860501 | no MR -> candidate analysis |
| Myosin regulatory light chain 2, atrial isoform levels | 9e-447 | rs66965282 | 2 | GCST90248482 | no MR -> candidate analysis |
| FETUB protein levels | 1e-224 | rs79014333 | 4 | GCST90469215 | no MR -> candidate analysis |
| CRTAC1 protein levels | 1e-101 | rs62292569 | 5 | GCST90468870 | no MR -> candidate analysis |
| Fetuin-B levels | 3e-97 | rs75443068 | 6 | GCST90137776 | no MR -> candidate analysis |
| Fetuin-B level in Chronic kidney disease with hypertension a | 4e-85 | rs6785067 | 1 | GCST90237345 | no MR -> candidate analysis |
| Circulating CRTAC1 levels | 1e-68 | rs193281601 | 1 | GCST90860500 | no MR -> candidate analysis |
| F11 protein levels | 2e-62 | rs4686434 | 2 | GCST90469165 | no MR -> candidate analysis |
| Serum levels of protein HRG | 7e-60 | rs62292569 | 1 | GCST90088856 | no MR -> candidate analysis |
| AHSG protein levels | 7e-47 | rs3755838 | 4 | GCST90468263 | no MR -> candidate analysis |
| HRG protein levels | 6e-38 | rs142403242 | 1 | GCST90469476 | no MR -> candidate analysis |
| Histidine-rich glycoprotein levels | 3e-32 | rs77190643 | 1 | GCST90162230 | no MR -> candidate analysis |
| _...and 9 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 156 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| metabolic disease | 0.045 | — | common-variant locus | no MR -> candidate analysis |
| urolithiasis | 0.043 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.043 | — | common-variant locus | no MR -> candidate analysis |
| central nervous system cancer | 0.04 | — | common-variant locus | no MR -> candidate analysis |

> Of the 4 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=2.1e-09, LOEUF=1.24 — LoF-tolerant |
| GWAS Catalog | 207 unique SNPs / 558 rows |
| ClinVar | 120 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 156 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'FETUB'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 120 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 21 traits by best p-value, aggregated from 43 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9UGM5 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000090512/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/FETUB — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/FETUB — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=FETUB%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/FETUB — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:39:39  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
