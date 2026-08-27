# Protein Dossier — PDGFRA (Platelet-derived growth factor receptor alpha)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: I83 Varicose veins of lower extremities | 0.118 | 0.0284 | 3.22e-05 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: M16 Coxarthrosis [arthrosis of hip] | 0.0954 | 0.0346 | 0.00584 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: deep venous thrombosis (dvt) | 0.0728 | 0.0301 | 0.0158 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: N81 Female genital prolapse | 0.0822 | 0.0352 | 0.0195 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: R14 Flatulence and related conditions | 0.313 | 0.142 | 0.0278 | Wald ratio | 1 | trans | NA |
| Creatinine (enzymatic) in urine | 0.00925 | 0.00438 | 0.0345 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: R55 Syncope and collapse | -0.111 | 0.0543 | 0.041 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: K57 Diverticular disease of intestine | -0.0703 | 0.0345 | 0.0416 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: osteoporosis | 0.0689 | 0.0343 | 0.0444 | Wald ratio | 1 | trans | NA |
| Diastolic blood pressure  automated reading | 0.00941 | 0.0047 | 0.0454 | Wald ratio | 1 | trans | NA |
| Fracture resulting from simple fall | 0.023 | 0.0117 | 0.0504 | Wald ratio | 1 | trans | NA |
| Coronary heart disease | 0.0481 | 0.0251 | 0.0558 | Wald ratio | 1 | trans | NA |
| _...and 57 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_56 association rows across 35 traits (52 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating PDGFRA levels | 2e-450 | rs35597368 | 3 | GCST90859718 | no MR -> candidate analysis |
| IL6ST/PDGFRA protein level ratio | 3e-441 | rs35597368 | 1 | GCST90315169 | no MR -> candidate analysis |
| Bone mineral density mean | 1e-300 | rs140863234 | 2 | GCST90321120 | no MR -> candidate analysis |
| Corneal curvature | 2e-73 | rs1800813 | 7 | GCST90012795 | no MR -> candidate analysis |
| PDGFRA protein levels | 9e-58 | rs139236922 | 3 | GCST90470191 | no MR -> candidate analysis |
| Height | 1e-36 | rs6554162 | 1 | GCST90245848 | no MR -> candidate analysis |
| Pulse pressure | 1e-22 | rs6554163 | 2 | GCST90310296 | no MR -> candidate analysis |
| Platelet-derived growth factor receptor alpha levels | 2e-21 | rs10028020 | 2 | GCST90060028 | no MR -> candidate analysis |
| Aortic stenosis | 2e-20 | rs4864857 | 3 | GCST90837544 | no MR -> candidate analysis |
| Core binding factor acute myeloid leukemia | 3e-18 | rs890206; rs1559715; rs17084040; rs718454; rs12506783; rs7678144 | 2 | GCST008413 | no MR -> candidate analysis |
| Mean corpuscular volume (UKB data field 30040) | 8e-17 | rs542853222 | 1 | GCST90468086 | no MR -> candidate analysis |
| Aortic stenosis (MTAG) | 2e-16 | rs4864861 | 1 | GCST90651070 | no MR -> candidate analysis |
| _...and 23 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 4767 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| gastrointestinal stromal tumor | 0.647 | — | established (curated) | no MR -> candidate analysis |
| GIST-plus syndrome | 0.835 | — | established (curated) | no MR -> candidate analysis |
| ovarian cancer | 0.625 | — | established (curated) | MR: beta=0.0397, p=0.225 (trans) |
| Abnormality of the skeletal system | 0.786 | — | common-variant locus | no MR -> candidate analysis |

> Of the 4 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 6 known modulators (Platelet-derived growth factor receptor alpha) |
| gnomAD constraint | pLI=1, LOEUF=0.287 — LoF-INTOLERANT |
| GWAS Catalog | 75 unique SNPs / 150 rows |
| ClinVar | 4021 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 4767 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'PDGFRA' and resolved to 'Platelet-derived growth factor receptor alpha' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 4021 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 35 traits by best p-value, aggregated from 56 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P16234 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000134853/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2007/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PDGFRA — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PDGFRA — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PDGFRA%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/PDGFRA — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:15:38  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
