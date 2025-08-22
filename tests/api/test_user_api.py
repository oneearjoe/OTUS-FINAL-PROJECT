import time
from services.user.user_api import UserAPI
from services.base import Base


def test_create_user(user_data):
    response = UserAPI.create_user(user_data)
    assert response.status_code == 200
    assert response.json()["message"] == str(user_data["id"])


def test_get_user_by_name(user_data):
    UserAPI.create_user(user_data)

    print(user_data)

    response = Base.wait_for_status(
        UserAPI.get_user_by_name, 200, username=user_data["username"]
    )
    assert response.json()["username"] == user_data["username"]

    body = response.json()
    assert body["username"] == user_data["username"]
    assert body["email"] == user_data["email"]


def test_login_user(user_data):
    UserAPI.create_user(user_data)

    response = UserAPI.login(user_data["username"], user_data["password"])
    assert response.status_code == 200
    assert "logged in user session" in response.text


def test_update_user(user_data):
    UserAPI.create_user(user_data)

    updated_data = user_data.copy()
    updated_data["firstName"] = "UpdatedName"

    response = UserAPI.update_user(user_data["username"], updated_data)
    assert response.status_code == 200
    assert response.json()["message"] == str(user_data["id"])

    response = Base.wait_for_status(
        UserAPI.get_user_by_name, 200, username=user_data["username"]
    )
    assert response.status_code == 200
    assert response.json()["firstName"] == "UpdatedName"


def test_logout_user():
    response = UserAPI.logout()
    assert response.status_code == 200


def test_delete_user(user_data):
    UserAPI.create_user(user_data)

    response = Base.wait_for_status(
        UserAPI.delete_user, 200, username=user_data["username"]
    )
    assert response.status_code == 200
    assert response.json()["message"] == user_data["username"]

    get_response = UserAPI.get_user_by_name(user_data["username"])
    assert get_response.status_code == 404
