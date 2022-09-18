import time

from .locators import ProductPageLocators
from .base_page import BasePage

class ProductPage(BasePage):
    def button_add_basket(self):
        time.sleep(10)
        self.browser.find_element(*ProductPageLocators.BASKET_BUTTON).click()
        self.solve_quiz_and_get_code()
        time.sleep(10)