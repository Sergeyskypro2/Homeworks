from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


cookie = {"name": "cookie_policy", "value": "1"}

browser = None

def open_labirint():
    # Перейти на сайт «Лабиринта»
    browser.get("https://www.labirint.ru/")
    browser.implicitly_wait(10)
    browser.maximize_window()
    browser.add_cookie(cookie)

def search(term):
    # Найти все книги по слову Python
    browser.find_element(By.CSS_SELECTOR, "#search-field").send_keys(term)
    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

def add_books():
    # Добавить все книги в корзину и посчитать
    buy_buttons = browser.find_elements(By.CSS_SELECTOR, "._btn.btn-tocart.buy-link")
    counter = 0
    for btn in buy_buttons:
        btn.click()
        counter += 1
    return counter

def go_to_cart():
    # Перейти в корзину
    browser.get("https://www.labirint.ru/cart/")

def get_cart_counter():
    # Проверить счетчик товаров
    txt = browser.find_element(By.CSS_SELECTOR, '[class="b-header-b-personal-e-icon-count-m-cart basket-in-cart-a j-cart-count"]').text
    return int(txt)

def close_driver():
    browser.quit()

def test_card_counter():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    open_labirint()
    search('ptyhon')
    added = add_books()
    go_to_cart()
    cart_counter = get_cart_counter()
    close_driver()
    assert added == cart_counter