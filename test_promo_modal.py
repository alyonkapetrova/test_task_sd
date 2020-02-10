from .pages.main_page import MainPage
from .pages.right_menu import HamburgerMenu
from .pages.promo_modal import PromoModalForm


link = "https://m.ennergiia.com/"

def test_guest_can_close_promo_modal(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_hamburger_menu()
    menu = HamburgerMenu(browser, browser.current_url)
    menu.go_to_women_section()
    menu.go_to_clothes_category()
    menu.go_to_dresses_subcategory()
    promo = PromoModalForm(browser, browser.current_url)
    promo.should_be_promo_modal()
    promo.close_promo__modal_form()
    promo.not_should_be_promo_modal_form()
