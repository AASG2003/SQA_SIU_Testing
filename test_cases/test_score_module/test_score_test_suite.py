import pytest
from selenium import webdriver
from page_elements.siu_scores.scores_module import SiuScores
import time
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path=".env.test")

class TestSiuScores:

    def setup_method(self):
        self.driver = webdriver.Edge()
        self.driver.maximize_window()
        self.driver.get("https://enlace.univalle.edu/san/webform/PAutenticar.aspx")
        time.sleep(2)

    def teardown_method(self):
        self.driver.quit()
        print("Testing finished")
    
    def test_scores_section(self):
        expected = 1
        Scores_page = SiuScores(self.driver, f"{os.getenv('TEST_USERNAME')}", f"{os.getenv('TEST_PASSWORD')}")
        Scores_page.ingresar_seccion_A()
        actual = len(Scores_page.revisar_seccion_notas())
        assert expected == actual, f"FAIL: expected: {expected}, actual:{actual}"
    
    def test_title_section(self):
        expected = "Boletín de calificaciones"
        Scores_page = SiuScores(self.driver, f"{os.getenv('TEST_USERNAME')}", f"{os.getenv('TEST_PASSWORD')}")
        Scores_page.ingresar_seccion_notas()
        actual = Scores_page.obtener_titulo()
        assert expected == actual, f"FAIL: expected: {expected}, actual:{actual}"

    def test_get_years(self):
        notExpected = [0, 1]
        Scores_page = SiuScores(self.driver, f"{os.getenv('TEST_USERNAME')}", f"{os.getenv('TEST_PASSWORD')}")
        Scores_page.ingresar_seccion_notas()
        actual = len(Scores_page.obtener_opciones())
        assert actual not in notExpected, f"FAIL: expected: {notExpected}, actual:{actual}"

    def test_error_box(self):
        expected = 2
        Scores_page = SiuScores(self.driver, f"{os.getenv('TEST_USERNAME')}", f"{os.getenv('TEST_PASSWORD')}")
        Scores_page.ingresar_seccion_notas()
        opciones = Scores_page.obtener_opciones()
        opciones[1].click()
        time.sleep(3)
        opciones = Scores_page.obtener_opciones()
        opciones[0].click()
        time.sleep(2)
        actual = len(Scores_page.revisar_error_gestiones())
        assert expected == actual, f"FAIL: expected: {expected}, actual:{actual}"

    def test_error_title(self):
        expected = "ATÉNCION"
        Scores_page = SiuScores(self.driver, f"{os.getenv('TEST_USERNAME')}", f"{os.getenv('TEST_PASSWORD')}")
        Scores_page.ingresar_seccion_notas()
        opciones = Scores_page.obtener_opciones()
        opciones[1].click()
        time.sleep(3)
        opciones = Scores_page.obtener_opciones()
        opciones[0].click()
        time.sleep(2)
        actual = Scores_page.obtener_titulo_error
        assert expected in actual, f"FAIL: expected: {expected}, actual:{actual}"
    
    def test_error_message(self):
        expected = "Debe seleccionar una gestión para que pueda apreciar las notas."
        Scores_page = SiuScores(self.driver, f"{os.getenv('TEST_USERNAME')}", f"{os.getenv('TEST_PASSWORD')}")
        Scores_page.ingresar_seccion_notas()
        opciones = Scores_page.obtener_opciones()
        opciones[1].click()
        time.sleep(3)
        opciones = Scores_page.obtener_opciones()
        opciones[0].click()
        time.sleep(2)
        actual = Scores_page.obtener_mensaje_error
        assert expected in actual, f"FAIL: expected: {expected}, actual:{actual}"