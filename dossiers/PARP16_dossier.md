# Protein Dossier — PARP16 (Protein mono-ADP-ribosyltransferase PARP16)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Serum creatinine (eGFRcrea) | -0.00647 | 0.00139 | 3.44e-06 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: K60 Fissure and fistula of anal and rectal regions | 0.171 | 0.0475 | 3.19e-04 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code self-reported: pulmonary embolism (with or without) dvt | -0.13 | 0.0481 | 0.00666 | Wald ratio | 1 | trans | NA |
| Type 2 diabetes | -0.0485 | 0.0193 | 0.0121 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: Z09 Follow-up examination after treatment for conditions other than malignant neoplasms | 0.071 | 0.0288 | 0.0137 | Wald ratio | 1 | trans | NA |
| Fracture resulting from simple fall | -0.0245 | 0.0103 | 0.018 | Wald ratio | 1 | trans | NA |
| Fractured or broken bones in last 5 years | -0.0259 | 0.0122 | 0.033 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | 0.0814 | 0.0417 | 0.0512 | Wald ratio | 1 | trans | NA |
| Caudate volume | 14.8 | 7.58 | 0.0515 | Wald ratio | 1 | trans | NA |
| Eye problems or disorders: Glaucoma | 0.0576 | 0.03 | 0.0551 | Wald ratio | 1 | trans | NA |
| Neo-openness to experience | -0.198 | 0.104 | 0.0559 | Wald ratio | 1 | trans | NA |
| Haemoglobin concentration | -0.0185 | 0.00985 | 0.0603 | Wald ratio | 1 | trans | NA |
| _...and 103 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_4 association rows across 4 traits (2 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| IGDCC4 protein levels | 3e-20 | rs56275228 | 1 | GCST90469523 | no MR -> candidate analysis |
| Left ventricular end systole inferoseptal wall thickness | 1e-8 | rs202032902 | 1 | GCST90278508 | no MR -> candidate analysis |
| Adolescent idiopathic scoliosis | 9e-8 | rs8027881 | 1 | GCST006287 | no MR -> candidate analysis |
| Left ventricular mass indexed by body surface area | 6e-7 | rs73468773 | 1 | GCST90244710 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 45 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Genu varum | 0.351 | — | common-variant locus | no MR -> candidate analysis |
| Genu valgum | 0.351 | — | common-variant locus | no MR -> candidate analysis |
| placental abruption | 0.291 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.065 | — | common-variant locus | no MR -> candidate analysis |
| nephrotic syndrome | 0.062 | — | common-variant locus | no MR -> candidate analysis |
| infectious meningitis | 0.053 | — | common-variant locus | no MR -> candidate analysis |
| spondylolisthesis | 0.053 | — | common-variant locus | no MR -> candidate analysis |

> Of the 7 rows above, **7 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Protein mono-ADP-ribosyltransferase PARP16) |
| gnomAD constraint | pLI=4.3e-10, LOEUF=1.19 — LoF-tolerant |
| GWAS Catalog | 26 unique SNPs / 51 rows |
| ClinVar | 77 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 45 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'PARP16' and resolved to 'Protein mono-ADP-ribosyltransferase PARP16' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 77 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 4 of 4 traits by best p-value, aggregated from 4 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q8N5Y8 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000138617/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4105981/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PARP16 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PARP16 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PARP16%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/PARP16 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:11:20  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
