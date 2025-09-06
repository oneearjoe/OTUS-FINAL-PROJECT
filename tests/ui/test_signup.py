import allure
from page_object.signup_page import SignupPage
from utils.data_generator import generate_user_data
from utils.api_helpers import register_user_via_api


@allure.feature("Регистрация")
@allure.story("Создание нового пользователя")
def test_user_can_signup(browser):
    signup_page = SignupPage(browser)

    with allure.step("Открываем страницу регистрации"):
        signup_page.open_login_signup_page()

    user_data = generate_user_data()

    with allure.step("Вводим имя и email"):
        signup_page.start_signup(user_data["name"], user_data["email"])

    with allure.step("Заполняем остальные поля регистрации"):
        signup_page.complete_signup(user_data)

    with allure.step("Проверяем сообщение об успешной регистрации"):
        signup_page.is_signed_up()


@allure.feature("Регистрация")
@allure.story("Попытка регистрации с существующим email")
def test_register_existing_email(browser):
    signup_page = SignupPage(browser)

    with allure.step("Создаём пользователя через API"):
        user_data = register_user_via_api()

    with allure.step("Открываем страницу регистрации"):
        signup_page.open_login_signup_page()

    with allure.step("Пытаемся зарегистрировать с существующим email"):
        signup_page.start_signup(user_data["name"], user_data["email"])

    with allure.step("Проверяем, что появилась ошибка о существующем email"):
        signup_page.is_email_already_exists_error_visible()
