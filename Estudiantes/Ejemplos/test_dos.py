import asyncio
import re
from playwright.sync_api import sync_playwright,Page, expect


def test_dos(page: Page):
    page.goto("https://demoqa.com/")
    expect(page).not_to_have_title("ToolsQA")

    #boton uno #metdodo uno
    # boton_uno = page.locator("text=Elements")
    # page.screenshot(path="imagenes/boton_uno.png")
    # boton_uno.click()
    # page.screenshot(path="imagenes/boton_uno_clock.png")

    #segundo metodo, ahoora 2 lineas mas de codigo llamando al metodo click directamente
    page.locator("text=Elements").click()
    page.screenshot(path="imagenes/boton_uno_click.png")
    

    #validar la URL
    expect(page).to_have_url(re.compile(".*elements"))

    page.locator("text=Text Box").click()
    page.screenshot(path="imagenes/boton_dos_click.png")


    #validar la segunda URL
    expect(page).to_have_url(re.compile(".*text-box"))

    #Primer agregada de texto en el campo nombre primer metodo
    #page.locator("#userName").fill("Rodrigo")

    #segundo metodo agregada de texto busqueda por xpath
    page.locator("//input[contains(@placeholder,'Full Name')]").fill("Rodrigo")
    page.screenshot(path="imagenes/texto_nombre.png")

    