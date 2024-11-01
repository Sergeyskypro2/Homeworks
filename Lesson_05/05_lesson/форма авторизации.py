from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

# открыть страницу
driver.get('https://the-internet.herokuapp.com/login')

# В поле username введите значение tomsmith
input_1 = driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')
input_1.send_keys("tomsmith")
sleep(3)

# В поле password введите значение SuperSecretPassword!
input_2 = driver.find_element(By.CSS_SELECTOR, 'input[type="password"]')
input_2.send_keys("SuperSecretPassword")
sleep(3)

# Нажмите кнопку Login
driver.find_element(By.CSS_SELECTOR, 'button[class="radius"]').click()
sleep(3)
driver.quit()