from selenium.webdriver.common.by import By
class Registration:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://www.saucedemo.com/')
        self._driver.implicitly_wait(10)
        self._driver.maximize_window()

    def registr(self, term, term_1):
        Username = self._driver.find_element(By.CSS_SELECTOR, 'input#user-name.input_error.form_input')
        Username.clear()
        Username.send_keys(term)

        Password = self._driver.find_element(By.CSS_SELECTOR, 'input#password.input_error.form_input')
        Password.clear()
        Password.send_keys(term_1)
        self._driver.find_element(By.CSS_SELECTOR, 'input[class="submit-button btn_action"]').click()