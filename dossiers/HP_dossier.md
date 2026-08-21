# Protein Dossier — HP (Haptoglobin)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Total cholesterol | -0.0658 | 0.00541 | 4.48e-34 | Wald ratio | 1 | cis | 1 |
| LDL cholesterol | -0.0628 | 0.00564 | 7.76e-29 | Wald ratio | 1 | cis | 1 |
| Non-cancer illness code  self-reported: high cholesterol | -0.0737 | 0.0102 | 5.13e-13 | Wald ratio | 1 | cis | 0.997 |
| Height | 0.0276 | 0.00437 | 2.69e-10 | Wald ratio | 1 | cis | 0.999 |
| Transferrin | -0.0493 | 0.0146 | 7.51e-04 | Wald ratio | 1 | cis | NA |
| Triglycerides | -0.017 | 0.00506 | 7.69e-04 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | 0.00959 | 0.00287 | 8.55e-04 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | 0.00957 | 0.00303 | 0.0016 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K80 Cholelithiasis | -0.0759 | 0.0263 | 0.00393 | Wald ratio | 1 | cis | NA |
| HDL cholesterol | -0.0146 | 0.00518 | 0.00477 | Wald ratio | 1 | cis | NA |
| Alzheimer's disease | 0.0589 | 0.0236 | 0.0125 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N81 Female genital prolapse | 0.0676 | 0.0274 | 0.0136 | Wald ratio | 1 | cis | NA |
| _...and 109 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3054_3_2` | Haptoglobin, Mixed Type | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_302 association rows across 211 traits (296 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Inhibin beta B chain (mixed) levels | 1e-688 | rs77303550 | 1 | GCST90266939 | no MR -> candidate analysis |
| Haptoglobin levels | 1e-582 | rs77303550 | 4 | GCST90247931 | no MR -> candidate analysis |
| Circulating GALNT2 levels | 3e-372 | rs12924886 | 2 | GCST90860544 | no MR -> candidate analysis |
| Glycoprotein acetyls levels | 3e-358 | rs77303550 | 3 | GCST90454488 | no MR -> candidate analysis |
| SERPIND1 protein levels | 2e-306 | rs77303550 | 1 | GCST90470595 | no MR -> candidate analysis |
| Total cholesterol levels | 1e-293 | rs77303550 | 13 | GCST90239673 | no MR -> candidate analysis |
| Low density lipoprotein cholesterol levels | 2e-248 | rs77303550 | 6 | GCST90239655 | no MR -> candidate analysis |
| Low-density lipoprotein levels | 1e-217 | rs77303550 | 2 | GCST90662892 | no MR -> candidate analysis |
| Blood protein levels | 8e-184 | rs77303550 | 8 | GCST006585 | no MR -> candidate analysis |
| Glycoprotein acetyls levels (UKB data field 23480) | 8e-178 | rs77303550 | 1 | GCST90269577 | no MR -> candidate analysis |
| HPT protein level (protein group normalized intensity) | 3e-168 | rs8062041 | 1 | GCST90570716 | no MR -> candidate analysis |
| Serum levels of protein HP | 6e-159 | rs12924886 | 2 | GCST90088210 | no MR -> candidate analysis |
| _...and 199 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1575 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Hypercholesterolemia | 0.936 | — | common-variant locus | MR: beta=-0.0658, p=4.48e-34 (cis) |
| metabolic disease | 0.896 | — | common-variant locus | no MR -> candidate analysis |
| hyperlipidemia | 0.896 | — | common-variant locus | no MR -> candidate analysis |
| coronary artery disorder | 0.853 | — | common-variant locus | no MR -> candidate analysis |
| metabolic syndrome | 0.798 | — | common-variant locus | no MR -> candidate analysis |
| anhaptoglobinemia | 0.567 | — | established (curated) | no MR -> candidate analysis |
| familial hyperlipidemia | 0.797 | — | common-variant locus | no MR -> candidate analysis |
| response to statin | 0.729 | — | common-variant locus | no MR -> candidate analysis |
| angina pectoris | 0.668 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.656 | — | common-variant locus | no MR -> candidate analysis |
| cardiovascular disorder | 0.585 | — | common-variant locus | no MR -> candidate analysis |
| coronary artery calcification | 0.584 | — | common-variant locus | no MR -> candidate analysis |
| familial hypercholesterolemia | 0.584 | — | common-variant locus | no MR -> candidate analysis |
| Disorder of lipid metabolism | 0.583 | — | common-variant locus | no MR -> candidate analysis |
| physical activity | 0.578 | — | common-variant locus | no MR -> candidate analysis |

> Of the 15 rows above, **14 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.47, LOEUF=0.677 — LoF-tolerant |
| GWAS Catalog | 162 unique SNPs / 420 rows |
| ClinVar | 130 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1575 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 130 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 211 traits by best p-value, aggregated from 302 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P00738 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000257017/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/HP — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/HP — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=HP%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/HP — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:01:36  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: chembl
