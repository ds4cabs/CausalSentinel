# Protein Dossier — CFI (Complement factor I)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Amyotrophic lateral sclerosis | -0.161 | 0.0574 | 0.00513 | Wald ratio | 1 | cis | NA |
| Birth weight | -0.0331 | 0.0122 | 0.00672 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hiatus hernia | -0.15 | 0.0603 | 0.0131 | Wald ratio | 1 | cis | NA |
| Fractured or broken bones in last 5 years | 0.0484 | 0.0234 | 0.0387 | Wald ratio | 1 | cis | NA |
| Invasive mucinous ovarian cancer | -0.262 | 0.129 | 0.0425 | Wald ratio | 1 | cis | NA |
| Thalamus volume | -40.8 | 20.3 | 0.0445 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Other bones | 0.0633 | 0.0322 | 0.0494 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I80 Phlebitis and thrombophlebitis | 0.188 | 0.0966 | 0.0514 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R11 Nausea and vomiting | 0.201 | 0.104 | 0.0529 | Wald ratio | 1 | cis | NA |
| Pancreatic cancer | -0.301 | 0.157 | 0.0546 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: uterine fibroids | 0.11 | 0.0572 | 0.0557 | Wald ratio | 1 | cis | NA |
| Red blood cell count | -0.0132 | 0.00706 | 0.0624 | Wald ratio | 1 | cis | NA |
| _...and 98 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2567_5_6` | Factor I | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_44 association rows across 30 traits (39 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| CFI protein levels | 4e-210 | rs10033900 | 4 | GCST90468730 | no MR -> candidate analysis |
| Complement factor I levels | 7e-85 | rs7439493 | 6 | GCST90246997 | no MR -> candidate analysis |
| Serum levels of protein CFI | 8e-54 | rs10033900 | 1 | GCST90087960 | no MR -> candidate analysis |
| Complement factor I levels (CFI.2567.5.6) | 9e-37 | rs7439493 | 1 | GCST90240782 | no MR -> candidate analysis |
| Circulating complement factor I levels | 9e-37 | rs7439493 | 1 | GCST90105032 | no MR -> candidate analysis |
| Blood protein levels | 4e-34 | rs10033900 | 1 | GCST006585 | no MR -> candidate analysis |
| Atrial fibrillation | 5e-27 | rs186391417 | 2 | GCST90624412 | MR: beta=0.0729, p=0.296 (cis) |
| Macular degeneration, dry (PheCode 362.21) | 9e-27 | rs141853578 | 2 | GCST90480043 | no MR -> candidate analysis |
| Degeneration of macula and posterior pole of retina (PheCode | 1e-18 | rs141853578 | 2 | GCST90475849 | no MR -> candidate analysis |
| Age-related macular degeneration or COVID-19 infection (MTAG | 2e-18 | rs10033900 | 1 | GCST90250834 | no MR -> candidate analysis |
| Age-related macular degeneration or COVID-19 hospitalization | 3e-18 | rs10033900 | 1 | GCST90250833 | no MR -> candidate analysis |
| Age-related macular degeneration or COVID-19 critical illnes | 4e-18 | rs10033900 | 1 | GCST90250832 | no MR -> candidate analysis |
| _...and 18 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 435 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| complement factor I deficiency | 0.866 | — | established (curated) | no MR -> candidate analysis |
| atypical hemolytic-uremic syndrome with I factor anomaly | 0.937 | — | established (curated) | no MR -> candidate analysis |
| age-related macular degeneration | 0.803 | 0.241 | established (curated) | no MR -> candidate analysis |
| atypical hemolytic-uremic syndrome | 0.895 | — | established (curated) | no MR -> candidate analysis |
| macular degeneration | 0.931 | — | common-variant locus | no MR -> candidate analysis |
| retinal disorder | 0.733 | 0.193 | multi-layer: burden+GWAS (allelic-series candidate) | no MR -> candidate analysis |
| degeneration of macula and posterior pole | 0.673 | 0.193 | multi-layer: burden+GWAS (allelic-series candidate) | no MR -> candidate analysis |
| COVID-19 | 0.778 | — | common-variant locus | no MR -> candidate analysis |
| wet macular degeneration | 0.749 | — | common-variant locus | no MR -> candidate analysis |
| dry age related macular degeneration | 0.609 | — | common-variant locus | no MR -> candidate analysis |
| atypical hemolytic uremic syndrome with complement gene abnormality | 0.608 | — | established (curated) | no MR -> candidate analysis |
| Familial drusen | 0.608 | — | established (curated) | no MR -> candidate analysis |
| atrophic macular degeneration | 0.572 | — | common-variant locus | no MR -> candidate analysis |
| peroxisome biogenesis disorder 4A (Zellweger) | 0.438 | — | established (curated) | no MR -> candidate analysis |
| C3 glomerulonephritis | 0.297 | — | established (curated) | no MR -> candidate analysis |

> Of the 15 rows above, **15 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 2 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=3.4e-19, LOEUF=1.03 — LoF-tolerant |
| GWAS Catalog | 36 unique SNPs / 72 rows |
| ClinVar | 851 records; 5 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 435 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'CFI'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 851 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 30 traits by best p-value, aggregated from 44 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P05156 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000205403/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CFI — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CFI — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CFI%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CFI — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:48:49  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
