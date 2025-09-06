import allure
from faker import Faker
from page_object.product_detail_page import ProductDetailPage

fake = Faker()


@allure.feature("Продукты")
@allure.story("Add Review on Product")
def test_add_review_on_product(browser):
    product_page = ProductDetailPage(browser)

    with allure.step("Открываем страницу продукта"):
        product_page.open_product_details_page()

    with allure.step("Заполняем форму отзыва"):
        product_page.fill_review_form(
            name=fake.first_name(), email=fake.email(), review="This is a test review"
        )

    with allure.step("Отправляем отзыв"):
        product_page.submit_review()

    with allure.step("Проверяем, что отзыв отправлен успешно"):
        product_page.is_review_submitted(), "Отзыв не был отправлен"
