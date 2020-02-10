from .base_page import BasePage
from .locators import PromoModalLocators

class PromoModalForm(BasePage):
    def should_be_promo_modal(self):
        self.should_be_promo_modal_form()

    def close_promo__modal_form(self):
        self.should_be_promo_modal_form_close_button()
        button = self.browser.find_element(*PromoModalLocators.CLOSE_FORM_BUTTON)
        button.click()

    def close_modal_banner(self):
        button = self.browser.find_element(*PromoModalLocators.CLOSE_BANNER_BUTTON)
        button.click()

    def should_be_promo_modal_form(self):
        assert self.is_element_present(*PromoModalLocators.PROMO_FORM), "Promo modal form is not presented"

    def should_be_promo_modal_form_close_button(self):
        assert self.is_element_present(*PromoModalLocators.CLOSE_FORM_BUTTON), "Close button for promo modal form is not presented"

    def not_should_be_promo_modal_form(self):
        assert self.is_element_present(*PromoModalLocators.PROMO_BANNER), "Promo modal form is presented"
