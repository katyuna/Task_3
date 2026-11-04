import allure
import requests

from data import Endpoints


@allure.step("Создать пользователя через API")
def register_user(user_data):
    return requests.post(Endpoints.REGISTER, json=user_data)


@allure.step("Удалить пользователя через API")
def delete_user(access_token):
    return requests.delete(Endpoints.USER, headers={"Authorization": access_token})


@allure.step("Получить id булки через API")
def get_bun_id():
    ingredients = requests.get(Endpoints.INGREDIENTS).json()["data"]
    return next(ingredient["_id"] for ingredient in ingredients if ingredient["type"] == "bun")


@allure.step("Создать заказ через API")
def create_order(access_token):
    response = requests.post(
        Endpoints.ORDERS,
        json={"ingredients": [get_bun_id()]},
        headers={"Authorization": access_token},
    )
    assert response.status_code == 200, f"Не удалось создать заказ: {response.text}"
    return response.json()["order"]["number"]
