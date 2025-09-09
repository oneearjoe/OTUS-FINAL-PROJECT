from selenium.webdriver.common.by import By
from page_object.base_page import BasePage


class ContactUsPage(BasePage):
    NAME_INPUT = (By.CSS_SELECTOR, '[data-qa="name"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, '[data-qa="email"]')
    SUBJECT_INPUT = (By.CSS_SELECTOR, '[data-qa="subject"]')
    MESSAGE_TEXTAREA = (By.CSS_SELECTOR, '[data-qa="message"]')
    UPLOAD_FILE_INPUT = (By.CSS_SELECTOR, '[name="upload_file"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '[data-qa="submit-button"]')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".status.alert.alert-success")

    def open_contact_page(self):
        self.logger.info(
            f"{self.class_name}: Open page {self.browser.base_url + '/contact_us'}"
        )

        self.browser.get(self.browser.base_url + "/contact_us")
        return self

    def fill_contact_form(self, name, email, subject, message):
        self.logger.info("Заполняем контактную инфу")
        self.input_value(self.NAME_INPUT, name)
        self.input_value(self.EMAIL_INPUT, email)
        self.input_value(self.SUBJECT_INPUT, subject)
        self.input_value(self.MESSAGE_TEXTAREA, message)

    def submit_form(self):
        self.logger.info("отправляе форму")
        self.click_element(self.SUBMIT_BUTTON)

    def is_success_message_visible(self):
        assert self.get_element(self.SUCCESS_MESSAGE).is_displayed()

    def accept_alert(self):
        self.logger.info("Переключаемся на алерт и жмем ок")
        alert = self.browser.switch_to.alert
        alert.accept()
