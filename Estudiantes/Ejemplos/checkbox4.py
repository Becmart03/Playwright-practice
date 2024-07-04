"""
playwright codegen https://datatables.net/extensions/select/examples/checkbox/checkbox.html
Este comando graba todo lo que realizas en el navegador
"""


import re, time
from playwright.sync_api import Playwright, sync_playwright, expect


def test_checkbox3(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
        viewport={"width":1500, "height":800},
        record_video_dir="videos/checkbox"
    )
    page = context.new_page()
    page.goto("https://datatables.net/extensions/select/examples/checkbox/checkbox.html")
    expect(page).to_have_title("Pruebas de campos checkbox")
    page.set_default_timeout(5000)
    time.sleep(2)

    for i in range(1,11):
        page.locator(f"(//input[contains(@aria-label,'Select row')])[1]").click() #no sirve el xpath


    context.close()
    browser.close()
