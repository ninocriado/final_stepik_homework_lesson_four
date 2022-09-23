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

class ProductPageLocators():
    BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    BOOK_NAME = (By.TAG_NAME, "h1")
    BOOK_PRICE = (By.CLASS_NAME, "price_color")
    BOOK_PRICE_IN_BASKET = (By.CLASS_NAME, "visible-xs-inline-block")
    BOOK_NAME_IN_BASKET = (By.CSS_SELECTOR, "[id='messages']>div:nth-child(1)>div>strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "[id='messages']>div:nth-child(1)")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

