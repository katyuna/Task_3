import allure

from data import Urls
from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):
    @allure.step("Открыть страницу восстановления пароля")
    def open_forgot_password_page(self):
        self.open(Urls.FORGOT_PASSWORD_PAGE)

    @allure.step("Ввести почту {email}")
    def enter_email(self, email):
        self.enter_text(ForgotPasswordPageLocators.EMAIL_INPUT, email)

    @allure.step("Нажать на кнопку «Восстановить»")
    def click_restore_button(self):
        self.click(ForgotPasswordPageLocators.RESTORE_BUTTON)
