from .base_page import BasePage
from .locators import GuestPageLocators


class GuestPage(BasePage):
    def go_to_wishlist(self):
        self.should_be_wishlist_button()
        wishlist = self.browser.find_element(*GuestPageLocators.WISHLIST)
        wishlist.click()

    def should_be_wishlist_button(self):
        assert self.is_element_present(*GuestPageLocators.WISHLIST), "Wishlist button is not presented"
