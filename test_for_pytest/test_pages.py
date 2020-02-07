from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pytest
import pickle
import random


link = 'https://m.ennergiia.com/'


@pytest.fixture
def browser():
    options = Options()
    options.add_argument("window-size=700,1400")
    browser = webdriver.Chrome(options=options)
    browser.get(link)
    yield browser
    browser.quit()


class TestMain():

    #@pytest.mark.test1
    def test_add_to_cart(self, browser):

        # проверяем, что счётчик корзины отсутствует
        WebDriverWait(browser, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "span.notification")))

        browser.implicitly_wait(10)

        #переход в гамбургер-меню
        browser.find_element_by_css_selector('header .hamburger').click()
        #выбор раздела "Дети"
        section = browser.find_element_by_css_selector('ul[data-test="hierarchyRoots"] :nth-child(3)')
        browser.execute_script("arguments[0].click();", section)
        #выбор категории "Школа"
        browser.find_element_by_css_selector('ul[data-test="hierarchyList"] :nth-child(9)').click()
        #выбор подкатегории "Рюкзаки"
        browser.find_element_by_css_selector('ul[data-test="hierarchyList"] :nth-child(4) button').click()

        #поиск и закрытие окна с предложением о скидке
        promo_modal_window = browser.find_element_by_css_selector('section[class="MegaUI__modal-body mindBoxSubscribeModal"]')
        promo_modal_window.find_element_by_css_selector('button.closeModal').click()

        #выбор случайного товара на странице
        products = browser.find_elements_by_css_selector('ul.virtualList li')
        products[random.randint(0, len(products) - 1)].click()

        #добавление товара в корзину
        browser.find_element_by_css_selector('div.MegaUI_button_dark').click()

        #скролл вверх страницы
        browser.execute_script("window.scrollTo(0, -document.body.scrollHeight)")
        #переход в корзину
        cart_page_button = browser.find_element_by_css_selector('ul.rightMenu li[data-test="navCartLink"]')
        cart_page_button.click()

        #поиск элементов в списке товаров в корзине
        cart_positions = browser.find_elements_by_css_selector('ul.cartPositions li')

        #запись cookie в файл 'cookies.pkl'
        pickle.dump(browser.get_cookies(), open("cookies.pkl","wb"))

        #проверка наличия в корзине только 1го товара
        assert len(cart_positions) == 1, f"В корзине не один товар ({len(wishlist_item)})"

    #@pytest.mark.test2
    def test_wishlist(self, browser):

        browser.implicitly_wait(10)

        #переход на страницу гостя
        browser.find_element_by_css_selector('ul.rightMenu li[data-test="navProfileLink"]').click()
        #переход в список избранного
        browser.find_element_by_css_selector('ul.list a[href="/wishlist"]').click()
        #проверка отсутствия товаров в избранном
        browser.find_elements_by_css_selector('div.emptyWrapper')
        #переход на главную страницу
        logo_button = browser.find_elements_by_css_selector('a.logoLink')
        logo_button[0].click()

        #переход в гамбургер-меню
        browser.find_element_by_css_selector('header .hamburger').click()
        #выбор случайного раздела
        section = browser.find_elements_by_css_selector('ul[data-test="hierarchyRoots"] li')
        section[random.randint(0, len(section) - 1)].click()
        #выбор случайной категории
        category = browser.find_elements_by_css_selector('ul[data-test="hierarchyList"] li')
        category[random.randint(0, len(category) - 1)].click()
        #выбор случайной подкатегории
        subcategory = browser.find_elements_by_css_selector('ul[data-test="hierarchyList"] li button')
        subcategory[random.randint(0, len(subcategory) - 1)].click()

        #поиск и закрытие окна с предложением о скидке
        promo_modal_window = browser.find_element_by_css_selector('section[class="MegaUI__modal-body mindBoxSubscribeModal"]')
        promo_modal_window.find_element_by_css_selector('button.closeModal').click()

        #выбор случайного товара на странице
        products = browser.find_elements_by_css_selector('ul.virtualList li')
        products[random.randint(0, len(products) - 1)].click()

        #добавление товара в избранное
        browser.find_element_by_css_selector('div.wishListButtonWrapper button[data-test="wishListAddButton"]').click()

        #скролл вверх страницы
        browser.execute_script("window.scrollTo(0, -document.body.scrollHeight)")
        #переход на страницу гостя
        browser.find_element_by_css_selector('ul.rightMenu li[data-test="navProfileLink"]').click()
        #переход в список избранного
        browser.find_element_by_css_selector('ul.list a[href="/wishlist"]').click()

        #поиск элементов в списке товаров в корзине
        wishlist_item = browser.find_elements_by_css_selector('ul.list li')

        #проверка наличия в збранном только 1го товара
        assert len(wishlist_item) == 1, f"В избранном не один товар ({len(wishlist_item)})"


    #@pytest.mark.test3
    def test_close_sale_dialogue(self, browser):

        browser.implicitly_wait(10)

        #переход в гамбургер-меню
        browser.find_element_by_css_selector('header .hamburger').click()
        #выбор раздела "Женщины"
        browser.find_element_by_css_selector('ul[data-test="hierarchyRoots"] :nth-child(1)').click()
        #выбор категории "Одежда"
        browser.find_element_by_css_selector('ul[data-test="hierarchyList"] :nth-child(4)').click()
        #выбор подкатегории "Платья"
        browser.find_element_by_css_selector('ul[data-test="hierarchyList"] :nth-child(8) button').click()

        #поиск и закрытие окна с предложением о скидке
        promo_modal_window = browser.find_element_by_css_selector('section[class="MegaUI__modal-body mindBoxSubscribeModal"]')
        browser.find_element_by_css_selector('button.closeModal').click()

        #проверка появления окна с предложением о скидке
        assert promo_modal_window, "Промо-предложение не появилось"
