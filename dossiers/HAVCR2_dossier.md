# Protein Dossier — HAVCR2 (Hepatitis A virus cellular receptor 2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: hyperthyroidism or thyrotoxicosis | 0.165 | 0.0416 | 7.44e-05 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: high cholesterol | -0.0397 | 0.0119 | 8.22e-04 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | 0.0567 | 0.0177 | 0.00137 | Wald ratio | 1 | cis | NA |
| LDL cholesterol | -0.025 | 0.00802 | 0.00181 | Inverse variance weighted | 2 | trans | NA |
| LDL cholesterol | -0.025 | 0.00802 | 0.00181 | Inverse variance weighted | 2 | cis | NA |
| Internalizing problems | -0.15 | 0.0609 | 0.0136 | Wald ratio | 1 | trans | NA |
| Total cholesterol | -0.0242 | 0.0109 | 0.0261 | Inverse variance weighted | 2 | trans | NA |
| Total cholesterol | -0.0242 | 0.0109 | 0.0261 | Inverse variance weighted | 2 | cis | NA |
| Eye problems or disorders: Glaucoma | -0.0817 | 0.0383 | 0.0328 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K35 Acute appendicitis | 0.115 | 0.0542 | 0.0346 | Wald ratio | 1 | cis | NA |
| Alcohol intake frequency | -0.0128 | 0.00624 | 0.0396 | Wald ratio | 1 | cis | NA |
| Hirschsprung's disease | 1.32 | 0.67 | 0.0489 | Wald ratio | 1 | cis | NA |
| _...and 112 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-5134_52_2` | TIMD3 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_44 association rows across 29 traits (37 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Hepatitis A virus cellular receptor 2 levels | 2e-517 | rs7442742 | 5 | GCST90247869 | no MR -> candidate analysis |
| Circulating HAVCR2 levels | 4e-316 | rs190211816 | 4 | GCST90860595 | no MR -> candidate analysis |
| HAVCR2 protein levels | 1e-297 | rs147827860 | 3 | GCST90469432 | no MR -> candidate analysis |
| Serum levels of protein HAVCR2 | 3e-176 | rs919744 | 2 | GCST90088950 | no MR -> candidate analysis |
| Hepatitis A virus cellular receptor 2 levels (HAVCR2.5134.52 | 1e-145 | rs6874178 | 1 | GCST90241395 | no MR -> candidate analysis |
| Hepatitis A virus cellular receptor 2 (analyte X5134.52) lev | 4e-145 | rs6873659 | 1 | GCST90426271 | no MR -> candidate analysis |
| HAVCR1 protein levels | 1e-113 | rs113319693 | 3 | GCST90469431 | no MR -> candidate analysis |
| Blood protein levels | 7e-104 | rs4704737 | 1 | GCST006585 | no MR -> candidate analysis |
| Circulating HAVCR1 levels (id: OID00426_OID21422) | 9e-97 | rs61159436 | 1 | GCST90859787 | no MR -> candidate analysis |
| HAVCR2/TNFRSF1B protein level ratio | 3e-80 | rs115961055 | 1 | GCST90315030 | no MR -> candidate analysis |
| Circulating HAVCR1 levels (id: OID01075_OID21422) | 2e-74 | rs61159436 | 1 | GCST90860291 | no MR -> candidate analysis |
| FOLR2/HAVCR2 protein level ratio | 2e-66 | rs115961055 | 1 | GCST90314865 | no MR -> candidate analysis |
| _...and 17 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 797 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| subcutaneous panniculitis-like T-cell lymphoma | 0.752 | — | established (curated) | no MR -> candidate analysis |
| late-onset Alzheimers disease | 0.43 | — | common-variant locus | no MR -> candidate analysis |
| dementia | 0.385 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 3 known modulators (Hepatitis A virus cellular receptor 2) |
| gnomAD constraint | pLI=0.013, LOEUF=0.838 — LoF-tolerant |
| GWAS Catalog | 105 unique SNPs / 209 rows |
| ClinVar | 101 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 797 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'HAVCR2' and resolved to 'Hepatitis A virus cellular receptor 2' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 101 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 29 traits by best p-value, aggregated from 44 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q8TDQ0 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000135077/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4630879/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/HAVCR2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/HAVCR2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=HAVCR2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/HAVCR2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:58:13  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
