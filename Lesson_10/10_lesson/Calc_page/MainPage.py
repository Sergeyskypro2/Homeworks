from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    """Ввод данный на калькуляторе"""
    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html') # noqa
        self._driver.implicitly_wait(10)
        self._driver.maximize_window()

    def time(self, term: int):
        """Найти нужный элемент"""
        time = self._driver.find_element(By.CSS_SELECTOR, 'input#delay')
        """Удаление последнего значения"""
        time.clear()
        """Запись нового значения"""
        time.send_keys(term)

    def count(self):
        """Найти и нажать на необходимые элементы"""
        self._driver.find_element(By.XPATH, "//span[text()='7']").click()
        self._driver.find_element(By.XPATH, "//span[text()='+']").click()
        self._driver.find_element(By.XPATH, "//span[text()='8']").click()
        self._driver.find_element(By.XPATH, "//span[text()='=']").click()

        WebDriverWait(self._driver, 50, 0.5).until(EC.text_to_be_present_in_element(( By.CSS_SELECTOR, ".screen"), "15")) # noqa

    def result(self) -> int:
        """Поиск элемента ответа"""
        res = self._driver.find_element(By.CSS_SELECTOR, ".screen").text
        return int(res)

