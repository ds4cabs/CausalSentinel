"""
natalie_agent.py
================
The Natalie drug-comparison agent, powered by Google Gemini.

Given two drug names, the agent AUTONOMOUSLY decides to call two database tools
for each drug (via Gemini function calling):

    natalie_get_molecular_properties(drug)  -> PubChem
    natalie_get_safety_signals(drug)        -> openFDA

That is 2 tools x 2 drugs = 4 autonomous tool calls per comparison. The agent
then:
    * assembles the captured tool results into a structured side-by-side table,
    * asks Gemini for a 3-5 sentence summary of property/safety patterns.

Usage (CLI):
    export GEMINI_API_KEY=your_key_here
    python natalie_agent.py aspirin ibuprofen

Programmatic:
    from natalie_agent import NatalieAgent
    result = NatalieAgent().compare("aspirin", "ibuprofen")
    print(result["summary"])
"""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List

from google import genai
from google.genai import types

from natalie_tools import (
    NATALIE_TOOL_FUNCTIONS,
    natalie_get_molecular_properties,
    natalie_get_safety_signals,
)

NATALIE_DEFAULT_MODEL = os.environ.get("NATALIE_GEMINI_MODEL", "gemini-flash-latest")


# ---------------------------------------------------------------------------
# Gemini function (tool) declarations
# ---------------------------------------------------------------------------

_MOLECULAR_DECL = types.FunctionDeclaration(
    name="natalie_get_molecular_properties",
    description=(
        "Fetch molecular properties for ONE drug from the PubChem database: "
        "molecular formula, molecular weight, LogP, hydrogen-bond donors and "
        "acceptors, polar surface area (TPSA), and rotatable bonds."
    ),
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "drug_name": types.Schema(
                type=types.Type.STRING,
                description="A single drug's common/generic name, e.g. 'aspirin'.",
            )
        },
        required=["drug_name"],
    ),
)

_SAFETY_DECL = types.FunctionDeclaration(
    name="natalie_get_safety_signals",
    description=(
        "Fetch safety signals for ONE drug from the openFDA database: the top "
        "reported adverse reactions with counts, whether a boxed (black-box) "
        "warning exists, and a short warnings excerpt."
    ),
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "drug_name": types.Schema(
                type=types.Type.STRING,
                description="A single drug's common/generic name, e.g. 'ibuprofen'.",
            )
        },
        required=["drug_name"],
    ),
)

_NATALIE_TOOLS = types.Tool(
    function_declarations=[_MOLECULAR_DECL, _SAFETY_DECL]
)


class NatalieAgentError(RuntimeError):
    """Raised for configuration problems (e.g. missing API key)."""


class NatalieAgent:
    """Gemini-powered agent that compares two drugs end to end."""

    def __init__(self, api_key: str | None = None, model: str | None = None):
        key = api_key or os.environ.get("GEMINI_API_KEY") or os.environ.get(
            "GOOGLE_API_KEY"
        )
        if not key:
            raise NatalieAgentError(
                "No Gemini API key found. Set GEMINI_API_KEY (see .env.example)."
            )
        self.client = genai.Client(api_key=key)
        self.model = model or NATALIE_DEFAULT_MODEL

    # -- internal: run one function-calling loop and capture every result ---
    def _run_tool_loop(self, drug_a: str, drug_b: str) -> Dict[str, Any]:
        """Let Gemini autonomously call the 2 tools for each drug.

        Returns a dict:
            {"captured": {func_name: {drug: result}}, "log": [ ... ]}
        """
        instruction = (
            "You are Natalie, a pharmacology data agent. The user wants to "
            f'compare two drugs: "{drug_a}" and "{drug_b}".\n\n'
            "You MUST gather real data before answering. For EACH of the two "
            "drugs, call BOTH tools exactly once:\n"
            "  1. natalie_get_molecular_properties(drug_name)\n"
            "  2. natalie_get_safety_signals(drug_name)\n"
            "That is four tool calls total. Do not fabricate any values. "
            "After all four calls return, reply with the single word DONE."
        )

        contents: List[types.Content] = [
            types.Content(role="user", parts=[types.Part(text=instruction)])
        ]
        config = types.GenerateContentConfig(
            tools=[_NATALIE_TOOLS],
            # We handle function execution ourselves so we can capture results.
            automatic_function_calling=types.AutomaticFunctionCallingConfig(
                disable=True
            ),
            temperature=0,
        )

        captured: Dict[str, Dict[str, Any]] = {
            "natalie_get_molecular_properties": {},
            "natalie_get_safety_signals": {},
        }
        log: List[Dict[str, Any]] = []

        # Safety bound on loop iterations.
        for _ in range(8):
            response = self.client.models.generate_content(
                model=self.model, contents=contents, config=config
            )
            calls = response.function_calls or []
            if not calls:
                break  # model produced text (e.g. "DONE") -> we're finished

            # Record the model's turn, then answer every requested call.
            contents.append(response.candidates[0].content)
            tool_response_parts: List[types.Part] = []
            for call in calls:
                fn = NATALIE_TOOL_FUNCTIONS.get(call.name)
                args = dict(call.args or {})
                drug = args.get("drug_name", "?")
                if fn is None:
                    result = {"error": f"unknown tool {call.name}"}
                else:
                    result = fn(**args)

                captured.setdefault(call.name, {})[drug] = result
                log.append({"tool": call.name, "drug": drug})
                tool_response_parts.append(
                    types.Part.from_function_response(
                        name=call.name, response={"result": result}
                    )
                )
            contents.append(types.Content(role="user", parts=tool_response_parts))

        return {"captured": captured, "log": log}

    # -- internal: ensure we have all 4 data pulls even if the model skips ---
    def _backfill(self, captured: Dict[str, Any], drug_a: str, drug_b: str) -> None:
        for drug in (drug_a, drug_b):
            mol = captured["natalie_get_molecular_properties"]
            saf = captured["natalie_get_safety_signals"]
            if drug not in mol:
                mol[drug] = natalie_get_molecular_properties(drug)
                mol[drug]["_backfilled"] = True
            if drug not in saf:
                saf[drug] = natalie_get_safety_signals(drug)
                saf[drug]["_backfilled"] = True

    # -- internal: build the structured side-by-side comparison table -------
    @staticmethod
    def _build_table(captured: Dict[str, Any], drug_a: str, drug_b: str
                     ) -> List[Dict[str, str]]:
        mol = captured["natalie_get_molecular_properties"]
        saf = captured["natalie_get_safety_signals"]

        def fmt_prop(data: Dict[str, Any], key: str) -> str:
            if data.get("error"):
                return "—"
            for p in data.get("properties", []):
                if p["key"] == key:
                    val = p["value"]
                    unit = f" {p['unit']}" if p["unit"] else ""
                    return f"{val}{unit}" if val not in ("N/A", None) else "—"
            return "—"

        def fmt_reactions(data: Dict[str, Any]) -> str:
            if data.get("error") or not data.get("top_adverse_reactions"):
                return "—"
            return "; ".join(
                f"{r['reaction']} ({r['count']:,})"
                for r in data["top_adverse_reactions"]
            )

        def fmt_boxed(data: Dict[str, Any]) -> str:
            bw = data.get("boxed_warning")
            if bw is None:
                return "—"
            return "Yes ⚠️" if bw else "No"

        rows: List[Dict[str, str]] = []
        table_spec = [
            ("Category", "PubChem CID",
             lambda d: str(mol[d].get("cid", "—")) if not mol[d].get("error") else "—"),
            ("Molecular", "Molecular formula",
             lambda d: fmt_prop(mol[d], "MolecularFormula")),
            ("Molecular", "Molecular weight",
             lambda d: fmt_prop(mol[d], "MolecularWeight")),
            ("Molecular", "LogP (lipophilicity)",
             lambda d: fmt_prop(mol[d], "XLogP")),
            ("Molecular", "H-bond donors",
             lambda d: fmt_prop(mol[d], "HBondDonorCount")),
            ("Molecular", "H-bond acceptors",
             lambda d: fmt_prop(mol[d], "HBondAcceptorCount")),
            ("Molecular", "Polar surface area (TPSA)",
             lambda d: fmt_prop(mol[d], "TPSA")),
            ("Molecular", "Rotatable bonds",
             lambda d: fmt_prop(mol[d], "RotatableBondCount")),
            ("Safety", "Boxed (black-box) warning",
             lambda d: fmt_boxed(saf[d])),
            ("Safety", "Total adverse-event reports",
             lambda d: f"{saf[d]['total_reports']:,}"
             if saf[d].get("total_reports") not in (None,) else "—"),
            ("Safety", "Top reported adverse reactions",
             lambda d: fmt_reactions(saf[d])),
        ]

        for category, prop, getter in table_spec:
            rows.append({
                "category": category,
                "property": prop,
                drug_a: getter(drug_a),
                drug_b: getter(drug_b),
            })
        return rows

    # -- internal: ask Gemini for the 3-5 sentence pattern summary ----------
    def _summarize(self, table: List[Dict[str, str]], drug_a: str, drug_b: str
                   ) -> str:
        table_text = json.dumps(table, indent=2)
        prompt = (
            "You are Natalie, a pharmacology analyst. Below is a verified "
            f"side-by-side comparison table of {drug_a} vs {drug_b}, built from "
            "PubChem (molecular properties) and openFDA (safety signals).\n\n"
            f"{table_text}\n\n"
            "Write a concise summary of 3 to 5 sentences that identifies "
            "PATTERNS linking molecular properties to safety signals (for "
            "example, how lipophilicity/LogP, polar surface area, or molecular "
            "weight may relate to the observed adverse-reaction profile or "
            "warnings). Compare the two drugs directly. Use only the data "
            "shown; do not invent numbers. Do not add disclaimers or headings, "
            "just the summary paragraph."
        )
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
            config=types.GenerateContentConfig(temperature=0.3),
        )
        return (response.text or "").strip()

    # -- public API ---------------------------------------------------------
    def compare(self, drug_a: str, drug_b: str) -> Dict[str, Any]:
        """Run the full Natalie comparison for two drugs.

        Returns:
            {
              "drug_a", "drug_b",
              "table": [ {category, property, <drug_a>, <drug_b>}, ... ],
              "summary": str,
              "tool_calls": [ {tool, drug}, ... ],   # autonomous calls made
              "raw": { captured tool results },
            }
        """
        drug_a = drug_a.strip()
        drug_b = drug_b.strip()
        if not drug_a or not drug_b:
            raise ValueError("Two drug names are required.")

        loop = self._run_tool_loop(drug_a, drug_b)
        captured = loop["captured"]
        self._backfill(captured, drug_a, drug_b)
        table = self._build_table(captured, drug_a, drug_b)
        summary = self._summarize(table, drug_a, drug_b)

        return {
            "drug_a": drug_a,
            "drug_b": drug_b,
            "table": table,
            "summary": summary,
            "tool_calls": loop["log"],
            "raw": captured,
        }


def _cli() -> None:
    import sys

    if len(sys.argv) < 3:
        print("Usage: python natalie_agent.py <drug_a> <drug_b>")
        raise SystemExit(1)

    agent = NatalieAgent()
    result = agent.compare(sys.argv[1], sys.argv[2])

    print(f"\n=== Natalie: {result['drug_a']} vs {result['drug_b']} ===\n")
    print(f"Autonomous tool calls made: {len(result['tool_calls'])}")
    for c in result["tool_calls"]:
        print(f"  - {c['tool']}({c['drug']})")

    print("\n--- Comparison table ---")
    da, db = result["drug_a"], result["drug_b"]
    print(f"{'Property':<32} | {da:<28} | {db:<28}")
    print("-" * 94)
    for row in result["table"]:
        print(f"{row['property']:<32} | {str(row[da])[:28]:<28} | "
              f"{str(row[db])[:28]:<28}")

    print("\n--- AI summary ---")
    print(result["summary"])


if __name__ == "__main__":
    _cli()
