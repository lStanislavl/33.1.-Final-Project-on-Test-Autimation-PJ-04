import time
from pages.base import BasePage
from pages.locators import ResetLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.auth_page import AuthPage
from config import Config


class ResetPage(BasePage):
    """Создаем класс страницы "Восстановление пароля" """

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)

        # Добавлена проверка текущего URL
        if "reset-credentials" not in driver.current_url:
            auth_page = AuthPage(driver)
            auth_page.go_to_reset_password_page()
            WebDriverWait(driver, 10).until(
                EC.url_contains("reset-credentials")
            )

        self.username = self.find_element(ResetLocators.AUTH_LOGIN)
        self.btn = self.find_element(ResetLocators.CONTINUE_BTN)

    def enter_username(self, value):
        """ Ввод логина """
        self.username.send_keys(value)

    def btn_click_continue(self):
        """ Кнопка "Продолжить" """
        self.btn.click()
        time.sleep(10)

    def get_right_elem_reset_page(self):
        """ Получаем названия табов блока восстановления пароля"""
        try:
            tabs = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_all_elements_located(ResetLocators.RIGHT_BLOCK_TABS)
            )
            return [tab.text.strip() for tab in tabs if tab.text]
        except:
            self.driver.save_screenshot('tabs_error.png')
            raise

    def get_text_from_login(self):
        """ Получить текст из поля ввода логина"""
        text_login = self.find_element(ResetLocators.RESET_LOGIN_TEXT)
        return text_login.text

    def go_back_to_auth(self):
        """ Вернуться в авторизации """
        back_btn = self.find_element(ResetLocators.BACK_BTN)
        back_btn.click()

    def get_text_of_form(self):
        self.find_element()