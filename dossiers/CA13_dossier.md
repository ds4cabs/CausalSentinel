# Protein Dossier — CA13 (Carbonic anhydrase 13)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Sleep duration | -0.0146 | 0.00501 | 0.00355 | Wald ratio | 1 | cis | NA |
| Hearing difficulty or problems: Yes | -0.0282 | 0.0114 | 0.0132 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Other bones | 0.0646 | 0.0262 | 0.0136 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: mania or bipolar disorder or manic depression | 0.236 | 0.101 | 0.0188 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: small intestine or small bowel cancer | 0.441 | 0.205 | 0.0312 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I84 Haemorrhoids | -0.0965 | 0.0455 | 0.034 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: enlarged prostate | -0.132 | 0.0629 | 0.0354 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: osteoarthritis | -0.0463 | 0.0225 | 0.0398 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K35 Acute appendicitis | 0.156 | 0.0795 | 0.0501 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M23 Internal derangement of knee | 0.0774 | 0.04 | 0.0529 | Wald ratio | 1 | cis | NA |
| Fracture resulting from simple fall | -0.0314 | 0.0176 | 0.0748 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R04 Haemorrhage from respiratory passages | -0.192 | 0.11 | 0.0804 | Wald ratio | 1 | cis | NA |
| _...and 65 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3420_21_2` | Carbonic anhydrase XIII | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_25 association rows across 21 traits (24 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| CA13/PPIB protein level ratio | 4e-2106 | rs7827175 | 1 | GCST90313563 | no MR -> candidate analysis |
| CA13/HARS1 protein level ratio | 2e-1610 | rs7827175 | 1 | GCST90313560 | no MR -> candidate analysis |
| ANXA4/CA13 protein level ratio | 3e-1299 | rs7827175 | 1 | GCST90313290 | no MR -> candidate analysis |
| CA13/LACTB2 protein level ratio | 3e-1242 | rs7827175 | 1 | GCST90313562 | no MR -> candidate analysis |
| CA13/TYMP protein level ratio | 7e-870 | rs7827175 | 1 | GCST90313568 | no MR -> candidate analysis |
| CA13/STAMBP protein level ratio | 4e-797 | rs7827175 | 1 | GCST90313566 | no MR -> candidate analysis |
| CA13/COMT protein level ratio | 1e-795 | rs7827175 | 1 | GCST90313557 | no MR -> candidate analysis |
| CA13/VTA1 protein level ratio | 5e-688 | rs7827175 | 1 | GCST90313570 | no MR -> candidate analysis |
| Circulating CA13 levels | 5e-637 | rs56072918 | 2 | GCST90860354 | no MR -> candidate analysis |
| CA13/QDPR protein level ratio | 2e-539 | rs7827175 | 1 | GCST90313564 | no MR -> candidate analysis |
| ABHD14B/CA13 protein level ratio | 3e-508 | rs7827175 | 1 | GCST90313138 | no MR -> candidate analysis |
| CA13/DPP7 protein level ratio | 2e-367 | rs7827175 | 1 | GCST90313558 | no MR -> candidate analysis |
| _...and 9 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 49 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Genu valgum | 0.376 | — | common-variant locus | no MR -> candidate analysis |
| Genu varum | 0.376 | — | common-variant locus | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Carbonic anhydrase 13) |
| gnomAD constraint | pLI=2.2e-05, LOEUF=0.959 — LoF-tolerant |
| GWAS Catalog | 40 unique SNPs / 80 rows |
| ClinVar | 88 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 49 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'CA13' and resolved to 'Carbonic anhydrase 13' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 88 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 21 traits by best p-value, aggregated from 25 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q8N1Q1 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000185015/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3912/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CA13 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CA13 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CA13%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CA13 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:24:47  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
