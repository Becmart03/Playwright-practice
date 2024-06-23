
from playwright.sync_api import Playwright
from Estudiantes.Ejemplos.funciones3 import Funciones_Globales
#el problema que tenia al importar libreria es que la carpeta Playwright es la mas externa, toca entrar a varias

#correr  playwright show-trace trace.zip
#lanzando el debud
#set PWDEBUG=1
#pytest Debug.py -s
#poner en el codigo
#page.pause()
#cuando se setea ese modo debug siempre va a netrar a ese modo, asi que cuidado
#la manera de quitarlo es 
#set PWDEBUG=0


tiempo = 3


def test_lista_dinamica(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(
        viewport={"width":1500, "height":800},
        #record_video_dir="videos/checkbox"
    )
    page = context.new_page()
    page.goto("http://www.google.com")
    F=Funciones_Globales(page)
    F.Espera(3)

    context.close()
    browser.close()


#volver a mirar la parte del trace viwver