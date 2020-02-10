from .base_page import BasePage
from .locators import CartPageLocators
import pickle


class CartPage(BasePage):
    def select_all_product(self, count_products):
        self.should_be_product_on_cart_page()
        products = self.browser.find_elements(*CartPageLocators.CART_POSITIONS)
        assert len(products) == count_products, f"On Cart page not {count_products} products"

    def get_cart_cookies(self):
        pickle.dump(self.browser.get_cookies(), open("cookies.pkl","wb"))

    def should_be_product_on_cart_page(self):
        assert self.is_element_present(*CartPageLocators.CART_POSITIONS), "Product is not presented on Cart page"
