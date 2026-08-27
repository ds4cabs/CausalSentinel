# Protein Dossier — A1CF (APOBEC1 complementation factor)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Serum creatinine (eGFRcrea) | -0.014 | 0.00301 | 3.44e-06 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: K60 Fissure and fistula of anal and rectal regions | 0.339 | 0.0874 | 1.07e-04 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: Z09 Follow-up examination after treatment for conditions other than malignant neoplasms | 0.148 | 0.0579 | 0.0107 | Wald ratio | 1 | trans | NA |
| Type 2 diabetes | -0.105 | 0.0418 | 0.0121 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code self-reported: pulmonary embolism (with or without) dvt | -0.307 | 0.126 | 0.0149 | Wald ratio | 1 | trans | NA |
| Fracture resulting from simple fall | -0.0537 | 0.0231 | 0.0199 | Wald ratio | 1 | trans | NA |
| Fractured or broken bones in last 5 years | -0.0569 | 0.0271 | 0.0359 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | 0.168 | 0.0833 | 0.0433 | Wald ratio | 1 | trans | NA |
| Eye problems or disorders: Glaucoma | 0.121 | 0.0612 | 0.0486 | Wald ratio | 1 | trans | NA |
| Caudate volume | 31.9 | 16.4 | 0.0515 | Wald ratio | 1 | trans | NA |
| Neo-openness to experience | -0.429 | 0.224 | 0.0559 | Wald ratio | 1 | trans | NA |
| Haemoglobin concentration | -0.04 | 0.0213 | 0.0603 | Wald ratio | 1 | trans | NA |
| _...and 100 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_182 association rows across 104 traits (171 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Serum urate levels | 8e-95 | rs10994860 | 4 | GCST90455669 | no MR -> candidate analysis |
| Gamma glutamyl transferase levels | 1e-84 | rs151068477 | 7 | GCST90662899 | no MR -> candidate analysis |
| Urate levels (UKB data field 30880) | 3e-78 | rs10994860 | 1 | GCST90468107 | no MR -> candidate analysis |
| Serum uric acid levels | 8e-67 | rs10994860 | 2 | GCST90018977 | no MR -> candidate analysis |
| Gamma glutamyltransferase levels (UKB data field 30730) | 1e-59 | rs151068477 | 2 | GCST90468070 | no MR -> candidate analysis |
| Creatinine levels | 2e-54 | rs11375604 | 4 | GCST90662902 | no MR -> candidate analysis |
| Estimated glomerular filtration rate (creatinine) | 5e-54 | rs10821905 | 4 | GCST90103633 | no MR -> candidate analysis |
| Urate levels | 9e-51 | rs17592117 | 8 | GCST011119 | no MR -> candidate analysis |
| Gamma glutamyl transpeptidase | 2e-48 | rs151068477 | 1 | GCST90018954 | no MR -> candidate analysis |
| Gout | 5e-45 | rs10994860 | 2 | GCST90455676 | no MR -> candidate analysis |
| Estimated glomerular filtration rate (creatinine, cystatin c | 5e-44 | rs10821907 | 1 | GCST90428446 | no MR -> candidate analysis |
| Creatinine levels (UKB data field 30700) | 3e-43 | rs10821907 | 1 | GCST90468067 | no MR -> candidate analysis |
| _...and 92 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 431 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| gout | 0.821 | — | common-variant locus | no MR -> candidate analysis |
| familial hyperlipidemia | 0.67 | — | common-variant locus | no MR -> candidate analysis |
| colorectal cancer | 0.534 | — | established (curated) | no MR -> candidate analysis |
| colorectal adenoma | 0.519 | — | common-variant locus | no MR -> candidate analysis |
| renal dialysis | 0.48 | — | common-variant locus | no MR -> candidate analysis |
| skull disorder | 0.48 | — | common-variant locus | no MR -> candidate analysis |
| type 2 diabetes mellitus | 0.414 | — | common-variant locus | no MR -> candidate analysis |

> Of the 7 rows above, **7 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1.1e-11, LOEUF=0.887 — LoF-tolerant |
| GWAS Catalog | 57 unique SNPs / 114 rows |
| ClinVar | 92 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 431 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'A1CF'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 92 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 104 traits by best p-value, aggregated from 182 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9NQ94 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000148584/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/A1CF — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/A1CF — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=A1CF%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/A1CF — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T00:50:27  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
