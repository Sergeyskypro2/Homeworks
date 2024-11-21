from selenium.webdriver.common.by import By
class CartPage:

    def __init__(self, browser):
        self._driver = browser

    def cart(self):
        total = self._driver.find_element(By.CSS_SELECTOR, 'div[class="summary_total_label"]').text
        print(total)
        return(total)
        