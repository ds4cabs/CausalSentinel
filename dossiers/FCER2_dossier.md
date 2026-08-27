# Protein Dossier — FCER2 (Low affinity immunoglobulin epsilon Fc receptor)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Forced vital capacity (FVC) | 0.0195 | 0.00644 | 0.0025 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I84 Haemorrhoids | 0.115 | 0.045 | 0.0105 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Injury or trauma resulting in loss of vision | 0.209 | 0.0838 | 0.0125 | Wald ratio | 1 | cis | NA |
| Amygdala volume | 19 | 7.99 | 0.0177 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: bladder problem (not cancer) | -0.339 | 0.148 | 0.0224 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | 0.0152 | 0.00679 | 0.0253 | Wald ratio | 1 | cis | NA |
| Neo-neuroticism | -0.714 | 0.321 | 0.0262 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: ankylosing spondylitis | 0.251 | 0.117 | 0.0322 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K60 Fissure and fistula of anal and rectal regions | 0.202 | 0.0958 | 0.0347 | Wald ratio | 1 | cis | NA |
| Pallidum volume | 13.2 | 6.57 | 0.0452 | Wald ratio | 1 | cis | NA |
| Neo-extraversion | 0.516 | 0.259 | 0.0459 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I48 Atrial fibrillation and flutter | -0.173 | 0.0891 | 0.0521 | Wald ratio | 1 | cis | NA |
| _...and 85 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3291_30_2` | CD23 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_80 association rows across 45 traits (74 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating CD209 levels | 5e-846 | rs151212242 | 3 | GCST90860672 | no MR -> candidate analysis |
| FCER2/FCRL1 protein level ratio | 1e-634 | rs12973524 | 1 | GCST90314789 | no MR -> candidate analysis |
| CD22/FCER2 protein level ratio | 5e-577 | rs12973524 | 1 | GCST90313756 | no MR -> candidate analysis |
| FCER2/TREML2 protein level ratio | 2e-493 | rs12973524 | 1 | GCST90314792 | no MR -> candidate analysis |
| FCER2/TNFRSF9 protein level ratio | 2e-479 | rs12973524 | 1 | GCST90314791 | no MR -> candidate analysis |
| Circulating FCER2 levels | 3e-418 | rs62110713 | 2 | GCST90860667 | no MR -> candidate analysis |
| Low affinity immunoglobulin epsilon Fc receptor levels | 2e-272 | rs12980031 | 10 | GCST90425675 | no MR -> candidate analysis |
| FCER2 protein levels | 1e-194 | rs12611038 | 7 | GCST90469199 | no MR -> candidate analysis |
| Cerebrospinal fluid protein FCER2 levels | 2e-193 | rs12980031 | 1 | GCST90944762 | no MR -> candidate analysis |
| CD209 antigen levels | 1e-151 | rs4804774 | 5 | GCST90246935 | no MR -> candidate analysis |
| GOLM2/STC1 protein level ratio | 9e-81 | rs12973524 | 1 | GCST90314952 | no MR -> candidate analysis |
| Circulating STC1 levels | 2e-78 | rs12460997 | 2 | GCST90860225 | no MR -> candidate analysis |
| _...and 33 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 473 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Abnormality of the skeletal system | 0.391 | — | common-variant locus | no MR -> candidate analysis |
| diabetes mellitus | 0.267 | — | common-variant locus | no MR -> candidate analysis |
| skin disorder | 0.22 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 1 known modulators (Low affinity immunoglobulin epsilon Fc receptor) |
| gnomAD constraint | pLI=1.6e-10, LOEUF=1 — LoF-tolerant |
| GWAS Catalog | 117 unique SNPs / 274 rows |
| ClinVar | 74 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 473 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'FCER2' and resolved to 'Low affinity immunoglobulin epsilon Fc receptor' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 74 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 45 traits by best p-value, aggregated from 80 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P06734 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000104921/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2940/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/FCER2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/FCER2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=FCER2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/FCER2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:36:51  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
