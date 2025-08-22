from selenium.webdriver.common.by import By

class GlobalLocators:
    RIGHT_BLOCK = (By.ID, "page-right")  # правый блок
    FOOTER_BLOCK = (By.CSS_SELECTOR, "footer")
    TAGLINE = (By.CSS_SELECTOR, ".what-is__desc") # слоган

class AuthLocators:
    AUTH_TITLE = (By.XPATH, "//h1[@class='card-container__title']") # Заголовок формы авторизации
    AUTH_BLOCK = (By.CSS_SELECTOR, ".rt-tabs.rt-tabs--orange.rt-tabs--small.tabs-input-container__tabs")
    AUTH_placeholder = (By.CSS_SELECTOR, "span.rt-input__placeholder")
    TAB_PHONE = (By.ID, "t-btn-tab-phone")  # Таб авторизации по телефону ("Номер")
    TAB_EMAIL = (By.ID, "t-btn-tab-mail")  # Таб авторизации по почте ("Почта")
    TAB_LOGIN = (By.ID, "t-btn-tab-login")  # Таб авторизации по логину ("Логин")
    TAB_LS = (By.ID, "t-btn-tab-ls")  # Таб авторизации по лицевому счету ("Лицевой счет")

    AUTH_LOGIN = (By.ID, "username")  # Поле ввода телефона/почты/логина/лицевого счета
    AUTH_PASS = (By.ID, "password")  # Поле для ввода пароля
    AUTH_BTN = (By.ID, "kc-login")  # Кнопка "Войти"
    AUTH_ACTIVE_TAB = (By.CSS_SELECTOR, "div.rt-tab.rt-tab--small.rt-tab--active")

    AUTH_LOGIN_TEXT = (By.XPATH, '//div[@class="rt-input-container tabs-input-container__login"]'
                                 '//span[@class="rt-input__placeholder"]')
    LOGOUT_BTN = (By.ID, "logout-btn")  # Кнопка "Выйти" в личном кабинете

    CAPTCHA = (By.ID, "captcha")  # Локатор капчи
    AUTH_FORM_ERROR = (By.XPATH, "//span[@id='form-error-message']")  # Сообщение об ошибке
    AUTH_MESS_ERROR = (By.CSS_SELECTOR, '.rt-input-container__meta--error')  # Сообщение об ошибке

    FORGOT_PASSWORD = (By.ID, "forgot_password") # Кнопка/Ссылка "Забыл пароль"
    REG_BTN = (By.ID, "kc-register") # Кнопка "Зарегистрироваться"

class ResetLocators:
    TEXT_RESET_FORM = (By.XPATH, "//h1[@class='card-container__title']") # Заголовок формы восстановления
    RIGHT_BLOCK_TABS = (By.CSS_SELECTOR, '.rt-tabs.rt-tabs--orange.rt-tabs--small.tabs-input-container__tabs')

    AUTH_LOGIN = (By.ID, "username")  # Поле ввода телефона/почты/логина/лицевого счета
    RESET_LOGIN_TEXT = (By.XPATH, ' //*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')
    CAPTCHA = (By.ID, "captcha") # Капча (поле ввода)
    BACK_BTN = (By.ID, "reset-back") # Кнопка "Вернуться назад"
    CONTINUE_BTN = (By.ID, "reset") # Кнопка "Продолжить"

    LOGIN_ERROR_BOX = (By.XPATH, "//*[@class='rt-input-container__meta rt-input-container__meta--error']") # Сообщение об ошибке валидации логина
    GENERAL_ERROR_BOX = (By.ID, "form-error-message") # Основное сообщение об ошибке

    TAB_PHONE = (By.ID, "t-btn-tab-phone")  # Таб по телефону ("Номер")
    TAB_EMAIL = (By.ID, "t-btn-tab-mail")  # Таб по почте ("Почта")
    TAB_LOGIN = (By.ID, "t-btn-tab-login")  # Таб по логину ("Логин")
    TAB_LS = (By.ID, "t-btn-tab-ls")  # Таб по лицевому счету ("Лицевой счет")

    NEW_PASS = (By.ID, "password-new") # Новое поле ввода пароля
    NEW_PASS_CONF = (By.ID, "password-confirm") # Поле подтверждения нового пароля
    SAVE_NEW_PASSWORD_BTN = (By.ID, "t-btn-reset-pass") # Кнопка "Сохранить"

    CODE_INPUTS = (By.CSS_SELECTOR, ".code-input__field") # Поля для ввода 6-значного кода подтверждения
    RESEND_CODE_BTN = (By.ID, "reset-resend-code") # Кнопка "Получить код повторно"
    CODE_ERROR_MESSAGE = (By.XPATH, "//span[@id='code-error-message']") # Сообщение об ошибке кода

    NEW_PASSWORD_ERROR = (By.XPATH, "//span[@id='password-new-error']") # Сообщение об ошибке под полем "Новый пароль"
    CONFIRM_PASSWORD_ERROR = (By.XPATH, "//span[@id='password-confirm-error']") # Сообщение об ошибке под полем "Подтверждение пароля"

class RegLocators:
    """Локаторы страницы регистрации"""

    REG_FORM = (By.CSS_SELECTOR, "form.register-form")
    # Поля формы
    REG_FIRSTNAME = (By.XPATH, "//input[@name='firstName' or contains(@id, 'firstName')]")
    REG_LASTNAME = (By.XPATH, "//input[@name='lastName' or contains(@id, 'lastName')]")
    REG_ADDRESS = (By.XPATH, "//input[@id='address' or @name='address']")
    REG_PASSWORD = (By.XPATH, "//input[@id='password' or @name='password']")
    REG_PASS_CONFIRM = (By.XPATH, "//input[@id='password-confirm' or @name='password-confirm']")

    REG_REGISTER = (By.NAME, 'register') # Кнопка "Продолжить"
    REG_CARD_MODAL = (By.XPATH, "//h2[@class='card-modal__title']") # Заголовок модального окна

    FIRST_NAME_ERROR = (By.XPATH, "//span[@id='error-firstName']") # Ошибка валидации имени
    LAST_NAME_ERROR = (By.XPATH, "//span[@id='error-lastName']") # Ошибка валидации фамилии
    ADDRESS_ERROR = (By.XPATH, "//span[@id='error-address']") # Ошибка валидации адреса/телефона
    PASSWORD_ERROR = (By.XPATH, "//span[@id='error-password']") # Ошибка валидации пароля
    CONFIRM_PASSWORD_ERROR = (By.XPATH, "//span[@id='error-password-confirm']") # Ошибка валидации подтверждения пароля

    EXISTING_ACCOUNT_MODAL = (By.XPATH, "//div[@class='card-modal__content']//h2[contains(text(), 'Учётная запись уже существует')]") # Модальное окно
    MODAL_LOGIN_BTN = (By.ID, "login_to_account_link") # Кнопка "Войти" в модалке
    MODAL_RESTORE_PASS_BTN = (By.ID, "restore_password_link") # Кнопка "Восстановить пароль" в модалке
    MODAL_CLOSE_BTN = (By.XPATH, "//div[@class='card-modal__content']//button[contains(@class, 'rt-btn') and contains(@class, 'card-modal__btn')]") # Кнопка закрытия модалки

    REG_CODE_INPUTS = (By.CSS_SELECTOR, ".code-input__field") # Поля для ввода кода подтверждения
    REG_RESEND_CODE_BTN = (By.ID, "reg-resend-code") # Кнопка "Получить код повторно"
    REG_CHANGE_PHONE_LINK = (By.ID, "reg-change-phone") # Ссылка "Изменить номер"
    REG_CHANGE_EMAIL_LINK = (By.ID, "reg-change-email") # Ссылка "Изменить почту"
    REG_CODE_ERROR_MESSAGE = (By.XPATH, "//span[@id='code-error-message']") # Сообщение об ошибке кода