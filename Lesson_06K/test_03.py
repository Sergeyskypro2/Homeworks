import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://www.saucedemo.com/')

Username = driver.find_element(By.CSS_SELECTOR, 'input#user-name.input_error.form_input')
Username.clear()
Username.send_keys("standard_user")

Password = driver.find_element(By.CSS_SELECTOR, 'input#password.input_error.form_input')
Password.clear()
Password.send_keys("secret_sauce")
driver.find_element(By.CSS_SELECTOR, 'input[class="submit-button btn_action"]').click()

driver.find_element(By.CSS_SELECTOR, 'button[name="add-to-cart-sauce-labs-backpack"]').click()
driver.find_element(By.CSS_SELECTOR, 'button[name="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
driver.find_element(By.CSS_SELECTOR, 'button[name="add-to-cart-sauce-labs-onesie"]').click()

driver.find_element(By.CSS_SELECTOR, 'a[class=shopping_cart_link]').click()
driver.find_element(By.CSS_SELECTOR, 'button#checkout.btn.btn_action.btn_medium.checkout_button ').click()

firstname = driver.find_element(By.CSS_SELECTOR, 'input#first-name.input_error.form_input')
firstname.clear()
firstname.send_keys("Sergei")

lastname = driver.find_element(By.CSS_SELECTOR, 'input#last-name.input_error.form_input')
lastname.clear()
lastname.send_keys("Shliapnikov")

postalcode = driver.find_element(By.CSS_SELECTOR, 'input#postal-code.input_error.form_input')
postalcode.clear()
postalcode.send_keys("607650")

driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

total = driver.find_element(By.CSS_SELECTOR, 'div[class="summary_total_label"]').text
print(total)

def test():
    assert total == "Total: $58.29"

driver.quit()

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.get('https://www.saucedemo.com/')

# Username = driver.find_element(By.CSS_SELECTOR, 'input#user-name.input_error.form_input')
# Username.clear()
# Username.send_keys("standard_user")

# Password = driver.find_element(By.CSS_SELECTOR, 'input#password.input_error.form_input')
# Password.clear()
# Password.send_keys("secret_sauce")
# driver.find_element(By.CSS_SELECTOR, 'input[class="submit-button btn_action"]').click()

# driver.find_element(By.CSS_SELECTOR, 'a[class=shopping_cart_link]').click()

# driver.find_element(By.CSS_SELECTOR, 'button#checkout.btn.btn_action.btn_medium.checkout_button ').click()

# firstname = driver.find_element(By.CSS_SELECTOR, 'input#first-name.input_error.form_input')
# firstname.clear()
# firstname.send_keys("Sergei")

# lastname = driver.find_element(By.CSS_SELECTOR, 'input#last-name.input_error.form_input')
# lastname.clear()
# lastname.send_keys("Shliapnikov")

# postalcode = driver.find_element(By.CSS_SELECTOR, 'input#postal-code.input_error.form_input')
# postalcode.clear()
# postalcode.send_keys("607650")

# driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

# total = driver.find_element(By.CSS_SELECTOR, 'div[class="summary_total_label"]').text
# print(total)

# def test():
#     assert total == "Total: $58.29"

# driver.quit()