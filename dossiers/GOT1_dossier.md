# Protein Dossier — GOT1 (Aspartate aminotransferase, cytoplasmic)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Mean cell haemoglobin concentration | -0.0321 | 0.00886 | 2.87e-04 | Inverse variance weighted | 2 | trans | NA |
| Mean cell haemoglobin concentration | -0.0321 | 0.00886 | 2.87e-04 | Inverse variance weighted | 2 | trans | NA |
| Knee osteoarthritis | 0.225 | 0.0687 | 0.00108 | Inverse variance weighted | 2 | trans | NA |
| Knee osteoarthritis | 0.225 | 0.0687 | 0.00108 | Inverse variance weighted | 2 | trans | NA |
| Non-cancer illness code  self-reported: bone disorder | 0.31 | 0.098 | 0.0016 | Inverse variance weighted | 2 | trans | NA |
| Non-cancer illness code  self-reported: bone disorder | 0.31 | 0.098 | 0.0016 | Inverse variance weighted | 2 | trans | NA |
| Non-cancer illness code  self-reported: gastro-oesophageal reflux (gord)  or  gastric reflux | 0.0722 | 0.0278 | 0.00936 | Inverse variance weighted | 2 | trans | NA |
| Non-cancer illness code  self-reported: gastro-oesophageal reflux (gord)  or  gastric reflux | 0.0722 | 0.0278 | 0.00936 | Inverse variance weighted | 2 | trans | NA |
| Diagnoses - main ICD10: M17 Gonarthrosis [arthrosis of knee] | 0.1 | 0.0404 | 0.0131 | Inverse variance weighted | 2 | trans | NA |
| Diagnoses - main ICD10: M17 Gonarthrosis [arthrosis of knee] | 0.1 | 0.0404 | 0.0131 | Inverse variance weighted | 2 | trans | NA |
| Non-cancer illness code  self-reported: osteoarthritis | 0.0488 | 0.0197 | 0.0134 | Inverse variance weighted | 2 | trans | NA |
| Non-cancer illness code  self-reported: osteoarthritis | 0.0488 | 0.0197 | 0.0134 | Inverse variance weighted | 2 | trans | NA |
| _...and 172 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-4912_17_1` | GOT1 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_130 association rows across 83 traits (113 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Aspartate aminotransferase levels | 1e-609 | rs749913156 | 11 | GCST90025980 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 3e-122 | rs11190131 | 2 | GCST90838671 | no MR -> candidate analysis |
| Aspartate aminotransferase (AST, minimum, inv-norm transform | 3e-94 | rs76850691 | 2 | GCST90479511 | no MR -> candidate analysis |
| Aspartate aminotransferase (AST, mean, inv-norm transformed) | 4e-88 | rs76850691 | 2 | GCST90479510 | no MR -> candidate analysis |
| mean corpuscular volume (MCV, maximum, inv-norm transformed) | 2e-68 | rs17094148 | 2 | GCST90475466 | no MR -> candidate analysis |
| Aspartate aminotransferase (AST, maximum, inv-norm transform | 2e-63 | rs76850691 | 1 | GCST90475116 | no MR -> candidate analysis |
| mean corpuscular hemoglobin (MCH, minimum, inv-norm transfor | 3e-57 | rs17094148 | 2 | GCST90475450 | no MR -> candidate analysis |
| monocyte (absolute count, mean, inv-norm transformed) | 5e-45 | rs11190134 | 1 | GCST90479702 | no MR -> candidate analysis |
| monocyte (fraction, mean, inv-norm transformed) | 8e-42 | rs11190134 | 1 | GCST90479705 | no MR -> candidate analysis |
| mean corpuscular hemoglobin (MCH, maximum, inv-norm transfor | 5e-41 | rs17094148 | 1 | GCST90479672 | no MR -> candidate analysis |
| mean corpuscular volume (MCV, mean, inv-norm transformed) | 2e-40 | rs17094148 | 1 | GCST90479676 | no MR -> candidate analysis |
| mean corpuscular hemoglobin (MCH, mean, inv-norm transformed | 2e-40 | rs17094148 | 1 | GCST90479673 | no MR -> candidate analysis |
| _...and 71 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 559 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| biliary tract disorder | 0.418 | — | common-variant locus | no MR -> candidate analysis |
| obesity disorder | 0.403 | — | common-variant locus | no MR -> candidate analysis |
| Abnormality of the skeletal system | 0.195 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Vesicle transport protein GOT1B) |
| gnomAD constraint | pLI=0.0007, LOEUF=0.724 — LoF-tolerant |
| GWAS Catalog | 88 unique SNPs / 176 rows |
| ClinVar | 88 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 559 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'GOT1' and resolved to 'Vesicle transport protein GOT1B' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 88 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 83 traits by best p-value, aggregated from 130 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P17174 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000120053/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL6066348/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/GOT1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/GOT1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=GOT1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/GOT1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:51:45  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
