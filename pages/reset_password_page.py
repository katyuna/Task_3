import allure

from locators.reset_password_page_locators import ResetPasswordPageLocators
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):
    @allure.step("Нажать на кнопку показать/скрыть пароль")
    def click_show_password_button(self):
        self.click(ResetPasswordPageLocators.SHOW_PASSWORD_BUTTON)

    @allure.step("Проверить, что поле пароля подсвечено")
    def is_password_field_active(self):
        return self.is_visible(ResetPasswordPageLocators.ACTIVE_PASSWORD_FIELD)
