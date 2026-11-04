from selenium.webdriver.common.by import By


# Шапка сайта — общая для всех страниц
class BasePageLocators:
    # li/a — чтобы не спутать с логотипом, который тоже ведёт на "/"
    CONSTRUCTOR_LINK = (By.XPATH, "//header//li/a[@href='/']")
    FEED_LINK = (By.XPATH, "//header//a[@href='/feed']")
    PERSONAL_ACCOUNT_LINK = (By.XPATH, "//header//a[@href='/account']")

    # Окно-загрузчик с затемнением: показывается при загрузке данных и перекрывает клики
    LOADING_OVERLAY = (By.XPATH, "//img[@alt='loading animation']/parent::div")
