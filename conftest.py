import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def browser(request):
    options = Options()
    #options.add_argument('headless')
    options.add_argument("window-size=375,812") #iphon 11 screen size
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
