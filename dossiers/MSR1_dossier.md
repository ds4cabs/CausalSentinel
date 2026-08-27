# Protein Dossier — MSR1 (Macrophage scavenger receptor types I and II)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Myocardial infarction | -0.129 | 0.0368 | 4.76e-04 | Wald ratio | 1 | trans | NA |
| Coronary heart disease | -0.111 | 0.0334 | 8.64e-04 | Wald ratio | 1 | trans | NA |
| Amyotrophic lateral sclerosis | -0.197 | 0.0604 | 0.00113 | Wald ratio | 1 | trans | NA |
| Eczema | 0.178 | 0.0591 | 0.00266 | Wald ratio | 1 | trans | NA |
| Years of schooling | -0.0394 | 0.0131 | 0.0027 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: N92 Excessive  frequent and irregular menstruation | 0.141 | 0.048 | 0.0033 | Wald ratio | 1 | trans | NA |
| Chronic kidney disease | 0.145 | 0.0526 | 0.00596 | Wald ratio | 1 | trans | NA |
| Forced vital capacity (FVC) | -0.0177 | 0.0065 | 0.00649 | Wald ratio | 1 | trans | NA |
| LDL cholesterol | -0.0496 | 0.0184 | 0.00701 | Wald ratio | 1 | trans | NA |
| Sodium in urine | 0.0197 | 0.0078 | 0.0115 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: deep venous thrombosis (dvt) | -0.165 | 0.0666 | 0.0133 | Wald ratio | 1 | trans | NA |
| Heel bone mineral density (BMD) T-score  automated | 0.0251 | 0.0103 | 0.0143 | Wald ratio | 1 | trans | NA |
| _...and 100 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3684_78_3` | Macrophage scavenger receptor | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_147 association rows across 90 traits (112 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating MSR1 levels | 7e-323 | rs76393968 | 9 | GCST90859674 | no MR -> candidate analysis |
| MSR1 protein levels | 2e-246 | rs10103856 | 6 | GCST90469950 | no MR -> candidate analysis |
| C1QTNF5 protein levels | 5e-205 | rs73665255 | 8 | GCST90468489 | no MR -> candidate analysis |
| LGALS3BP protein levels | 5e-187 | rs73665255 | 7 | GCST90469760 | no MR -> candidate analysis |
| Galectin-3-binding protein levels | 9e-172 | rs41341748 | 4 | GCST90247672 | no MR -> candidate analysis |
| Macrophage scavenger receptor types I and II levels | 4e-119 | rs41341748 | 6 | GCST90248385 | no MR -> candidate analysis |
| FOLR2/MSR1 protein level ratio | 1e-76 | rs17583220 | 1 | GCST90314866 | no MR -> candidate analysis |
| Cerebrospinal fluid protein MSR1 levels | 9e-76 | rs41341748 | 1 | GCST90944440 | no MR -> candidate analysis |
| Cerebrospinal fluid protein C1QTNF5 levels | 3e-44 | rs41341748 | 1 | GCST90944136 | no MR -> candidate analysis |
| ITGBL1 protein levels | 3e-32 | rs41341748 | 2 | GCST90469648 | no MR -> candidate analysis |
| PTX3 protein levels | 3e-32 | rs41341748 | 2 | GCST90470392 | no MR -> candidate analysis |
| MMP3 protein levels | 6e-31 | rs41341748 | 1 | GCST90469920 | no MR -> candidate analysis |
| _...and 78 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 435 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Barrett esophagus | 0.63 | — | established (curated) | no MR -> candidate analysis |
| ovarian cancer | 0.641 | — | established (curated) | MR: beta=-0.192, p=0.248 (trans) |
| esophageal adenocarcinoma | 0.547 | — | established (curated) | no MR -> candidate analysis |
| alcohol drinking | 0.548 | — | common-variant locus | no MR -> candidate analysis |
| urolithiasis | 0.548 | — | common-variant locus | no MR -> candidate analysis |
| cannabis dependence | 0.542 | — | common-variant locus | no MR -> candidate analysis |
| keloid | 0.523 | — | common-variant locus | no MR -> candidate analysis |
| cervical carcinoma | 0.492 | — | common-variant locus | no MR -> candidate analysis |
| fungal infectious disease | 0.495 | — | common-variant locus | no MR -> candidate analysis |
| sialadenitis | 0.492 | — | common-variant locus | no MR -> candidate analysis |
| carcinoma of esophagus | 0.486 | — | established (curated) | no MR -> candidate analysis |
| bipolar disorder | 0.478 | — | common-variant locus | MR: beta=0.0814, p=0.348 (trans) |
| muscle cramp | 0.424 | — | common-variant locus | no MR -> candidate analysis |
| coronary artery disorder | 0.404 | — | common-variant locus | no MR -> candidate analysis |
| diabetes mellitus | 0.396 | — | common-variant locus | no MR -> candidate analysis |

> Of the 15 rows above, **13 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Macrophage scavenger receptor types I and II) |
| gnomAD constraint | pLI=1.9e-20, LOEUF=1.41 — LoF-tolerant |
| GWAS Catalog | 117 unique SNPs / 185 rows |
| ClinVar | 239 records; 4 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 435 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'MSR1' and resolved to 'Macrophage scavenger receptor types I and II' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 239 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 90 traits by best p-value, aggregated from 147 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P21757 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000038945/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL5811/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/MSR1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/MSR1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=MSR1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/MSR1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:52:28  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
