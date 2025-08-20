import pytest
from faker import Faker

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
        "userStatus": 0
    }

