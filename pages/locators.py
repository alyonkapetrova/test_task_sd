from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGO_BUTTON = (By.CSS_SELECTOR, 'a.logoLink')

class RightMenuLocators():
    HAMBURGER_MENU = (By.CSS_SELECTOR, 'header .hamburger')
    SECTION = (By.CSS_SELECTOR, 'ul[data-test="hierarchyRoots"]')
    CATEGORY = (By.CSS_SELECTOR, 'ul[data-test="hierarchyList"]')
    SUBCATEGORY = (By.CSS_SELECTOR, 'ul[data-test="hierarchyList"] button')
    WOMEN_SECTION = (By.CSS_SELECTOR, 'ul[data-test="hierarchyRoots"] :nth-child(1)')
    CLOTHES_CATEGORY = (By.CSS_SELECTOR, 'ul[data-test="hierarchyList"] :nth-child(4)')
    DRESSES_SUBCATEGORY = (By.CSS_SELECTOR, 'ul[data-test="hierarchyList"] :nth-child(8) button')
    PRESENT_CATEGORY = (By.CSS_SELECTOR, 'ul[data-test="hierarchyList"] :nth-child(1)')
    BEAUTY_SUBCATEGORY = (By.CSS_SELECTOR, 'ul[data-test="hierarchyList"] :nth-child(2) button')
    RANDOM_SECTION = (By.CSS_SELECTOR, 'ul[data-test="hierarchyRoots"] li')
    RANDOM_CATEGORY = (By.CSS_SELECTOR, 'ul[data-test="hierarchyList"]  li')
    RANDOM_SUBCATEGORY = (By.CSS_SELECTOR, 'ul[data-test="hierarchyList"] li button')

class LeftMenuLocators():
    CART_PAGE_BUTTON = (By.CSS_SELECTOR, 'ul.rightMenu li[data-test="navCartLink"]')
    GUEST_PAGE_BUTTON = (By.CSS_SELECTOR, 'ul.rightMenu li[data-test="navProfileLink"]')

class CartPageLocators():
    CART_POSITIONS = (By.CSS_SELECTOR, 'ul.cartPositions li')
    NOTIFICATION = (By.CSS_SELECTOR, 'span.notification')

class GuestPageLocators():
    WISHLIST = (By.CSS_SELECTOR, 'ul.list a[href="/wishlist"]')

class WishlistPageLocators():
    EMPTY_ELEMENTS = (By.CSS_SELECTOR, 'div.emptyWrapper')
    WISHLIST_POSITIONS = (By.CSS_SELECTOR, 'ul.list li')

class CatalogPageLocators():
    ALL_PRODUCTS_ON_PAGE = (By.CSS_SELECTOR, 'ul.virtualList li')

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, 'div.MegaUI_button_dark')
    ADD_TO_WISHLIST_BUTTON = (By.CSS_SELECTOR, 'div.wishListButtonWrapper button[data-test="wishListAddButton"]')

class PromoModalLocators():
    PROMO_FORM = (By.CSS_SELECTOR, 'section[class="MegaUI__modal-body mindBoxSubscribeModal"]')
    PROMO_BANNER = (By.CSS_SELECTOR, 'div.mindBoxSubscribeBanner')
    CLOSE_FORM_BUTTON = (By.CSS_SELECTOR, 'button.closeModal')
    CLOSE_BANNER_BUTTON = (By.CSS_SELECTOR, 'button.closeButton')
