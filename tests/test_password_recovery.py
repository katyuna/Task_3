import allure

from data import Urls
from helpers.data_generators import generate_user_data
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from pages.reset_password_page import ResetPasswordPage


@allure.feature("Восстановление пароля")
class TestPasswordRecovery:
    @allure.title("Переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_click_forgot_password_link_opens_forgot_password_page(self, driver):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.click_forgot_password_link()

        assert login_page.is_url_opened(Urls.FORGOT_PASSWORD_PAGE)

    @allure.title("Ввод почты и клик по кнопке «Восстановить» открывают страницу сброса пароля")
    def test_submit_email_opens_reset_password_page(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.open_forgot_password_page()
        forgot_password_page.enter_email(generate_user_data()["email"])
        forgot_password_page.click_restore_button()

        assert forgot_password_page.is_url_opened(Urls.RESET_PASSWORD_PAGE)

    @allure.title("Клик по кнопке показать/скрыть пароль подсвечивает поле пароля")
    def test_show_password_button_highlights_password_field(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.open_forgot_password_page()
        forgot_password_page.enter_email(generate_user_data()["email"])
        forgot_password_page.click_restore_button()
        forgot_password_page.wait_for_url(Urls.RESET_PASSWORD_PAGE)

        reset_password_page = ResetPasswordPage(driver)
        reset_password_page.click_show_password_button()

        assert reset_password_page.is_password_field_active()
