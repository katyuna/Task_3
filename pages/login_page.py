import allure

from data import Urls
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step("Открыть страницу входа")
    def open_login_page(self):
        self.open(Urls.LOGIN_PAGE)

    @allure.step("Нажать на ссылку «Восстановить пароль»")
    def click_forgot_password_link(self):
        self.click(LoginPageLocators.FORGOT_PASSWORD_LINK)

    @allure.step("Войти в аккаунт с почтой {email}")
    def login(self, email, password):
        self.enter_text(LoginPageLocators.EMAIL_INPUT, email)
        self.enter_text(LoginPageLocators.PASSWORD_INPUT, password)
        self.click(LoginPageLocators.LOGIN_BUTTON)
        self.wait_for_url(Urls.MAIN_PAGE)
