# Protein Dossier — HPSE (Heparanase)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Melanoma | -0.415 | 0.126 | 9.75e-04 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | -0.0166 | 0.00535 | 0.00197 | Wald ratio | 1 | cis | NA |
| Weight | -0.0138 | 0.00472 | 0.00358 | Wald ratio | 1 | cis | NA |
| Platelet count | 2.41 | 0.876 | 0.00584 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: S66 Injury of muscle and tendon at wrist and hand level | 0.275 | 0.103 | 0.00749 | Wald ratio | 1 | cis | NA |
| Femoral neck bone mineral density | 0.0415 | 0.0165 | 0.0118 | Wald ratio | 1 | cis | NA |
| LDL cholesterol | -0.0257 | 0.0115 | 0.025 | Wald ratio | 1 | cis | NA |
| Paget's disease | 0.29 | 0.134 | 0.0306 | Wald ratio | 1 | cis | NA |
| Mean platelet volume | -0.00499 | 0.0024 | 0.0378 | Wald ratio | 1 | cis | NA |
| Cardioembolic stroke | -0.141 | 0.0691 | 0.0408 | Wald ratio | 1 | cis | NA |
| Mean cell volume | 0.113 | 0.0553 | 0.0417 | Wald ratio | 1 | cis | NA |
| Parkinson's disease | 0.185 | 0.0918 | 0.0438 | Wald ratio | 1 | cis | NA |
| _...and 80 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_15 association rows across 12 traits (11 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Serum levels of protein HPSE | 2e-133 | rs6535455 | 1 | GCST90089086 | no MR -> candidate analysis |
| HPSE protein levels | 2e-112 | rs61751211 | 3 | GCST90469473 | no MR -> candidate analysis |
| Blood protein levels | 8e-78 | rs11732810 | 2 | GCST006585 | no MR -> candidate analysis |
| Protrudin levels | 7e-41 | rs61751211 | 1 | GCST90249121 | no MR -> candidate analysis |
| Heparanase levels | 3e-37 | rs61751211 | 1 | GCST90247930 | no MR -> candidate analysis |
| Beta-defensin 121 levels | 1e-32 | rs61751211 | 1 | GCST90246676 | no MR -> candidate analysis |
| Serum levels of protein GCH1 | 2e-21 | rs4693078 | 1 | GCST90086595 | no MR -> candidate analysis |
| Free Cholesterol to Cholesteryl Esters in Large HDL ratio | 7e-10 | rs79764311 | 1 | GCST90827800 | no MR -> candidate analysis |
| Color vision defects (Deutan-Protan) | 2e-6 | rs188825767 | 1 | GCST90301670 | no MR -> candidate analysis |
| Crohn's disease (Tractor method with European ancestry) | 3e-6 | rs200013026 | 1 | GCST90825978 | no MR -> candidate analysis |
| COVID-19 (covid vs negative) | 4e-6 | rs72942343 | 1 | GCST90104729 | no MR -> candidate analysis |
| Number of clonal hematopoiesis mutations | 7e-6 | rs6535458 | 1 | GCST90100218 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 644 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| vitiligo | 0.468 | — | common-variant locus | no MR -> candidate analysis |
| lymphangioma | 0.416 | — | common-variant locus | no MR -> candidate analysis |
| hemangioma | 0.416 | — | common-variant locus | no MR -> candidate analysis |
| Hypercholesterolemia | 0.356 | — | common-variant locus | MR: beta=-0.0257, p=0.025 (cis) |
| systemic lupus erythematosus | 0.185 | — | common-variant locus | MR: beta=-0.109, p=0.279 (cis) |

> Of the 5 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 1 known modulators (Heparanase) |
| gnomAD constraint | pLI=1.8e-12, LOEUF=0.937 — LoF-tolerant |
| GWAS Catalog | 32 unique SNPs / 64 rows |
| ClinVar | 151 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 644 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'HPSE' and resolved to 'Heparanase' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 151 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 12 of 12 traits by best p-value, aggregated from 15 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9Y251 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000173083/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3921/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/HPSE — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/HPSE — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=HPSE%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/HPSE — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:02:11  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
