from selenium.webdriver.common.by import By
from selenium import webdriver
import requests
from io import BytesIO
from PIL import Image, ImageFilter,ImageEnhance
from page_elements.siu_login.login_module import SiuLogin
import pytesseract
import time
import re
import os

class SiuScores:
    def __init__(self, driver, usuario, pin):
        self.driver = driver
        self.usuario = usuario
        self.pin = pin
        self.desplegable_gestion = (By.XPATH, "//select");
        self.table = (By.XPATH, "//table");
        self.seccion_A = (By.XPATH, '//input[@id = "Menu_btnA"]')
        self.seccion_notas = (By.XPATH, '//a[text()="Notas" and contains(@class, "texto-12")]')
        self.titulo = (By.XPATH, '//span[contains(text(), "Bole")]')
        self.opciones = (By.XPATH, '//option')
        self.mensaje_error = (By.XPATH, '//div[contains(@class, "alert")]//span[@class="message"]')
        self.titulo_error = (By.XPATH, '//div[contains(@class, "alert")]//span[@class="title"]')
        self.seccion_error = (By.XPATH, '//div[contains(@class, "alert")]//span')
        
    def realizar_login(self):
        login = SiuLogin(self.driver)
        login.login_completo(self.usuario, self.pin)
    
    def ingresar_seccion_notas(self):
        self.realizar_login()
        self.click_seccion_A()
        self.click_seccion_notas()
    
    def ingresar_seccion_A(self):
        self.realizar_login()
        self.click_seccion_A()

    def revisar_seccion_notas(self):
        return self.driver.find_elements(*self.seccion_notas)

    def revisar_error_gestiones(self):
        return self.driver.find_elements(*self.seccion_error)
    
    def generar_gestion(self, gestion):
        return (By.XPATH, f"//option[@value='${gestion}']")
    
    def select_option_gestion(self, gestion):
        self.driver.find_element(self.generar_gestion(gestion)).click()
        
    def click_seccion_A(self):
        self.driver.find_element(*self.seccion_A).click()
        time.sleep(5)
    
    def click_seccion_notas(self):
        self.driver.find_element(*self.seccion_notas).click()
    
    def obtener_titulo(self):
        return self.driver.find_element(*self.titulo).text
    
    def obtener_opciones(self):
        return self.driver.find_elements(*self.opciones)
    
    def obtener_titulo_error(self):
        return self.driver.find_element(*self.titulo_error)
    
    def obtener_mensaje_error(self):
        return self.driver.find_element(*self.mensaje_error)
    
    


    
