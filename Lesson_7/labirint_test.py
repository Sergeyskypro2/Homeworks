from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

cookie = {"name": "cookie_policy", "value": "1"}

def test_card_counter():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Перейти на сайт «Лабиринта»
    browser.get("https://www.labirint.ru/")
    browser.implicitly_wait(10)
    browser.maximize_window()
    browser.add_cookie(cookie)

    # Найти все книги по слову Python
    browser.find_element(By.CSS_SELECTOR, "#search-field").send_keys("python")
    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    
    # Добавить все книги в корзину и посчитать
    buy_buttons = browser.find_elements(By.CSS_SELECTOR, "._btn.btn-tocart.buy-link")
    counter = 0
    for btn in buy_buttons:
        btn.click()
        counter += 1
       
    # Перейти в корзину
    browser.get("https://www.labirint.ru/cart/")

    # Проверить счетчик товаров
    txt = browser.find_element(
        By.CSS_SELECTOR, '[class="b-header-b-personal-e-icon-count-m-cart basket-in-cart-a j-cart-count"]').text
      
    # Сравнить c counter
    assert counter == int(txt)
    browser.quit()
  