from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Calc_page.MainPage import MainPage
import allure


@allure.severity("blocker")
@allure.feature("ASSERT")
@allure.title("Проверить результат сложения 8+7=15")
@allure.description("Заполнить калькулятор значениями") # noqa
def test_calc():
    """Проверка работы калькулятора"""
    with allure.step("Перейти на сайт калькулятора"):
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) # noqa

    with allure.step("Заменить время на {45}"):
        with allure.step("Заполнить поле значениями"):
            main_page = MainPage(browser)
            main_page.time("45")
            main_page.count()
            to_be = main_page.result()

    with allure.step("Сравнить результат с {15}"):
        assert to_be == 15

    with allure.step("Закрыть браузер"):
        browser.quit()
