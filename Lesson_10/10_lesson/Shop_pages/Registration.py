from selenium.webdriver.common.by import By


class Registration:
    """Авторизация с логином и паролем"""
    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://www.saucedemo.com/')
        self._driver.implicitly_wait(10)
        self._driver.maximize_window()

    def registr(self, term: str, term_1: str):
        """Посик элемента логина"""
        Username = self._driver.find_element(By.CSS_SELECTOR, 'input#user-name.input_error.form_input') # noqa
        """Удаление пустой строчки"""
        Username.clear()
        """Ввод логина"""
        Username.send_keys(term)

        """Посик элемента пароля"""
        Password = self._driver.find_element(By.CSS_SELECTOR, 'input#password.input_error.form_input') # noqa
        """Удаление пустой строчки"""
        Password.clear()
        """Ввод пароля"""
        Password.send_keys(term_1)

        self._driver.find_element(By.CSS_SELECTOR, 'input[class="submit-button btn_action"]').click() # noqa
