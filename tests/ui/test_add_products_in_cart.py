import time
import allure
from page_object.products_page import ProductsPage


@allure.feature("Корзина")
@allure.story("Add Products to Cart")
def test_add_products_to_cart(browser):
    products_page = ProductsPage(browser)

    with allure.step("Открываем страницу продуктов"):
        products_page.open()

    with allure.step("Добавляем первый продукт в корзину"):
        products_page.add_first_product_to_cart()

    with allure.step("Переходим в корзину"):
        products_page.go_to_cart()

    with allure.step("Проверяем, что продукт появился в корзине"):
        assert products_page.is_product_in_cart(), "Продукт не добавился в корзину"


@allure.feature("Корзина")
@allure.story("Remove Products from Cart")
def test_remove_products_from_cart(browser):
    products_page = ProductsPage(browser)

    with allure.step("Открываем страницу продуктов"):
        products_page.open()

    with allure.step("Добавляем первый продукт в корзину"):
        products_page.add_first_product_to_cart()

    time.sleep(2)
    with allure.step("Переходим в корзину"):
        products_page.go_to_cart()

    with allure.step("Проверяем, что продукт появился в корзине"):
        assert products_page.is_product_in_cart(), "Продукт не добавился в корзину"

    with allure.step("Удаляем продукт из корзины"):
        products_page.remove_product_from_cart()

    time.sleep(2)
    with allure.step("Проверяем, что корзина пустая"):
        products_page.is_cart_empty(), "Продукт не был удален из корзины"

