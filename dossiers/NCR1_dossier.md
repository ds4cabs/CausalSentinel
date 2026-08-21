# Protein Dossier — NCR1 (Natural cytotoxicity triggering receptor 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Clear cell ovarian cancer | -0.427 | 0.194 | 0.0272 | Wald ratio | 1 | cis | NA |
| Coronary heart disease | 0.0748 | 0.0489 | 0.127 | Wald ratio | 1 | cis | NA |
| Depressive symptoms | 0.0276 | 0.0193 | 0.153 | Wald ratio | 1 | cis | NA |
| Intracranial volume | 1.84e+04 | 1.3e+04 | 0.158 | Wald ratio | 1 | cis | NA |
| Lumbar spine bone mineral density | -0.0627 | 0.0505 | 0.215 | Wald ratio | 1 | cis | NA |
| Amyotrophic lateral sclerosis | 0.108 | 0.0895 | 0.226 | Wald ratio | 1 | cis | NA |
| Femoral neck bone mineral density | -0.0556 | 0.048 | 0.246 | Wald ratio | 1 | cis | NA |
| Thalamus volume | 46.2 | 42.1 | 0.273 | Wald ratio | 1 | cis | NA |
| Myocardial infarction | 0.0586 | 0.0547 | 0.284 | Wald ratio | 1 | cis | NA |
| Squamous cell lung cancer | -0.176 | 0.168 | 0.295 | Wald ratio | 1 | cis | NA |
| Lung adenocarcinoma | 0.146 | 0.147 | 0.322 | Wald ratio | 1 | cis | NA |
| Birth weight | -0.0163 | 0.0193 | 0.399 | Wald ratio | 1 | cis | NA |
| _...and 1 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-5104_57_3` | NKp46 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_41 association rows across 23 traits (39 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating FCAR levels | 3e-1287 | rs59090680 | 1 | GCST90860714 | no MR -> candidate analysis |
| Circulating NCR1 levels (id: OID01007_OID20566) | 2e-341 | rs2278427 | 4 | GCST90860233 | no MR -> candidate analysis |
| Circulating NCR1 levels (id: OID00816_OID20566) | 1e-337 | rs2278427 | 4 | GCST90860146 | no MR -> candidate analysis |
| FCAR protein levels | 7e-178 | rs9789251 | 2 | GCST90469197 | no MR -> candidate analysis |
| NCR1 protein levels | 1e-144 | rs11880295 | 2 | GCST90470009 | no MR -> candidate analysis |
| KIR2DS4 protein levels | 1e-119 | rs622941 | 3 | GCST90469686 | no MR -> candidate analysis |
| Natural cytotoxicity triggering receptor 1 levels | 2e-75 | rs2278428 | 3 | GCST90248750 | no MR -> candidate analysis |
| KIR2DL2 protein levels | 3e-51 | rs58244710 | 3 | GCST90469684 | no MR -> candidate analysis |
| KIR2DL3 protein levels | 1e-46 | rs62124577 | 2 | GCST90469685 | no MR -> candidate analysis |
| Immunoglobulin alpha Fc receptor levels | 5e-46 | rs57490427 | 1 | GCST90059957 | no MR -> candidate analysis |
| Natural cytotoxicity triggering receptor 1 (analyte X5104.57 | 2e-34 | rs140786877 | 1 | GCST90426248 | no MR -> candidate analysis |
| Serum levels of protein NCR1 | 9e-33 | rs2278427 | 1 | GCST90090153 | no MR -> candidate analysis |
| _...and 11 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 398 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| alcohol drinking | 0.263 | — | common-variant locus | no MR -> candidate analysis |
| urolithiasis | 0.263 | — | common-variant locus | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Natural cytotoxicity triggering receptor 1) |
| gnomAD constraint | pLI=3.6e-10, LOEUF=1.25 — LoF-tolerant |
| GWAS Catalog | 133 unique SNPs / 273 rows |
| ClinVar | 247 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 398 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'NCR1' and resolved to 'Natural cytotoxicity triggering receptor 1' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 247 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 23 traits by best p-value, aggregated from 41 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O76036 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000189430/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL6066290/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/NCR1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/NCR1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=NCR1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/NCR1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:56:53  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
