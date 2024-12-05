from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import os

load_dotenv(dotenv_path=".env.test")

class SiuAppProfile:
    def __init__(self, driver):
        self.driver = driver
        self.user = os.getenv("TEST_USERNAME")
        self.password = os.getenv("TEST_PASSWORD")
        self.barside = (AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Abrir panel de navegación"]')
        self.logout_button = (AppiumBy.XPATH, '//android.widget.TextView[@text="Cerrar sesión"]')
        self.warning_logout = (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout')
        self.boton_opcion_si_box = (AppiumBy.XPATH, '//android.widget.Button[@resource-id="android:id/button1"]')
        self.boton_opciones = (AppiumBy.XPATH, '//androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup[2]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup')
        self.titulo_modulo = (AppiumBy.XPATH, '//android.widget.LinearLayout[@resource-id="edu.univalle.siumovil:id/navigationlayout_appbar"]/android.view.ViewGroup/android.widget.TextView[1]')

        self.tipo_tema ='(//android.widget.FrameLayout[@resource-id="edu.univalle.siumovil:id/nav_host"])[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/'

        self.switch = (AppiumBy.XPATH, '//android.widget.Switch')
        self.boton_atras = (AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Atrás"]')
        self.calendario = (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup')
    
    def click_panel(self):
        self.driver.find_element(*self.barside).click()

    def click_cerrar_sesion(self):
        self.driver.find_element(*self.logout_button).click()
    
    def click_aceptar_cerrar_sesion(self):
        self.driver.find_element(*self.boton_opcion_si_box).click()

    def click_boton_opciones(self):
        self.driver.find_element(*self.boton_opciones).click()
        
    def obtener_aviso_cerrar_sesion(self):
        return self.driver.find_element(*self.warning_logout).is_displayed()
    
    def tema_clickeado(self, texto):
        return self.driver.find_element(AppiumBy.XPATH, f'//android.widget.RadioButton[@text="{texto}"]').get_attribute("checked")

    def click_tema_claro(self):
        #(//android.widget.FrameLayout[@resource-id="edu.univalle.siumovil:id/nav_host"])[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.RadioButton[1]
        new_path = ''.join((self.tipo_tema,"android.widget.RadioButton[1]"))
        self.driver.find_element(AppiumBy.XPATH, f'{self.tipo_tema}android.view.ViewGroup[1]/android.widget.RadioButton[1]').click()
    
    def click_tema_oscuro(self):
        self.driver.find_element(AppiumBy.XPATH,f'{self.tipo_tema}android.view.ViewGroup[2]/android.widget.RadioButton[1]').click()
    
    def click_tema_sistema(self):
        self.driver.find_element(AppiumBy.XPATH,f'{self.tipo_tema}android.view.ViewGroup[3]/android.widget.RadioButton[1]').click()
    
    def click_boton_atras(self):
        self.driver.find_element(*self.boton_atras).click()
    
    def click_switch_calendario(self):
        self.driver.find_element(*self.switch).click()
    
    def calendario_es_visible(self):
        return self.driver.find_element(*self.calendario).is_displayed()
