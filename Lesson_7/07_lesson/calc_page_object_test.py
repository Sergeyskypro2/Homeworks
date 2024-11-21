from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from Calc_page.MainPage import MainPage

def test_calc():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    main_page = MainPage(browser)
    main_page.time("45")
    main_page.count()
    to_be = main_page.result()

    assert to_be == 15
    browser.quit()