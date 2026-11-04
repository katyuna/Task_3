from selenium.webdriver.common.by import By


class FeedPageLocators:
    FIRST_ORDER_CARD = (By.XPATH, "(//li[contains(@class, 'OrderHistory_listItem')])[1]")
    ORDER_CARD_NUMBER = (By.XPATH, "//li[contains(@class, 'OrderHistory_listItem')]//p[.='{}']")
    ORDER_DETAILS = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//div[contains(@class, 'Modal_orderBox')]")

    TOTAL_COMPLETED_COUNTER = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY_COMPLETED_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")

    IN_PROGRESS_ORDER_NUMBER = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li[.='{}']")
