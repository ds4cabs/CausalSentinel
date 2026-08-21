# Protein Dossier — CD177 (CD177 antigen)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: diverticular disease or diverticulitis | 0.133 | 0.0457 | 0.00349 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: gout | -0.123 | 0.0524 | 0.0185 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: D25 Leiomyoma of uterus | -0.119 | 0.055 | 0.0297 | Wald ratio | 1 | cis | NA |
| Lung adenocarcinoma | -0.0941 | 0.0435 | 0.0305 | Wald ratio | 1 | cis | NA |
| Pulse rate | -0.0199 | 0.00962 | 0.0389 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Glaucoma | -0.101 | 0.0506 | 0.0455 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hayfever or allergic rhinitis | -0.0471 | 0.0238 | 0.0475 | Wald ratio | 1 | cis | NA |
| Invasive mucinous ovarian cancer | -0.172 | 0.0874 | 0.0485 | Wald ratio | 1 | cis | NA |
| Endometrioid ovarian cancer | -0.122 | 0.0644 | 0.0583 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | -0.0135 | 0.00713 | 0.0585 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Arm | -0.117 | 0.0626 | 0.0624 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: vitiligo | 0.428 | 0.232 | 0.0642 | Wald ratio | 1 | cis | NA |
| _...and 63 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_38 association rows across 15 traits (36 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating CD177 levels | 9e-265 | rs1806750 | 2 | GCST90860625 | no MR -> candidate analysis |
| CD177 antigen levels | 1e-154 | rs11671567 | 10 | GCST90246932 | no MR -> candidate analysis |
| CD177 protein levels | 3e-72 | rs150484653 | 4 | GCST90468603 | no MR -> candidate analysis |
| TNFRSF10C protein levels | 7e-67 | rs3816437 | 2 | GCST90470901 | no MR -> candidate analysis |
| CD177 antigen levels (CD177.13116.25.3) | 2e-65 | rs587670082 | 4 | GCST90240637 | no MR -> candidate analysis |
| PSG1 protein levels | 2e-59 | rs118164011 | 2 | GCST90470353 | no MR -> candidate analysis |
| Serum levels of protein CD177 | 2e-52 | rs28464741 | 5 | GCST90087384 | no MR -> candidate analysis |
| CEACAM21 protein levels | 5e-20 | rs77513223 | 1 | GCST90468694 | no MR -> candidate analysis |
| PLAU protein levels | 2e-16 | rs3816437 | 1 | GCST90470252 | no MR -> candidate analysis |
| TNFSF10 protein levels | 2e-15 | rs28464741 | 1 | GCST90470917 | no MR -> candidate analysis |
| PINLYP protein levels | 2e-13 | rs367925083 | 2 | GCST90470238 | no MR -> candidate analysis |
| Serum levels of protein PCDHGA1 | 4e-11 | rs12975477 | 1 | GCST90089439 | no MR -> candidate analysis |
| _...and 3 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=2e-15, LOEUF=1.39 — LoF-tolerant |
| GWAS Catalog | 129 unique SNPs / 312 rows |
| ClinVar | 111 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 749 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'CD177'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 111 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 15 of 15 traits by best p-value, aggregated from 38 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q8N6Q3 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000204936/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CD177 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CD177 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CD177%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CD177 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:40:55  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
