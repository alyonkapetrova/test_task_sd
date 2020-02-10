from .base_page import BasePage
from .locators import WishlistPageLocators


class WishlistPage(BasePage):
    def check_no_elements(self):
        assert self.is_element_present(*WishlistPageLocators.EMPTY_ELEMENTS), "Wishlist is not empty"

    def select_all_product(self, count_products):
        products = self.browser.find_elements(*WishlistPageLocators.WISHLIST_POSITIONS)
        assert len(products) == count_products, f"On Wishlist page not {count_products} products"
