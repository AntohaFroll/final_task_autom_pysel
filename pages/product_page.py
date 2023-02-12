from .base_page import BasePage
from .basket_page import BasketPage
from .locators import ProductPageLocators, BasketPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()

    def should_be_product_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.SUCCESS_MESSAGE), \
            "Product not added to basket"

    def find_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return product_name

    def find_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return product_price

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*BasketPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*BasketPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should be"

    def should_match_names(self):
        basket_page = BasketPage(self.browser, url=self.browser.current_url)
        assert self.find_product_name().text == basket_page.find_product_name_in_basket().text, \
            "Wrong product added to basket"

    def should_match_prices(self):
        basket_page = BasketPage(self.browser, url=self.browser.current_url)
        assert self.find_product_price().text == basket_page.find_product_price_in_basket().text, \
            "Wrong product price"
