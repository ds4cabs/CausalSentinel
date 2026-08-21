# Protein Dossier — PSMB1 (Proteasome subunit beta type-1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Age at menarche | -0.0388 | 0.0141 | 0.0059 | Wald ratio | 1 | cis | NA |
| ER-negative Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.0716 | 0.0282 | 0.011 | Wald ratio | 1 | cis | NA |
| Weight | -0.0123 | 0.00524 | 0.0188 | Wald ratio | 1 | cis | NA |
| Hearing difficulty or problems: Yes | -0.0242 | 0.0105 | 0.0212 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code self-reported: pulmonary embolism (with or without) dvt | 0.131 | 0.058 | 0.0239 | Wald ratio | 1 | cis | NA |
| Years of schooling | -0.0218 | 0.00971 | 0.0244 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | -0.0131 | 0.00594 | 0.0278 | Wald ratio | 1 | cis | NA |
| Alzheimer's disease | -0.0854 | 0.0403 | 0.034 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K57 Diverticular disease of intestine | -0.0957 | 0.0461 | 0.0378 | Wald ratio | 1 | cis | NA |
| Myocardial infarction | 0.0511 | 0.0253 | 0.0435 | Wald ratio | 1 | cis | NA |
| Gallbladder cancer | -1.6 | 0.796 | 0.0443 | Wald ratio | 1 | cis | NA |
| Mean cell haemoglobin concentration | 0.0167 | 0.0085 | 0.0487 | Wald ratio | 1 | cis | NA |
| _...and 101 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_11 association rows across 10 traits (10 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Serum levels of protein PSMB1 | 2e-101 | rs6930789 | 1 | GCST90087098 | no MR -> candidate analysis |
| Blood protein levels | 8e-67 | rs756519 | 1 | GCST006585 | no MR -> candidate analysis |
| Adolescent idiopathic scoliosis | 1e-31 | rs760500 | 1 | GCST006287 | no MR -> candidate analysis |
| Height | 1e-27 | rs11755081 | 2 | GCST90245848 | MR: beta=-0.0117, p=0.11 (cis) |
| Hematological traits (multi-trait analysis) | 2e-13 | rs9460014 | 1 | GCST90838669 | no MR -> candidate analysis |
| Red blood cell count | 1e-11 | rs9460014 | 1 | GCST90002363 | no MR -> candidate analysis |
| Platelet count | 3e-11 | rs9460014 | 1 | GCST90002357 | no MR -> candidate analysis |
| Total bilirubin levels | 6e-9 | rs11755081 | 1 | GCST90662900 | no MR -> candidate analysis |
| Dorsolateral prefrontal area | 2e-8 | rs6915605 | 1 | GCST90572714 | no MR -> candidate analysis |
| Memory decline in normal cognition | 5e-6 | rs7753099 | 1 | GCST90448447 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 273 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| neurodevelopmental disorder with microcephaly, hypotonia, and absent language | 0.596 | — | established (curated) | no MR -> candidate analysis |
| alcohol drinking | 0.339 | — | common-variant locus | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Proteasome component C5) |
| gnomAD constraint | pLI=0.97, LOEUF=0.518 — LoF-INTOLERANT |
| GWAS Catalog | 28 unique SNPs / 42 rows |
| ClinVar | 134 records; 10 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 273 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'PSMB1' and resolved to 'Proteasome component C5' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 134 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 10 of 10 traits by best p-value, aggregated from 11 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P20618 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000008018/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4208/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PSMB1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PSMB1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PSMB1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/PSMB1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:40:07  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
