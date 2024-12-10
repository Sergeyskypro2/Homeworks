
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def test_form(): 
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
    driver.find_element(By.CSS_SELECTOR, 'input[name=first-name]').send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR, 'input[name=last-name]').send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR, 'input[name=address]').send_keys("Ленина, 55-3")
    driver.find_element(By.CSS_SELECTOR, 'input[name=zip-code]').send_keys("")
    driver.find_element(By.CSS_SELECTOR, 'input[name=city]').send_keys("Москва")
    driver.find_element(By.CSS_SELECTOR, 'input[name=country').send_keys("Россия")
    driver.find_element(By.CSS_SELECTOR, 'input[name=e-mail]').send_keys("test@skypro.com")
    driver.find_element(By.CSS_SELECTOR, 'input[name=phone]').send_keys("+7985899998787")
    driver.find_element(By.CSS_SELECTOR, 'input[name=job-position]').send_keys("QA")
    driver.find_element(By.CSS_SELECTOR, 'input[name=company]').send_keys("SkyPro")

    driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-outline-primary.mt-3').click()

    assert "alert py-2 alert-danger" in driver.find_element(By.CSS_SELECTOR, 'input[name=zip-code]').get_attribute("class")

    driver.quit()
