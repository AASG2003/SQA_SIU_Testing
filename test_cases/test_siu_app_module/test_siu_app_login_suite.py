import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
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
        self.app = SiuApp(self.driver)
        time.sleep(5)
        
    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def test_username_is_write(self):
        actual = self.app.obtener_longitud_usuario()
        print(actual)

        assert len(actual) > 0 and actual is not "USUARIO", "Fail: username is empty"
    
    def test_login_is_redirect(self):
        self.app.iniciar_sesion()
        expected = "Univalle"
        time.sleep(6)
        actual = self.driver.find_element(AppiumBy.XPATH, '//android.widget.LinearLayout[@resource-id="edu.univalle.siumovil:id/navigationlayout_appbar"]/android.view.ViewGroup/android.widget.TextView[1]').text
        time.sleep(2)
        assert expected == actual, f"FAIL: Expected:{expected}, actual:{actual}"
    
    def test_login_recovery_account(self):
        expected = "Recuperar Cuenta y PIN"
        self.app.recupera_cuenta_click()
        time.sleep(3)
        actual = self.driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[1]').text

        assert expected == actual, f"FAIL: Exp:{expected}, ac:{actual}"
    
    def test_login_unlock_account(self):
        expected = 'Desbloquear Cuenta'
        self.app.desbloquea_cuenta_click()
        time.sleep(3)
        actual = self.driver.find_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[1]').text
        
        assert expected == actual, f"FAIL: Exp{expected}, Act: {actual}"

    def test_password_is_write(self):
        expected = True

        valor_actual = self.app.obtener_valor_default_password()
        time.sleep(2)

        self.app.ingresar_contrasena(f"{os.getenv("TEST_PASSWORD")}")
        time.sleep(2)
        nuevo_valor = self.driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="edu.univalle.siumovil:id/navigationlayout_content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.widget.EditText[1]').get_attribute('text')

        print(nuevo_valor)
        actual = valor_actual != nuevo_valor

        assert actual == expected, f"FAIL: Exp: {expected}, act: {actual}"
    
    def test_message_empty_pin(self):
        expected = "Debe ingresar un pin de usuario"
        self.app.ingresar_usuario("asdjio")
        time.sleep(1)
        self.app.click_boton_iniciar_sesion()
        time.sleep(2)
        actual = self.app.obtener_texto_warning()

        assert expected == actual, f"FAIL: Exp:{expected}, actu:{actual}"
    
    def test_message_user_empty(self):
        expected = "Debe ingresar una cuenta de usuario"

        self.app.ingresar_contrasena("12234")
        time.sleep(1)
        self.app.click_boton_iniciar_sesion()
        time.sleep(2)

        actual = self.app.obtener_texto_warning()

        assert expected == actual, f"FAIL: Exp:{expected}, actu:{actual}"
    
    def test_empty_country_and_cellphone_popup(self):
        expected = "Ingrese el código de país y el teléfono."
        self.app.recupera_cuenta_click()
        time.sleep(1)
        self.app.click_boton_solicitar()
        time.sleep(2)
        actual = self.app.obtener_texto_warning()

        assert expected == actual, f"FAIL: Exp{expected}, act:{actual}"