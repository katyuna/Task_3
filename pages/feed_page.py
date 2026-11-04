import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from data import WAIT_TIMEOUT, Urls
from locators.feed_page_locators import FeedPageLocators
from pages.base_page import BasePage


class FeedPage(BasePage):
    # Лента и счётчики приходят по веб-сокету, поэтому ждём появления первой карточки заказа
    @allure.step("Открыть ленту заказов")
    def open_feed_page(self):
        self.open(Urls.FEED_PAGE)
        self.wait_for_visible(FeedPageLocators.FIRST_ORDER_CARD)

    @allure.step("Нажать на заказ в ленте")
    def click_first_order(self):
        self.click(FeedPageLocators.FIRST_ORDER_CARD)

    @allure.step("Проверить, что открыто окно с деталями заказа")
    def is_order_details_opened(self):
        return self.is_visible(FeedPageLocators.ORDER_DETAILS)

    @allure.step("Проверить, что заказ {order_number} есть в ленте")
    def is_order_in_feed(self, order_number):
        by, xpath = FeedPageLocators.ORDER_CARD_NUMBER
        return self.is_visible((by, xpath.format(order_number)))

    @allure.step("Получить счётчик «Выполнено за всё время»")
    def get_total_completed_counter(self):
        return int(self.get_text(FeedPageLocators.TOTAL_COMPLETED_COUNTER))

    @allure.step("Получить счётчик «Выполнено за сегодня»")
    def get_today_completed_counter(self):
        return int(self.get_text(FeedPageLocators.TODAY_COMPLETED_COUNTER))

    @allure.step("Проверить, что счётчик «Выполнено за всё время» стал больше {value_before}")
    def is_total_completed_counter_increased(self, value_before):
        return self.is_counter_increased(FeedPageLocators.TOTAL_COMPLETED_COUNTER, value_before)

    @allure.step("Проверить, что счётчик «Выполнено за сегодня» стал больше {value_before}")
    def is_today_completed_counter_increased(self, value_before):
        return self.is_counter_increased(FeedPageLocators.TODAY_COMPLETED_COUNTER, value_before)

    # В разделе «В работе» приложение приписывает к номеру "0" спереди: 1169 -> "01169"
    @allure.step("Проверить, что заказ {order_number} появился в разделе «В работе»")
    def is_order_in_progress(self, order_number):
        by, xpath = FeedPageLocators.IN_PROGRESS_ORDER_NUMBER
        return self.is_visible((by, xpath.format(f"0{order_number}")))

    # Счётчик обновляется по веб-сокету не сразу, поэтому ждём, пока значение вырастет
    def is_counter_increased(self, locator, value_before):
        try:
            WebDriverWait(self.driver, WAIT_TIMEOUT).until(
                lambda driver: int(self.get_text(locator)) > value_before
            )
            return True
        except TimeoutException:
            return False
