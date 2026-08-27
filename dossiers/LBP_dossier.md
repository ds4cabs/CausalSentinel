# Protein Dossier — LBP (Lipopolysaccharide-binding protein)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Ovarian cancer | -0.0489 | 0.0275 | 0.0752 | Wald ratio | 1 | cis | NA |
| Thalamus volume | -22.7 | 13.5 | 0.0924 | Wald ratio | 1 | cis | NA |
| Endometrioid ovarian cancer | -0.0918 | 0.0586 | 0.117 | Wald ratio | 1 | cis | NA |
| Invasive mucinous ovarian cancer | -0.124 | 0.0792 | 0.117 | Wald ratio | 1 | cis | NA |
| Nucleus accumbens volume | -3.66 | 2.36 | 0.121 | Wald ratio | 1 | cis | NA |
| Hippocampus volume | 14 | 10 | 0.162 | Wald ratio | 1 | cis | NA |
| Amyotrophic lateral sclerosis | 0.0475 | 0.0359 | 0.186 | Wald ratio | 1 | cis | NA |
| Forearm bone mineral density | 0.0328 | 0.0293 | 0.263 | Wald ratio | 1 | cis | NA |
| High grade serous ovarian cancer | -0.0367 | 0.0329 | 0.264 | Wald ratio | 1 | cis | NA |
| Schizophrenia | 0.024 | 0.0216 | 0.267 | Wald ratio | 1 | cis | NA |
| Lung cancer | 0.0395 | 0.038 | 0.298 | Wald ratio | 1 | cis | NA |
| Eczema | 0.0375 | 0.0407 | 0.356 | Wald ratio | 1 | cis | NA |
| _...and 4 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_110 association rows across 67 traits (105 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| CSF1/LBP protein level ratio | 1e-2496 | rs2232613 | 1 | GCST90314286 | no MR -> candidate analysis |
| Lipopolysaccharide-binding protein levels | 4e-624 | rs2232613 | 11 | GCST90248250 | no MR -> candidate analysis |
| Colipase-like protein 1 levels | 8e-562 | rs2232613 | 2 | GCST90247109 | no MR -> candidate analysis |
| Serum levels of protein AKT2 | 1e-306 | rs2232613 | 2 | GCST90089022 | no MR -> candidate analysis |
| Serum levels of protein LBP | 9e-303 | rs2232613 | 1 | GCST90088224 | no MR -> candidate analysis |
| LBP protein levels | 5e-298 | rs11481047 | 12 | GCST90469743 | no MR -> candidate analysis |
| Serum levels of protein LYPD3 | 2e-264 | rs2232613 | 1 | GCST90090620 | no MR -> candidate analysis |
| Blood protein levels | 1e-186 | rs73112473 | 14 | GCST006585 | no MR -> candidate analysis |
| RING finger protein 24 levels | 3e-184 | rs2232613 | 2 | GCST90249349 | no MR -> candidate analysis |
| Serum levels of protein BPI | 4e-180 | rs1780617 | 2 | GCST90088584 | no MR -> candidate analysis |
| Serum levels of protein IL15 | 8e-163 | rs2232613 | 1 | GCST90086450 | no MR -> candidate analysis |
| Bactericidal permeability-increasing protein levels | 2e-112 | rs1018470 | 3 | GCST90246731 | no MR -> candidate analysis |
| _...and 55 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 633 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| macular degeneration | 0.517 | — | common-variant locus | no MR -> candidate analysis |
| temporomandibular joint disorder | 0.439 | — | common-variant locus | no MR -> candidate analysis |
| thrombophilia | 0.436 | — | common-variant locus | no MR -> candidate analysis |
| preeclampsia | 0.276 | — | common-variant locus | no MR -> candidate analysis |
| ovarian neoplasm | 0.114 | — | common-variant locus | no MR -> candidate analysis |

> Of the 5 rows above, **5 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Small ribosomal subunit protein uS2) |
| gnomAD constraint | pLI=2e-17, LOEUF=1.18 — LoF-tolerant |
| GWAS Catalog | 80 unique SNPs / 160 rows |
| ClinVar | 111 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 633 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'LBP' and resolved to 'Small ribosomal subunit protein uS2' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 111 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 67 traits by best p-value, aggregated from 110 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P18428 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000129988/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL6119/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/LBP — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/LBP — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=LBP%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/LBP — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:28:03  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
