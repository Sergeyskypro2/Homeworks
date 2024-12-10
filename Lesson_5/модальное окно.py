from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

# открыть страницу
driver.get('https://the-internet.herokuapp.com/entry_ad')
sleep(3)

# В модальном окне нажмите на кнопку Сlose
driver.find_element(By.CSS_SELECTOR, 'div[class="modal"]')
driver.find_element(By.CSS_SELECTOR, 'div[class="modal-footer"]').click()
sleep(3)
driver.quit()