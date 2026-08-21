# Protein Dossier — PDCD1LG2 (Programmed cell death 1 ligand 2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: asthma | 0.0417 | 0.0161 | 0.00978 | Inverse variance weighted | 2 | trans | NA |
| Non-cancer illness code  self-reported: asthma | 0.0417 | 0.0161 | 0.00978 | Inverse variance weighted | 2 | cis | NA |
| Mean cell haemoglobin concentration | -0.0232 | 0.00922 | 0.0119 | Inverse variance weighted | 2 | trans | NA |
| Mean cell haemoglobin concentration | -0.0232 | 0.00922 | 0.0119 | Inverse variance weighted | 2 | cis | NA |
| Non-cancer illness code  self-reported: bone disorder | 0.252 | 0.101 | 0.0123 | Inverse variance weighted | 2 | trans | NA |
| Non-cancer illness code  self-reported: bone disorder | 0.252 | 0.101 | 0.0123 | Inverse variance weighted | 2 | cis | NA |
| Age at menarche | 0.0313 | 0.0142 | 0.0275 | Inverse variance weighted | 2 | trans | NA |
| Age at menarche | 0.0313 | 0.0142 | 0.0275 | Inverse variance weighted | 2 | cis | NA |
| Chronic kidney disease | -0.083 | 0.0383 | 0.0301 | Inverse variance weighted | 2 | trans | NA |
| Chronic kidney disease | -0.083 | 0.0383 | 0.0301 | Inverse variance weighted | 2 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | -0.0168 | 0.00777 | 0.0308 | Inverse variance weighted | 2 | trans | NA |
| Heel bone mineral density (BMD) T-score  automated | -0.0168 | 0.00777 | 0.0308 | Inverse variance weighted | 2 | cis | NA |
| _...and 166 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3004_67_2` | PD-L2 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_78 association rows across 27 traits (71 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating PDCD1LG2 levels (id: OID00458_OID21273) | 5e-2776 | rs62556120 | 5 | GCST90859819 | no MR -> candidate analysis |
| Circulating PDCD1LG2 levels (id: OID00831_OID21273) | 6e-1968 | rs62556120 | 4 | GCST90860159 | no MR -> candidate analysis |
| ICOSLG/PDCD1LG2 protein level ratio | 3e-1870 | rs62556118 | 1 | GCST90315125 | no MR -> candidate analysis |
| Programmed cell death 1 ligand 2 levels | 3e-258 | rs16923189 | 16 | GCST90248874 | no MR -> candidate analysis |
| PDCD1LG2 protein levels | 9e-200 | rs56299437 | 19 | GCST90470180 | no MR -> candidate analysis |
| Circulating CD274 levels (id: OID00518_OID20966) | 5e-140 | rs7875928 | 2 | GCST90859874 | no MR -> candidate analysis |
| CD274 protein levels | 3e-135 | rs7875928 | 5 | GCST90468613 | no MR -> candidate analysis |
| Serum levels of protein PDCD1LG2 | 6e-127 | rs16923189 | 3 | GCST90088180 | no MR -> candidate analysis |
| Circulating CD274 levels (id: OID00799_OID20966) | 5e-125 | rs7875928 | 2 | GCST90860130 | no MR -> candidate analysis |
| Blood protein levels | 3e-70 | rs16923189 | 1 | GCST006585 | no MR -> candidate analysis |
| Programmed cell death 1 ligand 2 levels (PDCD1LG2.3004.67.2) | 8e-51 | rs16923189 | 3 | GCST90242384 | no MR -> candidate analysis |
| Eosinophill percentage (UKB data field 30210) | 1e-19 | rs1333192 | 1 | GCST90468069 | no MR -> candidate analysis |
| _...and 15 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 603 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| myxedema | 0.557 | — | common-variant locus | no MR -> candidate analysis |
| hypothyroidism | 0.557 | — | common-variant locus | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 1 known modulators (Programmed cell death 1 ligand 2) |
| gnomAD constraint | pLI=1.1e-12, LOEUF=1.52 — LoF-tolerant |
| GWAS Catalog | 108 unique SNPs / 217 rows |
| ClinVar | 222 records; 8 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 603 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'PDCD1LG2' and resolved to 'Programmed cell death 1 ligand 2' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 222 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 27 traits by best p-value, aggregated from 78 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9BQ51 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000197646/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3713006/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PDCD1LG2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PDCD1LG2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PDCD1LG2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/PDCD1LG2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:14:09  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
