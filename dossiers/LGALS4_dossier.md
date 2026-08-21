# Protein Dossier — LGALS4 (Galectin-4)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Pulse rate | 0.133 | 0.0234 | 1.50e-08 | Wald ratio | 1 | cis | NA |
| Lumbar spine bone mineral density | 0.191 | 0.0486 | 8.26e-05 | Wald ratio | 1 | cis | NA |
| Diastolic blood pressure  automated reading | 0.0532 | 0.0136 | 9.20e-05 | Wald ratio | 1 | cis | NA |
| Femoral neck bone mineral density | 0.161 | 0.0418 | 1.18e-04 | Wald ratio | 1 | cis | NA |
| Birth weight | 0.0652 | 0.0204 | 0.00143 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: D12 Benign neoplasm of colon  rectum  anus and anal canal | 0.27 | 0.0865 | 0.00181 | Wald ratio | 1 | cis | NA |
| HDL cholesterol | -0.0823 | 0.0265 | 0.00191 | Wald ratio | 1 | cis | NA |
| Lung cancer | -0.319 | 0.105 | 0.0024 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: vitiligo | 0.996 | 0.339 | 0.00328 | Wald ratio | 1 | cis | NA |
| Alcohol intake frequency | -0.056 | 0.0197 | 0.00436 | Wald ratio | 1 | cis | NA |
| Serum creatinine (eGFRcrea) | -0.0144 | 0.00508 | 0.00471 | Wald ratio | 1 | cis | NA |
| Mean platelet volume | -0.0155 | 0.00608 | 0.0109 | Wald ratio | 1 | cis | NA |
| _...and 111 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2982_82_2` | Galectin-4 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_7 association rows across 5 traits (7 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating LGALS7_LGALS7B levels | 6e-55 | rs58866020 | 2 | GCST90860535 | no MR -> candidate analysis |
| LGALS7 or LGALS7B protein levels | 9e-52 | rs58866020 | 2 | GCST90469763 | no MR -> candidate analysis |
| Blood protein levels | 2e-33 | rs4802890 | 1 | GCST006585 | no MR -> candidate analysis |
| Enoyl-CoA delta isomerase 2, mitochondrial levels | 4e-22 | rs4802890 | 1 | GCST90247387 | no MR -> candidate analysis |
| Phosphatidylcholines (35:2)B levels | 3e-8 | rs116923791 | 1 | GCST90102044 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 370 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Transient global amnesia | 0.155 | — | common-variant locus | no MR -> candidate analysis |
| coronary artery disorder | 0.052 | — | common-variant locus | no MR -> candidate analysis |
| Bell's palsy | 0.082 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Galectin-4) |
| gnomAD constraint | pLI=2e-12, LOEUF=1.23 — LoF-tolerant |
| GWAS Catalog | 60 unique SNPs / 120 rows |
| ClinVar | 67 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 370 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'LGALS4' and resolved to 'Galectin-4' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 67 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 5 of 5 traits by best p-value, aggregated from 7 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P56470 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000171747/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL1671608/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/LGALS4 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/LGALS4 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=LGALS4%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/LGALS4 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:31:16  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
