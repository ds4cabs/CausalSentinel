# OpenSentinel Project Summary

## Person & Context
**Natalie Huang** — UC Davis undergraduate with self-reported beginner Python skills, assigned a **2-week (~26 hour)** internship building a drug-comparison agent.

## Tasks & Deliverables

**Primary deliverable:** A working Gemini AI agent that accepts two drug names and produces comparison outputs.

**Specific outputs required:**
- Side-by-side comparison table of molecular properties and safety signals
- 3–5 sentence AI summary identifying property-safety patterns
- Minimum 2 example runs documented (e.g., aspirin vs. ibuprofen)
- README (screenshots of the app are sufficient; demo video optional/stretch)

**Agent functionality:** The system must autonomously call 2 database tools per submitted drug and assemble results into a structured table.

## Tools & Skills Required

**Database integrations (2 mandatory):**
- PubChem PUG REST for molecular properties (MW, LogP, formula, etc. — pulled directly from the API response, no local RDKit computation needed)
- openFDA FAERS for adverse events

**Technical stack:** Python, Streamlit, `google-generativeai`, requests library

**Programming paradigm:** "Computation Engine — Streamlit form (paste drug names) → side-by-side comparison table"

## Timeline & Structure

| Week | Duration | Focus |
|------|----------|-------|
| 1 | ~12h | Learn PubChem + FAERS APIs and Gemini basics; pair programming to build skeleton from starter template |
| 2 | ~14h | Wire up Streamlit table + AI summary, test with 2 example runs, write README |

## Critical Success Factors

The plan explicitly depends on: (a) a shared starter template existing before week 1, and (b) **Shucheng (PhD mentor) paired as technical guide** through week 2.

## Stretch Goals (optional, not required for MVP)

- ChEMBL REST for additional drug info
- openFDA Drugs@FDA for boxed warnings
- RDKit-based property computation

## Out of Scope

BindingDB, LiverTox, toxicity classifiers, 50-drug calibration, withdrawn-drug validation, and 200+ drug pathways analysis—deliberately excluded to fit beginner timeline.
