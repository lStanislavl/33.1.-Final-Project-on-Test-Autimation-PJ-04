import time
import pytest
from pages.reset_page import ResetPage
from pages.locators import ResetLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.auth_page import AuthPage
from pages.reset_page import ResetPage
from config import Config



def test_go_to_reset_password_page(chrome_browser):
    """Тест TC-017 Проверка перехода на страницу "Восстановление пароля" """
    page = AuthPage(chrome_browser)
    page.go_to_reset_password_page()
    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/reset-credentials'

def test_check_elem_res_form(chrome_browser):
    """Тест TC-018 Проверка в соответствии с требованиями нахождения элементов "Восстановление пароля" """
    page = ResetPage(chrome_browser)
    page.go_to_reset_password_page()
    assert page.get_right_elem_reset_page() == Config.REQ_ELEMENTS_RESET

def test_default_login_tab(chrome_browser):
    """ Тест TC-019 Проверка того что по умолчанию выбрана форма восстановления пароля по телефону"""
    page = ResetPage(chrome_browser)
    assert page.get_text_from_login() == Config.DEFAULT_LOGIN_TEXT

def test_check_captcha(chrome_browser):
    """Тест TC-020 Проверка страницы "Восстановление пароля" на присутствие капчи"""
    page = ResetPage(chrome_browser)
    page.go_to_reset_password_page()
    assert page.find_element(ResetLocators.CAPTCHA)


def test_back_button(chrome_browser):
    """Тест TC-021 Проверка наличия и работы кнопки "Вернуться назад"""
    page = ResetPage(chrome_browser)
    page.go_to_reset_password_page()
    page.go_back_to_auth()
    assert page.get_relative_link() == "/auth/realms/b2c/login-actions/authenticate"

def test_positive_reset_password(chrome_browser):
    """Тест TC-017 Проверка перехода на страницу "Восстановление пароля" """
    page = ResetPage(chrome_browser)
    page.go_to_reset_password_page()
    page.enter_username(Config.VALID_PHONE)
    time.sleep(5)