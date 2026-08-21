# Protein Dossier — ALPP (Alkaline phosphatase, placental type)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | -0.357 | 0.14 | 0.0106 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I48 Atrial fibrillation and flutter | 0.165 | 0.0647 | 0.0108 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K44 Diaphragmatic hernia | -0.192 | 0.0784 | 0.0142 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: H25 Senile cataract | 0.177 | 0.0771 | 0.0214 | Wald ratio | 1 | cis | NA |
| Alcohol intake frequency | 0.0271 | 0.0119 | 0.022 | Wald ratio | 1 | cis | NA |
| Forearm bone mineral density | -0.114 | 0.0514 | 0.0261 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: osteoporosis | -0.17 | 0.0768 | 0.0271 | Wald ratio | 1 | cis | NA |
| Hirschsprung's disease | -0.902 | 0.414 | 0.0293 | Wald ratio | 1 | cis | NA |
| Intracranial volume | -1.42e+04 | 6.63e+03 | 0.0318 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hayfever or allergic rhinitis | 0.062 | 0.031 | 0.0458 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: osteoarthritis | 0.0501 | 0.0255 | 0.0497 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | -0.0125 | 0.00658 | 0.0573 | Wald ratio | 1 | cis | NA |
| _...and 51 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_5 association rows across 3 traits (5 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Alkaline phosphatase, placental type levels | 1e-68 | rs2853378 | 1 | GCST90246488 | no MR -> candidate analysis |
| ALPP protein levels | 9e-16 | rs201578205 | 3 | GCST90468286 | no MR -> candidate analysis |
| Refractive error | 2e-10 | rs1130335 | 1 | GCST90104407 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 397 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| ovarian disorder | 0.412 | — | common-variant locus | no MR -> candidate analysis |
| fallopian tube disorder | 0.412 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.204 | — | common-variant locus | no MR -> candidate analysis |
| male reproductive organ cancer | 0.183 | — | common-variant locus | no MR -> candidate analysis |
| transient ischemic attack | 0.146 | — | common-variant locus | no MR -> candidate analysis |

> Of the 5 rows above, **5 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Alkaline phosphatase, placental type) |
| gnomAD constraint | pLI=7.9e-11, LOEUF=1 — LoF-tolerant |
| GWAS Catalog | 103 unique SNPs / 212 rows |
| ClinVar | 185 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 397 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'ALPP' and resolved to 'Alkaline phosphatase, placental type' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 185 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 3 of 3 traits by best p-value, aggregated from 5 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P05187 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000163283/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4458/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/ALPP — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/ALPP — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=ALPP%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/ALPP — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:01:37  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
