# Protein Dossier — ANGPTL3 (Angiopoietin-related protein 3)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Triglycerides | 0.548 | 0.0287 | 1.28e-81 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: high cholesterol | 0.381 | 0.0273 | 2.78e-44 | Wald ratio | 1 | trans | NA |
| Total cholesterol | 0.294 | 0.0301 | 1.63e-22 | Wald ratio | 1 | trans | NA |
| HDL cholesterol | -0.267 | 0.0296 | 1.88e-19 | Wald ratio | 1 | trans | NA |
| LDL cholesterol | 0.202 | 0.0319 | 2.65e-10 | Wald ratio | 1 | trans | NA |
| Ulcerative colitis | -0.284 | 0.0797 | 3.57e-04 | Wald ratio | 1 | trans | NA |
| Coronary heart disease | 0.209 | 0.0626 | 8.36e-04 | Wald ratio | 1 | trans | NA |
| Sleep duration | -0.0383 | 0.0115 | 9.12e-04 | Wald ratio | 1 | trans | NA |
| ER-positive Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.14 | 0.046 | 0.00237 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: gout | 0.277 | 0.0949 | 0.00352 | Wald ratio | 1 | trans | NA |
| Vascular or heart problems diagnosed by doctor: Angina | 0.195 | 0.0686 | 0.00452 | Wald ratio | 1 | trans | NA |
| Inflammatory bowel disease | -0.175 | 0.0624 | 0.00499 | Wald ratio | 1 | trans | NA |
| _...and 52 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3281_19_1` | ANGL3 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_36 association rows across 19 traits (36 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Cholesterol to Total Lipids in Small HDL percentage | 6e-380 | rs775677524 | 1 | GCST90501235 | no MR -> candidate analysis |
| Free Cholesterol to Total Lipids in IDL percentage | 2e-269 | rs775677524 | 1 | GCST90501126 | no MR -> candidate analysis |
| Phospholipids to Total Lipids in Medium LDL percentage | 2e-133 | rs775677524 | 1 | GCST90501203 | no MR -> candidate analysis |
| ANGPTL3 protein levels | 1e-86 | rs72649573 | 1 | GCST90468304 | no MR -> candidate analysis |
| Circulating ANGPTL3 levels | 1e-84 | rs72649573 | 1 | GCST90860502 | no MR -> candidate analysis |
| Apolipoprotein A levels (UKB data field 30630) | 5e-81 | rs775677524 | 1 | GCST90468061 | no MR -> candidate analysis |
| Triglyceride levels | 1e-63 | rs34483103 | 6 | GCST90239662 | no MR -> candidate analysis |
| Total cholesterol levels | 4e-59 | rs34483103 | 5 | GCST90239674 | no MR -> candidate analysis |
| Apolipoprotein A1 levels | 5e-42 | rs398122988 | 4 | GCST90025955 | no MR -> candidate analysis |
| Phosphatidylinositol(36:2)_[M-H]1- levels | 3e-34 | rs10789117 | 1 | GCST90060912 | no MR -> candidate analysis |
| Angiopoietin-related protein 3 levels | 3e-23 | rs72649573 | 1 | GCST90246508 | no MR -> candidate analysis |
| Low density lipoprotein cholesterol levels | 7e-22 | rs34483103 | 1 | GCST90239656 | no MR -> candidate analysis |
| _...and 7 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 495 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| familial hypobetalipoproteinemia 2 | 0.849 | — | established (curated) | no MR -> candidate analysis |
| Hypercholesterolemia | 0.568 | 0.453 | multi-layer: burden+GWAS (allelic-series candidate) | MR: beta=0.381, p=2.78e-44 (trans) |
| familial hypercholesterolemia | 0.296 | 0.296 | exploratory rare-variant signal | no MR -> candidate analysis |
| cardiovascular disorder | 0.364 | — | common-variant locus | no MR -> candidate analysis |
| metabolic disease | 0.577 | 0.58 | multi-layer: burden+GWAS (allelic-series candidate) | no MR -> candidate analysis |
| hereditary disease | 0.68 | — | established (curated) | no MR -> candidate analysis |
| genetic developmental and epileptic encephalopathy | 0.644 | — | established (curated) | no MR -> candidate analysis |
| hyperlipidemia | 0.527 | — | common-variant locus | no MR -> candidate analysis |
| Disorder of lipid metabolism | 0.413 | 0.431 | multi-layer: burden+GWAS (allelic-series candidate) | no MR -> candidate analysis |
| hypertriglyceridemia | 0.453 | — | common-variant locus | no MR -> candidate analysis |
| metabolic dysfunction-associated steatotic liver disease | 0.431 | — | common-variant locus | no MR -> candidate analysis |
| familial lipoprotein lipase deficiency | 0.458 | — | common-variant locus | no MR -> candidate analysis |
| familial hyperlipidemia | 0.442 | — | common-variant locus | no MR -> candidate analysis |
| small intestine neoplasm | 0.439 | 0.439 | exploratory rare-variant signal | no MR -> candidate analysis |
| coronary artery calcification | 0.431 | — | common-variant locus | no MR -> candidate analysis |

> Of the 15 rows above, **14 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 2 exploratory rare-variant signal(s), 3 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 1 known modulators (Angiopoietin-related protein 3) |
| gnomAD constraint | pLI=2.6e-17, LOEUF=1.22 — LoF-tolerant |
| GWAS Catalog | 217 unique SNPs / 587 rows |
| ClinVar | 190 records; 5 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 495 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'ANGPTL3' and resolved to 'Angiopoietin-related protein 3' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 190 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 19 of 19 traits by best p-value, aggregated from 36 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9Y5C1 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000132855/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3710485/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/ANGPTL3 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/ANGPTL3 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=ANGPTL3%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/ANGPTL3 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:04:06  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
