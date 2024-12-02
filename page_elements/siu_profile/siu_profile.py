from selenium.webdriver.common.by import By
import selenium
import time



class SiuProfile:
    
    def __init__(self, driver):
        self.driver = driver

    def obtener_valor_texto_perfil(self, texto):
        print(texto)
        texto_tipo = self.driver.find_element(By.XPATH, f"//span[contains(@id, {texto}) and contains(@id, 'CPH')]").text
        print(texto_tipo)
        return texto_tipo
    
    def click_boton_link(self, tipo):
        self.driver.find_element(By.XPATH, f"//div[contains(@class, 'col-6')]//child::u//following-sibling::span//child::input[contains(@name, {tipo})]").click()