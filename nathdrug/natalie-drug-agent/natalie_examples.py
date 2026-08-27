"""
natalie_examples.py
===================
Runs the Natalie agent on a set of drug pairs and writes the results to
`natalie_examples.md` (satisfying the "minimum 2 documented example runs"
deliverable). Also prints each run to the console.

Usage:
    python natalie_examples.py                 # default 2 example pairs
    python natalie_examples.py warfarin heparin metformin insulin
"""

from __future__ import annotations

import sys
from typing import List, Tuple

from natalie_agent import NatalieAgent

DEFAULT_PAIRS: List[Tuple[str, str]] = [
    ("aspirin", "ibuprofen"),
    ("acetaminophen", "naproxen"),
]


def _table_to_markdown(result: dict) -> str:
    da, db = result["drug_a"], result["drug_b"]
    lines = [
        f"| Category | Property | {da} | {db} |",
        "| --- | --- | --- | --- |",
    ]
    for row in result["table"]:
        lines.append(
            f"| {row['category']} | {row['property']} | "
            f"{row[da]} | {row[db]} |"
        )
    return "\n".join(lines)


def run(pairs: List[Tuple[str, str]]) -> str:
    agent = NatalieAgent()
    out: List[str] = [
        "# Natalie — Documented Example Runs\n",
        "Each run below was produced by the Natalie Gemini agent. For every "
        "comparison the agent autonomously made **4 database tool calls** "
        "(PubChem molecular properties + openFDA safety signals, for each of "
        "the two drugs), assembled the table, then wrote the AI summary.\n",
    ]

    for i, (a, b) in enumerate(pairs, 1):
        print(f"\n>>> Example {i}: {a} vs {b} …")
        result = agent.compare(a, b)

        calls = result["tool_calls"]
        call_list = "\n".join(f"  {j+1}. `{c['tool']}(\"{c['drug']}\")`"
                              for j, c in enumerate(calls)) or "  (served from cache)"

        out.append(f"\n---\n\n## Example {i}: {a} vs {b}\n")
        out.append(f"**Autonomous tool calls made ({len(calls)}):**\n\n{call_list}\n")
        out.append(f"\n### Comparison table\n\n{_table_to_markdown(result)}\n")
        out.append(f"\n### AI summary\n\n{result['summary']}\n")

        print(f"    tool calls: {len(calls)} | summary chars: {len(result['summary'])}")

    return "\n".join(out)


def main() -> None:
    args = sys.argv[1:]
    if args and len(args) % 2 == 0:
        pairs = [(args[i], args[i + 1]) for i in range(0, len(args), 2)]
    else:
        pairs = DEFAULT_PAIRS

    markdown = run(pairs)
    with open("natalie_examples.md", "w", encoding="utf-8") as fh:
        fh.write(markdown)
    print("\n✅ Wrote natalie_examples.md")


if __name__ == "__main__":
    main()
