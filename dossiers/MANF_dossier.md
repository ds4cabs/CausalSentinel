# Protein Dossier — MANF (Mesencephalic astrocyte-derived neurotrophic factor)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Height | -0.0563 | 0.0107 | 1.62e-07 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | 0.0372 | 0.00864 | 1.64e-05 | Wald ratio | 1 | cis | NA |
| Fracture resulting from simple fall | -0.0854 | 0.0248 | 5.81e-04 | Wald ratio | 1 | cis | NA |
| Parkinson's disease | -0.529 | 0.154 | 5.83e-04 | Wald ratio | 1 | cis | NA |
| Hip osteoarthritis | -0.313 | 0.0979 | 0.00141 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hayfever or allergic rhinitis | 0.0947 | 0.0324 | 0.00342 | Wald ratio | 1 | cis | NA |
| Age at menarche | -0.0614 | 0.0211 | 0.0036 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: D12 Benign neoplasm of colon  rectum  anus and anal canal | 0.148 | 0.0632 | 0.0189 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: Z09 Follow-up examination after treatment for conditions other than malignant neoplasms | 0.143 | 0.0612 | 0.0192 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R04 Haemorrhage from respiratory passages | 0.223 | 0.0971 | 0.0214 | Wald ratio | 1 | cis | NA |
| Invasive mucinous ovarian cancer | 0.337 | 0.149 | 0.0237 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: G56 Mononeuropathies of upper limb | -0.176 | 0.0789 | 0.026 | Wald ratio | 1 | cis | NA |
| _...and 111 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_No GWAS Catalog associations mapped to this gene._

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 460 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| diabetes, deafness, developmental delay, and short stature syndrome | 0.733 | — | established (curated) | no MR -> candidate analysis |
| Abnormality of the skeletal system | 0.73 | — | common-variant locus | no MR -> candidate analysis |
| Cerebro-costo-mandibular syndrome | 0.486 | — | established (curated) | no MR -> candidate analysis |
| smoking behavior | 0.285 | — | common-variant locus | no MR -> candidate analysis |
| obesity disorder | 0.196 | — | common-variant locus | no MR -> candidate analysis |
| major depressive disorder | 0.181 | — | common-variant locus | MR: beta=0.0731, p=0.349 (cis) |
| Alzheimer disease | 0.079 | — | common-variant locus | no MR -> candidate analysis |
| asthma | 0.185 | — | common-variant locus | MR: beta=0.0305, p=0.195 (cis) |
| dysthymic disorder | 0.181 | — | common-variant locus | no MR -> candidate analysis |
| stroke disorder | 0.042 | — | common-variant locus | no MR -> candidate analysis |
| liver disorder | 0.154 | — | common-variant locus | no MR -> candidate analysis |
| multinodular goiter | 0.154 | — | common-variant locus | no MR -> candidate analysis |

> Of the 12 rows above, **10 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.1, LOEUF=0.822 — LoF-tolerant |
| GWAS Catalog | 107 unique SNPs / 252 rows |
| ClinVar | 50 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 460 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'MANF'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 50 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — No GWAS Catalog associations mapped to this gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P55145 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000145050/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/MANF — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/MANF — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=MANF%5Bgene%5D — _ClinVar build Build260809-1055.1_

## Provenance

- Generated: 2026-08-14T03:42:38  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
