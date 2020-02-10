from .pages.main_page import MainPage
from .pages.right_menu import HamburgerMenu
from .pages.promo_modal import PromoModalForm
from .pages.catalog_page import CatalogPage
from .pages.product_page import ProductPage
from .pages.left_menu import LeftMenu
from .pages.cart_page import CartPage


link = "https://m.ennergiia.com/"

def test_guest_can_close_promo_modal(browser):
    page = MainPage(browser, link)
    page.open()
    page.not_notification_on_cart()
    page.go_to_hamburger_menu()
    r_menu = HamburgerMenu(browser, browser.current_url)
    r_menu.go_to_women_section()
    r_menu.go_to_present_category()
    r_menu.go_to_beauty_subcategory()
    promo = PromoModalForm(browser, browser.current_url)
    promo.should_be_promo_modal()
    promo.close_promo__modal_form()
    promo.close_modal_banner()
    catalog_item = CatalogPage(browser, browser.current_url)
    catalog_item.select_random_product()
    product = ProductPage(browser, browser.current_url)
    product.add_to_cart()
    l_menu = LeftMenu(browser, browser.current_url)
    l_menu.go_to_cart()
    cart = CartPage(browser, browser.current_url)
    cart.select_all_product(1) #переменная для проверки нужного количества товаров в корзине
    cart.get_cart_cookies()
