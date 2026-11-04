import allure

from data import Urls
from locators.order_history_page_locators import OrderHistoryPageLocators
from pages.base_page import BasePage


class OrderHistoryPage(BasePage):
    @allure.step("Открыть историю заказов")
    def open_order_history_page(self):
        self.open(Urls.ORDER_HISTORY_PAGE)

    @allure.step("Получить номер заказа из истории")
    def get_order_number(self):
        return self.get_text(OrderHistoryPageLocators.FIRST_ORDER_NUMBER)
