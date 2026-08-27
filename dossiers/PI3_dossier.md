# Protein Dossier — PI3 (Elafin)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Systolic blood pressure  automated reading | 0.0258 | 0.00824 | 0.00175 | Wald ratio | 1 | cis | NA |
| Caudate volume | 48.8 | 16.1 | 0.00242 | Wald ratio | 1 | cis | NA |
| 2hr glucose | -0.184 | 0.0612 | 0.0027 | Wald ratio | 1 | cis | NA |
| Lung cancer | 0.18 | 0.0639 | 0.00487 | Wald ratio | 1 | cis | NA |
| Bipolar disorder | -0.21 | 0.0791 | 0.00789 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: D25 Leiomyoma of uterus | 0.161 | 0.0608 | 0.00827 | Wald ratio | 1 | cis | NA |
| Large vessel disease | 0.303 | 0.115 | 0.00834 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M23 Internal derangement of knee | 0.125 | 0.0479 | 0.00882 | Wald ratio | 1 | cis | NA |
| LDL cholesterol | -0.0413 | 0.0173 | 0.0171 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: gout | 0.138 | 0.059 | 0.0191 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: anxiety or panic attacks | 0.14 | 0.0606 | 0.0213 | Wald ratio | 1 | cis | NA |
| Squamous cell lung cancer | 0.226 | 0.0997 | 0.0233 | Wald ratio | 1 | cis | NA |
| _...and 107 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-4982_54_1` | Elafin | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_19 association rows across 12 traits (17 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating PI3 levels | 2e-584 | rs56168207 | 4 | GCST90859955 | no MR -> candidate analysis |
| CD59/PI3 protein level ratio | 2e-451 | rs56063128 | 1 | GCST90313858 | no MR -> candidate analysis |
| Elafin levels | 3e-127 | rs35615384 | 3 | GCST90247436 | no MR -> candidate analysis |
| Serum levels of protein PI3 | 5e-45 | rs6104052 | 1 | GCST90088842 | no MR -> candidate analysis |
| PI3 protein levels | 4e-40 | rs77952882 | 1 | GCST90470230 | no MR -> candidate analysis |
| Elafin levels (PI3.4982.54.1) | 2e-35 | rs16989763 | 1 | GCST90241031 | no MR -> candidate analysis |
| Blood protein levels | 5e-32 | rs6104052 | 1 | GCST006585 | no MR -> candidate analysis |
| WFDC12 protein levels | 1e-23 | rs549974756 | 3 | GCST90471073 | no MR -> candidate analysis |
| SDC4 protein levels | 4e-18 | rs1983649 | 1 | GCST90470559 | no MR -> candidate analysis |
| Serum levels of protein SLPI | 1e-15 | rs6130775 | 1 | GCST90088681 | no MR -> candidate analysis |
| Parental longevity (mother's age at death) | 2e-6 | rs34602589 | 1 | GCST003393 | no MR -> candidate analysis |
| IgG glycosylation | 3e-6 | rs7361168 | 1 | GCST001848 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 420 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| placental abruption | 0.293 | — | common-variant locus | no MR -> candidate analysis |
| Abnormal male internal genitalia morphology | 0.165 | — | common-variant locus | no MR -> candidate analysis |
| ectropion | 0.144 | — | common-variant locus | no MR -> candidate analysis |
| entropion | 0.144 | — | common-variant locus | no MR -> candidate analysis |
| bipolar disorder | 0.059 | — | common-variant locus | MR: beta=-0.21, p=0.00789 (cis) |

> Of the 5 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Phosphoinositide 3-kinase regulatory subunit 4) |
| gnomAD constraint | pLI=0.06, LOEUF=1.54 — LoF-tolerant |
| GWAS Catalog | 54 unique SNPs / 108 rows |
| ClinVar | 28 records; 10 pathogenic in sample of 28 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 420 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'PI3' and resolved to 'Phosphoinositide 3-kinase regulatory subunit 4' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 28 record(s) retrieved, NOT over all 28 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 12 of 12 traits by best p-value, aggregated from 19 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P19957 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000124102/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2189144/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PI3 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PI3 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PI3%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/PI3 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:19:45  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
