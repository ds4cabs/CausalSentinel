# Protein Dossier — RRM1 (Ribonucleoside-diphosphate reductase large subunit)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Mean cell haemoglobin | 0.166 | 0.0231 | 6.88e-13 | Wald ratio | 1 | trans | NA |
| Mean cell volume | 0.381 | 0.059 | 1.05e-10 | Wald ratio | 1 | trans | NA |
| Fasting glucose | -0.0231 | 0.00714 | 0.00122 | Wald ratio | 1 | trans | NA |
| Systemic lupus erythematosus | -0.348 | 0.109 | 0.00135 | Wald ratio | 1 | trans | NA |
| Haemoglobin concentration | 0.038 | 0.0132 | 0.00407 | Wald ratio | 1 | trans | NA |
| Body mass index (BMI) | -0.0159 | 0.00566 | 0.00499 | Wald ratio | 1 | trans | NA |
| Weight | -0.014 | 0.005 | 0.00513 | Wald ratio | 1 | trans | NA |
| Depressive symptoms | -0.0231 | 0.0084 | 0.00596 | Wald ratio | 1 | trans | NA |
| Red blood cell count | -0.0136 | 0.00504 | 0.00676 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: anxiety or panic attacks | -0.152 | 0.057 | 0.00775 | Wald ratio | 1 | trans | NA |
| Mean cell haemoglobin concentration | 0.0206 | 0.00819 | 0.012 | Wald ratio | 1 | trans | NA |
| Cancer code  self-reported: prostate cancer | 0.133 | 0.0582 | 0.0219 | Wald ratio | 1 | trans | NA |
| _...and 96 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_37 association rows across 20 traits (33 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Mean corpuscular volume | 9e-65 | rs67074167 | 6 | GCST90002338 | no MR -> candidate analysis |
| Mean corpuscular hemoglobin | 2e-51 | rs725518 | 7 | GCST90002326 | no MR -> candidate analysis |
| Mean corpuscular volume (UKB data field 30040) | 1e-43 | rs11030967 | 1 | GCST90468086 | no MR -> candidate analysis |
| Mean corpuscular haemoglobin (UKB data field 30050) | 8e-39 | rs11030967 | 1 | GCST90468084 | no MR -> candidate analysis |
| Mean reticulocyte volume | 2e-27 | rs725518 | 1 | GCST90002396 | no MR -> candidate analysis |
| Mean reticulocyte volume (UKB data field 30260) | 1e-24 | rs11030976 | 1 | GCST90468088 | no MR -> candidate analysis |
| Mean spheric corpuscular volume | 2e-24 | rs725518 | 2 | GCST90002397 | no MR -> candidate analysis |
| Red cell distribution width | 3e-23 | rs232054 | 5 | GCST90002369 | no MR -> candidate analysis |
| Mitochondrial DNA copy number (adjusted) | 1e-19 | rs12806698 | 1 | GCST90268497 | no MR -> candidate analysis |
| Mean sphered cell volume (UKB data field 30270) | 6e-19 | rs11030976 | 1 | GCST90468089 | no MR -> candidate analysis |
| Mitochondrial DNA copy number (raw) | 4e-17 | rs12806698 | 1 | GCST90268498 | no MR -> candidate analysis |
| mean platelet volume (MPV, minimum, inv-norm transformed) | 8e-15 | rs10835611 | 1 | GCST90479709 | no MR -> candidate analysis |
| _...and 8 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 458 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| progressive external ophthalmoplegia with mitochondrial dna deletions, autosomal recessive 6 | 0.657 | — | established (curated) | no MR -> candidate analysis |

> Of the 1 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Ribonucleoside-diphosphate reductase large subunit) |
| gnomAD constraint | pLI=1, LOEUF=0.275 — LoF-INTOLERANT |
| GWAS Catalog | 42 unique SNPs / 84 rows |
| ClinVar | 110 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 13 clinical annotations across 5 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 458 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'RRM1' and resolved to 'Ribonucleoside-diphosphate reductase large subunit' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 110 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 20 of 20 traits by best p-value, aggregated from 37 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P23921 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000167325/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL1830/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/RRM1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/RRM1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=RRM1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=RRM1 — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/RRM1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:53:24  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
