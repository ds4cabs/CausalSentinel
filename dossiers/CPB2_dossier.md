# Protein Dossier — CPB2 (Carboxypeptidase B2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Alcohol intake frequency | -0.0128 | 0.00446 | 0.00405 | Wald ratio | 1 | cis | NA |
| Glioma | 0.129 | 0.0543 | 0.0177 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: malignant melanoma | -0.0847 | 0.0373 | 0.023 | Wald ratio | 1 | cis | NA |
| Depressive symptoms | -0.0106 | 0.00471 | 0.0244 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: D12 Benign neoplasm of colon  rectum  anus and anal canal | 0.054 | 0.0241 | 0.0253 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertension | -0.011 | 0.0052 | 0.0338 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: arthritis (nos) | 0.0682 | 0.0325 | 0.0357 | Wald ratio | 1 | cis | NA |
| Large vessel disease | -0.0907 | 0.0437 | 0.0379 | Wald ratio | 1 | cis | NA |
| Cardioembolic stroke | 0.0817 | 0.0397 | 0.0395 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | -0.00788 | 0.00391 | 0.0435 | Wald ratio | 1 | cis | NA |
| Height | -0.00695 | 0.00365 | 0.057 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: Z09 Follow-up examination after treatment for conditions other than malignant neoplasms | 0.0442 | 0.0235 | 0.0596 | Wald ratio | 1 | cis | NA |
| _...and 93 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3518_54_2` | TAFI | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_126 association rows across 74 traits (121 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Succinate-semialdehyde dehydrogenase, mitochondrial levels | 2e-2461 | rs1926446 | 1 | GCST90249659 | no MR -> candidate analysis |
| FAS-associated death domain protein levels | 1e-893 | rs1926446 | 2 | GCST90247545 | no MR -> candidate analysis |
| Carboxypeptidase B2 levels | 8e-839 | rs7336360 | 4 | GCST90246876 | no MR -> candidate analysis |
| Melanoregulin levels | 3e-749 | rs7336360 | 1 | GCST90248518 | no MR -> candidate analysis |
| Uncharacterized protein KIAA2013 levels | 2e-658 | rs1926446 | 1 | GCST90250135 | no MR -> candidate analysis |
| Pirin levels | 2e-436 | rs1926446 | 2 | GCST90249006 | no MR -> candidate analysis |
| Uncharacterized protein KIAA2013 levels (KIAA2013.6538.90.3) | 5e-232 | rs532540191 | 1 | GCST90243283 | no MR -> candidate analysis |
| Apelin levels | 9e-221 | rs9534305 | 1 | GCST90246537 | no MR -> candidate analysis |
| LCP1 protein levels | 3e-205 | rs11618380 | 6 | GCST90469748 | no MR -> candidate analysis |
| Serum levels of protein CPB2 | 5e-194 | rs9534313 | 1 | GCST90088431 | no MR -> candidate analysis |
| CPB2 protein levels | 2e-177 | rs17844025 | 15 | GCST90468840 | no MR -> candidate analysis |
| Serum levels of protein CALB1 | 5e-175 | rs9534313 | 1 | GCST90090908 | no MR -> candidate analysis |
| _...and 62 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 233 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| type 2 diabetes mellitus | 0.288 | — | common-variant locus | no MR -> candidate analysis |
| ovarian neoplasm | 0.079 | — | common-variant locus | no MR -> candidate analysis |
| deficiency anemia | 0.06 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Carboxypeptidase B2) |
| gnomAD constraint | pLI=6.2e-18, LOEUF=1.19 — LoF-tolerant |
| GWAS Catalog | 100 unique SNPs / 202 rows |
| ClinVar | 117 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 233 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'CPB2' and resolved to 'Carboxypeptidase B2' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 117 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 74 traits by best p-value, aggregated from 126 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q96IY4 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000080618/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3419/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CPB2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CPB2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CPB2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CPB2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:59:57  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
