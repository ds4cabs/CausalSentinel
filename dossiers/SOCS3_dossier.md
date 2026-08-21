# Protein Dossier — SOCS3 (Suppressor of cytokine signaling 3)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Forced vital capacity (FVC) | 0.0156 | 0.00328 | 1.85e-06 | Wald ratio | 1 | trans | NA |
| Forced expiratory volume in 1-second (FEV1) | 0.013 | 0.00346 | 1.71e-04 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: high cholesterol | 0.0322 | 0.0105 | 0.00211 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: hypertension | 0.0181 | 0.00669 | 0.0067 | Wald ratio | 1 | trans | NA |
| Neuroblastoma | 0.186 | 0.0712 | 0.00879 | Wald ratio | 1 | trans | NA |
| Neo-extraversion | -0.349 | 0.134 | 0.00894 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: migraine | -0.0635 | 0.0246 | 0.00991 | Wald ratio | 1 | trans | NA |
| Age at menarche | -0.024 | 0.00932 | 0.01 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | 0.0416 | 0.017 | 0.0147 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: arthritis (nos) | -0.123 | 0.0522 | 0.0183 | Wald ratio | 1 | trans | NA |
| Schizophrenia | -0.0401 | 0.0171 | 0.0187 | Wald ratio | 1 | trans | NA |
| Fractured bone site(s): Ankle | 0.0737 | 0.0317 | 0.02 | Wald ratio | 1 | trans | NA |
| _...and 92 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_57 association rows across 36 traits (50 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| C-reactive protein levels (UKB data field 30710) | 4e-38 | rs11658216 | 3 | GCST90468064 | no MR -> candidate analysis |
| C-reactive protein levels | 3e-36 | rs6501207 | 6 | GCST009777 | no MR -> candidate analysis |
| C-reactive protein | 1e-30 | rs12952093 | 1 | GCST90018950 | no MR -> candidate analysis |
| C-reactive protein levels (MTAG) | 2e-27 | rs6501207 | 6 | GCST90179146 | no MR -> candidate analysis |
| Height | 1e-26 | rs7213427 | 3 | GCST90245848 | MR: beta=0.00709, p=0.14 (trans) |
| Platelet count | 7e-19 | rs9892622 | 3 | GCST90662907 | no MR -> candidate analysis |
| Aspartate aminotransferase (AST, mean, inv-norm transformed) | 5e-18 | rs4969172 | 2 | GCST90475121 | no MR -> candidate analysis |
| Heel bone mineral density | 1e-17 | rs7225449 | 1 | GCST007066 | MR: beta=-0.00632, p=0.222 (trans) |
| Aspartate aminotransferase (AST, minimum, inv-norm transform | 5e-17 | rs6501201 | 2 | GCST90475124 | no MR -> candidate analysis |
| Glycated haemoglobin HbA1c levels (UKB data field 30750) | 7e-17 | rs9892622 | 1 | GCST90468072 | no MR -> candidate analysis |
| Creatine kinase levels | 1e-16 | rs6501201 | 2 | GCST90838680 | no MR -> candidate analysis |
| Platelet count (UKB data field 30080) | 1e-14 | rs11077357 | 1 | GCST90468095 | no MR -> candidate analysis |
| _...and 24 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 820 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| asthma | 0.269 | — | common-variant locus | MR: beta=0.00883, p=0.426 (trans) |
| respiratory system disorder | 0.215 | — | common-variant locus | no MR -> candidate analysis |
| osteoarthritis | 0.186 | — | common-variant locus | MR: beta=-0.0471, p=0.285 (trans) |
| open-angle glaucoma | 0.19 | — | common-variant locus | no MR -> candidate analysis |

> Of the 4 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.27, LOEUF=0.901 — LoF-tolerant |
| GWAS Catalog | 115 unique SNPs / 276 rows |
| ClinVar | 52 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 820 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'SOCS3'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 52 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 36 traits by best p-value, aggregated from 57 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O14543 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000184557/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/SOCS3 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/SOCS3 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=SOCS3%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/SOCS3 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:10:31  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
