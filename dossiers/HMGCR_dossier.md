# Protein Dossier — HMGCR (3-hydroxy-3-methylglutaryl-coenzyme A reductase)

**MR feasibility tier: B** — No published MR estimate in this resource, BUT a pQTL GWAS exists - instruments are derivable, so a two-sample MR could be run. The upstream is waiting.

## 1. Published MR estimates (retrieved, not computed)

_None in the EpiGraphDB pQTL resource. Absence of an estimate is not evidence of no effect._

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-5230_99_3` | HMGR | Suhre K | 2019 |

> Instruments exist but no MR estimate is in this resource — **a two-sample MR here is un-run work.**

## 3. GWAS Catalog results — traits with signal at this locus

_855 association rows across 463 traits (831 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Low density lipoprotein cholesterol levels | 1e-602 | rs12916 | 46 | GCST90239655 | no MR -> candidate analysis |
| Total cholesterol levels | 2e-546 | rs12916 | 51 | GCST90239673 | no MR -> candidate analysis |
| Low-density lipoprotein levels | 8e-401 | rs10942734 | 1 | GCST90662892 | no MR -> candidate analysis |
| Non-HDL cholesterol levels | 2e-399 | rs12916 | 5 | GCST90239667 | no MR -> candidate analysis |
| LDL cholesterol levels | 2e-187 | rs12916 | 13 | GCST010245 | no MR -> candidate analysis |
| Direct low density lipoprotein levels (UKB data field 30780) | 5e-176 | rs12916 | 1 | GCST90468080 | no MR -> candidate analysis |
| LDL cholesterol | 5e-173 | rs12916 | 11 | GCST90018961 | no MR -> candidate analysis |
| Cholesterol levels (UKB data field 30690) | 9e-165 | rs12916 | 1 | GCST90468066 | no MR -> candidate analysis |
| low density lipoprotein cholesterol (LDLC, maximum, inv-norm | 2e-164 | rs12916 | 3 | GCST90475412 | no MR -> candidate analysis |
| low density lipoprotein cholesterol (LDLC, mean, inv-norm tr | 2e-160 | rs12916 | 3 | GCST90475416 | no MR -> candidate analysis |
| total cholesterol (mean, inv-norm transformed) | 8e-155 | rs12916 | 3 | GCST90476424 | no MR -> candidate analysis |
| total cholesterol (maximum, inv-norm transformed) | 6e-150 | rs12916 | 3 | GCST90476420 | no MR -> candidate analysis |
| _...and 451 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1080 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Hypercholesterolemia | 0.857 | — | common-variant locus | no MR -> candidate analysis |
| hyperlipidemia | 0.822 | — | common-variant locus | no MR -> candidate analysis |
| coronary artery disorder | 0.687 | — | common-variant locus | no MR -> candidate analysis |
| familial hypercholesterolemia | 0.616 | — | common-variant locus | no MR -> candidate analysis |
| stroke disorder | 0.481 | — | common-variant locus | no MR -> candidate analysis |
| cardiovascular disorder | 0.462 | — | common-variant locus | no MR -> candidate analysis |
| muscular dystrophy, limb-girdle, autosomal recessive 28 | 0.795 | — | established (curated) | no MR -> candidate analysis |
| type 2 diabetes mellitus | 0.44 | — | common-variant locus | no MR -> candidate analysis |
| familial hyperlipidemia | 0.674 | — | common-variant locus | no MR -> candidate analysis |
| metabolic disease | 0.855 | — | common-variant locus | no MR -> candidate analysis |
| metabolic syndrome | 0.69 | — | common-variant locus | no MR -> candidate analysis |
| Disorder of lipid metabolism | 0.605 | — | common-variant locus | no MR -> candidate analysis |
| diabetes mellitus | 0.516 | — | common-variant locus | no MR -> candidate analysis |

> Of the 13 rows above, **13 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 10 known modulators (3-hydroxy-3-methylglutaryl-coenzyme A reductase) |
| gnomAD constraint | pLI=1, LOEUF=0.433 — LoF-INTOLERANT |
| GWAS Catalog | 92 unique SNPs / 177 rows |
| ClinVar | 112 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 10 clinical annotations across 6 drugs |

## Caveats declared by the tools

- **`mr_outcomes`** — No pQTL MR estimates for HMGCR in this resource. ABSENCE OF AN ESTIMATE IS NOT EVIDENCE OF NO EFFECT.
- **`phenome`** — Top 30 of 1080 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'HMGCR' and resolved to '3-hydroxy-3-methylglutaryl-coenzyme A reductase' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 112 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 20 of 463 traits by best p-value, aggregated from 855 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P04035 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000113161/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL402/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/HMGCR — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/HMGCR — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=HMGCR%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=HMGCR — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/HMGCR — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T00:48:03  ·  Tier: B
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
