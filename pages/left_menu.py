from .base_page import BasePage
from .locators import LeftMenuLocators


class LeftMenu(BasePage):
    def go_to_cart(self):
        self.should_be_cart_button()
        self.browser.execute_script("window.scrollTo(0, -document.body.scrollHeight)")
        cart = self.browser.find_element(*LeftMenuLocators.CART_PAGE_BUTTON)
        cart.click()

    def go_to_guest(self):
        self.should_be_guest_button()
        self.browser.execute_script("window.scrollTo(0, -document.body.scrollHeight)")
        guest = self.browser.find_element(*LeftMenuLocators.GUEST_PAGE_BUTTON)
        guest.click()

    def should_be_cart_button(self):
        assert self.is_element_present(*LeftMenuLocators.CART_PAGE_BUTTON), "Cart button is not presented on page"

    def should_be_guest_button(self):
        assert self.is_element_present(*LeftMenuLocators.GUEST_PAGE_BUTTON), "Guest button is not presented on page"
