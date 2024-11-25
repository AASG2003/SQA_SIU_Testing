# Aquí se incluirán los pasos específicos o comunes para poder interactuar con los elementos de la página

from selenium.webdriver.common.by import By
from selenium import webdriver
import requests
from io import BytesIO
from PIL import Image, ImageFilter,ImageEnhance
import pytesseract
import time

class SiuLogin:
    def __init__(self, driver):
        self.driver = driver
        self.boton_enviar = (By.XPATH, '//div[@class="row justify-content-center"]//descendant::div[@class = "col-12"]//child::input[@type="submit"]')
        self.ingresar_usuario = (By.XPATH, '//div[@class = "row justify-content-center"]//child::div[contains(@class, "input")]//child::input[@type = "text"]')
        self.ingresar_captcha = (By.XPATH, '//div[contains(@class, "input-group") and contains(@class, "mb-3")]//child::input[contains(@id, "Captch")]')
        self.imagen_captcha = (By.XPATH, '//div[contains(@class, "input-group") and contains(@class, "mb-3")]//img')
        self.boton_estudiante = (By.XPATH, '//div[contains(@class, "container-fluid")]//child::input[@type="submit"]')
        self.boton_enviar_pin = (By.XPATH, '//div[@class = "col"]//child::input[@type="submit" and contains(@name, "Valid")]')

    def boton_click_enviar(self):
        self.driver.find_element(*self.boton_enviar).click()

    def escribir_nombre_usuario(self, usuario):
        self.driver.find_element(*self.ingresar_usuario).send_keys(usuario)

    def escribir_captcha(self, texto):
        self.driver.find_element(*self.ingresar_captcha).send_keys(texto)
    
    def boton_click_estudiante_enviar(self):
        self.driver.find_element(*self.boton_estudiante).click()

    

    #Talvez no se llegue a utilizar
    def resolver_captcha(self):
        captcha_element = self.driver.find_element(*self.imagen_captcha)
        captcha_url = captcha_element.get_attribute('src')
        response = requests.get(captcha_url)
        img = Image.open(BytesIO(response.content))
        img = img.convert('L')
        img = img.filter(ImageFilter.MedianFilter(3))
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(2)
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        texto_captcha = pytesseract.image_to_string(img, config='--oem 3 --psm 6')

        texto_captcha = texto_captcha.strip()
        print(texto_captcha)
        self.escribir_captcha(texto_captcha)
    
    def escribir_pin(self, pin):
        name_att = self.driver.find_element(By.XPATH, "//input[@type = 'password']").get_attribute('name')
        for i in range(0, 6):
            pin_position = name_att.replace("1", str(i + 1))
            print(pin_position)
            self.driver.find_element(By.XPATH, f'//input[contains(@name, "{pin_position}")]').send_keys(pin[i])
            print(pin[i])
            time.sleep(2)
        
        time.sleep(2)
        self.driver.find_element(*self.boton_enviar_pin).click()

    def login_completo(self, usuario, pin):
        self.escribir_nombre_usuario(usuario)
        #tiempo para poder ingresar el pin correcto
        time.sleep(15)
        self.boton_click_enviar()
        time.sleep(5)
        self.boton_click_estudiante_enviar()
        time.sleep(5)
        self.escribir_pin(pin)
        time.sleep(5)
            
