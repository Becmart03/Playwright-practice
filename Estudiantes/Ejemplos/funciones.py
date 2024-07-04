import re
import time
from playwright.sync_api import Page, expect, Playwright, sync_playwright


class FuncionesGlobales:

    def __init__(self,page):
        self.page = page


    def Espera(self, tiempo=2):
        time.sleep(tiempo)

    
    def scroll_xy(self, x, y, tiempo=5):
        self.page.mouse.wheel(x,y)
        time.sleep(tiempo)


    def texto(self, selector, texto, tiempo=5):
        t = self.page.locator(selector)
        expect(t).to_be_visible()
        expect(t).to_be_enabled()
        expect(t).to_be_empty()
        t.highlight()
        t.fill(texto)
        time.sleep(tiempo)


    def texto_img(self, selector, texto, img="ruta de imagen", tiempo=5):
        t = self.page.locator(selector)
        expect(t).to_be_visible()
        expect(t).to_be_enabled()
        expect(t).to_be_empty()
        t.highlight()
        t.fill(texto)
        self.page.screenshot(path=img)
        time.sleep(tiempo)


    def click(self, selector,img, tiempo=5):
        """para validar checkbox"""
        t = self.page.locator(selector)
        expect(t).to_be_visible
        expect(t).to_be_enabled
        self.page.screenshot(path=img)
        time.sleep(tiempo)

    def click_normal(self, selector, tiempo=5):
        """para validar checkbox"""
        t = self.page.locator(selector)
        expect(t).to_be_visible
        expect(t).to_be_enabled
        time.sleep(tiempo)


    def combo_value(self, selector, valor,img, tiempo=5):
        t = self.page.locator(selector)
        expect(t).to_be_visible
        expect(t).to_be_enabled
        t.highlight()
        t.select_option(valor)
        self.page.screenshot(path=img)
        time.sleep(tiempo)


    def combo_label(self, selector, label,img, tiempo=5):
        t = self.page.locator(selector)
        expect(t).to_be_visible
        expect(t).to_be_enabled
        t.highlight()
        t.select_option(label)
        self.page.screenshot(path=img)
        time.sleep(tiempo)


        
    def validar_titulo_pagina(self, titulo, tiempo=5):
        expect(self.page).to_have_title(titulo)
        time.sleep(tiempo)
    
    
    def validar_url(self, texto, tiempo=5):
        expect(self.page).to_have_url(re.compile(texto))
        time.sleep(tiempo)


    def validar_texto(self, selector, texto, tiempo=5):
        t = self.page.locator(selector)
        expect(t).to_contain_text(texto)
        time.sleep(tiempo)

    
    def upload_file(self, selector, archivo, ruta, tiempo=5):
        self.page.locator(selector).set_input_files(archivo)
        time.sleep(tiempo)
        self.page.screenshot(path=ruta)


    def upload_file_remove(self, selector, tiempo=5):
        """elimina el archivo de la carga que habiamos agregado anteriormente"""
        self.page.locator(selector).set_input_files([])
        time.sleep(tiempo)
        