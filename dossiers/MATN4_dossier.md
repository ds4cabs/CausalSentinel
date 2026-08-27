# Protein Dossier — MATN4 (Matrilin-4)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Mean cell haemoglobin | -0.181 | 0.057 | 0.00154 | Wald ratio | 1 | cis | NA |
| ER-negative Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | 0.168 | 0.0574 | 0.00345 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: S76 Injury of muscle and tendon at hip and thigh level | 0.772 | 0.292 | 0.00829 | Wald ratio | 1 | cis | NA |
| Sodium in urine | -0.0303 | 0.0119 | 0.0107 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | 0.0387 | 0.0156 | 0.0129 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Cataract | -0.2 | 0.0814 | 0.0142 | Wald ratio | 1 | cis | NA |
| Schizophrenia | 0.127 | 0.0535 | 0.0172 | Wald ratio | 1 | cis | NA |
| Amygdala volume | 27.4 | 11.6 | 0.0179 | Wald ratio | 1 | cis | NA |
| Eczema | 0.191 | 0.084 | 0.0228 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: psoriasis | 0.209 | 0.0929 | 0.0242 | Wald ratio | 1 | cis | NA |
| Depressive symptoms | -0.0392 | 0.0174 | 0.0244 | Wald ratio | 1 | cis | NA |
| Mean platelet volume | -0.0135 | 0.00609 | 0.0268 | Wald ratio | 1 | cis | NA |
| _...and 104 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_13 association rows across 9 traits (11 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| WFDC12 protein levels | 1e-61 | rs77289229 | 4 | GCST90471073 | no MR -> candidate analysis |
| Matrilin-4 levels | 4e-53 | rs11086958 | 1 | GCST90248424 | no MR -> candidate analysis |
| Serum levels of protein MATN4 | 2e-38 | rs2076023 | 1 | GCST90089650 | no MR -> candidate analysis |
| Blood protein levels | 2e-23 | rs11086957 | 2 | GCST006585 | no MR -> candidate analysis |
| Height | 2e-19 | rs2227275 | 1 | GCST90245848 | MR: beta=-0.0348, p=0.0353 (cis) |
| Matrilin-4 levels (MATN4.7083.74.3) | 3e-16 | rs11697677 | 1 | GCST90241887 | no MR -> candidate analysis |
| SDC4 protein levels | 5e-14 | rs117801728 | 1 | GCST90470559 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 2e-9 | rs56365005 | 1 | GCST90838669 | no MR -> candidate analysis |
| Parental longevity (mother's age at death) | 6e-6 | rs371025208 | 1 | GCST003393 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 53 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| holoprosencephaly | 0.474 | — | established (curated) | no MR -> candidate analysis |
| Global developmental delay | 0.426 | — | established (curated) | no MR -> candidate analysis |
| Meningomyelocele | 0.426 | — | established (curated) | no MR -> candidate analysis |
| Proptosis | 0.426 | — | established (curated) | no MR -> candidate analysis |
| Seizure | 0.426 | — | established (curated) | no MR -> candidate analysis |
| diabetes insipidus | 0.426 | — | established (curated) | no MR -> candidate analysis |
| microcephaly | 0.426 | — | established (curated) | no MR -> candidate analysis |
| Oligomenorrhea | 0.152 | 0.152 | exploratory rare-variant signal | no MR -> candidate analysis |

> Of the 8 rows above, **8 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 1 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1.7e-10, LOEUF=0.953 — LoF-tolerant |
| GWAS Catalog | 62 unique SNPs / 123 rows |
| ClinVar | 134 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 53 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'MATN4'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 134 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 9 of 9 traits by best p-value, aggregated from 13 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O95460 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000124159/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/MATN4 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/MATN4 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=MATN4%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/MATN4 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:44:55  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
