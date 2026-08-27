# Protein Dossier — CD59 (CD59 glycoprotein)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Pulse rate | -0.0422 | 0.0133 | 0.00157 | Wald ratio | 1 | cis | NA |
| Systolic blood pressure  automated reading | -0.0226 | 0.00775 | 0.00347 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K20 Oesophagitis | 0.179 | 0.0642 | 0.00524 | Wald ratio | 1 | cis | NA |
| Birth weight | -0.0304 | 0.0119 | 0.0105 | Wald ratio | 1 | cis | NA |
| Pancreatic cancer | -0.385 | 0.151 | 0.0107 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: G47 Sleep disorders | 0.196 | 0.0818 | 0.0167 | Wald ratio | 1 | cis | NA |
| Diastolic blood pressure  automated reading | -0.0179 | 0.00775 | 0.0213 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | 0.0168 | 0.00757 | 0.0266 | Wald ratio | 1 | cis | NA |
| Thyroid cancer | 0.719 | 0.33 | 0.0293 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M17 Gonarthrosis [arthrosis of knee] | 0.107 | 0.0491 | 0.0296 | Wald ratio | 1 | cis | NA |
| Large vessel disease | -0.231 | 0.11 | 0.0348 | Wald ratio | 1 | cis | NA |
| Forearm bone mineral density | 0.104 | 0.0498 | 0.0374 | Wald ratio | 1 | cis | NA |
| _...and 96 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_21 association rows across 15 traits (19 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating CD59 levels | 7e-293 | rs2273121 | 3 | GCST90860447 | no MR -> candidate analysis |
| CD59 protein levels | 5e-288 | rs704701 | 2 | GCST90468639 | no MR -> candidate analysis |
| CD59 glycoprotein levels (CD59.11514.196.3) | 5e-41 | rs2273121 | 1 | GCST90240644 | no MR -> candidate analysis |
| CD59 glycoprotein levels | 5e-31 | rs704701 | 2 | GCST90246945 | no MR -> candidate analysis |
| Serum levels of protein CD59 | 3e-30 | rs831636 | 1 | GCST90086775 | no MR -> candidate analysis |
| Morning person | 1e-27 | rs11032362 | 2 | GCST007565 | no MR -> candidate analysis |
| Chronotype | 1e-27 | rs11032362 | 1 | GCST007576 | no MR -> candidate analysis |
| Morningness | 3e-17 | rs11032362 | 1 | GCST007983 | no MR -> candidate analysis |
| Blood protein levels | 1e-14 | rs831636 | 1 | GCST006585 | no MR -> candidate analysis |
| Fresh fruit consumption | 3e-11 | rs11032362 | 1 | GCST90132979 | no MR -> candidate analysis |
| Calcium (mean, inv-norm transformed) | 4e-11 | rs1718066 | 1 | GCST90479530 | no MR -> candidate analysis |
| Fruit consumption | 1e-10 | rs11032362 | 1 | GCST010136 | no MR -> candidate analysis |
| _...and 3 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1099 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| primary CD59 deficiency | 0.769 | — | established (curated) | no MR -> candidate analysis |
| hereditary disease | 0.294 | — | established (curated) | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (CD59 glycoprotein) |
| gnomAD constraint | pLI=0.29, LOEUF=1.1 — LoF-tolerant |
| GWAS Catalog | 25 unique SNPs / 50 rows |
| ClinVar | 149 records; 8 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1099 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'CD59' and resolved to 'CD59 glycoprotein' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 149 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 15 of 15 traits by best p-value, aggregated from 21 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P13987 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000085063/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL5724795/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CD59 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CD59 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CD59%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CD59 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:43:48  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
