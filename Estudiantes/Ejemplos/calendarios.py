import re
import time
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from funciones import funcionesGlobales
import random


ruta = "imagenes/calendarios"

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
    F.texto("pongo el selector 1 aca","tiempo")
    F.texto("pongo el selector 2 aca")
    F.texto("pongo el selector 3 aca","tiempo")
    F.texto("pongo el selector 4 aca","tiempo")
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

    #calendario, lo recomendable s asignar el valor en el navegador y copiarlo, hay que usar una funcion de click que es muy util
    F.combo_label("selector","etiqueta","screenshot ruta", tiempo=6)
    #revaliosisimo para "perder el foco"
    page.mouse.click(0, 50)  # cooordenadas x,y
    #tambien sirve para seguir al proximo elemento
    page.keyboard.press("Tab")
    #muchas veces los calendarios no permiten escribir directamente, podemos mandar directamente el click
    F.click("xpath del elemento de calendario aqui",tiempo=5)
    F.click("xpath del elemento dentro del calendario aqui",tiempo=5)


    #metodo random
    numA = random.sample(range(1,4),1)
    F.combo_label("selector","etiqueta","screenshot ruta", tiempo=6)

    if numA[0] == 1:
        F.combo_label("selector","Debian","screenshot ruta", tiempo=6)
    if numA[0] == 1:
        F.combo_label("selector","Linux","screenshot ruta", tiempo=6)
    if numA[0] == 1:
        F.combo_label("selector","RedHat","screenshot ruta", tiempo=6)
    

    context.close()
    browser.close()
