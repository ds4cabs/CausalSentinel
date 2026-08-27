# Protein Dossier — CCL17 (C-C motif chemokine 17)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Rheumatoid arthritis | 0.102 | 0.0386 | 0.00851 | Inverse variance weighted | 2 | trans | NA |
| Rheumatoid arthritis | 0.102 | 0.0386 | 0.00851 | Inverse variance weighted | 2 | trans | NA |
| Anorexia nervosa | 0.218 | 0.0845 | 0.00983 | Inverse variance weighted | 2 | trans | NA |
| Anorexia nervosa | 0.218 | 0.0845 | 0.00983 | Inverse variance weighted | 2 | trans | NA |
| Non-cancer illness code  self-reported: gastro-oesophageal reflux (gord)  or  gastric reflux | 0.00299 | 0.00119 | 0.0117 | Inverse variance weighted | 2 | trans | NA |
| Non-cancer illness code  self-reported: gastro-oesophageal reflux (gord)  or  gastric reflux | 0.00299 | 0.00119 | 0.0117 | Inverse variance weighted | 2 | trans | NA |
| Systemic lupus erythematosus | 0.272 | 0.114 | 0.0172 | Inverse variance weighted | 2 | trans | NA |
| Systemic lupus erythematosus | 0.272 | 0.114 | 0.0172 | Inverse variance weighted | 2 | trans | NA |
| Ischemic stroke | -0.081 | 0.0373 | 0.03 | Inverse variance weighted | 2 | trans | NA |
| Ischemic stroke | -0.081 | 0.0373 | 0.03 | Inverse variance weighted | 2 | trans | NA |
| Red blood cell count | -0.0116 | 0.00576 | 0.0444 | Inverse variance weighted | 2 | trans | NA |
| Red blood cell count | -0.0116 | 0.00576 | 0.0444 | Inverse variance weighted | 2 | trans | NA |
| _...and 183 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3519_3_2` | TARC | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_27 association rows across 17 traits (26 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating CCL17 levels (id: OID00439_OID20745) | 2e-450 | rs9302690 | 2 | GCST90859799 | no MR -> candidate analysis |
| CCL17 protein levels | 2e-279 | rs9302690 | 2 | GCST90468569 | no MR -> candidate analysis |
| Circulating CCL17 levels (id: OID00821_OID20745) | 8e-261 | rs9302690 | 2 | GCST90860150 | no MR -> candidate analysis |
| CCL17/CCL22 protein level ratio | 3e-133 | rs801506 | 1 | GCST90313682 | no MR -> candidate analysis |
| C-C motif chemokine 17 levels | 1e-78 | rs16956811 | 6 | GCST90246905 | no MR -> candidate analysis |
| Serum levels of protein CCL17 | 9e-49 | rs4396523 | 2 | GCST90088432 | no MR -> candidate analysis |
| Blood protein levels | 6e-30 | rs16956811 | 1 | GCST006585 | no MR -> candidate analysis |
| Thymus and reactivation regulated chemokine levels | 3e-29 | rs223896 | 1 | GCST011913 | no MR -> candidate analysis |
| Fractalkine levels | 3e-27 | rs62037103 | 1 | GCST90247635 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 7e-26 | rs60679405 | 1 | GCST90838669 | no MR -> candidate analysis |
| C-C motif chemokine 17 levels (CCL17.3519.3.2) | 2e-21 | rs113022368 | 1 | GCST90240486 | no MR -> candidate analysis |
| Cerebrospinal fluid protein CCL17 levels | 2e-20 | rs223896 | 1 | GCST90944147 | no MR -> candidate analysis |
| _...and 5 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 531 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| cardiomyopathy | 0.36 | — | common-variant locus | MR: beta=0.000116, p=0.173 (trans) |
| systemic lupus erythematosus | 0.216 | — | common-variant locus | MR: beta=0.272, p=0.0172 (trans) |

> Of the 2 rows above, **0 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (C-C motif chemokine 17) |
| gnomAD constraint | pLI=0.00075, LOEUF=1.96 — LoF-tolerant |
| GWAS Catalog | 67 unique SNPs / 134 rows |
| ClinVar | 49 records; 11 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 531 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'CCL17' and resolved to 'C-C motif chemokine 17' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 49 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 17 of 17 traits by best p-value, aggregated from 27 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q92583 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000102970/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4295915/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CCL17 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CCL17 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CCL17%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CCL17 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:31:54  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
