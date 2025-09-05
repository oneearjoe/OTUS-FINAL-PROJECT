import allure
from page_object.home_page import HomePage
from page_object.signup_page import SignupPage
from utils.data_generator import generate_user_data


@allure.feature("Регистрация")
@allure.story("Создание нового пользователя")
def test_user_can_signup(browser):
    """Тест регистрации нового пользователя"""

    signup_page = SignupPage(browser)

    # Открываем страницу
    with allure.step("Открываем страницу регистрации"):
        signup_page.open_login_signup_page()

    # Генерируем данные
    user_data = generate_user_data()

    # Заполняем имя + email
    with allure.step("Вводим имя и email"):
        signup_page.start_signup(user_data["name"], user_data["email"])

    # Заполняем остальное
    with allure.step("Заполняем остальные поля регистрации"):
        signup_page.complete_signup(user_data)

    # Проверяем создание аккаунта
    with allure.step("Проверяем сообщение об успешной регистрации"):
        assert signup_page.is_signed_up(), "Аккаунт не был создан!"

@allure.feature("Регистрация")
@allure.story("Попытка регистрации с существующим email")
def test_register_existing_email(browser):
    signup_page = SignupPage(browser)
    home_page = HomePage(browser)

    # Открываем страницу
    signup_page.open_login_signup_page()

    # Генерируем нового пользователя
    user_data = generate_user_data()

    # Сначала регистрируем пользователя нормально
    signup_page.start_signup(user_data["name"], user_data["email"])
    signup_page.complete_signup(user_data)

    home_page.open_home_page()
    home_page.logout()

    # Пытаемся зарегистрировать с тем же email
    signup_page.open_login_signup_page()  # обновляем страницу
    signup_page.start_signup(user_data["name"], user_data["email"])
    
    # Проверяем, что появилась ошибка о существующем email
    assert signup_page.is_email_already_exists_error_visible(), "Ошибка существующего email не появилась"
