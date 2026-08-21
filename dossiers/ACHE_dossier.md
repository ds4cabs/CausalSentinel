# Protein Dossier — ACHE (Acetylcholinesterase)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Pulse rate | 0.0856 | 0.0143 | 2.12e-09 | Wald ratio | 1 | cis | NA |
| Diastolic blood pressure  automated reading | 0.0438 | 0.00829 | 1.31e-07 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | -0.0416 | 0.0105 | 7.24e-05 | Wald ratio | 1 | cis | NA |
| Height | 0.037 | 0.00976 | 1.49e-04 | Wald ratio | 1 | cis | NA |
| Total cholesterol | 0.0579 | 0.0172 | 7.45e-04 | Wald ratio | 1 | cis | NA |
| Cough on most days | -0.159 | 0.0487 | 0.00106 | Wald ratio | 1 | cis | NA |
| Transferrin | 0.1 | 0.034 | 0.00317 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | 0.0196 | 0.00665 | 0.00327 | Wald ratio | 1 | cis | NA |
| Ulcerative colitis | 0.119 | 0.0418 | 0.00426 | Wald ratio | 1 | cis | NA |
| ER-negative Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | 0.108 | 0.038 | 0.00463 | Wald ratio | 1 | cis | NA |
| Transferrin Saturation | -0.0923 | 0.0333 | 0.00565 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | -0.109 | 0.0402 | 0.00662 | Wald ratio | 1 | cis | NA |
| _...and 115 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_41 association rows across 22 traits (39 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| ACHE protein levels | 2e-174 | rs145798043 | 1 | GCST90468199 | no MR -> candidate analysis |
| Pulse rate (UKB data field 102) | 1e-96 | rs13226864 | 1 | GCST90468177 | no MR -> candidate analysis |
| Resting heart rate | 1e-41 | rs17881696 | 2 | GCST003818 | no MR -> candidate analysis |
| Heart rate | 8e-27 | rs13245899 | 1 | GCST001969 | no MR -> candidate analysis |
| Heart rate response to recovery post exercise (10 sec) | 6e-21 | rs17883557 | 1 | GCST005846 | no MR -> candidate analysis |
| Heart rate increase in response to exercise | 3e-16 | rs76181418 | 1 | GCST005845 | no MR -> candidate analysis |
| Red blood cell count | 5e-16 | rs538605220 | 1 | GCST007069 | no MR -> candidate analysis |
| Body mass index | 1e-15 | rs1799805 | 2 | GCST90255621 | MR: beta=-0.0142, p=0.0793 (cis) |
| Red blood cell erythrocyte count (UKB data field 30010) | 1e-13 | rs538605220 | 1 | GCST90468098 | no MR -> candidate analysis |
| PILRB protein levels | 6e-13 | rs117954600 | 1 | GCST90470237 | no MR -> candidate analysis |
| Heel bone mineral density | 3e-12 | rs3847063 | 1 | GCST006979 | MR: beta=-0.0416, p=7.24e-05 (cis) |
| Free Cholesterol to Total Lipids in Medium HDL percentage | 1e-11 | rs76181418 | 1 | GCST90501187 | no MR -> candidate analysis |
| _...and 10 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 2712 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Abnormality of the skeletal system | 0.785 | — | common-variant locus | no MR -> candidate analysis |
| skin cancer | 0.572 | — | common-variant locus | no MR -> candidate analysis |
| hair color | 0.488 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 20 known modulators (Acetylcholinesterase) |
| gnomAD constraint | pLI=0.95, LOEUF=0.518 — LoF-INTOLERANT |
| GWAS Catalog | 102 unique SNPs / 228 rows |
| ClinVar | 100 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 1 clinical annotations across 1 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 2712 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'ACHE' and resolved to 'Acetylcholinesterase' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 100 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 20 of 22 traits by best p-value, aggregated from 41 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P22303 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000087085/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL220/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/ACHE — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/ACHE — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=ACHE%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=ACHE — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/ACHE — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T00:51:12  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
