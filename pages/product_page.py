from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        self.should_be_add_basket_button()
        add_basket_button = self.browser.find_element(*ProductPageLocators.ADD_BASKET_BUTTON)
        add_basket_button.click()

    def should_be_add_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BASKET_BUTTON), "Add basket button is not presented"

    def should_be_product_in_basket(self):
        self.should_be_basket_messages()
        self.should_be_product_name_in_basket_message()
        self.should_be_product_price_in_cost_basket_message()

    def should_be_basket_messages(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_MESSAGES), "Basket messages are not presented"

    def should_be_product_name_in_basket_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_message = self.browser.find_element(*ProductPageLocators.PRODUCT_MESSAGE).text
        assert product_name == product_message, "Product name in basket message is not presented"

    def should_be_product_price_in_cost_basket_message(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        cost_message = self.browser.find_element(*ProductPageLocators.COST_MESSAGE).text
        assert product_price == cost_message, "Product price in cost basket message is not presented"
