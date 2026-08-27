# Protein Dossier — MCAM (Cell surface glycoprotein MUC18)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Serum creatinine (eGFRcrea) | -0.0292 | 0.00694 | 2.67e-05 | Wald ratio | 1 | cis | NA |
| Platelet count | -12.4 | 3.41 | 2.87e-04 | Wald ratio | 1 | cis | NA |
| Height | -0.0764 | 0.0236 | 0.00122 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: asthma | 0.146 | 0.0463 | 0.0016 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: psoriasis | 0.378 | 0.125 | 0.00258 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertension | 0.0882 | 0.0298 | 0.00307 | Wald ratio | 1 | cis | NA |
| Chronic kidney disease | 0.312 | 0.118 | 0.00812 | Wald ratio | 1 | cis | NA |
| Coronary heart disease | -0.203 | 0.077 | 0.00857 | Wald ratio | 1 | cis | NA |
| Transferrin | -0.213 | 0.0819 | 0.00928 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: gastro-oesophageal reflux (gord)  or  gastric reflux | 0.185 | 0.0769 | 0.016 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: anxiety or panic attacks | 0.287 | 0.126 | 0.0227 | Wald ratio | 1 | cis | NA |
| Years of schooling | -0.0625 | 0.0278 | 0.0244 | Wald ratio | 1 | cis | NA |
| _...and 92 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_15 association rows across 14 traits (15 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| ITGB1/MCAM protein level ratio | 2e-165 | rs34587557 | 1 | GCST90315226 | no MR -> candidate analysis |
| CD58/MCAM protein level ratio | 1e-145 | rs34587557 | 1 | GCST90313852 | no MR -> candidate analysis |
| MCAM/NTRK3 protein level ratio | 4e-143 | rs34587557 | 1 | GCST90315409 | no MR -> candidate analysis |
| MCAM/NCAM1 protein level ratio | 6e-124 | rs34587557 | 1 | GCST90315408 | no MR -> candidate analysis |
| MCAM protein levels | 5e-123 | rs34587557 | 1 | GCST90469870 | no MR -> candidate analysis |
| Plateletcrit | 1e-27 | rs35929108 | 1 | GCST90002400 | no MR -> candidate analysis |
| Height | 1e-27 | rs2511847 | 1 | GCST90245848 | MR: beta=-0.0764, p=0.00122 (cis) |
| Platelet count | 1e-19 | rs7944487 | 2 | GCST90056183 | MR: beta=-12.4, p=2.87e-04 (cis) |
| Platelet-to-lymphocyte ratio | 2e-18 | rs2511842 | 1 | GCST90056184 | no MR -> candidate analysis |
| Blood protein levels | 6e-18 | rs2511847 | 1 | GCST006585 | no MR -> candidate analysis |
| Platelet crit (UKB data field 30090) | 5e-13 | rs182494271 | 1 | GCST90468096 | no MR -> candidate analysis |
| High density lipoprotein cholesterol levels | 1e-10 | rs71484135 | 1 | GCST90019510 | no MR -> candidate analysis |
| _...and 2 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 542 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| CBL-related disorder | 0.195 | — | established (curated) | no MR -> candidate analysis |
| spinal fracture | 0.136 | — | common-variant locus | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 1 known modulators (Cell surface glycoprotein MUC18) |
| gnomAD constraint | pLI=3.6e-13, LOEUF=0.87 — LoF-tolerant |
| GWAS Catalog | 83 unique SNPs / 164 rows |
| ClinVar | 165 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 542 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'MCAM' and resolved to 'Cell surface glycoprotein MUC18' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 165 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 14 of 14 traits by best p-value, aggregated from 15 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P43121 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000076706/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3712863/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/MCAM — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/MCAM — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=MCAM%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/MCAM — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:45:32  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
