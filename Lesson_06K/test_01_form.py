import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

input_1 = driver.find_element(By.CSS_SELECTOR, 'input[name=first-name]')
input_1.send_keys("Иван")

input_2 = driver.find_element(By.CSS_SELECTOR, 'input[name=last-name]')
input_2.send_keys("Петров")

input_3 = driver.find_element(By.CSS_SELECTOR, 'input[name=address]')
input_3.send_keys("Ленина, 55-3")

input_4 = driver.find_element(By.CSS_SELECTOR, 'input[name=zip-code]')
input_4.send_keys("")

input_4 = driver.find_element(By.CSS_SELECTOR, 'input[name=city]')
input_4.send_keys("Москва")

input_5 = driver.find_element(By.CSS_SELECTOR, 'input[name=country')
input_5.send_keys("Россия")

input_6 = driver.find_element(By.CSS_SELECTOR, 'input[name=e-mail]')
input_6.send_keys("test@skypro.com")

input_7 = driver.find_element(By.CSS_SELECTOR, 'input[name=phone]')
input_7.send_keys("+7985899998787")

input_8 = driver.find_element(By.CSS_SELECTOR, 'input[name=job-position]')
input_8.send_keys("QA")

input_9 = driver.find_element(By.CSS_SELECTOR, 'input[name=company]')
input_9.send_keys("SkyPro")

driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-outline-primary.mt-3').click()

color = driver.find_element(By.CSS_SELECTOR, 'input[name=zip-code]').value_of_css_property("color")
print(color)

driver.quit()