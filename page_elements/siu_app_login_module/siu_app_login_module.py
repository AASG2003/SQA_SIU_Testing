from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import os

load_dotenv(dotenv_path=".env.test")

class SiuApp:
    def __init__(self, driver):
        self.driver = driver
        self.user = os.getenv("TEST_USERNAME")
        self.password = os.getenv("TEST_PASSWORD")
        self.input_usuario = (AppiumBy.XPATH, '//android.widget.EditText[@resource-id="edu.univalle.siumovil:id/radEntry"]')
        self.input_password = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="edu.univalle.siumovil:id/navigationlayout_content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.widget.EditText[1]')
        self.boton_sesion = (AppiumBy.XPATH, '//android.widget.Button[@text="Iniciar Sesión"]')
        self.recupera_cuenta_boton = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="edu.univalle.siumovil:id/navigationlayout_content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.TextView[1]')
        self.desbloquea_cuenta_boton = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="edu.univalle.siumovil:id/navigationlayout_content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.TextView[2]')
        
        self.titulo = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="edu.univalle.siumovil:id/navigationlayout_content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView[1]')

        self.warning_account_empty = (AppiumBy.XPATH, '//androidx.appcompat.widget.LinearLayoutCompat[@resource-id="edu.univalle.siumovil:id/parentPanel"]')
        self.boton_solicitar = (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]/android.widget.Button[1]')

        self.texto_warning = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="android:id/message"]')

    def obtener_longitud_usuario(self):
        self.ingresar_usuario(self.user)
        return self.driver.find_element(*self.input_usuario).text

    def obtener_valor_default_password(self):
        return self.driver.find_element(*self.input_password).text
    
    def obtener_texto_warning(self):
        return self.driver.find_element(*self.texto_warning).text

    def ingresar_usuario(self, texto):
        self.driver.find_element(*self.input_usuario).send_keys(texto)
        time.sleep(2)

    def ingresar_contrasena(self, password):
        self.driver.find_element(*self.input_password).send_keys(password)
        time.sleep(2)
    
    def usuario_vacio_desplegado(self):
        return self.driver.find_element(*self.warning_account_empty).is_displayed()

    def ingresar_usuario_contrasena(self):
        self.ingresar_usuario(self.user)
        time.sleep(2)
        self.ingresar_contrasena(self.password)
        time.sleep(2)

    def click_boton_iniciar_sesion(self):
        self.driver.find_element(*self.boton_sesion).click()
    
    def click_boton_solicitar(self):
        self.driver.find_element(*self.boton_solicitar).click()

    def iniciar_sesion(self):
        self.ingresar_usuario_contrasena()
        time.sleep(2)
        self.click_boton_iniciar_sesion()
        time.sleep(2)

    def recupera_cuenta_click(self):
        self.driver.find_element(*self.recupera_cuenta_boton).click()
    
    def desbloquea_cuenta_click(self):
        self.driver.find_element(*self.desbloquea_cuenta_boton).click()