import allure
import pytest
from services.user.user_api import UserAPI
from services.base import Base

@pytest.mark.api
@allure.feature("User API")
@allure.story("Создание пользователя")
def test_create_user(user_data):
    response = UserAPI.create_user(user_data)
    UserAPI.check_response_status_code(response, 200)
    assert response.json()["message"] == str(user_data["id"]), f"Id пользователя в ответе не совпадает: ожидалось {user_data['id']}, получено {response.json()['message']}"

@pytest.mark.api
@allure.feature("User API")
@allure.story("Получение пользователя по имени")
def test_get_user_by_name(user_data):
    UserAPI.create_user(user_data)

    response = Base.wait_for_status(
        UserAPI.get_user_by_name, 200, username=user_data["username"]
    )
    UserAPI.check_response_status_code(response, 200)
    assert response.json()["username"] == user_data["username"], f"Имя пользователя не совпадает: ожидалось {user_data['username']}, получено {body['username']}"
    assert response.json()["email"] == user_data["email"], f"Email пользователя не совпадает: ожидалось {user_data['email']}, получено {body['email']}"

@pytest.mark.api
@allure.feature("User API")
@allure.story("Логин пользователя")
def test_login_user(user_data):
    UserAPI.create_user(user_data)
    response = UserAPI.login(user_data["username"], user_data["password"])
    UserAPI.check_response_status_code(response, 200)
    assert "logged in user session" in response.text

@pytest.mark.api
@allure.feature("User API")
@allure.story("Обновление данных пользователя")
def test_update_user(user_data):
    UserAPI.create_user(user_data)

    updated_data = user_data.copy()
    updated_data["firstName"] = "UpdatedName"

    response = UserAPI.update_user(user_data["username"], updated_data)
    UserAPI.check_response_status_code(response, 200)
    assert response.json()["message"] == str(user_data["id"]), f"Id пользователя в ответе не совпадает: ожидалось {user_data['id']}, получено {response.json()['message']}"

    response = Base.wait_for_status(
        UserAPI.get_user_by_name, 200, username=user_data["username"]
    )
    UserAPI.check_response_status_code(response, 200)
    assert response.json()["firstName"] == "UpdatedName", f"Имя пользователя не обновлено: ожидалось 'UpdatedName', получено {response.json()['firstName']}"

@pytest.mark.api
@allure.feature("User API")
@allure.story("Логаут пользователя")
def test_logout_user():
    response = UserAPI.logout()
    UserAPI.check_response_status_code(response, 200)

@pytest.mark.api
@allure.feature("User API")
@allure.story("Удаление пользователя")
def test_delete_user(user_data):
    UserAPI.create_user(user_data)

    response = Base.wait_for_status(
        UserAPI.delete_user, 200, username=user_data["username"]
    )
    UserAPI.check_response_status_code(response, 200)
    assert response.json()["message"] == user_data["username"], f"Username в ответе не совпадает: ожидалось {user_data['username']}, получено {response.json()['message']}"

    response = UserAPI.get_user_by_name(user_data["username"])
    UserAPI.check_response_status_code(response, 404)
