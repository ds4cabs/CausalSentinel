# -*- coding: utf-8 -*-
"""Screenshot the running OpenCausal app (localhost:8503) for README + deck."""
from playwright.sync_api import sync_playwright

URL = "http://localhost:8503"
OUT = "figs"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1440, "height": 980})
    page.goto(URL, wait_until="networkidle")
    page.wait_for_timeout(3000)

    page.screenshot(path=f"{OUT}/app_01_home.png")
    print("saved app_01_home.png")

    page.get_by_role("button", name="Build the evidence card").click()
    page.get_by_text("Download this card", exact=False).first.wait_for(timeout=180_000)
    page.wait_for_timeout(2500)
    page.screenshot(path=f"{OUT}/app_02_card.png")
    print("saved app_02_card.png")

    browser.close()
