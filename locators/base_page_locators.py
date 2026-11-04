from selenium.webdriver.common.by import By


class BasePageLocators:
    CONSTRUCTOR_LINK = (By.XPATH, "//header//li/a[@href='/']")
    FEED_LINK = (By.XPATH, "//header//a[@href='/feed']")
    PERSONAL_ACCOUNT_LINK = (By.XPATH, "//header//a[@href='/account']")

    LOADING_OVERLAY = (By.XPATH, "//img[@alt='loading animation']/parent::div")
