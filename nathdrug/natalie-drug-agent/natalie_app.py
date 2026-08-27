"""
natalie_app.py
==============
Streamlit web UI for the Natalie drug-comparison agent.

Run:
    export GEMINI_API_KEY=your_key_here
    streamlit run natalie_app.py
"""

from __future__ import annotations

import os

import pandas as pd
import streamlit as st

from natalie_agent import NatalieAgent, NatalieAgentError

st.set_page_config(page_title="Natalie · Drug Comparison Agent",
                   page_icon="💊", layout="wide")

# ---------------------------------------------------------------------------
# Header
# ---------------------------------------------------------------------------
st.title("💊 Natalie — Gemini Drug Comparison Agent")
st.caption(
    "Enter two drugs. Natalie autonomously calls **PubChem** (molecular "
    "properties) and **openFDA** (safety signals) for each drug — 4 tool "
    "calls — then builds a side-by-side table and an AI pattern summary."
)

# ---------------------------------------------------------------------------
# Sidebar: config
# ---------------------------------------------------------------------------
with st.sidebar:
    st.header("Configuration")
    env_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if env_key:
        st.success("Gemini API key detected from environment.")
        api_key = env_key
    else:
        api_key = st.text_input(
            "Gemini API key", type="password",
            help="Get a free key at https://aistudio.google.com/apikey",
        )
    model = st.text_input(
        "Model", value=os.environ.get("NATALIE_GEMINI_MODEL", "gemini-flash-latest")
    )
    st.markdown(
        "**Data sources**\n\n"
        "- 🧪 PubChem — molecular properties\n"
        "- ⚠️ openFDA — safety signals\n\n"
        "Both are free and need no key."
    )

# ---------------------------------------------------------------------------
# Inputs
# ---------------------------------------------------------------------------
col1, col2 = st.columns(2)
with col1:
    drug_a = st.text_input("Drug A", value="aspirin")
with col2:
    drug_b = st.text_input("Drug B", value="ibuprofen")

run = st.button("🔬 Compare drugs", type="primary", use_container_width=True)

# ---------------------------------------------------------------------------
# Run the agent
# ---------------------------------------------------------------------------
if run:
    if not api_key:
        st.error("Please provide a Gemini API key (sidebar) to run the agent.")
        st.stop()
    if not drug_a.strip() or not drug_b.strip():
        st.error("Please enter both drug names.")
        st.stop()

    try:
        agent = NatalieAgent(api_key=api_key, model=model)
    except NatalieAgentError as exc:
        st.error(str(exc))
        st.stop()

    with st.spinner(f"Natalie is researching {drug_a} vs {drug_b}…"):
        try:
            result = agent.compare(drug_a, drug_b)
        except Exception as exc:  # noqa: BLE001
            st.error(f"Agent run failed: {exc}")
            st.stop()

    da, db = result["drug_a"], result["drug_b"]

    # --- autonomous tool-call trace -------------------------------------
    st.subheader("🤖 Autonomous tool calls")
    tc = result["tool_calls"]
    st.write(
        f"Natalie made **{len(tc)}** autonomous database tool calls "
        "(PubChem + openFDA for each drug):"
    )
    st.dataframe(
        pd.DataFrame(tc) if tc else pd.DataFrame(
            [{"note": "results served from backfill cache"}]
        ),
        use_container_width=True, hide_index=True,
    )

    # --- comparison table ------------------------------------------------
    st.subheader(f"📊 {da} vs {db} — side-by-side comparison")
    df = pd.DataFrame(result["table"])[["category", "property", da, db]]
    df = df.rename(columns={"category": "Category", "property": "Property"})
    st.dataframe(df, use_container_width=True, hide_index=True)

    # --- AI summary ------------------------------------------------------
    st.subheader("🧠 AI summary — property / safety patterns")
    st.info(result["summary"])

    # --- raw data (optional) --------------------------------------------
    with st.expander("🔎 Raw tool data (JSON)"):
        st.json(result["raw"])

    # --- download --------------------------------------------------------
    st.download_button(
        "⬇️ Download comparison table (CSV)",
        data=df.to_csv(index=False).encode("utf-8"),
        file_name=f"natalie_{da}_vs_{db}.csv",
        mime="text/csv",
    )
else:
    st.info("Enter two drug names above and click **Compare drugs** to begin.")
