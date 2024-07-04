import re
import time
import random
import pytest
import sys
from playwright.sync_api import Page, expect, Playwright, sync_playwright




tiempo = 1.3
pdf1 = "Estudiantes/Ejemplos/pdf/Documento.pdf"
ruta = "Estudiantes/Ejemplos/upload"
url = "https://www.saucedemo.com/v1/"


@pytest.fixture(scope="function")
#con el fixture se le dice que va a aplciar a las funciones yq ue todo lo que se ponga dentro del set_up
#se va a aplicar dentro de las demas funciones
def set_up(playwright: Playwright)->None:
    browser = playwright.chromium.launch(headless = False, slow_mo = tiempo)
    context = browser.new_context(
        viewport={"width":1500, "height":800}
    )
    context.tracing.start()
    page = context.new_page()
    page.goto(url)
    page.set_default_timeout(5000)

    yield page

    context.close()
    browser.close()


