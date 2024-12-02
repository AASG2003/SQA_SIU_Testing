# Aquí se incluirán los pasos específicos o comunes para poder interactuar con los elementos de la página

from selenium.webdriver.common.by import By
from PIL import Image,ImageEnhance
import pytesseract
import time
import re
import os

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

    def resolver_modulo_captcha(self, texto):
        max_retries = 20
        attempts = 0
        while attempts <= max_retries:
            self.escribir_nombre_usuario(texto)
            time.sleep(1)
            captcha_element = self.driver.find_element(By.ID, "CPHBody_imgCaptcha")
            captcha_screenshot = captcha_element.screenshot_as_png
            with open("captcha.png", "wb") as file:
                file.write(captcha_screenshot)
            captcha_image = self.preprocess_image("captcha.png")
            pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
            custom_config = r'--oem 3 --psm 6'
            captcha_text = pytesseract.image_to_string(captcha_image, config=custom_config)
            print("Texto del CAPTCHA:", captcha_text)

            clean_text = re.sub(r'[^a-zA-Z0-9]', '', captcha_text)
            print("Texto limpio del CAPTCHA:", clean_text)

            self.driver.find_element(By.XPATH, "//input[@id='CPHBody_txbCaptcha']").send_keys(clean_text)
            self.driver.find_element(By.XPATH, "//input[@id='CPHBody_lbtnIngresar']").click()
            time.sleep(1)

            try:
                self.driver.find_element(By.XPATH, "//*[@id='CPHBody_lblCaptchaError']")
                print("Error: CAPTCHA incorrecto. Reintentando...")
                attempts += 1
                time.sleep(1)
            except:
                print("CAPTCHA ingresado correctamente.")
                os.remove("captcha.png")
                break
            os.remove("captcha.png")
    
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
        #unicamente necesita el usuario
        self.resolver_modulo_captcha(usuario)
        time.sleep(5)
        self.boton_click_estudiante_enviar()
        time.sleep(5)
        self.escribir_pin(pin)
        time.sleep(5)
            
    #Funcion para procesar la imagen
    def preprocess_image(self, image_path):
        img = Image.open(image_path)

        img_gray = img.convert('L')

        enhancer = ImageEnhance.Contrast(img_gray)
        img_enhanced = enhancer.enhance(2) 
        threshold = 150
        img_bw = img_enhanced.point(lambda p: p > threshold and 255)

        return img_bw
