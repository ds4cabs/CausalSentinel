# -*- coding: utf-8 -*-
"""Score the agent's verdicts against Minikel-2024 historical outcomes.

Run AFTER `python agent.py --batch benchmark/minikel20_pairs.txt
--exclude-tool get_clinical_evidence --allow-unvalidated --out-dir benchmark/cards_genetic_only`.

What a "score" means here, stated before the numbers so they cannot be oversold:

- The labels are history's verdicts: Launched = SUCCESS, died at phase II/III with no
  active programme = FAILURE.
- The agent judged from genetic-and-annotation evidence only; get_clinical_evidence was
  withheld because it would hand the model the answer (a launched drug is visible as an
  APPROVAL stage).
- Perfect accuracy is NOT the expectation and would itself be suspicious: most launched
  drugs have no genetic support for their indication (Nelson 2015 / Minikel 2024 — the
  whole point of that literature is that genetic support merely ~2.6x's the odds). The
  informative readout is the PATTERN: does a genetics-first GO enrich for success, and
  does the model resist inventing support where the retrieval has none?
- Residual leakage is audited, not assumed away: Open Targets' overall association score
  includes a known_drug datatype, which encodes clinical knowledge. It is reported per
  pair below.
"""
import csv
import glob
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
CARDS = os.path.join(HERE, "cards_genetic_only")


def verdict_word(v):
    v = (v or "").upper()
    if "NO-GO" in v or "NO GO" in v:
        return "NO-GO"
    if "INSUFFICIENT" in v:
        return "INSUFFICIENT"
    if re.search(r"\bGO\b", v):
        return "GO"
    return "?"


labels = {}
with open(os.path.join(HERE, "minikel20_labels.tsv"), encoding="utf-8") as f:
    for r in csv.DictReader(f, delimiter="\t"):
        labels[(r["gene"], r["disease"])] = r

cards = {}
for fp in glob.glob(os.path.join(CARDS, "*_evidence_card.json")):
    j = json.load(open(fp, encoding="utf-8"))
    cards[(j["protein"], j["disease"])] = j

rows, missing = [], []
for key, lab in labels.items():
    j = cards.get(key)
    if not j:
        missing.append(key)
        continue
    led = {e.get("tool"): e.get("result") for e in (j.get("tool_ledger") or [])}
    ot = led.get("get_target_disease_evidence") or {}
    # This OT release names the drug-derived datatype "clinical" (older docs say
    # known_drug); match either so the leakage audit cannot silently go blank.
    known_drug = None
    for k, v in (ot.get("datatype_scores") or {}).items():
        if "drug" in k.lower() or k.lower() == "clinical":
            known_drug = v
    rows.append({
        "gene": key[0], "disease": key[1][:34],
        "label": lab["label"], "phase": lab["historical_max_phase"],
        "genetic_status": lab["genetic_status"] or "(none)",
        "verdict": verdict_word(j.get("model_verdict")),
        "valid_ok": (j.get("validation") or {}).get("ok"),
        "known_drug_score": known_drug,
    })

print(f"{'gene':<9} {'label':<8} {'verdict':<13} {'valid':<6} {'knowndrug':<10} "
      f"{'genetic status':<20} disease")
for r in sorted(rows, key=lambda x: (x["label"], x["verdict"])):
    kd = f"{r['known_drug_score']:.2f}" if isinstance(r["known_drug_score"], (int, float)) else "-"
    print(f"{r['gene']:<9} {r['label']:<8} {r['verdict']:<13} {str(r['valid_ok']):<6} "
          f"{kd:<10} {r['genetic_status']:<20} {r['disease']}")

def n(label, verdicts):
    return sum(1 for r in rows if r["label"] == label and r["verdict"] in verdicts)

print("\n--- confusion ---")
print(f"                GO    NO-GO  INSUFF")
print(f"SUCCESS (10)    {n('SUCCESS', {'GO'}):>2}    {n('SUCCESS', {'NO-GO'}):>4}   {n('SUCCESS', {'INSUFFICIENT'}):>4}")
print(f"FAILURE (10)    {n('FAILURE', {'GO'}):>2}    {n('FAILURE', {'NO-GO'}):>4}   {n('FAILURE', {'INSUFFICIENT'}):>4}")

go_s, go_f = n("SUCCESS", {"GO"}), n("FAILURE", {"GO"})
if go_s + go_f:
    print(f"\nprecision of GO against history: {go_s}/{go_s + go_f}")
nogoish_f = n("FAILURE", {"NO-GO", "INSUFFICIENT"})
print(f"failures NOT endorsed (NO-GO or INSUFFICIENT): {nogoish_f}/10")
if missing:
    print(f"\nMISSING cards for: {missing}")
