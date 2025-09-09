import allure
import pytest
from services.store.store_api import StoreAPI
from services.base import Base

@pytest.mark.api
@allure.feature("Store API")
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
    json_data = response.json()
    StoreAPI.check_response_status_code(response, 200)

    assert json_data["id"] == order_data["id"], f"ID заказа не совпадает: ожидалось {order_data['id']}, получено {body['id']}"
    assert json_data["status"] == status, f"Статус заказа не совпадает: ожидалось {status}, получено {body['status']}"
    assert json_data["complete"] == complete, f"Флаг complete не совпадает: ожидалось {complete}, получено {body['complete']}"

@pytest.mark.api
@allure.feature("Store API")
@allure.story("Получение заказа по ID")
def test_get_order(order_id):
    response = StoreAPI.get_order(order_id)
    StoreAPI.check_response_status_code(response, 200)
    assert response.json()["id"] == order_id, f"ID заказа не совпадает: ожидалось {order_id}, получено {response.json()['id']}"

@pytest.mark.api
@allure.feature("Store API")
@allure.story("Удаление заказа")
def test_delete_order(order_id):
    response = Base.wait_for_status(
        StoreAPI.delete_order, 200, order_id=order_id
    )
    StoreAPI.check_response_status_code(response, 200)
    response = StoreAPI.get_order(order_id)
    StoreAPI.check_response_status_code(response, 404)

@pytest.mark.api
@allure.feature("Store API")
@allure.story("Удаление несуществующего заказа (негативный сценарий)")
def test_delete_order_negative():
    response = StoreAPI.delete_order(999999)
    StoreAPI.check_response_status_code(response, 404)

@pytest.mark.api
@allure.feature("Store API")
@allure.story("Получение инвентаря")
def test_get_inventory():
    response = StoreAPI.get_inventory()
    StoreAPI.check_response_status_code(response, 200)
    json_data = response.json()
    assert isinstance(json_data, dict)
