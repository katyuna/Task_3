import random
import string


def generate_random_string(length=8):
    return "".join(random.choices(string.ascii_lowercase + string.digits, k=length))


def generate_user_data():
    return {
        "email": f"test_{generate_random_string()}@yandex.ru",
        "password": generate_random_string(10),
        "name": f"User{generate_random_string(5)}",
    }
