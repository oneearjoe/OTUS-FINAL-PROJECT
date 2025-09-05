from selenium.webdriver.common.by import By
from page_object.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://automationexercise.com/login"

    # Локаторы
    EMAIL_INPUT = (By.CSS_SELECTOR, '[data-qa="login-email"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '[data-qa="login-password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[data-qa="login-button"]')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, 'a[href="/logout"]')  # появляется после логина
    ERROR_INVALID_LOGIN = (By.XPATH, '//p[text()="Your email or password is incorrect!"]')
    LOGIN_PAGE_HEADER = (By.XPATH, '//h2[text()="Login to your account"]')

    def open(self):
        """Открыть страницу логина"""
        self.browser.get(self.URL)

    def login(self, email: str, password: str):
        """Вводим email/пароль и жмем кнопку входа"""
        self.input_value(self.EMAIL_INPUT, email)
        self.input_value(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BUTTON)

    def is_logged_in(self) -> bool:
        """Проверка, что после логина появилась кнопка Logout"""
        try:
            return self.get_element(self.LOGOUT_BUTTON).is_displayed()
        except:
            return False
        
    def is_invalid_login_error_visible(self):
        try:
            return self.get_element(self.ERROR_INVALID_LOGIN).is_displayed()
        except:
            return False
        
    def is_login_page_open(self):
        assert self.get_element(self.LOGIN_PAGE_HEADER).is_displayed()
