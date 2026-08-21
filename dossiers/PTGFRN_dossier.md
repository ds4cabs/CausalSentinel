# Protein Dossier — PTGFRN (Prostaglandin F2 receptor negative regulator)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: joint disorder | 0.129 | 0.0414 | 0.00179 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | 0.0108 | 0.00417 | 0.00978 | Wald ratio | 1 | cis | NA |
| Sleep duration | -0.00579 | 0.00252 | 0.0214 | Wald ratio | 1 | cis | NA |
| Platelet count | 1.19 | 0.538 | 0.0271 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K29 Gastritis and duodenitis | -0.0475 | 0.0219 | 0.03 | Wald ratio | 1 | cis | NA |
| Endometrioid ovarian cancer | 0.0795 | 0.0386 | 0.0395 | Wald ratio | 1 | cis | NA |
| ER-positive Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | 0.021 | 0.0102 | 0.0395 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: G56 Mononeuropathies of upper limb | -0.0531 | 0.0259 | 0.04 | Wald ratio | 1 | cis | NA |
| Depressive symptoms | -0.00999 | 0.005 | 0.0455 | Wald ratio | 1 | cis | NA |
| Urate | 0.014 | 0.0071 | 0.0486 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: diverticular disease or diverticulitis | -0.0641 | 0.0325 | 0.0487 | Wald ratio | 1 | cis | NA |
| Bipolar disorder | 0.0622 | 0.0318 | 0.0505 | Wald ratio | 1 | cis | NA |
| _...and 90 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_70 association rows across 36 traits (60 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Prostaglandin F2 receptor negative regulator levels | 3e-431 | rs4233450 | 5 | GCST90248965 | no MR -> candidate analysis |
| Prostaglandin F2 receptor negative regulator levels (PTGFRN. | 2e-273 | rs4233450 | 3 | GCST90242401 | no MR -> candidate analysis |
| Serum levels of protein PTGFRN | 4e-83 | rs4233450 | 2 | GCST90087188 | no MR -> candidate analysis |
| CD101 protein levels | 2e-76 | rs75641997 | 10 | GCST90468596 | no MR -> candidate analysis |
| Prostaglandin F2 receptor negative regulator level in Chroni | 1e-75 | rs10159095 | 1 | GCST90233651 | no MR -> candidate analysis |
| Blood protein levels | 2e-50 | rs4233450 | 1 | GCST006585 | no MR -> candidate analysis |
| Type 2 diabetes | 2e-38 | rs1127215 | 10 | GCST90492734 | no MR -> candidate analysis |
| Type 2 diabetes (PheCode 250.2) | 3e-21 | rs1127215 | 2 | GCST90475667 | no MR -> candidate analysis |
| Diabetes mellitus (PheCode 250) | 1e-20 | rs1127215 | 2 | GCST90475658 | no MR -> candidate analysis |
| Neutrophil count | 3e-16 | rs72699131 | 4 | GCST90101731 | no MR -> candidate analysis |
| Height | 4e-16 | rs17036665 | 1 | GCST90245848 | no MR -> candidate analysis |
| Circulating CDH3 levels | 1e-15 | rs12130298 | 1 | GCST90859696 | no MR -> candidate analysis |
| _...and 24 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 130 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| type 2 diabetes mellitus | 0.756 | — | common-variant locus | no MR -> candidate analysis |
| diabetes mellitus | 0.505 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.349 | — | common-variant locus | no MR -> candidate analysis |
| diabetic neuropathy | 0.15 | — | common-variant locus | no MR -> candidate analysis |
| poisoning | 0.134 | — | common-variant locus | no MR -> candidate analysis |
| neutropenia | 0.046 | — | common-variant locus | no MR -> candidate analysis |

> Of the 6 rows above, **6 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.11, LOEUF=0.558 — LoF-tolerant |
| GWAS Catalog | 55 unique SNPs / 108 rows |
| ClinVar | 180 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 130 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'PTGFRN'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 180 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 36 traits by best p-value, aggregated from 70 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9P2B2 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000134247/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PTGFRN — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PTGFRN — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PTGFRN%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/PTGFRN — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:40:59  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
