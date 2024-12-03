from selenium.webdriver.common.by import By
import selenium
import time
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env.test")

class SiuProfile:
    
    def __init__(self, driver):
        self.driver = driver
        self.user = os.getenv("TEST_USERNAME")
        self.password = os.getenv("TEST_PASSWORD")
        self.correo_propio = (By.XPATH, "//span[@id = 'CPHBody_lblCorreoDatos']")
        self.correo_institucional = (By.XPATH, "//span[@id = 'CPHBody_lblCorreo']")

    def obtener_valor_texto_perfil(self, texto):
        print(texto)
        texto_tipo = self.driver.find_element(By.XPATH, f"//span[contains(@id, '{texto}') and contains(@id, 'CPH')]").text
        print(texto_tipo)
        return texto_tipo
    
    def obtener_correo_propio(self):
        return self.driver.find_element(*self.correo_propio).text
    
    def obtener_correo_institucional(self):
        return self.driver.find_element(*self.correo_institucional).text

    def click_boton_link(self, tipo):
        self.driver.find_element(By.XPATH, f"//div[contains(@class, 'col-6')]//child::u//following-sibling::span//child::input[contains(@name, '{tipo}')]").click()
    
    def obtener_nuevo_link(self, tipo):
        print(tipo)
        self.click_boton_link(tipo)
        time.sleep(6)

        actual_window = self.driver.current_window_handle
        for window in self.driver.window_handles:
            if window != actual_window:
                self.driver.switch_to.window(window)
                break
        nuevo_url = self.driver.current_url
        self.driver.close()
        self.driver.switch_to.window(actual_window)
        return nuevo_url
