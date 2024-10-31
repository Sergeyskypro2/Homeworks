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

# пять раз кликнуть на кнопку
for button in range(5):
    button = driver.find_element(By.CSS_SELECTOR, "[onclick='addElement()']").click()
    
#Соберите со страницы список кнопок Delete.
    buttons = driver.find_element(By.CSS_SELECTOR, "[onclick='deleteElement()']")

    print(f"ррр:{buttons}")

sleep(0)

