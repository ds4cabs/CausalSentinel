# Protein Dossier — CLPS (Colipase)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: joint disorder | 0.204 | 0.0676 | 0.0025 | Wald ratio | 1 | cis | NA |
| Clear cell ovarian cancer | 0.261 | 0.0926 | 0.00492 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: arthritis (nos) | 0.138 | 0.0568 | 0.0152 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: vitiligo | 0.516 | 0.216 | 0.0166 | Wald ratio | 1 | cis | NA |
| Potassium in urine | -0.0135 | 0.00573 | 0.0185 | Wald ratio | 1 | cis | NA |
| Creatinine (enzymatic) in urine | -0.0115 | 0.00541 | 0.0341 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | 0.121 | 0.0598 | 0.0422 | Wald ratio | 1 | cis | NA |
| Rheumatoid arthritis | -0.0681 | 0.0353 | 0.0536 | Wald ratio | 1 | cis | NA |
| Femoral neck bone mineral density | 0.0331 | 0.0173 | 0.0557 | Wald ratio | 1 | cis | NA |
| Weight | -0.00941 | 0.00499 | 0.0593 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Glaucoma | -0.0966 | 0.0521 | 0.0634 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K80 Cholelithiasis | 0.0655 | 0.0369 | 0.0755 | Wald ratio | 1 | cis | NA |
| _...and 57 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_12 association rows across 9 traits (11 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| CLPS protein levels | 9e-296 | rs116063149 | 2 | GCST90468786 | no MR -> candidate analysis |
| Serum levels of protein CLPS | 1e-141 | rs2766598 | 2 | GCST90089194 | no MR -> candidate analysis |
| Colipase levels | 9e-129 | rs9470101 | 2 | GCST90247108 | no MR -> candidate analysis |
| Colipase levels (CLPS.5749.53.3) | 5e-43 | rs2766594 | 1 | GCST90240742 | no MR -> candidate analysis |
| Height (baseline) | 1e-18 | rs6906260 | 1 | GCST90565843 | no MR -> candidate analysis |
| SEMA3G protein levels | 6e-12 | rs148028295 | 1 | GCST90470571 | no MR -> candidate analysis |
| Physical function (baseline) | 1e-10 | rs6906260 | 1 | GCST90565837 | no MR -> candidate analysis |
| Phospholipid levels in large HDL | 4e-8 | rs3748048 | 1 | GCST90092852 | no MR -> candidate analysis |
| Spondylolisthesis | 3e-7 | rs140407801 | 1 | GCST90104232 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 413 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| celiac disease | 0.219 | — | common-variant locus | no MR -> candidate analysis |
| dermatitis herpetiformis | 0.156 | — | common-variant locus | no MR -> candidate analysis |
| hypothyroidism | 0.13 | — | common-variant locus | MR: beta=0.0191, p=0.438 (cis) |
| myxedema | 0.13 | — | common-variant locus | no MR -> candidate analysis |

> Of the 4 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (E3 ubiquitin-protein ligase UBR1) |
| gnomAD constraint | pLI=0.0022, LOEUF=1.56 — LoF-tolerant |
| GWAS Catalog | 95 unique SNPs / 190 rows |
| ClinVar | 26 records; 7 pathogenic in sample of 26 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 413 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'CLPS' and resolved to 'E3 ubiquitin-protein ligase UBR1' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 26 record(s) retrieved, NOT over all 26 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 9 of 9 traits by best p-value, aggregated from 12 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P04118 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000137392/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL6066245/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CLPS — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CLPS — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CLPS%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CLPS — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:54:27  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
