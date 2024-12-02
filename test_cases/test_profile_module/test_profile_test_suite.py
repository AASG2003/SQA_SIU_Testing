import pytest
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time

from page_elements.siu_profile.siu_profile import SiuProfile
from page_elements.siu_login.login_module import SiuLogin

class TestProfile:
    
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://enlace.univalle.edu/san/webform/PAutenticar.aspx")
        time.sleep(5)
    
    def teardown_method(self):
        self.driver.quit()
        print("Test terminado")

    def test_profile_name_academy_unit(self):
        expected = "La Paz"
        login_page = SiuLogin(self.driver)
        self.profile_page = SiuProfile(self.driver)
        login_page.login_completo("qss2026503", "112898")

        time.sleep(5)
        actual = self.profile_page.obtener_valor_texto_perfil('Unidad')
        time.sleep(2)

        assert expected == actual, f"FAIL: expected: {expected}, actual:{actual}"

    def test_profile_career(self):
        expected = "La Paz"
        login_page = SiuLogin(self.driver)
        self.profile_page = SiuProfile(self.driver)
        login_page.login_completo("qss2026503", "112898")

        time.sleep(5)
        actual = self.profile_page.obtener_valor_texto_perfil('Carr')
        time.sleep(2)

        assert expected == actual, f"FAIL: expected: {expected}, actual:{actual}"

    def test_profile_mail(self):
        expected = "QSS2026503@est.univalle.edu"
        login_page = SiuLogin(self.driver)
        self.profile_page = SiuProfile(self.driver)
        login_page.login_completo("qss2026503", "112898")

        time.sleep(5)
        actual = self.profile_page.obtener_valor_texto_perfil('Correo')
        time.sleep(2)

        assert expected == actual, f"FAIL: expected: {expected}, actual:{actual}"
    
    def test_map_university_is_clickeable(self):
        expected = "https://www.google.com/maps/place/Universidad+Privada+del+Valle/@-16.5034557,-68.1225494,17z/data=!3m1!4b1!4m6!3m5!1s0x915f206782937445:0xacceb97486edb698!8m2!3d-16.5034609!4d-68.1199745!16s%2Fg%2F1hdzd_4wg?entry=tts"
        login_page = SiuLogin(self.driver)
        self.profile_page = SiuProfile(self.driver)
        login_page.login_completo('qss2026503', '112898')
        time.sleep(6)
        
        self.profile_page.click_boton_link("Unidad")
        time.sleep(5)

        actual_url = self.driver.current_window_handle
        for window in self.driver.window_handles:
            if window != actual_url:
                self.driver.switch_to.window(window)
                break
        actual = self.driver.current_url

        assert expected == actual, f"Fail: Expected: {expected}, actual: {actual}"
    
    def test_map_actual_location_is_clickeable(self):
        expected = "https://www.google.com/maps/place//@-16.5085184,-68.1181184,13z/data=!3m1!4b1?entry=ttu&g_ep=EgoyMDI0MTEyNC4xIKXMDSoASAFQAw%3D%3D"

        login_page = SiuLogin(self.driver)
        self.profile_page = SiuProfile(self.driver)
        login_page.login_completo('qss2026503', '112898')
        time.sleep(6)
        
        self.profile_page.click_boton_link("Unidad")
        time.sleep(5)

        actual_url = self.driver.current_window_handle
        for window in self.driver.window_handles:
            if window != actual_url:
                self.driver.switch_to.window(window)
                break
        time.sleep(2)
        actual = self.driver.current_url

        assert expected == actual, f"Fail: Expected: {expected}, actual: {actual}"
    

    def test_self_mail_button_redirects(self):
        print("entrando a test")
        expected = "https://siu.univalle.edu/WASIU/webform/PPerfilEstudianteSmart.aspx"

        login_page = SiuLogin(self.driver)
        self.profile_page = SiuProfile(self.driver)
        login_page.login_completo('qss2026503', '112898')
        time.sleep(6)
        
        self.profile_page.click_boton_link("CorreoDato")
        time.sleep(5)

        actual_url = self.driver.current_window_handle
        for window in self.driver.window_handles:
            if window != actual_url:
                self.driver.switch_to.window(window)
                break
        time.sleep(2)
        actual = self.driver.current_url
        print(actual)

        assert expected != actual, f"Fail: Expected: {expected}, actual: {actual}"
    
    def test_academy_mail_is_clickeable(self):
        expected = "https://siu.univalle.edu/WASIU/webform/PPerfilEstudianteSmart.aspx"

        login_page = SiuLogin(self.driver)
        self.profile_page = SiuProfile(self.driver)
        login_page.login_completo('qss2026503', '112898')
        time.sleep(6)
        
        self.profile_page.click_boton_link("CorreoLink")
        time.sleep(5)

        actual_url = self.driver.current_window_handle
        for window in self.driver.window_handles:
            if window != actual_url:
                self.driver.switch_to.window(window)
                break
        time.sleep(2)
        actual = self.driver.current_url

        assert expected != actual, f"Fail: Expected: {expected}, actual: {actual}"

