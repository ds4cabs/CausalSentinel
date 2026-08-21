# Protein Dossier — SFTPB (Pulmonary surfactant-associated protein B)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Lung adenocarcinoma | -0.164 | 0.0363 | 6.02e-06 | Wald ratio | 1 | cis | NA |
| Lung cancer | -0.0785 | 0.0251 | 0.0018 | Wald ratio | 1 | cis | NA |
| Rheumatoid arthritis | 0.0902 | 0.0317 | 0.0044 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: retinal detachment | 0.148 | 0.0528 | 0.00519 | Wald ratio | 1 | cis | NA |
| Type 2 diabetes | 0.0431 | 0.0181 | 0.0176 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Diabetes related eye disease | 0.0935 | 0.0409 | 0.0221 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | 0.085 | 0.0384 | 0.0268 | Wald ratio | 1 | cis | NA |
| Paget's disease | 0.236 | 0.109 | 0.0301 | Wald ratio | 1 | cis | NA |
| Invasive mucinous ovarian cancer | 0.121 | 0.0592 | 0.0418 | Wald ratio | 1 | cis | NA |
| Body fat | -0.0182 | 0.00918 | 0.0472 | Wald ratio | 1 | cis | NA |
| Pulse rate | 0.0115 | 0.00619 | 0.063 | Wald ratio | 1 | cis | NA |
| Amygdala volume | -6.67 | 3.62 | 0.0653 | Wald ratio | 1 | cis | NA |
| _...and 85 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_20 association rows across 11 traits (19 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating GNLY levels | 1e-837 | rs1030862 | 2 | GCST90860460 | no MR -> candidate analysis |
| Pulmonary surfactant-associated protein B levels | 2e-387 | rs1130866 | 1 | GCST90249163 | no MR -> candidate analysis |
| Blood protein levels | 3e-189 | rs1130866 | 1 | GCST006585 | no MR -> candidate analysis |
| GNLY protein levels | 7e-103 | rs143271190 | 7 | GCST90469372 | no MR -> candidate analysis |
| SFTPB protein levels | 1e-25 | rs1130866 | 1 | GCST90453140 | no MR -> candidate analysis |
| Granulysin levels | 1e-24 | rs59494763 | 3 | GCST90161663 | no MR -> candidate analysis |
| LAMP3 protein levels | 2e-15 | rs1130866 | 1 | GCST90469735 | no MR -> candidate analysis |
| PAEP protein levels | 1e-12 | rs1130866 | 1 | GCST90470144 | no MR -> candidate analysis |
| Gamma glutamyl transferase levels | 2e-9 | rs3024832 | 1 | GCST90019507 | no MR -> candidate analysis |
| Lung adenocarcinoma | 2e-8 | rs1130866 | 1 | GCST90297563 | MR: beta=-0.164, p=6.02e-06 (cis) |
| Core binding factor acute myeloid leukemia | 8e-6 | rs2232739; rs2232750; rs2304564; rs6547629; rs17736515; rs17508809; rs3821020; rs13414982; rs7316; rs3024811; rs2118177 | 1 | GCST008413 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 408 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Neonatal acute respiratory distress with surfactant metabolism deficiency | 0.82 | — | established (curated) | no MR -> candidate analysis |
| surfactant metabolism dysfunction, pulmonary, 1 | 0.839 | — | established (curated) | no MR -> candidate analysis |
| Congenital pulmonary alveolar proteinosis | 0.608 | — | established (curated) | no MR -> candidate analysis |
| hereditary pulmonary alveolar proteinosis | 0.858 | — | established (curated) | no MR -> candidate analysis |
| Moderate albuminuria | 0.279 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.261 | — | common-variant locus | no MR -> candidate analysis |

> Of the 6 rows above, **6 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=5.2e-07, LOEUF=0.843 — LoF-tolerant |
| GWAS Catalog | 108 unique SNPs / 228 rows |
| ClinVar | 273 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 408 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'SFTPB'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 273 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 11 of 11 traits by best p-value, aggregated from 20 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P07988 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000168878/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/SFTPB — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/SFTPB — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=SFTPB%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/SFTPB — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:04:02  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
