from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_card(self):
        btn = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        btn.click()
        self.solve_quiz_and_get_code()
    
    def should_be_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        result_product_name = self.browser.find_element(*ProductPageLocators.RESULT_PRODUCT_NAME)
        assert product_name.text == result_product_name.text, "name doesn't match"

    def should_be_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        result_product_price = self.browser.find_element(*ProductPageLocators.RESULT_PRODUCT_PRICE)
        assert product_price.text == result_product_price.text, "price doesn't match"
