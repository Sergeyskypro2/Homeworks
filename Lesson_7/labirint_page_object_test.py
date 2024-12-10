from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.CartPage import CartPage
from pages.MainPage import MainPage
from pages.ResultPage import ResultPage

def test_card_counter():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    main_page = MainPage(browser)
    main_page.set_cookie_policy()
    main_page.search('python')

    result_page = ResultPage(browser)
    to_be = result_page.add_books()

    cart_page = CartPage(browser)
    cart_page.get()
    as_is = cart_page.get_counter()

    assert as_is == to_be
    browser.quit()

def test_empty_search_result():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    main_page = MainPage(browser)
    main_page.set_cookie_policy()
    main_page.search('no book search term')

    result_page = ResultPage(browser)
    msg = result_page.get_empty_result_messeage()

    assert msg == "Все, что мы нашли в Лабиринте по запросу «no book search term»"
    browser.quit()
