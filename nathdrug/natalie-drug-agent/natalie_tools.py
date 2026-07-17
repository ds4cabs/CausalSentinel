"""
natalie_tools.py
================
Database tools for the Natalie drug-comparison agent.

Two independent, free, no-API-key data sources are exposed as tools. The Gemini
agent calls BOTH of these for EACH submitted drug (2 tools x 2 drugs = 4 calls):

    1. natalie_get_molecular_properties(drug_name) -> PubChem PUG REST
       Molecular properties: formula, weight, LogP, H-bond donors/acceptors,
       topological polar surface area (TPSA), rotatable bonds, SMILES.

    2. natalie_get_safety_signals(drug_name)      -> openFDA
       Safety signals: top reported adverse reactions (with counts), whether a
       boxed ("black box") warning exists, and a short warnings excerpt.

Every function returns a plain dict and never raises to the caller: on any
failure it returns {"drug": ..., "error": "<reason>", ...} so the agent and UI
can degrade gracefully.
"""

from __future__ import annotations

import time
from typing import Any, Dict, List

import requests

# ---------------------------------------------------------------------------
# Shared HTTP helpers
# ---------------------------------------------------------------------------

_PUBCHEM_BASE = "https://pubchem.ncbi.nlm.nih.gov/rest/pug"
_OPENFDA_BASE = "https://api.fda.gov/drug"
_TIMEOUT = 20
_HEADERS = {"User-Agent": "natalie-drug-agent/1.0 (research/education)"}


def _get_json(url: str, params: Dict[str, Any] | None = None) -> Dict[str, Any]:
    """GET a URL and return parsed JSON, with one retry on transient errors."""
    last_err = None
    for attempt in range(2):
        try:
            resp = requests.get(url, params=params, headers=_HEADERS, timeout=_TIMEOUT)
            if resp.status_code == 404:
                return {"_http_404": True}
            resp.raise_for_status()
            return resp.json()
        except Exception as exc:  # noqa: BLE001 - we intentionally soften all errors
            last_err = exc
            time.sleep(0.6 * (attempt + 1))
    raise RuntimeError(str(last_err))


# ---------------------------------------------------------------------------
# TOOL 1 -- Molecular properties (PubChem)
# ---------------------------------------------------------------------------

# Human-readable labels + units for each PubChem property we surface.
_MOLECULAR_FIELDS = [
    ("MolecularFormula", "Molecular formula", ""),
    ("MolecularWeight", "Molecular weight", "g/mol"),
    ("XLogP", "LogP (lipophilicity)", ""),
    ("HBondDonorCount", "H-bond donors", ""),
    ("HBondAcceptorCount", "H-bond acceptors", ""),
    ("TPSA", "Polar surface area (TPSA)", "Å²"),
    ("RotatableBondCount", "Rotatable bonds", ""),
]

_MOLECULAR_PROPS_QUERY = (
    "MolecularFormula,MolecularWeight,XLogP,HBondDonorCount,"
    "HBondAcceptorCount,TPSA,RotatableBondCount,SMILES,IUPACName"
)


def natalie_get_molecular_properties(drug_name: str) -> Dict[str, Any]:
    """Look up a drug's molecular properties from PubChem.

    Args:
        drug_name: Common or generic drug name, e.g. "aspirin".

    Returns:
        dict with keys: drug, source, cid, properties (list of
        {key,label,value,unit}), smiles, iupac_name. On failure includes
        an "error" key.
    """
    drug = (drug_name or "").strip()
    if not drug:
        return {"drug": drug_name, "source": "PubChem", "error": "empty drug name"}

    try:
        # Step 1: resolve name -> CID
        cid_json = _get_json(f"{_PUBCHEM_BASE}/compound/name/{drug}/cids/JSON")
        if cid_json.get("_http_404"):
            return {"drug": drug, "source": "PubChem",
                    "error": f'"{drug}" not found in PubChem'}
        cids = cid_json.get("IdentifierList", {}).get("CID", [])
        if not cids:
            return {"drug": drug, "source": "PubChem",
                    "error": f'no PubChem CID for "{drug}"'}
        cid = cids[0]

        # Step 2: fetch properties for that CID
        prop_json = _get_json(
            f"{_PUBCHEM_BASE}/compound/cid/{cid}/property/{_MOLECULAR_PROPS_QUERY}/JSON"
        )
        props_raw = (
            prop_json.get("PropertyTable", {}).get("Properties", [{}])[0]
        )

        properties: List[Dict[str, Any]] = []
        for key, label, unit in _MOLECULAR_FIELDS:
            val = props_raw.get(key, "N/A")
            properties.append({"key": key, "label": label, "value": val, "unit": unit})

        return {
            "drug": drug,
            "source": "PubChem",
            "cid": cid,
            "smiles": props_raw.get("SMILES", "N/A"),
            "iupac_name": props_raw.get("IUPACName", "N/A"),
            "properties": properties,
        }
    except Exception as exc:  # noqa: BLE001
        return {"drug": drug, "source": "PubChem", "error": f"lookup failed: {exc}"}


# ---------------------------------------------------------------------------
# TOOL 2 -- Safety signals (openFDA)
# ---------------------------------------------------------------------------

def natalie_get_safety_signals(drug_name: str, top_n: int = 5) -> Dict[str, Any]:
    """Look up a drug's safety signals from openFDA.

    Pulls the most-reported adverse reactions (FAERS event counts) and the
    boxed-warning / warnings text from the structured product label.

    Args:
        drug_name: Common or generic drug name, e.g. "ibuprofen".
        top_n: How many top adverse reactions to return.

    Returns:
        dict with keys: drug, source, top_adverse_reactions (list of
        {reaction,count}), boxed_warning (bool), warning_excerpt (str),
        total_reports (int). On failure includes an "error" key.
    """
    drug = (drug_name or "").strip()
    if not drug:
        return {"drug": drug_name, "source": "openFDA", "error": "empty drug name"}

    result: Dict[str, Any] = {
        "drug": drug,
        "source": "openFDA",
        "top_adverse_reactions": [],
        "boxed_warning": None,
        "warning_excerpt": "N/A",
        "total_reports": None,
    }

    # --- Part A: adverse-event reaction counts (FAERS) ---------------------
    try:
        events = _get_json(
            f"{_OPENFDA_BASE}/event.json",
            params={
                "search": f'patient.drug.medicinalproduct:"{drug}"',
                "count": "patient.reaction.reactionmeddrapt.exact",
            },
        )
        if not events.get("_http_404"):
            rows = events.get("results", [])
            reactions = [
                {"reaction": r["term"].title(), "count": r["count"]}
                for r in rows[:top_n]
            ]
            result["top_adverse_reactions"] = reactions
            result["total_reports"] = sum(r["count"] for r in rows) if rows else 0
    except Exception as exc:  # noqa: BLE001
        result["adverse_event_error"] = str(exc)

    # --- Part B: label warnings / boxed warning ---------------------------
    try:
        label = _get_json(
            f"{_OPENFDA_BASE}/label.json",
            params={
                "search": f'openfda.generic_name:"{drug}" '
                          f'openfda.brand_name:"{drug}"',
                "limit": 1,
            },
        )
        if not label.get("_http_404"):
            lab_rows = label.get("results", [])
            if lab_rows:
                rec = lab_rows[0]
                boxed = rec.get("boxed_warning")
                result["boxed_warning"] = bool(boxed)
                # Prefer boxed warning text, else general warnings.
                text_field = boxed or rec.get("warnings") or rec.get(
                    "warnings_and_cautions"
                )
                if text_field:
                    excerpt = " ".join(text_field)[:400].strip()
                    result["warning_excerpt"] = excerpt + (
                        "..." if len(" ".join(text_field)) > 400 else ""
                    )
    except Exception as exc:  # noqa: BLE001
        result["label_error"] = str(exc)

    # If we got nothing at all, mark an error.
    if not result["top_adverse_reactions"] and result["boxed_warning"] is None:
        result["error"] = f'no openFDA safety data for "{drug}"'

    return result


# ---------------------------------------------------------------------------
# Tool registry -- consumed by natalie_agent.py to build Gemini declarations
# ---------------------------------------------------------------------------

NATALIE_TOOL_FUNCTIONS = {
    "natalie_get_molecular_properties": natalie_get_molecular_properties,
    "natalie_get_safety_signals": natalie_get_safety_signals,
}


if __name__ == "__main__":
    # Quick manual smoke test: python natalie_tools.py aspirin
    import json
    import sys

    name = sys.argv[1] if len(sys.argv) > 1 else "aspirin"
    print(f"== molecular properties: {name} ==")
    print(json.dumps(natalie_get_molecular_properties(name), indent=2))
    print(f"\n== safety signals: {name} ==")
    print(json.dumps(natalie_get_safety_signals(name), indent=2))
