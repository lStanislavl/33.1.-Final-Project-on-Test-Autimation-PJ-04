from pages.auth_page import *
from pages.register_page import RegPage
from config import *
from selenium.webdriver.common.by import By
import pytest
import time

@pytest.mark.parametrize("firstname", ['', generate_string_rus(1), generate_string_rus(31),
                                       generate_string_rus(256), english_chars(), chinese_chars(),
                                       special_chars(), 11111],
                         ids=['empty', 'one char', '31 chars', '256 chars', 'english', 'chinese',
                              'special', 'number'])

def test_get_registration_invalid_format_firstname(chrome_browser, firstname):
    """Негативные сценарии регистрации на сайте, невалидный формат имени"""

    # Нажимаем на кнопку Зарегистрироваться:
    page = AuthPage(chrome_browser)
    page.go_to_reg_page()
    chrome_browser.implicitly_wait(10)
    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'

    page = RegPage(chrome_browser)
    # Вводим имя:
    page.enter_firstname(firstname)
    chrome_browser.implicitly_wait(5)
    # Вводим фамилию:
    page.enter_lastname(Config.INVALID_LASTNAME)
    chrome_browser.implicitly_wait(5)
    # Вводим адрес почты/Email:
    page.enter_email(Config.VALID_EMAIL)
    chrome_browser.implicitly_wait(5)
    # Вводим пароль:
    page.enter_password(Config.VALID_PASSWORD)
    chrome_browser.implicitly_wait(5)
    # Вводим подтверждение пароля:
    page.enter_pass_conf(Config.VALID_PASSWORD)
    chrome_browser.implicitly_wait(5)
    # Нажимаем на кнопку 'Зарегистрироваться':
    page.btn_click()

    error_mess = chrome_browser.find_element(*AuthLocators.AUTH_MESS_ERROR)

    assert error_mess.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


@pytest.mark.parametrize("lastname", ['', generate_string_rus(1), generate_string_rus(31),
                                       generate_string_rus(256), english_chars(), chinese_chars(),
                                       special_chars(), 11111],
                         ids=['empty', 'one char', '31 chars', '256 chars', 'english', 'chinese',
                              'special', 'number'])

def test_get_registration_invalid_format_lastname(chrome_browser, lastname):
    """Негативные сценарии регистрации на сайте, невалидный формат фамилии"""

    # Нажимаем на кнопку Зарегистрироваться:
    page = AuthPage(chrome_browser)
    page.go_to_reg_page()
    chrome_browser.implicitly_wait(5)
    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'

    page = RegPage(chrome_browser)
    # Вводим имя:
    page.enter_firstname(Config.FIRSTNAME)
    chrome_browser.implicitly_wait(5)
    # Вводим фамилию:
    page.enter_lastname(Config.INVALID_LASTNAME)
    chrome_browser.implicitly_wait(5)
    # Вводим адрес почты/Email:
    page.enter_email(Config.VALID_EMAIL)
    chrome_browser.implicitly_wait(5)
    # Вводим пароль:
    page.enter_password(Config.VALID_PASSWORD)
    chrome_browser.implicitly_wait(5)
    # Вводим подтверждение пароля:
    page.enter_pass_conf(Config.VALID_PASSWORD)
    chrome_browser.implicitly_wait(5)
    # Нажимаем на кнопку 'Зарегистрироваться':
    page.btn_click()

    error_mess = chrome_browser.find_element(*AuthLocators.AUTH_MESS_ERROR)

    assert error_mess.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


@pytest.mark.parametrize('phone', ['', 1, 7111111111, generate_string_rus(11), special_chars()],
                         ids=['empty', 'one digit', 'no 1 digit', 'string', 'specials'])

def test_get_registration_invalid_format_phone(chrome_browser, phone):

    """Негативные сценарии регистрации на сайте, невалидный формат номер телефона"""

    # Нажимаем на кнопку Зарегистрироваться:
    page = AuthPage(chrome_browser)
    page.go_to_reg_page()
    chrome_browser.implicitly_wait(2)
    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'

    page = RegPage(chrome_browser)
    # Вводим имя:
    page.enter_firstname(Config.FIRSTNAME)
    chrome_browser.implicitly_wait(5)
    # Вводим фамилию:
    page.enter_lastname(Config.LASTNAME)
    chrome_browser.implicitly_wait(5)
    # Вводим номер телефона:
    page.enter_email(Config.INVALID_PHONE)
    chrome_browser.implicitly_wait(3)
    # Вводим пароль:
    page.enter_password(Config.VALID_PASSWORD)
    chrome_browser.implicitly_wait(3)
    # Вводим подтверждение пароля:
    page.enter_pass_conf(Config.VALID_PASSWORD)
    chrome_browser.implicitly_wait(3)
    # Нажимаем на кнопку 'Зарегистрироваться':
    page.btn_click()

    error_mess = chrome_browser.find_element(*AuthLocators.AUTH_MESS_ERROR)
    assert error_mess.text == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, ' \
                              'или email в формате example@email.ru'


@pytest.mark.parametrize('email', ['', '@', '@.', '.', generate_string_rus(20), f'{russian_chars()}@mail.ru',
                                   f'{chinese_chars()}@mail.ru', 11111],
                         ids=['empty', 'at', 'at point', 'point', 'string', 'russian',
                              'chinese', 'numbers'])

def test_get_registration_invalid_format_email(chrome_browser, email):

    """Негативные сценарии регистрации на сайте, невалидный формат email"""

    # Нажимаем на кнопку Зарегистрироваться:
    page = AuthPage(chrome_browser)
    page.go_to_reg_page()
    chrome_browser.implicitly_wait(2)
    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'

    page = RegPage(chrome_browser)
    # Вводим имя:
    page.enter_firstname(Config.FIRSTNAME)
    chrome_browser.implicitly_wait(5)
    # Вводим фамилию:
    page.enter_lastname(Config.LASTNAME)
    chrome_browser.implicitly_wait(5)
    # Вводим адрес почты/Email:
    page.enter_email(Config.INVALID_EMAIL)
    chrome_browser.implicitly_wait(3)
    # Вводим пароль:
    page.enter_password(Config.VALID_PASSWORD)
    chrome_browser.implicitly_wait(3)
    # Вводим подтверждение пароля:
    page.enter_pass_conf(Config.VALID_PASSWORD)
    chrome_browser.implicitly_wait(3)
    # Нажимаем на кнопку 'Зарегистрироваться':
    page.btn_click()

    error_mess = chrome_browser.find_element(*AuthLocators.AUTH_MESS_ERROR)
    assert error_mess.text == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, ' \
                              'или email в формате example@email.ru'


@pytest.mark.parametrize('address', [Config.VALID_PHONE, Config.VALID_EMAIL],
                         ids=['living phone', 'living email'])

def test_get_registration_living_account(chrome_browser, address):
    """ ТС-028 Регистрация нового пользователя через уже использованый ранее e-mail """

    # Нажимаем на кнопку Зарегистрироваться:
    page = AuthPage(chrome_browser)
    page.go_to_reg_page()
    chrome_browser.implicitly_wait(2)
    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'

    page = RegPage(chrome_browser)
    # Вводим имя:
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
    # Нажимаем на кнопку 'Зарегистрироваться':
    page.btn_click()

    card_modal_title = chrome_browser.find_element(*RegLocators.REG_CARD_MODAL)

    assert card_modal_title.text == 'Учётная запись уже существует'


def test_get_registration_diff_pass_and_pass_conf(chrome_browser):

    """Негативные сценарии регистрации на сайте, проверка на совпадение паролей в
    полях ввода 'Пароль' и 'Подтверждение пароля'."""

    page = AuthPage(chrome_browser)
    page.go_to_reg_page()
    chrome_browser.implicitly_wait(2)
    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'

    page = RegPage(chrome_browser)
    # Вводим имя:
    page.enter_firstname(Config.FIRSTNAME)
    chrome_browser.implicitly_wait(5)
    # Вводим фамилию:
    page.enter_lastname(Config.LASTNAME)
    chrome_browser.implicitly_wait(5)
    # Вводим адрес почты/Email:
    page.enter_email(Config.VALID_EMAIL)
    chrome_browser.implicitly_wait(3)
    # Вводим пароль:
    page.enter_password(Config.INVALID_PASSWORD)
    chrome_browser.implicitly_wait(3)
    # Вводим подтверждение пароля:
    page.enter_pass_conf(Config.VALID_PASSWORD)
    chrome_browser.implicitly_wait(3)
    # Нажимаем на кнопку 'Зарегистрироваться':
    page.btn_click()

    error_mess = chrome_browser.find_element(*AuthLocators.AUTH_MESS_ERROR)
    assert error_mess.text == 'Пароли не совпадают'