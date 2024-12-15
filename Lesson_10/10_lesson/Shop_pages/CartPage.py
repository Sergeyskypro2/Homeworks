from selenium.webdriver.common.by import By


class CartPage:
    """Подтверждение заказа"""
    def __init__(self, browser):
        self._driver = browser

    def cart(self) -> float:
        """Посик элемента финальной суммы"""
        total = self._driver.find_element(By.CSS_SELECTOR, 'div[class="summary_total_label"]').text # noqa
        """Печатает оконательную сумму"""
        print(total)
        return total

