# Protein Dossier — CD163 (Scavenger receptor cysteine-rich type 1 protein M130)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: osteoporosis | 0.148 | 0.0636 | 0.0197 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: I30 Acute pericarditis | 0.671 | 0.295 | 0.0231 | Wald ratio | 1 | trans | NA |
| Cancer code  self-reported: prostate cancer | 0.2 | 0.0885 | 0.0239 | Wald ratio | 1 | trans | NA |
| Coronary heart disease | 0.109 | 0.0483 | 0.0242 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: B37 Candidiasis | 0.559 | 0.272 | 0.0403 | Wald ratio | 1 | trans | NA |
| Rheumatoid arthritis | -0.152 | 0.08 | 0.0572 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: asthma | 0.0463 | 0.0245 | 0.0588 | Wald ratio | 1 | trans | NA |
| Myocardial infarction | 0.0956 | 0.0518 | 0.0648 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | -0.269 | 0.146 | 0.0659 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: high cholesterol | -0.0475 | 0.026 | 0.0675 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: deep venous thrombosis (dvt) | -0.135 | 0.0747 | 0.0715 | Wald ratio | 1 | trans | NA |
| Sodium in urine | -0.0151 | 0.009 | 0.0945 | Wald ratio | 1 | trans | NA |
| _...and 53 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-5028_59_1` | sCD163 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_183 association rows across 105 traits (176 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Creatine kinase levels | 1e-337 | rs7305678 | 7 | GCST90838680 | no MR -> candidate analysis |
| FOLR2 protein levels | 3e-176 | rs61729512 | 3 | GCST90469260 | no MR -> candidate analysis |
| FOLR2/THY1 protein level ratio | 3e-142 | rs7980201 | 1 | GCST90314867 | no MR -> candidate analysis |
| Lactate dehydrogenase levels | 7e-104 | rs6488345 | 4 | GCST006013 | no MR -> candidate analysis |
| FOLR3 protein levels | 6e-101 | rs61729512 | 3 | GCST90469261 | no MR -> candidate analysis |
| Circulating FOLR3 levels | 3e-96 | rs61729512 | 3 | GCST90860079 | no MR -> candidate analysis |
| KLK7 protein levels | 6e-95 | rs61729512 | 3 | GCST90469706 | no MR -> candidate analysis |
| total creatine kinase (mean, inv-norm transformed) | 6e-84 | rs4883279 | 2 | GCST90480709 | no MR -> candidate analysis |
| total creatine kinase (minimum, inv-norm transformed) | 3e-82 | rs4883279 | 2 | GCST90480710 | no MR -> candidate analysis |
| Circulating CD163 levels | 5e-79 | rs7305678 | 4 | GCST90859926 | no MR -> candidate analysis |
| total creatine kinase (maximum, inv-norm transformed) | 3e-75 | rs4883279 | 2 | GCST90480708 | no MR -> candidate analysis |
| CLEC4C protein levels | 9e-72 | rs11054195 | 4 | GCST90468772 | no MR -> candidate analysis |
| _...and 93 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1418 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| adolescent idiopathic scoliosis | 0.416 | — | common-variant locus | no MR -> candidate analysis |
| arthropathy | 0.401 | — | common-variant locus | no MR -> candidate analysis |
| acute tonsillitis | 0.401 | — | common-variant locus | no MR -> candidate analysis |
| CINCA syndrome | 0.304 | — | established (curated) | no MR -> candidate analysis |
| stroke disorder | 0.262 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.262 | — | common-variant locus | no MR -> candidate analysis |

> Of the 6 rows above, **6 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=4e-07, LOEUF=0.61 — LoF-tolerant |
| GWAS Catalog | 117 unique SNPs / 260 rows |
| ClinVar | 197 records; 4 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1418 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'CD163'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 197 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 105 traits by best p-value, aggregated from 183 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q86VB7 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000177575/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CD163 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CD163 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CD163%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CD163 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:40:39  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
