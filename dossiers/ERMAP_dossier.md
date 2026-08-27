# Protein Dossier — ERMAP (Erythroid membrane-associated protein)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: I48 Atrial fibrillation and flutter | 0.233 | 0.0971 | 0.0164 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: enlarged prostate | 0.214 | 0.0893 | 0.0167 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: K20 Oesophagitis | 0.236 | 0.103 | 0.0225 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: Z09 Follow-up examination after treatment for conditions other than malignant neoplasms | -0.337 | 0.15 | 0.0248 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: N40 Hyperplasia of prostate | 0.233 | 0.107 | 0.0296 | Wald ratio | 1 | trans | NA |
| Fractured bone site(s): Wrist | -0.252 | 0.12 | 0.0354 | Wald ratio | 1 | trans | NA |
| Fractured bone site(s): Arm | 0.216 | 0.105 | 0.04 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: R04 Haemorrhage from respiratory passages | 0.281 | 0.138 | 0.0412 | Wald ratio | 1 | trans | NA |
| Pallidum volume | -19.7 | 9.96 | 0.0485 | Wald ratio | 1 | trans | NA |
| Thalamus volume | -61.6 | 32.9 | 0.0609 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: asthma | -0.0718 | 0.0386 | 0.0631 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: kidney stone or ureter stone or bladder stone | 0.219 | 0.118 | 0.0645 | Wald ratio | 1 | trans | NA |
| _...and 69 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_6 association rows across 5 traits (4 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| ERMAP protein levels | 1e-36 | rs3214967 | 1 | GCST90469147 | no MR -> candidate analysis |
| Red blood cell erythrocyte distribution width (UKB data fiel | 1e-13 | rs34441268 | 1 | GCST90468099 | no MR -> candidate analysis |
| Red cell distribution width | 5e-12 | rs12406643 | 2 | GCST007074 | no MR -> candidate analysis |
| Stuttering | 2e-6 | rs567238919 | 1 | GCST90707226 | no MR -> candidate analysis |
| Visceral fat | 6e-6 | rs72666872 | 1 | GCST008473 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 81 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| hypertensive disorder | 0.474 | — | common-variant locus | no MR -> candidate analysis |
| cardiovascular disorder | 0.356 | — | common-variant locus | no MR -> candidate analysis |
| placental abruption | 0.045 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=2.1e-08, LOEUF=0.915 — LoF-tolerant |
| GWAS Catalog | 23 unique SNPs / 46 rows |
| ClinVar | 103 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 81 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'ERMAP'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 103 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 5 of 5 traits by best p-value, aggregated from 6 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q96PL5 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000164010/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/ERMAP — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/ERMAP — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=ERMAP%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/ERMAP — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:28:50  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
