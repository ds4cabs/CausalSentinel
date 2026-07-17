"""Tool: get_chembl_modulators — known drugs/compounds for a target from ChEMBL (REST)."""
import requests

CHEMBL = "https://www.ebi.ac.uk/chembl/api/data"


def get_chembl_modulators(gene_symbol: str) -> dict:
    """Find known drugs / compounds that modulate a target, via ChEMBL.

    Use this to check whether a target is already druggable and what its known
    modulators are. Input should be a gene symbol such as PCSK9 or PNPLA3.
    Returns the ChEMBL target id and a list of mechanisms (drug id, action type,
    mechanism of action).
    """
    try:
        ts = requests.get(
            f"{CHEMBL}/target/search",
            params={"q": gene_symbol, "format": "json"},
            timeout=30,
        )
    except requests.RequestException as e:
        return {"error": f"ChEMBL request failed: {e}"}
    if ts.status_code != 200:
        return {"error": f"ChEMBL HTTP {ts.status_code}"}

    targets = ts.json().get("targets", [])
    if not targets:
        return {"found": False, "note": f"No ChEMBL target for '{gene_symbol}'."}
    # Prefer the human target.
    target = next((t for t in targets if t.get("organism") == "Homo sapiens"), targets[0])
    tid = target.get("target_chembl_id")

    mechanisms = []
    try:
        ms = requests.get(
            f"{CHEMBL}/mechanism",
            params={"target_chembl_id": tid, "format": "json", "limit": 20},
            timeout=30,
        )
        if ms.status_code == 200:
            mechanisms = ms.json().get("mechanisms", [])
    except requests.RequestException:
        mechanisms = []

    modulators = [
        {
            "drug": m.get("molecule_chembl_id"),
            "action": m.get("action_type"),
            "moa": m.get("mechanism_of_action"),
        }
        for m in mechanisms
    ]
    return {
        "found": True,
        "target_chembl_id": tid,
        "target_name": target.get("pref_name"),
        "n_modulators": len(modulators),
        "modulators": modulators[:10],
        "url": f"https://www.ebi.ac.uk/chembl/target_report_card/{tid}/",
    }


if __name__ == "__main__":
    import json
    print(json.dumps(get_chembl_modulators("PCSK9"), indent=2))
