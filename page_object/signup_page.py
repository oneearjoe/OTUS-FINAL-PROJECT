import time
from selenium.webdriver.common.by import By
from page_object.base_page import BasePage
from helpers.data_generator import generate_user_data
import allure



class SignupPage(BasePage):

    SIGNUP_NAME = (By.CSS_SELECTOR, '[data-qa="signup-name"]')
    SIGNUP_EMAIL = (By.CSS_SELECTOR, '[data-qa="signup-email"]')
    SIGNUP_BTN = (By.CSS_SELECTOR, '[data-qa="signup-button"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '[data-qa="password"]')
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, '[data-qa="first_name"]')
    LASTNAME_INPUT = (By.CSS_SELECTOR, '[data-qa="last_name"]')
    ADDRESS_INPUT = (By.CSS_SELECTOR, '[data-qa="address"]')
    COUNTRY_SELECT = (By.CSS_SELECTOR, '[data-qa="country"]')
    STATE_INPUT = (By.CSS_SELECTOR, '[data-qa="state"]')
    CITY_INPUT = (By.CSS_SELECTOR, '[data-qa="city"]')
    ZIPCODE_INPUT = (By.CSS_SELECTOR, '[data-qa="zipcode"]')
    MOBILE_INPUT = (By.CSS_SELECTOR, '[data-qa="mobile_number"]')
    CREATE_ACCOUNT_BTN = (By.CSS_SELECTOR, '[data-qa="create-account"]')
    ACCOUNT_CREATED_MSG = (By.CSS_SELECTOR, '[data-qa="account-created"]')
    ERROR_EMAIL_ALREADY_EXISTS = (By.XPATH,'//p[text()="Email Address already exist!"]')

    @allure.step("Открытие страница логина/регистрации")
    def open_login_signup_page(self):
        self.logger.info(
            f"{self.class_name}: Open page {self.browser.base_url + '/login'}"
        )

        self.browser.get(self.browser.base_url + "/login")
        return self

    def start_signup(self, name, email):
        """Вводим имя и email на первой форме"""
        self.logger.info(f"Старт регистрации: {name}, {email}")
        self.input_value(self.SIGNUP_NAME, name)
        self.input_value(self.SIGNUP_EMAIL, email)
        self.click_element(self.SIGNUP_BTN)


    def complete_signup(self, user_data: dict):
        """Заполняем полную форму регистрации"""
        self.logger.info("Заполняем форму регистрации")
        self.input_value(self.PASSWORD_INPUT, user_data["password"])
        self.input_value(self.FIRSTNAME_INPUT, user_data["firstname"])
        self.input_value(self.LASTNAME_INPUT, user_data["lastname"])
        self.input_value(self.ADDRESS_INPUT, user_data["address"])
        self.select_by_text(self.COUNTRY_SELECT, user_data["country"])
        self.input_value(self.STATE_INPUT, user_data["state"])
        self.input_value(self.CITY_INPUT, user_data["city"])
        self.input_value(self.ZIPCODE_INPUT, user_data["zipcode"])
        self.input_value(self.MOBILE_INPUT, user_data["mobile"])
        self.click_element(self.CREATE_ACCOUNT_BTN)

    def is_signed_up(self):
        time.sleep(1)
        """Проверка, что аккаунт создан"""
        element = self.get_element(self.ACCOUNT_CREATED_MSG)  # ждёт появления через WebDriverWait
        return element.is_displayed()

    def is_email_already_exists_error_visible(self) -> bool:
        """Проверка, что появилась ошибка существующего email"""

        element = self.get_element(self.ERROR_EMAIL_ALREADY_EXISTS)
        return element.is_displayed()
