from selenium.webdriver.common.by import By
from page_object.base_page import BasePage


class ProductsPage(BasePage):
    FIRST_PRODUCT_ADD_BUTTON = (By.CSS_SELECTOR, 'a[data-product-id="1"]')
    CART_BUTTON = (By.CSS_SELECTOR, 'a[href="/view_cart"]')
    CART_ITEMS = (By.CSS_SELECTOR, '.cart_info')
    REMOVE_PRODUCT_BTN = (By.CSS_SELECTOR, '.cart_quantity_delete')
    EMPTY_CART_MSG = (By.ID, "empty_cart")

    def open(self):
        self.browser.get("https://automationexercise.com/products")

    def add_first_product_to_cart(self):
        self.click_element(self.FIRST_PRODUCT_ADD_BUTTON)

    def go_to_cart(self):
        self.browser.get("https://automationexercise.com/view_cart")

    def is_product_in_cart(self) -> bool:
        try:
            return len(self.get_elements(self.CART_ITEMS)) > 0
        except:
            return False


    def remove_product_from_cart(self):
        self.click_element(self.REMOVE_PRODUCT_BTN)

    def is_cart_empty(self) -> bool:
        assert self.get_element(self.EMPTY_CART_MSG).is_displayed()