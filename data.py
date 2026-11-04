class Urls:
    BASE_URL = "https://stellarburgers.education-services.ru"
    MAIN_PAGE = f"{BASE_URL}/"
    LOGIN_PAGE = f"{BASE_URL}/login"
    FORGOT_PASSWORD_PAGE = f"{BASE_URL}/forgot-password"
    RESET_PASSWORD_PAGE = f"{BASE_URL}/reset-password"
    PROFILE_PAGE = f"{BASE_URL}/account/profile"
    ORDER_HISTORY_PAGE = f"{BASE_URL}/account/order-history"
    FEED_PAGE = f"{BASE_URL}/feed"


class Endpoints:
    REGISTER = f"{Urls.BASE_URL}/api/auth/register"
    USER = f"{Urls.BASE_URL}/api/auth/user"
    INGREDIENTS = f"{Urls.BASE_URL}/api/ingredients"
    ORDERS = f"{Urls.BASE_URL}/api/orders"


# Время ожидания элементов в секундах
WAIT_TIMEOUT = 10

BROWSERS = ["chrome", "firefox"]

# Сколько раз пробовать запустить браузер, если окно оказалось «битым» (см. conftest.py)
BROWSER_START_ATTEMPTS = 3

# Номер, который окно заказа показывает, пока сервер не вернул настоящий
ORDER_NUMBER_PLACEHOLDER = "9999"
