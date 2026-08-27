# Protein Dossier — FOXJ2 (Forkhead box protein J2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: R07 Pain in throat and chest | 0.113 | 0.0323 | 4.93e-04 | Wald ratio | 1 | trans | NA |
| Systolic blood pressure  automated reading | 0.0266 | 0.00827 | 0.0013 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: high cholesterol | 0.0559 | 0.0207 | 0.0069 | Wald ratio | 1 | trans | NA |
| Vascular or heart problems diagnosed by doctor: Angina | 0.107 | 0.0408 | 0.00862 | Wald ratio | 1 | trans | NA |
| Hippocampus volume | -36.8 | 14 | 0.0088 | Wald ratio | 1 | trans | NA |
| Hearing difficulty or problems: Yes | 0.0349 | 0.0135 | 0.0097 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: B37 Candidiasis | 0.586 | 0.229 | 0.0103 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: I48 Atrial fibrillation and flutter | 0.166 | 0.0652 | 0.0109 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: hyperthyroidism or thyrotoxicosis | 0.194 | 0.078 | 0.0128 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: H25 Senile cataract | -0.321 | 0.13 | 0.0133 | Wald ratio | 1 | trans | NA |
| Primary sclerosing cholangitis  | -0.206 | 0.0854 | 0.0161 | Wald ratio | 1 | trans | NA |
| Eye problems or disorders: Glaucoma | 0.141 | 0.0587 | 0.0164 | Wald ratio | 1 | trans | NA |
| _...and 79 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_17 association rows across 15 traits (16 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| CLEC4C protein levels | 3e-22 | rs117813943 | 2 | GCST90468772 | no MR -> candidate analysis |
| MGLL/PLA2G4A protein level ratio | 1e-17 | rs7957980 | 1 | GCST90315439 | no MR -> candidate analysis |
| Mean reticulocyte volume | 7e-17 | rs3782679 | 1 | GCST90002396 | no MR -> candidate analysis |
| CD69/F2R protein level ratio | 2e-16 | rs12304020 | 1 | GCST90313877 | no MR -> candidate analysis |
| Neutrophil count | 1e-15 | rs10846411 | 2 | GCST90002351 | no MR -> candidate analysis |
| Monocyte percentage (UKB data field 30190) | 5e-15 | rs10846411 | 1 | GCST90468091 | no MR -> candidate analysis |
| CD69/NFATC1 protein level ratio | 1e-14 | rs12304020 | 1 | GCST90313879 | no MR -> candidate analysis |
| Mean reticulocyte volume (UKB data field 30260) | 2e-13 | rs3782679 | 1 | GCST90468088 | no MR -> candidate analysis |
| Mean spheric corpuscular volume | 1e-12 | rs55680021 | 1 | GCST90002397 | no MR -> candidate analysis |
| Height | 1e-12 | rs11609309 | 1 | GCST90245848 | MR: beta=-0.00809, p=0.413 (trans) |
| Sebaceous cyst (PheCode 706.2) | 2e-12 | rs12304020 | 1 | GCST90480482 | no MR -> candidate analysis |
| Neutrophil percentage of white cells | 2e-11 | rs4883480 | 1 | GCST90002399 | no MR -> candidate analysis |
| _...and 3 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 97 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Epidermal Inclusion Cyst | 0.225 | — | common-variant locus | no MR -> candidate analysis |
| Abnormality of the skeletal system | 0.209 | — | common-variant locus | no MR -> candidate analysis |
| oral cavity neoplasm | 0.179 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1, LOEUF=0.39 — LoF-INTOLERANT |
| GWAS Catalog | 49 unique SNPs / 98 rows |
| ClinVar | 140 records; 5 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 97 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'FOXJ2'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 140 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 15 of 15 traits by best p-value, aggregated from 17 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9P0K8 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000065970/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/FOXJ2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/FOXJ2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=FOXJ2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/FOXJ2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:42:54  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
