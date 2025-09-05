from selenium.webdriver.common.by import By
from page_object.base_page import BasePage


class TestCasesPage(BasePage):
    TEST_CASES_HEADER = (By.CSS_SELECTOR, "h2.title.text-center")

    def is_test_cases_page_opened(self):
        assert self.get_element(self.TEST_CASES_HEADER).is_displayed()