# Protein Dossier — METAP2 (Methionine aminopeptidase 2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Mean platelet volume | -0.0813 | 0.0047 | 4.12e-67 | Wald ratio | 1 | trans | NA |
| Platelet count | 26 | 1.73 | 5.20e-51 | Wald ratio | 1 | trans | NA |
| Systemic lupus erythematosus | 0.502 | 0.171 | 0.00333 | Wald ratio | 1 | trans | NA |
| Juvenile idiopathic arthritis | 0.511 | 0.201 | 0.0108 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: hypertension | 0.037 | 0.0146 | 0.0111 | Wald ratio | 1 | trans | NA |
| Years of schooling | -0.0325 | 0.0145 | 0.0244 | Wald ratio | 1 | trans | NA |
| Knee and hip osteoarthritis | 0.176 | 0.0795 | 0.0265 | Wald ratio | 1 | trans | NA |
| Schizophrenia | -0.0875 | 0.0398 | 0.0278 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: N92 Excessive  frequent and irregular menstruation | 0.12 | 0.0549 | 0.0295 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: I48 Atrial fibrillation and flutter | 0.157 | 0.0721 | 0.0298 | Wald ratio | 1 | trans | NA |
| 2hr glucose | 0.166 | 0.0795 | 0.0365 | Wald ratio | 1 | trans | NA |
| Squamous cell lung cancer | 0.202 | 0.0978 | 0.0385 | Wald ratio | 1 | trans | NA |
| _...and 96 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3170_6_1` | AMPM2 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_18 association rows across 16 traits (16 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Height | 7e-65 | rs2596741 | 2 | GCST90245848 | no MR -> candidate analysis |
| High light scatter reticulocyte percentage of red cells | 3e-53 | rs784487 | 1 | GCST90002386 | no MR -> candidate analysis |
| High light scatter reticulocyte count | 1e-51 | rs784487 | 1 | GCST90002385 | no MR -> candidate analysis |
| Immature fraction of reticulocytes | 1e-45 | rs34994986 | 2 | GCST90002387 | no MR -> candidate analysis |
| Reticulocyte count | 3e-32 | rs784487 | 1 | GCST90002405 | no MR -> candidate analysis |
| height (mean, inv-normal transformed) | 9e-17 | rs301033 | 1 | GCST90479635 | no MR -> candidate analysis |
| Height (maximum, inv-normal transformed) | 6e-16 | rs301033 | 1 | GCST90479634 | no MR -> candidate analysis |
| Circulating METAP2 levels | 8e-16 | rs784487 | 1 | GCST90860036 | no MR -> candidate analysis |
| METAP2 protein levels | 1e-14 | rs784487 | 1 | GCST90469894 | no MR -> candidate analysis |
| Core binding factor acute myeloid leukemia | 2e-10 | rs301009; rs301011; rs11614671; rs4762519; rs11519597; rs2769469; rs2596741; rs3794261; rs1057739; rs301026; rs301024; rs7974458; rs301003; rs10777699; rs3812813; rs11108094; rs10498964; rs2769444 | 1 | GCST008413 | no MR -> candidate analysis |
| Sex hormone-binding globulin levels | 8e-10 | rs528806375 | 1 | GCST90012107 | no MR -> candidate analysis |
| Sex hormone-binding globulin levels adjusted for BMI | 2e-9 | rs528806375 | 1 | GCST90012106 | no MR -> candidate analysis |
| _...and 4 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 166 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| preeclampsia | 0.441 | — | common-variant locus | no MR -> candidate analysis |
| type 2 diabetes mellitus | 0.266 | — | common-variant locus | no MR -> candidate analysis |
| sialolithiasis | 0.142 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 2 known modulators (Methionine aminopeptidase 2) |
| gnomAD constraint | pLI=0.16, LOEUF=0.588 — LoF-tolerant |
| GWAS Catalog | 70 unique SNPs / 140 rows |
| ClinVar | 63 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 166 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'METAP2' and resolved to 'Methionine aminopeptidase 2' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 63 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 16 of 16 traits by best p-value, aggregated from 18 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P50579 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000111142/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3922/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/METAP2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/METAP2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=METAP2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/METAP2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:46:17  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
