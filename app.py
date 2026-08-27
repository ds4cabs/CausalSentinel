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
# page — one site, three tabs: build a card / ten worked cards / the 991 gallery
# ---------------------------------------------------------------------------------
st.set_page_config(page_title="OpenCausal", page_icon="\U0001f9ec", layout="wide")

# Look & feel: the deck palette (DEEP #065A82 / TEAL #1C7293), quieter chrome.
st.markdown("""
<style>
#MainMenu, footer, [data-testid="stToolbar"] {visibility: hidden;}
.block-container {padding-top: 1.1rem; max-width: 1200px;}
.oc-hero {background: linear-gradient(90deg, #065A82, #1C7293); border-radius: 14px;
          padding: 20px 28px; color: #fff; margin-bottom: 10px;}
.oc-hero h1 {color: #fff; font-size: 2.0rem; margin: 0 0 6px 0;}
.oc-hero p  {color: #DCE9F2; margin: 0; font-size: 0.97rem;}
.stTabs [data-baseweb="tab"] {font-size: 1.02rem; font-weight: 600;}
</style>
<div class="oc-hero">
  <h1>\U0001f9ec OpenCausal</h1>
  <p>One protein \u00d7 one disease \u2192 one evidence card you can check, line by line.
     Nine public databases, queried live, rendered by code \u2014 no account, no key, no cost.</p>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.header("Optional: add a model")
    st.markdown(
        "The card needs no model. A model only writes the **verdict line** and one "
        "paragraph \u2014 and then a validator checks both against the retrieval.\n\n"
        "Paste your own Gemini key to switch that on. It is used for this run only and "
        "never stored."
    )
    api_key = st.text_input("Gemini API key (optional)", type="password",
                            help="Free key: https://aistudio.google.com/apikey")
    model = st.text_input("Model", value=MODEL_DEFAULT)
    st.divider()
    st.markdown(
        "**Sources** \u2014 all free, all keyless\n\n"
        "EpiGraphDB \u00b7 Open Targets \u00b7 ChEMBL \u00b7 UniProt \u00b7 ClinVar \u00b7 gnomAD \u00b7 "
        "GWAS Catalog \u00b7 ClinPGx \u00b7 clinical development record"
    )
    st.markdown(
        "Also online: [protein gallery](https://ds4cabs.github.io/CausalSentinel/dossiers/) \u00b7 "
        "[card viewer](https://ds4cabs.github.io/CausalSentinel/viewer/)"
    )

tab_build, tab_viewer, tab_gallery = st.tabs(
    ["\U0001f528 Build a card", "\U0001f5c2\ufe0f Ten worked cards", "\U0001f9ed 991-protein gallery"])

# ================================ tab 1: build ====================================
with tab_build:
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
        c.button(f"{p} \u00d7 {d}", use_container_width=True, on_click=_set_pair, args=(p, d))

    c1, c2 = st.columns(2)
    protein = c1.text_input("Protein / gene symbol", key="protein_in")
    disease = c2.text_input("Disease", key="disease_in")
    go = st.button("Build the evidence card", type="primary", use_container_width=True)

    # Build on click; keep the result in session state so it SURVIVES reruns \u2014
    # without this, clicking the Download button (which reruns the script) wipes the card.
    if go:
        if not protein.strip() or not disease.strip():
            st.error("Give both a protein and a disease.")
            st.stop()

        bar = st.progress(0.0, text="starting \u2026")
        ledger = _run_tools(protein.strip(), disease.strip(), bar)
        bar.empty()

        verdict, reasoning = NO_MODEL_VERDICT, NO_MODEL_REASONING
        validation = None
        if api_key.strip():
            with st.spinner("the model is writing its two sentences \u2026"):
                try:
                    verdict, reasoning = _model_sentences(api_key.strip(), model.strip(),
                                                          protein.strip(), disease.strip(),
                                                          ledger)
                    validation = validate(verdict + "\n" + reasoning, ledger)
                except Exception as exc:  # noqa: BLE001
                    st.error(f"Model call failed \u2014 showing the card without it. ({exc})")
                    verdict, reasoning = NO_MODEL_VERDICT, NO_MODEL_REASONING

        card_md = render_card(protein.strip(), disease.strip(), ledger, reasoning, verdict,
                              model.strip() if validation else "none \u2014 no model was called")
        if validation is not None and not validation["ok"]:
            card_md += (
                "\n> **VALIDATION FAILED** \u2014 the model wrote claim tokens with no support "
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
                st.success("\u2705 VALIDATOR PASSED \u2014 " + format_report(validation))
            else:
                st.error("\u274c VALIDATION FAILED \u2014 every flagged word is something the "
                         "model wrote that the retrieval does not support:")
                st.table(pd.DataFrame(validation["unsupported"]))
        else:
            st.info("No model was called. Everything below is retrieval, rendered by code "
                    "\u2014 which is the point: the card does not depend on a model.")

        st.markdown("---")
        st.markdown(run["card_md"])

        with st.expander(f"\U0001f50e The ledger \u2014 every call and its verbatim return "
                         f"({len(run['entries'])} calls)"):
            for e in run["entries"]:
                st.markdown(f"**`{e.get('tool')}`** \u00b7 args: `{e.get('args')}`")
                st.json(e.get("result"), expanded=False)

        stem = f"{run['protein']}_{re.sub(r'[^A-Za-z0-9]+', '-', run['disease']).strip('-')}"
        st.download_button("\u2b07\ufe0f Download this card (Markdown)",
                           data=run["card_md"].encode("utf-8"),
                           file_name=f"{stem}_evidence_card.md", mime="text/markdown")
    else:
        st.info("Pick an example above or type your own pair, then press "
                "**Build the evidence card**.")

# ============================ tab 2: ten worked cards =============================
@st.cache_data(show_spinner=False)
def _load_worked_cards() -> dict:
    """The ten benchmark cards, loaded from cards/*.json (each carries its full ledger)."""
    out = {}
    for f in sorted((HERE / "cards").glob("*_evidence_card.json")):
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        out[f"{d.get('protein')} \u00d7 {d.get('disease')}"] = d
    return out

with tab_viewer:
    cards = _load_worked_cards()
    if not cards:
        st.info("No pre-built cards found in cards/.")
    else:
        pick = st.selectbox("Ten pairs, chosen to exercise different behaviours \u2014 "
                            "positive controls, no-MR-available, safety cases, a negative "
                            "control:", list(cards))
        d = cards[pick]
        val = d.get("validation") or {}
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("tool calls", len(d.get("tool_ledger") or []))
        m2.metric("validator", "PASS" if val.get("ok") else "FAIL")
        m3.metric("checked claim tokens", val.get("checked", 0))
        m4.metric("generated", (d.get("generated_at") or "")[:10])
        v = (d.get("model_verdict") or "").strip()
        if v.startswith("GO"):
            st.success(v)
        elif v.startswith("NO-GO"):
            st.error(v)
        else:
            st.info(v or "no verdict on record")
        t_card, t_tools = st.tabs(["The card", "Per-tool panels \u2014 the verbatim ledger"])
        with t_card:
            st.markdown(d.get("card_markdown") or "_no markdown stored_")
        with t_tools:
            for e in d.get("tool_ledger") or []:
                with st.expander(f"{e.get('tool')} \u00b7 args {e.get('args')}"):
                    st.json(e.get("result"), expanded=False)
        st.caption("The same ten cards with timelines: "
                   "[online viewer](https://ds4cabs.github.io/CausalSentinel/viewer/)")

# ============================ tab 3: the 991 gallery ==============================
@st.cache_data(show_spinner=False)
def _gallery_index() -> "pd.DataFrame":
    return pd.read_csv(HERE / "dossiers" / "master_index.csv", encoding="utf-8-sig")

with tab_gallery:
    try:
        idx = _gallery_index()
    except OSError:
        idx = None
    if idx is None or idx.empty:
        st.info("dossiers/master_index.csv not found \u2014 run proteome_sweep.py first.")
    else:
        g1, g2, g3 = st.columns(3)
        g1.metric("proteins", len(idx))
        g2.metric("retrieved MR estimate rows", f"{int(idx['n_mr_outcomes'].fillna(0).sum()):,}")
        g3.metric("with published MR (tier A)", int((idx["tier"] == "A").sum()))

        f1, f2 = st.columns([2, 1])
        q = f1.text_input("Filter proteins", placeholder="e.g. IL6R, ACE, PCSK9 \u2026")
        tiers = f2.multiselect("MR feasibility tier", sorted(idx["tier"].dropna().unique()),
                               default=[])
        view = idx
        if q.strip():
            view = view[view["protein"].str.contains(q.strip(), case=False, na=False)]
        if tiers:
            view = view[view["tier"].isin(tiers)]

        SHOW = ["protein", "tier", "n_mr_outcomes", "top_mr_outcome", "top_mr_p",
                "gwas_unique_snps", "n_modulators", "pLI", "LOEUF", "clinvar_records"]
        st.dataframe(
            view[SHOW], use_container_width=True, hide_index=True, height=260,
            column_config={
                "top_mr_p": st.column_config.NumberColumn(format="%.1e"),
                "pLI": st.column_config.NumberColumn(format="%.2e"),
                "LOEUF": st.column_config.NumberColumn(format="%.2f"),
            })

        if len(view):
            sel = st.selectbox("Open a dossier", view["protein"].tolist())
            md_path = HERE / "dossiers" / f"{sel}_dossier.md"
            if md_path.exists():
                st.markdown("---")
                st.markdown(md_path.read_text(encoding="utf-8"))
                st.caption(f"Same page online: "
                           f"https://ds4cabs.github.io/CausalSentinel/dossiers/{sel}_dossier")
            else:
                st.warning(f"{md_path.name} not found.")
