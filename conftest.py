import pytest
import allure
import uuid
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver(chrome_options):
    """Фикстура для создания экземпляра браузера Chrome"""
    # Убедимся, что папка для скриншотов существует
    if not os.path.exists('screenshots'):
        os.makedirs('screenshots')

    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--log-level=DEBUG')

    # Используем webdriver-manager для автоматической загрузки и настройки chromedriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.set_window_size(1400, 1000)
    yield driver
    driver.quit()

@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.add_argument('--disable-captcha')
    return chrome_options

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """Хук pytest: позволяет определить, упал ли тест"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture
def chrome_browser(request, driver):
    """Фикстура с обработкой ошибок и созданием скриншотов при падении"""
    browser = driver
    yield browser

    if request.node.rep_call.failed:
        try:
            browser.execute_script("document.body.bgColor = 'white';")
            # Используем os.path.join для правильного формирования пути
            screenshot_path = os.path.join('screenshots', f'{uuid.uuid4()}.png')
            browser.save_screenshot(screenshot_path)

            allure.attach(browser.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)

            print('URL: ', browser.current_url)
            print('Browser logs:')
            for log in browser.get_log('browser'):
                print(log)

        except Exception as e:
            print(f'Ошибка при снятии скриншота: {e}')
            pass

def get_test_case_docstring(item):
    """Получаем docstring из теста, чтобы использовать его как имя теста"""
    full_name = ''

    if item._obj.__doc__:
        name = str(item._obj.__doc__.split('.')[0]).strip()
        full_name = ' '.join(name.split())

        if hasattr(item, 'callspec'):
            params = item.callspec.params
            res_keys = sorted(params.keys())
            res = [f'{k}_"{"{}".format(params[k])}"' for k in res_keys]
            full_name += ' Parameters ' + ', '.join(res)
            full_name = full_name.replace(':', '')

    return full_name

def pytest_itemcollected(item):
    """Изменяем имя теста во время сбора, если указан docstring"""
    if item._obj.__doc__:
        item._nodeid = get_test_case_docstring(item)

def pytest_collection_finish(session):
    """Переименовываем тесты при использовании параметра --collect-only"""
    if session.config.option.collectonly is True:
        for item in session.items:
            if item._obj.__doc__:
                full_name = get_test_case_docstring(item)
                print(full_name)
        pytest.exit('Done!')