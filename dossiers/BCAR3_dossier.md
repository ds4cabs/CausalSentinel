# Protein Dossier — BCAR3 (Breast cancer anti-estrogen resistance protein 3)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Myocardial infarction | -0.122 | 0.035 | 4.76e-04 | Wald ratio | 1 | trans | NA |
| Coronary heart disease | -0.106 | 0.0318 | 8.64e-04 | Wald ratio | 1 | trans | NA |
| Amyotrophic lateral sclerosis | -0.187 | 0.0575 | 0.00113 | Wald ratio | 1 | trans | NA |
| Eczema | 0.169 | 0.0562 | 0.00266 | Wald ratio | 1 | trans | NA |
| Years of schooling | -0.0375 | 0.0125 | 0.0027 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: N92 Excessive  frequent and irregular menstruation | 0.135 | 0.046 | 0.0034 | Wald ratio | 1 | trans | NA |
| Chronic kidney disease | 0.137 | 0.05 | 0.00596 | Wald ratio | 1 | trans | NA |
| Forced vital capacity (FVC) | -0.0168 | 0.00618 | 0.00649 | Wald ratio | 1 | trans | NA |
| LDL cholesterol | -0.0472 | 0.0175 | 0.00701 | Wald ratio | 1 | trans | NA |
| Sodium in urine | 0.0187 | 0.00741 | 0.0115 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: deep venous thrombosis (dvt) | -0.156 | 0.0627 | 0.0128 | Wald ratio | 1 | trans | NA |
| Heel bone mineral density (BMD) T-score  automated | 0.0239 | 0.00975 | 0.0143 | Wald ratio | 1 | trans | NA |
| _...and 100 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-5262_57_3` | BCAR3 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_57 association rows across 46 traits (47 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Estimated glomerular filtration rate (creatinine) | 1e-19 | rs7514579 | 3 | GCST90103633 | no MR -> candidate analysis |
| Educational attainment | 2e-18 | rs23766 | 1 | GCST90105038 | no MR -> candidate analysis |
| Hip index | 5e-18 | rs11579685 | 5 | GCST90020026 | no MR -> candidate analysis |
| Telomere length (principal component 1) | 6e-16 | rs11165011 | 1 | GCST90435144 | no MR -> candidate analysis |
| Creatinine levels | 6e-16 | rs236335 | 1 | GCST90662902 | no MR -> candidate analysis |
| Estimated glomerular filtration rate (creatinine, cystatin c | 1e-15 | rs236321 | 1 | GCST90428446 | no MR -> candidate analysis |
| Estimated glomerular filtration rate based on creatinine and | 1e-14 | rs236335 | 1 | GCST90566737 | no MR -> candidate analysis |
| heart rate (HR, mean, inv-normal transformed) | 9e-14 | rs236321 | 1 | GCST90480666 | no MR -> candidate analysis |
| white blood cell count (WBC, minimum, inv-norm transformed) | 2e-13 | rs236336 | 1 | GCST90476456 | no MR -> candidate analysis |
| Aphasia (PheCode 292.11) | 4e-13 | rs564948849 | 1 | GCST90480740 | no MR -> candidate analysis |
| Creatinine levels (UKB data field 30700) | 5e-13 | rs7514579 | 1 | GCST90468067 | no MR -> candidate analysis |
| White blood cell count | 6e-13 | rs7555302 | 2 | GCST90002374 | no MR -> candidate analysis |
| _...and 34 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1168 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| hair color | 0.656 | — | common-variant locus | no MR -> candidate analysis |
| brain cancer | 0.603 | — | common-variant locus | no MR -> candidate analysis |
| open-angle glaucoma | 0.55 | — | common-variant locus | no MR -> candidate analysis |
| nervous system cancer | 0.482 | — | common-variant locus | no MR -> candidate analysis |
| alopecia areata | 0.453 | — | common-variant locus | no MR -> candidate analysis |
| schizophrenia | 0.443 | — | common-variant locus | no MR -> candidate analysis |
| intelligence | 0.443 | — | common-variant locus | no MR -> candidate analysis |
| Tinnitus | 0.237 | — | common-variant locus | no MR -> candidate analysis |

> Of the 8 rows above, **8 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.0022, LOEUF=0.608 — LoF-tolerant |
| GWAS Catalog | 52 unique SNPs / 104 rows |
| ClinVar | 175 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1168 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'BCAR3'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 175 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 46 traits by best p-value, aggregated from 57 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O75815 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000137936/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/BCAR3 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/BCAR3 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=BCAR3%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/BCAR3 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:16:24  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
