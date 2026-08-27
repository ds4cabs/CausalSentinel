# Protein Dossier — HBZ (Hemoglobin subunit zeta)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Heel bone mineral density (BMD) T-score  automated | 0.0112 | 0.00367 | 0.00228 | Wald ratio | 1 | cis | NA |
| Lumbar spine bone mineral density | 0.0324 | 0.0107 | 0.00242 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: malignant melanoma | -0.107 | 0.0359 | 0.00288 | Wald ratio | 1 | cis | NA |
| Femoral neck bone mineral density | 0.0279 | 0.00979 | 0.0043 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: bone disorder | 0.141 | 0.0528 | 0.00758 | Wald ratio | 1 | cis | NA |
| Systolic blood pressure  automated reading | -0.00745 | 0.00291 | 0.0105 | Wald ratio | 1 | cis | NA |
| Pulse rate | -0.0116 | 0.00503 | 0.0206 | Wald ratio | 1 | cis | NA |
| Forearm bone mineral density | 0.0424 | 0.0187 | 0.0235 | Wald ratio | 1 | cis | NA |
| Neuroticism | -0.0102 | 0.00452 | 0.0244 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K57 Diverticular disease of intestine | -0.046 | 0.0209 | 0.0281 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: B37 Candidiasis | 0.235 | 0.109 | 0.0304 | Wald ratio | 1 | cis | NA |
| Clear cell ovarian cancer | 0.106 | 0.0502 | 0.0346 | Wald ratio | 1 | cis | NA |
| _...and 74 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_56 association rows across 33 traits (53 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Hemoglobin subunit zeta levels | 1e-685 | rs2461286 | 2 | GCST90247854 | no MR -> candidate analysis |
| Hemoglobin subunit zeta levels (HBZ.6919.3.3) | 1e-389 | rs2461286 | 2 | GCST90241383 | no MR -> candidate analysis |
| Mean corpuscular hemoglobin | 7e-162 | rs11864973 | 9 | GCST90662875 | no MR -> candidate analysis |
| Mean corpuscular volume | 9e-134 | rs11864973 | 7 | GCST90662877 | no MR -> candidate analysis |
| Mean corpuscular haemoglobin (UKB data field 30050) | 1e-129 | rs113613943 | 2 | GCST90468084 | no MR -> candidate analysis |
| HBZ protein levels | 1e-96 | rs544061540 | 1 | GCST90469435 | no MR -> candidate analysis |
| Mean corpuscular volume (UKB data field 30040) | 4e-70 | rs11864973 | 1 | GCST90468086 | no MR -> candidate analysis |
| AHSP/CA2 protein level ratio | 9e-65 | rs7202152 | 1 | GCST90313215 | no MR -> candidate analysis |
| AHSP/BLVRB protein level ratio | 2e-60 | rs7202152 | 1 | GCST90313214 | no MR -> candidate analysis |
| AHSP/HMBS protein level ratio | 3e-50 | rs7202152 | 1 | GCST90313217 | no MR -> candidate analysis |
| Red blood cell count | 1e-45 | rs11864973 | 4 | GCST90662878 | no MR -> candidate analysis |
| Mean corpuscular hemoglobin concentration | 7e-30 | rs11864973 | 3 | GCST005992 | no MR -> candidate analysis |
| _...and 21 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 187 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| anemia (phenotype) | 0.247 | — | common-variant locus | no MR -> candidate analysis |
| Iron deficiency anemia | 0.251 | — | common-variant locus | no MR -> candidate analysis |
| inherited hemoglobinopathy | 0.17 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.081 | — | common-variant locus | no MR -> candidate analysis |
| stroke disorder | 0.081 | — | common-variant locus | no MR -> candidate analysis |

> Of the 5 rows above, **5 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Hemoglobin subunit zeta) |
| gnomAD constraint | pLI=0.42, LOEUF=1.09 — LoF-tolerant |
| GWAS Catalog | 174 unique SNPs / 419 rows |
| ClinVar | 85 records; 14 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 187 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'HBZ' and resolved to 'Hemoglobin subunit zeta' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 85 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 33 traits by best p-value, aggregated from 56 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P02008 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000130656/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL6066981/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/HBZ — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/HBZ — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=HBZ%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/HBZ — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:59:03  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
