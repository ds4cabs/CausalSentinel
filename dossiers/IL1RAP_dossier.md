# Protein Dossier — IL1RAP (Interleukin-1 receptor accessory protein)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: anxiety or panic attacks | 0.0918 | 0.0195 | 2.39e-06 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Ankle | 0.0567 | 0.02 | 0.00453 | Wald ratio | 1 | cis | NA |
| Age at menarche | -0.0141 | 0.00648 | 0.03 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypopituitarism | 0.223 | 0.109 | 0.0407 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: L03 Cellulitis | 0.0533 | 0.0262 | 0.0415 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K57 Diverticular disease of intestine | 0.0343 | 0.0168 | 0.0417 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I83 Varicose veins of lower extremities | 0.0333 | 0.0167 | 0.0464 | Wald ratio | 1 | cis | NA |
| Neo-extraversion | -0.16 | 0.0814 | 0.0486 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: J33 Nasal polyp | -0.076 | 0.0389 | 0.0505 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: S76 Injury of muscle and tendon at hip and thigh level | 0.192 | 0.0982 | 0.0508 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: H25 Senile cataract | -0.0584 | 0.03 | 0.0513 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: prostate cancer | 0.0534 | 0.0275 | 0.0522 | Wald ratio | 1 | cis | NA |
| _...and 94 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2630_12_2` | IL-1 R AcP | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_80 association rows across 29 traits (72 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Interleukin-1 Receptor accessory protein levels | 5e-2655 | rs7642797 | 18 | GCST90248049 | no MR -> candidate analysis |
| Interleukin-1 Receptor accessory protein levels (IL1RAP.2630 | 8e-720 | rs34908328 | 3 | GCST90241575 | no MR -> candidate analysis |
| Blood protein levels | 2e-567 | rs724609 | 2 | GCST006585 | no MR -> candidate analysis |
| Interleukin-1 Receptor accessory protein (analyte X14048.7)  | 4e-381 | rs6444442 | 1 | GCST90422429 | no MR -> candidate analysis |
| Interleukin-1 Receptor accessory protein (analyte X2630.12)  | 7e-369 | rs6444442 | 1 | GCST90425395 | no MR -> candidate analysis |
| IL1RAP protein levels | 1e-275 | rs11927365 | 24 | GCST90453382 | no MR -> candidate analysis |
| Cerebrospinal fluid protein IL1RAP levels | 2e-265 | rs6444442 | 1 | GCST90944794 | no MR -> candidate analysis |
| Serum levels of protein IL1RAP | 5e-203 | rs3796293 | 4 | GCST90087741 | no MR -> candidate analysis |
| Protein quantitative trait loci | 1e-119 | rs1024943 | 1 | GCST010900 | no MR -> candidate analysis |
| Protein levels in obesity | 5e-66 | rs6444444 | 1 | GCST010196 | no MR -> candidate analysis |
| Synaptotagmin-9 protein levels (SomaScan ID:14048-7) | 4e-32 | rs4686558 | 1 | GCST90443954 | no MR -> candidate analysis |
| Uncharacterized protein C21orf59 protein levels (SomaScan ID | 1e-31 | rs4686558 | 1 | GCST90443462 | no MR -> candidate analysis |
| _...and 17 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 288 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| response to antihypertensive drug | 0.428 | — | common-variant locus | no MR -> candidate analysis |
| diabetes mellitus | 0.407 | — | common-variant locus | no MR -> candidate analysis |
| pathological myopia | 0.182 | — | established (curated) | no MR -> candidate analysis |
| myopia | 0.182 | — | established (curated) | no MR -> candidate analysis |
| insomnia | 0.11 | — | common-variant locus | no MR -> candidate analysis |

> Of the 5 rows above, **5 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 1 known modulators (IL-33 receptor (ST2)) |
| gnomAD constraint | pLI=1.7e-06, LOEUF=0.764 — LoF-tolerant |
| GWAS Catalog | 74 unique SNPs / 148 rows |
| ClinVar | 107 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 288 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'IL1RAP' and resolved to 'IL-33 receptor (ST2)' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 107 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 29 traits by best p-value, aggregated from 80 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9NPH3 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000196083/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4804256/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/IL1RAP — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/IL1RAP — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=IL1RAP%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/IL1RAP — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:14:12  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
