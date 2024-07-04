import re
import time
import random
import pytest
import sys
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from Estudiantes.Ejemplos.funciones import FuncionesGlobales




tiempo = 1.3
pdf1 = "Estudiantes/Ejemplos/pdf/Documento.pdf"
ruta = "Estudiantes/Ejemplos/upload"
url = "https://www.saucedemo.com/v1/"


@pytest.fixture(scope="session")
#con el fixture se le dice que va a aplciar a las funciones yq ue todo lo que se ponga dentro del set_up
#se va a aplicar dentro de las demas sesiones
def set_up(playwright: Playwright)->None:
    browser = playwright.chromium.launch(headless = False, slow_mo = tiempo)
    context = browser.new_context(
        viewport={"width":1500, "height":800}
    )
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    page.goto(url)
    page.set_default_timeout(5000)

    F = FuncionesGlobales(page)
    F.validar_titulo_pagina('Swag Labs')
    F.scroll_xy(0,400)
    


    F.click_normal("//input[contains(@type,'text')]", tiempo)
    F.texto("//input[contains(@type,'text')]", "standard_user",tiempo)
    F.click_normal("//input[contains(@type,'password')]", tiempo)
    F.texto("//input[contains(@type,'password')]", "secret_sauce")
    F.click_normal("//input[contains(@type,'submit')]", tiempo)
    F.click_normal("//input[@type='submit']", tiempo)
    F.Espera(5)
    yield page
    context.tracing.stop(path='trace.zip')

    context.close()
    browser.close()


