"""Tool: classify_exposure_mechanism — WHY a plasma-pQTL MR sign may or may not match
the pharmacological direction, decided from retrievable features rather than asserted.

THE QUESTION THIS ANSWERS
-------------------------
"The retrieval does not cover drug action, so do not claim it" is a refusal, not an
explanation. The useful question is: **when does the sign of a plasma-protein MR invert
relative to what a drug would do, and can that be predicted in advance?**

It can, because a plasma protein concentration is not one quantity. It is the net of

    synthesis -> secretion -> proteolytic processing / ectodomain shedding
              -> complex formation -> receptor-mediated and renal clearance
              -> and finally, whether the assay reagent still binds

Only the synthesis route makes "higher plasma level" mean "more pathway activity". Each
of the others can inverte the sign, and they leave different, RETRIEVABLE fingerprints:

  production          secreted protein, no shed form, regulatory instrument
                      -> plasma level tracks synthesis, SIGN PRESERVED
  shedding_decoy      transmembrane protein with an annotated soluble/shed form
                      -> plasma level can rise while membrane signalling FALLS,
                         SIGN MAY INVERT
  processing_cleavage annotated cleavage generating active/inactive species
                      -> the assay may be measuring the wrong species
  assay_epitope_risk  the instrument is, or tags, a missense variant in the assayed
                      protein -> the pQTL may be reagent binding, not abundance

IL6R IS THE WORKED CASE, AND IT IS NOT AN ANECDOTE
--------------------------------------------------
Retrieved live 2026-08-16:

  UniProt P08887  Transmembrane x1; a separately annotated molecule "Soluble
                  interleukin-6 receptor subunit alpha" with its own subcellular
                  location; PTM comment "A short soluble form is released from the
                  membrane..."
  Ensembl VEP     instrument rs4129267 is an INTRON variant in IL6R, but it tags
                  rs2228145 = missense D/A at position 358 (r2 ~0.96-0.99 in Europeans)

So IL6R classifies as shedding_decoy WITH assay_epitope_risk, and sign inversion is the
EXPECTED behaviour, not a surprise: the 358Ala allele accelerates ADAM-mediated shedding,
raising soluble receptor while impairing classical signalling. "Genetically higher plasma
IL6R" and "IL-6R blockade is protective" are then the same statement.

LPA classifies as production: no transmembrane segment, no shedding annotation, intronic
instrument. Sign preserved. Same tool, same run, opposite class — which is why the two
cards should never have been given the same interpretive treatment.

WHAT IS STILL MISSING, NAMED
----------------------------
The one discriminator we cannot compute here is the SNP -> PROTEIN effect direction:
EpiGraphDB exposes the MR estimate and the instrument's alleles, but not the pQTL beta.
With it, eQTL/pQTL sign concordance would separate "post-transcriptional" from
"transcriptional" directly. Getting it means going back to the original pQTL summary
statistics (Sun 2018 and friends are downloadable), not to EpiGraphDB. That is the
highest-value next step and it is NOT done here.

Nothing in this file is computed from data we hold: every field is retrieved and cited.
"""
import re
import requests

UNIPROT = "https://rest.uniprot.org/uniprotkb"
VEP = "https://rest.ensembl.org/vep/human/id"
GWASCAT = "https://www.ebi.ac.uk/gwas/rest/api"

_SHED_RE = re.compile(r"\bshed\w*|soluble form|released from the membrane|"
                      r"ectodomain|ADAM\d*|sheddase", re.I)
_CLEAVE_RE = re.compile(r"\bcleav\w*|proteolytic|autolysis|furin|propeptide|"
                        r"zymogen|maturation", re.I)
_PTV = {"stop_gained", "frameshift_variant", "splice_acceptor_variant",
        "splice_donor_variant", "start_lost", "stop_lost"}


def _uniprot_features(accession: str) -> dict:
    try:
        r = requests.get(f"{UNIPROT}/{accession}.json", timeout=45)
        r.raise_for_status()
        d = r.json()
    except (requests.RequestException, ValueError) as e:
        return {"error": f"UniProt request failed: {e}"}

    feats = d.get("features") or []
    types = [f.get("type") for f in feats]
    n_tm = sum(1 for t in types if t == "Transmembrane")

    shed_evidence, cleave_evidence, soluble_molecules = [], [], []
    for c in (d.get("comments") or []):
        ctype = c.get("commentType")
        # A separately named molecule with its own location is the strongest signal that
        # the plasma species differs from the membrane species.
        if ctype == "SUBCELLULAR LOCATION" and c.get("molecule"):
            mol = c["molecule"]
            locs = [((loc.get("location") or {}).get("value")) for loc in
                    (c.get("subcellularLocations") or [])]
            if re.search(r"soluble|secreted|shed", f"{mol} {locs}", re.I):
                soluble_molecules.append({"molecule": mol, "locations": locs})
        for t in (c.get("texts") or []):
            v = t.get("value") or ""
            if ctype in ("PTM", "FUNCTION", "SUBCELLULAR LOCATION"):
                if _SHED_RE.search(v):
                    shed_evidence.append(v[:220])
                elif _CLEAVE_RE.search(v):
                    cleave_evidence.append(v[:220])

    return {
        "accession": accession,
        "n_transmembrane": n_tm,
        "has_signal_peptide": "Signal" in types,
        "n_chains": sum(1 for t in types if t == "Chain"),
        "soluble_molecules": soluble_molecules,
        "shedding_evidence": shed_evidence[:3],
        "cleavage_evidence": cleave_evidence[:3],
        "url": f"https://www.uniprot.org/uniprotkb/{accession}",
    }


def _variant_consequence(rsid: str, expected_gene: str = "") -> dict:
    try:
        r = requests.get(f"{VEP}/{rsid}", headers={"Accept": "application/json"}, timeout=45)
        r.raise_for_status()
        body = r.json()
    except (requests.RequestException, ValueError) as e:
        return {"error": f"Ensembl VEP request failed: {e}"}
    if not isinstance(body, list) or not body:
        return {"found": False, "rsid": rsid}

    d = body[0]
    tcs = d.get("transcript_consequences") or []
    genes = sorted({t.get("gene_symbol") for t in tcs if t.get("gene_symbol")})
    aa = next(({"amino_acids": t.get("amino_acids"), "position": t.get("protein_start"),
                "gene": t.get("gene_symbol")}
               for t in tcs if t.get("amino_acids")), None)
    cons = d.get("most_severe_consequence")

    # "cis" in a pQTL resource means a POSITION WINDOW around the gene. It does not mean
    # the variant acts on that gene. PCSK9's cis instrument rs191448950 is annotated by
    # VEP to USP24, the neighbour — exactly the LD-with-a-neighbouring-gene confounding
    # that a single-instrument Wald ratio with no colocalization cannot exclude.
    gene_mismatch = bool(expected_gene and genes and expected_gene.upper() not in
                         {g.upper() for g in genes})
    return {
        "found": True,
        "rsid": rsid,
        "most_severe_consequence": cons,
        "genes_annotated": genes,
        "amino_acid_change": aa,
        "is_missense": cons == "missense_variant",
        "is_ptv": cons in _PTV,
        "annotated_to_a_different_gene": gene_mismatch,
        "url": f"https://www.ensembl.org/Homo_sapiens/Variation/Explore?v={rsid}",
    }


def _gc(url: str) -> dict:
    try:
        r = requests.get(url, headers={"Accept": "application/json"}, timeout=45)
        r.raise_for_status()
        return r.json()
    except (requests.RequestException, ValueError):
        return {}


def instrument_effect_profile(rsid: str, gene_symbol: str = "", max_assoc: int = 40) -> dict:
    """Everything one instrument is reported to affect, with every effect anchored to the
    SAME allele so the signs can be compared.

    This is the discriminator that was previously listed as unavailable. EpiGraphDB gives
    the MR estimate but not the SNP -> protein beta; the GWAS Catalog gives the SNP's own
    associations, free and without authentication, so the effect on the protein and the
    effect on downstream readouts can be read off together.

    Betas in the GWAS Catalog are reported against whichever allele each study called the
    risk allele. Comparing them without re-anchoring is how sign errors get made, so every
    row here is flipped onto a single reference allele and `flipped` records whether it was.

    Worked example, retrieved live: for rs4129267, anchoring on T gives
    interleukin-6 receptor alpha +1.21, C-reactive protein -0.079, fibrinogen -0.011. The
    allele that RAISES soluble receptor LOWERS both downstream inflammatory readouts, which
    is the shedding mechanism visible in summary data alone.
    """
    body = _gc(f"{GWASCAT}/singleNucleotidePolymorphisms/{rsid}/associations")
    assoc = (body.get("_embedded") or {}).get("associations") or []
    if not assoc:
        return {"found": False, "rsid": rsid,
                "note": f"No GWAS Catalog associations for {rsid}."}

    rows, anchor = [], None
    for a in assoc[:max_assoc]:
        beta = a.get("betaNum")
        if beta is None:
            continue
        allele_name = (((a.get("loci") or [{}])[0].get("strongestRiskAlleles") or [{}])[0]
                       .get("riskAlleleName") or "")
        allele = allele_name.split("-")[-1].strip().upper()
        if allele in ("", "?"):
            continue
        # "increase"/"decrease" is the sign; the API stores magnitude unsigned.
        signed = -abs(beta) if (a.get("betaDirection") or "").lower() == "decrease" else abs(beta)
        links = a.get("_links") or {}
        traits = [t.get("trait") for t in
                  ((_gc((links.get("efoTraits") or {}).get("href", "")).get("_embedded") or {})
                   .get("efoTraits") or [])]
        study = _gc((links.get("study") or {}).get("href", ""))
        author = ((study.get("publicationInfo") or {}).get("author") or {}).get("fullname")
        if anchor is None:
            anchor = allele
        flipped = allele != anchor
        rows.append({
            "trait": "; ".join(t for t in traits if t) or None,
            "beta_on_anchor_allele": -signed if flipped else signed,
            "unit": a.get("betaUnit"),
            "reported_allele": allele,
            "flipped_to_anchor": flipped,
            "p_value": a.get("pvalue"),
            "study_author": author,
        })

    if not rows:
        return {"found": False, "rsid": rsid,
                "note": (f"{len(assoc)} associations for {rsid}, but none carried both a "
                         f"signed beta and a named risk allele, so no sign comparison is "
                         f"possible.")}

    # The comparison that matters is protein-vs-downstream, so group rather than just
    # sorting by magnitude — the downstream readouts are usually the SMALLEST effects
    # (CRP moves 0.08 while the protein moves 1.2) and a magnitude sort buries exactly
    # the rows the user came for.
    # Built as an explicit alternation list. Writing this as
    #   (escape(gene) + "|") if gene else "" + <rest>
    # silently produced the pattern "IL6R|", whose empty right branch matches EVERY trait,
    # so every row was classified as a protein measurement.
    # KNOWN LIMITATION, stated rather than hidden: this matches the GWAS Catalog's trait
    # STRING, and trait strings are not harmonised to the gene symbol. LPA's protein
    # measurement is filed as "lipoprotein A", which no pattern built from the symbol "LPA"
    # will catch, so LPA returns no protein row and therefore no concordance verdict. This
    # is the same un-normalised-trait-layer problem seen in MR-KG and in EpiGraphDB's
    # outcome side; a real fix needs ontology mapping, not a longer regex.
    parts = [r"protein (?:amount|level|measurement)", r"subunit alpha measurement"]
    if gene_symbol:
        parts.insert(0, re.escape(gene_symbol))
    prot_re = re.compile("|".join(parts), re.I)
    on_protein = [r for r in rows if r["trait"] and prot_re.search(r["trait"])]
    downstream = [r for r in rows if r not in on_protein]

    verdict = None
    if on_protein and downstream:
        p_sign = 1 if on_protein[0]["beta_on_anchor_allele"] > 0 else -1
        opp = [d for d in downstream if d["beta_on_anchor_allele"] * p_sign < 0]
        same = [d for d in downstream if d["beta_on_anchor_allele"] * p_sign > 0]
        verdict = (f"On the {anchor} allele the protein moves "
                   f"{'UP' if p_sign > 0 else 'DOWN'}; of {len(downstream)} other traits "
                   f"with a signed effect, {len(same)} move the same way and {len(opp)} "
                   f"move the opposite way. Opposite-moving pathway readouts are the "
                   f"fingerprint of a plasma pool that does not track pathway activity.")

    return {
        "found": True,
        "computed_here": False,
        "rsid": rsid,
        "anchor_allele": anchor,
        "n_associations_total": len(assoc),
        "n_with_signed_effect": len(rows),
        "effects_on_this_protein": sorted(on_protein,
                                          key=lambda d: -abs(d["beta_on_anchor_allele"]))[:6],
        "effects_on_other_traits": sorted(downstream,
                                          key=lambda d: -abs(d["beta_on_anchor_allele"]))[:14],
        "concordance_verdict": verdict,
        "associations": sorted(rows, key=lambda d: -abs(d["beta_on_anchor_allele"]))[:20],
        "note": (f"All effects are anchored to the {anchor} allele; rows marked "
                 f"flipped_to_anchor had their sign reversed from the study's reported risk "
                 f"allele. Compare the effect on the protein itself against the effects on "
                 f"downstream readouts: if the allele that RAISES the protein LOWERS its "
                 f"pathway markers, the plasma pool is not tracking pathway activity and an "
                 f"MR sign will not match the pharmacological direction. "
                 f"{len(on_protein)} row(s) look like protein or biomarker measurements. "
                 f"Traits and units are as the source studies defined them and are NOT "
                 f"harmonised, so magnitudes are not comparable across rows — only signs are."),
        "source_release": "GWAS Catalog REST API, retrieved live; no authentication required",
        "url": f"https://www.ebi.ac.uk/gwas/variants/{rsid}",
    }


def classify_exposure_mechanism(gene_symbol: str, accession: str,
                                instrument_rsid: str = "",
                                tagged_variant_rsid: str = "") -> dict:
    """Decide what a cis-pQTL on this protein is actually instrumenting, and whether the
    MR sign is expected to match the pharmacological direction.

    Use this before turning a plasma-protein MR estimate into any statement about what a
    drug would do. Inputs: gene symbol, its UniProt accession, the instrument rsID, and
    optionally a known variant the instrument tags through LD (e.g. rs2228145 for IL6R).

    Returns a mechanism class, whether sign inversion is expected, and the retrieved
    evidence behind each call. The classes are production, shedding_decoy,
    processing_cleavage and assay_epitope_risk; a protein can carry more than one flag.
    """
    up = _uniprot_features(accession)
    if up.get("error"):
        return {"error": up["error"], "gene_symbol": gene_symbol}

    vep = _variant_consequence(instrument_rsid, gene_symbol) if instrument_rsid else {}
    tagged = _variant_consequence(tagged_variant_rsid, gene_symbol) if tagged_variant_rsid else {}

    flags, why = [], []
    is_membrane = up["n_transmembrane"] > 0
    sheds = bool(up["soluble_molecules"]) or bool(up["shedding_evidence"])

    if is_membrane and sheds:
        flags.append("shedding_decoy")
        why.append("membrane protein with an annotated soluble/shed species: the plasma "
                   "pool and the membrane pool are DIFFERENT quantities, and a variant "
                   "that accelerates shedding raises one while lowering the other")
    elif sheds:
        flags.append("processing_cleavage")
        why.append("a soluble or shed species is annotated without a transmembrane "
                   "segment: the assay may be measuring a processed form")
    elif up["cleavage_evidence"]:
        flags.append("processing_cleavage")
        why.append("annotated proteolytic processing can generate active and inactive "
                   "species that an affinity assay does not distinguish")

    epitope = False
    for v, label in ((vep, "instrument"), (tagged, "tagged variant")):
        if v.get("is_missense"):
            epitope = True
            aa = v.get("amino_acid_change") or {}
            why.append(f"the {label} {v['rsid']} is a MISSENSE variant "
                       f"({aa.get('amino_acids')} at {aa.get('position')}) in the assayed "
                       f"protein: an affinity reagent may bind the two forms differently, "
                       f"so the pQTL can reflect binding rather than abundance")
    if epitope:
        flags.append("assay_epitope_risk")

    if not flags:
        flags.append("production")
        why.append("secreted protein with no annotated shedding or processing and a "
                   "non-coding instrument: the plasma level plausibly tracks synthesis")

    inversion = "shedding_decoy" in flags
    if inversion:
        sign_note = ("SIGN INVERSION IS EXPECTED. Higher plasma protein here can mean LESS "
                     "pathway activity, so the MR sign and the therapeutic direction may "
                     "legitimately disagree. Do not 'correct' the card by flipping it — "
                     "state the abundance-outcome direction and say which species was "
                     "measured.")
    elif "assay_epitope_risk" in flags:
        sign_note = ("SIGN IS UNRELIABLE rather than inverted: if the pQTL is reagent "
                     "binding, the estimate is about the assay, not the protein. Seek "
                     "cross-platform or mass-spectrometry replication before using it.")
    elif "processing_cleavage" in flags:
        # An earlier version dropped this case into the "nothing found" branch, so PCSK9
        # was flagged processing_cleavage and told in the same breath that no processing
        # mechanism had been retrieved. A tool that contradicts its own flag is worse than
        # one that stays silent.
        sign_note = ("SIGN DIRECTION IS PROBABLY PRESERVED BUT THE MAGNITUDE IS NOT "
                     "INTERPRETABLE: annotated proteolytic processing means the assay may "
                     "be measuring total protein across active and inactive species. A "
                     "one-SD change in the measured quantity is not a one-SD change in "
                     "the active pool, so treat the effect size as ordinal, not as a dose.")
    else:
        sign_note = ("SIGN IS EXPECTED TO BE PRESERVED: no shedding, processing or epitope "
                     "mechanism was retrieved that would decouple plasma abundance from "
                     "pathway activity.")

    gene_mismatch = vep.get("annotated_to_a_different_gene")
    if gene_mismatch:
        why.append(f"the instrument {vep['rsid']} is labelled cis for {gene_symbol} but "
                   f"VEP annotates its transcript consequence to {vep['genes_annotated']}. "
                   f"'cis' is a position window, not evidence that the variant acts on "
                   f"this gene — this is the LD-with-a-neighbouring-gene confounding that "
                   f"a single-instrument Wald ratio without colocalization cannot exclude")

    return {
        "found": True,
        "computed_here": False,
        "gene_symbol": gene_symbol,
        "mechanism_flags": flags,
        "sign_inversion_expected": inversion,
        "sign_guidance": sign_note,
        "reasoning": why,
        "instrument_may_act_on_another_gene": bool(gene_mismatch),
        "uniprot": up,
        "instrument_consequence": vep or None,
        "tagged_variant_consequence": tagged or None,
        "next_check": ("Run instrument_effect_profile(instrument_rsid, gene_symbol) to see "
                       "the SNP's own effects on the protein AND on downstream readouts, "
                       "all anchored to one allele. If the allele that raises the protein "
                       "lowers its pathway markers, the inversion is confirmed in summary "
                       "data — no individual-level access and no bulk download needed."),
        "still_not_available": ("eQTL/pQTL effect-size concordance in a MATCHED tissue. The "
                                "GWAS Catalog route gives the SNP->protein effect, but "
                                "pairing it with a tissue-specific transcript effect on the "
                                "same allele still needs the original pQTL summary "
                                "statistics or an OpenGWAS token (free, but registration "
                                "required since May 2024)."),
        "source_release": "UniProt REST + Ensembl VEP REST, retrieved live",
    }


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    cases = [
        ("IL6R", "P08887", "rs4129267", "rs2228145"),
        ("LPA", "P08519", "rs55730499", ""),
        ("PCSK9", "Q8NBP7", "rs191448950", ""),
    ]
    for sym, acc, inst, tag in cases:
        r = classify_exposure_mechanism(sym, acc, inst, tag)
        print("=" * 76)
        print(f"{sym}  flags={r['mechanism_flags']}  inversion_expected={r['sign_inversion_expected']}")
        print(f"  {r['sign_guidance']}")
        for w in r["reasoning"]:
            print(f"   - {w}")
        if r["instrument_may_act_on_another_gene"]:
            print("   !! instrument annotated to a different gene")
        prof = instrument_effect_profile(inst, sym)
        if prof.get("found"):
            print(f"   --- effects anchored to the {prof['anchor_allele']} allele "
                  f"({prof['n_with_signed_effect']}/{prof['n_associations_total']} signed)")
            print("   on the protein itself:")
            for a in prof["effects_on_this_protein"][:3]:
                print(f"     {a['beta_on_anchor_allele']:+9.4g}  {str(a['trait'])[:50]}")
            print("   on other traits:")
            for a in prof["effects_on_other_traits"][:6]:
                print(f"     {a['beta_on_anchor_allele']:+9.4g}  {str(a['trait'])[:50]}")
            if prof.get("concordance_verdict"):
                print(f"   => {prof['concordance_verdict']}")
        else:
            print(f"   effect profile: {prof.get('note')}")
        print()
