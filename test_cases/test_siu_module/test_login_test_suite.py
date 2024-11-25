# Incluir acá los test cases para el módulo específico.
import pytest
from selenium import webdriver
from page_elements.siu_login.login_module import SiuLogin
import time
from selenium.webdriver.common.by import By
class TestSiuLogin:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://enlace.univalle.edu/san/webform/PAutenticar.aspx")
        time.sleep(2)

    def teardown_method(self):
        self.driver.quit()
        print("Testing finished")
    
    def test_siu_login_entry_user_and_captcha(self):
        expected = 'Bienvenido QSS2026503'
        page = SiuLogin(self.driver)
        page.escribir_nombre_usuario("qss2026503")
        time.sleep(5)
        #page.resolver_captcha()
        page.boton_click_enviar()

        time.sleep(5)
        
        text = self.driver.find_element(By.XPATH,'//div[@class = "col"]//child::span[contains(@id, "Usuario")]').text
        assert text == expected, f"FAIL: Current:{text}, Expected: {expected}"
    
    def test_siu_login_invalid_user_and_captcha(self):
        expected = 'Bienvenido QSS2026503'
        page = SiuLogin(self.driver)
        page.escribir_nombre_usuario("1283941")
        page.escribir_captcha("asjdioaj")
        time.sleep(5)
        #page.resolver_captcha()
        page.boton_click_enviar()

        time.sleep(5)
        
        text = self.driver.find_element(By.XPATH,'//div[@class = "col"]//child::span[contains(@id, "Usuario")]').text
        assert text != expected, f"FAIL: Current:{text}, Expected: {expected}"
    
    def test_siu_login_incorrect_captcha_text(self):
        expected = True

        page = SiuLogin(self.driver)
        page.escribir_nombre_usuario("QSS2026503")
        page.escribir_captcha("ASDHJKF")
        time.sleep(5)
        page.boton_click_enviar()

        time.sleep(3)
        actual = self.driver.find_element(By.XPATH, '//div[contains(@class, "col-12")]//child::div[contains(@id, "captcha")]//child::span[contains(@id, "Captcha")]').is_displayed()

        assert actual == expected, f"FAIL: Current:{actual}, Expected: {expected}"
    
    def test_siu_login_empty_user_text(self):
        expected = True
        page = SiuLogin(self.driver)
        page.escribir_nombre_usuario("")
        page.escribir_captcha("ASDHJKF")
        time.sleep(5)
        page.boton_click_enviar()
        time.sleep(5)
        actual = self.driver.find_element(By.XPATH, '//div[contains(@class, "col-12")]//child::span[contains(@id, "Cuenta") and contains(@class, "texto-error")]').is_displayed()

        assert expected == actual, f"FAIL: Current:{actual}, Expected: {expected}"

    def test_siu_login_empty_captcha_text(self):
        expected =  True

        page = SiuLogin(self.driver)
        page.escribir_nombre_usuario("qss2026503")
        time.sleep(5)
        page.boton_click_enviar()
        actual = self.driver.find_element(By.XPATH, '//div[contains(@class, "col-12")]//child::span[contains(@id, "Captcha") and contains(@class, "texto-error")]').is_displayed()
        assert expected == actual, f"FAIL: Current: {actual}, Expected:{expected}"
    

    def test_siu_login_insert_correct_pin(self):
        expected = 'BOLIVIA'
        page = SiuLogin(self.driver)
        page.escribir_nombre_usuario("qss2026503")
        time.sleep(5)
        #page.resolver_captcha()
        page.boton_click_enviar()

        time.sleep(5)

        page.boton_click_estudiante_enviar()
        time.sleep(2)

        page.escribir_pin("112898")
        time.sleep(5)

        actual = self.driver.find_element(By.XPATH,'//span[contains(@id, "Pais")]').text
        assert actual == expected, f"FAIL: Current:{actual}, Expected:{expected}"
    
    def test_siu_login_full_section(self):
        expected = 'BOLIVIA'
        page = SiuLogin(self.driver)
        page.login_completo("qss2026503", "112898")
        actual = self.driver.find_element(By.XPATH,'//span[contains(@id, "Pais")]').text
        assert actual == expected, f"FAIL: Current:{actual}, Expected:{expected}"



