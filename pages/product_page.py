import time

from .locators import ProductPageLocators
from .base_page import BasePage

class ProductPage(BasePage):
    def button_add_basket(self):
        time.sleep(10)
        self.browser.find_element(*ProductPageLocators.BASKET_BUTTON).click()
        #self.solve_quiz_and_get_code()
        time.sleep(10)
    def should_be_price_on_the_page(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        assert book_price, "Price is not present"
        book_price_basket = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_IN_BASKET)
        assert book_price_basket, "Price in basket is not present"
        assert book_price.text == book_price_basket.text, "Price not matched"

    def should_be_name_on_the_page(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        assert book_name, "Book name is not present"
        book_name_basket = self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_BASKET)
        assert book_name_basket, "Book name in basket is not present"
        assert book_name.text == book_name_basket.text, "Book name not matched"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"