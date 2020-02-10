from .base_page import BasePage
from .locators import CatalogPageLocators
import random

class CatalogPage(BasePage):
    def select_random_product(self):
        self.should_be_product_on_page()
        products = self.browser.find_elements(*CatalogPageLocators.ALL_PRODUCTS_ON_PAGE)
        products[random.randint(0, len(products) - 1)].click()

    def should_be_product_on_page(self):
        assert self.is_element_present(*CatalogPageLocators.ALL_PRODUCTS_ON_PAGE), "Product in catalog is not presented"
