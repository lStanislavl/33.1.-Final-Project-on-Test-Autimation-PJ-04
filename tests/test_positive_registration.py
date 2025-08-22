from pages.auth_page import *
from pages.register_page import RegPage
from config import Config
import pytest
import time

def test_create_new_acc(chrome_browser):
    """ ТС-027 Регистрация нового пользователя через e-mail при использовании валидных данных """
    page = AuthPage(chrome_browser)
    page.go_to_reg_page()
    chrome_browser.implicitly_wait(5)
    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'

    page = RegPage(chrome_browser)
    # Вводим имя
    page.enter_firstname(Config.FIRSTNAME)
    chrome_browser.implicitly_wait(5)
    # Вводим фамилию:
    page.enter_lastname(Config.LASTNAME)
    chrome_browser.implicitly_wait(5)
    # Вводим адрес почты/Email:
    page.enter_email(Config.VALID_EMAIL)
    chrome_browser.implicitly_wait(3)
    # Вводим пароль:
    page.enter_password(Config.VALID_PASSWORD)
    chrome_browser.implicitly_wait(3)
    # Вводим подтверждение пароля:
    page.enter_pass_conf(Config.VALID_PASSWORD)
    chrome_browser.implicitly_wait(3)
    page.btn_click()
    time.sleep(30)