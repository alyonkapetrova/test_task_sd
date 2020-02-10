from .base_page import BasePage
from .locators import MainPageLocators
from .locators import RightMenuLocators
from .locators import LeftMenuLocators
from .locators import CartPageLocators


class MainPage(BasePage):

    def go_to_main_page(self):
        self.should_be_logo_button()
        logo_button = menu = self.browser.find_elements(*MainPageLocators.LOGO_BUTTON)
        logo_button[0].click()

    def go_to_hamburger_menu(self):
        self.should_be_hamburger_menu()
        menu = self.browser.find_element(*RightMenuLocators.HAMBURGER_MENU)
        menu.click()

    def not_notification_on_cart(self):
        assert self.is_not_element_present(*CartPageLocators.NOTIFICATION), "Notification menu is presented"

    def go_to_guest_page(self):
        self.should_be_guest_page_button()
        guest_page = self.browser.find_element(*LeftMenuLocators.GUEST_PAGE_BUTTON)
        guest_page.click()

    def should_be_hamburger_menu(self):
        assert self.is_element_present(*RightMenuLocators.HAMBURGER_MENU), "Hamburger menu is not presented"

    def should_be_guest_page_button(self):
        assert self.is_element_present(*LeftMenuLocators.GUEST_PAGE_BUTTON), "Guest page button is not presented"

    def should_be_logo_button(self):
        assert self.is_element_present(*MainPageLocators.LOGO_BUTTON), "Logo button is not presented"
