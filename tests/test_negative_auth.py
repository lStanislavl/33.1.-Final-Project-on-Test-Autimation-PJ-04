import pytest
import time
from pages.auth_page import AuthPage
from pages.locators import AuthLocators
from config import Config
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_with_invalid_phone(chrome_browser):
    """ TC-013 Авторизация по номеру телефона при использовании невалидного номера телефона """
    page = AuthPage(chrome_browser)

    chrome_browser.implicitly_wait(10)

    page.enter_login(Config.INVALID_PHONE)
    page.enter_pass(Config.VALID_PASSWORD)

    time.sleep(2)
    page.btn_click()

    error_mess = page.find_element(AuthLocators.AUTH_FORM_ERROR)
    forgot_pass = page.find_element(AuthLocators.FORGOT_PASSWORD)
    assert error_mess.text in [
        'Неверный логин или пароль',
        'Неверно введен текст с картинки'
    ]

def test_login_with_invalid_email(chrome_browser):
    """ TC-014 Авторизация по номеру телефона при использовании невалидного e-mail """
    page = AuthPage(chrome_browser)
    page.click_email_tab()
    page.enter_login(Config.INVALID_EMAIL)
    page.enter_pass(Config.VALID_PASSWORD)
    # Ожидание для ручного ввода капчи
    try:
        # Проверяем наличие капчи
        if page.is_captcha_present():
            pytest.skip("Тест требует ручного ввода капчи")

        page.btn_click()
        error_mess = page.find_element(AuthLocators.AUTH_FORM_ERROR)
        forgot_pass = page.find_element(AuthLocators.FORGOT_PASSWORD)
        assert error_mess.text == 'Неверный логин или пароль' and \
           page.check_color(forgot_pass) == '#ff4f12'
    except Exception as e:
        chrome_browser.save_screenshot("error.png")
        raise e


def test_login_with_valid_email_invalid_pass(chrome_browser):
    """ TC-018 Авторизация по номеру телефона при использовании невалидного пароля """
    page = AuthPage(chrome_browser)
    page.click_email_tab()
    page.enter_login(Config.VALID_EMAIL)
    page.enter_pass(Config.INVALID_PASSWORD)
    chrome_browser.implicitly_wait(25)
    page.btn_click()

    # Добавить обработку капчи, если она появилась
    if page.is_captcha_present():
        pytest.skip("Тест требует ручного ввода капчи")

    error_mess = page.find_element(AuthLocators.AUTH_FORM_ERROR)
    forgot_pass = page.find_element(AuthLocators.FORGOT_PASSWORD)
    assert error_mess.text == 'Неверный логин или пароль' and \
           page.check_color(forgot_pass) == '#ff4f12'

def test_login_with_valid_phone_invalid_pass(chrome_browser):
    """ TC-019 Авторизация по e-mail при использовании невалидного пароля """
    page = AuthPage(chrome_browser)
    page.enter_login(Config.VALID_PHONE)
    page.enter_pass(Config.INVALID_PASSWORD)

    chrome_browser.implicitly_wait(30)
    page.btn_click()

    if page.is_captcha_present():
        pytest.skip("Тест требует ручного ввода капчи")

    error_mess = page.find_element(AuthLocators. AUTH_FORM_ERROR)
    forgot_pass = page.find_element(AuthLocators.FORGOT_PASSWORD)
    assert error_mess.text == 'Неверный логин или пароль' and \
           page.check_color(forgot_pass) == '#ff4f12'