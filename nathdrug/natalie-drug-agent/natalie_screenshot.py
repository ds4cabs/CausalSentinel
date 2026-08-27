"""
natalie_screenshot.py
=====================
Captures screenshots of the running Natalie Streamlit app into
natalie_screenshots/ for the README. Requires the app to be running at
http://localhost:8501 (start it with ./natalie_run.sh app).

    python natalie_screenshot.py
"""
from playwright.sync_api import sync_playwright

URL = "http://localhost:8501"
OUT = "natalie_screenshots"


def main() -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1400, "height": 1000})
        page.goto(URL, wait_until="networkidle")
        page.wait_for_timeout(2500)

        # 1) Landing page
        page.screenshot(path=f"{OUT}/natalie_01_home.png")
        print("saved natalie_01_home.png")

        # 2) Click "Compare drugs" and wait for the results to render.
        page.get_by_role("button", name="Compare drugs").click()
        summary = page.get_by_text("AI summary", exact=False).first
        summary.wait_for(timeout=120_000)
        page.wait_for_timeout(1500)

        # Top of results: tool-call trace + start of the comparison table.
        page.screenshot(path=f"{OUT}/natalie_02_toolcalls.png")
        print("saved natalie_02_toolcalls.png")

        # 3) Scroll the AI summary into view and capture it.
        summary.scroll_into_view_if_needed()
        page.wait_for_timeout(800)
        page.screenshot(path=f"{OUT}/natalie_03_summary.png")
        print("saved natalie_03_summary.png")

        browser.close()


if __name__ == "__main__":
    main()
