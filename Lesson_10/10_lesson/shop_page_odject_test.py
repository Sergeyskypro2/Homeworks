from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Shop_pages.Registration import Registration
from Shop_pages.MainPage import MainPage
from Shop_pages.Checkout import Checkout
from Shop_pages.CartPage import CartPage
import allure


@allure.severity("blocker")
@allure.feature("ADD")
@allure.title("Получение финальной суммы товаров")
@allure.description("Авторизоваться с валидными параметрами и проверить финальную цену") # noqa
def test_total():
    """Проверка работы сайта покупки вещей"""
    with allure.step("Перейти на сайт"):
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) # noqa

    with allure.step("Зарегистрироваться на сайте"):
        with allure.step("Заполнить поля логин и пароль {standard_user}:{secret_sauce}"): # noqa
            Username = Registration(browser)
            Username.registr("standard_user", "secret_sauce")

    with allure.step("Выбрать нужные вещи"):
        main_page = MainPage(browser)
        main_page.add()

    with allure.step("Заполнить форму отправки"):
        with allure.step("Заполнить поля имя, фамилия, почтовый индекс {Sergei}:{Shlyapnikov}:{607650}"): # noqa
            info = Checkout(browser)
            info.info("Sergei", "Shlyapnikov", "607650")

    with allure.step("Подтвердить оплату картой"):
        cart_page = CartPage(browser)
        total = cart_page.cart()

    with allure.step("Проверить финальную сумму с 'Total: $58.29'"):
        assert total == "Total: $58.29"

    with allure.step("Закрыть браузер"):
        browser.quit()
