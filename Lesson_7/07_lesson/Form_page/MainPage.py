from selenium.webdriver.common.by import By
class MainPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
        self._driver.implicitly_wait(10)
        self._driver.maximize_window()

    def input_first(self, term):
        self._driver.find_element(By.CSS_SELECTOR, 'input[name=first-name]').send_keys(term)
    def input_last(self, term):    
        self._driver.find_element(By.CSS_SELECTOR, 'input[name=last-name]').send_keys(term)
    def input_address(self, term): 
        self._driver.find_element(By.CSS_SELECTOR, 'input[name=address]').send_keys(term)
    def input_zip(self, term): 
        self._driver.find_element(By.CSS_SELECTOR, 'input[name=zip-code]').send_keys(term)
    def input_city(self, term): 
        self._driver.find_element(By.CSS_SELECTOR, 'input[name=city]').send_keys(term)
    def input_country(self, term): 
        self._driver.find_element(By.CSS_SELECTOR, 'input[name=country').send_keys(term)
    def input_mail(self, term): 
        self._driver.find_element(By.CSS_SELECTOR, 'input[name=e-mail]').send_keys(term)
    def input_phone(self, term): 
        self._driver.find_element(By.CSS_SELECTOR, 'input[name=phone]').send_keys(term)
    def input_job(self, term): 
        self._driver.find_element(By.CSS_SELECTOR, 'input[name=job-position]').send_keys(term)
    def input_company(self, term): 
        self._driver.find_element(By.CSS_SELECTOR, 'input[name=company]').send_keys(term)
        self._driver.find_element(
            By.CSS_SELECTOR, 'button.btn.btn-outline-primary.mt-3').click()