from selenium.webdriver.common.by import By
from page_object.base_page import BasePage


class ProductDetailPage(BasePage):
    REVIEW_NAME_INPUT = (By.ID, "name")
    REVIEW_EMAIL_INPUT = (By.ID, "email")
    REVIEW_TEXTAREA = (By.ID, "review")
    SUBMIT_REVIEW_BTN = (By.ID, "button-review")
    SUCCESS_REVIEW_MSG = (By.CSS_SELECTOR, ".alert-success")

    def open_product_details_page(self):
        self.logger.info(
            f"{self.class_name}: Open page {self.browser.base_url + '/product_details/1'}"
        )

        self.browser.get(self.browser.base_url + "/product_details/1")
        return self

    def fill_review_form(self, name, email, review):
        self.logger.info("Заполняем отзыв")
        self.input_value(self.REVIEW_NAME_INPUT, name)
        self.input_value(self.REVIEW_EMAIL_INPUT, email)
        self.input_value(self.REVIEW_TEXTAREA, review)

    def submit_review(self):
        self.logger.info("Подтверждаем отзыв")
        self.click_element(self.SUBMIT_REVIEW_BTN)

    def is_review_submitted(self):
        assert self.get_element(self.SUCCESS_REVIEW_MSG).is_displayed()
