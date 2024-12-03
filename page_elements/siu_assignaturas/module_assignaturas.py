# Aquí se incluirán los pasos específicos o comunes para poder interactuar con los elementos de la página
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image, ImageEnhance
import pytesseract
import time
import re
import os

class Atestear:
    def __init__(self, driver):
        self.driver = driver
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    def preprocess_image(self, image_path):
        # Cargar la imagen
        img = Image.open(image_path)
        # Convertir la imagen a escala de grises
        img_gray = img.convert('L')
        # Mejorar el contraste (opcional)
        enhancer = ImageEnhance.Contrast(img_gray)
        img_enhanced = enhancer.enhance(2)
        # Convertir la imagen en blanco y negro (umbralización)
        threshold = 150
        img_bw = img_enhanced.point(lambda p: p > threshold and 255)
        return img_bw
    
    def verify_login(self):
            #Intentos para resolver CAPTCHA
            max_retries = 50
            attempts = 0
            captcha_solved = False
            while attempts < max_retries and not captcha_solved:
                self.fill_form("//input[@maxlength='15']", "CAJ2026045")
                time.sleep(3)
                try:
                    captcha_text = self.solve_captcha("CPHBody_imgCaptcha", "//input[@id='CPHBody_txbCaptcha']")
                    self.click_element("//input[@id='CPHBody_lbtnIngresar']")
                    time.sleep(1)
                    # Verificar si hay error
                    self.driver.find_element(By.XPATH, "//*[@id='CPHBody_lblCaptchaError']")
                    print(f"Error: CAPTCHA incorrecto. Reintentando... ({captcha_text})")
                    attempts += 1
                except:
                    print("CAPTCHA ingresado correctamente.")
                    captcha_solved = True
            # Validar PIN
            self.driver.find_element(By.XPATH, "//*[@id='CPHBody_RolRepeater_btnRol_0']").click()
            time.sleep(3)
            pin = "123640"
            for idx, digit in enumerate(pin, start=1):
                self.fill_form(f"//input[@id='CPHBody_txbDigito{idx}']", digit)
            time.sleep(3)
            self.click_element("//input[@id='CPHBody_lkbValidatePin']")
            time.sleep(5)

    def solve_captcha(self, captcha_xpath, captcha_field_xpath):
            captcha_element = self.driver.find_element(By.ID, captcha_xpath)
            # Capturar el CAPTCHA como imagen
            captcha_screenshot = captcha_element.screenshot_as_png
            with open("captcha.png", "wb") as file:
                file.write(captcha_screenshot)
            captcha_image = self.preprocess_image("captcha.png")
            custom_config = r'--oem 3 --psm 6'
            captcha_text = pytesseract.image_to_string(captcha_image, config=custom_config)

            clean_text = re.sub(r'[^a-zA-Z0-9]', '', captcha_text)
            self.driver.find_element(By.XPATH, captcha_field_xpath).send_keys(clean_text)
            os.remove("captcha.png")
            return clean_text

    def open_url(self, url):
        self.driver.get(url)

    def fill_form(self, field_xpath, value):
        self.driver.find_element(By.XPATH, field_xpath).send_keys(value)

    def click_element(self, element_xpath):
        self.driver.find_element(By.XPATH, element_xpath).click()

    def get_text(self, element_xpath):
        return self.driver.find_element(By.XPATH, element_xpath).text
    
    def get_element(self, element_xpath):
        self.driver.find_element(By.XPATH, element_xpath)
    
    def entrar_asignaturas(self):
        self.click_element("//*[@id='Menu_btnM']")
        time.sleep(1)
        self.click_element("//*[@id='Menu_MenuRepeater_btn_0']")   
