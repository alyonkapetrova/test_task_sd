from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_cart(self):
        product = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        product.click()

    def add_to_wishlist(self):
        product = self.browser.find_element(*ProductPageLocators.ADD_TO_WISHLIST_BUTTON)
        product.click()

    def should_be_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BUTTON), "Add to cart button is not presented on Product page"

    def should_be_guest_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_WISHLIST_BUTTON), "Add to wishlist button is not presented on Product page"
