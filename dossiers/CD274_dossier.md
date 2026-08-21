# Protein Dossier — CD274 (Programmed cell death 1 ligand 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | 0.144 | 0.0342 | 2.47e-05 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K43 Ventral hernia | 0.259 | 0.104 | 0.013 | Wald ratio | 1 | cis | NA |
| Intracranial volume | 1.59e+04 | 6.92e+03 | 0.022 | Wald ratio | 1 | cis | NA |
| 2hr glucose | 0.155 | 0.0677 | 0.0223 | Wald ratio | 1 | cis | NA |
| Cardioembolic stroke | -0.256 | 0.113 | 0.0235 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I84 Haemorrhoids | 0.115 | 0.0511 | 0.0245 | Wald ratio | 1 | cis | NA |
| Primary sclerosing cholangitis  | -0.236 | 0.11 | 0.0312 | Wald ratio | 1 | cis | NA |
| High grade serous ovarian cancer | 0.123 | 0.0575 | 0.032 | Wald ratio | 1 | cis | NA |
| Hearing difficulty or problems: Yes | 0.0316 | 0.0149 | 0.0334 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: depression | -0.0844 | 0.0399 | 0.0345 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: bladder problem (not cancer) | 0.203 | 0.0962 | 0.0352 | Wald ratio | 1 | cis | NA |
| Neuroticism | 0.0258 | 0.0129 | 0.0455 | Wald ratio | 1 | cis | NA |
| _...and 90 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-5060_62_3` | B7-H1 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_60 association rows across 22 traits (55 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating CD274 levels (id: OID00799_OID20966) | 4e-501 | rs7041009 | 8 | GCST90860130 | no MR -> candidate analysis |
| CD274/EFNA4 protein level ratio | 4e-500 | rs822340 | 1 | GCST90313768 | no MR -> candidate analysis |
| Circulating CD274 levels (id: OID00518_OID20966) | 8e-470 | rs7041009 | 8 | GCST90859874 | no MR -> candidate analysis |
| PDCD1LG2 protein levels | 9e-237 | rs76778936 | 12 | GCST90470180 | no MR -> candidate analysis |
| CD274 protein levels | 3e-135 | rs7875928 | 7 | GCST90468613 | no MR -> candidate analysis |
| Programmed cell death 1 ligand 1 levels | 2e-100 | rs7048841 | 7 | GCST90426218 | no MR -> candidate analysis |
| Cerebrospinal fluid protein CD274 levels | 2e-67 | rs7048841 | 1 | GCST90943153 | no MR -> candidate analysis |
| Serum levels of protein CD274 | 1e-56 | rs1411262 | 1 | GCST90088892 | no MR -> candidate analysis |
| Blood protein levels | 2e-29 | rs1411262 | 1 | GCST006585 | no MR -> candidate analysis |
| Circulating PDCD1LG2 levels (id: OID00831_OID21273) | 2e-25 | rs117829177 | 1 | GCST90860159 | no MR -> candidate analysis |
| Circulating PDCD1LG2 levels (id: OID00458_OID21273) | 3e-24 | rs117829177 | 1 | GCST90859819 | no MR -> candidate analysis |
| Serum levels of protein PDCD1LG2 | 1e-21 | rs10975153 | 1 | GCST90088180 | no MR -> candidate analysis |
| _...and 10 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1982 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| neoplasm | 0.195 | — | established (curated) | MR: beta=0.0949, p=0.167 (cis) |
| hypothyroidism | 0.659 | — | common-variant locus | MR: beta=0.144, p=2.47e-05 (cis) |

> Of the 2 rows above, **0 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 13 known modulators (Programmed cell death 1 ligand 1) |
| gnomAD constraint | pLI=0.99, LOEUF=0.48 — LoF-INTOLERANT |
| GWAS Catalog | 96 unique SNPs / 192 rows |
| ClinVar | 196 records; 14 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1982 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'CD274' and resolved to 'Programmed cell death 1 ligand 1' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 196 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 22 traits by best p-value, aggregated from 60 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9NZQ7 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000120217/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3580522/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CD274 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CD274 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CD274%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CD274 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:41:22  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
