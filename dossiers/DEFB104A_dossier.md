# Protein Dossier — DEFB104A (Beta-defensin 104)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Endometrioid ovarian cancer | 0.481 | 0.274 | 0.0797 | Wald ratio | 1 | cis | NA |
| Neuroticism | -0.0416 | 0.0297 | 0.162 | Wald ratio | 1 | cis | NA |
| Ovarian cancer | 0.15 | 0.132 | 0.257 | Wald ratio | 1 | cis | NA |
| Low grade serous ovarian cancer | 0.506 | 0.454 | 0.264 | Wald ratio | 1 | cis | NA |
| Forearm bone mineral density | -0.138 | 0.126 | 0.271 | Wald ratio | 1 | cis | NA |
| Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | 0.0714 | 0.0658 | 0.278 | Wald ratio | 1 | cis | NA |
| Invasive mucinous ovarian cancer | 0.366 | 0.388 | 0.346 | Wald ratio | 1 | cis | NA |
| Eczema | -1.76 | 2.18 | 0.419 | Wald ratio | 1 | cis | NA |
| Femoral neck bone mineral density | -0.0451 | 0.0639 | 0.48 | Wald ratio | 1 | cis | NA |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_1 association rows across 1 traits (1 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Creatinine levels in top 1% of individuals by creatinine lev | 1e-8 | rs529832206 | 1 | GCST90566751 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=NA, LOEUF=NA — Constraint metrics missing; LoF tolerance cannot be judged. |
| GWAS Catalog | 4 unique SNPs / 8 rows |
| ClinVar | 212 records; 17 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 1 of 1 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'DEFB104A'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 212 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 1 of 1 traits by best p-value, aggregated from 1 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q8WTQ1 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000177023/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/DEFB104A — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/DEFB104A — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=DEFB104A%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/DEFB104A — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:15:35  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
