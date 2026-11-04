import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchWindowException

from data import BROWSER_START_ATTEMPTS, BROWSERS, Urls
from helpers.api_helpers import delete_user, register_user
from helpers.data_generators import generate_user_data
from pages.login_page import LoginPage


def create_driver(browser_name):
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        return webdriver.Chrome(options=options)
    options = webdriver.FirefoxOptions()
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    return webdriver.Firefox(options=options)


# Firefox изредка запускается с «битым» окном: первая же навигация падает с
# NoSuchWindowException (Browsing context has been discarded), и повторы в той же сессии
# не помогают. Поэтому сразу после запуска открываем сайт, а при сбое перезапускаем браузер.
def create_working_driver(browser_name):
    for _ in range(BROWSER_START_ATTEMPTS):
        browser = create_driver(browser_name)
        try:
            browser.get(Urls.MAIN_PAGE)
            return browser
        except NoSuchWindowException:
            browser.quit()
    raise RuntimeError(f"Не удалось запустить {browser_name} за {BROWSER_START_ATTEMPTS} попытки")


# Каждый тест запускается дважды - в Chrome и в Firefox
@pytest.fixture(params=BROWSERS)
def driver(request):
    browser = create_working_driver(request.param)
    yield browser
    browser.quit()


# Создание пользователя через API и удаление после теста
@pytest.fixture
def user():
    user_data = generate_user_data()
    response = register_user(user_data)
    assert response.status_code == 200, f"Не удалось создать пользователя: {response.text}"
    user_data["access_token"] = response.json()["accessToken"]
    yield user_data
    delete_user(user_data["access_token"])


# Браузер с пользователем, который уже вошёл в аккаунт
@pytest.fixture
def logged_in_driver(driver, user):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login(user["email"], user["password"])
    return driver
