import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data import WAIT_TIMEOUT
from locators.base_page_locators import BasePageLocators

# drag-and-drop скрипт
DRAG_AND_DROP_SCRIPT = """
const source = arguments[0];
const target = arguments[1];
const dataTransfer = new DataTransfer();
const fire = (element, type) => element.dispatchEvent(
    new DragEvent(type, {bubbles: true, cancelable: true, dataTransfer: dataTransfer})
);
fire(source, 'dragstart');
fire(target, 'dragenter');
fire(target, 'dragover');
fire(target, 'drop');
fire(source, 'dragend');
"""


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть страницу {url}")
    def open(self, url):
        self.driver.get(url)

    def wait_for_visible(self, locator):
        return WebDriverWait(self.driver, WAIT_TIMEOUT).until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        wait = WebDriverWait(self.driver, WAIT_TIMEOUT)
        wait.until(EC.invisibility_of_element_located(BasePageLocators.LOADING_OVERLAY))
        wait.until(EC.element_to_be_clickable(locator)).click()

    def enter_text(self, locator, text):
        self.wait_for_visible(locator).send_keys(text)

    def get_text(self, locator):
        return self.wait_for_visible(locator).text

    def drag_and_drop(self, source_locator, target_locator):
        source = self.wait_for_visible(source_locator)
        target = self.wait_for_visible(target_locator)
        self.driver.execute_script(DRAG_AND_DROP_SCRIPT, source, target)

    @allure.step("Дождаться перехода на {url}")
    def wait_for_url(self, url):
        WebDriverWait(self.driver, WAIT_TIMEOUT).until(EC.url_to_be(url))

    @allure.step("Проверить, что открыта страница {url}")
    def is_url_opened(self, url):
        try:
            WebDriverWait(self.driver, WAIT_TIMEOUT).until(EC.url_to_be(url))
            return True
        except TimeoutException:
            return False

    def is_visible(self, locator):
        try:
            self.wait_for_visible(locator)
            return True
        except TimeoutException:
            return False

    def is_invisible(self, locator):
        try:
            WebDriverWait(self.driver, WAIT_TIMEOUT).until(EC.invisibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    @allure.step("Нажать на «Конструктор» в шапке")
    def click_constructor_link(self):
        self.click(BasePageLocators.CONSTRUCTOR_LINK)

    @allure.step("Нажать на «Лента заказов» в шапке")
    def click_feed_link(self):
        self.click(BasePageLocators.FEED_LINK)

    @allure.step("Нажать на «Личный кабинет» в шапке")
    def click_personal_account_link(self):
        self.click(BasePageLocators.PERSONAL_ACCOUNT_LINK)
