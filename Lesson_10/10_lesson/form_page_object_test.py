from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from Form_page.MainPage import MainPage
import allure


@allure.severity("blocker")
@allure.feature("ASSERT")
@allure.title("Проверить пустое поле zip-code")
@allure.description("Заполнить таблицу опредененными данными") # noqa
def test_form():
    """Проверка изменения цвета на красный поля 'zip-code'"""
    with allure.step("Перейти на сайт"):
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) # noqa
        main_page = MainPage(browser)

    with allure.step("Заполнить поля данными"):
        main_page.input_first("Иван")
        main_page.input_last("Петров")
        main_page.input_address("Ленина, 55-3")
        main_page.input_zip("")
        main_page.input_city("Москва")
        main_page.input_country("Россия")
        main_page.input_mail("test@skypro.com")
        main_page.input_phone("+7985899998787")
        main_page.input_job("QA")
        main_page.input_company("SkyPro")

    with allure.step("Проверить каждое поле по цвету"):
        assert 'success' in main_page._driver.find_element(By.ID, 'first-name').get_attribute("class") # noqa
        assert 'success' in main_page._driver.find_element(By.ID, 'last-name').get_attribute("class") # noqa
        assert 'success' in main_page._driver.find_element(By.ID, 'address').get_attribute("class") # noqa
        assert 'danger' in main_page._driver.find_element(By.ID, 'zip-code').get_attribute("class") # noqa
        assert 'success' in main_page._driver.find_element(By.ID, 'city').get_attribute("class") # noqa
        assert 'success' in main_page._driver.find_element(By.ID, 'country').get_attribute("class") # noqa
        assert 'success' in main_page._driver.find_element(By.ID, 'e-mail').get_attribute("class") # noqa
        assert 'success' in main_page._driver.find_element(By.ID, 'phone').get_attribute("class") # noqa
        assert 'success' in main_page._driver.find_element(By.ID, 'job-position').get_attribute("class") # noqa
        assert 'success' in main_page._driver.find_element(By.ID, 'company').get_attribute("class") # noqa

    with allure.step("Закрыть браузер"):
        browser.quit()

