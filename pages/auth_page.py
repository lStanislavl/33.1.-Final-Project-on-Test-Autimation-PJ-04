from pages.base import BasePage
from pages.locators import *
from config import Config
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class AuthPage(BasePage):
    """Создаем класс страницы "Авторизация"""
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = Config.BASE_URL or "https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid"
        driver.get(url)

        # Ожидаем загрузки ключевых элементов
        wait = WebDriverWait(driver, timeout)
        wait.until(EC.url_contains("passport.rt.ru"))

        self.login = self.find_element(AuthLocators.AUTH_LOGIN)
        self.password = self.find_element(AuthLocators.AUTH_PASS)
        self.btn_submit = self.find_element(AuthLocators.AUTH_BTN)
        self.phone_tab = self.find_element(AuthLocators.TAB_PHONE)
        self.mail_tab = self.find_element(AuthLocators.TAB_EMAIL)
        self.log_tab = self.find_element(AuthLocators.TAB_LOGIN)
        self.LS_tab = self.find_element(AuthLocators.TAB_LS)
        self.forgot_btn = self.find_element(AuthLocators.FORGOT_PASSWORD)

    def enter_login(self, value):
        """Ввести данные в поле логина"""
        self.login.send_keys(value)

    def enter_pass(self, value):
        """Ввести пароль"""
        self.password.send_keys(value)

    def btn_click(self):
        """Нажать на кнопку "Войти" """
        self.btn_submit.click()

    def find_logout_btn(self, timeout=10):
         # Поиск кнопки выхода для подтверждения успешной авторизации
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(AuthLocators.LOGOUT_BTN)
            )
        except:
            return None

    def get_right_elem_auth(self):
        """ Получаем текст правого блока страницы авторизация"""
        title = self.find_element(AuthLocators.AUTH_TITLE)
        title = [''.join(title.text)]

        right_block_auth = self.find_elements(AuthLocators.AUTH_BLOCK)
        elements_list = right_block_auth if isinstance(right_block_auth, list) else [right_block_auth]

        tabs = "".join([x.text for x in elements_list]).split('\n')
        elements = title + tabs
        return elements

    def get_text_from_login(self):
        """ Получить текст из поля ввода логина"""
        login_label = self.driver.find_element(*AuthLocators.AUTH_LOGIN_TEXT)
        return login_label.text

    def check_info_about_slogan(self):
        """Получить слоган со страницы Авторизации"""
        try:
            tagline = self.driver.find_element(*GlobalLocators.TAGLINE)
            return tagline.text if tagline.is_displayed() else ""
        except:
            return ""

    def click_phone_tab(self):
        """Нажать на таб "Номер" """
        self.phone_tab.click()

    def click_email_tab(self):
        """Нажать на таб "Почта" """
        self.mail_tab.click()

    def click_login_tab(self):
        """Нажать на таб "Логин" """
        self.log_tab.click()

    def click_LS_tab(self):
        """Нажать на таб "ЛС" """
        self.LS_tab.click()

    def logout_btn_click(self):
        """Нажать на кнопку "Выйти" на странице личного кабинета"""
        button = self.find_element(*AuthLocators.LOGOUT_BTN)
        button.click()

    def go_to_reg_page(self):
        """Перейти на страницу "Зарегистрироваться" со страницы "Авторизация" """
        reg_button = self.find_element(AuthLocators.REG_BTN)
        reg_button.click()

    def is_captcha_present(self, timeout=5):
        """Проверяет наличие капчи на странице"""
        try:
            return bool(self.find_element(AuthLocators.CAPTCHA, timeout))
        except:
            return False

    def go_to_reset_password_page(self):
        forgot_password = self.find_element(AuthLocators.FORGOT_PASSWORD)
        forgot_password.click()

    def get_error_message(self):
        """Получить текст сообщения об ошибке (например, "Неверный логин или пароль")"""
        try:
            error_element = self.find_element(AuthLocators.AUTH_MESS_ERROR)
            return error_element.text
        except:
            return None # Или ""

    def is_forgot_password_link_orange(self):
        """Проверить, стал ли элемент "Забыл пароль" оранжевым (например, после ошибки).
        Требует уточнения в locators.py, как определяется "оранжевый" (по классу или цвету CSS)."""
        try:
            class_attribute = self.forgot_btn.get_attribute("class")
            return "orange" in class_attribute.lower()
        except:
            return False