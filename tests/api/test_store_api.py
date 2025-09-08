import allure
import pytest
from services.store.store_api import StoreAPI
from services.base import Base


@allure.feature("API магазина")
@allure.story("Создание заказа с разными статусами")
@pytest.mark.parametrize(
    "status, complete",
    [
        ("placed", True),
        ("placed", False),
        ("approved", True),
        ("approved", False),
        ("delivered", True),
        ("delivered", False),
    ],
)
def test_place_order(order_data, status, complete):
    order_data["status"] = status
    order_data["complete"] = complete

    response = StoreAPI.create_order(order_data)

    assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"
    body = response.json()
    assert body["id"] == order_data["id"], f"ID заказа не совпадает: ожидалось {order_data['id']}, получено {body['id']}"
    assert body["status"] == status, f"Статус заказа не совпадает: ожидалось {status}, получено {body['status']}"
    assert body["complete"] == complete, f"Флаг complete не совпадает: ожидалось {complete}, получено {body['complete']}"


@allure.feature("API магазина")
@allure.story("Получение заказа по ID")
def test_get_order(order_id):
    response = StoreAPI.get_order(order_id)
    assert response.status_code == 200, f"Ожидался статус 200 при получении заказа, получен {response.status_code}"
    assert response.json()["id"] == order_id, f"ID заказа не совпадает: ожидалось {order_id}, получено {response.json()['id']}"


@allure.feature("API магазина")
@allure.story("Удаление заказа")
def test_delete_order(order_id):
    delete_response = Base.wait_for_status(
        StoreAPI.delete_order, 200, order_id=order_id
    )
    assert delete_response.status_code == 200, f"Ожидался статус 200 при удалении заказа, получен {delete_response.status_code}"

    get_response = StoreAPI.get_order(order_id)
    assert get_response.status_code == 404, f"После удаления заказ должен быть недоступен (404), получен {get_response.status_code}"


@allure.feature("API магазина")
@allure.story("Удаление несуществующего заказа (негативный сценарий)")
def test_delete_order_negative():
    response = StoreAPI.delete_order(999999)
    assert response.status_code == 404, f"Для несуществующего заказа ожидается 404, получен {response.status_code}"


@allure.feature("API магазина")
@allure.story("Получение инвентаря")
def test_get_inventory():
    response = StoreAPI.get_inventory()
    assert response.status_code == 200, f"Ожидался статус 200 при получении инвентаря, получен {response.status_code}"
    data = response.json()
    assert isinstance(data, dict), f"Ожидался словарь в ответе, получен {type(data)}"
    for status, quantity in data.items():
        assert isinstance(status, str), f"Статус должен быть строкой, получено {type(status)}"
        assert isinstance(quantity, int), f"Количество должно быть числом, получено {type(quantity)}"
