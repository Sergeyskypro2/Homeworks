from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://ya.ru')
driver.maximize_window()
sleep(3)
driver.minimize_window()
sleep(3)
driver.fullscreen_window()
sleep(3)
driver.set_window_size(700,100)
sleep(5)