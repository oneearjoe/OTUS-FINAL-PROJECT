from selenium.webdriver.common.by import By
from page_object.base_page import BasePage


class ProductDetailPage(BasePage):
    REVIEW_NAME_INPUT = (By.ID, "name")
    REVIEW_EMAIL_INPUT = (By.ID, "email")
    REVIEW_TEXTAREA = (By.ID, "review")
    SUBMIT_REVIEW_BTN = (By.ID, "button-review")
    SUCCESS_REVIEW_MSG = (By.CSS_SELECTOR, ".alert-success")  # сообщение после отправки

    def open(self, product_url: str):
        self.browser.get(product_url)

    def fill_review_form(self, name: str, email: str, review: str):
        self.input_value(self.REVIEW_NAME_INPUT, name)
        self.input_value(self.REVIEW_EMAIL_INPUT, email)
        self.input_value(self.REVIEW_TEXTAREA, review)

    def submit_review(self):
        self.click_element(self.SUBMIT_REVIEW_BTN)

    def is_review_submitted(self) -> bool:
        try:
            return self.get_element(self.SUCCESS_REVIEW_MSG).is_displayed()
        except:
            return False
