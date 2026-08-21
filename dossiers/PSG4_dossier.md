# Protein Dossier — PSG4 (Pregnancy-specific beta-1-glycoprotein 4)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Clear cell ovarian cancer | -0.226 | 0.0681 | 8.95e-04 | Wald ratio | 1 | cis | NA |
| Eczema | 0.0801 | 0.0302 | 0.00792 | Wald ratio | 1 | cis | NA |
| Age at menopause | -0.0601 | 0.03 | 0.0455 | Wald ratio | 1 | cis | NA |
| Percent emphysema | -0.0324 | 0.0171 | 0.0581 | Wald ratio | 1 | cis | NA |
| HbA1C | -0.00916 | 0.00541 | 0.0902 | Wald ratio | 1 | cis | NA |
| Myocardial infarction | -0.0273 | 0.0167 | 0.103 | Wald ratio | 1 | cis | NA |
| Bulimia nervosa | 0.0676 | 0.0435 | 0.121 | Wald ratio | 1 | cis | NA |
| Subjective well being | 0.00901 | 0.00601 | 0.134 | Wald ratio | 1 | cis | NA |
| Years of schooling | 0.00901 | 0.00601 | 0.134 | Wald ratio | 1 | cis | NA |
| Caudate volume | 9.72 | 7.61 | 0.202 | Wald ratio | 1 | cis | NA |
| Age at menarche | 0.011 | 0.00994 | 0.27 | Wald ratio | 1 | cis | NA |
| Fasting glucose | 0.00541 | 0.00495 | 0.275 | Wald ratio | 1 | cis | NA |
| _...and 18 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_55 association rows across 15 traits (14 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Pregnancy-specific beta-1-glycoprotein 4 levels | 2e-800 | rs12978398 | 2 | GCST90249150 | no MR -> candidate analysis |
| Pregnancy-specific beta-1-glycoprotein 4 levels (PSG4.5649.8 | 5e-163 | rs1138888 | 1 | GCST90242344 | no MR -> candidate analysis |
| Serum levels of protein PSG3 | 2e-121 | rs7249791 | 1 | GCST90089430 | no MR -> candidate analysis |
| Pregnancy-specific beta-1-glycoprotein 3 levels (PSG3.6444.1 | 1e-119 | rs35269301 | 1 | GCST90242343 | no MR -> candidate analysis |
| Protocadherin gamma-A1 levels | 2e-55 | rs59398928 | 1 | GCST90248885 | no MR -> candidate analysis |
| GLIPR1 protein levels | 8e-20 | rs572506627 | 1 | GCST90469357 | no MR -> candidate analysis |
| Pregnancy-specific beta-1-glycoprotein 3 level in Chronic ki | 6e-18 | rs1138888 | 1 | GCST90238277 | no MR -> candidate analysis |
| Pregnancy-specific beta-1-glycoprotein 9 levels (PSG9.9335.2 | 1e-15 | rs35143187 | 1 | GCST90242348 | no MR -> candidate analysis |
| Circulating PLAU levels (id: OID00481_OID21124) | 8e-15 | rs540797082 | 1 | GCST90859841 | no MR -> candidate analysis |
| Circulating PLAUR levels | 3e-14 | rs540797082 | 1 | GCST90859965 | no MR -> candidate analysis |
| Circulating PLAU levels (id: OID00631_OID21124) | 7e-14 | rs540797082 | 1 | GCST90859976 | no MR -> candidate analysis |
| Pregnancy-specific beta-1-glycoprotein 4 level in Chronic ki | 8e-14 | rs4802157 | 1 | GCST90238011 | no MR -> candidate analysis |
| _...and 3 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=6.5e-27, LOEUF=1.7 — LoF-tolerant |
| GWAS Catalog | 144 unique SNPs / 347 rows |
| ClinVar | 157 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 84 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'PSG4'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 157 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 15 of 15 traits by best p-value, aggregated from 55 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q00888 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000243137/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PSG4 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PSG4 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PSG4%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/PSG4 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:39:50  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
