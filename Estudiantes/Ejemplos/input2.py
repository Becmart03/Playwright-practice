import re
import time
from playwright.sync_api import Page, expect, Playwright, sync_playwright


def test_input2(page: Page):
    page.goto("http://www.testingqarvn.com.es/datos-personales/")
    expect(page).to_have_title("Datos Personales  | TestingQaRvn")


    #tiempo de espera de 3 segundos
    page.set_default_timeout(3000)


    #asserts o validadores, espera que el elemento sea visible
    apellidos = page.locator("elemento")
    #visible
    expect(apellidos).to_be_visible()
    #Enabled
    expect(apellidos).to_be_enabled()
    #validador que se asegura que tiene que estar vacio
    expect(apellidos).to_be_empty()
    #Validador que tenga un id en especifico
    expect(apellidos).to_have_id("nombre del id")
    #valida que tenga una url
    expect(page).to_have_url()




    page.locator("locator1").fill("Rodrigo")
    page.locator("locator2").fill("Apellido")
    page.locator("locator3").fill("Correo")
    page.locator("locator4").fill("telefono")
    page.locator("locator5").fill("direccioj")
    page.locator("locator6").click()
    #timepo forzado de 30 segundos
    time.sleep(30)


#paara generar un context
def test_input2(playwright: Playwright) ->None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    #cambiar el tamaño de las paginas
    context = browser.new_context(
        viewport={'width':1500, 'height':800}
    )
    #para grabar video
    folder = "imagenes"
    context = browser.new_context(record_video_dir=folder)
    page = context.new_page()

    page.goto("")
    #sino tengo el browser para ponerle el tamaño, puedo definirlo en la pagina
    page.set_viewport_size({'width':1500, 'height':800})
    expect(page).to_have_title("")
    
