# Protein Dossier — BPI (Bactericidal permeability-increasing protein)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Endometrioid ovarian cancer | -0.142 | 0.0671 | 0.0346 | Wald ratio | 1 | cis | NA |
| Clear cell ovarian cancer | -0.195 | 0.0935 | 0.0373 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: D25 Leiomyoma of uterus | -0.118 | 0.0572 | 0.0389 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N92 Excessive  frequent and irregular menstruation | -0.0903 | 0.0438 | 0.0393 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | -0.166 | 0.0813 | 0.0408 | Wald ratio | 1 | cis | NA |
| Thalamus volume | -29.1 | 14.4 | 0.0427 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: uterine fibroids | -0.104 | 0.0516 | 0.0436 | Wald ratio | 1 | cis | NA |
| Serum cystatin C (eGFRcys) | 0.00962 | 0.00497 | 0.0527 | Wald ratio | 1 | cis | NA |
| Caudate volume | 21.3 | 11.2 | 0.0568 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K60 Fissure and fistula of anal and rectal regions | 0.14 | 0.0743 | 0.0602 | Wald ratio | 1 | cis | NA |
| Systolic blood pressure  automated reading | -0.0108 | 0.00587 | 0.0653 | Wald ratio | 1 | cis | NA |
| Fasting proinsulin | -0.0341 | 0.0186 | 0.0668 | Wald ratio | 1 | cis | NA |
| _...and 85 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-4126_22_1` | BPI | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_55 association rows across 27 traits (50 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Bactericidal permeability-increasing protein levels | 5e-231 | rs6127742 | 8 | GCST90246731 | no MR -> candidate analysis |
| Serum levels of protein BPI | 4e-180 | rs1780617 | 4 | GCST90088584 | no MR -> candidate analysis |
| Blood protein levels | 9e-113 | rs1780617 | 3 | GCST006585 | no MR -> candidate analysis |
| Serum levels of protein MUL1 | 9e-98 | rs1780617 | 4 | GCST90090625 | no MR -> candidate analysis |
| Bactericidal permeability-increasing protein levels (BPI.412 | 1e-67 | rs1780617 | 3 | GCST90240373 | no MR -> candidate analysis |
| LBP protein levels | 2e-37 | rs1205422 | 4 | GCST90469743 | no MR -> candidate analysis |
| Lipopolysaccharide-binding protein levels | 3e-29 | rs2232575 | 2 | GCST90161628 | no MR -> candidate analysis |
| Mitochondrial ubiquitin ligase activator of NFKB 1 levels (M | 4e-26 | rs11086556 | 2 | GCST90241945 | no MR -> candidate analysis |
| RETN protein levels | 4e-25 | rs6069597 | 1 | GCST90470457 | no MR -> candidate analysis |
| Circulating RETN levels | 1e-19 | rs6064367 | 4 | GCST90859950 | no MR -> candidate analysis |
| Monocyte percentage (UKB data field 30190) | 3e-15 | rs6123584 | 1 | GCST90468091 | no MR -> candidate analysis |
| Monocyte percentage of white cells | 7e-15 | rs5743511 | 2 | GCST90002394 | no MR -> candidate analysis |
| _...and 15 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 281 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| retinal degeneration | 0.463 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.407 | — | common-variant locus | no MR -> candidate analysis |
| asthma | 0.395 | — | common-variant locus | no MR -> candidate analysis |
| acute tonsillitis | 0.395 | — | common-variant locus | no MR -> candidate analysis |

> Of the 4 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=3.4e-14, LOEUF=1.06 — LoF-tolerant |
| GWAS Catalog | 107 unique SNPs / 210 rows |
| ClinVar | 109 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 281 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'BPI'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 109 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 27 traits by best p-value, aggregated from 55 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P17213 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000101425/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/BPI — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/BPI — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=BPI%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/BPI — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:18:08  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
