import allure
from page_object.login_page import LoginPage
from page_object.home_page import HomePage
from page_object.signup_page import SignupPage
from utils.data_generator import generate_user_data

@allure.feature("Авторизация")
@allure.story("Login User with correct email and password")
def test_login_with_correct_credentials(browser):
    signup_page = SignupPage(browser)
    login_page = LoginPage(browser)
    home_page = HomePage(browser)

    with allure.step("Открываем страницу логина"):
        signup_page.open_login_signup_page()

    user_data = generate_user_data()

        # Заполняем имя + email
    with allure.step("Вводим имя и email"):
        signup_page.start_signup(user_data["name"], user_data["email"])

    # Заполняем остальное
    with allure.step("Заполняем остальные поля регистрации"):
        signup_page.complete_signup(user_data)

    home_page.open_home_page()
    home_page.logout()

    with allure.step("Вводим корректный email и пароль"):
        # ⚠️ тут нужны данные существующего пользователя!
        email = user_data["email"]
        password = "Test123!"
        login_page.login(email, password)

    with allure.step("Проверяем, что пользователь успешно вошёл"):
        assert login_page.is_logged_in(), "Пользователь не смог войти в систему"

@allure.feature("Авторизация")
@allure.story("Login User with incorrect email and password")
def test_login_user_with_incorrect_credentials(browser):
    login_page = LoginPage(browser)

    with allure.step("Открываем страницу логина"):
        login_page.open()

    with allure.step("Вводим неверные данные"):
        login_page.login("wrong_email@example.com", "wrongpassword123")

    with allure.step("Проверяем, что появилось сообщение об ошибке"):
        assert login_page.is_invalid_login_error_visible(), \
            "Сообщение об ошибке не появилось при неверном логине"
        
@allure.feature("Авторизация")
@allure.story("Login User with correct email and password")
def test_logout(browser):
    signup_page = SignupPage(browser)
    login_page = LoginPage(browser)
    home_page = HomePage(browser)

    with allure.step("Открываем страницу логина"):
        signup_page.open_login_signup_page()

    user_data = generate_user_data()

        # Заполняем имя + email
    with allure.step("Вводим имя и email"):
        signup_page.start_signup(user_data["name"], user_data["email"])

    # Заполняем остальное
    with allure.step("Заполняем остальные поля регистрации"):
        signup_page.complete_signup(user_data)

    home_page.open_home_page()
    home_page.logout()

    login_page.is_login_page_open()
