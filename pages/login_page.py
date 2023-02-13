import time
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()).split(".")[0]
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_FIELD).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_FIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD_FIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER).click()

    def should_be_login_form(self):
        self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        self.browser.current_url.find("login"), "'Login' is not in url"
        assert True

    def should_be_register_form(self):
        self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        assert True
