# Protein Dossier — JAML (Junctional adhesion molecule-like)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Weight | -0.00683 | 0.00216 | 0.00156 | Wald ratio | 1 | cis | NA |
| Height | -0.00783 | 0.00291 | 0.00715 | Wald ratio | 1 | cis | NA |
| Creatinine (enzymatic) in urine | -0.00617 | 0.00234 | 0.00843 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: D12 Benign neoplasm of colon  rectum  anus and anal canal | 0.0516 | 0.0196 | 0.0085 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | -0.0054 | 0.00212 | 0.0107 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: deep venous thrombosis (dvt) | -0.044 | 0.0181 | 0.0152 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | -0.00477 | 0.00201 | 0.0174 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hyperthyroidism or thyrotoxicosis | 0.0603 | 0.0268 | 0.0243 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | 0.0231 | 0.0106 | 0.0294 | Wald ratio | 1 | cis | NA |
| Sodium in urine | -0.0049 | 0.00241 | 0.0418 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | -0.00496 | 0.00244 | 0.0426 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: emphysema or chronic bronchitis | 0.0409 | 0.0203 | 0.0442 | Wald ratio | 1 | cis | NA |
| _...and 57 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-5094_62_3` | JAML1 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_49 association rows across 26 traits (48 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Junctional adhesion molecule-like (analyte X8232.90) levels | 1e-828 | rs1805 | 1 | GCST90427279 | no MR -> candidate analysis |
| Junctional adhesion molecule-like levels (AMICA1.8232.90.3) | 6e-667 | rs17121881 | 1 | GCST90241666 | no MR -> candidate analysis |
| Blood protein levels | 2e-338 | rs4938490 | 1 | GCST006585 | no MR -> candidate analysis |
| SCN4B protein levels | 9e-69 | rs117705089 | 3 | GCST90470551 | no MR -> candidate analysis |
| White blood cell count | 2e-49 | rs143034248 | 8 | GCST90002374 | no MR -> candidate analysis |
| Neutrophil count | 5e-43 | rs143034248 | 7 | GCST90002351 | no MR -> candidate analysis |
| white blood cell count (WBC, mean, inv-norm transformed) | 3e-39 | rs143034248 | 2 | GCST90476454 | no MR -> candidate analysis |
| white blood cell count (WBC, minimum, inv-norm transformed) | 4e-35 | rs143034248 | 2 | GCST90476457 | no MR -> candidate analysis |
| Protein Wnt-10a protein levels (SomaScan ID:8232-90) | 8e-35 | rs17121881 | 1 | GCST90437240 | no MR -> candidate analysis |
| Neutrophill count (UKB data field 30140) | 6e-32 | rs143034248 | 2 | GCST90468092 | no MR -> candidate analysis |
| neutrophil (absolute count, mean, inv-norm transformed) | 5e-26 | rs143034248 | 2 | GCST90475529 | no MR -> candidate analysis |
| neutrophil (absolute count, minimum, inv-norm transformed) | 4e-25 | rs143034248 | 2 | GCST90475532 | no MR -> candidate analysis |
| _...and 14 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 114 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| lung adenocarcinoma | 0.364 | — | common-variant locus | no MR -> candidate analysis |
| intracranial hemorrhage | 0.33 | — | common-variant locus | no MR -> candidate analysis |
| placenta praevia | 0.33 | — | common-variant locus | no MR -> candidate analysis |
| lung carcinoma | 0.271 | — | common-variant locus | no MR -> candidate analysis |
| non-small cell lung carcinoma | 0.151 | — | common-variant locus | no MR -> candidate analysis |
| lung cancer | 0.11 | — | established (curated) | no MR -> candidate analysis |

> Of the 6 rows above, **6 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=8e-06, LOEUF=0.889 — LoF-tolerant |
| GWAS Catalog | 68 unique SNPs / 136 rows |
| ClinVar | 49 records; 10 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 114 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'JAML'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 49 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 26 traits by best p-value, aggregated from 49 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q86YT9 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000160593/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/JAML — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/JAML — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=JAML%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/JAML — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:20:34  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
