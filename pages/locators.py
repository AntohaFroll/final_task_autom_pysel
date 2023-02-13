from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.XPATH, '//a[@id="login_link"]')
    LOGIN_LINK_INVALID = (By.XPATH, '//a[@id="login_link_inc"]')
    BASKET_LINK = (By.XPATH, '//a[@class="btn btn-default"]')
    USER_ICON = (By.XPATH, '//i[@class="icon-user"]')


class MainPageLocators:
    LOGIN_LINK = (By.XPATH, '//a[@id="login_link"]')


class LoginPageLocators:
    LOGIN_FORM = (By.XPATH, '//form[@id="login_form"]')
    REGISTER_FORM = (By.XPATH, '//form[@id="register_form"]')
    REGISTER_EMAIL_FIELD = (By.XPATH, '//input[@name="registration-email"]')
    REGISTER_PASSWORD_FIELD = (By.XPATH, '//input[@name="registration-password1"]')
    REGISTER_CONFIRM_PASSWORD_FIELD = (By.XPATH, '//input[@name="registration-password2"]')
    BUTTON_REGISTER = (By.XPATH, '//button[@name="registration_submit"]')


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.XPATH, '//button[contains(@class, "btn-add-to-basket")]')
    PRODUCT_NAME = (By.XPATH, '//div[@class="col-sm-6 product_main"]/h1')
    PRODUCT_PRICE = (By.XPATH, '//div[@class="col-sm-6 product_main"]/p[@class="price_color"]')


class BasketPageLocators:
    SUCCESS_MESSAGE = (By.XPATH, '//div[@class="alert alert-safe alert-noicon alert-success  fade in"]')
    PRODUCT_NAME_IN_BASKET = (By.XPATH, '//div[@class="alertinner "]/strong')
    PRODUCT_PRICE_IN_BASKET = (By.XPATH, '//div[@class="alertinner "]/p/strong')
    BASKET_IS_EMPTY = (By.XPATH, '//div[@id="content_inner"]/p')
