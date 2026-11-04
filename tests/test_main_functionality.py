import allure

from data import ORDER_NUMBER_PLACEHOLDER, Urls
from pages.main_page import MainPage


@allure.feature("Основной функционал")
class TestMainFunctionality:
    @allure.title("Переход в конструктор по клику на «Конструктор»")
    def test_click_constructor_opens_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.open(Urls.FEED_PAGE)
        main_page.click_constructor_link()

        assert main_page.is_url_opened(Urls.MAIN_PAGE)

    @allure.title("Переход в ленту заказов по клику на «Лента заказов»")
    def test_click_feed_opens_feed_page(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_feed_link()

        assert main_page.is_url_opened(Urls.FEED_PAGE)

    @allure.title("Клик на ингредиент открывает окно с деталями")
    def test_click_ingredient_opens_details_modal(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_bun()

        assert main_page.is_ingredient_details_opened()

    @allure.title("Окно с деталями ингредиента закрывается кликом по крестику")
    def test_close_ingredient_details_modal(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_bun()
        main_page.close_modal()

        assert main_page.is_modal_closed()

    @allure.title("При добавлении ингредиента в заказ увеличивается его каунтер")
    def test_add_ingredient_increases_counter(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        counter_before = main_page.get_bun_counter()
        main_page.add_bun_to_order()

        assert main_page.get_bun_counter() > counter_before

    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_logged_in_user_can_place_order(self, logged_in_driver):
        main_page = MainPage(logged_in_driver)
        main_page.add_bun_to_order()
        main_page.click_order_button()

        assert main_page.get_order_number() != ORDER_NUMBER_PLACEHOLDER
