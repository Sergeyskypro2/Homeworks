from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

# открыть страницу
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

# Пять раз кликните на кнопку Add Element
for _ in range(5):
    driver.find_element(By.CSS_SELECTOR, 'button[onclick="addElement()"]').click()
    sleep(1)

#Соберите со страницы список кнопок Delete.
buttons = driver.find_elements(By.CSS_SELECTOR, 'button[class="added-manually"]')
print(f"Количество кнопок Delete: {len(buttons)}")
sleep(3)
driver.quit()