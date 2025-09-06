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

    assert response.status_code == 200
    body = response.json()
    assert body["id"] == order_data["id"]
    assert body["status"] == status
    assert body["complete"] == complete


@allure.feature("API магазина")
@allure.story("Получение заказа по ID")
def test_get_order(order_id):
    response = StoreAPI.get_order(order_id)
    assert response.status_code == 200
    assert response.json()["id"] == order_id


@allure.feature("API магазина")
@allure.story("Удаление заказа")
def test_delete_order(order_id):
    delete_response = Base.wait_for_status(
        StoreAPI.delete_order, 200, order_id=order_id
    )
    assert delete_response.status_code == 200

    get_response = StoreAPI.get_order(order_id)
    assert get_response.status_code == 404


@allure.feature("API магазина")
@allure.story("Удаление несуществующего заказа (негативный сценарий)")
def test_delete_order_negative():
    response = StoreAPI.delete_order(999999)
    assert response.status_code == 404


@allure.feature("API магазина")
@allure.story("Получение инвентаря")
def test_get_inventory():
    response = StoreAPI.get_inventory()
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    for status, quantity in data.items():
        assert isinstance(status, str)
        assert isinstance(quantity, int)
