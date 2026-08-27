# Protein Dossier — HSD17B14 (L-fucose dehydrogenase)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: S76 Injury of muscle and tendon at hip and thigh level | 1.15 | 0.287 | 5.96e-05 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: gastro-oesophageal reflux (gord)  or  gastric reflux | 0.202 | 0.0686 | 0.00322 | Wald ratio | 1 | cis | NA |
| Sodium in urine | 0.0502 | 0.0171 | 0.00323 | Wald ratio | 1 | cis | NA |
| Forearm bone mineral density | 0.278 | 0.108 | 0.01 | Wald ratio | 1 | cis | NA |
| Cough on most days | -0.286 | 0.12 | 0.0176 | Wald ratio | 1 | cis | NA |
| Lumbar spine bone mineral density | 0.137 | 0.0622 | 0.0279 | Wald ratio | 1 | cis | NA |
| Femoral neck bone mineral density | 0.114 | 0.0538 | 0.0342 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hayfever or allergic rhinitis | 0.129 | 0.0629 | 0.04 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: asthma | 0.0879 | 0.0446 | 0.0486 | Wald ratio | 1 | cis | NA |
| Alcohol intake frequency | 0.0496 | 0.0256 | 0.0528 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K20 Oesophagitis | 0.265 | 0.137 | 0.0532 | Wald ratio | 1 | cis | NA |
| Caudate volume | -82.3 | 43.4 | 0.0579 | Wald ratio | 1 | cis | NA |
| _...and 67 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_41 association rows across 32 traits (39 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| MUC2 protein levels | 6e-106 | rs116922356 | 1 | GCST90469965 | no MR -> candidate analysis |
| HSD17B14 protein levels | 2e-102 | rs141119542 | 5 | GCST90469483 | no MR -> candidate analysis |
| ALPI protein levels | 9e-92 | rs116922356 | 1 | GCST90468285 | no MR -> candidate analysis |
| PRSS27 protein levels | 2e-80 | rs116922356 | 1 | GCST90470342 | no MR -> candidate analysis |
| Isoleucine levels | 5e-80 | rs10685064 | 4 | GCST90501133 | no MR -> candidate analysis |
| FAM3D protein levels | 3e-58 | rs473464 | 1 | GCST90469188 | no MR -> candidate analysis |
| KLK1 protein levels | 7e-48 | rs140351309 | 1 | GCST90469702 | no MR -> candidate analysis |
| CDH17 protein levels | 2e-47 | rs4459651 | 1 | GCST90468669 | no MR -> candidate analysis |
| Metabolite levels (fucose) | 3e-45 | rs35299026 | 2 | GCST90300006 | no MR -> candidate analysis |
| BPIFA2 protein levels | 4e-39 | rs632115 | 1 | GCST90468461 | no MR -> candidate analysis |
| Metabolite levels (ribose) | 1e-30 | rs35299026 | 1 | GCST90300217 | no MR -> candidate analysis |
| SERPINI2 protein levels | 3e-26 | rs632115 | 1 | GCST90470603 | no MR -> candidate analysis |
| _...and 20 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 135 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| myopia | 0.182 | — | established (curated) | no MR -> candidate analysis |
| pathological myopia | 0.182 | — | established (curated) | no MR -> candidate analysis |
| head and neck cancer | 0.125 | — | common-variant locus | no MR -> candidate analysis |
| placental abruption | 0.086 | — | common-variant locus | no MR -> candidate analysis |
| cholelithiasis | 0.085 | — | common-variant locus | MR: beta=-0.183, p=0.218 (cis) |

> Of the 5 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (17-beta-hydroxysteroid dehydrogenase 14) |
| gnomAD constraint | pLI=1.8e-11, LOEUF=1.33 — LoF-tolerant |
| GWAS Catalog | 183 unique SNPs / 472 rows |
| ClinVar | 67 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 135 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'HSD17B14' and resolved to '17-beta-hydroxysteroid dehydrogenase 14' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 67 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 32 traits by best p-value, aggregated from 41 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9BPX1 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000087076/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3712868/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/HSD17B14 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/HSD17B14 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=HSD17B14%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/HSD17B14 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:03:01  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
