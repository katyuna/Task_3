from selenium.webdriver.common.by import By


class MainPageLocators:
    FIRST_BUN = (By.XPATH, "(//h2[text()='Булки']/following-sibling::ul[1]//a[contains(@class, 'BurgerIngredient')])[1]")
    FIRST_BUN_COUNTER = (By.XPATH, "(//h2[text()='Булки']/following-sibling::ul[1]//a[contains(@class, 'BurgerIngredient')])[1]//p[contains(@class, 'counter_counter__num')]")
    BURGER_CONSTRUCTOR = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")

    # Открытое всплывающее окно (у закрытого нет класса Modal_modal_opened)
    OPENED_MODAL = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]")
    INGREDIENT_DETAILS_TITLE = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//h2[text()='Детали ингредиента']")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//button[contains(@class, 'Modal_modal__close')]")
    ORDER_NUMBER = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//h2[contains(@class, 'text_type_digits-large')]")
