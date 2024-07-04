
import re
import time
from playwright.sync_api import Page, expect, Playwright, sync_playwright


def test_checkbox(playwright: Playwright) ->None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    #grabar un video
    context = browser.new_context(record_video_dir="Videos/checkbox")

    #cambiar el tamaño de las paginas
    context = browser.new_context(
        viewport={'width':1500, 'height':800}
    )

    
    page = context.new_page()

    page.goto("http://demoqa.com/checkbox")
    expect(page).to_have_title("DEMOQA")

    page.set_default_timeout(5000)


    """
    primera manera de aproximacion -------------------------------
    che1 = page.locator("//button[contains(@aria-label,'Toggle')]")
    
    expect(che1).to_be_visible()
    che1.click()

    page.locator("(//button[contains(@aria-label,'Toggle')])[2]").click
    time.sleep(3)

    page.locator("(//button[contains(@aria-label,'Toggle')])[2]").click

    page.locator("")

    context.close()
    browser.close()
    """

    """segunda manera de aproximacion---------------------------------
    
    #localizo la clase del boton
    page.locator("[aria-label=Toggle]").click()
    #segundo elemento
    page.locator("[aria-label=Toggle]").nth(1).click()
    #tercer elemento
        #primera forma
    page.locator("text=Commands").click()
        #segunda forma
    page.locator("text=NotesCommands >> svg").nth(2).click()
    """

    """tercera manera de aproximacion---------------------------------
    

    """

    page.locator("(//button[contains(@aria-label,'Toggle')])[2]").click
    time.sleep(3)

    page.locator("(//button[contains(@aria-label,'Toggle')])[2]").click

    page.locator("")

    context.close()
    browser.close()