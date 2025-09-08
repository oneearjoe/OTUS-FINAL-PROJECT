import allure
from services.user.user_api import UserAPI
from services.base import Base


@allure.feature("API пользователей")
@allure.story("Создание пользователя")
def test_create_user(user_data):
    response = UserAPI.create_user(user_data)
    assert response.status_code == 200, f"Ожидался статус 200 при создании пользователя, получен {response.status_code}"
    assert response.json()["message"] == str(user_data["id"]), f"Сообщение в ответе не совпадает: ожидалось {user_data['id']}, получено {response.json()['message']}"


@allure.feature("API пользователей")
@allure.story("Получение пользователя по имени")
def test_get_user_by_name(user_data):
    UserAPI.create_user(user_data)

    response = Base.wait_for_status(
        UserAPI.get_user_by_name, 200, username=user_data["username"]
    )
    body = response.json()
    assert response.status_code == 200, f"Ожидался статус 200 при получении пользователя, получен {response.status_code}"
    assert body["username"] == user_data["username"], f"Имя пользователя не совпадает: ожидалось {user_data['username']}, получено {body['username']}"
    assert body["email"] == user_data["email"], f"Email пользователя не совпадает: ожидалось {user_data['email']}, получено {body['email']}"


@allure.feature("API пользователей")
@allure.story("Логин пользователя")
def test_login_user(user_data):
    UserAPI.create_user(user_data)
    response = UserAPI.login(user_data["username"], user_data["password"])
    assert response.status_code == 200, f"Ожидался статус 200 при логине пользователя, получен {response.status_code}"
    assert "logged in user session" in response.text, f"В ответе не найдена строка 'logged in user session': {response.text}"


@allure.feature("API пользователей")
@allure.story("Обновление данных пользователя")
def test_update_user(user_data):
    UserAPI.create_user(user_data)

    updated_data = user_data.copy()
    updated_data["firstName"] = "UpdatedName"

    response = UserAPI.update_user(user_data["username"], updated_data)
    assert response.status_code == 200, f"Ожидался статус 200 при обновлении пользователя, получен {response.status_code}"
    assert response.json()["message"] == str(user_data["id"]), f"Сообщение в ответе не совпадает: ожидалось {user_data['id']}, получено {response.json()['message']}"

    response = Base.wait_for_status(
        UserAPI.get_user_by_name, 200, username=user_data["username"]
    )
    assert response.status_code == 200, f"Ожидался статус 200 при проверке обновлённого пользователя, получен {response.status_code}"
    assert response.json()["firstName"] == "UpdatedName", f"Имя пользователя не обновлено: ожидалось 'UpdatedName', получено {response.json()['firstName']}"


@allure.feature("API пользователей")
@allure.story("Логаут пользователя")
def test_logout_user():
    response = UserAPI.logout()
    assert response.status_code == 200, f"Ожидался статус 200 при логауте пользователя, получен {response.status_code}"


@allure.feature("API пользователей")
@allure.story("Удаление пользователя")
def test_delete_user(user_data):
    UserAPI.create_user(user_data)

    response = Base.wait_for_status(
        UserAPI.delete_user, 200, username=user_data["username"]
    )
    assert response.status_code == 200, f"Ожидался статус 200 при удалении пользователя, получен {response.status_code}"
    assert response.json()["message"] == user_data["username"], f"Сообщение при удалении не совпадает: ожидалось {user_data['username']}, получено {response.json()['message']}"

    get_response = UserAPI.get_user_by_name(user_data["username"])
    assert get_response.status_code == 404, f"После удаления пользователь должен быть недоступен (404), получен {get_response.status_code}"
