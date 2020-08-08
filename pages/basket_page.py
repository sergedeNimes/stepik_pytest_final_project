from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty_basket(self):
        self.is_not_element_present(*BasketPageLocators.NOT_EMPTY_BASKET), \
                                    "Basket should be empty, but it is not"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), \
                                       "Empty basket message is not presented, but should be"
