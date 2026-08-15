"""Enrich sweep caches with GWAS-trait tables and re-render every dossier.

Why this exists: the first full sweep ran while get_gwas_associations was being added, so
its caches predate the GWAS-trait step. This pass is idempotent and cheap - one GWAS
Catalog call per protein that lacks the data, then a full re-render of dossiers and the
master index with the current renderer. Safe to re-run anytime.

    python enrich_dossiers.py
"""
import json
import sys
import time
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from tools.gwas import get_gwas_associations
import proteome_sweep as ps

HERE = Path(__file__).resolve().parent
CACHE = HERE / "dossiers" / "_cache"
OUT = HERE / "dossiers"


def main() -> None:
    files = sorted(CACHE.glob("*.json"))
    print(f"[enrich] {len(files)} cached proteins")
    fetched = 0
    rows = {}
    t0 = time.time()
    for i, f in enumerate(files, 1):
        res = json.loads(f.read_text(encoding="utf-8"))
        sym = res["_meta"]["protein"]
        if "gwas_traits" not in res:
            try:
                res["gwas_traits"] = get_gwas_associations(sym)
            except Exception as e:                  # noqa: BLE001 - keep sweeping
                res["gwas_traits"] = {"error": f"{type(e).__name__}: {e}"}
            f.write_text(json.dumps(res, indent=1, ensure_ascii=False, default=str),
                         encoding="utf-8")
            fetched += 1
            time.sleep(0.3)
        (OUT / f"{sym}_dossier.md").write_text(ps.render_dossier(res), encoding="utf-8")
        rows[sym] = {k: ("" if v is None else v) for k, v in ps.index_row(res).items()}
        if i % 100 == 0:
            print(f"  [{i}/{len(files)}] fetched so far: {fetched}")

    import csv
    with open(OUT / "master_index.csv", "w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=ps.CSV_COLS)
        w.writeheader()
        for sym in sorted(rows):
            w.writerow({k: rows[sym].get(k, "") for k in ps.CSV_COLS})

    print(f"[enrich] done in {(time.time()-t0)/60:.1f} min - {fetched} proteins fetched, "
          f"{len(files)} dossiers re-rendered, index rebuilt with GWAS-trait columns")


if __name__ == "__main__":
    main()
