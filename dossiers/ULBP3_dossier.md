# Protein Dossier — ULBP3 (UL16-binding protein 3)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Alcohol intake frequency | -0.0739 | 0.025 | 0.00308 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: psoriasis | 0.335 | 0.116 | 0.00372 | Wald ratio | 1 | cis | NA |
| Height | 0.0585 | 0.0205 | 0.00427 | Wald ratio | 1 | cis | NA |
| Fasting glucose | 0.0497 | 0.0216 | 0.0216 | Wald ratio | 1 | cis | NA |
| 2hr glucose | 0.304 | 0.135 | 0.0238 | Wald ratio | 1 | cis | NA |
| Neo-openness to experience | 1.09 | 0.492 | 0.0264 | Wald ratio | 1 | cis | NA |
| Caudate volume | 72.7 | 33.2 | 0.0284 | Wald ratio | 1 | cis | NA |
| Urate | 0.0819 | 0.0386 | 0.0339 | Wald ratio | 1 | cis | NA |
| Large vessel disease | 0.489 | 0.239 | 0.0407 | Wald ratio | 1 | cis | NA |
| Rheumatoid arthritis | 0.239 | 0.124 | 0.055 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertension | 0.0523 | 0.0274 | 0.0558 | Wald ratio | 1 | cis | NA |
| Knee osteoarthritis | 0.362 | 0.191 | 0.0578 | Wald ratio | 1 | cis | NA |
| _...and 80 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2747_3_2` | ULBP-3 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_22 association rows across 18 traits (13 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| NKG2D ligand 3 levels | 1e-106 | rs6918234 | 1 | GCST90425447 | no MR -> candidate analysis |
| ULBP2 protein levels | 2e-41 | rs116968353 | 3 | GCST90471008 | no MR -> candidate analysis |
| LRP11 protein levels | 4e-28 | rs9383665 | 1 | GCST90469796 | no MR -> candidate analysis |
| SH2 domain-containing adapter protein D levels | 3e-11 | rs12662494 | 1 | GCST90424770 | no MR -> candidate analysis |
| Core binding factor acute myeloid leukemia | 6e-10 | rs7769185; rs7764312; rs1999670; rs1107835; rs9383690; rs1408505 | 2 | GCST008413 | no MR -> candidate analysis |
| Blood protein levels | 2e-9 | rs17054300 | 2 | GCST006585 | no MR -> candidate analysis |
| Eosinophil count | 3e-8 | rs10428766 | 1 | GCST007065 | no MR -> candidate analysis |
| Gut microbiome abundance (class Bacteroides sp. 8 (at 1 year | 3e-8 | rs6922684 | 1 | GCST90568729 | no MR -> candidate analysis |
| Total PHF-tau (SNP x SNP interaction) | 3e-8 | rs912558 x rs6941758 | 1 | GCST010340 | no MR -> candidate analysis |
| Pain intensity in opioid-treated advanced cancer | 3e-7 | rs9479734 | 1 | GCST90435150 | no MR -> candidate analysis |
| Gut microbiome abundance (class Tyzzerella sp. 3 (at 3 month | 3e-7 | rs75811154 | 1 | GCST90568675 | no MR -> candidate analysis |
| Cerebral amyloid angiopathy x APOEe4 status interaction in A | 5e-7 | rs13207159 | 1 | GCST012484 | no MR -> candidate analysis |
| _...and 6 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 92 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| esophageal ulcer | 0.404 | — | common-variant locus | no MR -> candidate analysis |
| self-injurious ideation | 0.343 | — | common-variant locus | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=3e-09, LOEUF=1.4 — LoF-tolerant |
| GWAS Catalog | 71 unique SNPs / 129 rows |
| ClinVar | 59 records; 4 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 92 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'ULBP3'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 59 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 18 of 18 traits by best p-value, aggregated from 22 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9BZM4 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000131019/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/ULBP3 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/ULBP3 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=ULBP3%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/ULBP3 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:32:49  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
