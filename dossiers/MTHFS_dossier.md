# Protein Dossier — MTHFS (5-formyltetrahydrofolate cyclo-ligase)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: hayfever or allergic rhinitis | -0.174 | 0.0581 | 0.00268 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K35 Acute appendicitis | 0.329 | 0.124 | 0.0083 | Wald ratio | 1 | cis | NA |
| Intracranial volume | 2.44e+04 | 9.25e+03 | 0.00837 | Wald ratio | 1 | cis | NA |
| Pulse rate | -0.0489 | 0.0209 | 0.0191 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: Z09 Follow-up examination after treatment for conditions other than malignant neoplasms | 0.183 | 0.0807 | 0.0238 | Wald ratio | 1 | cis | NA |
| Schizophrenia | -0.116 | 0.0517 | 0.0247 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: L03 Cellulitis | 0.236 | 0.105 | 0.0249 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I83 Varicose veins of lower extremities | 0.15 | 0.0715 | 0.0364 | Wald ratio | 1 | cis | NA |
| Weight | 0.0218 | 0.0104 | 0.0366 | Wald ratio | 1 | cis | NA |
| Clear cell ovarian cancer | 0.409 | 0.202 | 0.0427 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: emphysema or chronic bronchitis | 0.173 | 0.0868 | 0.046 | Wald ratio | 1 | cis | NA |
| Primary sclerosing cholangitis  | -0.283 | 0.146 | 0.0523 | Wald ratio | 1 | cis | NA |
| _...and 110 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_50 association rows across 30 traits (44 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| 5-formyltetrahydrofolate cyclo-ligase levels | 5e-315 | rs4994246 | 5 | GCST90248534 | no MR -> candidate analysis |
| Eosinophil count | 4e-64 | rs7257 | 7 | GCST90002302 | no MR -> candidate analysis |
| Monocyte percentage (UKB data field 30190) | 1e-59 | rs5813998 | 2 | GCST90468091 | no MR -> candidate analysis |
| Serum levels of protein MTHFS | 2e-55 | rs4779164 | 3 | GCST90087789 | no MR -> candidate analysis |
| Monocyte count (UKB data field 30130) | 1e-40 | rs184575290 | 2 | GCST90468090 | no MR -> candidate analysis |
| eosinophil (absolute count, mean, inv-norm transformed) | 1e-40 | rs2115535 | 1 | GCST90479602 | no MR -> candidate analysis |
| eosinophil (fraction, mean, inv-norm transformed) | 2e-37 | rs2115535 | 1 | GCST90479605 | no MR -> candidate analysis |
| Eosinophil percentage of white cells | 4e-37 | rs3826008 | 2 | GCST90002382 | no MR -> candidate analysis |
| Eosinophill percentage (UKB data field 30210) | 3e-36 | rs3826008 | 1 | GCST90468069 | no MR -> candidate analysis |
| 5-formyltetrahydrofolate cyclo-ligase level in Chronic kidne | 1e-35 | rs8030396 | 1 | GCST90234194 | no MR -> candidate analysis |
| Blood protein levels | 6e-35 | rs35144922 | 1 | GCST006585 | no MR -> candidate analysis |
| Eosinophill count (UKB data field 30150) | 5e-33 | rs3826008 | 1 | GCST90468068 | no MR -> candidate analysis |
| _...and 18 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 441 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| neurodevelopmental disorder with microcephaly, epilepsy, and hypomyelination | 0.806 | — | established (curated) | no MR -> candidate analysis |
| inflammatory bowel disease | 0.29 | — | common-variant locus | no MR -> candidate analysis |
| hypertensive disorder | 0.2 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.049, LOEUF=1.03 — LoF-tolerant |
| GWAS Catalog | 71 unique SNPs / 142 rows |
| ClinVar | 83 records; 7 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 441 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'MTHFS'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 83 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 30 traits by best p-value, aggregated from 50 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P49914 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000136371/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/MTHFS — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/MTHFS — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=MTHFS%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/MTHFS — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:52:43  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
