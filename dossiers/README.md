# Protein Dossiers — 991 proteins, pre-generated, no key needed

One dossier per protein with a published plasma-pQTL instrument probe. Everything here is
**retrieved from public databases and rendered mechanically** — no language model wrote or
touched any number on these pages, and the whole set regenerates from `proteome_sweep.py`.

**What a dossier holds:** the published Mendelian randomization estimates for that protein
(retrieved from EpiGraphDB's pQTL resource, Zheng et al. *Nat Genet* 2020 — never computed
here), the pQTL instrument datasets that exist for it, GWAS Catalog signal at the locus, and
a phenome map showing where the gene is a genetic locus versus where an MR estimate actually
exists.

**How to read the tiers:** **A** = published pQTL-MR estimates exist (985 proteins,
101,543 protein-outcome estimates in total). **B** = a pQTL instrument exists but no
published MR estimate was retrieved. **C** = no plasma pQTL instrument found — which means
*no estimate*, not *no effect*.

**Two honesty rules that hold on every page:** an absent estimate is never evidence of no
effect, and every number names the database release it came from.

| Protein | Tier | MR outcomes | Top MR outcome | p | Genetic diseases |
|---|---|---|---|---|---|
| [A1CF](A1CF_dossier.md) | A | 112 | Serum creatinine (eGFRcrea) | 3e-06 | 7 |
| [ACE](ACE_dossier.md) | A | 107 | Non-cancer illness code  self-reported: hyper... | 4e-05 | 13 |
| [ACHE](ACHE_dossier.md) | A | 127 | Pulse rate | 2e-09 | 3 |
| [ACP1](ACP1_dossier.md) | A | 115 | Height | 1e-06 | 19 |
| [ACP2](ACP2_dossier.md) | A | 113 | Systemic lupus erythematosus | 0.00123 | 16 |
| [ACP5](ACP5_dossier.md) | A | 88 | Paget's disease | 9e-04 | 5 |
| [ACP6](ACP6_dossier.md) | A | 105 | Non-cancer illness code  self-reported: hyper... | 0.0022 | 5 |
| [ADA2](ADA2_dossier.md) | A | 120 | Weight | 5e-04 | 12 |
| [ADAM12](ADAM12_dossier.md) | A | 93 | Diagnoses - main ICD10: S76 Injury of muscle ... | 9e-04 | 19 |
| [ADAM15](ADAM15_dossier.md) | A | 75 | Non-cancer illness code  self-reported: high ... | 4e-06 | 14 |
| [ADAM19](ADAM19_dossier.md) | A | 121 | Forced expiratory volume in 1-second (FEV1) | 2e-14 | 9 |
| [ADAM22](ADAM22_dossier.md) | A | 72 | Schizophrenia | 3e-05 | 9 |
| [ADAM23](ADAM23_dossier.md) | A | 114 | Diagnoses - main ICD10: K80 Cholelithiasis | 0.00675 | 13 |
| [ADAMTS13](ADAMTS13_dossier.md) | A | 82 | Primary sclerosing cholangitis  | 0.00157 | 7 |
| [ADAMTS5](ADAMTS5_dossier.md) | A | 116 | Height | 6e-05 | 23 |
| [ADGRE2](ADGRE2_dossier.md) | A | 104 | Diagnoses - main ICD10: D25 Leiomyoma of uterus | 1e-05 | 3 |
| [ADH4](ADH4_dossier.md) | A | 112 | Diagnoses - main ICD10: B37 Candidiasis | 1e-05 | 4 |
| [ADH5](ADH5_dossier.md) | A | 118 | HOMA-IR | 6e-05 | 9 |
| [ADH7](ADH7_dossier.md) | A | 95 | Alcohol intake frequency | 7e-04 | 4 |
| [ADIPOQ](ADIPOQ_dossier.md) | A | 65 | Non-cancer illness code self-reported: pulmon... | 4e-04 | 6 |
| [ADM](ADM_dossier.md) | A | 193 | Eye problems or disorders: Glaucoma | 0.00242 | 21 |
| [AFM](AFM_dossier.md) | A | 98 | Cancer code  self-reported: malignant melanoma | 0.00865 | 6 |
| [AFP](AFP_dossier.md) | A | 114 | Diagnoses - main ICD10: B37 Candidiasis | 8e-05 | 4 |
| [AGER](AGER_dossier.md) | A | 112 | Age at menarche | 4e-06 | 0 |
| [AGRP](AGRP_dossier.md) | A | 118 | Height | 3e-09 | 7 |
| [AGT](AGT_dossier.md) | A | 116 | Diastolic blood pressure  automated reading | 1e-11 | 17 |
| [AHSG](AHSG_dossier.md) | A | 106 | Non-cancer illness code  self-reported: diver... | 0.00566 | 3 |
| [AIFM1](AIFM1_dossier.md) | A | 76 | Weight | 4e-04 | 24 |
| [AKR1A1](AKR1A1_dossier.md) | A | 80 | Breast cancer (Combined Oncoarray; iCOGS; GWA... | 0.00237 | 3 |
| [AKR1B1](AKR1B1_dossier.md) | A | 60 | Birth weight | 0.011 | 3 |
| [AKR1C1](AKR1C1_dossier.md) | A | 111 | Height | 1e-13 | 7 |
| [AKR7A2](AKR7A2_dossier.md) | A | 96 | Diagnoses - main ICD10: M23 Internal derangem... | 3e-04 | 3 |
| [ALCAM](ALCAM_dossier.md) | A | 109 | Height | 3e-07 | 26 |
| [ALDH3A1](ALDH3A1_dossier.md) | A | 110 | Lung adenocarcinoma | 0.00469 | 2 |
| [ALPP](ALPP_dossier.md) | A | 63 | Diagnoses - main ICD10: N20 Calculus of kidne... | 0.0106 | 5 |
| [ALPPL2](ALPPL2_dossier.md) | A | 72 | Body mass index (BMI) | 0.0192 | 7 |
| [AMBP](AMBP_dossier.md) | A | 110 | Forced vital capacity (FVC) | 7e-05 | 15 |
| [AMH](AMH_dossier.md) | A | 82 | Femoral neck bone mineral density | 0.00216 | 5 |
| [AMY1A](AMY1A_dossier.md) | A | 84 | Diagnoses - main ICD10: I84 Haemorrhoids | 0.00746 | 16 |
| [AMY2B](AMY2B_dossier.md) | A | 101 | Eczema | 0.0114 | 13 |
| [ANG](ANG_dossier.md) | A | 112 | Diagnoses - main ICD10: B37 Candidiasis | 6e-04 | 5 |
| [ANGPTL1](ANGPTL1_dossier.md) | A | 117 | HDL cholesterol | 4e-04 | 3 |
| [ANGPTL3](ANGPTL3_dossier.md) | A | 64 | Triglycerides | 1e-81 | 20 |
| [ANXA1](ANXA1_dossier.md) | A | 101 | Urate | 0.00173 | 15 |
| [ANXA2](ANXA2_dossier.md) | A | 119 | Age at menarche | 9e-05 | 8 |
| [AOC1](AOC1_dossier.md) | A | 117 | Height | 5e-10 | 15 |
| [AP1G2](AP1G2_dossier.md) | A | 102 | Diagnoses - main ICD10: C50 Malignant neoplas... | 0.00434 | 5 |
| [AP4M1](AP4M1_dossier.md) | A | 207 | Diagnoses - main ICD10: H25 Senile cataract | 0.00229 | 13 |
| [APCS](APCS_dossier.md) | A | 87 | Non-cancer illness code  self-reported: muscl... | 9e-04 | 6 |
| [APMAP](APMAP_dossier.md) | A | 102 | Body mass index (BMI) | 0.00109 | 3 |
| [APOA1](APOA1_dossier.md) | A | 69 | Non-cancer illness code  self-reported: hypot... | 0.0118 | 25 |
| [APOA5](APOA5_dossier.md) | A | 93 | Non-cancer illness code  self-reported: high ... | 6e-23 | 29 |
| [APOB](APOB_dossier.md) | A | 249 | LDL cholesterol | 2e-54 | 30 |
| [APOBEC3G](APOBEC3G_dossier.md) | A | 106 | Non-cancer illness code  self-reported: hiatu... | 0.00112 | 2 |
| [APOF](APOF_dossier.md) | A | 87 | Height | 6e-15 | 5 |
| [APOH](APOH_dossier.md) | A | 95 | Height | 5e-04 | 15 |
| [APOL1](APOL1_dossier.md) | A | 262 | Haemoglobin concentration | 3e-04 | 29 |
| [ARFIP1](ARFIP1_dossier.md) | A | 104 | Height | 0.00744 | 7 |
| [ARHGAP1](ARHGAP1_dossier.md) | A | 76 | Systolic blood pressure  automated reading | 0.00149 | 13 |
| [ARHGEF10](ARHGEF10_dossier.md) | A | 93 | Amyotrophic lateral sclerosis | 0.0248 | 8 |
| [ART3](ART3_dossier.md) | A | 88 | Diagnoses - main ICD10: I30 Acute pericarditis | 0.00418 | 5 |
| [ART4](ART4_dossier.md) | A | 111 | Heel bone mineral density (BMD) T-score  auto... | 9e-07 | 12 |
| [ASAH2;ASAH2B](ASAH2;ASAH2B_dossier.md) | A | 20 | Ovarian cancer | 0.0141 | 0 |
| [ASIP](ASIP_dossier.md) | A | 97 | Weight | 2e-17 | 23 |
| [ASMTL](ASMTL_dossier.md) | A | 13 | Amyotrophic lateral sclerosis | 0.00156 | 2 |
| [ASPH](ASPH_dossier.md) | A | 89 | Diagnoses - main ICD10: M23 Internal derangem... | 0.00578 | 24 |
| [ASPN](ASPN_dossier.md) | A | 111 | Height | 1e-14 | 4 |
| [ATF6](ATF6_dossier.md) | A | 73 | Eczema | 0.00641 | 13 |
| [ATP1B2](ATP1B2_dossier.md) | A | 113 | Non-cancer illness code  self-reported: hyper... | 0.00105 | 12 |
| [ATP2A3](ATP2A3_dossier.md) | A | 125 | HDL cholesterol | 3e-17 | 18 |
| [ATP4B](ATP4B_dossier.md) | A | 95 | Red blood cell count | 0.00146 | 0 |
| [AZU1](AZU1_dossier.md) | A | 107 | Heel bone mineral density (BMD) T-score  auto... | 2e-10 | 5 |
| [B2M](B2M_dossier.md) | A | 136 | Non-cancer illness code  self-reported: hypot... | 4e-191 | 7 |
| [B3GALT6](B3GALT6_dossier.md) | A | 105 | Diagnoses - main ICD10: K35 Acute appendicitis | 0.00136 | 15 |
| [B3GALTL](B3GALTL_dossier.md) | A | 118 | Heel bone mineral density (BMD) T-score  auto... | 1e-05 | 28 |
| [B3GAT3](B3GAT3_dossier.md) | A | 93 | Forced expiratory volume in 1-second (FEV1) | 9e-07 | 4 |
| [B3GNT2](B3GNT2_dossier.md) | A | 118 | Height | 3e-18 | 25 |
| [B3GNT8](B3GNT8_dossier.md) | A | 124 | Height | 1e-20 | 5 |
| [B4GALT1](B4GALT1_dossier.md) | A | 207 | LDL cholesterol | 4e-05 | 9 |
| [B4GALT2](B4GALT2_dossier.md) | A | 81 | Diagnoses - main ICD10: R10 Abdominal and pel... | 0.02 | 1 |
| [B4GALT6](B4GALT6_dossier.md) | A | 69 | Pallidum volume | 7e-04 | 2 |
| [B4GAT1](B4GAT1_dossier.md) | A | 15 | Amyotrophic lateral sclerosis | 0.00332 | 9 |
| [BCAN](BCAN_dossier.md) | A | 111 | Diagnoses - main ICD10: S76 Injury of muscle ... | 2e-04 | 4 |
| [BCAR3](BCAR3_dossier.md) | A | 112 | Myocardial infarction | 5e-04 | 8 |
| [BCHE](BCHE_dossier.md) | A | 170 | LDL cholesterol | 3e-05 | 19 |
| [BCL10](BCL10_dossier.md) | A | 72 | Non-cancer illness code  self-reported: hypop... | 4e-10 | 4 |
| [BGLAP](BGLAP_dossier.md) | A | 117 | Pulse rate | 0.00252 | 15 |
| [BMP6](BMP6_dossier.md) | A | 93 | Diagnoses - main ICD10: D12 Benign neoplasm o... | 4e-06 | 24 |
| [BOC](BOC_dossier.md) | A | 93 | Height | 8e-06 | 19 |
| [BPI](BPI_dossier.md) | A | 97 | Endometrioid ovarian cancer | 0.0346 | 4 |
| [BPIFA2](BPIFA2_dossier.md) | A | 51 | Non-cancer illness code  self-reported: mania... | 2e-04 | 4 |
| [BPIFB1](BPIFB1_dossier.md) | A | 80 | ER-positive Breast cancer (Combined Oncoarray... | 0.0103 | 3 |
| [BST1](BST1_dossier.md) | A | 79 | Diagnoses - main ICD10: N20 Calculus of kidne... | 2e-04 | 9 |
| [BTD](BTD_dossier.md) | A | 76 | Diagnoses - main ICD10: N92 Excessive  freque... | 0.00204 | 10 |
| [BTNL8](BTNL8_dossier.md) | A | 102 | Eye problems or disorders: Injury or trauma r... | 6e-04 | 2 |
| [C10orf10](C10orf10_dossier.md) | A | 17 | Amyotrophic lateral sclerosis | 0.0134 | 9 |
| [C17orf78](C17orf78_dossier.md) | A | 77 | Non-cancer illness code  self-reported: enlar... | 7e-04 | 6 |
| [C1QC](C1QC_dossier.md) | A | 153 | Platelet count | 0.00979 | 7 |
| [C1QL1](C1QL1_dossier.md) | A | 116 | Systolic blood pressure  automated reading | 2e-05 | 4 |
| [C1QTNF1](C1QTNF1_dossier.md) | A | 182 | Age at menarche | 0.0012 | 0 |
| [C1QTNF3](C1QTNF3_dossier.md) | A | 93 | Depressive symptoms | 0.0027 | 3 |
| [C1QTNF5](C1QTNF5_dossier.md) | A | 320 | Crohn's disease | 7e-36 | 7 |
| [C1RL](C1RL_dossier.md) | A | 56 | Myocardial infarction | 5e-04 | 1 |
| [C1S](C1S_dossier.md) | A | 106 | Systolic blood pressure  automated reading | 7e-04 | 8 |
| [C3](C3_dossier.md) | A | 98 | Diagnoses - main ICD10: I80 Phlebitis and thr... | 2e-04 | 26 |
| [C4BPA](C4BPA_dossier.md) | A | 113 | Rheumatoid arthritis | 0.00155 | 4 |
| [C5](C5_dossier.md) | A | 106 | Diagnoses - main ICD10: C50 Malignant neoplas... | 1e-04 | 7 |
| [C6orf89](C6orf89_dossier.md) | A | 77 | Alcohol intake frequency | 0.0238 | 7 |
| [C7](C7_dossier.md) | A | 99 | Years of schooling | 5e-04 | 10 |
| [C8A;C8B;C8G](C8A;C8B;C8G_dossier.md) | A | 95 | Non-cancer illness code  self-reported: polio... | 0.0015 | 0 |
| [C8orf33](C8orf33_dossier.md) | A | 110 | Diagnoses - main ICD10: N20 Calculus of kidne... | 0.00535 | 3 |
| [C9](C9_dossier.md) | A | 99 | Non-cancer illness code  self-reported: muscl... | 0.0042 | 21 |
| [CA1](CA1_dossier.md) | A | 116 | Fractured bone site(s): Other bones | 0.00271 | 0 |
| [CA10](CA10_dossier.md) | A | 67 | Non-cancer illness code  self-reported: gout | 0.00363 | 29 |
| [CA13](CA13_dossier.md) | A | 77 | Sleep duration | 0.00355 | 2 |
| [CA3](CA3_dossier.md) | A | 92 | Diagnoses - main ICD10: R11 Nausea and vomiting | 8e-04 | 1 |
| [CA5A](CA5A_dossier.md) | A | 82 | Body mass index (BMI) | 0.00907 | 18 |
| [CA6](CA6_dossier.md) | A | 64 | ER-negative Breast cancer (Combined Oncoarray... | 0.0054 | 6 |
| [CA8](CA8_dossier.md) | A | 91 | Diagnoses - main ICD10: I83 Varicose veins of... | 1e-04 | 26 |
| [CACNA2D3](CACNA2D3_dossier.md) | A | 198 | Forced expiratory volume in 1-second (FEV1) | 1e-04 | 6 |
| [CALB1](CALB1_dossier.md) | A | 92 | Alcohol intake frequency | 0.00514 | 13 |
| [CALCOCO2](CALCOCO2_dossier.md) | A | 128 | Height | 1e-04 | 13 |
| [CANX](CANX_dossier.md) | A | 52 | Ulcerative colitis | 0.0187 | 2 |
| [CAPG](CAPG_dossier.md) | A | 84 | Hearing difficulty or problems: Yes | 1e-04 | 2 |
| [CAPN1;CAPNS1](CAPN1;CAPNS1_dossier.md) | A | 117 | Pulse rate | 9e-06 | 0 |
| [CASP3](CASP3_dossier.md) | A | 100 | Systemic lupus erythematosus | 0.00339 | 4 |
| [CAT](CAT_dossier.md) | A | 99 | Diagnoses - main ICD10: C61 Malignant neoplas... | 0.0113 | 7 |
| [CBLN1](CBLN1_dossier.md) | A | 82 | Non-cancer illness code  self-reported: arthr... | 2e-04 | 14 |
| [CBLN4](CBLN4_dossier.md) | A | 117 | Weight | 1e-07 | 17 |
| [CBR1](CBR1_dossier.md) | A | 75 | Fractured bone site(s): Wrist | 4e-04 | 12 |
| [CBR3](CBR3_dossier.md) | A | 127 | Schizophrenia | 4e-04 | 9 |
| [CCDC126](CCDC126_dossier.md) | A | 111 | Diagnoses - main ICD10: R07 Pain in throat an... | 3e-04 | 7 |
| [CCL1](CCL1_dossier.md) | A | 119 | Childhood intelligence | 0.00257 | 1 |
| [CCL11](CCL11_dossier.md) | A | 4 | Percent emphysema | 0.0892 | 9 |
| [CCL14](CCL14_dossier.md) | A | 163 | Melanoma | 0.0217 | 1 |
| [CCL15](CCL15_dossier.md) | A | 113 | Subjective well being | 0.0027 | 0 |
| [CCL16](CCL16_dossier.md) | A | 79 | Non-cancer illness code  self-reported: hypop... | 0.00286 | 1 |
| [CCL17](CCL17_dossier.md) | A | 195 | Rheumatoid arthritis | 0.00851 | 2 |
| [CCL18](CCL18_dossier.md) | A | 94 | Diagnoses - main ICD10: G47 Sleep disorders | 0.0108 | 0 |
| [CCL2](CCL2_dossier.md) | A | 83 | Non-cancer illness code  self-reported: hypot... | 6e-04 | 25 |
| [CCL21](CCL21_dossier.md) | A | 121 | Total cholesterol | 7e-07 | 8 |
| [CCL22](CCL22_dossier.md) | A | 75 | Non-cancer illness code  self-reported: high ... | 2e-26 | 3 |
| [CCL23](CCL23_dossier.md) | A | 91 | Non-cancer illness code  self-reported: bladd... | 0.00208 | 3 |
| [CCL25](CCL25_dossier.md) | A | 174 | Height | 1e-07 | 1 |
| [CCL27](CCL27_dossier.md) | A | 109 | Serum creatinine (eGFRcrea) | 0.00511 | 0 |
| [CCL28](CCL28_dossier.md) | A | 171 | Diagnoses - main ICD10: K43 Ventral hernia | 3e-04 | 1 |
| [CCL3](CCL3_dossier.md) | A | 90 | Neo-openness to experience | 0.00567 | 0 |
| [CCL3L1](CCL3L1_dossier.md) | A | 94 | Neo-openness to experience | 0.00408 | 0 |
| [CCL4](CCL4_dossier.md) | A | 171 | Ulcerative colitis | 3e-05 | 0 |
| [CCL4L1](CCL4L1_dossier.md) | A | 99 | Fractured bone site(s): Ankle | 5e-04 | 1 |
| [CCL5](CCL5_dossier.md) | A | 114 | Neo-agreeableness | 6e-04 | 1 |
| [CCL7](CCL7_dossier.md) | A | 111 | Crohn's disease | 0.00239 | 14 |
| [CCL8](CCL8_dossier.md) | A | 109 | Crohn's disease | 0.00239 | 4 |
| [CCNH](CCNH_dossier.md) | A | 113 | Large vessel disease | 7e-05 | 23 |
| [CD109](CD109_dossier.md) | A | 118 | Heel bone mineral density (BMD) T-score  auto... | 2e-13 | 29 |
| [CD14](CD14_dossier.md) | A | 205 | Systolic blood pressure  automated reading | 0.00335 | 2 |
| [CD163](CD163_dossier.md) | A | 65 | Non-cancer illness code  self-reported: osteo... | 0.0197 | 6 |
| [CD177](CD177_dossier.md) | A | 75 | Non-cancer illness code  self-reported: diver... | 0.00349 | 0 |
| [CD200R1](CD200R1_dossier.md) | A | 106 | Non-cancer illness code  self-reported: asthma | 9e-06 | 8 |
| [CD274](CD274_dossier.md) | A | 102 | Non-cancer illness code  self-reported: hypot... | 2e-05 | 2 |
| [CD300A](CD300A_dossier.md) | A | 107 | Diastolic blood pressure  automated reading | 0.00479 | 2 |
| [CD300C](CD300C_dossier.md) | A | 168 | Coronary heart disease | 2e-05 | 1 |
| [CD300E](CD300E_dossier.md) | A | 108 | Triglycerides | 0.00404 | 3 |
| [CD33](CD33_dossier.md) | A | 113 | Alzheimer's disease | 7e-08 | 3 |
| [CD34](CD34_dossier.md) | A | 110 | Height | 1e-14 | 14 |
| [CD3E](CD3E_dossier.md) | A | 94 | Non-cancer illness code  self-reported: high ... | 0.00945 | 3 |
| [CD48](CD48_dossier.md) | A | 74 | Eye problems or disorders: Diabetes related e... | 7e-04 | 2 |
| [CD55](CD55_dossier.md) | A | 114 | Non-cancer illness code  self-reported: retin... | 0.00112 | 19 |
| [CD59](CD59_dossier.md) | A | 108 | Pulse rate | 0.00157 | 2 |
| [CD5L](CD5L_dossier.md) | A | 101 | Non-cancer illness code  self-reported: diver... | 0.00124 | 2 |
| [CD7](CD7_dossier.md) | A | 95 | Non-cancer illness code  self-reported: asthma | 0.00639 | 2 |
| [CD8A](CD8A_dossier.md) | A | 70 | Invasive mucinous ovarian cancer | 0.00497 | 3 |
| [CDCP1](CDCP1_dossier.md) | A | 90 | Diagnoses - main ICD10: D12 Benign neoplasm o... | 3e-07 | 6 |
| [CDH11](CDH11_dossier.md) | A | 98 | Alcohol intake frequency | 0.00118 | 10 |
| [CDH13](CDH13_dossier.md) | A | 77 | Non-cancer illness code  self-reported: high ... | 2e-06 | 30 |
| [CDH7](CDH7_dossier.md) | A | 102 | Non-cancer illness code  self-reported: hypop... | 0.00516 | 18 |
| [CDNF](CDNF_dossier.md) | A | 68 | Eczema | 0.00641 | 1 |
| [CDON](CDON_dossier.md) | A | 109 | Birth length | 0.00198 | 21 |
| [CDSN](CDSN_dossier.md) | A | 198 | Body mass index (BMI) | 0.00107 | 4 |
| [CEL](CEL_dossier.md) | A | 95 | Diagnoses - main ICD10: N92 Excessive  freque... | 0.00167 | 5 |
| [CFB](CFB_dossier.md) | A | 121 | Forearm bone mineral density | 7e-06 | 9 |
| [CFH](CFH_dossier.md) | A | 119 | Forced vital capacity (FVC) | 2e-04 | 27 |
| [CFHR1](CFHR1_dossier.md) | A | 107 | Forearm bone mineral density | 0.00406 | 14 |
| [CFHR4](CFHR4_dossier.md) | A | 122 | Systolic blood pressure  automated reading | 3e-07 | 16 |
| [CFHR5](CFHR5_dossier.md) | A | 98 | Non-cancer illness code  self-reported: deep ... | 0.0029 | 18 |
| [CFI](CFI_dossier.md) | A | 110 | Amyotrophic lateral sclerosis | 0.00513 | 22 |
| [CGA](CGA_dossier.md) | A | 91 | Creatinine (enzymatic) in urine | 0.00107 | 3 |
| [CGA;CGB3;CGB7](CGA;CGB3;CGB7_dossier.md) | A | 103 | Diagnoses - main ICD10: N92 Excessive  freque... | 0.00358 | 0 |
| [CGA;LHB](CGA;LHB_dossier.md) | A | 105 | Creatinine (enzymatic) in urine | 0.00108 | 0 |
| [CGREF1](CGREF1_dossier.md) | A | 96 | Eye problems or disorders: Glaucoma | 1e-04 | 19 |
| [CHI3L1](CHI3L1_dossier.md) | A | 57 | Non-cancer illness code  self-reported: asthma | 0.00386 | 5 |
| [CHIC2](CHIC2_dossier.md) | A | 125 | Creatinine (enzymatic) in urine | 0.00648 | 0 |
| [CHIT1](CHIT1_dossier.md) | A | 126 | Knee osteoarthritis | 0.00863 | 6 |
| [CHL1](CHL1_dossier.md) | A | 102 | Heel bone mineral density (BMD) T-score  auto... | 0.00299 | 21 |
| [CHRDL2](CHRDL2_dossier.md) | A | 95 | Diagnoses - main ICD10: D12 Benign neoplasm o... | 1e-05 | 14 |
| [CHST1](CHST1_dossier.md) | A | 105 | HDL cholesterol | 1e-13 | 22 |
| [CHST12](CHST12_dossier.md) | A | 72 | Diagnoses - main ICD10: I30 Acute pericarditis | 1e-04 | 3 |
| [CHST9](CHST9_dossier.md) | A | 91 | Non-cancer illness code  self-reported: mania... | 3e-04 | 21 |
| [CKM](CKM_dossier.md) | A | 76 | Forearm bone mineral density | 0.00208 | 11 |
| [CLEC11A](CLEC11A_dossier.md) | A | 92 | Diagnoses - main ICD10: K40 Inguinal hernia | 4e-04 | 0 |
| [CLEC12A](CLEC12A_dossier.md) | A | 75 | Eye problems or disorders: Diabetes related e... | 9e-04 | 3 |
| [CLEC1B](CLEC1B_dossier.md) | A | 97 | Diagnoses - main ICD10: N40 Hyperplasia of pr... | 0.0162 | 0 |
| [CLEC3B](CLEC3B_dossier.md) | A | 106 | Neuroticism | 2e-04 | 2 |
| [CLEC4C](CLEC4C_dossier.md) | A | 69 | Thalamus volume | 0.00254 | 1 |
| [CLEC5A](CLEC5A_dossier.md) | A | 19 | Major depressive disorder | 0.0603 | 0 |
| [CLIC5](CLIC5_dossier.md) | A | 60 | Clear cell ovarian cancer | 0.0131 | 29 |
| [CLMP](CLMP_dossier.md) | A | 121 | Heel bone mineral density (BMD) T-score  auto... | 1e-04 | 21 |
| [CLN5](CLN5_dossier.md) | A | 89 | Total cholesterol | 0.00437 | 15 |
| [CLPS](CLPS_dossier.md) | A | 69 | Non-cancer illness code  self-reported: joint... | 0.0025 | 4 |
| [CNDP1](CNDP1_dossier.md) | A | 103 | Gallbladder cancer | 0.00126 | 7 |
| [CNP](CNP_dossier.md) | A | 81 | Non-cancer illness code  self-reported: osteo... | 3e-04 | 5 |
| [CNTFR](CNTFR_dossier.md) | A | 67 | Non-cancer illness code  self-reported: bladd... | 4e-04 | 6 |
| [CNTN1](CNTN1_dossier.md) | A | 170 | Diagnoses - main ICD10: B37 Candidiasis | 0.0028 | 14 |
| [CNTN2](CNTN2_dossier.md) | A | 119 | Mean platelet volume | 9e-10 | 16 |
| [CNTN4](CNTN4_dossier.md) | A | 75 | Diagnoses - main ICD10: R10 Abdominal and pel... | 4e-05 | 30 |
| [CNTN5](CNTN5_dossier.md) | A | 107 | Diastolic blood pressure  automated reading | 1e-04 | 30 |
| [CNTNAP2](CNTNAP2_dossier.md) | A | 98 | Non-cancer illness code  self-reported: depre... | 1e-04 | 28 |
| [COCH](COCH_dossier.md) | A | 89 | Underlying (primary) cause of death: ICD10: E... | 1e-05 | 11 |
| [COL15A1](COL15A1_dossier.md) | A | 110 | Height | 1e-07 | 14 |
| [COL18A1](COL18A1_dossier.md) | A | 56 | Diagnoses - main ICD10: M72 Fibroblastic diso... | 0.00246 | 17 |
| [COL1A1](COL1A1_dossier.md) | A | 169 | Body mass index (BMI) | 1e-04 | 24 |
| [COL6A1](COL6A1_dossier.md) | A | 103 | Eye problems or disorders: Injury or trauma r... | 0.00303 | 18 |
| [COLEC12](COLEC12_dossier.md) | A | 123 | Diagnoses - main ICD10: K80 Cholelithiasis | 1e-04 | 11 |
| [COLGALT1](COLGALT1_dossier.md) | A | 150 | Systolic blood pressure  automated reading | 0.00462 | 7 |
| [COX8A](COX8A_dossier.md) | A | 96 | Height | 0.00338 | 3 |
| [CP](CP_dossier.md) | A | 74 | Non-cancer illness code  self-reported: hypot... | 7e-04 | 7 |
| [CPA2](CPA2_dossier.md) | A | 77 | Alcohol intake frequency | 0.0238 | 2 |
| [CPA4](CPA4_dossier.md) | A | 118 | Diastolic blood pressure  automated reading | 1e-04 | 3 |
| [CPB1](CPB1_dossier.md) | A | 165 | Ulcerative colitis | 3e-04 | 5 |
| [CPB2](CPB2_dossier.md) | A | 105 | Alcohol intake frequency | 0.00405 | 3 |
| [CPM](CPM_dossier.md) | A | 62 | Heel bone mineral density (BMD) T-score  auto... | 3e-04 | 11 |
| [CPNE1](CPNE1_dossier.md) | A | 103 | Height | 2e-25 | 13 |
| [CPQ](CPQ_dossier.md) | A | 74 | Non-cancer illness code  self-reported: retin... | 0.0012 | 19 |
| [CPXM1](CPXM1_dossier.md) | A | 4 | ER-positive Breast cancer (Combined Oncoarray... | 0.0341 | 5 |
| [CPZ](CPZ_dossier.md) | A | 101 | Diagnoses - main ICD10: J33 Nasal polyp | 0.00112 | 15 |
| [CREB3L4](CREB3L4_dossier.md) | A | 123 | Schizophrenia | 2e-04 | 6 |
| [CREG1](CREG1_dossier.md) | A | 109 | Diagnoses - main ICD10: H25 Senile cataract | 4e-06 | 7 |
| [CRELD1](CRELD1_dossier.md) | A | 126 | Weight | 1e-07 | 7 |
| [CRHBP](CRHBP_dossier.md) | A | 98 | HOMA-B | 0.0267 | 3 |
| [CRISP2](CRISP2_dossier.md) | A | 87 | Underlying (primary) cause of death: ICD10: E... | 9e-07 | 2 |
| [CRISPLD2](CRISPLD2_dossier.md) | A | 77 | Lung cancer | 0.00199 | 19 |
| [CRLF1](CRLF1_dossier.md) | A | 116 | Potassium in urine | 3e-04 | 15 |
| [CROT](CROT_dossier.md) | A | 104 | Bipolar disorder | 4e-05 | 11 |
| [CRP](CRP_dossier.md) | A | 330 | Heel bone mineral density (BMD) T-score  auto... | 3e-04 | 11 |
| [CRTAC1](CRTAC1_dossier.md) | A | 117 | Diagnoses - main ICD10: I84 Haemorrhoids | 0.00343 | 17 |
| [CRTAM](CRTAM_dossier.md) | A | 94 | Systemic lupus erythematosus | 0.00129 | 9 |
| [CRYZ](CRYZ_dossier.md) | A | 125 | Non-cancer illness code  self-reported: muscl... | 0.00211 | 10 |
| [CSF1](CSF1_dossier.md) | A | 105 | Forced vital capacity (FVC) | 0.0011 | 6 |
| [CSF2RB](CSF2RB_dossier.md) | A | 103 | Amyotrophic lateral sclerosis | 0.00301 | 9 |
| [CSGALNACT2](CSGALNACT2_dossier.md) | A | 125 | Hirschsprung's disease | 2e-09 | 11 |
| [CST1](CST1_dossier.md) | A | 121 | Iron | 4e-05 | 2 |
| [CST2](CST2_dossier.md) | A | 121 | Iron | 4e-05 | 3 |
| [CST3](CST3_dossier.md) | A | 110 | Serum cystatin C (eGFRcys) | 2e-203 | 10 |
| [CST4](CST4_dossier.md) | A | 93 | Serum cystatin C (eGFRcys) | 4e-28 | 2 |
| [CST5](CST5_dossier.md) | A | 96 | Serum cystatin C (eGFRcys) | 2e-09 | 6 |
| [CST6](CST6_dossier.md) | A | 82 | Alcohol intake frequency | 0.00255 | 3 |
| [CST7](CST7_dossier.md) | A | 104 | Mean cell haemoglobin concentration | 0.00984 | 4 |
| [CST8](CST8_dossier.md) | A | 1 | Alzheimer's disease | 0.108 | 2 |
| [CTGF](CTGF_dossier.md) | A | 96 | Diagnoses - main ICD10: K40 Inguinal hernia | 3e-04 | 10 |
| [CTRB1](CTRB1_dossier.md) | A | 119 | Inflammatory bowel disease | 5e-05 | 22 |
| [CTSA](CTSA_dossier.md) | A | 130 | Mean platelet volume | 3e-32 | 13 |
| [CTSB](CTSB_dossier.md) | A | 113 | Heel bone mineral density (BMD) T-score  auto... | 8e-09 | 16 |
| [CTSC](CTSC_dossier.md) | A | 114 | Serum cystatin C (eGFRcys) | 0.00639 | 23 |
| [CTSD](CTSD_dossier.md) | A | 68 | Non-cancer illness code  self-reported: bladd... | 0.00752 | 12 |
| [CTSF](CTSF_dossier.md) | A | 117 | Breast cancer (Combined Oncoarray; iCOGS; GWA... | 8e-06 | 13 |
| [CTSH](CTSH_dossier.md) | A | 84 | Hearing difficulty or problems: Yes | 0.00351 | 19 |
| [CTSS](CTSS_dossier.md) | A | 74 | Forced vital capacity (FVC) | 2e-05 | 20 |
| [CX3CL1](CX3CL1_dossier.md) | A | 74 | Body mass index (BMI) | 6e-04 | 0 |
| [CXCL1](CXCL1_dossier.md) | A | 95 | Diagnoses - main ICD10: G56 Mononeuropathies ... | 0.00591 | 0 |
| [CXCL10](CXCL10_dossier.md) | A | 103 | Alzheimer's disease | 0.00306 | 0 |
| [CXCL11](CXCL11_dossier.md) | A | 102 | Alzheimer's disease | 0.00137 | 0 |
| [CXCL16](CXCL16_dossier.md) | A | 283 | Crohn's disease | 1e-06 | 2 |
| [CXCL6](CXCL6_dossier.md) | A | 97 | Weight | 0.00954 | 2 |
| [CYB5D2](CYB5D2_dossier.md) | A | 105 | ER-negative Breast cancer (Combined Oncoarray... | 9e-05 | 16 |
| [CYTL1](CYTL1_dossier.md) | A | 64 | Low grade serous ovarian cancer | 0.00964 | 21 |
| [DAPK2](DAPK2_dossier.md) | A | 110 | Diagnoses - main ICD10: I30 Acute pericarditis | 0.0055 | 7 |
| [DCBLD2](DCBLD2_dossier.md) | A | 100 | Diagnoses - main ICD10: R04 Haemorrhage from ... | 4e-04 | 17 |
| [DEFB1](DEFB1_dossier.md) | A | 113 | Squamous cell lung cancer | 0.00123 | 5 |
| [DEFB104A](DEFB104A_dossier.md) | A | 9 | Endometrioid ovarian cancer | 0.0797 | 0 |
| [DEFB112](DEFB112_dossier.md) | A | 11 | Femoral neck bone mineral density | 0.0267 | 15 |
| [DEFB119](DEFB119_dossier.md) | A | 164 | Squamous cell lung cancer | 6e-08 | 6 |
| [DHFR](DHFR_dossier.md) | A | 95 | Platelet count | 0.00382 | 5 |
| [DHX8](DHX8_dossier.md) | A | 100 | Diastolic blood pressure  automated reading | 1e-04 | 5 |
| [DKK1](DKK1_dossier.md) | A | 102 | Eye problems or disorders: Cataract | 0.00138 | 10 |
| [DKK2](DKK2_dossier.md) | A | 76 | Ovarian cancer | 0.00146 | 23 |
| [DKK3](DKK3_dossier.md) | A | 100 | Diagnoses - main ICD10: D25 Leiomyoma of uterus | 0.0121 | 10 |
| [DKK4](DKK4_dossier.md) | A | 106 | Non-cancer illness code  self-reported: hyper... | 2e-08 | 6 |
| [DLK1](DLK1_dossier.md) | A | 96 | Age at menarche | 9e-08 | 17 |
| [DLL1](DLL1_dossier.md) | A | 76 | Diagnoses - main ICD10: R14 Flatulence and re... | 1e-04 | 25 |
| [DNAJB9](DNAJB9_dossier.md) | A | 73 | Underlying (primary) cause of death: ICD10: E... | 2e-26 | 11 |
| [DNAJC30](DNAJC30_dossier.md) | A | 74 | Eye problems or disorders: Glaucoma | 0.00321 | 9 |
| [DNER](DNER_dossier.md) | A | 67 | Birth weight | 0.0146 | 13 |
| [DPEP1](DPEP1_dossier.md) | A | 17 | Schizophrenia | 0.00278 | 16 |
| [DPP4](DPP4_dossier.md) | A | 19 | Invasive mucinous ovarian cancer | 0.0537 | 11 |
| [DPP7](DPP7_dossier.md) | A | 69 | Non-cancer illness code  self-reported: hyper... | 0.00132 | 1 |
| [DPT](DPT_dossier.md) | A | 86 | Body mass index (BMI) | 1e-04 | 30 |
| [DRGX](DRGX_dossier.md) | A | 102 | Diagnoses - main ICD10: I48 Atrial fibrillati... | 9e-05 | 6 |
| [DSC2](DSC2_dossier.md) | A | 69 | Diagnoses - main ICD10: K43 Ventral hernia | 0.00779 | 18 |
| [DSG2](DSG2_dossier.md) | A | 103 | Diagnoses - main ICD10: I48 Atrial fibrillati... | 1e-03 | 25 |
| [DUSP13](DUSP13_dossier.md) | A | 169 | Cough on most days | 0.00259 | 11 |
| [DUT](DUT_dossier.md) | A | 67 | Pallidum volume | 6e-04 | 20 |
| [DYNLL1](DYNLL1_dossier.md) | A | 64 | Diagnoses - main ICD10: J33 Nasal polyp | 0.00323 | 2 |
| [DYNLL2](DYNLL2_dossier.md) | A | 67 | Body mass index (BMI) | 7e-07 | 5 |
| [DYNLRB1](DYNLRB1_dossier.md) | A | 183 | Juvenile idiopathic arthritis | 0.0108 | 20 |
| [EBI3](EBI3_dossier.md) | A | 116 | Diagnoses - main ICD10: Z09 Follow-up examina... | 0.00315 | 2 |
| [ECE1](ECE1_dossier.md) | B | 0 |  |  | 12 |
| [ECH1](ECH1_dossier.md) | A | 71 | Non-cancer illness code  self-reported: kidne... | 0.00368 | 5 |
| [ECM1](ECM1_dossier.md) | A | 122 | Eczema | 2e-08 | 13 |
| [EDAR](EDAR_dossier.md) | A | 98 | Heel bone mineral density (BMD) T-score  auto... | 4e-04 | 23 |
| [EFEMP1](EFEMP1_dossier.md) | A | 128 | Forced vital capacity (FVC) | 3e-69 | 30 |
| [EGF](EGF_dossier.md) | A | 124 | Platelet count | 6e-06 | 7 |
| [EHBP1](EHBP1_dossier.md) | A | 90 | Body mass index (BMI) | 0.00607 | 29 |
| [EMC1](EMC1_dossier.md) | A | 91 | Forced expiratory volume in 1-second (FEV1) | 0.00295 | 11 |
| [EMC4](EMC4_dossier.md) | A | 103 | Squamous cell lung cancer | 0.0022 | 1 |
| [EMILIN3](EMILIN3_dossier.md) | A | 75 | Cancer code  self-reported: malignant melanoma | 0.00601 | 13 |
| [ENDOU](ENDOU_dossier.md) | A | 69 | Cough on most days | 8e-07 | 4 |
| [ENPP5](ENPP5_dossier.md) | A | 121 | Autism | 8e-05 | 17 |
| [ENPP7](ENPP7_dossier.md) | A | 106 | Non-cancer illness code  self-reported: hyper... | 0.00538 | 11 |
| [ENTPD1](ENTPD1_dossier.md) | A | 101 | Diagnoses - main ICD10: K57 Diverticular dise... | 0.00214 | 10 |
| [ENTPD5](ENTPD5_dossier.md) | A | 110 | Fractured or broken bones in last 5 years | 0.00611 | 6 |
| [EPHA1](EPHA1_dossier.md) | A | 107 | Non-cancer illness code  self-reported: hyper... | 3e-04 | 5 |
| [EPHB2](EPHB2_dossier.md) | A | 107 | Neo-agreeableness | 3e-04 | 13 |
| [EPHB3](EPHB3_dossier.md) | A | 94 | Diagnoses - main ICD10: R04 Haemorrhage from ... | 0.00843 | 9 |
| [EPHB6](EPHB6_dossier.md) | A | 77 | Heel bone mineral density (BMD) T-score  auto... | 7e-04 | 0 |
| [EPYC](EPYC_dossier.md) | A | 74 | Non-cancer illness code  self-reported: high ... | 2e-27 | 7 |
| [ERAP1](ERAP1_dossier.md) | A | 129 | Non-cancer illness code  self-reported: ankyl... | 6e-04 | 26 |
| [ERAP2](ERAP2_dossier.md) | A | 120 | Crohn's disease | 2e-13 | 18 |
| [ERLEC1](ERLEC1_dossier.md) | A | 77 | Schizophrenia | 1e-05 | 19 |
| [ERMAP](ERMAP_dossier.md) | A | 81 | Diagnoses - main ICD10: I48 Atrial fibrillati... | 0.0164 | 3 |
| [ERO1B](ERO1B_dossier.md) | A | 161 | Age at menopause | 5e-04 | 8 |
| [ESAM](ESAM_dossier.md) | A | 121 | Schizophrenia | 2e-08 | 14 |
| [ESD](ESD_dossier.md) | A | 82 | Diagnoses - main ICD10: K43 Ventral hernia | 0.0174 | 23 |
| [ETHE1](ETHE1_dossier.md) | A | 105 | Intracranial volume | 0.0103 | 3 |
| [EVA1C](EVA1C_dossier.md) | A | 190 | Diagnoses - main ICD10: K80 Cholelithiasis | 4e-04 | 8 |
| [EXOSC3](EXOSC3_dossier.md) | A | 73 | Non-cancer illness code  self-reported: emphy... | 0.00152 | 14 |
| [F10](F10_dossier.md) | A | 110 | Diagnoses - main ICD10: K35 Acute appendicitis | 8e-05 | 9 |
| [F11](F11_dossier.md) | A | 197 | Non-cancer illness code  self-reported: hypop... | 0.00356 | 29 |
| [F13B](F13B_dossier.md) | A | 128 | Systolic blood pressure  automated reading | 2e-08 | 18 |
| [F7](F7_dossier.md) | A | 116 | Diagnoses - main ICD10: D12 Benign neoplasm o... | 0.00312 | 14 |
| [FABP1](FABP1_dossier.md) | A | 94 | Diagnoses - main ICD10: K44 Diaphragmatic hernia | 0.00894 | 3 |
| [FAH](FAH_dossier.md) | A | 75 | Diagnoses - main ICD10: R04 Haemorrhage from ... | 0.0199 | 11 |
| [FAM151A](FAM151A_dossier.md) | A | 99 | Underlying (primary) cause of death: ICD10: E... | 3e-10 | 7 |
| [FAM171B](FAM171B_dossier.md) | A | 97 | HbA1C | 0.00585 | 17 |
| [FAM174A](FAM174A_dossier.md) | A | 89 | Squamous cell lung cancer | 0.0118 | 7 |
| [FAM189A2](FAM189A2_dossier.md) | A | 179 | Diagnoses - main ICD10: R14 Flatulence and re... | 5e-04 | 12 |
| [FAM20A](FAM20A_dossier.md) | A | 74 | Alzheimer's disease | 0.00346 | 17 |
| [FAM213A](FAM213A_dossier.md) | A | 112 | Heel bone mineral density (BMD) T-score  auto... | 1e-05 | 7 |
| [FAM3B](FAM3B_dossier.md) | A | 140 | Fractured bone site(s): Ankle | 0.00687 | 12 |
| [FAM3D](FAM3D_dossier.md) | A | 117 | Amyotrophic lateral sclerosis | 0.00395 | 3 |
| [FARS2](FARS2_dossier.md) | A | 88 | Diagnoses - main ICD10: D12 Benign neoplasm o... | 0.00324 | 21 |
| [FAS](FAS_dossier.md) | A | 105 | Non-cancer illness code  self-reported: ankyl... | 8e-04 | 8 |
| [FCER2](FCER2_dossier.md) | A | 97 | Forced vital capacity (FVC) | 0.0025 | 3 |
| [FCGR2A;FCGR2B](FCGR2A;FCGR2B_dossier.md) | A | 117 | Ulcerative colitis | 1e-41 | 0 |
| [FCGR2B](FCGR2B_dossier.md) | A | 96 | Birth weight | 7e-08 | 4 |
| [FCGR3B](FCGR3B_dossier.md) | A | 105 | Ulcerative colitis | 7e-07 | 13 |
| [FCN1](FCN1_dossier.md) | A | 105 | Mean cell haemoglobin concentration | 7e-04 | 7 |
| [FCN2](FCN2_dossier.md) | A | 167 | ER-positive Breast cancer (Combined Oncoarray... | 9e-04 | 6 |
| [FCN3](FCN3_dossier.md) | A | 120 | Non-cancer illness code  self-reported: hyper... | 1e-06 | 5 |
| [FCRL3](FCRL3_dossier.md) | A | 108 | Rheumatoid arthritis | 4e-11 | 14 |
| [FCRL4](FCRL4_dossier.md) | A | 108 | Cardioembolic stroke | 0.00266 | 2 |
| [FCRL6](FCRL6_dossier.md) | A | 115 | IgA nephropathy | 0.0183 | 2 |
| [FETUB](FETUB_dossier.md) | A | 104 | Non-cancer illness code  self-reported: hypop... | 0.0076 | 4 |
| [FGF2](FGF2_dossier.md) | A | 83 | Weight | 1e-05 | 5 |
| [FGF7](FGF7_dossier.md) | A | 80 | Fracture resulting from simple fall | 0.0242 | 21 |
| [FGF8](FGF8_dossier.md) | A | 64 | Sleep duration | 0.00601 | 18 |
| [FGFBP3](FGFBP3_dossier.md) | A | 106 | Years of schooling | 0.00115 | 13 |
| [FGFR3](FGFR3_dossier.md) | A | 65 | Non-cancer illness code  self-reported: hypop... | 9e-06 | 25 |
| [FGL1](FGL1_dossier.md) | A | 106 | Non-cancer illness code  self-reported: enlar... | 0.0102 | 10 |
| [FKBP7](FKBP7_dossier.md) | A | 97 | Height | 0.00547 | 20 |
| [FLRT2](FLRT2_dossier.md) | A | 110 | Pulse rate | 3e-22 | 28 |
| [FLRT3](FLRT3_dossier.md) | A | 85 | Femoral neck bone mineral density | 8e-05 | 27 |
| [FLT4](FLT4_dossier.md) | A | 160 | HbA1C | 0.00184 | 8 |
| [FMOD](FMOD_dossier.md) | A | 82 | Diagnoses - main ICD10: I30 Acute pericarditis | 4e-04 | 4 |
| [FN1](FN1_dossier.md) | A | 116 | Systolic blood pressure  automated reading | 2e-11 | 18 |
| [FNDC5](FNDC5_dossier.md) | A | 96 | Femoral neck bone mineral density | 0.00481 | 2 |
| [FOXJ2](FOXJ2_dossier.md) | A | 91 | Diagnoses - main ICD10: R07 Pain in throat an... | 5e-04 | 3 |
| [FRZB](FRZB_dossier.md) | A | 99 | Height | 3e-05 | 3 |
| [FST](FST_dossier.md) | A | 139 | Triglycerides | 7e-250 | 21 |
| [FSTL1](FSTL1_dossier.md) | A | 73 | Non-cancer illness code  self-reported: vitiligo | 2e-06 | 1 |
| [FTCD](FTCD_dossier.md) | A | 46 | Fractured or broken bones in last 5 years | 0.0172 | 11 |
| [FTL;FTH1](FTL;FTH1_dossier.md) | A | 115 | Total cholesterol | 4e-34 | 0 |
| [FUT10](FUT10_dossier.md) | A | 115 | Body mass index (BMI) | 2e-05 | 17 |
| [FUT3](FUT3_dossier.md) | A | 84 | Non-cancer illness code  self-reported: asthma | 9e-04 | 17 |
| [FUT5](FUT5_dossier.md) | A | 111 | Non-cancer illness code  self-reported: asthma | 0.00346 | 13 |
| [FUT8](FUT8_dossier.md) | A | 91 | Height | 3e-04 | 19 |
| [GAA](GAA_dossier.md) | A | 106 | LDL cholesterol | 0.00648 | 18 |
| [GABBR2](GABBR2_dossier.md) | A | 29 | Ovarian cancer | 0.0109 | 13 |
| [GAL](GAL_dossier.md) | A | 1 | Glioma | 0.124 | 8 |
| [GALNT16](GALNT16_dossier.md) | A | 95 | Invasive mucinous ovarian cancer | 0.00173 | 25 |
| [GALP](GALP_dossier.md) | A | 58 | Non-cancer illness code  self-reported: osteo... | 0.00839 | 1 |
| [GDF11](GDF11_dossier.md) | A | 199 | Body mass index (BMI) | 1e-07 | 3 |
| [GDF15](GDF15_dossier.md) | A | 83 | Body mass index (BMI) | 6e-07 | 6 |
| [GDI2](GDI2_dossier.md) | A | 119 | ER-positive Breast cancer (Combined Oncoarray... | 3e-06 | 7 |
| [GFRA1](GFRA1_dossier.md) | A | 89 | Non-cancer illness code  self-reported: uteri... | 0.0183 | 18 |
| [GFRA2](GFRA2_dossier.md) | A | 107 | Hearing difficulty or problems: Yes | 8e-05 | 21 |
| [GFRAL](GFRAL_dossier.md) | A | 60 | Diagnoses - main ICD10: R14 Flatulence and re... | 0.00167 | 17 |
| [GGH](GGH_dossier.md) | A | 99 | Diagnoses - main ICD10: S66 Injury of muscle ... | 1e-05 | 9 |
| [GHR](GHR_dossier.md) | A | 5 | Birth weight | 0.131 | 9 |
| [GKN2](GKN2_dossier.md) | A | 94 | Lung adenocarcinoma | 8e-04 | 2 |
| [GLCE](GLCE_dossier.md) | A | 120 | Non-cancer illness code  self-reported: high ... | 0.0047 | 5 |
| [GLO1](GLO1_dossier.md) | A | 98 | Body mass index (BMI) | 8e-05 | 7 |
| [GLRX2](GLRX2_dossier.md) | A | 56 | Potassium in urine | 6e-04 | 2 |
| [GLTD2](GLTD2_dossier.md) | A | 77 | Diagnoses - main ICD10: G47 Sleep disorders | 0.00654 | 0 |
| [GNLY](GNLY_dossier.md) | A | 98 | Birth weight | 6e-04 | 4 |
| [GNMT](GNMT_dossier.md) | A | 82 | Creatinine (enzymatic) in urine | 0.00159 | 1 |
| [GNPTG](GNPTG_dossier.md) | A | 103 | Fractured bone site(s): Wrist | 2e-04 | 7 |
| [GNRH2](GNRH2_dossier.md) | A | 95 | Non-cancer illness code  self-reported: polio... | 7e-04 | 0 |
| [GOT1](GOT1_dossier.md) | A | 184 | Mean cell haemoglobin concentration | 3e-04 | 3 |
| [GP1BA](GP1BA_dossier.md) | A | 244 | Juvenile idiopathic arthritis | 2e-06 | 11 |
| [GP5](GP5_dossier.md) | A | 216 | Mean platelet volume | 3e-05 | 3 |
| [GP6](GP6_dossier.md) | A | 107 | Platelet count | 2e-04 | 9 |
| [GPC1](GPC1_dossier.md) | A | 101 | Non-cancer illness code  self-reported: pneum... | 6e-06 | 5 |
| [GPC5](GPC5_dossier.md) | A | 183 | Thyroid cancer | 6e-09 | 29 |
| [GPHA2](GPHA2_dossier.md) | A | 110 | Eye problems or disorders: Glaucoma | 0.00161 | 1 |
| [GPNMB](GPNMB_dossier.md) | A | 166 | Diagnoses - main ICD10: J33 Nasal polyp | 0.00659 | 9 |
| [GPX7](GPX7_dossier.md) | A | 110 | Non-cancer illness code  self-reported: pneum... | 7e-05 | 4 |
| [GRAMD1C](GRAMD1C_dossier.md) | A | 93 | Fractured bone site(s): Ankle | 2e-04 | 2 |
| [GRID2](GRID2_dossier.md) | A | 115 | Rheumatoid arthritis | 8e-04 | 27 |
| [GRN](GRN_dossier.md) | A | 206 | Serum cystatin C (eGFRcys) | 0.00268 | 18 |
| [GRP](GRP_dossier.md) | A | 19 | Major depressive disorder | 0.0603 | 8 |
| [GSN](GSN_dossier.md) | A | 72 | Non-cancer illness code  self-reported: gastr... | 0.00483 | 5 |
| [GSTA1](GSTA1_dossier.md) | A | 122 | Haemoglobin concentration | 2e-04 | 3 |
| [GSTM3](GSTM3_dossier.md) | A | 100 | ER-positive Breast cancer (Combined Oncoarray... | 9e-05 | 4 |
| [GSTO1](GSTO1_dossier.md) | A | 115 | Happiness | 3e-04 | 3 |
| [GSTP1](GSTP1_dossier.md) | A | 116 | Weight | 2e-05 | 1 |
| [GUCA1A](GUCA1A_dossier.md) | A | 92 | Systolic blood pressure  automated reading | 0.00161 | 14 |
| [GZMB](GZMB_dossier.md) | A | 99 | Diagnoses - main ICD10: M54 Dorsalgia | 3e-04 | 6 |
| [GZMM](GZMM_dossier.md) | A | 65 | Neuroticism | 0.0336 | 2 |
| [H6PD](H6PD_dossier.md) | A | 159 | Height | 3e-06 | 11 |
| [HAAO](HAAO_dossier.md) | A | 99 | Eye problems or disorders: Glaucoma | 3e-04 | 25 |
| [HAVCR1](HAVCR1_dossier.md) | A | 116 | Diagnoses - main ICD10: L03 Cellulitis | 2e-04 | 5 |
| [HAVCR2](HAVCR2_dossier.md) | A | 124 | Non-cancer illness code  self-reported: hyper... | 7e-05 | 3 |
| [HBA1;HBB](HBA1;HBB_dossier.md) | A | 113 | LDL cholesterol | 2e-45 | 0 |
| [HBEGF](HBEGF_dossier.md) | A | 54 | Mean platelet volume | 1e-37 | 7 |
| [HBZ](HBZ_dossier.md) | A | 86 | Heel bone mineral density (BMD) T-score  auto... | 0.00228 | 5 |
| [HDGF](HDGF_dossier.md) | A | 125 | Heel bone mineral density (BMD) T-score  auto... | 4e-04 | 3 |
| [HDHD2](HDHD2_dossier.md) | A | 73 | Sodium in urine | 0.0164 | 6 |
| [HFE2](HFE2_dossier.md) | A | 123 | Triglycerides | 5e-04 | 4 |
| [HGF](HGF_dossier.md) | A | 96 | Non-cancer illness code  self-reported: hypop... | 1e-03 | 5 |
| [HGFAC](HGFAC_dossier.md) | A | 99 | Forced vital capacity (FVC) | 3e-05 | 23 |
| [HIBCH](HIBCH_dossier.md) | A | 117 | Diastolic blood pressure  automated reading | 0.00141 | 16 |
| [HMGCR](HMGCR_dossier.md) | B | 0 |  |  | 13 |
| [HNF4A](HNF4A_dossier.md) | A | 73 | Weight | 3e-04 | 28 |
| [HNRNPC](HNRNPC_dossier.md) | A | 96 | Height | 0.00338 | 3 |
| [HP](HP_dossier.md) | A | 121 | Total cholesterol | 4e-34 | 21 |
| [HPGDS](HPGDS_dossier.md) | A | 112 | Age at menarche | 3e-05 | 12 |
| [HPSE](HPSE_dossier.md) | A | 92 | Melanoma | 1e-03 | 5 |
| [HPX](HPX_dossier.md) | A | 160 | Cardioembolic stroke | 0.00774 | 1 |
| [HS6ST1](HS6ST1_dossier.md) | A | 70 | Vascular or heart problems diagnosed by docto... | 0.00276 | 13 |
| [HSD17B14](HSD17B14_dossier.md) | A | 79 | Diagnoses - main ICD10: S76 Injury of muscle ... | 6e-05 | 5 |
| [HSP90B1](HSP90B1_dossier.md) | A | 111 | Heel bone mineral density (BMD) T-score  auto... | 2e-04 | 4 |
| [HSPB1](HSPB1_dossier.md) | A | 80 | Non-cancer illness code  self-reported: hyper... | 2e-04 | 9 |
| [HTATIP2](HTATIP2_dossier.md) | A | 91 | Height | 3e-04 | 7 |
| [ICAM1](ICAM1_dossier.md) | A | 291 | Diastolic blood pressure  automated reading | 2e-04 | 8 |
| [ICAM5](ICAM5_dossier.md) | A | 93 | Crohn's disease | 2e-07 | 25 |
| [ICOS](ICOS_dossier.md) | A | 119 | Systolic blood pressure  automated reading | 1e-06 | 24 |
| [ICOSLG](ICOSLG_dossier.md) | A | 119 | Rheumatoid arthritis | 5e-07 | 9 |
| [IDO1](IDO1_dossier.md) | A | 89 | Non-cancer illness code  self-reported: uteri... | 0.0081 | 2 |
| [IDUA](IDUA_dossier.md) | A | 79 | Systolic blood pressure  automated reading | 8e-06 | 30 |
| [IFI16](IFI16_dossier.md) | A | 84 | Myocardial infarction | 0.00396 | 6 |
| [IFNAR1](IFNAR1_dossier.md) | A | 84 | Cancer code  self-reported: basal cell carcinoma | 0.00114 | 1 |
| [IFNGR1](IFNGR1_dossier.md) | A | 19 | Major depressive disorder | 0.0603 | 11 |
| [IFNLR1](IFNLR1_dossier.md) | A | 82 | Parkinson's disease | 0.00227 | 10 |
| [IGDCC4](IGDCC4_dossier.md) | A | 88 | Diagnoses - main ICD10: R55 Syncope and collapse | 3e-04 | 12 |
| [IGF1](IGF1_dossier.md) | A | 120 | Diastolic blood pressure  automated reading | 9e-09 | 23 |
| [IGF2R](IGF2R_dossier.md) | A | 115 | Birth length | 3e-04 | 22 |
| [IGFBP1](IGFBP1_dossier.md) | A | 147 | Triglycerides | 7e-250 | 5 |
| [IGFBP3](IGFBP3_dossier.md) | A | 120 | Diastolic blood pressure  automated reading | 9e-09 | 25 |
| [IGFBP5](IGFBP5_dossier.md) | A | 54 | Non-cancer illness code  self-reported: kidne... | 3e-04 | 14 |
| [IGFBP7](IGFBP7_dossier.md) | A | 96 | Neo-extraversion | 0.00439 | 25 |
| [IGFLR1](IGFLR1_dossier.md) | A | 113 | Body fat | 0.00186 | 5 |
| [IGLL1](IGLL1_dossier.md) | A | 258 | Non-cancer illness code  self-reported: hyper... | 2e-05 | 12 |
| [IL10RB](IL10RB_dossier.md) | A | 92 | Non-cancer illness code  self-reported: retin... | 3e-04 | 11 |
| [IL11RA](IL11RA_dossier.md) | A | 123 | Non-cancer illness code  self-reported: hyper... | 9e-04 | 4 |
| [IL12B](IL12B_dossier.md) | A | 102 | Inflammatory bowel disease | 1e-33 | 22 |
| [IL12RB1](IL12RB1_dossier.md) | A | 103 | Non-cancer illness code  self-reported: gout | 1e-04 | 7 |
| [IL12RB2](IL12RB2_dossier.md) | A | 75 | Non-cancer illness code  self-reported: chron... | 0.00352 | 27 |
| [IL15RA](IL15RA_dossier.md) | A | 103 | Non-cancer illness code  self-reported: hypot... | 8e-04 | 6 |
| [IL16](IL16_dossier.md) | A | 107 | Height | 1e-05 | 10 |
| [IL17RA](IL17RA_dossier.md) | A | 95 | Cancer code  self-reported: small intestine o... | 0.00932 | 6 |
| [IL17RB](IL17RB_dossier.md) | A | 72 | Height | 0.0057 | 17 |
| [IL17RD](IL17RD_dossier.md) | A | 120 | Forced expiratory volume in 1-second (FEV1) | 1e-05 | 10 |
| [IL18](IL18_dossier.md) | A | 172 | Type 2 diabetes | 3e-04 | 2 |
| [IL18R1](IL18R1_dossier.md) | A | 101 | Crohn's disease | 2e-13 | 30 |
| [IL18RAP](IL18RAP_dossier.md) | A | 108 | Diagnoses - main ICD10: G56 Mononeuropathies ... | 0.00105 | 28 |
| [IL1R1](IL1R1_dossier.md) | A | 118 | Non-cancer illness code  self-reported: asthma | 1e-11 | 9 |
| [IL1R2](IL1R2_dossier.md) | A | 123 | Ulcerative colitis | 8e-10 | 12 |
| [IL1RAP](IL1RAP_dossier.md) | A | 106 | Non-cancer illness code  self-reported: anxie... | 2e-06 | 5 |
| [IL1RL1](IL1RL1_dossier.md) | A | 117 | Crohn's disease | 4e-19 | 30 |
| [IL1RL2](IL1RL2_dossier.md) | A | 85 | Non-cancer illness code self-reported: pulmon... | 0.00152 | 13 |
| [IL1RN](IL1RN_dossier.md) | A | 116 | Myocardial infarction | 2e-06 | 17 |
| [IL23R](IL23R_dossier.md) | A | 72 | Inflammatory bowel disease | 2e-166 | 27 |
| [IL25](IL25_dossier.md) | A | 103 | Weight | 5e-04 | 1 |
| [IL27](IL27_dossier.md) | A | 5 | Crohn's disease | 1e-20 | 13 |
| [IL27RA](IL27RA_dossier.md) | A | 74 | Sleep duration | 0.00389 | 1 |
| [IL5RA](IL5RA_dossier.md) | A | 60 | Nucleus accumbens volume | 0.0029 | 11 |
| [IL6R](IL6R_dossier.md) | A | 133 | Rheumatoid arthritis | 1e-09 | 23 |
| [IL6ST](IL6ST_dossier.md) | A | 373 | Forced vital capacity (FVC) | 0.00151 | 8 |
| [IL7](IL7_dossier.md) | A | 101 | Non-cancer illness code  self-reported: hypot... | 3e-04 | 18 |
| [IL7R](IL7R_dossier.md) | A | 121 | Inflammatory bowel disease | 2e-05 | 26 |
| [IMPAD1](IMPAD1_dossier.md) | A | 69 | Non-cancer illness code  self-reported: psori... | 5e-04 | 19 |
| [IMPDH1](IMPDH1_dossier.md) | A | 203 | Forced expiratory volume in 1-second (FEV1) | 9e-05 | 5 |
| [IMPDH2](IMPDH2_dossier.md) | A | 113 | Height | 4e-10 | 3 |
| [INPP5B](INPP5B_dossier.md) | A | 125 | Bulimia nervosa | 0.00415 | 27 |
| [ISG15](ISG15_dossier.md) | A | 85 | Alcohol intake frequency | 6e-06 | 0 |
| [ISLR2](ISLR2_dossier.md) | A | 165 | LDL cholesterol | 7e-11 | 8 |
| [ITIH1](ITIH1_dossier.md) | A | 182 | Diagnoses - main ICD10: K43 Ventral hernia | 0.00153 | 25 |
| [ITIH2](ITIH2_dossier.md) | A | 95 | Non-cancer illness code  self-reported: hyper... | 0.0116 | 12 |
| [ITIH3](ITIH3_dossier.md) | A | 135 | Schizophrenia | 4e-11 | 26 |
| [ITIH5](ITIH5_dossier.md) | A | 64 | Diagnoses - main ICD10: L03 Cellulitis | 0.00321 | 12 |
| [JAG1](JAG1_dossier.md) | A | 119 | Large vessel disease | 3e-04 | 26 |
| [JAK2](JAK2_dossier.md) | A | 96 | Eye problems or disorders: Glaucoma | 1e-04 | 21 |
| [JAM3](JAM3_dossier.md) | A | 106 | Schizophrenia | 3e-05 | 12 |
| [JAML](JAML_dossier.md) | A | 69 | Weight | 0.00156 | 6 |
| [KDELC2](KDELC2_dossier.md) | A | 87 | Non-cancer illness code  self-reported: uteri... | 7e-09 | 26 |
| [KDR](KDR_dossier.md) | A | 67 | Diagnoses - main ICD10: R07 Pain in throat an... | 0.0213 | 3 |
| [KIAA1161](KIAA1161_dossier.md) | A | 82 | Non-cancer illness code  self-reported: hayfe... | 5e-04 | 11 |
| [KIAA1549L](KIAA1549L_dossier.md) | A | 108 | Diagnoses - main ICD10: K57 Diverticular dise... | 1e-03 | 14 |
| [KIAA2013](KIAA2013_dossier.md) | A | 110 | Neuroblastoma | 7e-04 | 4 |
| [KITLG](KITLG_dossier.md) | A | 124 | HDL cholesterol | 3e-17 | 29 |
| [KLK10](KLK10_dossier.md) | A | 91 | Body fat | 0.00203 | 3 |
| [KLK11](KLK11_dossier.md) | A | 101 | Sodium in urine | 0.00554 | 2 |
| [KLK12](KLK12_dossier.md) | A | 108 | Neo-extraversion | 0.0164 | 0 |
| [KLK13](KLK13_dossier.md) | A | 86 | Years of schooling | 0.0027 | 1 |
| [KLK14](KLK14_dossier.md) | A | 108 | Diagnoses - main ICD10: S76 Injury of muscle ... | 0.0027 | 2 |
| [KLK6](KLK6_dossier.md) | A | 73 | Diagnoses - main ICD10: N40 Hyperplasia of pr... | 3e-05 | 4 |
| [KLK7](KLK7_dossier.md) | A | 115 | Age at menopause | 0.00596 | 2 |
| [KLK8](KLK8_dossier.md) | A | 65 | Sodium in urine | 4e-04 | 1 |
| [KLKB1](KLKB1_dossier.md) | A | 192 | Crohn's disease | 2e-21 | 17 |
| [KLRB1](KLRB1_dossier.md) | A | 7 | Depressive symptoms | 0.0244 | 3 |
| [KLRC3](KLRC3_dossier.md) | A | 78 | Non-cancer illness code  self-reported: hypop... | 9e-04 | 3 |
| [KNG1](KNG1_dossier.md) | A | 117 | Serum creatinine (eGFRcrea) | 3e-06 | 13 |
| [KYNU](KYNU_dossier.md) | A | 110 | Forced vital capacity (FVC) | 2e-05 | 24 |
| [LAG3](LAG3_dossier.md) | A | 85 | Eye problems or disorders: Injury or trauma r... | 2e-05 | 1 |
| [LAMB1;LAMC1;LAMA1](LAMB1;LAMC1;LAMA1_dossier.md) | A | 212 | Height | 4e-04 | 0 |
| [LAMC2](LAMC2_dossier.md) | A | 109 | Diastolic blood pressure  automated reading | 6e-04 | 23 |
| [LANCL1](LANCL1_dossier.md) | A | 55 | Cancer code  self-reported: prostate cancer | 0.00156 | 7 |
| [LBP](LBP_dossier.md) | A | 16 | Ovarian cancer | 0.0752 | 5 |
| [LCMT1](LCMT1_dossier.md) | A | 112 | Serum creatinine (eGFRcrea) | 3e-06 | 5 |
| [LCT](LCT_dossier.md) | A | 135 | Total cholesterol | 1e-14 | 21 |
| [LDLR](LDLR_dossier.md) | A | 77 | Non-cancer illness code  self-reported: high ... | 2e-06 | 30 |
| [LDOC1](LDOC1_dossier.md) | A | 79 | Diagnoses - main ICD10: R11 Nausea and vomiting | 0.00498 | 0 |
| [LEAP2](LEAP2_dossier.md) | A | 114 | Heel bone mineral density (BMD) T-score  auto... | 1e-07 | 0 |
| [LECT2](LECT2_dossier.md) | A | 116 | Cancer code  self-reported: basal cell carcinoma | 0.00362 | 0 |
| [LEPR](LEPR_dossier.md) | A | 98 | Childhood intelligence | 0.00328 | 19 |
| [LGALS2](LGALS2_dossier.md) | A | 116 | Packed cell volume | 4e-04 | 2 |
| [LGALS3](LGALS3_dossier.md) | A | 293 | Diagnoses - main ICD10: R07 Pain in throat an... | 2e-04 | 3 |
| [LGALS3BP](LGALS3BP_dossier.md) | A | 83 | PGC cross-disorder traits | 0.0114 | 1 |
| [LGALS4](LGALS4_dossier.md) | A | 123 | Pulse rate | 1e-08 | 3 |
| [LGALS9](LGALS9_dossier.md) | A | 115 | Crohn's disease | 7e-07 | 1 |
| [LGMN](LGMN_dossier.md) | A | 76 | Forced vital capacity (FVC) | 5e-04 | 6 |
| [LHB](LHB_dossier.md) | A | 105 | Creatinine (enzymatic) in urine | 0.00117 | 4 |
| [LILRA3](LILRA3_dossier.md) | A | 130 | HDL cholesterol | 7e-13 | 0 |
| [LILRA4](LILRA4_dossier.md) | A | 157 | Potassium in urine | 0.00111 | 2 |
| [LILRA5](LILRA5_dossier.md) | A | 109 | HDL cholesterol | 3e-11 | 6 |
| [LILRA6](LILRA6_dossier.md) | A | 71 | Diagnoses - main ICD10: H25 Senile cataract | 0.00496 | 2 |
| [LILRB1](LILRB1_dossier.md) | A | 3 | Juvenile idiopathic arthritis | 0.0934 | 2 |
| [LILRB2](LILRB2_dossier.md) | A | 104 | HDL cholesterol | 9e-11 | 8 |
| [LILRB4](LILRB4_dossier.md) | A | 106 | Fasting proinsulin | 6e-04 | 2 |
| [LILRB5](LILRB5_dossier.md) | A | 82 | Hirschsprung's disease | 0.00188 | 6 |
| [LIPN](LIPN_dossier.md) | A | 99 | Height | 0.00331 | 5 |
| [LMAN2L](LMAN2L_dossier.md) | A | 119 | Bipolar disorder | 5e-07 | 15 |
| [LMNB1](LMNB1_dossier.md) | A | 63 | Cancer code  self-reported: small intestine o... | 0.00442 | 14 |
| [LPA](LPA_dossier.md) | A | 111 | Non-cancer illness code  self-reported: high ... | 1e-41 | 30 |
| [LPO](LPO_dossier.md) | A | 78 | Non-cancer illness code  self-reported: high ... | 5e-04 | 7 |
| [LRIG3](LRIG3_dossier.md) | A | 94 | Non-cancer illness code  self-reported: hypop... | 0.00431 | 6 |
| [LRP11](LRP11_dossier.md) | A | 118 | Internalizing problems | 0.00156 | 5 |
| [LRP12](LRP12_dossier.md) | A | 81 | Non-cancer illness code  self-reported: gastr... | 5e-04 | 28 |
| [LRP8](LRP8_dossier.md) | A | 119 | Diagnoses - main ICD10: I83 Varicose veins of... | 4e-05 | 5 |
| [LRPAP1](LRPAP1_dossier.md) | A | 100 | Depressive symptoms | 0.00461 | 7 |
| [LRRC15](LRRC15_dossier.md) | A | 81 | Non-cancer illness code  self-reported: gastr... | 0.00112 | 2 |
| [LRRC19](LRRC19_dossier.md) | A | 47 | Forearm bone mineral density | 0.00544 | 4 |
| [LRRC4C](LRRC4C_dossier.md) | A | 102 | Depressive symptoms | 0.00596 | 30 |
| [LRRN1](LRRN1_dossier.md) | A | 98 | Forced expiratory volume in 1-second (FEV1) | 4e-05 | 25 |
| [LSAMP](LSAMP_dossier.md) | A | 113 | Non-cancer illness code  self-reported: sleep... | 3e-04 | 23 |
| [LY9](LY9_dossier.md) | A | 76 | Inflammatory bowel disease | 4e-05 | 1 |
| [LYG1](LYG1_dossier.md) | A | 9 | Femoral neck bone mineral density | 0.0279 | 9 |
| [LYVE1](LYVE1_dossier.md) | A | 76 | Diagnoses - main ICD10: N40 Hyperplasia of pr... | 4e-06 | 6 |
| [LYZ](LYZ_dossier.md) | A | 114 | Body mass index (BMI) | 2e-05 | 13 |
| [MAN1A2](MAN1A2_dossier.md) | A | 79 | Clear cell ovarian cancer | 8e-04 | 12 |
| [MAN1C1](MAN1C1_dossier.md) | A | 81 | ER-negative Breast cancer (Combined Oncoarray... | 8e-04 | 7 |
| [MAN2B2](MAN2B2_dossier.md) | A | 108 | Non-cancer illness code  self-reported: retin... | 0.00651 | 6 |
| [MANBA](MANBA_dossier.md) | A | 124 | Diastolic blood pressure  automated reading | 2e-06 | 30 |
| [MANEA](MANEA_dossier.md) | A | 109 | Height | 5e-05 | 19 |
| [MANF](MANF_dossier.md) | A | 123 | Height | 2e-07 | 12 |
| [MANSC1](MANSC1_dossier.md) | A | 105 | Diagnoses - main ICD10: R55 Syncope and collapse | 9e-04 | 9 |
| [MANSC4](MANSC4_dossier.md) | A | 100 | Type 2 diabetes | 8e-04 | 23 |
| [MAP2K2](MAP2K2_dossier.md) | A | 124 | Diastolic blood pressure  automated reading | 0.00131 | 7 |
| [MAP2K4](MAP2K4_dossier.md) | A | 98 | HDL cholesterol | 8e-38 | 4 |
| [MAPK13](MAPK13_dossier.md) | A | 109 | Red blood cell count | 5e-05 | 3 |
| [MAPKAPK2](MAPKAPK2_dossier.md) | A | 119 | Ulcerative colitis | 5e-08 | 6 |
| [MAPKAPK3](MAPKAPK3_dossier.md) | A | 117 | Non-cancer illness code  self-reported: gout | 0.0131 | 9 |
| [MASP1](MASP1_dossier.md) | A | 106 | Systolic blood pressure  automated reading | 0.00409 | 13 |
| [MATN4](MATN4_dossier.md) | A | 116 | Mean cell haemoglobin | 0.00154 | 8 |
| [MBL2](MBL2_dossier.md) | A | 115 | Heel bone mineral density (BMD) T-score  auto... | 4e-08 | 25 |
| [MCAM](MCAM_dossier.md) | A | 104 | Serum creatinine (eGFRcrea) | 3e-05 | 2 |
| [MED1](MED1_dossier.md) | A | 3 | Pancreatic cancer | 0.125 | 3 |
| [MENT](MENT_dossier.md) | A | 76 | Diagnoses - main ICD10: R10 Abdominal and pel... | 0.00176 | 6 |
| [METAP2](METAP2_dossier.md) | A | 108 | Mean platelet volume | 4e-67 | 3 |
| [METTL24](METTL24_dossier.md) | A | 78 | Diagnoses - main ICD10: R11 Nausea and vomiting | 0.00132 | 13 |
| [MFAP2](MFAP2_dossier.md) | A | 75 | Forced vital capacity (FVC) | 3e-30 | 10 |
| [MFGE8](MFGE8_dossier.md) | A | 120 | Creatinine (enzymatic) in urine | 0.00874 | 12 |
| [MGAT2](MGAT2_dossier.md) | A | 117 | Forced vital capacity (FVC) | 7e-04 | 10 |
| [MGAT4B](MGAT4B_dossier.md) | A | 62 | Weight | 0.00178 | 2 |
| [MGP](MGP_dossier.md) | A | 102 | Heel bone mineral density (BMD) T-score  auto... | 6e-06 | 12 |
| [MIA](MIA_dossier.md) | A | 110 | Creatinine (enzymatic) in urine | 0.00204 | 8 |
| [MIF](MIF_dossier.md) | A | 117 | Non-cancer illness code  self-reported: gout | 0.00957 | 2 |
| [MILR1](MILR1_dossier.md) | A | 80 | Body mass index (BMI) | 0.00934 | 5 |
| [MINPP1](MINPP1_dossier.md) | A | 63 | Diastolic blood pressure  automated reading | 0.00371 | 11 |
| [MLN](MLN_dossier.md) | A | 102 | Body mass index (BMI) | 5e-05 | 30 |
| [MMP1](MMP1_dossier.md) | A | 97 | Diagnoses - main ICD10: K20 Oesophagitis | 7e-04 | 3 |
| [MMP10](MMP10_dossier.md) | A | 72 | Eczema | 0.0122 | 3 |
| [MMP12](MMP12_dossier.md) | A | 101 | Eczema | 2e-04 | 14 |
| [MMP7](MMP7_dossier.md) | A | 106 | Diagnoses - main ICD10: R55 Syncope and collapse | 0.00688 | 2 |
| [MMP8](MMP8_dossier.md) | A | 168 | Height | 5e-06 | 1 |
| [MMP9](MMP9_dossier.md) | A | 139 | Non-cancer illness code  self-reported: hypot... | 0.015 | 6 |
| [MPO](MPO_dossier.md) | A | 404 | Sleep duration | 7e-04 | 4 |
| [MPZ](MPZ_dossier.md) | A | 88 | HDL cholesterol | 5e-04 | 27 |
| [MRC2](MRC2_dossier.md) | A | 74 | Diagnoses - main ICD10: I80 Phlebitis and thr... | 2e-05 | 9 |
| [MSMB](MSMB_dossier.md) | A | 116 | Cancer code  self-reported: prostate cancer | 8e-13 | 18 |
| [MSR1](MSR1_dossier.md) | A | 112 | Myocardial infarction | 5e-04 | 29 |
| [MTHFS](MTHFS_dossier.md) | A | 122 | Non-cancer illness code  self-reported: hayfe... | 0.00268 | 3 |
| [MTRF1L](MTRF1L_dossier.md) | A | 105 | PGC cross-disorder traits | 9e-05 | 12 |
| [MUC16](MUC16_dossier.md) | A | 68 | Non-cancer illness code  self-reported: asthma | 2e-07 | 7 |
| [MUL1](MUL1_dossier.md) | A | 101 | Glioma | 5e-04 | 3 |
| [MXRA7](MXRA7_dossier.md) | A | 110 | Pulse rate | 1e-05 | 4 |
| [NAAA](NAAA_dossier.md) | A | 110 | Rheumatoid arthritis | 0.00396 | 6 |
| [NAALAD2](NAALAD2_dossier.md) | A | 217 | Celiac disease | 9e-07 | 21 |
| [NAGK](NAGK_dossier.md) | A | 114 | Forearm bone mineral density | 0.00657 | 4 |
| [NAGPA](NAGPA_dossier.md) | A | 81 | Hearing difficulty or problems: Yes | 0.00621 | 13 |
| [NAPB](NAPB_dossier.md) | A | 90 | Non-cancer illness code  self-reported: enlar... | 0.0026 | 4 |
| [NAT1](NAT1_dossier.md) | A | 102 | Bipolar disorder | 0.00306 | 12 |
| [NCAM1](NCAM1_dossier.md) | A | 225 | Pancreatic cancer | 2e-04 | 30 |
| [NCAM2](NCAM2_dossier.md) | A | 102 | Fractured or broken bones in last 5 years | 0.00339 | 30 |
| [NCR1](NCR1_dossier.md) | A | 13 | Clear cell ovarian cancer | 0.0272 | 2 |
| [NDC80](NDC80_dossier.md) | A | 90 | Diagnoses - main ICD10: M72 Fibroblastic diso... | 0.00248 | 20 |
| [NEGR1](NEGR1_dossier.md) | A | 119 | Body mass index (BMI) | 4e-10 | 30 |
| [NELL1](NELL1_dossier.md) | A | 189 | Diagnoses - main ICD10: R14 Flatulence and re... | 9e-04 | 25 |
| [NEO1](NEO1_dossier.md) | A | 93 | Pulse rate | 4e-05 | 14 |
| [NFASC](NFASC_dossier.md) | A | 169 | Diagnoses - main ICD10: I84 Haemorrhoids | 5e-04 | 10 |
| [NHLRC3](NHLRC3_dossier.md) | A | 80 | Body mass index (BMI) | 0.00934 | 22 |
| [NID1](NID1_dossier.md) | A | 106 | Non-cancer illness code  self-reported: high ... | 0.00959 | 11 |
| [NID2](NID2_dossier.md) | A | 106 | Fractured bone site(s): Other bones | 4e-05 | 20 |
| [NLGN2](NLGN2_dossier.md) | A | 107 | Diagnoses - main ICD10: R14 Flatulence and re... | 1e-04 | 6 |
| [NMB](NMB_dossier.md) | A | 112 | Schizophrenia | 1e-08 | 19 |
| [NMRAL1](NMRAL1_dossier.md) | A | 68 | Diagnoses - main ICD10: L03 Cellulitis | 0.00381 | 4 |
| [NOG](NOG_dossier.md) | A | 71 | Non-cancer illness code  self-reported: hyper... | 8e-05 | 27 |
| [NOV](NOV_dossier.md) | A | 114 | Diastolic blood pressure  automated reading | 2e-17 | 1 |
| [NPC2](NPC2_dossier.md) | C | 0 |  |  | 21 |
| [NPNT](NPNT_dossier.md) | A | 74 | Forced expiratory volume in 1-second (FEV1) | 6e-11 | 22 |
| [NPPB](NPPB_dossier.md) | A | 4 | Neuroblastoma | 0.185 | 7 |
| [NPTX1](NPTX1_dossier.md) | A | 116 | Body mass index (BMI) | 6e-06 | 12 |
| [NPTXR](NPTXR_dossier.md) | A | 74 | Diagnoses - main ICD10: R11 Nausea and vomiting | 2e-06 | 4 |
| [NPW](NPW_dossier.md) | A | 99 | Weight | 2e-05 | 1 |
| [NQO1](NQO1_dossier.md) | A | 132 | Body mass index (BMI) | 2e-06 | 5 |
| [NQO2](NQO2_dossier.md) | A | 17 | Amygdala volume | 0.0511 | 1 |
| [NR1D2](NR1D2_dossier.md) | A | 121 | Diagnoses - main ICD10: K80 Cholelithiasis | 1e-04 | 16 |
| [NRCAM](NRCAM_dossier.md) | A | 106 | Non-cancer illness code  self-reported: high ... | 2e-05 | 11 |
| [NRP1](NRP1_dossier.md) | A | 216 | ER-negative Breast cancer (Combined Oncoarray... | 0.00124 | 28 |
| [NRP2](NRP2_dossier.md) | A | 109 | Small vessel disease | 0.00194 | 29 |
| [NT5C](NT5C_dossier.md) | A | 65 | Diagnoses - main ICD10: K40 Inguinal hernia | 0.0037 | 1 |
| [NTM](NTM_dossier.md) | C | 0 |  |  | 29 |
| [NTN1](NTN1_dossier.md) | A | 116 | Diagnoses - main ICD10: B37 Candidiasis | 0.00603 | 22 |
| [NTN4](NTN4_dossier.md) | A | 105 | Myocardial infarction | 0.00634 | 20 |
| [NTNG1](NTNG1_dossier.md) | A | 85 | Ovarian cancer | 5e-04 | 26 |
| [NTRK3](NTRK3_dossier.md) | A | 98 | Alcohol intake frequency | 0.0067 | 2 |
| [NUDT12](NUDT12_dossier.md) | A | 79 | Heel bone mineral density (BMD) T-score  auto... | 0.0044 | 29 |
| [NUDT16L1](NUDT16L1_dossier.md) | A | 92 | Diagnoses - main ICD10: N81 Female genital pr... | 0.0186 | 3 |
| [NUDT9](NUDT9_dossier.md) | A | 163 | Underlying (primary) cause of death: ICD10: E... | 1e-03 | 12 |
| [OAF](OAF_dossier.md) | A | 62 | Cough on most days | 0.0024 | 11 |
| [OAS1](OAS1_dossier.md) | A | 102 | Body mass index (BMI) | 3e-04 | 16 |
| [OBP2B](OBP2B_dossier.md) | A | 167 | Diagnoses - main ICD10: D12 Benign neoplasm o... | 0.00201 | 0 |
| [OCIAD1](OCIAD1_dossier.md) | A | 112 | Myocardial infarction | 5e-04 | 4 |
| [OLFM1](OLFM1_dossier.md) | A | 76 | Non-cancer illness code  self-reported: hiatu... | 0.0019 | 18 |
| [OLFM2](OLFM2_dossier.md) | A | 62 | Fractured bone site(s): Other bones | 0.0376 | 7 |
| [ORM1](ORM1_dossier.md) | A | 74 | Forced vital capacity (FVC) | 9e-05 | 0 |
| [OSBPL11](OSBPL11_dossier.md) | A | 55 | Non-cancer illness code  self-reported: muscl... | 0.00356 | 6 |
| [OSCAR](OSCAR_dossier.md) | A | 95 | Urinary albumin-to-creatinine ratio | 0.0027 | 0 |
| [OSMR](OSMR_dossier.md) | A | 98 | Cancer code  self-reported: prostate cancer | 4e-04 | 23 |
| [OXT](OXT_dossier.md) | A | 86 | Creatinine (enzymatic) in urine | 8e-04 | 1 |
| [PAM](PAM_dossier.md) | A | 122 | Sleep duration | 5e-06 | 29 |
| [PARP16](PARP16_dossier.md) | A | 115 | Serum creatinine (eGFRcrea) | 3e-06 | 7 |
| [PATE4](PATE4_dossier.md) | A | 92 | HOMA-IR | 8e-05 | 4 |
| [PCBD1](PCBD1_dossier.md) | A | 93 | Lung adenocarcinoma | 0.00165 | 14 |
| [PCDH9](PCDH9_dossier.md) | A | 83 | Systolic blood pressure  automated reading | 8e-04 | 30 |
| [PCDHA7](PCDHA7_dossier.md) | A | 95 | Eye problems or disorders: Glaucoma | 7e-05 | 4 |
| [PCDHB2](PCDHB2_dossier.md) | A | 106 | Bipolar disorder | 0.00143 | 0 |
| [PCOLCE](PCOLCE_dossier.md) | A | 119 | Red blood cell count | 2e-18 | 4 |
| [PCOLCE2](PCOLCE2_dossier.md) | A | 89 | Height | 1e-05 | 12 |
| [PCSK1](PCSK1_dossier.md) | A | 90 | Weight | 1e-15 | 30 |
| [PCSK7](PCSK7_dossier.md) | A | 136 | Triglycerides | 3e-08 | 21 |
| [PCSK9](PCSK9_dossier.md) | A | 64 | Non-cancer illness code  self-reported: high ... | 4e-21 | 26 |
| [PCYOX1](PCYOX1_dossier.md) | A | 122 | Body mass index (BMI) | 3e-04 | 3 |
| [PDCD1LG2](PDCD1LG2_dossier.md) | A | 178 | Non-cancer illness code  self-reported: asthma | 0.00978 | 2 |
| [PDCD5](PDCD5_dossier.md) | A | 109 | Serum creatinine (eGFRcrea) | 1e-03 | 3 |
| [PDE5A](PDE5A_dossier.md) | A | 113 | Non-cancer illness code  self-reported: uteri... | 5e-04 | 3 |
| [PDGFB](PDGFB_dossier.md) | A | 80 | Non-cancer illness code  self-reported: deep ... | 5e-07 | 15 |
| [PDGFD](PDGFD_dossier.md) | A | 88 | Hearing difficulty or problems: Yes | 3e-04 | 21 |
| [PDGFRA](PDGFRA_dossier.md) | A | 69 | Diagnoses - main ICD10: I83 Varicose veins of... | 3e-05 | 4 |
| [PDIA3](PDIA3_dossier.md) | A | 115 | Breast cancer (Combined Oncoarray; iCOGS; GWA... | 3e-05 | 7 |
| [PDIA5](PDIA5_dossier.md) | A | 106 | Platelet count | 3e-04 | 21 |
| [PDK1](PDK1_dossier.md) | A | 93 | Ferritin | 0.00195 | 6 |
| [PDLIM4](PDLIM4_dossier.md) | A | 95 | Height | 4e-08 | 16 |
| [PEAR1](PEAR1_dossier.md) | A | 119 | Systolic blood pressure  automated reading | 3e-04 | 5 |
| [PEBP1](PEBP1_dossier.md) | A | 74 | Cancer code  self-reported: basal cell carcinoma | 0.0111 | 1 |
| [PENK](PENK_dossier.md) | A | 113 | Height | 2e-07 | 8 |
| [PF4V1](PF4V1_dossier.md) | A | 92 | Forced expiratory volume in 1-second (FEV1) | 0.00295 | 0 |
| [PGF](PGF_dossier.md) | A | 79 | Diagnoses - main ICD10: M23 Internal derangem... | 0.00302 | 2 |
| [PGK1](PGK1_dossier.md) | A | 155 | Fasting glucose | 0.0119 | 14 |
| [PGLYRP1](PGLYRP1_dossier.md) | A | 72 | Forced vital capacity (FVC) | 0.00637 | 2 |
| [PGLYRP2](PGLYRP2_dossier.md) | A | 81 | Eye problems or disorders: Diabetes related e... | 0.0198 | 0 |
| [PGM1](PGM1_dossier.md) | A | 98 | Cancer code  self-reported: prostate cancer | 6e-04 | 12 |
| [PI3](PI3_dossier.md) | A | 119 | Systolic blood pressure  automated reading | 0.00175 | 5 |
| [PIANP](PIANP_dossier.md) | A | 4 | Neuroticism | 0.134 | 0 |
| [PIP](PIP_dossier.md) | A | 112 | Non-cancer illness code  self-reported: gastr... | 0.00185 | 2 |
| [PIR](PIR_dossier.md) | A | 110 | Diagnoses - main ICD10: N20 Calculus of kidne... | 0.0116 | 1 |
| [PKDCC](PKDCC_dossier.md) | A | 126 | Heel bone mineral density (BMD) T-score  auto... | 2e-35 | 27 |
| [PLA2G2A](PLA2G2A_dossier.md) | A | 80 | Cancer code  self-reported: prostate cancer | 0.00649 | 4 |
| [PLA2R1](PLA2R1_dossier.md) | A | 103 | Age at menopause | 6e-05 | 15 |
| [PLAT](PLAT_dossier.md) | A | 98 | Diagnoses - main ICD10: N81 Female genital pr... | 0.00412 | 4 |
| [PLAU](PLAU_dossier.md) | A | 192 | Crohn's disease | 5e-13 | 10 |
| [PLAUR](PLAUR_dossier.md) | A | 82 | Non-cancer illness code  self-reported: diver... | 0.00398 | 9 |
| [PLEKHA7](PLEKHA7_dossier.md) | A | 96 | Non-cancer illness code  self-reported: hyper... | 1e-04 | 22 |
| [PLG](PLG_dossier.md) | A | 89 | Weight | 5e-04 | 17 |
| [PLXNA1](PLXNA1_dossier.md) | A | 114 | Forced vital capacity (FVC) | 2e-05 | 14 |
| [PLXNB2](PLXNB2_dossier.md) | A | 86 | Heel bone mineral density (BMD) T-score  auto... | 2e-08 | 9 |
| [PLXNC1](PLXNC1_dossier.md) | A | 137 | HOMA-B | 0.0071 | 27 |
| [PMEL](PMEL_dossier.md) | A | 76 | Non-cancer illness code  self-reported: asthma | 1e-06 | 1 |
| [PMP2](PMP2_dossier.md) | A | 82 | Diagnoses - main ICD10: K60 Fissure and fistu... | 0.00134 | 5 |
| [PNLIPRP1](PNLIPRP1_dossier.md) | A | 68 | Coronary heart disease | 2e-06 | 7 |
| [PNLIPRP2](PNLIPRP2_dossier.md) | A | 107 | LDL cholesterol | 4e-04 | 4 |
| [PNPLA3](PNPLA3_dossier.md) | C | 0 |  |  | 30 |
| [POFUT1](POFUT1_dossier.md) | A | 99 | Caudate volume | 5e-04 | 8 |
| [POFUT2](POFUT2_dossier.md) | A | 65 | Diagnoses - main ICD10: K80 Cholelithiasis | 0.00179 | 6 |
| [POGLUT1](POGLUT1_dossier.md) | A | 116 | Happiness | 3e-04 | 3 |
| [POMC](POMC_dossier.md) | A | 82 | Non-cancer illness code  self-reported: high ... | 3e-05 | 19 |
| [POMGNT2](POMGNT2_dossier.md) | A | 215 | Bulimia nervosa | 0.0027 | 17 |
| [PON1](PON1_dossier.md) | A | 116 | Body mass index (BMI) | 0.00996 | 6 |
| [POSTN](POSTN_dossier.md) | A | 77 | Squamous cell lung cancer | 3e-04 | 14 |
| [PPA1](PPA1_dossier.md) | A | 119 | Age at menopause | 6e-05 | 1 |
| [PPBP](PPBP_dossier.md) | A | 104 | Height | 5e-06 | 3 |
| [PPID](PPID_dossier.md) | A | 119 | Ischemic stroke | 6e-04 | 9 |
| [PPIE](PPIE_dossier.md) | A | 104 | Body mass index (BMI) | 0.00424 | 3 |
| [PPIL1](PPIL1_dossier.md) | A | 81 | Cigarettes smoked per day | 0.0192 | 8 |
| [PPP2R3A](PPP2R3A_dossier.md) | A | 103 | Systolic blood pressure  automated reading | 7e-04 | 29 |
| [PPP3CA;PPP3R1](PPP3CA;PPP3R1_dossier.md) | A | 127 | Inflammatory bowel disease | 1e-08 | 0 |
| [PPT1](PPT1_dossier.md) | A | 71 | Pallidum volume | 0.00154 | 13 |
| [PPY](PPY_dossier.md) | A | 63 | Cancer code  self-reported: small intestine o... | 0.00338 | 1 |
| [PRCP](PRCP_dossier.md) | A | 64 | Non-cancer illness code  self-reported: muscl... | 4e-05 | 5 |
| [PRDM1](PRDM1_dossier.md) | A | 96 | Height | 0.00338 | 10 |
| [PRDX6](PRDX6_dossier.md) | A | 116 | Forced vital capacity (FVC) | 5e-04 | 10 |
| [PRELP](PRELP_dossier.md) | A | 66 | Body mass index (BMI) | 0.00196 | 6 |
| [PREP](PREP_dossier.md) | A | 109 | Cardioembolic stroke | 0.0038 | 18 |
| [PROC](PROC_dossier.md) | A | 126 | Non-cancer illness code  self-reported: deep ... | 1e-10 | 23 |
| [PROK2](PROK2_dossier.md) | A | 109 | Diagnoses - main ICD10: I30 Acute pericarditis | 0.00593 | 23 |
| [PRRG1](PRRG1_dossier.md) | A | 118 | Systolic blood pressure  automated reading | 4e-04 | 0 |
| [PRSS2](PRSS2_dossier.md) | A | 165 | Multiple sclerosis | 1e-04 | 4 |
| [PRSS22](PRSS22_dossier.md) | A | 109 | Lung cancer | 0.00211 | 3 |
| [PRSS57](PRSS57_dossier.md) | A | 93 | Eye problems or disorders: Diabetes related e... | 0.00212 | 2 |
| [PRTN3](PRTN3_dossier.md) | A | 58 | Heel bone mineral density (BMD) T-score  auto... | 0.00116 | 5 |
| [PSAP](PSAP_dossier.md) | A | 85 | Diagnoses - main ICD10: R55 Syncope and collapse | 0.00229 | 20 |
| [PSAPL1](PSAPL1_dossier.md) | A | 104 | Anorexia nervosa | 0.00862 | 23 |
| [PSD](PSD_dossier.md) | A | 108 | Forced vital capacity (FVC) | 0.00142 | 8 |
| [PSG3](PSG3_dossier.md) | A | 21 | Clear cell ovarian cancer | 0.00163 | 3 |
| [PSG4](PSG4_dossier.md) | A | 30 | Clear cell ovarian cancer | 9e-04 | 0 |
| [PSMB1](PSMB1_dossier.md) | A | 113 | Age at menarche | 0.0059 | 2 |
| [PSMD5](PSMD5_dossier.md) | A | 64 | Diagnoses - main ICD10: H25 Senile cataract | 0.00381 | 16 |
| [PTGDS](PTGDS_dossier.md) | A | 106 | Non-cancer illness code  self-reported: mania... | 7e-04 | 1 |
| [PTGFRN](PTGFRN_dossier.md) | A | 102 | Non-cancer illness code  self-reported: joint... | 0.00179 | 6 |
| [PTGR1](PTGR1_dossier.md) | A | 54 | Cancer code  self-reported: prostate cancer | 1e-05 | 9 |
| [PTHLH](PTHLH_dossier.md) | A | 124 | Height | 2e-10 | 28 |
| [PTN](PTN_dossier.md) | A | 123 | Alcohol intake frequency | 5e-04 | 17 |
| [PTPN4](PTPN4_dossier.md) | A | 99 | Body mass index (BMI) | 0.00116 | 11 |
| [PTPRU](PTPRU_dossier.md) | A | 83 | Diagnoses - main ICD10: R11 Nausea and vomiting | 0.00116 | 17 |
| [PXDN](PXDN_dossier.md) | A | 76 | Diagnoses - main ICD10: B37 Candidiasis | 0.00214 | 23 |
| [PYY](PYY_dossier.md) | A | 109 | Diagnoses - main ICD10: G47 Sleep disorders | 9e-07 | 3 |
| [PZP](PZP_dossier.md) | A | 112 | Diagnoses - main ICD10: R55 Syncope and collapse | 0.00997 | 9 |
| [QDPR](QDPR_dossier.md) | A | 103 | Transferrin | 7e-04 | 21 |
| [QPCT](QPCT_dossier.md) | A | 80 | Schizophrenia | 8e-04 | 15 |
| [QPCTL](QPCTL_dossier.md) | A | 89 | Non-cancer illness code  self-reported: enlar... | 3e-04 | 12 |
| [QSOX1](QSOX1_dossier.md) | A | 77 | Non-cancer illness code  self-reported: enlar... | 0.00125 | 3 |
| [QSOX2](QSOX2_dossier.md) | A | 85 | Forced vital capacity (FVC) | 4e-06 | 8 |
| [RAB6B](RAB6B_dossier.md) | A | 107 | Transferrin | 2e-05 | 8 |
| [RAD51D](RAD51D_dossier.md) | A | 98 | Body mass index (BMI) | 4e-08 | 17 |
| [RAET1E](RAET1E_dossier.md) | A | 117 | Non-cancer illness code  self-reported: gout | 0.0104 | 0 |
| [RARRES1](RARRES1_dossier.md) | A | 113 | Diagnoses - main ICD10: K43 Ventral hernia | 0.00167 | 12 |
| [RARRES2](RARRES2_dossier.md) | A | 108 | Thyroid cancer | 5e-07 | 1 |
| [RBP4](RBP4_dossier.md) | A | 82 | Non-cancer illness code  self-reported: vitiligo | 3e-04 | 15 |
| [RCAN1](RCAN1_dossier.md) | A | 70 | Diagnoses - main ICD10: R10 Abdominal and pel... | 0.0312 | 7 |
| [RDH16](RDH16_dossier.md) | A | 1 | Cancer code  self-reported: prostate cancer | 0.0225 | 1 |
| [RECQL](RECQL_dossier.md) | A | 106 | Weight | 3e-04 | 16 |
| [REG1A](REG1A_dossier.md) | A | 165 | Non-cancer illness code  self-reported: perni... | 0.00326 | 6 |
| [REG3G](REG3G_dossier.md) | A | 110 | Diagnoses - main ICD10: N81 Female genital pr... | 2e-04 | 19 |
| [REG4](REG4_dossier.md) | A | 55 | Diagnoses - main ICD10: I30 Acute pericarditis | 6e-05 | 3 |
| [RELL1](RELL1_dossier.md) | A | 87 | Lung cancer | 7e-07 | 11 |
| [RELT](RELT_dossier.md) | A | 115 | Forced expiratory volume in 1-second (FEV1) | 3e-07 | 11 |
| [RET](RET_dossier.md) | A | 68 | Hirschsprung's disease | 4e-04 | 17 |
| [RETN](RETN_dossier.md) | A | 205 | Multiple sclerosis | 3e-06 | 1 |
| [RFESD](RFESD_dossier.md) | A | 69 | Diagnoses - main ICD10: D25 Leiomyoma of uterus | 0.00786 | 5 |
| [RGMA](RGMA_dossier.md) | A | 183 | Height | 1e-07 | 27 |
| [RGMB](RGMB_dossier.md) | A | 127 | Creatinine (enzymatic) in urine | 2e-04 | 23 |
| [RIDA](RIDA_dossier.md) | A | 106 | PGC cross-disorder traits | 0.00209 | 5 |
| [RMDN1](RMDN1_dossier.md) | A | 112 | Body mass index (BMI) | 2e-07 | 9 |
| [RNASE1](RNASE1_dossier.md) | A | 94 | Underlying (primary) cause of death: ICD10: E... | 0.00266 | 2 |
| [RNASE2](RNASE2_dossier.md) | A | 68 | Underlying (primary) cause of death: ICD10: E... | 8e-05 | 1 |
| [RNASE3](RNASE3_dossier.md) | A | 71 | ER-positive Breast cancer (Combined Oncoarray... | 0.00379 | 0 |
| [RNASE4](RNASE4_dossier.md) | A | 116 | Hirschsprung's disease | 1e-06 | 5 |
| [RNASE6](RNASE6_dossier.md) | A | 106 | Non-cancer illness code  self-reported: joint... | 0.00549 | 1 |
| [RNPEP](RNPEP_dossier.md) | A | 122 | Diagnoses - main ICD10: I80 Phlebitis and thr... | 0.0017 | 2 |
| [ROR1](ROR1_dossier.md) | A | 65 | Body mass index (BMI) | 0.00245 | 12 |
| [RPIA](RPIA_dossier.md) | A | 57 | Diagnoses - main ICD10: N81 Female genital pr... | 8e-04 | 16 |
| [RPN1](RPN1_dossier.md) | A | 141 | Alzheimer's disease | 2e-05 | 6 |
| [RPRD1A](RPRD1A_dossier.md) | A | 103 | Alcohol intake frequency | 0.00527 | 6 |
| [RRM1](RRM1_dossier.md) | A | 108 | Mean cell haemoglobin | 7e-13 | 1 |
| [RRM2B](RRM2B_dossier.md) | A | 109 | Non-cancer illness code  self-reported: gastr... | 0.0025 | 10 |
| [RSPO3](RSPO3_dossier.md) | A | 140 | Heel bone mineral density (BMD) T-score  auto... | 2e-82 | 18 |
| [RSPO4](RSPO4_dossier.md) | A | 106 | Non-cancer illness code  self-reported: chron... | 0.0102 | 11 |
| [RTN4R](RTN4R_dossier.md) | A | 79 | Non-cancer illness code  self-reported: kidne... | 0.00128 | 4 |
| [S100A4](S100A4_dossier.md) | A | 113 | Diagnoses - main ICD10: D25 Leiomyoma of uterus | 2e-04 | 0 |
| [S100A5](S100A5_dossier.md) | A | 110 | Low grade serous ovarian cancer | 0.00325 | 2 |
| [S100A7](S100A7_dossier.md) | A | 76 | Non-cancer illness code  self-reported: asthma | 0.00151 | 0 |
| [SAA1](SAA1_dossier.md) | A | 290 | Mean cell volume | 8e-04 | 1 |
| [SCARF1](SCARF1_dossier.md) | A | 108 | Depressive symptoms | 0.00596 | 2 |
| [SCARF2](SCARF2_dossier.md) | A | 119 | Forced expiratory volume in 1-second (FEV1) | 4e-06 | 9 |
| [SCG3](SCG3_dossier.md) | A | 110 | Weight | 2e-06 | 12 |
| [SCIN](SCIN_dossier.md) | A | 68 | Sodium in urine | 0.00696 | 17 |
| [SCP2D1](SCP2D1_dossier.md) | A | 99 | Cancer code  self-reported: basal cell carcinoma | 0.00251 | 12 |
| [SCUBE1](SCUBE1_dossier.md) | A | 109 | Urate | 0.00178 | 7 |
| [SECTM1](SECTM1_dossier.md) | A | 118 | Hirschsprung's disease | 0.00629 | 2 |
| [SELL](SELL_dossier.md) | A | 99 | Autism | 9e-04 | 11 |
| [SELP](SELP_dossier.md) | A | 147 | Height | 0.0379 | 10 |
| [SELPLG](SELPLG_dossier.md) | A | 68 | Diagnoses - main ICD10: I84 Haemorrhoids | 0.00547 | 4 |
| [SEMA3C](SEMA3C_dossier.md) | A | 100 | Systolic blood pressure  automated reading | 0.00272 | 28 |
| [SEMA3E](SEMA3E_dossier.md) | A | 86 | Neuroticism | 3e-04 | 21 |
| [SEMA3G](SEMA3G_dossier.md) | A | 119 | HDL cholesterol | 4e-06 | 4 |
| [SEMA4C](SEMA4C_dossier.md) | A | 69 | Schizophrenia | 0.00689 | 0 |
| [SEMA4D](SEMA4D_dossier.md) | A | 81 | Body mass index (BMI) | 0.00136 | 5 |
| [SEMA5A](SEMA5A_dossier.md) | A | 75 | Systolic blood pressure  automated reading | 4e-04 | 30 |
| [SEMG1](SEMG1_dossier.md) | A | 79 | Birth weight | 1e-04 | 0 |
| [SEMG2](SEMG2_dossier.md) | A | 96 | Age at menarche | 9e-08 | 2 |
| [SEPT10](SEPT10_dossier.md) | A | 121 | Childhood intelligence | 0.00239 | 8 |
| [SERPINA1](SERPINA1_dossier.md) | A | 120 | Breast cancer (Combined Oncoarray; iCOGS; GWA... | 0.00172 | 30 |
| [SERPINA10](SERPINA10_dossier.md) | A | 272 | Potassium in urine | 0.00812 | 7 |
| [SERPINA11](SERPINA11_dossier.md) | A | 105 | Fasting insulin | 0.00313 | 8 |
| [SERPINA3](SERPINA3_dossier.md) | A | 111 | Diagnoses - main ICD10: M54 Dorsalgia | 1e-04 | 2 |
| [SERPINA4](SERPINA4_dossier.md) | A | 157 | Non-cancer illness code  self-reported: bladd... | 0.00108 | 1 |
| [SERPIND1](SERPIND1_dossier.md) | A | 116 | LDL cholesterol | 2e-45 | 6 |
| [SERPINE2](SERPINE2_dossier.md) | A | 80 | Non-cancer illness code  self-reported: deep ... | 1e-04 | 5 |
| [SERPINF1](SERPINF1_dossier.md) | A | 105 | Forced vital capacity (FVC) | 3e-07 | 12 |
| [SERPINF2](SERPINF2_dossier.md) | A | 75 | Heel bone mineral density (BMD) T-score  auto... | 0.00255 | 11 |
| [SERPING1](SERPING1_dossier.md) | A | 123 | Schizophrenia | 2e-05 | 25 |
| [SFRP4](SFRP4_dossier.md) | A | 79 | Diagnoses - main ICD10: M16 Coxarthrosis [art... | 1e-04 | 1 |
| [SFTPB](SFTPB_dossier.md) | A | 97 | Lung adenocarcinoma | 6e-06 | 6 |
| [SHANK3](SHANK3_dossier.md) | A | 125 | Coronary heart disease | 0.00303 | 30 |
| [SHBG](SHBG_dossier.md) | A | 124 | Body fat | 7e-05 | 8 |
| [SHISA3](SHISA3_dossier.md) | A | 71 | Eczema | 7e-09 | 9 |
| [SHMT1](SHMT1_dossier.md) | A | 75 | Alcohol intake frequency | 1e-05 | 5 |
| [SIGLEC12](SIGLEC12_dossier.md) | A | 100 | Non-cancer illness code  self-reported: pneum... | 0.00294 | 1 |
| [SIGLEC14](SIGLEC14_dossier.md) | A | 76 | Diagnoses - main ICD10: N40 Hyperplasia of pr... | 0.0239 | 2 |
| [SIGLEC6](SIGLEC6_dossier.md) | A | 110 | Rheumatoid arthritis | 6e-05 | 1 |
| [SIGLEC7](SIGLEC7_dossier.md) | A | 60 | Diagnoses - main ICD10: I84 Haemorrhoids | 0.00147 | 2 |
| [SIGLEC9](SIGLEC9_dossier.md) | A | 112 | Weight | 6e-05 | 3 |
| [SIRPA](SIRPA_dossier.md) | A | 76 | Sodium in urine | 0.00129 | 7 |
| [SIRPB1](SIRPB1_dossier.md) | A | 103 | Neo-neuroticism | 9e-04 | 4 |
| [SIRPG](SIRPG_dossier.md) | A | 106 | Diagnoses - main ICD10: R55 Syncope and collapse | 3e-04 | 10 |
| [SIRT2](SIRT2_dossier.md) | A | 285 | Diagnoses - main ICD10: R11 Nausea and vomiting | 0.00101 | 3 |
| [SLAMF7](SLAMF7_dossier.md) | A | 62 | Ulcerative colitis | 7e-05 | 5 |
| [SLC22A16](SLC22A16_dossier.md) | A | 91 | Non-cancer illness code  self-reported: high ... | 0.0086 | 9 |
| [SLC5A8](SLC5A8_dossier.md) | A | 117 | Triglycerides | 8e-73 | 12 |
| [SLITRK3](SLITRK3_dossier.md) | A | 76 | Non-cancer illness code  self-reported: hayfe... | 0.0155 | 15 |
| [SMIM9](SMIM9_dossier.md) | A | 114 | Vascular or heart problems diagnosed by docto... | 7e-04 | 0 |
| [SMOC1](SMOC1_dossier.md) | A | 99 | Mean cell volume | 7e-06 | 17 |
| [SMPD1](SMPD1_dossier.md) | A | 79 | Non-cancer illness code  self-reported: vitiligo | 0.00296 | 13 |
| [SMPDL3A](SMPDL3A_dossier.md) | A | 109 | Weight | 0.00707 | 11 |
| [SMR3A](SMR3A_dossier.md) | A | 78 | Diagnoses - main ICD10: R11 Nausea and vomiting | 0.00434 | 0 |
| [SNCA](SNCA_dossier.md) | A | 108 | Neuroticism | 7e-06 | 27 |
| [SOCS3](SOCS3_dossier.md) | A | 104 | Forced vital capacity (FVC) | 2e-06 | 4 |
| [SOD3](SOD3_dossier.md) | A | 107 | Diagnoses - main ICD10: R55 Syncope and collapse | 8e-05 | 9 |
| [SPARCL1](SPARCL1_dossier.md) | A | 175 | Diagnoses - main ICD10: Z09 Follow-up examina... | 1e-04 | 7 |
| [SPATA20](SPATA20_dossier.md) | A | 118 | Birth weight | 2e-05 | 1 |
| [SPINK1](SPINK1_dossier.md) | A | 96 | Non-cancer illness code  self-reported: diver... | 0.00489 | 8 |
| [SPINK2](SPINK2_dossier.md) | A | 82 | Squamous cell lung cancer | 2e-06 | 6 |
| [SPINK5](SPINK5_dossier.md) | A | 96 | Total cholesterol | 0.00253 | 8 |
| [SPINK6](SPINK6_dossier.md) | A | 104 | Serum cystatin C (eGFRcys) | 0.00379 | 0 |
| [SPINT1](SPINT1_dossier.md) | A | 108 | Thyroid cancer | 2e-07 | 0 |
| [SPINT2](SPINT2_dossier.md) | A | 118 | Diagnoses - main ICD10: C61 Malignant neoplas... | 6e-04 | 10 |
| [SPINT3](SPINT3_dossier.md) | A | 102 | Non-cancer illness code  self-reported: hyper... | 0.00269 | 3 |
| [SPOCK2](SPOCK2_dossier.md) | A | 120 | Non-cancer illness code  self-reported: pneum... | 4e-04 | 11 |
| [SPOCK3](SPOCK3_dossier.md) | A | 66 | Pallidum volume | 0.00383 | 30 |
| [SPON1](SPON1_dossier.md) | A | 99 | Diastolic blood pressure  automated reading | 9e-07 | 21 |
| [SPON2](SPON2_dossier.md) | A | 109 | Heel bone mineral density (BMD) T-score  auto... | 6e-14 | 12 |
| [ST3GAL1](ST3GAL1_dossier.md) | A | 70 | Diagnoses - main ICD10: R10 Abdominal and pel... | 9e-04 | 21 |
| [ST3GAL6](ST3GAL6_dossier.md) | A | 110 | Diagnoses - main ICD10: R04 Haemorrhage from ... | 6e-04 | 20 |
| [ST6GALNAC6](ST6GALNAC6_dossier.md) | A | 3 | Squamous cell lung cancer | 0.244 | 0 |
| [STIM1](STIM1_dossier.md) | A | 90 | Diagnoses - main ICD10: R04 Haemorrhage from ... | 0.00462 | 25 |
| [STK17B](STK17B_dossier.md) | A | 111 | Myocardial infarction | 5e-04 | 14 |
| [STX10](STX10_dossier.md) | A | 115 | Body mass index (BMI) | 0.00996 | 7 |
| [STX7](STX7_dossier.md) | A | 112 | Serum creatinine (eGFRcrea) | 3e-06 | 6 |
| [SULF2](SULF2_dossier.md) | A | 126 | Non-cancer illness code  self-reported: gout | 7e-23 | 26 |
| [SULT2A1](SULT2A1_dossier.md) | A | 105 | Diagnoses - main ICD10: K80 Cholelithiasis | 2e-06 | 12 |
| [SUMF1](SUMF1_dossier.md) | A | 160 | Potassium in urine | 0.00282 | 22 |
| [SURF1](SURF1_dossier.md) | A | 98 | Diagnoses - main ICD10: D12 Benign neoplasm o... | 0.00342 | 13 |
| [SVEP1](SVEP1_dossier.md) | A | 132 | Diagnoses - main ICD10: B37 Candidiasis | 3e-05 | 15 |
| [SWAP70](SWAP70_dossier.md) | A | 107 | Non-cancer illness code  self-reported: hyper... | 2e-09 | 27 |
| [TAPBPL](TAPBPL_dossier.md) | A | 102 | Forced vital capacity (FVC) | 4e-04 | 3 |
| [TCN1](TCN1_dossier.md) | A | 61 | Hearing difficulty or problems: Yes | 0.0125 | 11 |
| [TCN2](TCN2_dossier.md) | A | 117 | Height | 2e-04 | 15 |
| [TDGF1](TDGF1_dossier.md) | A | 105 | Non-cancer illness code  self-reported: gout | 0.00206 | 7 |
| [TEK](TEK_dossier.md) | A | 103 | Underlying (primary) cause of death: ICD10: E... | 6e-24 | 11 |
| [TEPSIN](TEPSIN_dossier.md) | A | 61 | Non-cancer illness code  self-reported: asthma | 0.00224 | 3 |
| [TEX29](TEX29_dossier.md) | A | 59 | Diagnoses - main ICD10: R55 Syncope and collapse | 0.00124 | 18 |
| [TF](TF_dossier.md) | A | 113 | Transferrin | 0e+00 | 7 |
| [TFF1](TFF1_dossier.md) | A | 69 | Non-cancer illness code  self-reported: vitiligo | 1e-05 | 1 |
| [TFRC](TFRC_dossier.md) | A | 122 | Transferrin Saturation | 1e-80 | 7 |
| [TGFB1](TGFB1_dossier.md) | A | 126 | Height | 4e-08 | 20 |
| [TGFBI](TGFBI_dossier.md) | A | 118 | Femoral neck bone mineral density | 4e-05 | 17 |
| [THBS2](THBS2_dossier.md) | A | 75 | Diagnoses - main ICD10: D25 Leiomyoma of uterus | 0.00118 | 29 |
| [THBS4](THBS4_dossier.md) | A | 78 | Non-cancer illness code  self-reported: sleep... | 0.00234 | 11 |
| [THSD1](THSD1_dossier.md) | A | 54 | Myocardial infarction | 0.00391 | 10 |
| [TIE1](TIE1_dossier.md) | A | 209 | Non-cancer illness code  self-reported: hyper... | 3e-04 | 3 |
| [TIMP1](TIMP1_dossier.md) | A | 97 | Diagnoses - main ICD10: D12 Benign neoplasm o... | 0.00656 | 0 |
| [TIMP2](TIMP2_dossier.md) | A | 123 | Height | 9e-05 | 4 |
| [TIMP3](TIMP3_dossier.md) | A | 110 | Myocardial infarction | 0.00111 | 19 |
| [TIMP4](TIMP4_dossier.md) | A | 119 | Non-cancer illness code  self-reported: hypot... | 1e-05 | 23 |
| [TIRAP](TIRAP_dossier.md) | A | 88 | Diagnoses - main ICD10: N92 Excessive  freque... | 1e-05 | 7 |
| [TLR4;LY96](TLR4;LY96_dossier.md) | A | 178 | Non-cancer illness code  self-reported: hyper... | 0.00606 | 0 |
| [TMED10](TMED10_dossier.md) | A | 121 | Serum cystatin C (eGFRcys) | 1e-197 | 10 |
| [TMEM106B](TMEM106B_dossier.md) | A | 131 | Non-cancer illness code  self-reported: depre... | 3e-08 | 29 |
| [TMEM132A](TMEM132A_dossier.md) | A | 105 | Type 2 diabetes | 0.0165 | 0 |
| [TMEM132B](TMEM132B_dossier.md) | A | 84 | Potassium in urine | 4e-04 | 30 |
| [TMEM132C](TMEM132C_dossier.md) | A | 185 | Ischemic stroke | 0.00358 | 29 |
| [TMEM132D](TMEM132D_dossier.md) | A | 68 | Diagnoses - main ICD10: C50 Malignant neoplas... | 7e-04 | 30 |
| [TMEM190](TMEM190_dossier.md) | A | 86 | Diagnoses - main ICD10: M16 Coxarthrosis [art... | 1e-04 | 1 |
| [TMEM2](TMEM2_dossier.md) | A | 104 | Eye problems or disorders: Glaucoma | 0.00104 | 27 |
| [TNC](TNC_dossier.md) | A | 67 | Body mass index (BMI) | 0.00196 | 26 |
| [TNFAIP6](TNFAIP6_dossier.md) | A | 118 | Diagnoses - main ICD10: S66 Injury of muscle ... | 0.00121 | 6 |
| [TNFRSF10B](TNFRSF10B_dossier.md) | A | 60 | Non-cancer illness code  self-reported: joint... | 0.00109 | 15 |
| [TNFRSF11A](TNFRSF11A_dossier.md) | A | 116 | Paget's disease | 5e-13 | 29 |
| [TNFRSF19](TNFRSF19_dossier.md) | A | 85 | Cancer code  self-reported: small intestine o... | 3e-04 | 9 |
| [TNFRSF1B](TNFRSF1B_dossier.md) | A | 106 | Eye problems or disorders: Injury or trauma r... | 2e-04 | 3 |
| [TNFRSF6B](TNFRSF6B_dossier.md) | A | 5 | Invasive mucinous ovarian cancer | 0.00625 | 25 |
| [TNFSF11](TNFSF11_dossier.md) | A | 42 | Iron | 0.00679 | 17 |
| [TNFSF12;TNFSF12-TNFSF13](TNFSF12;TNFSF12-TNFSF13_dossier.md) | A | 98 | Non-cancer illness code  self-reported: hyper... | 3e-08 | 0 |
| [TNFSF14](TNFSF14_dossier.md) | A | 95 | Cancer code  self-reported: prostate cancer | 0.008 | 6 |
| [TOR1AIP1](TOR1AIP1_dossier.md) | A | 96 | Non-cancer illness code  self-reported: high ... | 0.0098 | 9 |
| [TPPP2](TPPP2_dossier.md) | A | 127 | Height | 3e-08 | 2 |
| [TPSAB1;TPSB2](TPSAB1;TPSB2_dossier.md) | A | 92 | Birth weight | 9e-05 | 0 |
| [TPST1](TPST1_dossier.md) | A | 109 | Weight | 1e-04 | 3 |
| [TPST2](TPST2_dossier.md) | A | 89 | Sodium in urine | 0.00121 | 12 |
| [TREM1](TREM1_dossier.md) | A | 103 | Alzheimer's disease | 0.00201 | 2 |
| [TREM2](TREM2_dossier.md) | A | 51 | Non-cancer illness code  self-reported: perni... | 0.00295 | 10 |
| [TREML1](TREML1_dossier.md) | A | 105 | Vascular or heart problems diagnosed by docto... | 0.00269 | 4 |
| [TREML2](TREML2_dossier.md) | A | 74 | Weight | 9e-04 | 3 |
| [TST](TST_dossier.md) | A | 94 | Diastolic blood pressure  automated reading | 4e-04 | 9 |
| [TXNDC12](TXNDC12_dossier.md) | A | 129 | Inflammatory bowel disease | 1e-19 | 3 |
| [TXNDC15](TXNDC15_dossier.md) | A | 102 | Height | 3e-07 | 4 |
| [TXNDC5](TXNDC5_dossier.md) | A | 104 | Underlying (primary) cause of death: ICD10: E... | 2e-04 | 6 |
| [TYK2](TYK2_dossier.md) | A | 111 | Myocardial infarction | 5e-04 | 20 |
| [TYMP](TYMP_dossier.md) | A | 111 | Mean cell volume | 6e-16 | 7 |
| [TYRO3](TYRO3_dossier.md) | A | 81 | Diastolic blood pressure  automated reading | 3e-06 | 10 |
| [UBASH3B](UBASH3B_dossier.md) | A | 119 | HDL cholesterol | 7e-09 | 23 |
| [UCMA](UCMA_dossier.md) | A | 97 | Non-cancer illness code  self-reported: pneum... | 0.00125 | 10 |
| [UGT1A6](UGT1A6_dossier.md) | A | 115 | Total cholesterol | 7e-10 | 25 |
| [ULBP3](ULBP3_dossier.md) | A | 92 | Alcohol intake frequency | 0.00308 | 2 |
| [UNC5C](UNC5C_dossier.md) | A | 6 | Forearm bone mineral density | 0.08 | 26 |
| [UNC5D](UNC5D_dossier.md) | A | 110 | Alcohol intake frequency | 3e-04 | 28 |
| [UROS](UROS_dossier.md) | A | 80 | Thalamus volume | 0.00994 | 3 |
| [UST](UST_dossier.md) | A | 117 | Platelet count | 0.00135 | 25 |
| [UXS1](UXS1_dossier.md) | A | 85 | Diastolic blood pressure  automated reading | 1e-05 | 11 |
| [VAV1](VAV1_dossier.md) | A | 91 | Alzheimer's disease | 0.00268 | 0 |
| [VCAM1](VCAM1_dossier.md) | A | 142 | Non-cancer illness code  self-reported: hypot... | 2e-161 | 3 |
| [VEGFA](VEGFA_dossier.md) | A | 112 | Body mass index (BMI) | 0.01 | 4 |
| [VEGFC](VEGFC_dossier.md) | A | 58 | Non-cancer illness code  self-reported: joint... | 0.00875 | 18 |
| [VIT](VIT_dossier.md) | A | 91 | Diagnoses - main ICD10: S66 Injury of muscle ... | 3e-04 | 11 |
| [VSIG2](VSIG2_dossier.md) | A | 95 | Height | 5e-04 | 15 |
| [VSIR](VSIR_dossier.md) | A | 93 | Body fat | 0.00367 | 3 |
| [VTN](VTN_dossier.md) | C | 0 |  |  | 7 |
| [VWA2](VWA2_dossier.md) | A | 111 | Pallidum volume | 1e-04 | 13 |
| [VWC2](VWC2_dossier.md) | A | 113 | Chronic kidney disease | 0.0027 | 18 |
| [WARS](WARS_dossier.md) | A | 126 | Age at menarche | 2e-05 | 11 |
| [WFDC1](WFDC1_dossier.md) | A | 103 | Age at menarche | 8e-04 | 4 |
| [WFDC5](WFDC5_dossier.md) | A | 107 | Height | 1e-05 | 2 |
| [WFIKKN1](WFIKKN1_dossier.md) | A | 103 | Diagnoses - main ICD10: R07 Pain in throat an... | 0.012 | 0 |
| [WFIKKN2](WFIKKN2_dossier.md) | A | 119 | Weight | 4e-07 | 5 |
| [WISP1](WISP1_dossier.md) | A | 109 | Rheumatoid arthritis | 1e-04 | 11 |
| [WISP2](WISP2_dossier.md) | A | 104 | Cancer code  self-reported: small intestine o... | 3e-04 | 1 |
| [XCL1](XCL1_dossier.md) | A | 123 | Cancer code  self-reported: prostate cancer | 0.0169 | 8 |
| [XPNPEP2](XPNPEP2_dossier.md) | A | 121 | Urate | 2e-08 | 4 |
| [XRCC4](XRCC4_dossier.md) | A | 52 | Lung adenocarcinoma | 0.00522 | 22 |
| [XXYLT1](XXYLT1_dossier.md) | A | 69 | Non-cancer illness code  self-reported: bone ... | 0.00136 | 19 |
| [ZG16B](ZG16B_dossier.md) | A | 100 | Age at menopause | 0.0124 | 2 |

---

*Generated from `dossiers/master_index.csv` by the proteome sweep. To rebuild:
`python proteome_sweep.py`. To generate a full evidence card (verdict + reasoning) for any
protein-disease pair, see the [main README](../README.md) — that path uses a Gemini key;
these pages do not.*
