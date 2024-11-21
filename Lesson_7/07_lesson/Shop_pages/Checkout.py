from selenium.webdriver.common.by import By
class Checkout:

    def __init__(self, browser):
        self._driver = browser

    def info(self, term1, term2, term3):
        self._driver.find_element(By.CSS_SELECTOR, 'input#first-name.input_error.form_input').send_keys(term1)
        self._driver.find_element(By.CSS_SELECTOR, 'input#last-name.input_error.form_input').send_keys(term2)
        self._driver.find_element(By.CSS_SELECTOR, 'input#postal-code.input_error.form_input').send_keys(term3)
        self._driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()