from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class BasePage:
    def __init__(self, browser, wait=3):
        self.browser = browser
        self.wait = WebDriverWait(browser, wait)
        self.actions = ActionChains(browser)
        self.logger = browser.logger
        self.class_name = type(self).__name__

    def is_element_visible(self, locator, timeout=5):
        self.logger.debug(
            "%s: Check if element %s is present" % (self.class_name, str(locator))
        )

        return WebDriverWait(self.browser, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def is_elements_visible(self, locators, timeout=5):
        for locator in locators:
            self.logger.debug(
                "%s: Check if element %s is present" % (self.class_name, str(locator))
            )
            self.is_element_visible(locator, timeout)

    def get_element(self, locator):
        self.logger.debug(
            "%s: Check if element %s is present" % (self.class_name, str(locator))
        )
        return self.is_element_visible(locator)

    def get_elements(self, locator):
        self.logger.debug(
            "%s: Check if element %s is present" % (self.class_name, str(locator))
        )
        return WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located(locator)
        )

    def click_element(self, locator):
        self.logger.debug("%s: Clicking element: %s" % (self.class_name, str(locator)))
        ActionChains(self.browser).move_to_element(self.get_element(locator)).pause(
            0.3
        ).click().perform()

    def input_value(self, locator: tuple, text: str):
        self.logger.debug("%s: Input %s in input %s" % (self.class_name, text, locator))
        self.click_element(locator)
        self.get_element(locator).clear()
        for i in text:
            self.get_element(locator).send_keys(i)

    def select_by_text(self, locator, text: str):
        self.logger.debug(
            "%s: Select option '%s' in dropdown %s" % (self.class_name, text, locator)
        )
        element = self.get_element(locator)
        Select(element).select_by_visible_text(text)
