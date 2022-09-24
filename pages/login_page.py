from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url, "Wrong URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_LOGIN), "Wrong login"
        assert self.is_element_present(*LoginPageLocators.PASSWORD_LOGIN),"Wrong password"
        assert self.is_element_present(*LoginPageLocators.LOGIN_SUBMIT), "Wrong login or password"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.EMAIL_REGISTRATION), "Wrong email"
        assert self.is_element_present(*LoginPageLocators.PASSWORD1_REGISTRATION), "Password field is not present"
        assert self.is_element_present(*LoginPageLocators.PASSWORD2_REGISTRATION), "Password field is not present"
        assert self.is_element_present(*LoginPageLocators.BUTTON_REGISTRATION), "Button registration is not present"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.EMAIL_REGISTRATION).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD1_REGISTRATION).send_keys(password)
        self.browser.find_element(*LoginPageLocators.PASSWORD2_REGISTRATION).send_keys(password)
        self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION).click()
