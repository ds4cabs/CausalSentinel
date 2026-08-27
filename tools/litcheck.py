"""Tool: get_published_mr — has an MR analysis of this protein-disease pair ever been PUBLISHED?

WHY THIS EXISTS
---------------
Every other tool answers "what does database X hold". This one answers a different and
harder question: **has a human ever published this analysis?** That distinction is the
whole point. A pair can be absent from a precomputed MR resource and still have a
dedicated paper behind it, and a pair can have been swept by a 2,000-protein screen and
still have nobody who ever looked at it.

So the verdict is deliberately THREE-VALUED, not two:

    dedicated      a paper whose exposure-outcome focus includes this pair
    swept          the pair falls inside a large screen, but no paper is about it
                   ("computed by someone; interpreted by no-one")
    no_record      nothing found — a candidate for analysis, NOT proof of absence

TWO SOURCES, BECAUSE NEITHER IS ENOUGH
--------------------------------------
1. **MR-KG** (Bristol MRC IEU) — 15,000+ MR papers with LLM-extracted exposure/outcome
   pairs. High precision, and it gives structured results. But its trait layer is
   free text taken from each paper and is NOT normalised: `trait=IL6R` returns 3 studies,
   `trait=interleukin-6 receptor` returns 0, and `trait=PNPLA3` returns 0 despite PNPLA3 MR
   papers existing. Used alone it would manufacture false "nobody has done this" claims.
2. **Europe PMC** — full literature search, no key required, high recall, no structure.

Neither is used as ground truth alone. Synonym expansion happens here, and where a model
is available it judges each candidate abstract; without one the tool degrades to string
matching and says so in the result.

We call MR-KG's public API. We do **not** vendor their code: MR-KG is GPL-3.0, and copying
it would relicense this project. Their extraction schema informed the shape of the
`results` we read back — an idea, not a copy.
"""
import json
import os
import re
import time

import requests

MRKG = "https://epigraphdb.org/mr-kg/api"
EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
MR_TERMS = '("Mendelian randomization" OR "Mendelian randomisation" OR "Mendelian randomization analysis")'
PAGE = 100                      # Europe PMC default is 25 — a silent truncation trap
MAX_PAGES = 5
MAX_ABSTRACTS_TO_JUDGE = 25
# A "nobody has published this" claim is only as good as the fraction of retrieved
# abstracts that were actually read. Judging 12 of 316 and declaring a gap is not a
# finding, it is a sampling artifact — so coverage is reported and gates the confidence.
MIN_COVERAGE_FOR_CONFIDENT_GAP = 0.6


# ----------------------------------------------------------------- synonyms
def _protein_synonyms(protein: str) -> list:
    """Gene symbol plus whatever UniProt calls it. Unnormalised trait text is the single
    largest source of false negatives here, so this list matters more than it looks."""
    out = [protein]
    try:
        from .uniprot import get_uniprot_dossier
        u = get_uniprot_dossier(protein)
        if u.get("found"):
            out += [g for g in (u.get("gene_names") or []) if g]
            name = u.get("protein_name")
            if name and name != "N/A":
                out.append(name)
                # "Interleukin-6 receptor subunit alpha" -> also try without the suffix
                short = re.sub(r"\s+(subunit|chain|precursor|isoform)\b.*$", "", name, flags=re.I)
                if short != name:
                    out.append(short)
    except Exception:
        pass
    seen, uniq = set(), []
    for s in out:
        k = s.lower().strip()
        if k and k not in seen:
            seen.add(k)
            uniq.append(s.strip())
    return uniq


def _disease_synonyms(disease: str) -> list:
    out = [disease]
    d = disease.lower()
    ALIAS = {
        "masld": ["non-alcoholic fatty liver disease", "NAFLD", "steatotic liver disease",
                  "hepatic steatosis"],
        "nafld": ["non-alcoholic fatty liver disease", "MASLD", "hepatic steatosis"],
        "coronary heart disease": ["coronary artery disease", "myocardial infarction", "CHD"],
        "coronary artery disease": ["coronary heart disease", "myocardial infarction", "CAD"],
        "high cholesterol": ["hypercholesterolemia", "LDL cholesterol", "hyperlipidemia"],
        "type 2 diabetes": ["T2D", "type 2 diabetes mellitus"],
        "alzheimer disease": ["Alzheimer's disease", "AD", "dementia"],
    }
    for k, v in ALIAS.items():
        if k in d:
            out += v
    seen, uniq = set(), []
    for s in out:
        if s.lower() not in seen:
            seen.add(s.lower())
            uniq.append(s)
    return uniq


# ----------------------------------------------------------------- MR-KG
def _mrkg_candidates(protein: str, syns: list) -> list:
    """Studies MR-KG associates with this protein, via both its structured trait index and
    its free-text search (the free-text route consistently finds ~10x more)."""
    seen, out = set(), []
    queries = [("trait", s) for s in syns[:4]] + [("q", protein)]
    for key, val in queries:
        try:
            r = requests.get(f"{MRKG}/studies", params={key: val, "limit": 25}, timeout=30)
            if r.status_code != 200:
                continue
            for s in r.json().get("studies", []):
                pmid = str(s.get("pmid"))
                if pmid and pmid not in seen:
                    seen.add(pmid)
                    out.append({**s, "_via": f"mrkg:{key}={val}"})
        except requests.RequestException:
            continue
        time.sleep(0.15)
    return out


def _mrkg_pairs(pmid: str) -> list:
    """The extracted exposure->outcome rows MR-KG holds for one paper."""
    try:
        r = requests.get(f"{MRKG}/studies/{pmid}/extraction", timeout=30)
        if r.status_code != 200:
            return []
        return r.json().get("results", []) or []
    except (requests.RequestException, ValueError):
        return []


# ----------------------------------------------------------------- Europe PMC
def _epmc_search(protein_syns: list, disease_syns: list) -> tuple:
    """Return (hits, total_reported). Paginated deliberately: Europe PMC defaults to 25
    results, and a silently truncated search is exactly how a 'nobody has done this'
    claim becomes false."""
    p = " OR ".join(f'"{s}"' for s in protein_syns[:5])
    d = " OR ".join(f'"{s}"' for s in disease_syns[:5])
    query = f"({p}) AND ({d}) AND {MR_TERMS}"
    hits, total, cursor, pages = [], None, "*", 0
    while pages < MAX_PAGES:
        try:
            r = requests.get(EPMC, params={"query": query, "format": "json",
                                           "pageSize": PAGE, "cursorMark": cursor,
                                           "resultType": "core"}, timeout=45)
            r.raise_for_status()
            d_ = r.json()
        except (requests.RequestException, ValueError):
            break
        res = d_.get("resultList", {}).get("result", [])
        if total is None:
            total = d_.get("hitCount")
        for x in res:
            hits.append({
                "pmid": x.get("pmid"), "doi": x.get("doi"), "title": x.get("title"),
                "journal": (x.get("journalInfo") or {}).get("journal", {}).get("title"),
                "year": x.get("pubYear"), "abstract": (x.get("abstractText") or "")[:2500],
                "is_open_access": x.get("isOpenAccess"),
                # Per-hit source attribution. An earlier version tagged only Semantic
                # Scholar hits and then stripped the tag before returning, so no caller
                # could ever say WHICH source produced a paper — which is exactly the
                # question a coverage classification asks.
                "_source": "europe_pmc",
            })
        nxt = d_.get("nextCursorMark")
        pages += 1
        if not nxt or nxt == cursor or not res:
            break
        cursor = nxt
        time.sleep(0.2)
    return hits, total, query


# ----------------------------------------------------------------- Semantic Scholar
S2 = "https://api.semanticscholar.org/graph/v1/paper/search"
S2_FIELDS = "title,abstract,year,venue,externalIds,openAccessPdf"


def _s2_search(protein: str, disease: str, seen_keys: set) -> list:
    """Third source, for what Europe PMC structurally misses: preprints and venues outside
    PubMed's index. Its recall is narrower but its coverage is *differently* shaped, which
    is the only reason to pay the extra call.

    Rate limits are aggressive even with a key, so this backs off and gives up quietly
    rather than holding up the whole check.
    """
    key = os.environ.get("SEMANTIC_SCHOLAR_API_KEY")
    headers = {"x-api-key": key} if key else {}
    query = f"{protein} {disease} Mendelian randomization"
    out = []
    for attempt in range(3):
        try:
            r = requests.get(S2, params={"query": query, "limit": 20, "fields": S2_FIELDS},
                             headers=headers, timeout=40)
            if r.status_code == 429:
                time.sleep(2 * (attempt + 1))
                continue
            r.raise_for_status()
            data = r.json().get("data", []) or []
        except (requests.RequestException, ValueError):
            return out
        for x in data:
            ext = x.get("externalIds") or {}
            # Check EVERY id the record carries, not the first non-empty one. The old
            # first-non-empty cascade let the same paper through twice whenever the
            # Europe PMC record had a pmid but the Semantic Scholar record only a DOI —
            # common for preprints indexed both ways.
            keys = [str(v).lower() for v in
                    (ext.get("PMID"), ext.get("DOI"), (x.get("title") or "")[:60]) if v]
            if not keys or any(k in seen_keys for k in keys):
                continue
            seen_keys.update(keys)
            out.append({
                "pmid": ext.get("PMID"), "doi": ext.get("DOI"),
                "title": x.get("title"), "journal": x.get("venue"), "year": x.get("year"),
                "abstract": (x.get("abstract") or "")[:2500],
                "_source": "semantic_scholar",
            })
        return out
    return out


# ----------------------------------------------------------------- LLM judge
_JUDGE_PROMPT = """You are screening abstracts for one specific question.

QUESTION: does this paper report a Mendelian randomization (MR) analysis in which
  EXPOSURE  = {protein}  (the protein/gene, or its plasma level)
  OUTCOME   = {disease}  (or a clearly equivalent phenotype)

Answer with JSON only, no prose:
{{"verdict": "dedicated" | "swept" | "unrelated", "reason": "<one short sentence>"}}

Use "dedicated" when this pair is one the paper is actually about — it appears in the
title, aims, or headline results.
Use "swept" when the paper is a large screen (many exposures or many outcomes) that would
have included this pair, but the pair is not what the paper is about.
Use "unrelated" when the paper does not test this pair at all, or is not MR.

Be strict. If the exposure is a different molecule, or the outcome is a different disease,
answer "unrelated". Do not use outside knowledge; judge only what the abstract says.

TITLE: {title}
ABSTRACT: {abstract}
"""


def _judge(client, model, protein, disease, hit):
    try:
        resp = client.models.generate_content(
            model=model,
            contents=_JUDGE_PROMPT.format(protein=protein, disease=disease,
                                          title=hit.get("title") or "",
                                          abstract=hit.get("abstract") or ""),
        )
        txt = (resp.text or "").strip()
        m = re.search(r"\{.*\}", txt, re.S)
        if not m:
            return None
        v = json.loads(m.group())
        if v.get("verdict") in ("dedicated", "swept", "unrelated"):
            return v
    except Exception:
        return None
    return None


def get_published_mr(protein: str, disease: str, use_llm: bool = True) -> dict:
    """Check whether an MR analysis of this protein-disease pair has ever been PUBLISHED.

    Use this to tell a genuine evidence gap ("nobody has run this") from a mere database
    gap ("our precomputed resource lacks it"). Inputs: protein (gene symbol) and disease
    name. Searches MR-KG (LLM-extracted MR literature) and Europe PMC with synonym
    expansion, then judges candidate abstracts.

    Returns a THREE-VALUED verdict — dedicated / swept / no_record — never a bare yes-no.
    "no_record" means nothing was found, which is a candidate for analysis and NOT proof
    that the analysis was never done.
    """
    p_syns = _protein_synonyms(protein)
    d_syns = _disease_synonyms(disease)

    # --- source 1: MR-KG structured pairs -------------------------------
    mrkg_hits, mrkg_matched = [], []
    for s in _mrkg_candidates(protein, p_syns):
        pairs = _mrkg_pairs(s["pmid"])
        for pr in pairs:
            exp, out = (pr.get("exposure") or ""), (pr.get("outcome") or "")
            if any(x.lower() in exp.lower() for x in p_syns) and \
               any(x.lower() in out.lower() for x in d_syns):
                mrkg_matched.append({"pmid": s["pmid"], "title": s.get("title"),
                                     "journal": s.get("journal"), "pair": pr})
        mrkg_hits.append({"pmid": s["pmid"], "title": s.get("title"),
                          "n_pairs_extracted": len(pairs), "via": s.get("_via")})
        time.sleep(0.1)

    # --- source 2: Europe PMC -------------------------------------------
    epmc_hits, epmc_total, epmc_query = _epmc_search(p_syns, d_syns)

    # --- source 3: Semantic Scholar (preprints / non-PubMed venues) ------
    # Seed the dedup set with EVERY id each EPMC hit carries (see _s2_search for why).
    seen_keys = set()
    for h in epmc_hits:
        seen_keys.update(str(v).lower() for v in
                         (h.get("pmid"), h.get("doi"), (h.get("title") or "")[:60]) if v)
    s2_hits = _s2_search(protein, disease, seen_keys)
    epmc_hits = epmc_hits + s2_hits          # judged together from here on

    # --- judge ------------------------------------------------------------
    judged, judge_note = [], None
    client = model = None
    if use_llm:
        try:
            from dotenv import load_dotenv
            from google import genai
            load_dotenv()
            key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
            if key:
                client = genai.Client(api_key=key)
                model = "gemini-flash-lite-latest"
        except Exception:
            client = None

    if client:
        for h in epmc_hits[:MAX_ABSTRACTS_TO_JUDGE]:
            if not h.get("abstract"):
                continue
            v = _judge(client, model, protein, disease, h)
            if v and v["verdict"] != "unrelated":
                judged.append({**{k: h[k] for k in ("pmid", "doi", "title", "journal", "year")},
                               "source": h.get("_source", "europe_pmc"),
                               "verdict": v["verdict"], "reason": v.get("reason")})
            time.sleep(0.2)
        if len(epmc_hits) > MAX_ABSTRACTS_TO_JUDGE:
            judge_note = (f"Only the first {MAX_ABSTRACTS_TO_JUDGE} of {len(epmc_hits)} "
                          f"retrieved abstracts were judged.")
    else:
        judge_note = ("No model available: abstracts were NOT judged, so hits below are "
                      "keyword matches only and over-count.")

    # --- verdict ----------------------------------------------------------
    dedicated = [j for j in judged if j["verdict"] == "dedicated"] + \
                [{"pmid": m["pmid"], "title": m["title"], "journal": m.get("journal"),
                  "source": "mr_kg",
                  # Keep MR-KG's structured extraction row. It is the ONLY literature-side
                  # object in this pipeline that names the exposure and outcome in a
                  # machine-readable way — an earlier version dropped it right here, which
                  # made cross-source direction comparison unrecoverable by construction.
                  "pair": m.get("pair"),
                  "verdict": "dedicated", "reason": "MR-KG extracted this exposure-outcome pair"}
                 for m in mrkg_matched]
    # One paper, one row: the same pmid can arrive via the judged abstracts AND via MR-KG.
    # Prefer the MR-KG row when both exist, because it carries the structured pair.
    by_pmid = {}
    for d in dedicated:
        k = str(d.get("pmid") or d.get("doi") or d.get("title"))
        if k not in by_pmid or (d.get("pair") and not by_pmid[k].get("pair")):
            by_pmid[k] = d
    dedicated = list(by_pmid.values())
    swept = [j for j in judged if j["verdict"] == "swept"]

    n_judged = min(len(epmc_hits), MAX_ABSTRACTS_TO_JUDGE) if client else 0
    coverage = (n_judged / len(epmc_hits)) if epmc_hits else 1.0

    if dedicated:
        verdict, confidence = "dedicated", "high"
        note = "At least one publication reports MR for this pair. This is NOT an evidence gap."
    elif swept:
        verdict, confidence = "swept", "high"
        note = ("This pair falls inside a published large-scale screen but no paper is about "
                "it — computed by someone, interpreted by no-one. Arguably still a gap, but "
                "say so precisely.")
    else:
        verdict = "no_record"
        confident = client and coverage >= MIN_COVERAGE_FOR_CONFIDENT_GAP
        confidence = "moderate" if confident else "low"
        note = ("No published MR found for this pair in MR-KG or Europe PMC under the "
                "synonyms tried. A CANDIDATE for analysis — NOT proof it has never been "
                "done. Recall is bounded by synonym coverage and by abstract-level "
                "screening: a pair buried in a large screen's supplementary table is "
                "invisible here.")
        if not confident:
            note = ("LOW-CONFIDENCE 'no record': only "
                    f"{n_judged} of {len(epmc_hits)} retrieved abstracts were screened "
                    f"({coverage:.0%}). Do not report this pair as an evidence gap without "
                    f"screening more of them. ") + note
    if judge_note:
        note += " " + judge_note

    return {
        "found": verdict != "no_record",
        "verdict": verdict,
        "confidence": confidence,
        "screening_coverage": round(coverage, 3),
        "n_abstracts_screened": n_judged,
        "protein": protein,
        "disease": disease,
        "dedicated_papers": dedicated[:8],
        "swept_papers": swept[:5],
        "n_candidates_total": len(epmc_hits),
        "n_epmc_reported_total": epmc_total,
        "n_semantic_scholar_extra": len(s2_hits),
        "n_mrkg_studies_seen": len(mrkg_hits),
        "protein_synonyms_used": p_syns[:6],
        "disease_synonyms_used": d_syns[:6],
        "epmc_query": epmc_query,
        "judged_by_model": bool(client),
        "note": note,
        "url": "https://europepmc.org/",
        "source_release": ("Europe PMC REST + Semantic Scholar + MR-KG "
                           "(Bristol MRC IEU, LLM-extracted MR literature; queried via its "
                           "public API, code not used — MR-KG is GPL-3.0)"),
    }


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    for prot, dis in [("IL6R", "coronary heart disease"), ("PNPLA3", "MASLD"),
                      ("CTRB1", "type 2 diabetes")]:
        r = get_published_mr(prot, dis)
        print("=" * 70)
        print(f"{prot} x {dis}  ->  {r['verdict']}")
        print(f"  candidates={r['n_candidates_total']} (epmc {r['n_epmc_reported_total']}, +S2 {r['n_semantic_scholar_extra']}) "
              f"| mrkg studies={r['n_mrkg_studies_seen']} | judged={r['judged_by_model']}")
        print(f"  confidence={r['confidence']}  coverage={r['screening_coverage']:.0%} ({r['n_abstracts_screened']} judged)")
        for d in r["dedicated_papers"][:3]:
            print(f"  DEDICATED  {d.get('pmid')}  {str(d.get('title'))[:70]}")
        for s in r["swept_papers"][:2]:
            print(f"  SWEPT      {s.get('pmid')}  {str(s.get('title'))[:70]}")
