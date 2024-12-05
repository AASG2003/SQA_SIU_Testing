import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from page_elements.siu_app_profile_module.siu_app_profile_module import SiuAppProfile
from page_elements.siu_app_login_module.siu_app_login_module import SiuApp
from dotenv import load_dotenv
import pytest
import time
import os

load_dotenv(dotenv_path=".env.test")

options = UiAutomator2Options()
options.platform_version = os.getenv("TEST_APP_DEVICE_VERSION")
options.platform_name = os.getenv("TEST_APP_DEVICE_PLATFORM")
options.device_name = os.getenv("TEST_APP_DEVICE_NAME")
options.app_package = "edu.univalle.siumovil"
options.app_activity = "crc6479014e7916869f4b.MainActivity"
options.no_reset = False

appium_server_url = 'http://127.0.0.1:4723'

class TestApp(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(command_executor=appium_server_url, options=options)
        self.app = SiuAppProfile(self.driver)
        self.login = SiuApp(self.driver)
        time.sleep(5)
        
    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def test_press_logout(self):
        expected = "Bienvenid@s"
        self.login.iniciar_sesion()
        time.sleep(3)
        self.app.click_panel()
        time.sleep(3)
        self.app.click_cerrar_sesion()
        time.sleep(3)
        self.app.click_aceptar_cerrar_sesion()
        time.sleep(3)
        actual = self.driver.find_element(*self.login.titulo).text

        assert actual == expected, f"FAIL: Exp{expected}, act: {actual}"


    def test_warning_logout_is_displayed(self):
        expected = True
        self.login.iniciar_sesion()
        time.sleep(5)
        self.app.click_panel()
        time.sleep(3)
        self.app.click_cerrar_sesion()
        time.sleep(3)

        actual = self.app.obtener_aviso_cerrar_sesion()

        assert expected == actual, f"FAIL: Expected:{expected}, Actual:{actual}"

    def test_light_theme_is_checked(self):
        expected = "true"
        self.login.iniciar_sesion()
        time.sleep(5)
        self.app.click_panel()
        time.sleep(3)
        self.app.click_boton_opciones()
        time.sleep(3)
        self.app.click_tema_claro()
        time.sleep(2)
        actual = self.app.tema_clickeado("Claro")
        assert expected == actual, f"FAIL: Exp: {expected}, act: {actual}"
        
    def test_dark_theme_is_checked(self):
        expected = "true"
        self.login.iniciar_sesion()
        time.sleep(5)
        self.app.click_panel()
        time.sleep(3)
        self.app.click_boton_opciones()
        time.sleep(3)
        self.app.click_tema_oscuro()
        time.sleep(2)
        actual = self.app.tema_clickeado("Oscuro")
        assert expected == actual, f"FAIL: Exp: {expected}, act: {actual}"

    def test_system_theme_is_checked(self):
        expected = "true"
        self.login.iniciar_sesion()
        time.sleep(5)
        self.app.click_panel()
        time.sleep(3)
        self.app.click_boton_opciones()
        time.sleep(3)
        self.app.click_tema_sistema()
        time.sleep(2)
        actual = self.app.tema_clickeado("Sistema")
        assert expected == actual, f"FAIL: Exp: {expected}, act: {actual}"
    
    def test_calendary_is_deployed(self):
        expected = True
        self.login.iniciar_sesion()
        time.sleep(3)
        self.app.click_panel()
        time.sleep(3)
        self.app.click_boton_opciones()
        time.sleep(3)
        self.app.click_switch_calendario()
        time.sleep(3)
        self.app.click_boton_atras()
        time.sleep(3)
        actual = self.app.calendario_es_visible()

        assert expected == actual, f"FAIL: Exp: {expected}, act: {actual}"