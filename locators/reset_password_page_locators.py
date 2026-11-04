from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//label[text()='Пароль']/following-sibling::div[contains(@class, 'input__icon-action')]")
    ACTIVE_PASSWORD_FIELD = (By.XPATH, "//label[text()='Пароль']/parent::div[contains(@class, 'input_status_active')]")
