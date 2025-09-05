from selenium.webdriver.common.by import By
from page_object.base_page import BasePage


class ContactUsPage(BasePage):
    # Локаторы
    NAME_INPUT = (By.CSS_SELECTOR, '[data-qa="name"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, '[data-qa="email"]')
    SUBJECT_INPUT = (By.CSS_SELECTOR, '[data-qa="subject"]')
    MESSAGE_TEXTAREA = (By.CSS_SELECTOR, '[data-qa="message"]')
    UPLOAD_FILE_INPUT = (By.CSS_SELECTOR, '[name="upload_file"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '[data-qa="submit-button"]')

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.status.alert.alert-success')

    def open(self):
        self.browser.get("https://automationexercise.com/contact_us")

    def fill_contact_form(self, name, email, subject, message, file_path=None):
        self.input_value(self.NAME_INPUT, name)
        self.input_value(self.EMAIL_INPUT, email)
        self.input_value(self.SUBJECT_INPUT, subject)
        self.input_value(self.MESSAGE_TEXTAREA, message)
        if file_path:
            self.get_element(self.UPLOAD_FILE_INPUT).send_keys(file_path)

    def submit_form(self):
        self.click_element(self.SUBMIT_BUTTON)

    def is_success_message_visible(self) -> bool:
        try:
            return self.get_element(self.SUCCESS_MESSAGE).is_displayed()
        except:
            return False
        
    def accept_alert(self):
        alert = self.browser.switch_to.alert
        alert.accept()
