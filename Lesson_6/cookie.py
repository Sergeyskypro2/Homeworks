from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
my_ccokie = {
    'name': 'cookie_policy',
    'value': '1'
}

driver.get('https://labirint.ru')
driver.add_cookie(my_ccokie)

cookie = driver.get_cookie("PHPSESSID")
cookies = driver.get_cookies()


#driver.refresh()
driver.delete_all_cookies()


driver.quit()