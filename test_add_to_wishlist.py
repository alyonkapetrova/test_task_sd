from .pages.main_page import MainPage
from .pages.right_menu import HamburgerMenu
from .pages.promo_modal import PromoModalForm
from .pages.catalog_page import CatalogPage
from .pages.product_page import ProductPage
from .pages.left_menu import LeftMenu
from .pages.guest_page import GuestPage
from .pages.wishlist_page import WishlistPage


link = "https://m.ennergiia.com/"

def test_guest_can_close_promo_modal(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_guest_page()
    guest = GuestPage(browser, browser.current_url)
    guest.go_to_wishlist()
    wishlist = WishlistPage(browser, browser.current_url)
    wishlist.check_no_elements()
    page.go_to_main_page()
    page.go_to_hamburger_menu()
    r_menu = HamburgerMenu(browser, browser.current_url)
    r_menu.go_to_random_section()
    r_menu.go_to_random_category()
    r_menu.go_to_random_category()
    promo = PromoModalForm(browser, browser.current_url)
    promo.should_be_promo_modal()
    promo.close_promo__modal_form()
    promo.close_modal_banner()
    catalog_item = CatalogPage(browser, browser.current_url)
    catalog_item.select_random_product()
    product = ProductPage(browser, browser.current_url)
    product.add_to_wishlist()
    l_menu = LeftMenu(browser, browser.current_url)
    l_menu.go_to_guest()
    guest.go_to_wishlist()
    wishlist.select_all_product(1) #переменная для проверки нужного количества товаров в избранном
