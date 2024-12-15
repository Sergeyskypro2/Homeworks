from selenium.webdriver.common.by import By


class Checkout:
    """Ввод данных покупателя для оформления заказа"""
    def __init__(self, browser):
        self._driver = browser

    def info(self, term1: str, term2: str, term3: int):
        self._driver.find_element(By.CSS_SELECTOR, 'input#first-name.input_error.form_input').send_keys(term1) # noqa
        """Посик элемента имени"""
        self._driver.find_element(By.CSS_SELECTOR, 'input#last-name.input_error.form_input').send_keys(term2) # noqa
        """Посик элемента фамилия"""
        self._driver.find_element(By.CSS_SELECTOR, 'input#postal-code.input_error.form_input').send_keys(term3) # noqa
        """Посик элемента почтового индекса"""
        self._driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
