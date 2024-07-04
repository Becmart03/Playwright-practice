"""
playwright codegen http://demoqa.com/checkbox
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
    page.goto("https://demoqa.com/checkbox")
    expect(page).to_have_title("Pruebas de campos checkbox")
    page.set_default_timeout(5000)

    #mover el mouse hacia abajo
    page.mouse.wheel(0,400)
    

    context.close()
    browser.close()
