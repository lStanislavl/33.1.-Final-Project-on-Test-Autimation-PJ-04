import string
class Config:
    BASE_URL = 'https://b2c.passport.rt.ru/'  # страница авторизации
    BASE_REG_URL = 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration'  # страница регистрации
    BASE_RESET_URL = 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials?client_id=account_b2c&tab_id=gb3butOTVtE'  # страница восстановления пароля

    VALID_EMAIL = "kuyanovso@gmail.com"
    VALID_PHONE = "+79371000403"
    VALID_PASSWORD = "951753tP"
    INVALID_EMAIL = "test@mail.com"
    INVALID_PHONE = "+79058961473"
    INVALID_PASSWORD = "123456itP"
    NEW_PASSWORD = "Tpn258456"
    REQ_ELEMENTS_AUTH = ["Авторизация", "Телефон", "Почта", "Логин", "Лицевой счёт"]
    REQ_ELEMENTS_RESET = ["Телефон", "Почта", "Логин", "Лицевой счёт"]
    DEFAULT_LOGIN_TEXT = "Мобильный телефон"
    TAGLINE_TEXT = "Персональный помощник в цифровом мире Ростелекома"

    FIRSTNAME = "Станислав"
    INVALID_FIRSTNAME = "<Tester>"
    LASTNAME = "Куянов"
    INVALID_LASTNAME = "Tester"

def generate_string_rus(n):
    return 'б' * n

def generate_string_en(n):
    return 'x' * n

def english_chars():
    return 'qwertyuiopasdfghjklzxcvbnm'

def russian_chars():
    return 'абвгдеёжзиклмнопрстуфхцчшщъыьэюя'

def chinese_chars():  # 20 популярных китайских иероглифов
    return '的一是不了人我在有他这为之大来以个中上们'

def special_chars():
    return f'{string.punctuation}'