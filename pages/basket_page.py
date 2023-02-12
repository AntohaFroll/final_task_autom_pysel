from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def find_product_name_in_basket(self):
        product_name_in_basket = self.browser.find_elements(*BasketPageLocators.PRODUCT_NAME_IN_BASKET)[0]
        return product_name_in_basket

    def find_product_price_in_basket(self):
        product_price_in_basket = self.browser.find_element(*BasketPageLocators.PRODUCT_PRICE_IN_BASKET)
        return product_price_in_basket
