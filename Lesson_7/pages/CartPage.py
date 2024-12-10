from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class CartPage:

    def __init__(self, browser):
        self._driver = browser
        self._driver.execute_script("document.body.style.zoom='80%'")

    def get(self):
        self._driver.get("https://www.labirint.ru/cart/")

    def get_counter(self):
        txt = self._driver.find_element(By.CSS_SELECTOR, '[class="b-header-b-personal-e-icon-count-m-cart basket-in-cart-a j-cart-count"]').text
        return int(txt)
