# Protein Dossier — APOB (Apolipoprotein B-100)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| LDL cholesterol | -0.19 | 0.0122 | 1.84e-54 | Wald ratio | 1 | cis | NA |
| Total cholesterol | -0.154 | 0.0119 | 1.22e-38 | Wald ratio | 1 | cis | NA |
| HDL cholesterol | 0.092 | 0.0112 | 2.29e-16 | Wald ratio | 1 | cis | NA |
| Triglycerides | -0.0841 | 0.0112 | 6.38e-14 | Wald ratio | 1 | cis | NA |
| Neo-openness to experience | 0.747 | 0.235 | 0.0015 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: gastro-oesophageal reflux (gord)  or  gastric reflux | 0.00391 | 0.00178 | 0.028 | Inverse variance weighted | 3 | trans | NA |
| Non-cancer illness code  self-reported: gastro-oesophageal reflux (gord)  or  gastric reflux | 0.00391 | 0.00178 | 0.028 | Inverse variance weighted | 3 | trans | NA |
| Non-cancer illness code  self-reported: gastro-oesophageal reflux (gord)  or  gastric reflux | 0.00391 | 0.00178 | 0.028 | Inverse variance weighted | 3 | cis | NA |
| Subjective well being | -0.0198 | 0.00948 | 0.0368 | Inverse variance weighted | 2 | trans | NA |
| Subjective well being | -0.0198 | 0.00948 | 0.0368 | Inverse variance weighted | 2 | cis | NA |
| ER-negative Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.0701 | 0.0336 | 0.0368 | Inverse variance weighted | 3 | trans | NA |
| ER-negative Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.0701 | 0.0336 | 0.0368 | Inverse variance weighted | 3 | trans | NA |
| _...and 237 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2797_56_2` | Apo B | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_2667 association rows across 1083 traits (2576 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Low density lipoprotein cholesterol levels | 9e-971 | rs934197 | 94 | GCST90239655 | no MR -> candidate analysis |
| Total cholesterol levels | 5e-796 | rs934197 | 116 | GCST90239673 | no MR -> candidate analysis |
| Non-HDL cholesterol levels | 2e-670 | rs934197 | 7 | GCST90239667 | no MR -> candidate analysis |
| Phospholipids to Total Lipids in IDL percentage | 2e-622 | rs676210 | 2 | GCST90501130 | no MR -> candidate analysis |
| Triglycerides in small VLDL | 3e-506 | rs676210 | 3 | GCST90501268 | no MR -> candidate analysis |
| Cholesteryl Esters to Total Lipids in IDL percentage | 6e-477 | rs676210 | 2 | GCST90501124 | no MR -> candidate analysis |
| Free Cholesterol to Total Lipids in Large LDL percentage | 3e-442 | rs676210 | 2 | GCST90501151 | no MR -> candidate analysis |
| Cholesterol to Total Lipids in IDL percentage | 1e-420 | rs676210 | 2 | GCST90501122 | no MR -> candidate analysis |
| Cysteine-rich protein 1 levels | 1e-418 | rs679899 | 1 | GCST90247157 | no MR -> candidate analysis |
| Concentration of small VLDL particles | 2e-401 | rs676210 | 4 | GCST90501265 | no MR -> candidate analysis |
| Triglyceride levels | 4e-398 | rs676210 | 47 | GCST90239661 | no MR -> candidate analysis |
| Triglyceride to phosphoglyceride ratio | 2e-389 | rs676210 | 2 | GCST90501273 | no MR -> candidate analysis |
| _...and 1071 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1224 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| hypercholesterolemia, autosomal dominant, type B | 0.909 | — | established (curated) | no MR -> candidate analysis |
| Hypercholesterolemia | 0.916 | 0.955 | established (curated) | MR: beta=-0.19, p=1.84e-54 (cis) |
| familial hypobetalipoproteinemia 1 | 0.91 | — | established (curated) | no MR -> candidate analysis |
| familial hypercholesterolemia | 0.85 | 0.783 | established (curated) | no MR -> candidate analysis |
| metabolic disease | 0.942 | 0.926 | multi-layer: burden+GWAS (allelic-series candidate) | no MR -> candidate analysis |
| hypobetalipoproteinemia | 0.919 | — | established (curated) | no MR -> candidate analysis |
| coronary artery disorder | 0.906 | — | common-variant locus | no MR -> candidate analysis |
| Disorder of lipid metabolism | 0.838 | 0.84 | multi-layer: burden+GWAS (allelic-series candidate) | no MR -> candidate analysis |
| cardiovascular disorder | 0.867 | — | common-variant locus | no MR -> candidate analysis |
| hyperlipidemia | 0.938 | — | common-variant locus | no MR -> candidate analysis |
| hypercholesterolemia, familial, 1 | 0.931 | — | established (curated) | no MR -> candidate analysis |
| metabolic syndrome | 0.884 | — | common-variant locus | no MR -> candidate analysis |
| familial hyperlipidemia | 0.886 | — | common-variant locus | no MR -> candidate analysis |
| homozygous familial hypercholesterolemia | 0.72 | — | established (curated) | no MR -> candidate analysis |
| Abnormality of the cardiovascular system | 0.909 | — | established (curated) | no MR -> candidate analysis |

> Of the 15 rows above, **14 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 2 exploratory rare-variant signal(s), 2 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Apolipoprotein B-100) |
| gnomAD constraint | pLI=1.8e-14, LOEUF=0.557 — LoF-tolerant |
| GWAS Catalog | 187 unique SNPs / 539 rows |
| ClinVar | 5193 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 5 clinical annotations across 3 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1224 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'APOB' and resolved to 'Apolipoprotein B-100' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 5193 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 20 of 1083 traits by best p-value, aggregated from 2667 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P04114 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000084674/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4549/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/APOB — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/APOB — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=APOB%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=APOB — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/APOB — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:07:48  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
