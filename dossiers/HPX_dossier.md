# Protein Dossier — HPX (Hemopexin)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Cardioembolic stroke | -0.14 | 0.0524 | 0.00774 | Inverse variance weighted | 2 | cis | NA |
| Cardioembolic stroke | -0.14 | 0.0524 | 0.00774 | Inverse variance weighted | 2 | trans | NA |
| Systolic blood pressure  automated reading | 0.00943 | 0.00366 | 0.00995 | Inverse variance weighted | 2 | cis | NA |
| Systolic blood pressure  automated reading | 0.00943 | 0.00366 | 0.00995 | Inverse variance weighted | 2 | trans | NA |
| Diastolic blood pressure  automated reading | 0.00936 | 0.00366 | 0.0105 | Inverse variance weighted | 2 | cis | NA |
| Diastolic blood pressure  automated reading | 0.00936 | 0.00366 | 0.0105 | Inverse variance weighted | 2 | trans | NA |
| Weight | 0.0076 | 0.00316 | 0.016 | Inverse variance weighted | 2 | cis | NA |
| Weight | 0.0076 | 0.00316 | 0.016 | Inverse variance weighted | 2 | trans | NA |
| Body mass index (BMI) | 0.0084 | 0.00357 | 0.0186 | Inverse variance weighted | 2 | cis | NA |
| Body mass index (BMI) | 0.0084 | 0.00357 | 0.0186 | Inverse variance weighted | 2 | trans | NA |
| Internalizing problems | -0.0946 | 0.0407 | 0.02 | Wald ratio | 1 | trans | NA |
| Mean cell volume | -0.112 | 0.05 | 0.0247 | Wald ratio | 1 | trans | NA |
| _...and 148 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2768_56_2` | Hemopexin | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_48 association rows across 43 traits (48 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| GTPase KRas levels | 5e-88 | rs76881753 | 1 | GCST90137602 | no MR -> candidate analysis |
| Muellerian-inhibiting factor levels | 7e-64 | rs35862450 | 3 | GCST90248474 | no MR -> candidate analysis |
| Syntaxin-17 level in Chronic kidney disease with hypertensio | 1e-54 | rs12117 | 1 | GCST90235794 | no MR -> candidate analysis |
| Apolipoprotein L1 level in Chronic kidney disease with hyper | 2e-50 | rs12117 | 1 | GCST90239378 | no MR -> candidate analysis |
| Tumor necrosis factor ligand superfamily member 18 level in  | 4e-48 | rs12117 | 1 | GCST90237057 | no MR -> candidate analysis |
| Core-binding factor subunit beta level in Chronic kidney dis | 8e-48 | rs12117 | 1 | GCST90232819 | no MR -> candidate analysis |
| Exportin-5 level in Chronic kidney disease with hypertension | 2e-47 | rs12117 | 1 | GCST90237001 | no MR -> candidate analysis |
| SMPD1/SMPDL3A protein level ratio | 2e-45 | rs35274104 | 1 | GCST90315854 | no MR -> candidate analysis |
| NTF2-related export protein 2 level in Chronic kidney diseas | 4e-44 | rs12117 | 1 | GCST90235181 | no MR -> candidate analysis |
| Tumor necrosis factor level in Chronic kidney disease with h | 1e-39 | rs12117 | 1 | GCST90238125 | no MR -> candidate analysis |
| Homeobox protein SIX6 level in Chronic kidney disease with h | 1e-35 | rs12117 | 1 | GCST90235543 | no MR -> candidate analysis |
| Tumor necrosis factor ligand superfamily member 18 levels | 1e-34 | rs77296242 | 1 | GCST90161439 | no MR -> candidate analysis |
| _...and 31 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 697 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| panniculitis | 0.353 | — | common-variant locus | no MR -> candidate analysis |

> Of the 1 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Hemopexin) |
| gnomAD constraint | pLI=9.1e-12, LOEUF=1.01 — LoF-tolerant |
| GWAS Catalog | 54 unique SNPs / 108 rows |
| ClinVar | 120 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 697 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'HPX' and resolved to 'Hemopexin' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 120 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 43 traits by best p-value, aggregated from 48 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P02790 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000110169/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2176811/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/HPX — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/HPX — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=HPX%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/HPX — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:02:29  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
