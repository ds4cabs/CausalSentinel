# Protein Dossier — LECT2 (Leukocyte cell-derived chemotaxin-2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Cancer code  self-reported: basal cell carcinoma | 0.199 | 0.0684 | 0.00362 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Wrist | -0.189 | 0.069 | 0.00621 | Wald ratio | 1 | cis | NA |
| Fractured or broken bones in last 5 years | -0.0702 | 0.0266 | 0.00846 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: iron deficiency anaemia | 0.223 | 0.0881 | 0.0115 | Wald ratio | 1 | cis | NA |
| Endometrioid ovarian cancer | 0.207 | 0.0948 | 0.0289 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: depression | -0.0759 | 0.0354 | 0.0321 | Wald ratio | 1 | cis | NA |
| Pancreatic cancer | -0.335 | 0.159 | 0.0346 | Wald ratio | 1 | cis | NA |
| Transferrin | 0.0699 | 0.0337 | 0.0379 | Wald ratio | 1 | cis | NA |
| Age at menarche | 0.0385 | 0.0185 | 0.038 | Wald ratio | 1 | cis | NA |
| ER-positive Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | 0.0513 | 0.025 | 0.0402 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: mania or bipolar disorder or manic depression | 0.251 | 0.124 | 0.0419 | Wald ratio | 1 | cis | NA |
| HOMA-B | -0.0215 | 0.0106 | 0.0423 | Wald ratio | 1 | cis | NA |
| _...and 104 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_58 association rows across 28 traits (56 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Leukocyte cell-derived chemotaxin-2 levels | 2e-842 | rs2428665 | 2 | GCST90248271 | no MR -> candidate analysis |
| Cerebrospinal fluid protein LECT2 levels | 8e-392 | rs31517 | 1 | GCST90944392 | no MR -> candidate analysis |
| LECT2 protein levels | 1e-119 | rs114094505 | 22 | GCST90469751 | no MR -> candidate analysis |
| Leukocyte cell-derived chemotaxin-2 (analyte X16763.11) leve | 2e-116 | rs31517 | 1 | GCST90422856 | no MR -> candidate analysis |
| Interleukin-9 levels | 5e-114 | rs31517 | 1 | GCST90426521 | no MR -> candidate analysis |
| Serum levels of protein LECT2 | 7e-55 | rs2526145 | 1 | GCST90089250 | no MR -> candidate analysis |
| TGFBI protein levels | 2e-36 | rs145349976 | 4 | GCST90470845 | no MR -> candidate analysis |
| Blood protein levels | 4e-33 | rs248160 | 1 | GCST006585 | no MR -> candidate analysis |
| Height | 5e-29 | rs2428158 | 2 | GCST90245848 | MR: beta=0.0131, p=0.172 (cis) |
| RILP-like protein 2 protein levels (SomaScan ID:16763-11) | 5e-21 | rs2428665 | 1 | GCST90443757 | no MR -> candidate analysis |
| Transforming growth factor-beta-induced protein ig-h3 levels | 3e-14 | rs7728408 | 3 | GCST90161688 | no MR -> candidate analysis |
| Leukocyte cell-derived chemotaxin-2 level in Chronic kidney  | 3e-14 | rs2428665 | 1 | GCST90234562 | no MR -> candidate analysis |
| _...and 16 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.0026, LOEUF=1.09 — LoF-tolerant |
| GWAS Catalog | 85 unique SNPs / 157 rows |
| ClinVar | 38 records; 6 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 169 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'LECT2'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 38 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 28 traits by best p-value, aggregated from 58 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O14960 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000145826/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/LECT2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/LECT2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=LECT2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/LECT2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:29:34  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
