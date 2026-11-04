from selenium.webdriver.common.by import By


class OrderHistoryPageLocators:
    FIRST_ORDER_NUMBER = (By.XPATH, "(//li[contains(@class, 'OrderHistory_listItem')])[1]//div[contains(@class, 'OrderHistory_textBox')]/p[1]")
