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
# without a model we simply call the SELECTED sources (all nine by default).
# label -> (function, argument kind); order = the order they run and render.
PLAN_LABELS = {
    "🧬 MR estimate (EpiGraphDB)": (get_mr_result, "protein_disease"),
    "🏥 Clinical record (Open Targets)": (get_clinical_evidence, "protein_disease"),
    "🎯 Target-disease association (Open Targets)": (get_target_disease_evidence, "protein_disease"),
    "🧾 Protein context (UniProt)": (get_uniprot_dossier, "protein"),
    "💊 Druggability (ChEMBL)": (get_chembl_modulators, "protein"),
    "🩺 Clinical variants (ClinVar)": (get_clinvar_variants, "protein"),
    "🛡️ Constraint / knock-out tolerance (gnomAD)": (get_gnomad_constraint, "protein"),
    "📈 GWAS signal (GWAS Catalog)": (get_gwas_catalog, "protein"),
    "⚗️ Pharmacogenomics (ClinPGx)": (get_pharmgkb_drug_gene, "protein"),
}
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


@st.cache_data(show_spinner=False)
def _figures(protein: str):
    """The two per-protein figures (forest of retrieved MR estimates; gnomAD
    constraint), drawn by plots.py from live tool output."""
    import tempfile
    from plots import mr_forest, constraint_plot
    out = Path(tempfile.mkdtemp(prefix="opencausal_figs_"))
    f1 = f2 = None
    try:
        f1 = mr_forest(protein, out)
    except Exception:
        pass
    try:
        f2 = constraint_plot(protein, out)
    except Exception:
        pass
    return (str(f1) if f1 else None, str(f2) if f2 else None)


def _code_reading(results: dict) -> str:
    """A reading of the evidence composed by CODE from the tool results.

    This is what sits at the top of a no-model card: every clause below is a
    fixed template filled with a retrieved value — no model, no free text.
    """
    parts = []

    mr = results.get("get_mr_result") or {}
    ests = mr.get("matched_disease_estimates") or []
    if ests:
        m = ests[0]
        conc = results.get("classify_evidence_concordance") or {}
        depth = conc.get("best_validation_depth")
        sent = (f"EpiGraphDB holds a published MR estimate for this pair "
                f"(beta {m.get('beta')}, p {m.get('p_value')}, "
                f"{m.get('n_snp')} instrument(s), {m.get('cis_or_trans')})")
        if depth is not None:
            sent += f"; sensitivity checks reported: {depth} of 3"
        parts.append(sent + ".")
    elif mr.get("found"):
        parts.append(f"The protein has {mr.get('n_outcomes_available')} outcomes in the "
                     "MR resource, but none matches this disease.")
    else:
        parts.append("No published MR estimate exists for this pair in the resource — "
                     "absence of an estimate is not evidence of no effect.")

    clin = results.get("get_clinical_evidence") or {}
    if clin.get("drugs_for_this_disease"):
        parts.append(f"The clinic has already tried this target for this disease "
                     f"(max stage: {clin.get('max_stage_this_disease')}) — a stage means "
                     "a trial exists, not that it worked.")
    elif clin.get("n_drug_programmes"):
        parts.append(f"No programme for this disease is on record; "
                     f"{clin.get('n_drug_programmes')} drug programme(s) exist against "
                     "this target for other diseases.")
    elif clin:
        parts.append("No drug or clinical candidate against this target is on record.")

    gn = results.get("get_gnomad_constraint") or {}
    pli, loeuf = gn.get("pLI"), gn.get("LOEUF")
    if pli is not None or loeuf is not None:
        if (pli is not None and pli > 0.9) or (loeuf is not None and loeuf < 0.35):
            parts.append("gnomAD marks the gene LoF-intolerant — a safety flag.")
        else:
            parts.append("gnomAD marks the gene LoF-tolerant — a hint about safety, "
                         "not a licence to inhibit.")

    gw = results.get("get_gwas_catalog") or {}
    if gw.get("n_unique_snps") is not None:
        parts.append(f"The GWAS Catalog maps {gw.get('n_unique_snps')} unique SNPs "
                     "to the locus.")

    ch = results.get("get_chembl_modulators") or {}
    if ch.get("n_modulators"):
        parts.append(f"ChEMBL lists {ch.get('n_modulators')} known modulator(s).")
    elif ch and ch.get("found") is not False:
        parts.append("ChEMBL lists no known modulators — druggability is unproven.")

    parts.append("Every value above appears in a panel below, with the database "
                 "release it came from.")
    return " ".join(parts)


def _run_tools(protein: str, disease: str, progress=None, plan=None) -> ToolLedger:
    """Call the nine public sources through the ledger, then classify concordance."""
    ledger = ToolLedger(TOOLS)
    plan = PLAN if plan is None else plan
    for i, (fn, kind) in enumerate(plan):
        if progress is not None:
            progress.progress((i + 1) / (len(plan) + 1), text=f"querying {fn.__name__} …")
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
    st.header("Databases")
    st.caption("Query only these \u2014 all free, all keyless. Un-tick what you don't "
               "need and the run gets faster; skipped sources say so on the card.")

    def _set_all_dbs(value: bool) -> None:
        for k in PLAN_LABELS:
            st.session_state[f"db_{k}"] = value

    ca, cb = st.columns(2)
    ca.button("All", use_container_width=True, on_click=_set_all_dbs, args=(True,))
    cb.button("None", use_container_width=True, on_click=_set_all_dbs, args=(False,))
    sel_labels = [k for k in PLAN_LABELS
                  if st.checkbox(k, value=True, key=f"db_{k}")]
    st.markdown(
        "Also online: [protein gallery](https://ds4cabs.github.io/CausalSentinel/dossiers/) \u00b7 "
        "[card viewer](https://ds4cabs.github.io/CausalSentinel/viewer/)"
    )

import datetime as _dt
from streamlit.components.v1 import html as _components_html

_VIEWER = HERE / "viewer" / "index.html"
_BUNDLE = HERE / "viewer" / "cards_data.js"


def _viewer_embed(single: dict | None = None, height: int = 1500) -> None:
    """Render cards through viewer/index.html — the panel-per-tool interface.

    With single=None the full viewer is embedded: the ten worked pairs plus the
    genetics-to-clinic timelines. With a card dict, the same engine renders JUST
    that card — PAIRS is rewritten to one pair, the chrome is hidden, and the
    data bundle is that one card — so a freshly built card looks exactly like
    the published ones.
    """
    page = _VIEWER.read_text(encoding="utf-8")
    if single is None:
        bundle = _BUNDLE.read_text(encoding="utf-8")
    else:
        p, d = single["protein"], single["disease"]
        fname = f"{p}_{re.sub(r'[^A-Za-z0-9]+', '-', d).strip('-')}_evidence_card.json"
        bundle = ("window.CARD_DATA = "
                  + json.dumps({fname: single}, ensure_ascii=False, default=str) + ";")
    page = page.replace('<script src="cards_data.js"></script>',
                        "<script>" + bundle + "</script>", 1)
    if single is not None:
        p, d = single["protein"], single["disease"]
        page = re.sub(r"const PAIRS = \[.*?\];",
                      "const PAIRS = [[" + json.dumps(p) + ", " + json.dumps(d) + "]];",
                      page, count=1, flags=re.S)
        extra = (
            "<style>.tabs, .picker, header, footer {display:none !important}"
            ".tlhead {margin:1.4rem 0 .2rem}</style>"
            "<script>(function(){var n=0,t=setInterval(function(){"
            "var el=document.getElementById(\"card\");"
            "if(el&&el.childElementCount){clearInterval(t);"
            "var prot=PAIRS[0][0].toUpperCase();"
            "var hits=CASES.filter(function(c){return c.name.toUpperCase().indexOf(prot)===0});"
            "if(hits.length){el.insertAdjacentHTML(\"beforeend\","
            "\"<h2 class=tlhead>Genetics → clinic timeline — hand-verified</h2>\""
            "+hits.map(caseHTML).join(\"\"))}}"
            "else if(++n>60){clearInterval(t)}},200);})();</script>"
        )
        page = page.replace("</body>", extra + "</body>", 1)
    _components_html(page, height=height, scrolling=True)


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

        if not sel_labels:
            st.error("Pick at least one database in the sidebar.")
            st.stop()
        plan = [PLAN_LABELS[k] for k in PLAN_LABELS if k in sel_labels]
        bar = st.progress(0.0, text="starting \u2026")
        ledger = _run_tools(protein.strip(), disease.strip(), bar, plan=plan)
        bar.empty()

        verdict, reasoning = NO_MODEL_VERDICT, NO_MODEL_REASONING
        validation = None
        if not api_key.strip():
            reasoning = _code_reading(ledger.results_by_tool())
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
            "verdict": verdict,
            "reasoning": reasoning,
            "model": model.strip() if validation is not None else "none — no model was called",
            "generated_at": _dt.datetime.now().isoformat(timespec="seconds"),
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
        _viewer_embed(single={
            "protein": run["protein"],
            "disease": run["disease"],
            "generated_at": run.get("generated_at", ""),
            "model": run.get("model", ""),
            "model_verdict": run.get("verdict", ""),
            "model_reasoning": run.get("reasoning", ""),
            "validation": run["validation"] or {"ok": True, "checked": 0, "unsupported": []},
            "tool_ledger": run["entries"],
        }, height=1350)

        with st.expander("📈 Figures — drawn from tool output, nothing typed in", expanded=True):
            with st.spinner("drawing …"):
                fig_forest, fig_con = _figures(run["protein"])
            fc1, fc2 = st.columns(2)
            if fig_forest:
                fc1.image(fig_forest, use_container_width=True)
            else:
                fc1.caption("no retrieved MR estimates — nothing to plot")
            if fig_con:
                fc2.image(fig_con, use_container_width=True)
            else:
                fc2.caption("no gnomAD constraint data")

        stem = f"{run['protein']}_{re.sub(r'[^A-Za-z0-9]+', '-', run['disease']).strip('-')}"
        st.download_button("\u2b07\ufe0f Download this card (Markdown)",
                           data=run["card_md"].encode("utf-8"),
                           file_name=f"{stem}_evidence_card.md", mime="text/markdown")
    else:
        st.info("Pick an example above or type your own pair, then press "
                "**Build the evidence card**.")

# ============================ tab 2: ten worked cards =============================
with tab_viewer:
    st.caption("The card viewer \u2014 one panel per tool, every value read from each "
               "card's own ledger. Second tab inside: the genetics \u2192 clinic timelines.")
    _viewer_embed(None, height=1600)

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
