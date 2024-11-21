from selenium.webdriver.common.by import By
class MainPage:
    def __init__(self, browser):
        self._driver = browser

    def add(self):
        self._driver.find_element(By.CSS_SELECTOR, 'button[name="add-to-cart-sauce-labs-backpack"]').click()
        self._driver.find_element(By.CSS_SELECTOR, 'button[name="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        self._driver.find_element(By.CSS_SELECTOR, 'button[name="add-to-cart-sauce-labs-onesie"]').click()

        self._driver.find_element(By.CSS_SELECTOR, 'a[class=shopping_cart_link]').click()
        self._driver.find_element(By.CSS_SELECTOR, 'button#checkout.btn.btn_action.btn_medium.checkout_button ').click()
