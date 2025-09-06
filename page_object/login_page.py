from selenium.webdriver.common.by import By
from page_object.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://automationexercise.com/login"

    EMAIL_INPUT = (By.CSS_SELECTOR, '[data-qa="login-email"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '[data-qa="login-password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[data-qa="login-button"]')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, 'a[href="/logout"]')
    ERROR_INVALID_LOGIN = (
        By.XPATH,
        '//p[text()="Your email or password is incorrect!"]',
    )
    LOGIN_PAGE_HEADER = (By.XPATH, '//h2[text()="Login to your account"]')

    def login(self, email, password):
        self.logger.info("Логин с email = {email} и password = {password}")

        self.input_value(self.EMAIL_INPUT, email)
        self.input_value(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BUTTON)

    def is_logged_in(self):
        assert self.get_element(self.LOGOUT_BUTTON).is_displayed()

    def is_invalid_login_error_visible(self):
        assert self.get_element(self.ERROR_INVALID_LOGIN).is_displayed()

    def is_login_page_open(self):
        assert self.get_element(self.LOGIN_PAGE_HEADER).is_displayed()
