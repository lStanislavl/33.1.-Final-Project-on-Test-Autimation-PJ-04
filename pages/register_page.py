from pages.base import BasePage
from pages.locators import *
from pages.locators import RegLocators
from config import Config
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class RegPage(BasePage):
    def __init__(self, driver, timeout=20):
        super().__init__(driver, timeout)
        driver.get(Config.BASE_REG_URL)
        # Ожидаем загрузки формы регистрации
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(RegLocators.REG_FORM)
        )

    def enter_firstname(self, value):
        self.first_name = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(RegLocators.REG_FIRSTNAME)
        )
        self.first_name.clear()
        self.first_name.send_keys(value)

    def enter_lastname(self, value):
        self.last_name = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(RegLocators.REG_LASTNAME)
        )
        self.last_name.clear()
        self.last_name.send_keys(value)

    def enter_email(self, value):
        self.email = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(RegLocators.REG_ADDRESS)
        )
        self.email.clear()
        self.email.send_keys(value)

    def enter_password(self, value):
        self.password = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(RegLocators.REG_PASSWORD)
        )
        self.password.clear()
        self.password.send_keys(value)

    def enter_pass_conf(self, value):
        self.pass_conf = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(RegLocators.REG_PASS_CONFIRM)
        )
        self.pass_conf.clear()
        self.pass_conf.send_keys(value)

    def btn_click(self):
        self.btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(RegLocators.REG_REGISTER)
        )
        self.btn.click()