# Protein Dossier — LRP11 (Low-density lipoprotein receptor-related protein 11)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Internalizing problems | 0.087 | 0.0275 | 0.00156 | Wald ratio | 1 | cis | NA |
| Pallidum volume | 7.21 | 2.34 | 0.00209 | Wald ratio | 1 | cis | NA |
| Potassium in urine | 0.00832 | 0.00303 | 0.00596 | Wald ratio | 1 | cis | NA |
| Hearing difficulty or problems: Yes | 0.0131 | 0.00508 | 0.0102 | Wald ratio | 1 | cis | NA |
| Mean cell haemoglobin concentration | -0.0112 | 0.00436 | 0.0106 | Wald ratio | 1 | cis | NA |
| Age at menarche | -0.0206 | 0.00839 | 0.014 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertension | -0.0118 | 0.00515 | 0.0215 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | 0.00875 | 0.00386 | 0.0234 | Wald ratio | 1 | cis | NA |
| Serum creatinine (eGFRcrea) | 0.00242 | 0.00112 | 0.0297 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: malignant melanoma | -0.0796 | 0.0367 | 0.03 | Wald ratio | 1 | cis | NA |
| Parkinson's disease | -0.109 | 0.0502 | 0.0302 | Wald ratio | 1 | cis | NA |
| Urate | 0.0158 | 0.00727 | 0.0303 | Wald ratio | 1 | cis | NA |
| _...and 106 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_33 association rows across 29 traits (31 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Low-density lipoprotein receptor-related protein 11 levels | 2e-1411 | rs9322225 | 1 | GCST90248262 | no MR -> candidate analysis |
| Circulating LRP11 levels | 4e-79 | rs142987810 | 1 | GCST90860386 | no MR -> candidate analysis |
| LRP11 protein levels | 4e-58 | rs142987810 | 4 | GCST90469796 | no MR -> candidate analysis |
| Brain morphology (MOSTest) | 2e-31 | rs7752089 | 1 | GCST90239729 | no MR -> candidate analysis |
| Low-density lipoprotein receptor-related protein 11 (analyte | 4e-23 | rs1889471 | 1 | GCST90422684 | no MR -> candidate analysis |
| Macular thickness | 3e-19 | rs14314 | 1 | GCST006976 | no MR -> candidate analysis |
| 5-methylthioadenosine (mta) levels | 3e-18 | rs869109015 | 1 | GCST90139562 | no MR -> candidate analysis |
| Vertex-wise sulcal depth | 7e-17 | rs14314 | 1 | GCST90095129 | no MR -> candidate analysis |
| Cerebrospinal fluid 5-methylthioadenosine (MTA) levels | 4e-16 | rs1889473 | 1 | GCST90318216 | no MR -> candidate analysis |
| Plasma S-adenosylhomocysteine (SAH) levels in chronic kidney | 4e-16 | rs14314 | 1 | GCST90265918 | no MR -> candidate analysis |
| Inosine triphosphate pyrophosphatase protein levels (SomaSca | 2e-15 | rs1889473 | 1 | GCST90438881 | no MR -> candidate analysis |
| Left hippocampal volume (body) | 7e-15 | rs14314 | 1 | GCST90267904 | no MR -> candidate analysis |
| _...and 17 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 129 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| mixed connective tissue disease | 0.391 | — | common-variant locus | no MR -> candidate analysis |
| testicular germ cell tumor | 0.198 | — | common-variant locus | no MR -> candidate analysis |
| migraine disorder | 0.16 | — | common-variant locus | no MR -> candidate analysis |
| binge eating disorder | 0.15 | — | common-variant locus | no MR -> candidate analysis |
| hypertrophic cardiomyopathy | 0.151 | — | common-variant locus | no MR -> candidate analysis |

> Of the 5 rows above, **5 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=5.3e-05, LOEUF=0.811 — LoF-tolerant |
| GWAS Catalog | 86 unique SNPs / 172 rows |
| ClinVar | 93 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 129 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'LRP11'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 93 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 29 traits by best p-value, aggregated from 33 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q86VZ4 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000120256/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/LRP11 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/LRP11 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=LRP11%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/LRP11 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:37:12  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
