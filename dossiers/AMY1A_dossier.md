# Protein Dossier — AMY1A (Alpha-amylase 1A)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: I84 Haemorrhoids | 0.0911 | 0.034 | 0.00746 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: osteoporosis | -0.124 | 0.0528 | 0.0187 | Wald ratio | 1 | cis | NA |
| Intracranial volume | 1.48e+04 | 6.35e+03 | 0.02 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: ankylosing spondylitis | 0.203 | 0.0903 | 0.0247 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Arm | -0.153 | 0.0683 | 0.0251 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N40 Hyperplasia of prostate | 0.119 | 0.0537 | 0.0272 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K57 Diverticular disease of intestine | 0.0792 | 0.0377 | 0.0357 | Wald ratio | 1 | cis | NA |
| Thalamus volume | 37.3 | 18.4 | 0.0423 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertension | -0.0202 | 0.0101 | 0.0455 | Wald ratio | 1 | cis | NA |
| Eczema | -0.103 | 0.0517 | 0.0463 | Wald ratio | 1 | cis | NA |
| Neuroticism | -0.0183 | 0.00962 | 0.0574 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: H25 Senile cataract | -0.141 | 0.0766 | 0.0662 | Wald ratio | 1 | cis | NA |
| _...and 72 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_1 association rows across 1 traits (1 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Alpha-amylase 1 levels (AMY1A.7918.114.3) | 3e-19 | rs370981115 | 1 | GCST90240245 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 47 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| dentures | 0.757 | — | common-variant locus | no MR -> candidate analysis |
| dental caries | 0.536 | — | common-variant locus | no MR -> candidate analysis |
| osteoarthritis | 0.058 | — | common-variant locus | MR: beta=-0.0242, p=0.223 (cis) |
| oropharynx cancer | 0.052 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.052 | — | common-variant locus | no MR -> candidate analysis |
| seasonal allergic rhinitis | 0.052 | — | common-variant locus | no MR -> candidate analysis |
| intelligence | 0.048 | — | common-variant locus | no MR -> candidate analysis |
| chronic atrophic gastritis | 0.042 | — | common-variant locus | no MR -> candidate analysis |
| hyperaldosteronism | 0.042 | — | common-variant locus | no MR -> candidate analysis |
| polycythemia | 0.04 | — | common-variant locus | no MR -> candidate analysis |
| trauma complication | 0.037 | — | common-variant locus | no MR -> candidate analysis |
| viral pneumonia | 0.037 | — | common-variant locus | no MR -> candidate analysis |
| disease of peritoneum | 0.034 | — | common-variant locus | no MR -> candidate analysis |
| vertebral joint disorder | 0.033 | — | common-variant locus | no MR -> candidate analysis |
| Abnormality of the skeletal system | 0.032 | — | common-variant locus | no MR -> candidate analysis |

> Of the 15 rows above, **14 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Alpha-amylase 1A) |
| gnomAD constraint | pLI=0.92, LOEUF=0.572 — LoF-INTOLERANT |
| GWAS Catalog | 22 unique SNPs / 44 rows |
| ClinVar | 48 records; 6 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 47 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'AMY1A' and resolved to 'Alpha-amylase 1A' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 48 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 1 of 1 traits by best p-value, aggregated from 1 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P0DUB6 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000237763/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2478/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/AMY1A — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/AMY1A — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=AMY1A%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/AMY1A — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:02:42  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
