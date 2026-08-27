"""ToolLedger — capture every tool call the model makes, so the card can be built from
the tool output itself rather than from the model's memory of it.

WHY THIS EXISTS
---------------
Gemini's automatic function calling executes tools inside the SDK, so by default the
caller never sees what came back — the card is whatever the model *remembers*. That is
exactly how a tool-declared caveat ("count truncated", "this is a lower bound") gets
silently dropped and a truncated internal number becomes a flat factual claim.

The ledger wraps each tool in a recorder that keeps the arguments and the verbatim return
value. Everything downstream — the evidence table, the caveat block, the source list, the
validator — is built from that record, not from prose. The model is left with one job:
writing the connective reasoning, which the validator then checks against this ledger.
"""
import functools
import time


class ToolLedger:
    """Wraps tool callables and records every invocation."""

    def __init__(self, tools):
        self.entries = []          # [{tool, args, kwargs, result, seconds, error}]
        self._tools = list(tools)

    def wrapped(self):
        """Return wrapped copies to hand to the model.

        The wrapper preserves __name__, __doc__ and __annotations__ because the SDK reads
        all three to build the function declaration the model sees.
        """
        out = []
        for fn in self._tools:
            out.append(self._wrap(fn))
        return out

    def _wrap(self, fn):
        @functools.wraps(fn)
        def recorder(*args, **kwargs):
            t0 = time.perf_counter()
            try:
                result = fn(*args, **kwargs)
                err = None
            except Exception as e:                     # a tool crash must not kill the run
                result = {"error": f"{type(e).__name__}: {e}"}
                err = repr(e)
            self.entries.append({
                "tool": fn.__name__,
                "args": list(args),
                "kwargs": dict(kwargs),
                "result": result,
                "seconds": round(time.perf_counter() - t0, 3),
                "exception": err,
            })
            return result
        return recorder

    # ---- read side -------------------------------------------------------
    def results_by_tool(self) -> dict:
        """Latest result per tool name — a success is never displaced by a later failure.

        Plain last-call-wins let a failed retry erase an earlier good result from the
        card, the validator haystack and the concordance input. Now the latest
        SUCCESSFUL call wins; an errored result stands only if the tool never succeeded.
        """
        latest, latest_ok = {}, {}
        for e in self.entries:
            errored = bool(e.get("exception")) or (
                isinstance(e.get("result"), dict) and e["result"].get("error"))
            latest[e["tool"]] = e["result"]
            if not errored:
                latest_ok[e["tool"]] = e["result"]
        return {t: latest_ok.get(t, r) for t, r in latest.items()}

    def called(self) -> list:
        return [e["tool"] for e in self.entries]

    def notes(self) -> list:
        """Every caveat any tool declared, with its tool name. These MUST reach the card."""
        found = []
        for e in self.entries:
            r = e["result"]
            if isinstance(r, dict) and r.get("note"):
                found.append((e["tool"], r["note"]))
        return found

    def sources(self) -> list:
        """(tool, url, source_release) for every tool that returned a human-facing URL."""
        out, seen = [], set()
        for e in self.entries:
            r = e["result"]
            if isinstance(r, dict) and r.get("url") and r["url"] not in seen:
                seen.add(r["url"])
                out.append((e["tool"], r["url"], r.get("source_release")))
        return out
