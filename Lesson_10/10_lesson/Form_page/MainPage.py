from selenium.webdriver.common.by import By


class MainPage:
    """Заполнение таблицы необходимыми значениями"""
    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html') # noqa
        self._driver.implicitly_wait(10)
        self._driver.maximize_window()

    def input_first(self, term: str):
        """Поиск элемента имени"""
        self._driver.find_element(By.CSS_SELECTOR, 'input[name=first-name]').send_keys(term) # noqa

    def input_last(self, term: str):
        """Поиск элемента фамилия"""
        self._driver.find_element(By.CSS_SELECTOR, 'input[name=last-name]').send_keys(term) # noqa

    def input_address(self, term: str):
        """Посик элемента адреса проживания"""
        self._driver.find_element(By.CSS_SELECTOR, 'input[name=address]').send_keys(term) # noqa

    def input_zip(self, term: int):
        """Посик элемента почтового индекса"""
        self._driver.find_element(By.CSS_SELECTOR, 'input[name=zip-code]').send_keys(term) # noqa

    def input_city(self, term: str):
        """Посик элемента города проживания"""
        self._driver.find_element(By.CSS_SELECTOR, 'input[name=city]').send_keys(term) # noqa

    def input_country(self, term: str):
        """Посик элемента страны проживания"""
        self._driver.find_element(By.CSS_SELECTOR, 'input[name=country').send_keys(term) # noqa

    def input_mail(self, term: str):
        """Посик элемента действующей электронной почты"""
        self._driver.find_element(By.CSS_SELECTOR, 'input[name=e-mail]').send_keys(term) # noqa

    def input_phone(self, term: int):
        """Посик элемента номера телефона"""
        self._driver.find_element(By.CSS_SELECTOR, 'input[name=phone]').send_keys(term) # noqa

    def input_job(self, term: str):
        """Посик элемента профессии"""
        self._driver.find_element(By.CSS_SELECTOR, 'input[name=job-position]').send_keys(term) # noqa

    def input_company(self, term: str):
        """Посик элемента компании"""
        self._driver.find_element(By.CSS_SELECTOR, 'input[name=company]').send_keys(term) # noqa

        self._driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-outline-primary.mt-3').click() # noqa

