"""Enrichment pass: re-fetch the phenome map for every cached protein so each disease row
carries the gene_burden (ExWAS) score, then re-render dossiers and rebuild the index.

Why this exists: the first sweep's phenome rows had genetic_association only. The owner
pointed out — correctly — that Mendelian-disease genes can still anchor causal claims for
OTHER phenotypes via rare-variant (ExWAS) burden tests, so "no MR" rows split into three:
Mendelian disease itself (MR adds nothing), rare-variant anchor available (Genebass /
AZ PheWAS via Open Targets' gene_burden datasource), and true MR gaps.

Idempotent and resumable: proteins whose cached phenome rows already contain the
gene_burden_exwas key are skipped. Safe to re-run.
"""
import json
import sys
import time
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from tools.opentargets import get_gene_phenome
import proteome_sweep as ps

HERE = Path(__file__).resolve().parent
CACHE = HERE / "dossiers" / "_cache"
OUT = HERE / "dossiers"


def has_burden_key(res: dict) -> bool:
    # Skip-check keys on the NEWEST field so a cache written by an older enrichment run
    # (burden only, no causal_status) still gets refetched exactly once.
    rows = (res.get("phenome") or {}).get("top_diseases") or []
    return bool(rows) and "causal_status" in rows[0]


def main() -> None:
    files = sorted(CACHE.glob("*.json"))
    print(f"[enrich-phenome] {len(files)} cached proteins")
    t0, fetched = time.time(), 0
    rows = {}
    for i, f in enumerate(files, 1):
        res = json.loads(f.read_text(encoding="utf-8"))
        sym = res["_meta"]["protein"]
        if not has_burden_key(res):
            try:
                res["phenome"] = get_gene_phenome(sym)
                fetched += 1
            except Exception as e:                  # noqa: BLE001
                print(f"  {sym}: phenome refetch failed ({type(e).__name__})")
            f.write_text(json.dumps(res, indent=1, ensure_ascii=False, default=str),
                         encoding="utf-8")
            time.sleep(0.3)
        (OUT / f"{sym}_dossier.md").write_text(ps.render_dossier(res), encoding="utf-8")
        rows[sym] = {k: ("" if v is None else v) for k, v in ps.index_row(res).items()}
        if i % 100 == 0:
            print(f"  [{i}/{len(files)}] refetched so far: {fetched}", flush=True)

    import csv
    with open(OUT / "master_index.csv", "w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=ps.CSV_COLS)
        w.writeheader()
        for r in rows.values():
            w.writerow({k: r.get(k, "") for k in ps.CSV_COLS})

    n_anchor = sum(1 for r in rows.values() if r.get("n_burden_diseases"))
    print(f"[enrich-phenome] done in {(time.time()-t0)/60:.1f} min — {fetched} refetched, "
          f"{len(rows)} dossiers re-rendered; {n_anchor} proteins carry ExWAS burden anchors")


if __name__ == "__main__":
    main()
