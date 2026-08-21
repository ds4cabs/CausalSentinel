# Protein Dossier — CNDP1 (Beta-Ala-His dipeptidase)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Gallbladder cancer | 2.82 | 0.874 | 0.00126 | Wald ratio | 1 | cis | NA |
| Birth weight | -0.0263 | 0.0109 | 0.0155 | Wald ratio | 1 | cis | NA |
| Invasive mucinous ovarian cancer | 0.275 | 0.123 | 0.0246 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: muscle or soft tissue injuries | -0.239 | 0.108 | 0.0263 | Wald ratio | 1 | cis | NA |
| Urate | 0.04 | 0.0186 | 0.0313 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: S76 Injury of muscle and tendon at hip and thigh level | 0.464 | 0.225 | 0.0391 | Wald ratio | 1 | cis | NA |
| HOMA-IR | -0.0274 | 0.0134 | 0.0411 | Wald ratio | 1 | cis | NA |
| Pulse rate | 0.0253 | 0.0125 | 0.0435 | Wald ratio | 1 | cis | NA |
| Glioma | -0.26 | 0.129 | 0.0442 | Wald ratio | 1 | cis | NA |
| Lumbar spine bone mineral density | -0.0486 | 0.025 | 0.0519 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K80 Cholelithiasis | 0.0879 | 0.0453 | 0.0523 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K35 Acute appendicitis | -0.25 | 0.134 | 0.0607 | Wald ratio | 1 | cis | NA |
| _...and 91 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3604_6_4` | CNDP1 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_40 association rows across 12 traits (39 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating CNDP1 levels | 4e-467 | rs17817077 | 7 | GCST90860496 | no MR -> candidate analysis |
| CNDP1/EGFR protein level ratio | 2e-275 | rs17238585 | 1 | GCST90314146 | no MR -> candidate analysis |
| CNDP1 protein levels | 1e-211 | rs4329999 | 8 | GCST90468796 | no MR -> candidate analysis |
| Beta-Ala-His dipeptidase levels | 4e-145 | rs17817077 | 10 | GCST90246651 | no MR -> candidate analysis |
| Serum levels of protein CNDP1 | 2e-69 | rs17817077 | 4 | GCST90089039 | no MR -> candidate analysis |
| Beta-Ala-His dipeptidase (analyte X7870.8) levels | 7e-34 | rs58692747 | 1 | GCST90427120 | no MR -> candidate analysis |
| Blood protein levels | 1e-28 | rs62099911 | 2 | GCST006585 | no MR -> candidate analysis |
| Cerebrospinal fluid homocarnosine levels | 1e-19 | rs56042934 | 3 | GCST90318245 | no MR -> candidate analysis |
| Cerebrospinal fluid protein CNDP1 levels | 2e-17 | rs4329999 | 1 | GCST90944972 | no MR -> candidate analysis |
| Beta-Ala-His dipeptidase (analyte X5456.59) levels | 1e-15 | rs58692747 | 1 | GCST90426351 | no MR -> candidate analysis |
| Urine carnosine levels in chronic kidney disease | 1e-12 | rs17089382 | 1 | GCST90264901 | no MR -> candidate analysis |
| Neovascular age-related macular degeneration | 1e-5 | rs9965945 | 1 | GCST90860786 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 167 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| response to antihypertensive drug | 0.421 | — | common-variant locus | no MR -> candidate analysis |
| multiple sclerosis | 0.338 | — | common-variant locus | no MR -> candidate analysis |
| myopia | 0.059 | — | common-variant locus | no MR -> candidate analysis |
| stroke disorder | 0.058 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.058 | — | common-variant locus | no MR -> candidate analysis |
| Retinal hemorrhage | 0.045 | — | common-variant locus | no MR -> candidate analysis |
| duodenal ulcer | 0.035 | — | common-variant locus | no MR -> candidate analysis |

> Of the 7 rows above, **7 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=6.8e-12, LOEUF=0.974 — LoF-tolerant |
| GWAS Catalog | 87 unique SNPs / 174 rows |
| ClinVar | 276 records; 6 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 167 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'CNDP1'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 276 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 12 of 12 traits by best p-value, aggregated from 40 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q96KN2 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000150656/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CNDP1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CNDP1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CNDP1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CNDP1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:54:39  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
