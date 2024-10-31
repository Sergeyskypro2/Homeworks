from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

# открыть страницу
driver.get("http://uitestingplayground.com/dynamicid")

# кликнуть на кнопку
button = driver.find_element(By.CSS_SELECTOR, '[id="3ec09a99-b3cb-6dce-9fb7-a06c83971a1d"]').click()
button.click()
