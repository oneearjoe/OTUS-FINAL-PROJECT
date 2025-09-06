from selenium.webdriver.common.by import By
from page_object.base_page import BasePage


class HomePage(BasePage):
    LOGOUT_BTN = (By.LINK_TEXT, "Logout")
    TEST_CASES_LINK = (By.LINK_TEXT, "Test Cases")

    def logout(self):
        self.logger.info("Выходим из аккаунта")
        self.click_element(self.LOGOUT_BTN)

    def open_home_page(self):
        self.logger.info(f"{self.class_name}: Open page {self.browser.base_url}")

        self.browser.get(self.browser.base_url)
        return self
