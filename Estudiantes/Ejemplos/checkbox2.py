"""
playwright codegen http://demoqa.com/checkbox
Este comando graba todo lo que realizas en el navegador
"""


import re, time
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demoqa.com/checkbox")
    page.get_by_label("Toggle").click()
    page.locator("li").filter(has_text=re.compile(r"^Desktop$")).get_by_label("Toggle").click()
    page.locator("label").filter(has_text="Commands").get_by_role("img").first.click()

    # ---------------------
    time.sleep(3)
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
