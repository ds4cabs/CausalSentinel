# Protein Dossier — AKR1A1 (Aldo-keto reductase family 1 member A1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.033 | 0.0108 | 0.00237 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: gastro-oesophageal reflux (gord)  or  gastric reflux | 0.0549 | 0.0198 | 0.00557 | Wald ratio | 1 | cis | NA |
| ER-positive Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.035 | 0.0128 | 0.00624 | Wald ratio | 1 | cis | NA |
| High grade serous ovarian cancer | 0.0708 | 0.0286 | 0.0132 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K57 Diverticular disease of intestine | 0.0691 | 0.0285 | 0.0154 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I84 Haemorrhoids | -0.0696 | 0.0299 | 0.02 | Wald ratio | 1 | cis | NA |
| Nucleus accumbens volume | -4.5 | 2 | 0.0246 | Wald ratio | 1 | cis | NA |
| Ovarian cancer | 0.0519 | 0.024 | 0.0303 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: J33 Nasal polyp | -0.161 | 0.0746 | 0.0306 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hiatus hernia | -0.0584 | 0.0302 | 0.0533 | Wald ratio | 1 | cis | NA |
| Fracture resulting from simple fall | -0.0224 | 0.0119 | 0.0592 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: arthritis (nos) | -0.103 | 0.0556 | 0.0647 | Wald ratio | 1 | cis | NA |
| _...and 68 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-4192_10_2` | AK1A1 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_48 association rows across 35 traits (46 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Ribitol levels | 2e-123 | rs2229540 | 1 | GCST90139610 | no MR -> candidate analysis |
| Alcohol dehydrogenase [NADP(+)] levels | 5e-68 | rs2229540 | 2 | GCST90162010 | no MR -> candidate analysis |
| Erythritol levels | 4e-64 | rs2229540 | 3 | GCST90245187 | no MR -> candidate analysis |
| Height | 4e-50 | rs518365 | 3 | GCST90245848 | no MR -> candidate analysis |
| Peroxiredoxin-1 levels | 2e-48 | rs2356552 | 1 | GCST90248961 | no MR -> candidate analysis |
| platelet count (mean, inv-norm transformed) | 5e-39 | rs11211137 | 1 | GCST90480651 | no MR -> candidate analysis |
| platelet count (maximum, inv-norm transformed) | 3e-34 | rs11211137 | 1 | GCST90480650 | no MR -> candidate analysis |
| Urine ribitol levels in chronic kidney disease | 1e-31 | rs2229540 | 1 | GCST90265910 | no MR -> candidate analysis |
| Creatinine levels | 2e-27 | rs35349030 | 3 | GCST90662902 | no MR -> candidate analysis |
| Circulating PRDX1 levels | 6e-25 | rs2356552 | 1 | GCST90860183 | no MR -> candidate analysis |
| Estimated glomerular filtration rate (creatinine) | 1e-24 | rs499600 | 1 | GCST90100220 | no MR -> candidate analysis |
| PRDX1 protein levels | 1e-23 | rs2356552 | 2 | GCST90470315 | no MR -> candidate analysis |
| _...and 23 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 551 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| heart failure | 0.211 | — | common-variant locus | no MR -> candidate analysis |
| deep vein thrombosis | 0.119 | — | common-variant locus | no MR -> candidate analysis |
| Arthralgia | 0.081 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Aldo-keto reductase family 1 member A1) |
| gnomAD constraint | pLI=2.2e-06, LOEUF=0.921 — LoF-tolerant |
| GWAS Catalog | 87 unique SNPs / 173 rows |
| ClinVar | 69 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 551 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'AKR1A1' and resolved to 'Aldo-keto reductase family 1 member A1' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 69 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 35 traits by best p-value, aggregated from 48 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P14550 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000117448/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2246/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/AKR1A1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/AKR1A1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=AKR1A1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/AKR1A1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T00:59:41  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
