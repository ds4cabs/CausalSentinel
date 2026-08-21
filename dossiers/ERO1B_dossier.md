# Protein Dossier — ERO1B (ERO1-like protein beta)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Age at menopause | 0.183 | 0.0523 | 4.65e-04 | Wald ratio | 1 | cis | NA |
| Serum creatinine (eGFRcrea) | 0.00628 | 0.00241 | 0.00909 | Wald ratio | 1 | cis | NA |
| Gallbladder cancer | -1.89 | 0.782 | 0.0157 | Wald ratio | 1 | cis | NA |
| Neuroblastoma | -0.271 | 0.113 | 0.0166 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | -0.0117 | 0.00501 | 0.0198 | Inverse variance weighted | 2 | trans | NA |
| Forced expiratory volume in 1-second (FEV1) | -0.0117 | 0.00501 | 0.0198 | Inverse variance weighted | 2 | cis | NA |
| Neo-neuroticism | -0.593 | 0.258 | 0.0214 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: anxiety or panic attacks | -0.156 | 0.0713 | 0.0282 | Inverse variance weighted | 2 | trans | NA |
| Non-cancer illness code  self-reported: anxiety or panic attacks | -0.156 | 0.0713 | 0.0282 | Inverse variance weighted | 2 | cis | NA |
| Schizophrenia | 0.0546 | 0.0261 | 0.0363 | Inverse variance weighted | 2 | trans | NA |
| Schizophrenia | 0.0546 | 0.0261 | 0.0363 | Inverse variance weighted | 2 | cis | NA |
| Years of schooling | -0.0209 | 0.0105 | 0.0455 | Wald ratio | 1 | cis | NA |
| _...and 149 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_24 association rows across 20 traits (17 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| ERO1-like protein beta levels | 2e-151 | rs1749555 | 2 | GCST90427195 | no MR -> candidate analysis |
| Serum levels of protein ERO1B | 1e-69 | rs1726631 | 1 | GCST90089971 | no MR -> candidate analysis |
| ERO1-like protein beta levels (ERO1LB.7994.41.3) | 2e-56 | rs1254194 | 1 | GCST90241103 | no MR -> candidate analysis |
| Blood protein levels | 9e-37 | rs1726625 | 1 | GCST006585 | no MR -> candidate analysis |
| Apoptosis-inducing factor 1, mitochondrial levels | 2e-22 | rs1621565 | 1 | GCST90427838 | no MR -> candidate analysis |
| LPO protein levels | 5e-12 | rs6696318 | 1 | GCST90469789 | no MR -> candidate analysis |
| Thyroid-stimulating hormone levels | 2e-10 | rs12563092 | 1 | GCST90662868 | no MR -> candidate analysis |
| Vertex-wise cortical surface area | 5e-9 | rs2449 | 1 | GCST90095130 | no MR -> candidate analysis |
| Type 2 diabetes | 1e-8 | rs1726669 | 3 | GCST90492734 | MR: beta=0.0638, p=0.41 (trans) |
| Fasting blood glucose | 2e-8 | rs1254194 | 1 | GCST90662896 | no MR -> candidate analysis |
| Cortical surface area | 2e-8 | rs2449 | 1 | GCST90091060 | no MR -> candidate analysis |
| Sib-shared facial trait 1030; Facial segment 62; 3D morpholo | 2e-8 | rs2141128 | 1 | GCST90016543 | no MR -> candidate analysis |
| _...and 8 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 110 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| type 2 diabetes mellitus | 0.456 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.421 | — | common-variant locus | no MR -> candidate analysis |
| urolithiasis | 0.421 | — | common-variant locus | no MR -> candidate analysis |
| ovarian dysfunction | 0.379 | — | common-variant locus | no MR -> candidate analysis |
| Developmental cataract | 0.195 | — | established (curated) | no MR -> candidate analysis |
| Abnormal nasolacrimal system morphology | 0.154 | — | common-variant locus | no MR -> candidate analysis |
| hypothyroidism | 0.076 | — | common-variant locus | no MR -> candidate analysis |
| aging | 0.068 | — | common-variant locus | no MR -> candidate analysis |

> Of the 8 rows above, **8 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=8.4e-11, LOEUF=0.826 — LoF-tolerant |
| GWAS Catalog | 65 unique SNPs / 116 rows |
| ClinVar | 167 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 110 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'ERO1B'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 167 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 20 traits by best p-value, aggregated from 24 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q86YB8 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000086619/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/ERO1B — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/ERO1B — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=ERO1B%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/ERO1B — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:29:02  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
