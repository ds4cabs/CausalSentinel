# Protein Dossier — GRP (Gastrin-releasing peptide)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Major depressive disorder | -0.175 | 0.0933 | 0.0603 | Wald ratio | 1 | trans | NA |
| Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | 0.0425 | 0.0262 | 0.105 | Wald ratio | 1 | trans | NA |
| Rheumatoid arthritis | -0.118 | 0.0793 | 0.136 | Wald ratio | 1 | trans | NA |
| Squamous cell lung cancer | -0.173 | 0.125 | 0.167 | Wald ratio | 1 | trans | NA |
| Hip osteoarthritis | 0.128 | 0.102 | 0.208 | Wald ratio | 1 | trans | NA |
| Platelet count | 37.1 | 30.4 | 0.222 | Wald ratio | 1 | trans | NA |
| Invasive mucinous ovarian cancer | -0.193 | 0.158 | 0.223 | Wald ratio | 1 | trans | NA |
| ER-positive Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | 0.0377 | 0.0314 | 0.23 | Wald ratio | 1 | trans | NA |
| Primary sclerosing cholangitis  | -0.141 | 0.118 | 0.234 | Wald ratio | 1 | trans | NA |
| Depressive symptoms | 0.0153 | 0.0138 | 0.267 | Wald ratio | 1 | trans | NA |
| Knee and hip osteoarthritis | 0.0787 | 0.0744 | 0.29 | Wald ratio | 1 | trans | NA |
| Birth weight | -0.0156 | 0.0149 | 0.293 | Wald ratio | 1 | trans | NA |
| _...and 7 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_80 association rows across 49 traits (63 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| GRP protein levels | 1e-55 | rs9952787 | 6 | GCST90469406 | no MR -> candidate analysis |
| Body mass index | 2e-25 | rs7243357 | 17 | GCST90255621 | no MR -> candidate analysis |
| Weight (maximum, inv-normal transformed) | 3e-23 | rs1517036 | 1 | GCST90480726 | no MR -> candidate analysis |
| Body mass index (BMI, maximum, inv-normal transformed) | 3e-21 | rs55932597 | 1 | GCST90479521 | no MR -> candidate analysis |
| Body mass index (MTAG) | 2e-20 | rs7243357 | 1 | GCST90179150 | no MR -> candidate analysis |
| Height | 3e-20 | rs7230581 | 1 | GCST90245848 | no MR -> candidate analysis |
| Weight (mean, inv-normal transformed) | 4e-20 | rs1517036 | 1 | GCST90480727 | no MR -> candidate analysis |
| Type 2 diabetes | 5e-19 | rs9957320 | 7 | GCST90492734 | no MR -> candidate analysis |
| Body mass index (BMI, mean, inv-normal transformed) | 1e-18 | rs55932597 | 1 | GCST90479522 | no MR -> candidate analysis |
| Circulating PON3 levels | 5e-17 | rs8091691 | 1 | GCST90859987 | no MR -> candidate analysis |
| Metabolic syndrome | 2e-16 | rs7243357 | 1 | GCST90444487 | no MR -> candidate analysis |
| Weight | 2e-16 | rs9951619 | 1 | GCST90662910 | MR: beta=-0.0156, p=0.293 (trans) |
| _...and 37 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 559 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| type 2 diabetes mellitus | 0.858 | — | common-variant locus | no MR -> candidate analysis |
| obesity disorder | 0.806 | — | common-variant locus | no MR -> candidate analysis |
| diabetes mellitus | 0.801 | — | common-variant locus | no MR -> candidate analysis |
| Abnormality of the skeletal system | 0.752 | — | common-variant locus | no MR -> candidate analysis |
| morbid obesity | 0.686 | — | common-variant locus | no MR -> candidate analysis |
| hypertensive disorder | 0.552 | — | common-variant locus | no MR -> candidate analysis |
| overnutrition | 0.538 | — | common-variant locus | no MR -> candidate analysis |
| conduction system disorder | 0.473 | — | common-variant locus | no MR -> candidate analysis |

> Of the 8 rows above, **8 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Gastrin-releasing peptide receptor) |
| gnomAD constraint | pLI=0.0003, LOEUF=1.44 — LoF-tolerant |
| GWAS Catalog | 55 unique SNPs / 110 rows |
| ClinVar | 104 records; 12 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 559 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'GRP' and resolved to 'Gastrin-releasing peptide receptor' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 104 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 49 traits by best p-value, aggregated from 80 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P07492 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000134443/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4959/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/GRP — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/GRP — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=GRP%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/GRP — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:54:50  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
