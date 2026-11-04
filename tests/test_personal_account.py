import allure

from data import Urls
from pages.profile_page import ProfilePage


@allure.feature("Личный кабинет")
class TestPersonalAccount:
    @allure.title("Переход в личный кабинет по клику на «Личный кабинет»")
    def test_click_personal_account_opens_profile_page(self, logged_in_driver):
        profile_page = ProfilePage(logged_in_driver)
        profile_page.click_personal_account_link()

        assert profile_page.is_url_opened(Urls.PROFILE_PAGE)

    @allure.title("Переход в раздел «История заказов»")
    def test_click_order_history_opens_order_history_page(self, logged_in_driver):
        profile_page = ProfilePage(logged_in_driver)
        profile_page.open_profile_page()
        profile_page.click_order_history_link()

        assert profile_page.is_url_opened(Urls.ORDER_HISTORY_PAGE)

    @allure.title("Выход из аккаунта перенаправляет на страницу входа")
    def test_logout_redirects_to_login_page(self, logged_in_driver):
        profile_page = ProfilePage(logged_in_driver)
        profile_page.open_profile_page()
        profile_page.click_logout_button()

        assert profile_page.is_url_opened(Urls.LOGIN_PAGE)
