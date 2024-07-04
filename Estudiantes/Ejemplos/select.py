import re
import time
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from funciones import funcionesGlobales


def test_select1(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(
        viewport={"width":1500, "height":800},
        #record_video_dir="videos/checkbox"
    )

    page = context.new_page()
    page.goto("")

    
    page.set_default_timeout(5000)
    page.mouse.wheel(0,400)
    time.sleep(2)

    
    F = funcionesGlobales(page)
    F.validar_titulo_pagina("titulo de la pagina")
    F.Espera(4)


    #nombre
    F.texto("pongo el selector 1 aca")
    F.texto("pongo el selector 2 aca")
    F.texto("pongo el selector 3 aca")
    F.texto("pongo el selector 4 aca")
    F.texto_img("pongo el selector 4 aca", "RUTA imagen","timepo" )


    #checkbox
    F.click("selector","rutaelementoscreenshot", tiempo=6)


    #combobox
    F.combo_value("selector","linux","screenshot ruta", tiempo=6)

    F.combo_label("selector","etiqueta","screenshot ruta", tiempo=6)


    #submit
    F.click("selector", tiempo=4)

    #validar url
    F.validar_url("url", "tiempo")


    #validar texto
    F.validar_texto("selector aqui", "texto", "timepo")

    context.close()
    browser.close()
