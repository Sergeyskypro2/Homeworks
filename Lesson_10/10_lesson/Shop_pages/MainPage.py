from selenium.webdriver.common.by import By


class MainPage:
    """Выбор товара и добавление в корзину"""
    def __init__(self, browser):
        self._driver = browser

    def add(self):
        """Посик элемента товара"""
        self._driver.find_element(By.CSS_SELECTOR, 'button[name="add-to-cart-sauce-labs-backpack"]').click() # noqa
        """Посик элемента товара"""
        self._driver.find_element(By.CSS_SELECTOR, 'button[name="add-to-cart-sauce-labs-bolt-t-shirt"]').click() # noqa
        """Посик элемента товара"""
        self._driver.find_element(By.CSS_SELECTOR, 'button[name="add-to-cart-sauce-labs-onesie"]').click() # noqa

        self._driver.find_element(By.CSS_SELECTOR, 'a[class=shopping_cart_link]').click() # noqa
        self._driver.find_element(By.CSS_SELECTOR, 'button#checkout.btn.btn_action.btn_medium.checkout_button ').click() # noqa
