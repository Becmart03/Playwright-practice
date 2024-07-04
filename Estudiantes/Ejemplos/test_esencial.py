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

def test_inicio(set_up) -> None:
    page = set_up
    F = FuncionesGlobales(page)
    F.validar_titulo_pagina("titulo de pagina")
    F.scroll_xy(0,400)
    F.Espera(tiempo)


def test_carga_textos(set_up) -> None:
    page = set_up
    F = FuncionesGlobales(page)
    F.validar_titulo_pagina("google")
    F.Espera(tiempo)


def test_checkbox(set_up) -> None:
    page = set_up
    page.goto("http://www.google.com")
    page.set_default_timeout(5000)
    page.mouse.wheel(0,400)
    time.sleep(2)
    F = FuncionesGlobales(page)
    F.validar_titulo_pagina("google")
    F.Espera(4)


def test_upload(set_up):
    page = set_up
    browser = Playwright.chromium.launch(headless=False, slow_mo=tiempo)
    context = browser.new_context(
        viewport={"width":1500, "height":800}
    )
    context.trace.start(screeshots=True, snapshots=True, sources=True)
    page.context
