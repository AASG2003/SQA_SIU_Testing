# Incluir acá los test cases para el módulo específico.
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from page_elements.siu_assignaturas.module_assignaturas import Atestear
import time

class TestAssig:
    def setup_method(self):
        self.driver = webdriver.Edge()
        self.driver.maximize_window()
        self.login_page = Atestear(self.driver)
        self.login_page.open_url('https://enlace.univalle.edu/san/webform/PAutenticar.aspx')

    def teardown_method(self):
        self.driver.quit()
    
    def test_verify_testo_academico(self):
        self.login_page.verify_login()
        self.login_page.entrar_asignaturas()
        expected = 'Gestión Académica'
        actual = self.login_page.get_text("//span[contains(text(),'Gestión Académica')]")
        assert expected == actual, f"Fail: actual: {actual}, esperado: {expected}"
        print(f'Se encontró: {actual}')
        print('Proceso terminado.')

    def test_verify_gestion(self):
        self.login_page.verify_login()
        self.login_page.entrar_asignaturas()
        expected = 'Gestión 2/2024'
        self.login_page.click_element("//*[@id='CPHBody_ddlGestion']")
        actual = self.login_page.get_text("//option[contains(text(),'Gestión 2/2024')]")
        assert expected == actual, f"Fail: actual: {actual}, esperado: {expected}"
        print(f'Se encontró: {actual}')
        print('Proceso terminado.')

    def test_busqueda_y_error_mensajes_nohay(self):
        self.login_page.verify_login()
        self.login_page.entrar_asignaturas()
        expected = 'No existen mensajes para la materia.'
        self.login_page.click_element("//*[@id='accordionFormulario']/div[2]/h2/button")
        time.sleep(1)
        self.login_page.click_element("//*[@id='CPHBody_MateriasRepeater_lkbArchivo_1']")
        time.sleep(1)
        self.login_page.fill_form("//*[@id='CPHBody_CUMensajeEstudiante_TXBBusqueda']","Ya aprobeeee?")
        time.sleep(1)
        self.login_page.click_element("//*[@id='CPHBody_CUMensajeEstudiante_IBTBuscar']")
        time.sleep(4)
        actual = self.login_page.get_text("//*[contains(text(),'No existen mensajes para la materia.')]")
        assert expected == actual, f"Fail: actual: {actual}, esperado: {expected}"
        print(f'Se encontró: {actual}')
        print('Proceso terminado.')

    def test_verificar_guia(self):
        self.login_page.verify_login()
        self.login_page.entrar_asignaturas()
        expected = 'RE-10-LAB-061 REALIDAD VIRTUAL Y AUMENTADA v1.pdf'
        self.login_page.click_element("//*[@id='accordionFormulario']/div[2]/h2/button")
        time.sleep(1)
        self.login_page.click_element("//*[@id='CPHBody_MateriasRepeater_LinkButton1_1']")
        time.sleep(1)
        self.login_page.click_element("//*[@id='CPHBody_CUGuiaEstudiante_GRVGuia_LKBArchivo_0']")
        time.sleep(3)
        actual = self.login_page.get_text("//a[contains(text(),'RE-10-LAB-061 REALIDAD VIRTUAL Y AUMENTADA v1.pdf')]")
        assert expected == actual, f"Fail: actual: {actual}, esperado: {expected}"
        print(f'Se encontró: {actual}')
        print('Proceso terminado.')
    
    def test_error_noguia(self):
        self.login_page.verify_login()
        self.login_page.entrar_asignaturas()
        expected = 'La materia no tiene guías registradas.'
        self.login_page.click_element("//*[@id='CPHBody_MateriasRepeater_LinkButton1_0']")
        time.sleep(2)
        actual = self.login_page.get_text("//span[contains(text(),'La materia no tiene guías registradas.')]")
        assert expected == actual, f"Fail: actual: {actual}, esperado: {expected}"
        print(f'Se encontró: {actual}')
        print('Proceso terminado.')

    def test_verificar_asistencia(self):
        self.login_page.verify_login()
        self.login_page.entrar_asignaturas()
        expected = 'Mi Registro de Asistencias '
        self.login_page.click_element("//*[@id='accordionFormulario']/div[3]/h2/button")
        time.sleep(1)
        self.login_page.click_element("//*[@id='CPHBody_MateriasRepeater_LinkButton2_3']")
        time.sleep(6)
        actual = self.login_page.get_text("//h3[contains(text(),'Mi Registro de Asistencias ')]")
        assert expected == actual, f"Fail: actual: {actual}, esperado: {expected}"
        print(f'Se encontró: {actual}')
        print('Proceso terminado.')
    
    def test_verify_ciudad(self):
        self.login_page.verify_login()
        self.login_page.entrar_asignaturas()
        expected = 'La Paz'
        time.sleep(2)
        actual = self.login_page.get_text("//div[contains(text(),'La Paz')]")
        assert expected == actual, f"Fail: actual: {actual}, esperado: {expected}"
        print(f'Se encontró: {actual}')
        print('Proceso terminado.')

    def test_verify_fecha(self):
        self.login_page.verify_login()
        self.login_page.entrar_asignaturas()
        expected = '03 diciembre 2024'
        time.sleep(2)
        actual = self.login_page.get_text("//span[contains(text(),'03 diciembre 2024')]")
        assert expected == actual, f"Fail: actual: {actual}, esperado: {expected}"
        print(f'Se encontró: {actual}')
        print('Proceso terminado.')

