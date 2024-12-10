from selenium.webdriver.common.by import By
class ResultPage:
    def __init__(self, browser):
        self._driver = browser
        self._driver.execute_script("document.body.style.zoom='80%'")

    def add_books(self):
        buy_buttons = self._driver.find_elements(By.CSS_SELECTOR, "._btn.btn-tocart.buy-link")
        counter = 0
        for btn in buy_buttons:
            btn.click()
            counter += 1
        return counter
    
    def get_empty_result_messeage(self):
        div = self._driver.find_element(By.CSS_SELECTOR, 'div[class="index-top-title-outer"]')
        h1 = div.find_element(By.CSS_SELECTOR, "h1")
        return h1.text