# Causal Card — PNPLA3 × MASLD

**Verdict:** GO — PNPLA3 is one of the strongest genetically validated targets for MASLD, though current lack of known chemical modulators suggests a challenging path to drug discovery.

## Evidence
| Evidence | Tool | Result |
|---|---|---|
| Causal effect (MR) | get_mr_result | Stub: Placeholder results; actual MR estimates not available. |
| Target–disease association | get_target_disease_evidence | Overall score: 0.71 (Strong genetic association: 0.87). |
| Protein context | get_uniprot_dossier | Lipid droplet-associated protein involved in triglyceride metabolism. |
| Known modulators | get_chembl_modulators | Found: false (No ChEMBL target records for PNPLA3). |
| Clinical variants | get_clinvar_variants | 216 records, no pathogenic variants identified in sampled set. |
| Population constraint / LoF tolerance | get_gnomad_constraint | LoF-tolerant (LOEUF: 1.26, pLI: ~0). |
| Extra genetic evidence | get_gwas_catalog | 51 unique GWAS SNPs mapped to gene. |
| Pharmacogenomics | get_pharmgkb_drug_gene | 2 annotations related to drug-induced toxicity (e.g., ethanol, asparaginase). |

## Reasoning
PNPLA3 has a very strong genetic association with MASLD/NAFLD, most notably the well-characterized p.I148M variant, making it a high-confidence biological target. The gene shows high tolerance to loss-of-function (LoF) mutations in gnomAD, which suggests that inhibiting the protein is likely to be safe. However, there are currently no known small-molecule modulators in ChEMBL, indicating that significant medicinal chemistry investment would be required. The MR results remain as placeholders, but the existing body of genetic literature strongly supports the importance of this target.

## Sources
* [Open Targets: PNPLA3-MASLD](https://platform.opentargets.org/evidence/ENSG00000100344/MONDO_0013209)
* [UniProt: PNPLA3](https://www.uniprot.org/uniprotkb/Q9NST1)
* [gnomAD: PNPLA3](https://gnomad.broadinstitute.org/gene/PNPLA3)
* [GWAS Catalog: PNPLA3](https://www.ebi.ac.uk/gwas/genes/PNPLA3)
* [PharmGKB: PNPLA3](https://www.pharmgkb.org/search?query=PNPLA3)
* [ClinVar: PNPLA3](https://www.ncbi.nlm.nih.gov/clinvar/?term=PNPLA3%5Bgene%5D)