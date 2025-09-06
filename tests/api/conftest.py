import pytest
from faker import Faker
from services.store.store_api import StoreAPI

fake = Faker()


@pytest.fixture
def user_data():
    return {
        "id": fake.random_int(min=10000, max=99999),
        "username": fake.user_name() + str(fake.random_int(1000, 9999)),
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "email": fake.email(),
        "password": fake.password(length=10),
        "phone": fake.msisdn(),
        "userStatus": 0,
    }


@pytest.fixture
def order_data():
    """Базовый заказ с дефолтными значениями"""
    return {
        "id": fake.unique.random_int(min=10000, max=99999),
        "petId": fake.random_int(min=1000, max=9999),
        "quantity": fake.random_int(min=1, max=5),
        "shipDate": fake.future_datetime().isoformat(),
        "status": "placed",
        "complete": True,
    }


@pytest.fixture
def order_id(order_data):
    """Создаёт заказ и возвращает его id"""
    response = StoreAPI.create_order(order_data)
    assert response.status_code == 200, f"Ошибка при создании заказа: {response.text}"
    return order_data["id"]


@pytest.fixture
def pet_data():
    """Генерация уникальных данных для пета"""
    return {
        "id": fake.random_int(min=100000, max=999999),
        "name": fake.first_name(),
        "photoUrls": [fake.image_url()],
        "status": fake.random_element(elements=("available", "pending", "sold")),
    }
