# Protein Dossier — CNP (2',3'-cyclic-nucleotide 3'-phosphodiesterase)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: osteoarthritis | 0.15 | 0.0418 | 3.43e-04 | Wald ratio | 1 | cis | NA |
| Amyotrophic lateral sclerosis | 0.392 | 0.11 | 3.49e-04 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | -0.0339 | 0.0119 | 0.00438 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | -0.0357 | 0.0125 | 0.00445 | Wald ratio | 1 | cis | NA |
| Coronary heart disease | -0.164 | 0.0576 | 0.00451 | Wald ratio | 1 | cis | NA |
| Potassium in urine | 0.0386 | 0.0147 | 0.00861 | Wald ratio | 1 | cis | NA |
| Sodium in urine | 0.037 | 0.0143 | 0.00943 | Wald ratio | 1 | cis | NA |
| Creatinine (enzymatic) in urine | 0.0348 | 0.0139 | 0.0121 | Wald ratio | 1 | cis | NA |
| Myocardial infarction | -0.155 | 0.0639 | 0.0152 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | 0.136 | 0.0564 | 0.0159 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Diabetes related eye disease | 0.316 | 0.139 | 0.0226 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: asthma | 0.0795 | 0.0375 | 0.0342 | Wald ratio | 1 | cis | NA |
| _...and 69 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_2 association rows across 2 traits (2 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| 2,3-cyclic-nucleotide 3-phosphodiesterase levels | 6e-13 | rs11079027 | 1 | GCST90247075 | no MR -> candidate analysis |
| Blood protein levels | 4e-12 | rs12602950 | 1 | GCST006585 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1679 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| myopia 2, autosomal dominant | 0.816 | — | established (curated) | no MR -> candidate analysis |
| leukodystrophy, hypomyelinating, 20 | 0.555 | — | established (curated) | no MR -> candidate analysis |
| Abnormality of the skeletal system | 0.25 | — | common-variant locus | no MR -> candidate analysis |
| achondroplasia | 0.195 | — | established (curated) | no MR -> candidate analysis |
| marfanoid habitus and intellectual disability | 0.195 | — | established (curated) | no MR -> candidate analysis |

> Of the 5 rows above, **5 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (2',3'-cyclic-nucleotide 3'-phosphodiesterase) |
| gnomAD constraint | pLI=1, LOEUF=0.381 — LoF-INTOLERANT |
| GWAS Catalog | 21 unique SNPs / 42 rows |
| ClinVar | 85 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1679 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'CNP' and resolved to '2',3'-cyclic-nucleotide 3'-phosphodiesterase' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 85 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 2 of 2 traits by best p-value, aggregated from 2 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P09543 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000173786/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL6066309/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CNP — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CNP — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CNP%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CNP — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:54:53  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
