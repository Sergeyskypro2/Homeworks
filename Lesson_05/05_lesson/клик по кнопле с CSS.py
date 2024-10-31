from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

# открыть страницу
driver.get("http://uitestingplayground.com/classattr")

# кликнуть на синию кнопку
button = driver.find_element(By.CSS_SELECTOR, '[class="btn class3 btn-primary btn-test"]').click()
sleep(10)
button.click()



