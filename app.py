"""OpenCausal — the web app.

WHY THIS WORKS WITH NO KEY AND NO SETUP
---------------------------------------
The evidence card is rendered by code from the tool ledger, not written by a model
(see render.py). All nine sources are public APIs that need no key. So a visitor can
type any protein-disease pair and get the complete card — table, strength grading,
declared caveats, sources with database releases, and the verbatim tool returns —
without an account, a key, or a cent of cost.

The ONLY thing a model contributes is the one-line verdict and one paragraph. That is
optional here: paste your own Gemini key in the sidebar and the app adds those two
sentences AND runs the validator against them, which is the part worth watching.

Run locally:
    streamlit run app.py
"""
from __future__ import annotations

import json
import os
import re
from pathlib import Path

import pandas as pd
import streamlit as st

from ledger import ToolLedger
from render import render_card
from validate_card import validate, format_report

from tools import TOOLS
from tools.uniprot import get_uniprot_dossier
from tools.opentargets import get_target_disease_evidence
from tools.chembl import get_chembl_modulators
from tools.mr import get_mr_result
from tools.clinvar import get_clinvar_variants
from tools.gnomad import get_gnomad_constraint
from tools.gwas import get_gwas_catalog
from tools.pharmgkb import get_pharmgkb_drug_gene
from tools.clinical import get_clinical_evidence
from tools.concordance import classify_evidence_concordance

HERE = Path(__file__).resolve().parent
MODEL_DEFAULT = "gemini-flash-lite-latest"

NO_MODEL_VERDICT = (
    "no verdict — no model was called in this run. Everything below was retrieved and "
    "rendered by code."
)
NO_MODEL_REASONING = (
    "_The verdict sentence and this paragraph are the only things a model ever writes "
    "on this card. No model ran here, so both are absent — and nothing else on the card "
    "changes because of that._"
)

# Which tools run, in which order, and with which arguments. The model normally picks;
# without a model we simply call all nine, which is what it converges on anyway.
PLAN = [
    (get_mr_result, "protein_disease"),
    (get_clinical_evidence, "protein_disease"),
    (get_target_disease_evidence, "protein_disease"),
    (get_uniprot_dossier, "protein"),
    (get_chembl_modulators, "protein"),
    (get_clinvar_variants, "protein"),
    (get_gnomad_constraint, "protein"),
    (get_gwas_catalog, "protein"),
    (get_pharmgkb_drug_gene, "protein"),
]


def _run_tools(protein: str, disease: str, progress=None) -> ToolLedger:
    """Call the nine public sources through the ledger, then classify concordance."""
    ledger = ToolLedger(TOOLS)
    for i, (fn, kind) in enumerate(PLAN):
        if progress is not None:
            progress.progress((i + 1) / (len(PLAN) + 1), text=f"querying {fn.__name__} …")
        # ToolLedger._wrap never raises: a crashed tool comes back as {"error": ...}.
        # So a dead API is detected on the RESULT, not with try/except.
        if kind == "protein_disease":
            res = ledger._wrap(fn)(protein, disease)
        else:
            res = ledger._wrap(fn)(protein)
        if isinstance(res, dict) and res.get("error"):
            st.warning(f"{fn.__name__}: {res['error']}")

    mr_res = ledger.results_by_tool().get("get_mr_result")
    if isinstance(mr_res, dict) and not mr_res.get("error"):
        res = ledger._wrap(classify_evidence_concordance)(protein, disease, mr_result=mr_res)
        if isinstance(res, dict) and res.get("error"):
            st.warning(f"classify_evidence_concordance: {res['error']}")
    if progress is not None:
        progress.progress(1.0, text="rendering the card …")
    return ledger


def _model_sentences(api_key: str, model: str, protein: str, disease: str, ledger):
    """Optional: let Gemini write the two sentences, given what was already retrieved."""
    from google import genai
    from google.genai import types
    from agent import WRITER_INSTRUCTION, split_model_output

    # The CLI prompt orders the model to CALL tools; here the tools were already run and
    # no tool is declared, so that order must be overridden or the reply goes off-format.
    system_prompt = (
        (HERE / "system_prompt.md").read_text(encoding="utf-8")
        + "\n\nOVERRIDE FOR THIS RUN: the tools have already been called for you; their "
        "verbatim results are in the user message. Do NOT attempt to call any tool — "
        "read the results and write the two blocks."
    )
    evidence = json.dumps(ledger.results_by_tool(), ensure_ascii=False, default=str)[:120_000]
    client = genai.Client(api_key=api_key)
    resp = client.models.generate_content(
        model=model,
        contents=(
            f"Protein: {protein}\nDisease: {disease}\n\n"
            "These are the tool results already retrieved for this pair. Do not invent "
            "anything that is not in them.\n\n" + evidence
        ),
        config=types.GenerateContentConfig(
            system_instruction=system_prompt + "\n\n" + WRITER_INSTRUCTION,
        ),
    )
    return split_model_output(resp.text or "")


# ---------------------------------------------------------------------------------
# page
# ---------------------------------------------------------------------------------
st.set_page_config(page_title="OpenCausal — target evidence card",
                   page_icon="🧬", layout="wide")

st.title("🧬 OpenCausal — target evidence card")
st.caption(
    "Type a protein and a disease. Nine public databases are queried live, and the card "
    "below is assembled **by code** from what came back — every number traceable to the "
    "tool and database release it came from. No account, no key, no cost."
)

with st.sidebar:
    st.header("Optional: add a model")
    st.markdown(
        "The card needs no model. A model only writes the **verdict line** and one "
        "paragraph — and then a validator checks both against the retrieval.\n\n"
        "Paste your own Gemini key to switch that on. It is used for this run only and "
        "never stored."
    )
    api_key = st.text_input("Gemini API key (optional)", type="password",
                            help="Free key: https://aistudio.google.com/apikey")
    model = st.text_input("Model", value=MODEL_DEFAULT)
    st.divider()
    st.markdown(
        "**Sources** — all free, all keyless\n\n"
        "EpiGraphDB · Open Targets · ChEMBL · UniProt · ClinVar · gnomAD · "
        "GWAS Catalog · ClinPGx · clinical development record"
    )
    st.markdown(
        "[991 pre-built protein pages](https://ds4cabs.github.io/CausalSentinel/dossiers/) · "
        "[worked examples](https://ds4cabs.github.io/CausalSentinel/viewer/)"
    )

EXAMPLES = [
    ("PCSK9", "high cholesterol"),
    ("IL6R", "coronary heart disease"),
    ("PNPLA3", "MASLD"),
    ("LPA", "coronary heart disease"),
]

st.session_state.setdefault("protein_in", "PCSK9")
st.session_state.setdefault("disease_in", "high cholesterol")


def _set_pair(p: str, d: str) -> None:
    # Widget state must be changed via a callback, BEFORE the widgets render.
    st.session_state.protein_in = p
    st.session_state.disease_in = d


cols = st.columns(len(EXAMPLES))
for c, (p, d) in zip(cols, EXAMPLES):
    c.button(f"{p} × {d}", use_container_width=True, on_click=_set_pair, args=(p, d))

c1, c2 = st.columns(2)
protein = c1.text_input("Protein / gene symbol", key="protein_in")
disease = c2.text_input("Disease", key="disease_in")
go = st.button("Build the evidence card", type="primary", use_container_width=True)

# Build on click; keep the result in session state so it SURVIVES reruns —
# without this, clicking the Download button (which reruns the script) wipes the card.
if go:
    if not protein.strip() or not disease.strip():
        st.error("Give both a protein and a disease.")
        st.stop()

    bar = st.progress(0.0, text="starting …")
    ledger = _run_tools(protein.strip(), disease.strip(), bar)
    bar.empty()

    verdict, reasoning = NO_MODEL_VERDICT, NO_MODEL_REASONING
    validation = None
    if api_key.strip():
        with st.spinner("the model is writing its two sentences …"):
            try:
                verdict, reasoning = _model_sentences(api_key.strip(), model.strip(),
                                                      protein.strip(), disease.strip(), ledger)
                validation = validate(verdict + "\n" + reasoning, ledger)
            except Exception as exc:  # noqa: BLE001
                st.error(f"Model call failed — showing the card without it. ({exc})")
                verdict, reasoning = NO_MODEL_VERDICT, NO_MODEL_REASONING

    card_md = render_card(protein.strip(), disease.strip(), ledger, reasoning, verdict,
                          model.strip() if validation else "none — no model was called")
    if validation is not None and not validation["ok"]:
        card_md += (
            "\n> **VALIDATION FAILED** — the model wrote claim tokens with no support "
            "in tool output:\n"
            + "\n".join(f"> - [{u['kind']}] `{u['token']}`"
                        for u in validation["unsupported"]) + "\n"
        )

    st.session_state["last_run"] = {
        "protein": protein.strip(),
        "disease": disease.strip(),
        "card_md": card_md,
        "entries": ledger.entries,
        "validation": validation,
    }

run = st.session_state.get("last_run")
if run:
    validation = run["validation"]
    if validation is not None:
        if validation["ok"]:
            st.success("✅ VALIDATOR PASSED — " + format_report(validation))
        else:
            st.error("❌ VALIDATION FAILED — every flagged word is something the model "
                     "wrote that the retrieval does not support:")
            st.table(pd.DataFrame(validation["unsupported"]))
    else:
        st.info("No model was called. Everything below is retrieval, rendered by code — "
                "which is the point: the card does not depend on a model.")

    st.markdown("---")
    st.markdown(run["card_md"])

    with st.expander(f"🔎 The ledger — every call and its verbatim return "
                     f"({len(run['entries'])} calls)"):
        for e in run["entries"]:
            st.markdown(f"**`{e.get('tool')}`** · args: `{e.get('args')}`")
            st.json(e.get("result"), expanded=False)

    stem = f"{run['protein']}_{re.sub(r'[^A-Za-z0-9]+', '-', run['disease']).strip('-')}"
    st.download_button("⬇️ Download this card (Markdown)",
                       data=run["card_md"].encode("utf-8"),
                       file_name=f"{stem}_evidence_card.md", mime="text/markdown")
else:
    st.info("Pick an example above or type your own pair, then press "
            "**Build the evidence card**.")
