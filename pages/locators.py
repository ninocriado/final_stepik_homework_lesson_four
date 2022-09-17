from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_BUTTON = (By.ID, "login_link")
    EMAIL_REGISTRATION = (By.NAME, "registration-email")
    PASSWORD1_REGISTRATION = (By.NAME, "registration-password1")
    PASSWORD2_REGISTRATION = (By.NAME, "registration-password2")
    BUTTON_REGISTRATION = (By.NAME, "registration_submit")
    EMAIL_LOGIN = (By.NAME, "login-username")
    PASSWORD_LOGIN = (By.NAME, "login-password")
    LOGIN_SUBMIT = (By.NAME, "login_submit")