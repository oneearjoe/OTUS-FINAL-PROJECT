import allure
import pytest
from faker import Faker
from page_object.contact_us_page import ContactUsPage

fake = Faker()

@pytest.mark.ui
@allure.feature("Форма обратной связи")
@allure.story("Contact Us Form")
def test_contact_us_form(browser, tmp_path):
    contact_page = ContactUsPage(browser)

    with allure.step("Открываем страницу Contact Us"):
        contact_page.open_contact_page()

    with allure.step("Заполняем форму"):
        contact_page.fill_contact_form(
            name=fake.first_name(),
            email=fake.email(),
            subject="Test Subject",
            message="This is a test message",
        )

    with allure.step("Отправляем форму"):
        contact_page.submit_form()

        contact_page.accept_alert()

    with allure.step("Проверяем сообщение об успешной отправке"):
        contact_page.is_success_message_visible()
