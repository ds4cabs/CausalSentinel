# Protein Dossier — TAPBPL (Tapasin-related protein)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Forced vital capacity (FVC) | -0.00613 | 0.00174 | 4.24e-04 | Wald ratio | 1 | cis | NA |
| Knee osteoarthritis | -0.075 | 0.0244 | 0.00213 | Wald ratio | 1 | cis | NA |
| Height | -0.00708 | 0.00254 | 0.00542 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | -0.00497 | 0.00183 | 0.00667 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: C50 Malignant neoplasm of breast | -0.0442 | 0.0173 | 0.0107 | Wald ratio | 1 | cis | NA |
| Amyotrophic lateral sclerosis | -0.0392 | 0.0154 | 0.011 | Wald ratio | 1 | cis | NA |
| Microalbuminuria | -0.0421 | 0.0175 | 0.016 | Wald ratio | 1 | cis | NA |
| Urinary albumin-to-creatinine ratio | -0.0119 | 0.00509 | 0.0191 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Arm | -0.0526 | 0.0225 | 0.0194 | Wald ratio | 1 | cis | NA |
| Fractured or broken bones in last 5 years | -0.0149 | 0.00671 | 0.0268 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: chronic obstructive airways disease or copd | 0.0746 | 0.0337 | 0.0269 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K60 Fissure and fistula of anal and rectal regions | -0.0728 | 0.0338 | 0.0309 | Wald ratio | 1 | cis | NA |
| _...and 90 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_13 association rows across 11 traits (12 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Tapasin-related protein levels | 2e-5081 | rs2532497 | 2 | GCST90249957 | no MR -> candidate analysis |
| Tapasin-related protein levels (TAPBPL.6364.7.3) | 4e-1297 | rs2532497 | 2 | GCST90242972 | no MR -> candidate analysis |
| Blood protein levels | 3e-362 | rs12964 | 1 | GCST006585 | no MR -> candidate analysis |
| Tapasin-related protein level in Chronic kidney disease with | 1e-109 | rs2041387 | 1 | GCST90238226 | no MR -> candidate analysis |
| Matrilin-3 protein levels (SomaScan ID:6364-7) | 7e-63 | rs2534711 | 1 | GCST90438806 | no MR -> candidate analysis |
| Circulating CD27 levels (id: OID00703_OID21527) | 7e-47 | rs7132503 | 1 | GCST90860046 | no MR -> candidate analysis |
| Circulating CD27 levels (id: OID00800_OID21527) | 2e-31 | rs7132503 | 1 | GCST90860131 | no MR -> candidate analysis |
| CD27 protein levels | 4e-29 | rs7132503 | 1 | GCST90468615 | no MR -> candidate analysis |
| Serum levels of protein TAPBPL | 4e-25 | rs3782729 | 1 | GCST90089368 | no MR -> candidate analysis |
| Height (baseline) | 1e-9 | rs12964 | 1 | GCST90565843 | no MR -> candidate analysis |
| Height | 7e-8 | rs12964 | 1 | GCST007841 | MR: beta=-0.00708, p=0.00542 (cis) |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 55 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| marfanoid habitus and intellectual disability | 0.195 | — | established (curated) | no MR -> candidate analysis |
| vertebral column disorder | 0.041 | — | common-variant locus | no MR -> candidate analysis |
| poisoning | 0.041 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=2.3e-08, LOEUF=0.959 — LoF-tolerant |
| GWAS Catalog | 98 unique SNPs / 196 rows |
| ClinVar | 278 records; 7 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 55 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'TAPBPL'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 278 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 11 of 11 traits by best p-value, aggregated from 13 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9BX59 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000139192/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/TAPBPL — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/TAPBPL — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=TAPBPL%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/TAPBPL — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:17:42  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
