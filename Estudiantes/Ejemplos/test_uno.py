import re
from playwright.sync_api import Page, expect


def test_uno(page: Page):
    page.goto("https://playwright.dev/")
    expect(page).to_have_title(re.compile("Playwright"))

    #busca en la pagina un boton y le da click
    buton_uno = page.locator("text=Get started")
    expect(buton_uno).to_have_attribute("href","/docs/intro")
    
    #tomar foto inicial
    page.screenshot(path="imagenes/test_uno.png")
    buton_uno.click()

    #tomat foto final
    page.screenshot(path="imagenes/test_uno.png")

    #validando el resultado enla pagina destino
    expect(page).to_have_url(re.compile(".*docs/intro"))