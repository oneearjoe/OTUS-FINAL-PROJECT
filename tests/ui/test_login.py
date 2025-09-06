import allure
from page_object.login_page import LoginPage
from page_object.home_page import HomePage
from page_object.signup_page import SignupPage
from utils.api_helpers import register_user_via_api


@allure.feature("Авторизация")
@allure.story("Login User with correct email and password")
def test_login_with_correct_credentials(browser):
    signup_page = SignupPage(browser)
    login_page = LoginPage(browser)

    with allure.step("Создаём пользователя через API"):
        user_data = register_user_via_api()

    with allure.step("Открываем страницу логина"):
        signup_page.open_login_signup_page()

    with allure.step("Вводим корректные email и пароль"):
        login_page.login(user_data["email"], user_data["password"])

    with allure.step("Проверяем, что пользователь успешно вошёл"):
        login_page.is_logged_in()


@allure.feature("Авторизация")
@allure.story("Login User with incorrect email and password")
def test_login_user_with_incorrect_credentials(browser):
    signup_page = SignupPage(browser)
    login_page = LoginPage(browser)

    with allure.step("Открываем страницу логина"):
        signup_page.open_login_signup_page()

    with allure.step("Вводим неверные данные"):
        login_page.login("wrong_email@example.com", "wrongpassword123")

    with allure.step("Проверяем, что появилось сообщение об ошибке"):
        login_page.is_invalid_login_error_visible()


@allure.feature("Авторизация")
@allure.story("Logout User")
def test_logout(browser):
    signup_page = SignupPage(browser)
    login_page = LoginPage(browser)
    home_page = HomePage(browser)

    with allure.step("Создаём пользователя через API"):
        user_data = register_user_via_api()

    with allure.step("Открываем страницу логина"):
        signup_page.open_login_signup_page()

    with allure.step("Вводим корректный email и пароль"):
        login_page.login(user_data["email"], user_data["password"])

    with allure.step("Разлогиниваемся"):
        home_page.logout()

    with allure.step("Проверяем, что открылась страница логина"):
        login_page.is_login_page_open(), "Страница логина не открылась"
