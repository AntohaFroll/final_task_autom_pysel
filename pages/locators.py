from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.XPATH, '//a[@id="login_link"]')


class LoginPageLocators:
    LOGIN_FORM = (By.XPATH, '//form[@id="login_form"]')
    REGISTER_FORM = (By.XPATH, '//form[@id="register_form"]')


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.XPATH, '//button[contains(@class, "btn-add-to-basket")]')
    ADDED_FORM_IN_BASKET = (By.XPATH, '//div[@id="messages"]')
    PRODUCT_NAME = (By.XPATH, '//div[@class="col-sm-6 product_main"]/h1')
    PRODUCT_PRICE = (By.XPATH, '//div[@class="col-sm-6 product_main"]/p[@class="price_color"]')
    PRODUCT_NAME_IN_BASKET = (By.XPATH, '//div[@class="alertinner "]')
    PRODUCT_PRICE_IN_BASKET = (By.XPATH, '//div[@class="basket-mini pull-right hidden-xs"]/strong')
