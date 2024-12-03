import pytest
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time

from page_elements.siu_profile.siu_profile import SiuProfile
from page_elements.siu_login.login_module import SiuLogin
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env.test")

class TestProfile:
    
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://enlace.univalle.edu/san/webform/PAutenticar.aspx")
        self.loginmodule = SiuLogin(self.driver)
        self.loginmodule.login_completo(os.getenv("TEST_USERNAME"), os.getenv("TEST_PASSWORD"))
        time.sleep(5)
    
    def teardown_method(self):
        self.driver.quit()
        print("Test terminado")

    def test_profile_name_academy_unit(self):
        expected = "La Paz"
        self.profile_page = SiuProfile(self.driver)

        time.sleep(5)
        actual = self.profile_page.obtener_valor_texto_perfil('Unidad')
        time.sleep(2)

        assert expected == actual, f"FAIL: expected: {expected}, actual:{actual}"

    def test_profile_career(self):
        expected = "ING. DE SISTEMAS INFORMATICOS"
        self.profile_page = SiuProfile(self.driver)
        time.sleep(5)
        actual = self.profile_page.obtener_valor_texto_perfil('Carr')
        time.sleep(2)

        assert expected == actual, f"FAIL: expected: {expected}, actual:{actual}"

    def test_profile_mail_university(self):
        expected = "QSS2026503@est.univalle.edu"
        self.profile_page = SiuProfile(self.driver)
        time.sleep(5)
        actual = self.profile_page.obtener_correo_institucional()
        time.sleep(2)

        assert expected == actual, f"FAIL: expected: {expected}, actual:{actual}"
    
    def test_profile_mail_self(self):
        expected = "sergioantonioqui@gmail.com"
        self.profile_page = SiuProfile(self.driver)
        time.sleep(5)
        actual = self.profile_page.obtener_correo_propio()
        time.sleep(2)

        assert expected == actual, f"FAIL: expected: {expected}, actual:{actual}"

    def test_map_university_is_redirects(self):
        expected = self.driver.current_url
        self.profile_page = SiuProfile(self.driver)
        time.sleep(6)
        
        actual = self.profile_page.obtener_nuevo_link("Unidad")
        assert expected != actual, f"Fail: Expected: {expected}, actual: {actual}"
    
    def test_map_live_is_redirects(self):
        expected = self.driver.current_url
        self.profile_page = SiuProfile(self.driver)
        time.sleep(6)
        actual = self.profile_page.obtener_nuevo_link("Ubicacion")

        assert expected != actual, f"Fail: Expected: {expected}, actual: {actual}"
    

    def test_self_mail_button_redirects(self):
        expected = self.driver.current_url
        self.profile_page = SiuProfile(self.driver)
        time.sleep(6)
        
        actual = self.profile_page.obtener_nuevo_link("CorreoDato")

        assert expected != actual, f"Fail: Expected: {expected}, actual: {actual}"
    
    def test_academy_mail_is_redirects(self):
        expected = self.driver.current_url
        self.profile_page = SiuProfile(self.driver)
        time.sleep(6)
        
        actual = self.profile_page.obtener_nuevo_link("CorreoLink")
        assert expected != actual, f"Fail: Expected: {expected}, actual: {actual}"