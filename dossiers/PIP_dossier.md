# Protein Dossier — PIP (Prolactin-inducible protein)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: gastro-oesophageal reflux (gord)  or  gastric reflux | 0.187 | 0.06 | 0.00185 | Wald ratio | 1 | cis | NA |
| Birth weight | -0.0676 | 0.0234 | 0.0039 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I84 Haemorrhoids | 0.211 | 0.0784 | 0.00708 | Wald ratio | 1 | cis | NA |
| Birth length | -0.159 | 0.0596 | 0.00759 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: muscle or soft tissue injuries | 0.341 | 0.128 | 0.00771 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypopituitarism | 0.926 | 0.377 | 0.0141 | Wald ratio | 1 | cis | NA |
| Fasting glucose | 0.0489 | 0.0202 | 0.0155 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Cataract | -0.251 | 0.107 | 0.0185 | Wald ratio | 1 | cis | NA |
| Weight | -0.0293 | 0.0132 | 0.0265 | Wald ratio | 1 | cis | NA |
| HOMA-B | -0.0447 | 0.0202 | 0.0271 | Wald ratio | 1 | cis | NA |
| Hippocampus volume | -70.7 | 32.2 | 0.028 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: S76 Injury of muscle and tendon at hip and thigh level | 0.805 | 0.371 | 0.0302 | Wald ratio | 1 | cis | NA |
| _...and 100 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_11 association rows across 9 traits (8 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Prolactin-inducible protein levels | 1e-159 | rs73170678 | 2 | GCST90249003 | no MR -> candidate analysis |
| Protein LEG1 homolog levels | 5e-109 | rs75076193 | 2 | GCST90248272 | no MR -> candidate analysis |
| Extracellular glycoprotein lacritin levels | 4e-63 | rs75076193 | 1 | GCST90248223 | no MR -> candidate analysis |
| Serum levels of protein PIP | 6e-40 | rs73170678 | 1 | GCST90089271 | no MR -> candidate analysis |
| EPHA1 protein levels | 2e-13 | rs560996067 | 1 | GCST90469129 | no MR -> candidate analysis |
| Amphoterin-induced protein 1:Cytoplasmic domain protein leve | 7e-9 | rs73170678 | 1 | GCST90441947 | no MR -> candidate analysis |
| Major depressive disorder in trauma-unexposed individuals | 2e-7 | rs28672333 | 1 | GCST009981 | no MR -> candidate analysis |
| Cancer | 3e-7 | rs2078176; rs6975391; rs17837474; rs17837475; rs6968949; rs6946770; rs17251; rs6959895; rs10273639; rs2367486; rs12539089; rs11327; rs3134906; rs4281045; rs7805607; rs17163745; rs2063993; rs4987668; rs4252435; rs4252416; rs4252381; rs17164103; rs1506403; rs9986765; rs534126 | 1 | GCST005275 | MR: beta=0.187, p=0.00185 (cis) |
| Dermatomyositis | 7e-7 | rs9986765 | 1 | GCST003522 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 381 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| chronic laryngitis | 0.331 | — | common-variant locus | no MR -> candidate analysis |
| diabetic ketoacidosis | 0.293 | — | common-variant locus | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 2 known modulators (1-phosphatidylinositol 3-phosphate 5-kinase) |
| gnomAD constraint | pLI=0.0043, LOEUF=1.23 — LoF-tolerant |
| GWAS Catalog | 12 unique SNPs / 24 rows |
| ClinVar | 77 records; 13 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 381 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'PIP' and resolved to '1-phosphatidylinositol 3-phosphate 5-kinase' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 77 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 9 of 9 traits by best p-value, aggregated from 11 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P12273 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000159763/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL1938222/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PIP — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PIP — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PIP%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/PIP — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:20:46  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: pharmgkb
