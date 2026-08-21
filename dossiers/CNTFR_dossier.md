# Protein Dossier — CNTFR (Ciliary neurotrophic factor receptor subunit alpha)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: bladder problem (not cancer) | 0.408 | 0.115 | 3.85e-04 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: depression | 0.127 | 0.0472 | 0.00714 | Wald ratio | 1 | cis | NA |
| Caudate volume | 81.3 | 30.5 | 0.00775 | Wald ratio | 1 | cis | NA |
| Clear cell ovarian cancer | 0.602 | 0.248 | 0.0152 | Wald ratio | 1 | cis | NA |
| Diastolic blood pressure  automated reading | 0.0314 | 0.0133 | 0.0179 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: diverticular disease or diverticulitis | 0.23 | 0.0985 | 0.0195 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | 0.0261 | 0.0112 | 0.0202 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K60 Fissure and fistula of anal and rectal regions | 0.297 | 0.146 | 0.0423 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | 0.0211 | 0.0106 | 0.0472 | Wald ratio | 1 | cis | NA |
| Nucleus accumbens volume | 14.2 | 7.22 | 0.0491 | Wald ratio | 1 | cis | NA |
| Putamen volume | 71 | 36.7 | 0.0531 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Wrist | 0.14 | 0.081 | 0.0832 | Wald ratio | 1 | cis | NA |
| _...and 55 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2711_6_2` | CNTFR alpha | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_24 association rows across 20 traits (21 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Ciliary neurotrophic factor receptor subunit alpha levels | 2e-48 | rs10972159 | 2 | GCST90247080 | no MR -> candidate analysis |
| Serum levels of protein CNTFR | 4e-32 | rs10972159 | 2 | GCST90087783 | no MR -> candidate analysis |
| NUDT2 protein levels | 1e-19 | rs7037232 | 1 | GCST90470106 | no MR -> candidate analysis |
| Blood protein levels | 3e-18 | rs1571401 | 2 | GCST006585 | no MR -> candidate analysis |
| Osteoarthritis | 2e-14 | rs7036975 | 1 | GCST90566795 | no MR -> candidate analysis |
| Ciliary neurotrophic factor receptor subunit alpha levels (C | 1e-13 | rs10972159 | 1 | GCST90240708 | no MR -> candidate analysis |
| IDUA protein levels | 3e-13 | rs3763613 | 1 | GCST90469508 | no MR -> candidate analysis |
| Ciliary neurotrophic factor receptor subunit alpha level in  | 3e-12 | rs73645429 | 1 | GCST90234188 | no MR -> candidate analysis |
| Body mass index | 3e-12 | rs73645429 | 1 | GCST90662912 | no MR -> candidate analysis |
| Diastolic blood pressure | 2e-11 | rs10814119 | 1 | GCST90662909 | MR: beta=0.0314, p=0.0179 (cis) |
| Adolescent idiopathic scoliosis | 2e-10 | rs13290451 | 2 | GCST008788 | no MR -> candidate analysis |
| Aspartate aminotransferase levels | 1e-9 | rs13290451 | 1 | GCST90018944 | no MR -> candidate analysis |
| _...and 8 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 229 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| response to antihypertensive drug | 0.344 | — | common-variant locus | no MR -> candidate analysis |
| hypertensive disorder | 0.122 | — | common-variant locus | no MR -> candidate analysis |
| response to xenobiotic stimulus | 0.088 | — | common-variant locus | no MR -> candidate analysis |
| Nephropathy | 0.088 | — | common-variant locus | no MR -> candidate analysis |
| nephritis | 0.088 | — | common-variant locus | no MR -> candidate analysis |
| hypertensive heart disease | 0.083 | — | common-variant locus | no MR -> candidate analysis |

> Of the 6 rows above, **6 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.99, LOEUF=0.481 — LoF-INTOLERANT |
| GWAS Catalog | 50 unique SNPs / 99 rows |
| ClinVar | 130 records; 5 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 229 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'CNTFR'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 130 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 20 traits by best p-value, aggregated from 24 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P26992 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000122756/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CNTFR — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CNTFR — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CNTFR%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CNTFR — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:55:06  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
