import allure

from helpers.api_helpers import create_order
from pages.feed_page import FeedPage
from pages.order_history_page import OrderHistoryPage


@allure.feature("Лента заказов")
class TestOrderFeed:
    @allure.title("Клик на заказ открывает окно с деталями")
    def test_click_order_opens_details_modal(self, driver):
        feed_page = FeedPage(driver)
        feed_page.open_feed_page()
        feed_page.click_first_order()

        assert feed_page.is_order_details_opened()

    @allure.title("Заказы из «Истории заказов» отображаются в ленте")
    def test_order_from_history_is_shown_in_feed(self, logged_in_driver, user):
        create_order(user["access_token"])
        order_history_page = OrderHistoryPage(logged_in_driver)
        order_history_page.open_order_history_page()
        order_number = order_history_page.get_order_number()

        feed_page = FeedPage(logged_in_driver)
        feed_page.open_feed_page()

        assert feed_page.is_order_in_feed(order_number)

    @allure.title("При создании заказа увеличивается счётчик «Выполнено за всё время»")
    def test_new_order_increases_total_completed_counter(self, driver, user):
        feed_page = FeedPage(driver)
        feed_page.open_feed_page()
        counter_before = feed_page.get_total_completed_counter()
        create_order(user["access_token"])

        assert feed_page.is_total_completed_counter_increased(counter_before)

    @allure.title("При создании заказа увеличивается счётчик «Выполнено за сегодня»")
    def test_new_order_increases_today_completed_counter(self, driver, user):
        feed_page = FeedPage(driver)
        feed_page.open_feed_page()
        counter_before = feed_page.get_today_completed_counter()
        create_order(user["access_token"])

        assert feed_page.is_today_completed_counter_increased(counter_before)

    @allure.title("Номер нового заказа появляется в разделе «В работе»")
    def test_new_order_number_appears_in_progress(self, driver, user):
        feed_page = FeedPage(driver)
        feed_page.open_feed_page()
        order_number = create_order(user["access_token"])

        assert feed_page.is_order_in_progress(order_number)
