import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from data import ORDER_NUMBER_PLACEHOLDER, WAIT_TIMEOUT, Urls
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step("Открыть главную страницу (конструктор)")
    def open_main_page(self):
        self.open(Urls.MAIN_PAGE)

    @allure.step("Нажать на булку")
    def click_bun(self):
        self.click(MainPageLocators.FIRST_BUN)

    @allure.step("Проверить, что открыто окно «Детали ингредиента»")
    def is_ingredient_details_opened(self):
        return self.is_visible(MainPageLocators.INGREDIENT_DETAILS_TITLE)

    @allure.step("Закрыть окно крестиком")
    def close_modal(self):
        self.click(MainPageLocators.MODAL_CLOSE_BUTTON)

    @allure.step("Проверить, что окно закрыто")
    def is_modal_closed(self):
        return self.is_invisible(MainPageLocators.OPENED_MODAL)

    @allure.step("Получить значение каунтера булки")
    def get_bun_counter(self):
        return int(self.get_text(MainPageLocators.FIRST_BUN_COUNTER))

    @allure.step("Перетащить булку в конструктор")
    def add_bun_to_order(self):
        self.drag_and_drop(MainPageLocators.FIRST_BUN, MainPageLocators.BURGER_CONSTRUCTOR)

    @allure.step("Нажать на кнопку «Оформить заказ»")
    def click_order_button(self):
        self.click(MainPageLocators.ORDER_BUTTON)

    @allure.step("Получить номер оформленного заказа")
    def get_order_number(self):
        try:
            WebDriverWait(self.driver, WAIT_TIMEOUT).until(
                lambda driver: self.get_text(MainPageLocators.ORDER_NUMBER) != ORDER_NUMBER_PLACEHOLDER
            )
        except TimeoutException:
            pass
        return self.get_text(MainPageLocators.ORDER_NUMBER)
