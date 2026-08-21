# Protein Dossier — PCBD1 (Pterin-4-alpha-carbinolamine dehydratase)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Lung adenocarcinoma | 0.496 | 0.158 | 0.00165 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R14 Flatulence and related conditions | 0.935 | 0.3 | 0.00182 | Wald ratio | 1 | cis | NA |
| PGC cross-disorder traits | 0.255 | 0.0842 | 0.00248 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: depression | -0.252 | 0.0885 | 0.00439 | Wald ratio | 1 | cis | NA |
| Major depressive disorder | 0.372 | 0.149 | 0.0126 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: small intestine or small bowel cancer | 0.882 | 0.38 | 0.0204 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Glaucoma | -0.668 | 0.301 | 0.0265 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: pernicious anaemia | 0.44 | 0.207 | 0.0334 | Wald ratio | 1 | cis | NA |
| Lung cancer | 0.229 | 0.11 | 0.0371 | Wald ratio | 1 | cis | NA |
| Fasting insulin | -0.0428 | 0.0217 | 0.0482 | Wald ratio | 1 | cis | NA |
| Knee and hip osteoarthritis | 0.282 | 0.144 | 0.05 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | 0.127 | 0.065 | 0.0509 | Wald ratio | 1 | cis | NA |
| _...and 81 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_3 association rows across 2 traits (3 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Immature fraction of reticulocytes | 3e-10 | rs10999573 | 1 | GCST004628 | no MR -> candidate analysis |
| Type 2 diabetes | 4e-10 | rs827237 | 2 | GCST010555 | MR: beta=0.269, p=0.109 (cis) |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 404 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Hyperphenylalaninemia | 0.907 | — | established (curated) | no MR -> candidate analysis |
| pterin-4 alpha-carbinolamine dehydratase 1 deficiency | 0.849 | — | established (curated) | no MR -> candidate analysis |
| Dehydratase deficiency | 0.608 | — | established (curated) | no MR -> candidate analysis |
| type 2 diabetes mellitus | 0.742 | — | common-variant locus | no MR -> candidate analysis |
| diabetes mellitus | 0.546 | — | common-variant locus | no MR -> candidate analysis |
| neuroendocrine neoplasm | 0.388 | — | common-variant locus | no MR -> candidate analysis |
| ovarian neoplasm | 0.388 | — | common-variant locus | no MR -> candidate analysis |
| placenta praevia | 0.378 | — | common-variant locus | no MR -> candidate analysis |
| amyotrophic lateral sclerosis | 0.36 | — | common-variant locus | no MR -> candidate analysis |
| digestive system disorder | 0.348 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.32 | — | common-variant locus | no MR -> candidate analysis |
| frozen shoulder | 0.306 | — | common-variant locus | no MR -> candidate analysis |
| urolithiasis | 0.306 | — | common-variant locus | no MR -> candidate analysis |
| hereditary disease | 0.285 | — | established (curated) | no MR -> candidate analysis |

> Of the 14 rows above, **14 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=3e-07, LOEUF=1.93 — LoF-tolerant |
| GWAS Catalog | 38 unique SNPs / 76 rows |
| ClinVar | 155 records; 7 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 404 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'PCBD1'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 155 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 2 of 2 traits by best p-value, aggregated from 3 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P61457 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000166228/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PCBD1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PCBD1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PCBD1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/PCBD1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:11:46  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
