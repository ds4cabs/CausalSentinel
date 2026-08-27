# Protein Dossier — BCL10 (B-cell lymphoma/leukemia 10)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: hypopituitarism | 1.23 | 0.197 | 4.09e-10 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: hypertrophic cardiomyopathy (hcm  or  hocm) | 1.15 | 0.292 | 8.42e-05 | Wald ratio | 1 | trans | NA |
| Weight | -0.0379 | 0.0105 | 3.08e-04 | Wald ratio | 1 | trans | NA |
| Body mass index (BMI) | -0.0382 | 0.0119 | 0.00133 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: Z09 Follow-up examination after treatment for conditions other than malignant neoplasms | 0.206 | 0.0794 | 0.00959 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: C61 Malignant neoplasm of prostate | 0.275 | 0.113 | 0.0146 | Wald ratio | 1 | trans | NA |
| Cancer code  self-reported: prostate cancer | 0.248 | 0.11 | 0.0246 | Wald ratio | 1 | trans | NA |
| Potassium in urine | -0.0244 | 0.0121 | 0.0432 | Wald ratio | 1 | trans | NA |
| Thalamus volume | 71.2 | 37.8 | 0.0599 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: chronic obstructive airways disease or copd | 0.288 | 0.158 | 0.0679 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: K20 Oesophagitis | 0.183 | 0.101 | 0.07 | Wald ratio | 1 | trans | NA |
| Cancer code  self-reported: basal cell carcinoma | 0.188 | 0.104 | 0.0722 | Wald ratio | 1 | trans | NA |
| _...and 60 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_74 association rows across 47 traits (67 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating DDAH1 levels | 6e-132 | rs2284797 | 2 | GCST90860518 | no MR -> candidate analysis |
| DDAH1 protein levels | 7e-131 | rs12138621 | 2 | GCST90468966 | no MR -> candidate analysis |
| X-24518 levels | 3e-119 | rs233074 | 2 | GCST90200634 | no MR -> candidate analysis |
| Urine X-24518 levels in chronic kidney disease | 2e-98 | rs233071 | 1 | GCST90266747 | no MR -> candidate analysis |
| Height | 5e-94 | rs17388521 | 2 | GCST90245848 | no MR -> candidate analysis |
| Plasma X-24518 levels in chronic kidney disease | 6e-91 | rs233069 | 1 | GCST90266746 | no MR -> candidate analysis |
| Urine X-12097 levels in chronic kidney disease | 7e-42 | rs4949890 | 1 | GCST90266194 | no MR -> candidate analysis |
| Asymmetrical dimethylarginine levels | 1e-40 | rs28489187 | 2 | GCST002241 | no MR -> candidate analysis |
| Protein quantitative trait loci (liver) | 8e-37 | rs233112 | 9 | GCST011427 | no MR -> candidate analysis |
| Dimethylarginine (sdma + adma) levels | 1e-34 | rs233050 | 4 | GCST90245172 | no MR -> candidate analysis |
| Urinary metabolite levels in chronic kidney disease | 2e-32 | rs3949301 | 2 | GCST009733 | no MR -> candidate analysis |
| Metabolite levels (dimethylarginine (SDMA + ADMA); ADMA) | 1e-23 | rs233066 | 1 | GCST90299584 | no MR -> candidate analysis |
| _...and 35 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 348 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| immunodeficiency 37 | 0.861 | — | established (curated) | no MR -> candidate analysis |
| MALT lymphoma | 0.195 | — | established (curated) | no MR -> candidate analysis |
| testicular germ cell tumor | 0.195 | — | established (curated) | no MR -> candidate analysis |
| multiple sclerosis | 0.61 | — | common-variant locus | no MR -> candidate analysis |

> Of the 4 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Caspase recruitment domain-containing protein 19) |
| gnomAD constraint | pLI=0.94, LOEUF=0.546 — LoF-INTOLERANT |
| GWAS Catalog | 62 unique SNPs / 109 rows |
| ClinVar | 166 records; 4 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 348 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'BCL10' and resolved to 'Caspase recruitment domain-containing protein 19' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 166 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 47 traits by best p-value, aggregated from 74 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O95999 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000142867/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL6067439/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/BCL10 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/BCL10 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=BCL10%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/BCL10 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:17:00  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
