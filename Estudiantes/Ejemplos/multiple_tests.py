import re
import time
from playwright.sync_api import expect, Playwright, sync_playwright
from Estudiantes.Ejemplos.funciones import FuncionesGlobales
import random
import pytest

ruta = "Estudiantes/Ejemplos/upload"
pdf1 = "Estudiantes/Ejemplos/pdf"
tiempo = 10

# @pytest.mark.skip(reason="modulo esta inhabilitado")
# @pytest.mark.xfail(reason="modulo esta inhabilitado")
@pytest.mark.skipif(tiempo>1.5,reason="modulo esta inhabilitado")
def test_inicio(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(
        viewport={"width":1500, "height":800},
        #record_video_dir="videos/checkbox"
    )


    #inicia trace viewer
    context.tracing.start(screenshots=True, snapshots=True,sources=True)
    page = context.new_page()
    page.goto("http://www.google.com")

    
    page.set_default_timeout(5000)
    page.mouse.wheel(0,400)
    time.sleep(2)

    
    F = FuncionesGlobales(page)
    F.validar_titulo_pagina("google")
    F.Espera(4)

    context.close()
    browser.close()
    




def test_carga_textos(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(
        viewport={"width":1500, "height":800},
        #record_video_dir="videos/checkbox"
    )


    #inicia trace viewer
    context.tracing.start(screenshots=True, snapshots=True,sources=True)
    page = context.new_page()
    page.goto("http://www.google.com")

    
    page.set_default_timeout(5000)
    page.mouse.wheel(0,400)
    time.sleep(2)

    
    F = FuncionesGlobales(page)
    F.validar_titulo_pagina("google")
    F.Espera(4)

    context.close()
    browser.close()


def test_checkbox(playwright: Playwright) -> None:
    page = set_up
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(
        viewport={"width":1500, "height":800},
        #record_video_dir="videos/checkbox"
    )


    #inicia trace viewer
    context.tracing.start(screenshots=True, snapshots=True,sources=True)
    page = context.new_page()
    page.goto("http://www.google.com")

    
    page.set_default_timeout(5000)
    page.mouse.wheel(0,400)
    time.sleep(2)

    
    F = FuncionesGlobales(page)
    F.validar_titulo_pagina("google")
    F.Espera(4)

    context.close()
    browser.close()
    

