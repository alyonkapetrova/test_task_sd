from .base_page import BasePage
from .locators import RightMenuLocators
import random


class HamburgerMenu(BasePage):
    def go_to_women_section(self):
        self.should_be_section()
        section = self.browser.find_element(*RightMenuLocators.WOMEN_SECTION)
        section.click()

    def go_to_clothes_category(self):
        self.should_be_category()
        category = self.browser.find_element(*RightMenuLocators.CLOTHES_CATEGORY)
        category.click()

    def go_to_present_category(self):
        self.should_be_category()
        category = self.browser.find_element(*RightMenuLocators.PRESENT_CATEGORY)
        category.click()

    def go_to_dresses_subcategory(self):
        self.should_be_subcategory()
        subcategory = self.browser.find_element(*RightMenuLocators.DRESSES_SUBCATEGORY)
        subcategory.click()

    def go_to_beauty_subcategory(self):
        self.should_be_subcategory()
        subcategory = self.browser.find_element(*RightMenuLocators.BEAUTY_SUBCATEGORY)
        subcategory.click()

    def go_to_random_section(self):
        self.should_be_section()
        section = self.browser.find_elements(*RightMenuLocators.RANDOM_SECTION)
        section[random.randint(0, len(section) - 1)].click()

    def go_to_random_category(self):
        self.should_be_category()
        category = self.browser.find_elements(*RightMenuLocators.RANDOM_CATEGORY)
        category[random.randint(0, len(category) - 1)].click()

    def go_to_random_subcategory(self):
        self.should_be_subcategory()
        subcategory = self.browser.find_element(*RightMenuLocators.RAND_CATEGORY_SUBCATEGORY)
        subcategory[random.randint(0, len(subcategory) - 1)].click()


    def should_be_section(self):
        assert self.is_element_present(*RightMenuLocators.SECTION), "Section items is not presented"

    def should_be_category(self):
        assert self.is_element_present(*RightMenuLocators.CATEGORY), "Category items is not presented"

    def should_be_subcategory(self):
        assert self.is_element_present(*RightMenuLocators.SUBCATEGORY), "Subcategory items is not presented"
