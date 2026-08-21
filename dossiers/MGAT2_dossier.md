# Protein Dossier — MGAT2 (Alpha-1,6-mannosyl-glycoprotein 2-beta-N-acetylglucosaminyltransferase)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Forced vital capacity (FVC) | 0.0345 | 0.0102 | 6.90e-04 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | 0.033 | 0.0107 | 0.00207 | Wald ratio | 1 | cis | NA |
| Height | 0.0405 | 0.0149 | 0.00645 | Wald ratio | 1 | cis | NA |
| Urate | -0.0718 | 0.0272 | 0.00825 | Wald ratio | 1 | cis | NA |
| Transferrin | 0.137 | 0.0523 | 0.00885 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: anxiety or panic attacks | 0.219 | 0.0864 | 0.0111 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | 0.123 | 0.0488 | 0.0119 | Wald ratio | 1 | cis | NA |
| Bipolar disorder | -0.299 | 0.12 | 0.0126 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: malignant melanoma | 0.27 | 0.109 | 0.013 | Wald ratio | 1 | cis | NA |
| Squamous cell lung cancer | 0.326 | 0.133 | 0.0146 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: asthma | -0.0918 | 0.0381 | 0.0159 | Wald ratio | 1 | cis | NA |
| Caudate volume | -58.6 | 25.2 | 0.0199 | Wald ratio | 1 | cis | NA |
| _...and 105 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_No GWAS Catalog associations mapped to this gene._

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 629 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| MGAT2-congenital disorder of glycosylation | 0.834 | — | established (curated) | no MR -> candidate analysis |
| Abnormal facial shape | 0.426 | — | established (curated) | no MR -> candidate analysis |
| Global developmental delay | 0.426 | — | established (curated) | no MR -> candidate analysis |
| Abnormal glycosylation | 0.426 | — | established (curated) | no MR -> candidate analysis |
| hereditary disease | 0.316 | — | established (curated) | no MR -> candidate analysis |
| autoimmune disorder of musculoskeletal system | 0.104 | — | common-variant locus | no MR -> candidate analysis |
| corneal neovascularization | 0.098 | — | common-variant locus | no MR -> candidate analysis |
| Abnormality of the gastrointestinal tract | 0.095 | — | common-variant locus | no MR -> candidate analysis |
| lagophthalmos | 0.094 | — | common-variant locus | no MR -> candidate analysis |
| liver disorder | 0.094 | — | common-variant locus | no MR -> candidate analysis |

> Of the 10 rows above, **10 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Alpha-1,6-mannosyl-glycoprotein 2-beta-N-acetylglucosaminyltransferase) |
| gnomAD constraint | pLI=0.0093, LOEUF=0.755 — LoF-tolerant |
| GWAS Catalog | 21 unique SNPs / 42 rows |
| ClinVar | 185 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 629 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'MGAT2' and resolved to 'Alpha-1,6-mannosyl-glycoprotein 2-beta-N-acetylglucosaminyltransferase' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 185 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — No GWAS Catalog associations mapped to this gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q10469 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000168282/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2321630/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/MGAT2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/MGAT2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=MGAT2%5Bgene%5D — _ClinVar build Build260809-1055.1_

## Provenance

- Generated: 2026-08-14T03:47:21  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
