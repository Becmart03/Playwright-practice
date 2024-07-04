import re
import random
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from Estudiantes.Ejemplos.funciones import FuncionesGlobales

# pytest sesion2.py -s -v

#varibales globales
tiempo = 0.9
ruta = "Estudiantes/Ejemplos/imagenes"
pdf1 = "Estudiantes/Ejemplos/pdf"


def test_sesion(set_up)->None:
    page = set_up
    F  = FuncionesGlobales(page)
    F.validar_titulo_pagina("Swag Labs", tiempo)


def test_sesion2(set_up)->None:
    page = set_up
    F  = FuncionesGlobales(page)
    F.click_normal("//input[contains(@type,'text')]", tiempo)
    F.texto("//input[contains(@type,'text')]", "standard_user",5)
    F.click_normal("//input[contains(@type,'password')]", tiempo)
    F.texto("//input[contains(@type,'password')]", "secret_sauce")
    F.click_normal("//input[contains(@type,'submit')]", tiempo)
    