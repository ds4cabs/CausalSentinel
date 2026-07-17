# Natalie — Documented Example Runs

Each run below was produced by the Natalie Gemini agent. For every comparison the agent autonomously made **4 database tool calls** (PubChem molecular properties + openFDA safety signals, for each of the two drugs), assembled the table, then wrote the AI summary.


---

## Example 1: aspirin vs ibuprofen

**Autonomous tool calls made (4):**

  1. `natalie_get_molecular_properties("aspirin")`
  2. `natalie_get_safety_signals("aspirin")`
  3. `natalie_get_molecular_properties("ibuprofen")`
  4. `natalie_get_safety_signals("ibuprofen")`


### Comparison table

| Category | Property | aspirin | ibuprofen |
| --- | --- | --- | --- |
| Category | PubChem CID | 2244 | 3672 |
| Molecular | Molecular formula | C9H8O4 | C13H18O2 |
| Molecular | Molecular weight | 180.16 g/mol | 206.28 g/mol |
| Molecular | LogP (lipophilicity) | 1.2 | 3.5 |
| Molecular | H-bond donors | 1 | 1 |
| Molecular | H-bond acceptors | 4 | 2 |
| Molecular | Polar surface area (TPSA) | 63.6 Å² | 37.3 Å² |
| Molecular | Rotatable bonds | 3 | 4 |
| Safety | Boxed (black-box) warning | No | No |
| Safety | Total adverse-event reports | 1,108,094 | 522,477 |
| Safety | Top reported adverse reactions | Fatigue (38,025); Dyspnoea (31,831); Nausea (31,454); Diarrhoea (31,179); Drug Ineffective (26,657) | Drug Ineffective (16,909); Pain (15,923); Fatigue (15,075); Nausea (14,241); Headache (12,779) |


### AI summary

Ibuprofen’s higher lipophilicity (LogP of 3.5 vs. 1.2 for aspirin) and lower polar surface area (37.3 Å² vs. 63.6 Å²) link to a safety profile featuring headache (12,779 reports) in its top reactions, an effect not seen in aspirin's top list. Conversely, aspirin’s smaller molecular weight of 180.16 g/mol and higher hydrogen-bond acceptor count of 4 (compared to ibuprofen's 206.28 g/mol and 2 acceptors) are associated with a much higher volume of safety signals, totaling 1,108,094 adverse-event reports compared to ibuprofen's 522,477. While neither drug carries a boxed warning, their differing molecular structures—such as aspirin having 3 rotatable bonds and ibuprofen having 4—pattern with distinct top adverse reactions like dyspnoea (31,831 reports) for aspirin and pain (15,923 reports) for ibuprofen. Despite these differing molecular properties, both drugs still share nausea as a top adverse reaction, resulting in 31,454 reports for aspirin and 14,241 reports for ibuprofen.


---

## Example 2: acetaminophen vs naproxen

**Autonomous tool calls made (4):**

  1. `natalie_get_molecular_properties("acetaminophen")`
  2. `natalie_get_safety_signals("acetaminophen")`
  3. `natalie_get_molecular_properties("naproxen")`
  4. `natalie_get_safety_signals("naproxen")`


### Comparison table

| Category | Property | acetaminophen | naproxen |
| --- | --- | --- | --- |
| Category | PubChem CID | 1983 | 156391 |
| Molecular | Molecular formula | C8H9NO2 | C14H14O3 |
| Molecular | Molecular weight | 151.16 g/mol | 230.26 g/mol |
| Molecular | LogP (lipophilicity) | 0.5 | 3.3 |
| Molecular | H-bond donors | 2 | 1 |
| Molecular | H-bond acceptors | 2 | 3 |
| Molecular | Polar surface area (TPSA) | 49.3 Å² | 46.5 Å² |
| Molecular | Rotatable bonds | 1 | 3 |
| Safety | Boxed (black-box) warning | No | Yes ⚠️ |
| Safety | Total adverse-event reports | 1,191,130 | 387,838 |
| Safety | Top reported adverse reactions | Drug Dependence (51,167); Overdose (44,695); Pain (42,153); Dependence (36,997); Death (29,509) | Drug Ineffective (12,614); Pain (10,867); Fatigue (9,645); Arthralgia (9,063); Nausea (9,056) |


### AI summary

Acetaminophen's smaller molecular weight (151.16 g/mol) and low lipophilicity (LogP of 0.5) link to a safety profile devoid of a boxed warning but dominated by high-volume toxicity signals, including 1,191,130 total adverse-event reports with prominent counts for overdose (44,695) and death (29,509). Conversely, naproxen’s larger molecular weight (230.26 g/mol) and significantly higher lipophilicity (LogP of 3.3) associate with a boxed warning and a lower volume of 387,838 total reports. This higher lipophilicity and greater molecular flexibility (3 rotatable bonds compared to acetaminophen's 1) correlate with a safety profile characterized by systemic tolerability issues like fatigue (9,645 reports) and nausea (9,056 reports). Finally, despite having similar polar surface areas (49.3 Å² for acetaminophen and 46.5 Å² for naproxen), their differing hydrogen bond donor counts (2 for acetaminophen and 1 for naproxen) underscore how distinct chemical structures align with acetaminophen's association with drug dependence (51,167 reports) versus naproxen's primary report of the drug being ineffective (12,614 reports).
