# Protein Dossier — TMEM132A (Transmembrane protein 132A)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Type 2 diabetes | -0.0479 | 0.02 | 0.0165 | Wald ratio | 1 | cis | NA |
| Diastolic blood pressure  automated reading | -0.0111 | 0.00469 | 0.0186 | Wald ratio | 1 | cis | NA |
| Systolic blood pressure  automated reading | -0.0108 | 0.00469 | 0.0211 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M16 Coxarthrosis [arthrosis of hip] | -0.0971 | 0.0421 | 0.0212 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K57 Diverticular disease of intestine | -0.074 | 0.0348 | 0.0333 | Wald ratio | 1 | cis | NA |
| High grade serous ovarian cancer | -0.0644 | 0.0306 | 0.0355 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R04 Haemorrhage from respiratory passages | -0.157 | 0.075 | 0.036 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: anxiety or panic attacks | -0.0888 | 0.0432 | 0.04 | Wald ratio | 1 | cis | NA |
| Ovarian cancer | -0.0509 | 0.0257 | 0.0479 | Wald ratio | 1 | cis | NA |
| Nucleus accumbens volume | -4.06 | 2.06 | 0.0487 | Wald ratio | 1 | cis | NA |
| Internalizing problems | -0.0839 | 0.0429 | 0.0506 | Wald ratio | 1 | cis | NA |
| Endometrioid ovarian cancer | -0.104 | 0.056 | 0.0624 | Wald ratio | 1 | cis | NA |
| _...and 93 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_28 association rows across 14 traits (28 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Transmembrane protein 132A levels (TMEM132A.7871.16.3) | 2e-112 | rs11230521 | 1 | GCST90243088 | no MR -> candidate analysis |
| Serum levels of protein TMEM132A | 2e-112 | rs55920775 | 1 | GCST90089891 | no MR -> candidate analysis |
| TMEM132A protein levels | 2e-41 | rs61745629 | 4 | GCST90470887 | no MR -> candidate analysis |
| Transmembrane protein 132A levels | 3e-34 | rs55920775 | 1 | GCST90427121 | no MR -> candidate analysis |
| SLIT-ROBO Rho GTPase-activating protein 2 levels | 1e-24 | rs11230522 | 1 | GCST90425196 | no MR -> candidate analysis |
| Transmembrane protein 132A level in Chronic kidney disease w | 5e-20 | rs524523 | 1 | GCST90238680 | no MR -> candidate analysis |
| DnaJ homolog subfamily C member 30 levels | 2e-18 | rs11230521 | 1 | GCST90427118 | no MR -> candidate analysis |
| Omega-3 fatty acids to total fatty acids percentage | 3e-14 | rs61745629 | 5 | GCST90502082 | no MR -> candidate analysis |
| Degree of unsaturation | 1e-13 | rs61745629 | 3 | GCST90502225 | no MR -> candidate analysis |
| Omega-3 fatty acids to Omega-6 fatty acids ratio | 3e-11 | rs61745629 | 4 | GCST90502069 | no MR -> candidate analysis |
| Omega-3 fatty acid levels | 8e-11 | rs61745629 | 2 | GCST90502064 | no MR -> candidate analysis |
| Docosahexaenoic acid levels | 8e-10 | rs61745629 | 1 | GCST90502243 | no MR -> candidate analysis |
| _...and 2 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1.9e-11, LOEUF=0.874 — LoF-tolerant |
| GWAS Catalog | 94 unique SNPs / 188 rows |
| ClinVar | 218 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 543 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'TMEM132A'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 218 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 14 of 14 traits by best p-value, aggregated from 28 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q24JP5 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000006118/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/TMEM132A — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/TMEM132A — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=TMEM132A%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/TMEM132A — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:23:18  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
