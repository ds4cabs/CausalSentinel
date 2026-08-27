# -*- coding: utf-8 -*-
"""Screenshot tour of the running OpenCausal app (localhost:8501) for README + deck.

Captures the whole product, one shot per surface:
  app_01_home.png      the build tab before a run
  app_02_card.png      a freshly built card — verdict, code-written reading, panels
  app_03_figures.png   the two live figures under the card (forest + constraint)
  app_04_viewer.png    the ten worked cards, viewer engine
  app_05_timeline.png  the hand-verified genetics -> clinic timelines
  app_06_gallery.png   the 991-protein gallery
"""
from playwright.sync_api import sync_playwright

URL = "http://localhost:8501"
OUT = "figs"
VIEW = {"width": 1440, "height": 980}


def viewer_frame(page):
    """The component iframe that carries the viewer engine (has a #card node)."""
    for f in page.frames:
        if f == page.main_frame:
            continue
        try:
            if f.locator("#card").count():
                return f
        except Exception:
            continue
    return None


with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport=VIEW)
    page.goto(URL, wait_until="networkidle")
    page.wait_for_timeout(3000)

    # 1 — home
    page.screenshot(path=f"{OUT}/app_01_home.png")
    print("saved app_01_home.png")

    # 2 — build a card, wait for the download button that ends the run
    page.get_by_role("button", name="Build the evidence card").click()
    page.get_by_text("Download this card", exact=False).first.wait_for(timeout=180_000)
    page.wait_for_timeout(2500)
    page.mouse.wheel(0, 520)
    page.wait_for_timeout(600)
    page.screenshot(path=f"{OUT}/app_02_card.png")
    print("saved app_02_card.png")

    # 3 — the figures expander sits below the embedded card
    figs = page.get_by_text("Figures — drawn from tool output", exact=False).first
    figs.scroll_into_view_if_needed()
    page.wait_for_timeout(2500)
    page.screenshot(path=f"{OUT}/app_03_figures.png")
    print("saved app_03_figures.png")

    # 4 — ten worked cards (viewer engine, GO banner on top)
    page.get_by_role("tab", name="Ten worked cards").click()
    page.wait_for_timeout(5000)
    page.screenshot(path=f"{OUT}/app_04_viewer.png")
    print("saved app_04_viewer.png")

    # 5 — the genetics -> clinic timelines inside the embedded viewer
    fr = viewer_frame(page)
    if fr:
        fr.locator('button.tab[data-tab="timeline"]').click()
        page.wait_for_timeout(1500)
        fr.locator(".tl-case").first.scroll_into_view_if_needed()
        page.wait_for_timeout(600)
        page.screenshot(path=f"{OUT}/app_05_timeline.png")
        print("saved app_05_timeline.png")

    # 6 — the 991-protein gallery
    page.get_by_role("tab", name="991-protein gallery").click()
    page.wait_for_timeout(5000)
    page.screenshot(path=f"{OUT}/app_06_gallery.png")
    print("saved app_06_gallery.png")

    # 7 — pick your databases: un-tick six sources, build with three, and show the
    # sidebar chips next to a card whose skipped panels say "tool not called"
    page.get_by_role("tab", name="Build a card").click()
    page.wait_for_timeout(1000)
    ms = page.locator('[data-testid="stMultiSelect"]')
    for label in ["🏥 Clinical record (Open Targets)",
                  "🎯 Target-disease association (Open Targets)",
                  "💊 Druggability (ChEMBL)", "🩺 Clinical variants (ClinVar)",
                  "⚗️ Pharmacogenomics (ClinPGx)", "📈 GWAS signal (GWAS Catalog)"]:
        btn = ms.get_by_role("button", name=f"Remove {label}")
        if btn.count():
            btn.first.click()
            page.wait_for_timeout(400)
    page.get_by_role("button", name="Build the evidence card").click()
    # the PREVIOUS card (all nine sources) stays on screen while the subset run is in
    # flight, so waiting for the Download button returns immediately — instead poll the
    # embedded card until a skipped panel says "tool not called in this run"
    for _ in range(60):
        page.wait_for_timeout(2000)
        done = False
        for fr in page.frames:
            if fr == page.main_frame:
                continue
            try:
                if fr.locator("#card").count() and \
                   "tool not called in this run" in fr.evaluate(
                       "document.getElementById('card').innerText"):
                    done = True
            except Exception:
                pass
        if done:
            break
    page.wait_for_timeout(1500)
    page.mouse.wheel(0, 420)
    page.wait_for_timeout(600)
    page.screenshot(path=f"{OUT}/app_07_pick_sources.png")
    print("saved app_07_pick_sources.png")

    browser.close()
