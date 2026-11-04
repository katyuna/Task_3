import allure

from data import Urls
from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePage


class ProfilePage(BasePage):
    @allure.step("Открыть страницу профиля")
    def open_profile_page(self):
        self.open(Urls.PROFILE_PAGE)

    @allure.step("Нажать на «История заказов»")
    def click_order_history_link(self):
        self.click(ProfilePageLocators.ORDER_HISTORY_LINK)

    @allure.step("Нажать на кнопку «Выход»")
    def click_logout_button(self):
        self.click(ProfilePageLocators.LOGOUT_BUTTON)
