# Protein Dossier — JAK2 (Tyrosine-protein kinase JAK2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Eye problems or disorders: Glaucoma | 0.262 | 0.0678 | 1.09e-04 | Wald ratio | 1 | trans | NA |
| Eye problems or disorders: Injury or trauma resulting in loss of vision | 0.362 | 0.0965 | 1.72e-04 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: K60 Fissure and fistula of anal and rectal regions | 0.394 | 0.106 | 1.99e-04 | Wald ratio | 1 | trans | NA |
| Squamous cell lung cancer | -0.448 | 0.128 | 4.65e-04 | Wald ratio | 1 | trans | NA |
| Forced vital capacity (FVC) | 0.027 | 0.00861 | 0.00172 | Wald ratio | 1 | trans | NA |
| Packed cell volume | -0.296 | 0.112 | 0.00814 | Wald ratio | 1 | trans | NA |
| Haemoglobin concentration | -0.0973 | 0.037 | 0.00848 | Wald ratio | 1 | trans | NA |
| Height | 0.0382 | 0.0157 | 0.015 | Wald ratio | 1 | trans | NA |
| Percent emphysema | -0.0965 | 0.0416 | 0.0205 | Wald ratio | 1 | trans | NA |
| Forced expiratory volume in 1-second (FEV1) | 0.0208 | 0.00908 | 0.0218 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: diverticular disease or diverticulitis | -0.311 | 0.139 | 0.0246 | Wald ratio | 1 | trans | NA |
| Serum creatinine (eGFRcrea) | 0.00935 | 0.00425 | 0.0278 | Wald ratio | 1 | trans | NA |
| _...and 84 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-4998_50_1` | JAK2 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_346 association rows across 160 traits (325 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Myeloproliferative disease (PheCode 200) | 1e-323 | rs77375493 | 4 | GCST90475608 | no MR -> candidate analysis |
| Polycythemia vera (PheCode 200.1) | 1e-323 | rs77375493 | 3 | GCST90479825 | no MR -> candidate analysis |
| red cell diameter width (RDW, mean, inv-norm transformed) | 1e-323 | rs77375493 | 3 | GCST90476361 | no MR -> candidate analysis |
| red cell diameter width (RDW, maximum, inv-norm transformed) | 9e-308 | rs77375493 | 3 | GCST90476357 | no MR -> candidate analysis |
| red cell diameter width (RDW, minimum, inv-norm transformed) | 2e-264 | rs77375493 | 3 | GCST90476365 | no MR -> candidate analysis |
| platelet count (maximum, inv-norm transformed) | 5e-234 | rs77375493 | 2 | GCST90480650 | no MR -> candidate analysis |
| Other diseases of blood and blood-forming organs (PheCode 28 | 2e-199 | rs77375493 | 3 | GCST90479994 | no MR -> candidate analysis |
| monocyte (fraction, mean, inv-norm transformed) | 8e-171 | rs77375493 | 3 | GCST90475511 | no MR -> candidate analysis |
| red blood cell count (RBC, maximum, inv-norm transformed) | 4e-165 | rs77375493 | 3 | GCST90476345 | no MR -> candidate analysis |
| white blood cell count (WBC, mean, inv-norm transformed) | 2e-160 | rs77375493 | 3 | GCST90476454 | no MR -> candidate analysis |
| mean corpuscular hemoglobin concentration (MCHC, minimum, in | 1e-157 | rs77375493 | 3 | GCST90475462 | no MR -> candidate analysis |
| lymphocyte (fraction, mean, inv-norm transformed) | 8e-155 | rs77375493 | 3 | GCST90475435 | no MR -> candidate analysis |
| _...and 148 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1636 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| acquired polycythemia vera | 0.784 | 0.758 | established (curated) | no MR -> candidate analysis |
| primary myelofibrosis | 0.642 | 0.249 | established (curated) | no MR -> candidate analysis |
| ulcerative colitis | 0.818 | — | common-variant locus | no MR -> candidate analysis |
| myeloproliferative disorder | 0.68 | 0.713 | established (curated) | no MR -> candidate analysis |
| Crohn disease | 0.807 | — | common-variant locus | no MR -> candidate analysis |
| neoplasm | 0.647 | 0.76 | established (curated) | MR: beta=0.166, p=0.134 (trans) |
| Splenomegaly | 0.79 | 0.865 | established (curated) | no MR -> candidate analysis |
| acute myeloid leukemia | 0.743 | — | established (curated) | no MR -> candidate analysis |
| cancer | 0.654 | — | common-variant locus | MR: beta=-0.448, p=4.65e-04 (trans) |
| essential thrombocythemia | 0.377 | — | established (curated) | no MR -> candidate analysis |
| thrombocythemia 3 | 0.826 | — | established (curated) | no MR -> candidate analysis |
| hematologic disorder | 0.81 | 0.824 | multi-layer: burden+GWAS (allelic-series candidate) | no MR -> candidate analysis |
| ankylosing spondylitis | 0.492 | — | common-variant locus | MR: beta=-0.465, p=0.207 (trans) |
| hemorrhagic disease | 0.751 | 0.76 | multi-layer: burden+GWAS (allelic-series candidate) | no MR -> candidate analysis |
| Hepatomegaly | 0.707 | 0.753 | multi-layer: burden+GWAS (allelic-series candidate) | no MR -> candidate analysis |

> Of the 15 rows above, **12 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 1 exploratory rare-variant signal(s), 3 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 20 known modulators (Tyrosine-protein kinase JAK2) |
| gnomAD constraint | pLI=1.2e-16, LOEUF=0.739 — LoF-tolerant |
| GWAS Catalog | 103 unique SNPs / 217 rows |
| ClinVar | 796 records; 7 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1636 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'JAK2' and resolved to 'Tyrosine-protein kinase JAK2' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 796 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 160 traits by best p-value, aggregated from 346 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O60674 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000096968/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2971/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/JAK2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/JAK2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=JAK2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/JAK2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:20:07  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
