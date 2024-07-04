import re
import random
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from Estudiantes.Ejemplos.funciones import FuncionesGlobales

# pytest sesion2.py -s -v
# pytest sesion2.py -s -v --browser-channel=chrome -n 4
#el anterior comando manda a ejecutar cuatro navagadores en paralelo


#varibales globales
tiempo = 0.9
ruta = "Estudiantes/Ejemplos/imagenes"
pdf1 = "Estudiantes/Ejemplos/pdf"



def test_sesion1(set_up)->None:
    page = set_up
    F  = FuncionesGlobales(page)
    F.validar_titulo_pagina("Swag Labs", tiempo)

    
def test_sesion2(set_up_session_2)->None:
    page = set_up_session_2
    F  = FuncionesGlobales(page)
    F.click_normal("(//button[contains(.,'ADD TO CART')])[1]", tiempo)
    F.Espera(2)
    