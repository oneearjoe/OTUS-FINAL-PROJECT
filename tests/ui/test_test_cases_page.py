import allure
import pytest
from page_object.home_page import HomePage
from page_object.test_cases_page import TestCasesPage

@pytest.mark.ui
@allure.title("Test Case: Verify Test Cases Page")
def test_verify_test_cases_page(browser):
    home_page = HomePage(browser)
    test_cases_page = TestCasesPage(browser)

    with allure.step("Открываем главную страницу"):
        home_page.open_home_page()

    with allure.step("Переходим на страницу Test Cases"):
        home_page.click_element(home_page.TEST_CASES_LINK)

    with allure.step("Проверяем, что открылась страница Test Cases"):
        (test_cases_page.is_test_cases_page_opened(),)
