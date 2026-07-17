# OpenSentinel — MVP Version (Gemini AI Agent · Computation Engine, Beginner-Scaffolded)

**Intern:** Natalie Huang (黄心怡)
**Level:** UC Davis undergrad, **Beginner Python**
**Timeline:** 2–3 weeks (~40 hours)
**Paradigm:** **Computation Engine** — Streamlit form (paste drug names) → side-by-side comparison table of molecular properties and safety signals.
**Database count:** **4** (deliberately held at the minimum because Natalie self-reported as Beginner. Adding more would compromise her ability to ship a working agent in 3 weeks).

---

## The Agent

**What the agent does (autonomous workflow on submit):** Agent autonomously calls 4 tools per drug, assembles a comparison table, produces a 3-5 sentence summary noting property-safety patterns.

**Input:** Comma-separated drug names via Streamlit text input.
**Output:** Comparison table + short AI summary.

**Tools (4 public databases):**

1. `get_molecular_properties(drug_name)` — **PubChem PUG REST** + **RDKit**: MW, logP, HBD, HBA, TPSA.
2. `get_faers_events(drug_name, year=2024)` — **openFDA FAERS**: total reports + top 5 adverse events.
3. `get_chembl_drug_info(drug_name)` — **ChEMBL REST**: max approval phase, mechanism, indication class.
4. `get_drug_label(drug_name)` — **openFDA Drugs@FDA**: boxed warnings.

**Example runs (≥3):**

- *Form input:* "aspirin, ibuprofen". *Output:* comparison table + 3-sentence note.
- *Form input:* "atorvastatin, simvastatin". *Output:* table noting same-class similarity.
- *Form input:* "metformin". *Output:* single-drug profile.

---

## Week-by-Week

**Week 1 (~12h) — Learning Week.** RDKit tutorial + Gemini quickstart. Pair-program with Shucheng (PhD team-mate).
**Week 2 (~15h):** Clone cohort starter template (engine sub-template). Fill in 4 tool functions.
**Week 3 (~13h):** Run on 5 inputs; tune system prompt with Shucheng's help; README + 1-min demo.

## What's OUT

BindingDB, LiverTox, Open Targets, GTEx, HPA; toxicity classifier; 50-drug calibration; 30 withdrawn-drug validation; environmental toxins; 200 drugs × 15 pathways.

## Stretch Goals

- 5th tool (only if MVP done early): `get_sider_side_effects(drug)` for label-derived side effects.

## Realistic CV Entry

*Built OpenSentinel, a working Gemini AI computation-engine agent for preclinical drug-property and adverse-event comparison.*

- Wrapped 4 public databases (PubChem + RDKit, openFDA FAERS, ChEMBL, openFDA Drugs@FDA) into a Gemini agent producing side-by-side comparison tables.
- Delivered within a 3-week beginner-scaffolded scope as foundation for the team's full safety-screening module.

## Tech Stack

Python (Jupyter + scripts), `google-generativeai`, Streamlit, RDKit, requests, openFDA, ChEMBL, PubChem.

---

## Note for the program lead

Deliberately held at 4 databases (the cohort minimum) given Natalie's Beginner Python self-report. The plan succeeds only if (a) Christina's shared starter template exists before week 1 and (b) Shucheng is paired with her as technical mentor through week 3.

---

## Shared Agent Skeleton (three paradigms, one Gemini primitive)

Every intern's agent uses Gemini's automatic function calling, but the interface layer differs by paradigm. The cohort uses **one starter repo with three sub-templates** that interns clone in week 1:

- **Dossier-generator template** — CLI script: takes structured args, runs the agent workflow autonomously, writes `*.md` + `*.json` to disk. Used by Beyza, Chin Hung, Christina, Shucheng, Xiaoxue.
- **Dashboard template** — Streamlit page with selectors and tables; the agent is invoked on button-click for specific synthesis tasks. Used by Aaron, Jason, Shawn.
- **Computation-engine template** — Streamlit form (or CLI) that takes structured analytical inputs, runs the agent workflow, produces a downloadable analytical report with plots. Used by Reuben, Kening, Natalie.

**Why no chat interfaces?** Scientists need reproducible, shareable artifacts. The agent dimension (Gemini-as-orchestrator, autonomous tool-calling across multiple public databases, synthesis across sources) is preserved in all three paradigms; only the deliverable shape changes.

**Christina** (OpenRepurpose evidence-and-validation module) owns the starter repo with all three sub-templates. The shared repo should also include pre-built wrappers for the most heavily-used databases (ChEMBL, openFDA FAERS, Open Targets, ClinVar) so multiple interns don't redo the same boilerplate.

### Reference snippet — Gemini function calling (same across all three paradigms)

```python
import google.generativeai as genai
import os
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def my_tool(arg: str) -> dict:
    """One-line docstring Gemini uses to decide when to call this tool."""
    return {"result": ...}

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    tools=[my_tool, other_tool, ...],   # 4-8 tools per agent
    system_instruction=open("system_prompt.md").read(),
)
chat = model.start_chat(enable_automatic_function_calling=True)
response = chat.send_message("structured request — one shot, not a conversation")
```
