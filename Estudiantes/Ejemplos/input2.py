import re
import time
from playwright.sync_api import Page, expect, Playwright, sync_playwright


def test_input2(page: Page):
    page.goto("http://www.testingqarvn.com.es/datos-personales/")
    expect(page).to_have_title("Datos Personales  | TestingQaRvn")


    page.locator("locator1").fill("Rodrigo")
    page.locator("locator2").fill("Apellido")
    page.locator("locator3").fill("Correo")
    page.locator("locator4").fill("telefono")
    page.locator("locator5").fill("direccioj")
    page.locator("locator6").click()
    