import requests
from utils.data_generator import generate_user_data

API_URL = "https://automationexercise.com/api/createAccount"


def register_user_via_api() -> dict:
    """Регистрирует пользователя через API и возвращает его данные"""
    user_data = generate_user_data()

    files = {key: (None, value) for key, value in user_data.items()}
    response = requests.post(API_URL, files=files)

    if response.status_code != 200:
        raise Exception(
            f"Ошибка при создании пользователя: {response.status_code}, {response.text}"
        )

    if "Account already exists" in response.text:
        raise Exception(f"Email уже существует: {user_data['email']}")

    return user_data
