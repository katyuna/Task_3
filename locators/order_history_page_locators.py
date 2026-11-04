from selenium.webdriver.common.by import By


class OrderHistoryPageLocators:
    # Номер заказа в карточке, например "#01169" (первый <p> в заголовке карточки, второй — дата)
    FIRST_ORDER_NUMBER = (By.XPATH, "(//li[contains(@class, 'OrderHistory_listItem')])[1]//div[contains(@class, 'OrderHistory_textBox')]/p[1]")
